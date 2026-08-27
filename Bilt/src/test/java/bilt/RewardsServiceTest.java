package bilt;

import java.util.List;
import java.util.Map;
import java.util.Objects;

import bilt.RewardsService.Result;
import bilt.RewardsService.Transaction;

/**
 * No Maven/JUnit required. From the Bilt folder:
 *
 *   ./run-tests.sh
 */
public class RewardsServiceTest {

    private static int passed = 0;
    private static int failed = 0;

    public static void main(String[] args) {
        RewardsService service = new RewardsService();
        run("calculatesTriplePointsForRestaurants", () -> calculatesTriplePointsForRestaurants(service));
        run("returnsUnknownForNullBlankOrWhitespaceMerchantCode",
                () -> returnsUnknownForNullBlankOrWhitespaceMerchantCode(service));
        run("aggregatesPointsByUtcCalendarDate", () -> aggregatesPointsByUtcCalendarDate(service));
        run("handlesEmptyInput", () -> handlesEmptyInput(service));
        run("keepsMerchantCodesInInputOrder", () -> keepsMerchantCodesInInputOrder(service));
        run("treatsBlankCategoryAsOneTimesPoints", () -> treatsBlankCategoryAsOneTimesPoints(service));
        run("matchesRestaurantInAllCaps", () -> matchesRestaurantInAllCaps(service));
        run("normalizesTabOnlyMerchantToUnknown", () -> normalizesTabOnlyMerchantToUnknown(service));
        run("mergesSeveralTxsOnSameUtcDay", () -> mergesSeveralTxsOnSameUtcDay(service));
        run("appliesRestaurantMultiplierOnUtcDay", () -> appliesRestaurantMultiplierOnUtcDay(service));
        run("treatsZAndPlusZeroOffsetAsSameInstant", () -> treatsZAndPlusZeroOffsetAsSameInstant(service));
        run("handlesZeroAmount", () -> handlesZeroAmount(service));

        run("uniqueMerchantsNormalizesAndKeepsFirst", () -> uniqueMerchantsNormalizesAndKeepsFirst(service));
        run("uniqueMerchantsTreatsTrimmedDupesAsOne", () -> uniqueMerchantsTreatsTrimmedDupesAsOne(service));
        run("capsEachUtcDayIndependently", () -> capsEachUtcDayIndependently(service));
        run("capDoesNotChangeDaysUnderTheLimit", () -> capDoesNotChangeDaysUnderTheLimit(service));
        run("subtractsRefundsUsingSameRules", () -> subtractsRefundsUsingSameRules(service));
        run("refundCannotDriveADayNegative", () -> refundCannotDriveADayNegative(service));
        run("restaurantRefundSubtractsTriplePoints", () -> restaurantRefundSubtractsTriplePoints(service));

        System.out.println();
        System.out.println(passed + " passed, " + failed + " failed");
        if (failed > 0) {
            System.exit(1);
        }
    }

    static void calculatesTriplePointsForRestaurants(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(10, "Restaurant", "CHIPOTLE", "2024-01-15T12:00:00Z"),
                new Transaction(10, "restaurant", "SWEETGREEN", "2024-01-15T12:00:00Z"),
                new Transaction(10, " Restaurant ", "SHAKE_SHACK", "2024-01-15T12:00:00Z"),
                new Transaction(10, "Grocery", "WHOLE_FOODS", "2024-01-15T12:00:00Z"),
                new Transaction(10, null, "UBER", "2024-01-15T12:00:00Z"));

        Result result = service.processRewards(txs);

        // 3 restaurant txs * 10 * 3, plus grocery 10, plus null-category 10
        assertEquals(110, result.dailyPoints.get("2024-01-15"));
        assertEquals(Map.of("2024-01-15", 110), result.dailyPoints);
    }

    static void returnsUnknownForNullBlankOrWhitespaceMerchantCode(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(5, "Grocery", null, "2024-01-15T12:00:00Z"),
                new Transaction(5, "Grocery", "", "2024-01-15T12:00:00Z"),
                new Transaction(5, "Grocery", "   ", "2024-01-15T12:00:00Z"),
                new Transaction(5, "Grocery", "  CHIPOTLE  ", "2024-01-15T12:00:00Z"));

        Result result = service.processRewards(txs);

        assertEquals(List.of("UNKNOWN", "UNKNOWN", "UNKNOWN", "CHIPOTLE"),
                result.normalizedMerchantCodes);
    }

    static void aggregatesPointsByUtcCalendarDate(RewardsService service) {
        List<Transaction> txs = List.of(
                // 23:30 EST = 04:30 UTC next day
                new Transaction(10, "Grocery", "A", "2024-01-15T23:30:00-05:00"),
                // 00:30 IST = 19:00 UTC previous day
                new Transaction(7, "Grocery", "B", "2024-01-16T00:30:00+05:00"),
                new Transaction(3, "Grocery", "C", "2024-01-16T00:00:00Z"));

        Result result = service.processRewards(txs);

        assertEquals(List.of("A", "B", "C"), result.normalizedMerchantCodes);
        assertEquals(7, result.dailyPoints.get("2024-01-15"));
        assertEquals(13, result.dailyPoints.get("2024-01-16"));
        assertEquals(2, result.dailyPoints.size());
    }

    static void handlesEmptyInput(RewardsService service) {
        Result result = service.processRewards(List.of());
        assertEquals(List.of(), result.normalizedMerchantCodes);
        assertEquals(Map.of(), result.dailyPoints);
    }

    static void keepsMerchantCodesInInputOrder(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(1, "Grocery", "  B  ", "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", null, "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", "A", "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", "   ", "2024-01-15T12:00:00Z"));

        Result result = service.processRewards(txs);

        assertEquals(List.of("B", "UNKNOWN", "A", "UNKNOWN"), result.normalizedMerchantCodes);
    }

    static void treatsBlankCategoryAsOneTimesPoints(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(10, "", "A", "2024-01-15T12:00:00Z"),
                new Transaction(10, "   ", "B", "2024-01-15T12:00:00Z"));

        Result result = service.processRewards(txs);
        assertEquals(20, result.dailyPoints.get("2024-01-15"));
    }

    static void matchesRestaurantInAllCaps(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(10, "RESTAURANT", "A", "2024-01-15T12:00:00Z"));

        Result result = service.processRewards(txs);
        assertEquals(30, result.dailyPoints.get("2024-01-15"));
    }

    static void normalizesTabOnlyMerchantToUnknown(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(1, "Grocery", "\t", "2024-01-15T12:00:00Z"));

        Result result = service.processRewards(txs);
        assertEquals(List.of("UNKNOWN"), result.normalizedMerchantCodes);
    }

    static void mergesSeveralTxsOnSameUtcDay(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(2, "Grocery", "A", "2024-01-15T00:00:00Z"),
                new Transaction(3, "Grocery", "B", "2024-01-15T12:00:00Z"),
                new Transaction(5, "Grocery", "C", "2024-01-15T23:59:59Z"));

        Result result = service.processRewards(txs);
        assertEquals(Map.of("2024-01-15", 10), result.dailyPoints);
    }

    static void appliesRestaurantMultiplierOnUtcDay(RewardsService service) {
        // Local date is Jan 15 in EST, UTC date is Jan 16. Restaurant → 3×10 = 30 on 2024-01-16.
        List<Transaction> txs = List.of(
                new Transaction(10, "Restaurant", "CHIPOTLE", "2024-01-15T23:30:00-05:00"));

        Result result = service.processRewards(txs);
        assertEquals(List.of("CHIPOTLE"), result.normalizedMerchantCodes);
        assertEquals(Map.of("2024-01-16", 30), result.dailyPoints);
    }

    static void treatsZAndPlusZeroOffsetAsSameInstant(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(4, "Grocery", "A", "2024-01-15T12:00:00Z"),
                new Transaction(6, "Grocery", "B", "2024-01-15T12:00:00+00:00"));

        Result result = service.processRewards(txs);
        assertEquals(Map.of("2024-01-15", 10), result.dailyPoints);
    }

    static void handlesZeroAmount(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(0, "Restaurant", "A", "2024-01-15T12:00:00Z"));

        Result result = service.processRewards(txs);
        assertEquals(0, result.dailyPoints.get("2024-01-15"));
        assertEquals(List.of("A"), result.normalizedMerchantCodes);
    }

    static void uniqueMerchantsNormalizesAndKeepsFirst(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(1, "Grocery", null, "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", "  B  ", "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", "", "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", "A", "2024-01-15T12:00:00Z"));

        assertEquals(List.of("UNKNOWN", "B", "A"), service.uniqueNormalizedMerchants(txs));
    }

    static void uniqueMerchantsTreatsTrimmedDupesAsOne(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(1, "Grocery", "  CHIPOTLE  ", "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", "CHIPOTLE", "2024-01-15T12:00:00Z"),
                new Transaction(1, "Grocery", "SWEETGREEN", "2024-01-15T12:00:00Z"));

        assertEquals(List.of("CHIPOTLE", "SWEETGREEN"), service.uniqueNormalizedMerchants(txs));
    }

    static void capsEachUtcDayIndependently(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(10, "Grocery", "A", "2024-01-15T12:00:00Z"),
                new Transaction(3, "Grocery", "B", "2024-01-16T12:00:00Z"));

        Result result = service.processRewardsWithDailyCap(txs, 6);
        assertEquals(6, result.dailyPoints.get("2024-01-15"));
        assertEquals(3, result.dailyPoints.get("2024-01-16"));
    }

    static void capDoesNotChangeDaysUnderTheLimit(RewardsService service) {
        List<Transaction> txs = List.of(
                new Transaction(3, "Grocery", "A", "2024-01-15T12:00:00Z"),
                new Transaction(20, "Grocery", "B", "2024-01-16T12:00:00Z"));

        Result result = service.processRewardsWithDailyCap(txs, 10);
        assertEquals(3, result.dailyPoints.get("2024-01-15"));
        assertEquals(10, result.dailyPoints.get("2024-01-16"));
    }

    static void subtractsRefundsUsingSameRules(RewardsService service) {
        List<Transaction> charges = List.of(
                new Transaction(10, "Grocery", "A", "2024-01-15T12:00:00Z"));
        List<Transaction> refunds = List.of(
                new Transaction(4, "Grocery", "A", "2024-01-15T18:00:00Z"));

        Map<String, Integer> net = service.netDailyPoints(charges, refunds);
        assertEquals(6, net.get("2024-01-15"));
    }

    static void refundCannotDriveADayNegative(RewardsService service) {
        List<Transaction> charges = List.of(
                new Transaction(5, "Grocery", "A", "2024-01-15T12:00:00Z"));
        List<Transaction> refunds = List.of(
                new Transaction(9, "Grocery", "A", "2024-01-15T18:00:00Z"));

        Map<String, Integer> net = service.netDailyPoints(charges, refunds);
        int day = net.getOrDefault("2024-01-15", 0);
        if (day < 0) {
            throw new AssertionError("expected day >= 0 but was <" + day + ">");
        }
        assertEquals(0, day);
    }

    static void restaurantRefundSubtractsTriplePoints(RewardsService service) {
        List<Transaction> charges = List.of(
                new Transaction(10, "Restaurant", "A", "2024-01-15T12:00:00Z"));
        List<Transaction> refunds = List.of(
                new Transaction(10, "Restaurant", "A", "2024-01-15T18:00:00Z"));

        Map<String, Integer> net = service.netDailyPoints(charges, refunds);
        assertEquals(0, net.getOrDefault("2024-01-15", 0));
    }

    private static void run(String name, Runnable test) {
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
}
