<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 09 Exercise</span> — <span dir="ltr">UPI Capability/Contract Review</span>

- <span dir="ltr">Timebox: 8 minutes after reading the case</span>
- <span dir="ltr">Input:</span> [<span dir="ltr">UPI Case File</span>](../case-studies/week-01-upi-fa.md)
- <span dir="ltr">Output: Fact/Inference table</span> + <span dir="ltr">Traceability chain</span> + <span dir="ltr">ADR-lite</span>

## <span dir="ltr">1. Evidence discipline</span>

از پرونده استخراج کن:

| <span dir="ltr">Statement</span> | <span dir="ltr">Label: FACT/INFERENCE/UNKNOWN</span> | <span dir="ltr">Source or reason</span> |
|---|---|---|
| پنج <span dir="ltr">Fact</span> |  |  |
| سه <span dir="ltr">Inference</span> |  |  |
| سه <span dir="ltr">Unknown</span> |  |  |

## <span dir="ltr">2. Traceability</span>

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


برای این پنج مورد <span dir="ltr">Authority</span> بنویس:

- <span dir="ltr">Payer account balance</span>
- <span dir="ltr">Participant routing</span>
- <span dir="ltr">App experience</span>
- <span dir="ltr">Transaction status</span>
- <span dir="ltr">Complaint resolution</span>

## <span dir="ltr">3. Failure loop</span>

حلقهٔ <span dir="ltr">`timeout → status check → load → more timeout`</span> را در چهار گام و با یک <span dir="ltr">Control</span> پیشنهادی برای هر گام بنویس. <span dir="ltr">Control</span>ها <span dir="ltr">Hypothesis</span> هستند؛ آن‌ها را <span dir="ltr">Fact</span> جاری <span dir="ltr">UPI</span> معرفی نکن.

## <span dir="ltr">4. ADR-lite</span>

**<span dir="ltr">Question:</span>** آیا <span dir="ltr">Core Banking Lab</span> باید یک <span dir="ltr">UPI-like central hub</span> بسازد؟


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


## <span dir="ltr">Acceptance criteria</span>

- <span dir="ltr">App</span>، <span dir="ltr">Network</span> و <span dir="ltr">Bank core</span> یکی فرض نشوند.
- <span dir="ltr">NPCI</span> مالک ماندهٔ حساب معرفی نشود.
- دست‌کم یک <span dir="ltr">Detail</span> فنی <span dir="ltr">`UNKNOWN`</span> باقی بماند.
- <span dir="ltr">Outage</span> به درس <span dir="ltr">Rate limit/Retry</span> و <span dir="ltr">Ownership</span> متصل شود.
- تصمیم <span dir="ltr">ADR</span> از <span dir="ltr">Scale</span> و <span dir="ltr">Context</span> پروژهٔ خودمان دفاع شود، نه از محبوبیت <span dir="ltr">UPI.</span>


</div>
