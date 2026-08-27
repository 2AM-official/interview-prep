package bilt.part1;

import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Interview PointService. Dining MCC 5812 → 3× floor(amount), else 1×.
 * Skip duplicate TRANSACTION_ID (unique on card_transaction.transaction_id).
 */
@ApplicationScoped
public class PointService {
    @Inject
    PointRepository pointRepository;

    public PointService() {
        this.pointRepository = new PointRepository();
    }

    PointService(PointRepository pointRepository) {
        this.pointRepository = pointRepository;
    }

    public PointRepository getPointRepository() {
        return pointRepository;
    }

    public void calculatePoints() throws Exception {
        List<CSVRecord> csvRecords;
        try {
            csvRecords = TransactionFileHelper.parseFile("/BILT_TRANSACTIONS.csv");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        Set<String> seen = new HashSet<>();
        List<CardTransaction> transactions = new ArrayList<>();
        for (CSVRecord record : csvRecords) {
            String transactionId = record.get("TRANSACTION_ID");
            if (!seen.add(transactionId)) {
                continue;
            }

            BigDecimal amount = new BigDecimal(record.get("TRAN_AMT"));
            int mcc = Integer.parseInt(record.get("MCC"));
            int base = amount.setScale(0, RoundingMode.DOWN).intValue();
            int points = (mcc == 5812) ? base * 3 : base;

            CardTransaction tx = new CardTransaction();
            tx.setUserId(Long.parseLong(record.get("USER_ID")));
            tx.setTransactionId(transactionId);
            tx.setTransactionAmount(amount);
            tx.setPointValue(points);
            tx.setMerchantCategoryCode(mcc);
            transactions.add(tx);
        }

        pointRepository.insertCardTransactions(transactions);
    }

    public long getTotalPointsEarned(long userId) throws SQLException {
        return pointRepository.getTotalPointsEarned(userId)
                .orElseThrow(NotFoundException::new);
    }
}
