package com.example.corebankinglab.craftsmanship.week02;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class LegacyTransferFeeCalculatorCharacterizationTest {

    private final LegacyTransferFeeCalculator calculator = new LegacyTransferFeeCalculator();

    @Test
    void internalTransferHasNoFee() {
        assertEquals(0, calculator.calculate("INTERNAL", 100_000_000, false));
    }

    @Test
    void achAppliesMinimumFee() {
        assertEquals(50_000, calculator.calculate("ACH", 100_000_000, false));
    }

    @Test
    void achUsesPercentageInsideTheBand() {
        assertEquals(200_000, calculator.calculate("ACH", 1_000_000_000, false));
    }

    @Test
    void achCapsTheFee() {
        assertEquals(250_000, calculator.calculate("ACH", 5_000_000_000L, false));
    }

    @Test
    void rtgsUsesFixedFee() {
        assertEquals(200_000, calculator.calculate("RTGS", 1_000_000_000, false));
    }

    @Test
    void preferredCustomerGetsHalfOfTheCalculatedFee() {
        assertEquals(100_000, calculator.calculate("RTGS", 1_000_000_000, true));
    }

    @Test
    void rejectsUnsupportedRail() {
        assertThrows(
                IllegalArgumentException.class,
                () -> calculator.calculate("UNKNOWN", 1_000_000, false)
        );
    }

    @Test
    void rejectsNonPositiveAmountEvenForInternalTransfer() {
        assertThrows(
                IllegalArgumentException.class,
                () -> calculator.calculate("INTERNAL", 0, false)
        );
    }
}
