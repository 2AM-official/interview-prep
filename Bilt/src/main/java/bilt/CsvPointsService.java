package bilt;

import java.io.BufferedReader;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Objects;

/**
 * Practice for: import CSV, award 1x/3x points, call a third-party API with retries.
 *
 * Stdin example (feature 2 only):
 *   /path/to.csv
 *   100
 *   restaurant
 * prints 300
 */
public class CsvPointsService {

    public static final int BATCH_SIZE = 5_000;
    public static final int MAX_ATTEMPTS = 3;

    public interface Database {
        void insertBatch(List<Row> rows);
    }

    public interface ThirdPartyApi {
        /** Throws ApiException on failure. */
        void postPoints(String idempotencyKey, int points) throws ApiException;
    }

    public static class Row {
        public final String merchant;
        public final String category;
        public final BigDecimal price;

        public Row(String merchant, String category, BigDecimal price) {
            this.merchant = merchant;
            this.category = category;
            this.price = price;
        }
    }

    public static class ImportStats {
        public int imported;
        public int skippedBadRows;
    }

    public static class ApiException extends Exception {
        public final int status; // 0 = network/timeout
        public final boolean retryable;

        public ApiException(int status, boolean retryable, String message) {
            super(message);
            this.status = status;
            this.retryable = retryable;
        }
    }

    /** Feature 2: standard 1x price, restaurant 3x. Use FLOOR so 10.90 → 10. */
    public static int pointsFor(BigDecimal price, boolean restaurant) {
        if (price == null || price.signum() < 0) {
            throw new IllegalArgumentException("price must be >= 0");
        }
        int base = price.setScale(0, RoundingMode.FLOOR).intValueExact();
        return restaurant ? base * 3 : base;
    }

    public static int pointsFor(String priceLine, String categoryLine) {
        BigDecimal price = new BigDecimal(priceLine.trim());
        boolean restaurant = categoryLine != null
                && "restaurant".equalsIgnoreCase(categoryLine.trim());
        return pointsFor(price, restaurant);
    }

    /**
     * Feature 1: stream CSV (up to 1e6 rows). Do not load the whole file.
     * Format: merchant,category,price   (header optional)
     * Bad rows are skipped, not fatal.
     */
    public ImportStats importCsv(Path csvPath, Database db) throws IOException {
        Objects.requireNonNull(csvPath, "csv path");
        Objects.requireNonNull(db, "database");
        if (!Files.isRegularFile(csvPath)) {
            throw new IllegalArgumentException("CSV not found: " + csvPath);
        }

        ImportStats stats = new ImportStats();
        List<Row> batch = new ArrayList<>(BATCH_SIZE);

        try (BufferedReader reader = Files.newBufferedReader(csvPath)) {
            String line;
            boolean maybeHeader = true;
            while ((line = reader.readLine()) != null) {
                if (line.isBlank()) {
                    continue;
                }
                if (maybeHeader) {
                    maybeHeader = false;
                    if (looksLikeHeader(line)) {
                        continue;
                    }
                }
                Row row = parseRow(line);
                if (row == null) {
                    stats.skippedBadRows++;
                    continue;
                }
                batch.add(row);
                if (batch.size() >= BATCH_SIZE) {
                    db.insertBatch(batch);
                    stats.imported += batch.size();
                    batch.clear();
                }
            }
        }
        if (!batch.isEmpty()) {
            db.insertBatch(batch);
            stats.imported += batch.size();
        }
        return stats;
    }

    /**
     * Feature 3: post points to a third party.
     * Retry timeouts and 5xx/429. Do not retry 4xx (except 429). Give up after MAX_ATTEMPTS.
     */
    public void submitPoints(ThirdPartyApi api, String idempotencyKey, int points)
            throws ApiException {
        ApiException last = null;
        for (int attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
            try {
                api.postPoints(idempotencyKey, points);
                return;
            } catch (ApiException e) {
                last = e;
                if (!e.retryable || attempt == MAX_ATTEMPTS) {
                    throw e;
                }
            }
        }
        throw last;
    }

    static boolean looksLikeHeader(String line) {
        String lower = line.toLowerCase(Locale.ROOT);
        return lower.contains("merchant") || lower.contains("category") || lower.contains("price");
    }

    static Row parseRow(String line) {
        String[] parts = line.split(",", -1);
        if (parts.length < 3) {
            return null;
        }
        try {
            BigDecimal price = new BigDecimal(parts[2].trim());
            if (price.signum() < 0) {
                return null;
            }
            return new Row(parts[0].trim(), parts[1].trim(), price);
        } catch (NumberFormatException e) {
            return null;
        }
    }
}
