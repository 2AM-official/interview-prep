package bilt;

import java.io.IOException;
import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicInteger;

import bilt.CsvPointsService.ApiException;
import bilt.CsvPointsService.Database;
import bilt.CsvPointsService.ImportStats;
import bilt.CsvPointsService.Row;
import bilt.CsvPointsService.ThirdPartyApi;

public class CsvPointsServiceTest {

    private static int passed = 0;
    private static int failed = 0;

    public static void main(String[] args) throws Exception {
        CsvPointsService svc = new CsvPointsService();
        run("exampleRestaurantIs300", () -> exampleRestaurantIs300());
        run("groceryIs1x", () -> groceryIs1x());
        run("floorsPrice", () -> floorsPrice());
        run("importsCsvInBatchesAndSkipsBadRows", () -> importsCsvInBatchesAndSkipsBadRows(svc));
        run("missingCsvIsAnError", () -> missingCsvIsAnError(svc));
        run("retriesRetryableApiThenSucceeds", () -> retriesRetryableApiThenSucceeds(svc));
        run("doesNotRetryClientError", () -> doesNotRetryClientError(svc));
        run("givesUpAfterMaxAttempts", () -> givesUpAfterMaxAttempts(svc));

        System.out.println();
        System.out.println(passed + " passed, " + failed + " failed");
        if (failed > 0) {
            System.exit(1);
        }
    }

    static void exampleRestaurantIs300() {
        assertEquals(300, CsvPointsService.pointsFor("100", "restaurant"));
    }

    static void groceryIs1x() {
        assertEquals(100, CsvPointsService.pointsFor("100", "grocery"));
        assertEquals(100, CsvPointsService.pointsFor("100", null));
    }

    static void floorsPrice() {
        assertEquals(30, CsvPointsService.pointsFor(new BigDecimal("10.90"), true));
    }

    static void importsCsvInBatchesAndSkipsBadRows(CsvPointsService svc) throws IOException {
        Path csv = Files.createTempFile("bilt-merchants", ".csv");
        Files.writeString(csv, String.join("\n",
                "merchant,category,price",
                "Chipotle,Restaurant,10.90",
                "bad-row",
                "Whole Foods,Grocery,8",
                "Nope,Grocery,-1",
                "Shake Shack,restaurant,10"));
        RecordingDb db = new RecordingDb();
        ImportStats stats = svc.importCsv(csv, db);
        assertEquals(3, stats.imported);
        assertEquals(2, stats.skippedBadRows);
        assertEquals(3, db.rows.size());
        Files.deleteIfExists(csv);
    }

    static void missingCsvIsAnError(CsvPointsService svc) {
        RecordingDb db = new RecordingDb();
        try {
            svc.importCsv(Path.of("/no/such/file.csv"), db);
            throw new AssertionError("expected IllegalArgumentException");
        } catch (IllegalArgumentException | IOException expected) {
            if (expected instanceof IOException) {
                throw new AssertionError("missing file should fail fast, not IOException after open");
            }
        }
    }

    static void retriesRetryableApiThenSucceeds(CsvPointsService svc) throws ApiException {
        FlakyApi api = new FlakyApi(2, 503, true);
        svc.submitPoints(api, "txn-1", 300);
        assertEquals(3, api.calls.get());
    }

    static void doesNotRetryClientError(CsvPointsService svc) {
        FlakyApi api = new FlakyApi(5, 400, false);
        try {
            svc.submitPoints(api, "txn-2", 100);
            throw new AssertionError("expected ApiException");
        } catch (ApiException e) {
            assertEquals(400, e.status);
            assertEquals(1, api.calls.get());
        }
    }

    static void givesUpAfterMaxAttempts(CsvPointsService svc) {
        FlakyApi api = new FlakyApi(10, 0, true);
        try {
            svc.submitPoints(api, "txn-3", 100);
            throw new AssertionError("expected ApiException");
        } catch (ApiException e) {
            assertEquals(true, e.retryable);
            assertEquals(CsvPointsService.MAX_ATTEMPTS, api.calls.get());
        }
    }

    private static void run(String name, ThrowingRunnable test) {
        try {
            test.run();
            passed++;
            System.out.println("PASS  " + name);
        } catch (Throwable t) {
            failed++;
            System.out.println("FAIL  " + name);
            t.printStackTrace(System.out);
            System.out.println();
        }
    }

    private static void assertEquals(Object expected, Object actual) {
        if (!Objects.equals(expected, actual)) {
            throw new AssertionError("expected <" + expected + "> but was <" + actual + ">");
        }
    }

    interface ThrowingRunnable {
        void run() throws Exception;
    }

    static class RecordingDb implements Database {
        final List<Row> rows = new ArrayList<>();

        @Override
        public void insertBatch(List<Row> batch) {
            rows.addAll(batch);
        }
    }

    static class FlakyApi implements ThirdPartyApi {
        final int failTimes;
        final int status;
        final boolean retryable;
        final AtomicInteger calls = new AtomicInteger();

        FlakyApi(int failTimes, int status, boolean retryable) {
            this.failTimes = failTimes;
            this.status = status;
            this.retryable = retryable;
        }

        @Override
        public void postPoints(String idempotencyKey, int points) throws ApiException {
            int n = calls.incrementAndGet();
            if (n <= failTimes) {
                throw new ApiException(status, retryable, "fail " + n);
            }
        }
    }
}
