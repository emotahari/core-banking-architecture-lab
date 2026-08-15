# Day 09 Exercise — UPI Capability/Contract Review

- Timebox: 8 minutes after reading the case
- Input: [UPI Case File](../case-studies/week-01-upi-fa.md)
- Output: Fact/Inference table + Traceability chain + ADR-lite

## 1. Evidence discipline

از پرونده استخراج کن:

| Statement | Label: FACT/INFERENCE/UNKNOWN | Source or reason |
|---|---|---|
| پنج Fact |  |  |
| سه Inference |  |  |
| سه Unknown |  |  |

## 2. Traceability

زنجیرهٔ زیر را کامل کن:

```text
Instant interoperable payment capability
→ domains/roles
→ context hypotheses
→ Push Payment use case
→ command/result/events
```

برای این پنج مورد Authority بنویس:

- Payer account balance
- Participant routing
- App experience
- Transaction status
- Complaint resolution

## 3. Failure loop

حلقهٔ `timeout → status check → load → more timeout` را در چهار گام و با یک Control پیشنهادی برای هر گام بنویس. Controlها Hypothesis هستند؛ آن‌ها را Fact جاری UPI معرفی نکن.

## 4. ADR-lite

**Question:** آیا Core Banking Lab باید یک UPI-like central hub بسازد؟

```text
Context:
Forces:
Option A — central hub:
Option B — domain-owned flows/contracts:
Decision for the current lab:
Consequences:
Revisit trigger:
```

## Acceptance criteria

- App، Network و Bank core یکی فرض نشوند.
- NPCI مالک ماندهٔ حساب معرفی نشود.
- دست‌کم یک Detail فنی `UNKNOWN` باقی بماند.
- Outage به درس Rate limit/Retry و Ownership متصل شود.
- تصمیم ADR از Scale و Context پروژهٔ خودمان دفاع شود، نه از محبوبیت UPI.

