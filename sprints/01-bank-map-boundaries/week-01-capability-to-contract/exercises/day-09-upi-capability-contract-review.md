<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 09 Exercise</bdi> — <bdi dir="ltr">UPI Capability/Contract Review</bdi>

- <bdi dir="ltr">Timebox: 8 minutes after reading the case</bdi>
- <bdi dir="ltr">Input:</bdi> [<bdi dir="ltr">UPI Case File</bdi>](../case-studies/week-01-upi-fa.md)
- <bdi dir="ltr">Output: Fact/Inference table</bdi> + <bdi dir="ltr">Traceability chain</bdi> + <bdi dir="ltr">ADR-lite</bdi>

## <bdi dir="ltr">1. Evidence discipline</bdi>

از پرونده استخراج کن:

| <bdi dir="ltr">Statement</bdi> | <bdi dir="ltr">Label: FACT/INFERENCE/UNKNOWN</bdi> | <bdi dir="ltr">Source or reason</bdi> |
|---|---|---|
| پنج <bdi dir="ltr">Fact</bdi> |  |  |
| سه <bdi dir="ltr">Inference</bdi> |  |  |
| سه <bdi dir="ltr">Unknown</bdi> |  |  |

## <bdi dir="ltr">2. Traceability</bdi>

زنجیرهٔ زیر را کامل کن:


</div>

<div dir="ltr" align="left">

```text
Instant interoperable payment capability
→ domains/roles
→ context hypotheses
→ Push Payment use case
→ command/result/events
```

</div>

<div dir="rtl" align="right">


برای این پنج مورد <bdi dir="ltr">Authority</bdi> بنویس:

- <bdi dir="ltr">Payer account balance</bdi>
- <bdi dir="ltr">Participant routing</bdi>
- <bdi dir="ltr">App experience</bdi>
- <bdi dir="ltr">Transaction status</bdi>
- <bdi dir="ltr">Complaint resolution</bdi>

## <bdi dir="ltr">3. Failure loop</bdi>

حلقهٔ <bdi dir="ltr">`timeout → status check → load → more timeout`</bdi> را در چهار گام و با یک <bdi dir="ltr">Control</bdi> پیشنهادی برای هر گام بنویس. <bdi dir="ltr">Control</bdi>ها <bdi dir="ltr">Hypothesis</bdi> هستند؛ آن‌ها را <bdi dir="ltr">Fact</bdi> جاری <bdi dir="ltr">UPI</bdi> معرفی نکن.

## <bdi dir="ltr">4. ADR-lite</bdi>

**<bdi dir="ltr">Question:</bdi>** آیا <bdi dir="ltr">Core Banking Lab</bdi> باید یک <bdi dir="ltr">UPI-like central hub</bdi> بسازد؟


</div>

<div dir="ltr" align="left">

```text
Context:
Forces:
Option A — central hub:
Option B — domain-owned flows/contracts:
Decision for the current lab:
Consequences:
Revisit trigger:
```

</div>

<div dir="rtl" align="right">


## <bdi dir="ltr">Acceptance criteria</bdi>

- <bdi dir="ltr">App</bdi>، <bdi dir="ltr">Network</bdi> و <bdi dir="ltr">Bank core</bdi> یکی فرض نشوند.
- <bdi dir="ltr">NPCI</bdi> مالک ماندهٔ حساب معرفی نشود.
- دست‌کم یک <bdi dir="ltr">Detail</bdi> فنی <bdi dir="ltr">`UNKNOWN`</bdi> باقی بماند.
- <bdi dir="ltr">Outage</bdi> به درس <bdi dir="ltr">Rate limit/Retry</bdi> و <bdi dir="ltr">Ownership</bdi> متصل شود.
- تصمیم <bdi dir="ltr">ADR</bdi> از <bdi dir="ltr">Scale</bdi> و <bdi dir="ltr">Context</bdi> پروژهٔ خودمان دفاع شود، نه از محبوبیت <bdi dir="ltr">UPI.</bdi>


</div>
