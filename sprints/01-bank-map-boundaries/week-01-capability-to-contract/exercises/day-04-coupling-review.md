<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 04 Exercise</span> — <span dir="ltr">Coupling Review</span>

- <span dir="ltr">Timebox: 23 minutes</span>
- <span dir="ltr">Output:</span> [<span dir="ltr">Coupling Review Template</span>](../artifacts/coupling-review-template.md)
- <span dir="ltr">Goal:</span> نقد <span dir="ltr">Evidence-based</span>، نه استفادهٔ شعاری از <span dir="ltr">SOLID</span>

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


هر شش <span dir="ltr">Component</span> به یک دیتابیس و مدل مشترک دسترسی دارند. <span dir="ltr">Channel</span> می‌داند <span dir="ltr">Step 3</span> تا 6 به همین ترتیب اجرا می‌شوند.

## بخش A — <span dir="ltr">Smell</span> و <span dir="ltr">Coupling map</span>

حداقل هشت مورد پیدا کن. برای هر مورد بنویس:

| <span dir="ltr">Location/step</span> | <span dir="ltr">Coupling type</span> | <span dir="ltr">Hidden knowledge</span> | <span dir="ltr">Concrete change/failure risk</span> |
|---|---|---|---|
|  |  |  |  |

از این نوع‌ها استفاده کن: <span dir="ltr">Structural</span>، <span dir="ltr">Data</span>، <span dir="ltr">Behavioral</span>، <span dir="ltr">Temporal</span>، <span dir="ltr">Change</span>، <span dir="ltr">Operational.</span>

## بخش B — <span dir="ltr">Cohesion</span> و <span dir="ltr">Authority</span>

برای <span dir="ltr">Lending</span>، <span dir="ltr">Deposits</span>، <span dir="ltr">Accounting</span>، <span dir="ltr">Notification</span> و <span dir="ltr">Channel</span> یک جملهٔ مسئولیت و <span dir="ltr">Fact</span>های تحت <span dir="ltr">Authority</span> بنویس. سپس مشخص کن <span dir="ltr">Orchestrator</span> کدام <span dir="ltr">Authority</span>ها را تصاحب کرده است.

## بخش C — <span dir="ltr">Encapsulation vs Information Hiding</span>

دو مثال جدا بده:

1. <span dir="ltr">Invariant</span>ی که <span dir="ltr">Encapsulation</span> آن شکسته شده است.
2. تصمیم داخلی‌ای که باید <span dir="ltr">Information Hidden</span> باشد ولی نشت کرده است.

## بخش D — <span dir="ltr">Redesign</span>

راه‌حل را بدون انتخاب <span dir="ltr">Transport</span> بازنویسی کن:


</div>

<div dir="ltr" align="left">

```text
Owner → Intent/Contract → Owner → Fact/Result
```

</div>

<div dir="rtl" align="right">


حداقل یک <span dir="ltr">Failure</span> را توضیح بده: <span dir="ltr">Deposit Credit</span> انجام شده ولی پاسخ به <span dir="ltr">Lending</span> گم شده است. فقط <span dir="ltr">Expected safety property</span> را بنویس؛ طراحی <span dir="ltr">Idempotency/Saga</span> به <span dir="ltr">Week</span>های بعد موکول است.

## <span dir="ltr">Acceptance criteria</span>

- حداقل پنج نوع <span dir="ltr">Coupling</span> با شاهد مشخص شود.
- <span dir="ltr">Redesign</span> به <span dir="ltr">CRUD</span> عمومی یا <span dir="ltr">Database share</span> متکی نباشد.
- مرز مدل از مرز <span dir="ltr">Deployment</span> جدا بماند.
- شماره سند باعث <span dir="ltr">Coupling</span> همگام بی‌دلیل عملیات اصلی نشود؛ <span dir="ltr">Trade-off</span> ثبت شود.
- یک <span dir="ltr">Debt</span> و یک <span dir="ltr">Open question</span> باقی بماند.


</div>
