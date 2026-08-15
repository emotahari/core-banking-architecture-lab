package com.example.corebankinglab.craftsmanship.week02;

/**
 * Deliberately awkward, test-scoped starter code for the Week 02 refactoring lab.
 *
 * <p>The numbers are fictional educational rules, not a real bank tariff.</p>
 */
final class LegacyTransferFeeCalculator {

    long calculate(String paymentRail, long amountRials, boolean preferredCustomer) {
        if (paymentRail == null || paymentRail.isBlank()) {
            throw new IllegalArgumentException("paymentRail is required");
        }
        if (amountRials <= 0) {
            throw new IllegalArgumentException("amountRials must be positive");
        }

        long fee;
        if (paymentRail.equals("INTERNAL")) {
            fee = 0;
        } else if (paymentRail.equals("ACH")) {
            fee = amountRials * 2 / 10_000;
            if (fee < 50_000) {
                fee = 50_000;
            }
            if (fee > 250_000) {
                fee = 250_000;
            }
        } else if (paymentRail.equals("RTGS")) {
            fee = 200_000;
        } else {
            throw new IllegalArgumentException("unsupported paymentRail: " + paymentRail);
        }

        if (preferredCustomer) {
            fee = fee / 2;
        }

        return fee;
    }
}
