package bilt.part1;

import java.math.BigDecimal;

/** Matches the interview model setters used by InterviewTest / PointRepository. */
public class CardTransaction {
    private long userId;
    private String transactionId;
    private BigDecimal transactionAmount;
    private int pointValue;
    private int merchantCategoryCode;

    public long getUserId() {
        return userId;
    }

    public void setUserId(long userId) {
        this.userId = userId;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public void setTransactionId(String transactionId) {
        this.transactionId = transactionId;
    }

    public BigDecimal getTransactionAmount() {
        return transactionAmount;
    }

    public void setTransactionAmount(BigDecimal transactionAmount) {
        this.transactionAmount = transactionAmount;
    }

    public int getPointValue() {
        return pointValue;
    }

    public void setPointValue(int pointValue) {
        this.pointValue = pointValue;
    }

    public int getMerchantCategoryCode() {
        return merchantCategoryCode;
    }

    public void setMerchantCategoryCode(int merchantCategoryCode) {
        this.merchantCategoryCode = merchantCategoryCode;
    }
}
