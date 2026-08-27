package bilt;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.time.Instant;
import java.time.ZoneOffset;


/**
 * Practice copy of the common Bilt Java screen.
 *
 * Run the tests, read the failures, then fix this class. Do not change tests
 * unless you can prove one is wrong.
 */
public class RewardsService {

    public static class Transaction {
        public int amount;
        public String category;
        public String merchantCode;
        public String timestamp; // ISO-8601 with timezone

        public Transaction(int amount, String category, String merchantCode, String timestamp) {
            this.amount = amount;
            this.category = category;
            this.merchantCode = merchantCode;
            this.timestamp = timestamp;
        }
    }

    public Result processRewards(List<Transaction> transactions) {
        List<String> codes = new ArrayList<>();
        Map<String, Integer> daily = new HashMap<>();
        for (Transaction tx : transactions) {
            if (tx.merchantCode == null || tx.merchantCode.isBlank()) {
                codes.add("UNKNOWN");
            } else {
                codes.add(tx.merchantCode.trim());
            }

            int multiplier = 1;
            if (tx.category != null && "Restaurant".equalsIgnoreCase(tx.category.trim())) {
                multiplier = 3;
            }
            int points = tx.amount * multiplier;

            String day = Instant.parse(tx.timestamp)
                            .atZone(ZoneOffset.UTC)
                            .toLocalDate()
                            .toString();

            daily.merge(day, points, Integer::sum);
        }
        Result result = new Result();
        result.normalizedMerchantCodes = codes;
        result.dailyPoints = daily;
        return result;
    }

    /**
     * Unique merchant codes after the same UNKNOWN/trim rules.
     * First occurrence wins. Keep input order.
     */
    public List<String> uniqueNormalizedMerchants(List<Transaction> transactions) {
        java.util.Set<String> seen = new java.util.HashSet<>();
        List<String> out = new ArrayList<>();
        for (Transaction tx : transactions) {
            if (tx.merchantCode == null || tx.merchantCode.isBlank()) {
                continue;
            }
            String merchantCode = tx.merchantCode.trim();
            if (seen.add(merchantCode)) {
                out.add(merchantCode);
            }
        }
        return out;
    }

    /**
     * Same processRewards rules, then cap each UTC day's points at dailyCap.
     *
     * BUG: if the grand total exceeds the cap, every day is overwritten with dailyCap.
     */
    public Result processRewardsWithDailyCap(List<Transaction> transactions, int dailyCap) {
        Result result = processRewards(transactions);
        int total = 0;
        for (int pts : result.dailyPoints.values()) {
            total += pts;
        }
        if (total > dailyCap) {
            for (String day : result.dailyPoints.keySet()) {
                result.dailyPoints.put(day, dailyCap);
            }
        }
        return result;
    }

    /**
     * Charges minus refunds, same 3× / UTC rules. A day cannot go below 0.
     *
     * BUG: refunds are added, not subtracted, and negatives are allowed.
     */
    public Map<String, Integer> netDailyPoints(List<Transaction> charges, List<Transaction> refunds) {
        Result charged = processRewards(charges);
        Result refunded = processRewards(refunds);
        Map<String, Integer> net = new HashMap<>(charged.dailyPoints);
        for (Map.Entry<String, Integer> e : refunded.dailyPoints.entrySet()) {
            net.merge(e.getKey(), e.getValue(), Integer::sum);
        }
        return net;
    }
}
