package bilt.part1;

import java.sql.SQLException;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * Practice stand-in for the interview JDBC repository.
 * Same unique(transaction_id) rule as H2: duplicates throw.
 *
 * Interview SQL:
 *   SELECT SUM(points) AS total_points FROM card_transaction WHERE user_id = ? GROUP BY user_id
 */
public class PointRepository {
    private final Map<String, CardTransaction> byTxnId = new LinkedHashMap<>();

    public int[] insertCardTransactions(Collection<CardTransaction> transactions) throws SQLException {
        int[] counts = new int[transactions.size()];
        int i = 0;
        for (CardTransaction tx : transactions) {
            if (byTxnId.containsKey(tx.getTransactionId())) {
                throw new SQLException("Unique index violation on transaction_id: " + tx.getTransactionId());
            }
            byTxnId.put(tx.getTransactionId(), tx);
            counts[i++] = 1;
        }
        return counts;
    }

    public Optional<Long> getTotalPointsEarned(long userId) {
        boolean seen = false;
        long total = 0;
        for (CardTransaction tx : byTxnId.values()) {
            if (tx.getUserId() == userId) {
                seen = true;
                total += tx.getPointValue();
            }
        }
        return seen ? Optional.of(total) : Optional.empty();
    }

    public List<CardTransaction> findAll() {
        return List.copyOf(byTxnId.values());
    }
}
