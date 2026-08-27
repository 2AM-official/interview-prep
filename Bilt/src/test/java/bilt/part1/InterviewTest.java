package bilt.part1;

import java.math.BigDecimal;
import java.util.Arrays;
import java.util.Objects;

/**
 * Local copy of the Codespaces {@code InterviewTest}.
 *
 * Real CSV assertions:
 *   user 6  → 1968L
 *   user 1  → 903L
 *   user 39 → 268L
 *
 * This practice CSV uses smaller known totals. Run {@code ./run-part1-tests.sh}.
 */
public class InterviewTest {

    private static int passed = 0;
    private static int failed = 0;

    public static void main(String[] args) throws Exception {
        run("transactions_inserted_to_db", InterviewTest::transactions_inserted_to_db);
        run("dining_multipliers_applied", InterviewTest::dining_multipliers_applied);
        run("point_balance_query_returns_user_total", InterviewTest::point_balance_query_returns_user_total);
        run("calculate_points_persists_transactions", InterviewTest::calculate_points_persists_transactions);

        System.out.println();
        System.out.println(passed + " passed, " + failed + " failed");
        if (failed > 0) {
            System.exit(1);
        }
    }

    static void transactions_inserted_to_db() throws Exception {
        PointService pointService = new PointService();
        pointService.calculatePoints();
        // practice: 100 + 150 + first duplicate 1.55*3 = 253
        assertEquals(253L, pointService.getTotalPointsEarned(6));
    }

    static void dining_multipliers_applied() throws Exception {
        PointService pointService = new PointService();
        pointService.calculatePoints();
        // practice: user 1 = 10*3 + 20 + 15*3 = 95; user 39 = 7*3 = 21
        assertEquals(95L, pointService.getTotalPointsEarned(1));
        assertEquals(21L, pointService.getTotalPointsEarned(39));
    }

    static void point_balance_query_returns_user_total() throws Exception {
        PointService pointService = new PointService();
        PointRepository pointRepository = pointService.getPointRepository();

        CardTransaction firstTransaction = new CardTransaction();
        firstTransaction.setUserId(987654);
        firstTransaction.setTransactionId("interview-test-transaction-1");
        firstTransaction.setTransactionAmount(BigDecimal.TEN);
        firstTransaction.setPointValue(10);
        firstTransaction.setMerchantCategoryCode(1234);

        CardTransaction secondTransaction = new CardTransaction();
        secondTransaction.setUserId(987654);
        secondTransaction.setTransactionId("interview-test-transaction-2");
        secondTransaction.setTransactionAmount(BigDecimal.ONE);
        secondTransaction.setPointValue(7);
        secondTransaction.setMerchantCategoryCode(5678);

        pointRepository.insertCardTransactions(Arrays.asList(firstTransaction, secondTransaction));
        assertEquals(17L, pointService.getTotalPointsEarned(987654));
    }

    static void calculate_points_persists_transactions() throws Exception {
        PointService pointService = new PointService();
        pointService.calculatePoints();
        if (pointService.getPointRepository().findAll().isEmpty()) {
            throw new AssertionError("expected COUNT(*) from card_transaction > 0");
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
}
