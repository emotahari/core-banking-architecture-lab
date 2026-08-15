<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 04 Exercise</bdi> — <bdi dir="ltr">Coupling Review</bdi>

- <bdi dir="ltr">Timebox: 23 minutes</bdi>
- <bdi dir="ltr">Output:</bdi> [<bdi dir="ltr">Coupling Review Template</bdi>](../artifacts/coupling-review-template.md)
- <bdi dir="ltr">Goal:</bdi> نقد <bdi dir="ltr">Evidence-based</bdi>، نه استفادهٔ شعاری از <bdi dir="ltr">SOLID</bdi>

## طراحی مورد نقد


</div>

<div dir="ltr" align="left">

```text
LoanDisbursementOrchestrator.disburse(loanId, depositNo)
  1. SELECT * FROM LOAN WHERE ID = ?
  2. UPDATE LOAN SET STATUS = 'DISBURSED'
  3. SELECT BALANCE FROM DEPOSIT WHERE NUMBER = ?
  4. UPDATE DEPOSIT SET BALANCE = BALANCE + loan.amount
  5. INSERT two rows into ACCOUNTING.DOCUMENT_LINE
  6. call SMS gateway
  7. return documentNo to channel
```

</div>

<div dir="rtl" align="right">


هر شش <bdi dir="ltr">Component</bdi> به یک دیتابیس و مدل مشترک دسترسی دارند. <bdi dir="ltr">Channel</bdi> می‌داند <bdi dir="ltr">Step 3</bdi> تا 6 به همین ترتیب اجرا می‌شوند.

## بخش A — <bdi dir="ltr">Smell</bdi> و <bdi dir="ltr">Coupling map</bdi>

حداقل هشت مورد پیدا کن. برای هر مورد بنویس:

| <bdi dir="ltr">Location/step</bdi> | <bdi dir="ltr">Coupling type</bdi> | <bdi dir="ltr">Hidden knowledge</bdi> | <bdi dir="ltr">Concrete change/failure risk</bdi> |
|---|---|---|---|
|  |  |  |  |

از این نوع‌ها استفاده کن: <bdi dir="ltr">Structural</bdi>، <bdi dir="ltr">Data</bdi>، <bdi dir="ltr">Behavioral</bdi>، <bdi dir="ltr">Temporal</bdi>، <bdi dir="ltr">Change</bdi>، <bdi dir="ltr">Operational.</bdi>

## بخش B — <bdi dir="ltr">Cohesion</bdi> و <bdi dir="ltr">Authority</bdi>

برای <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Accounting</bdi>، <bdi dir="ltr">Notification</bdi> و <bdi dir="ltr">Channel</bdi> یک جملهٔ مسئولیت و <bdi dir="ltr">Fact</bdi>های تحت <bdi dir="ltr">Authority</bdi> بنویس. سپس مشخص کن <bdi dir="ltr">Orchestrator</bdi> کدام <bdi dir="ltr">Authority</bdi>ها را تصاحب کرده است.

## بخش C — <bdi dir="ltr">Encapsulation vs Information Hiding</bdi>

دو مثال جدا بده:

1. <bdi dir="ltr">Invariant</bdi>ی که <bdi dir="ltr">Encapsulation</bdi> آن شکسته شده است.
2. تصمیم داخلی‌ای که باید <bdi dir="ltr">Information Hidden</bdi> باشد ولی نشت کرده است.

## بخش D — <bdi dir="ltr">Redesign</bdi>

راه‌حل را بدون انتخاب <bdi dir="ltr">Transport</bdi> بازنویسی کن:


</div>

<div dir="ltr" align="left">

```text
Owner → Intent/Contract → Owner → Fact/Result
```

</div>

<div dir="rtl" align="right">


حداقل یک <bdi dir="ltr">Failure</bdi> را توضیح بده: <bdi dir="ltr">Deposit Credit</bdi> انجام شده ولی پاسخ به <bdi dir="ltr">Lending</bdi> گم شده است. فقط <bdi dir="ltr">Expected safety property</bdi> را بنویس؛ طراحی <bdi dir="ltr">Idempotency/Saga</bdi> به <bdi dir="ltr">Week</bdi>های بعد موکول است.

## <bdi dir="ltr">Acceptance criteria</bdi>

- حداقل پنج نوع <bdi dir="ltr">Coupling</bdi> با شاهد مشخص شود.
- <bdi dir="ltr">Redesign</bdi> به <bdi dir="ltr">CRUD</bdi> عمومی یا <bdi dir="ltr">Database share</bdi> متکی نباشد.
- مرز مدل از مرز <bdi dir="ltr">Deployment</bdi> جدا بماند.
- شماره سند باعث <bdi dir="ltr">Coupling</bdi> همگام بی‌دلیل عملیات اصلی نشود؛ <bdi dir="ltr">Trade-off</bdi> ثبت شود.
- یک <bdi dir="ltr">Debt</bdi> و یک <bdi dir="ltr">Open question</bdi> باقی بماند.


</div>
