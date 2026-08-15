package com.example.corebankinglab.craftsmanship.week01;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

class PrimitiveTransferRequestCharacterizationTest {

    @Test
    void validRequestPreservesEveryPrimitiveValue() {
        var request = validRequest(new BigDecimal("125000.00"));

        assertThat(request.sourceAccountId()).isEqualTo("ACC-1001");
        assertThat(request.targetAccountId()).isEqualTo("ACC-2002");
        assertThat(request.customerId()).isEqualTo("CUS-77");
        assertThat(request.originatingBranchId()).isEqualTo("BR-001");
        assertThat(request.amount()).isEqualTo(new BigDecimal("125000.00"));
        assertThat(request.currency()).isEqualTo("IRR");
    }

    @Test
    void sameSourceAndTargetAccountFails() {
        assertThatThrownBy(() -> new PrimitiveTransferRequest(
                        "ACC-1001", "ACC-1001", "CUS-77", "BR-001",
                        new BigDecimal("1"), "IRR"))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("source and target accounts must differ");
    }

    @Test
    void nullAmountFails() {
        assertThatThrownBy(() -> validRequest(null))
                .isInstanceOf(NullPointerException.class)
                .hasMessage("amount must not be null");
    }

    @Test
    void zeroAmountFails() {
        assertThatThrownBy(() -> validRequest(BigDecimal.ZERO))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("amount must be greater than zero");
    }

    @Test
    void negativeAmountFails() {
        assertThatThrownBy(() -> validRequest(new BigDecimal("-0.01")))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("amount must be greater than zero");
    }

    @Test
    void blankCurrencyFails() {
        assertThatThrownBy(() -> new PrimitiveTransferRequest(
                        "ACC-1001", "ACC-2002", "CUS-77", "BR-001",
                        new BigDecimal("1"), " "))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("currency must not be blank");
    }

    @Test
    void blankIdentifierFailsAtConstructionBoundary() {
        assertThatThrownBy(() -> new PrimitiveTransferRequest(
                        " ", "ACC-2002", "CUS-77", "BR-001",
                        new BigDecimal("1"), "IRR"))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("sourceAccountId must not be blank");
    }

    @Test
    void amountScaleIsNotSilentlyRoundedOrNormalized() {
        var request = validRequest(new BigDecimal("125000.0000"));

        assertThat(request.amount().scale()).isEqualTo(4);
        assertThat(request.amount()).isEqualTo(new BigDecimal("125000.0000"));
    }

    @Test
    void auditKeyCapturesTheCurrentObservableRepresentation() {
        var request = validRequest(new BigDecimal("125000.00"));

        assertThat(request.auditKey())
                .isEqualTo("CUS-77|BR-001|ACC-1001|ACC-2002|125000.00|IRR");
    }

    private static PrimitiveTransferRequest validRequest(BigDecimal amount) {
        return new PrimitiveTransferRequest(
                "ACC-1001",
                "ACC-2002",
                "CUS-77",
                "BR-001",
                amount,
                "IRR");
    }
}

