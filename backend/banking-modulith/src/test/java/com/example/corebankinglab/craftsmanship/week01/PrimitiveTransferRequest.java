package com.example.corebankinglab.craftsmanship.week01;

import java.math.BigDecimal;
import java.util.Objects;

/**
 * Test-scoped legacy fixture for the Week 01 refactoring kata.
 *
 * <p>The primitive design is intentional. Learners first characterize its behavior and then
 * introduce domain value objects in small, green steps. This is not a production banking
 * contract.</p>
 */
final class PrimitiveTransferRequest {

    private final String sourceAccountId;
    private final String targetAccountId;
    private final String customerId;
    private final String originatingBranchId;
    private final BigDecimal amount;
    private final String currency;

    PrimitiveTransferRequest(
            String sourceAccountId,
            String targetAccountId,
            String customerId,
            String originatingBranchId,
            BigDecimal amount,
            String currency) {
        this.sourceAccountId = requiredText(sourceAccountId, "sourceAccountId");
        this.targetAccountId = requiredText(targetAccountId, "targetAccountId");
        this.customerId = requiredText(customerId, "customerId");
        this.originatingBranchId = requiredText(originatingBranchId, "originatingBranchId");
        this.amount = Objects.requireNonNull(amount, "amount must not be null");
        this.currency = requiredText(currency, "currency");

        if (this.sourceAccountId.equals(this.targetAccountId)) {
            throw new IllegalArgumentException("source and target accounts must differ");
        }
        if (this.amount.signum() <= 0) {
            throw new IllegalArgumentException("amount must be greater than zero");
        }
    }

    String sourceAccountId() {
        return sourceAccountId;
    }

    String targetAccountId() {
        return targetAccountId;
    }

    String customerId() {
        return customerId;
    }

    String originatingBranchId() {
        return originatingBranchId;
    }

    BigDecimal amount() {
        return amount;
    }

    String currency() {
        return currency;
    }

    String auditKey() {
        return customerId + "|" + originatingBranchId + "|" + sourceAccountId + "|"
                + targetAccountId + "|" + amount.toPlainString() + "|" + currency;
    }

    private static String requiredText(String value, String field) {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException(field + " must not be blank");
        }
        return value;
    }
}

