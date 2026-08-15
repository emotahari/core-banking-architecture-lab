# Day 04 Exercise — Coupling Review

- Timebox: 23 minutes
- Output: [Coupling Review Template](../artifacts/coupling-review-template.md)
- Goal: نقد Evidence-based، نه استفادهٔ شعاری از SOLID

## طراحی مورد نقد

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

هر شش Component به یک دیتابیس و مدل مشترک دسترسی دارند. Channel می‌داند Step 3 تا 6 به همین ترتیب اجرا می‌شوند.

## بخش A — Smell و Coupling map

حداقل هشت مورد پیدا کن. برای هر مورد بنویس:

| Location/step | Coupling type | Hidden knowledge | Concrete change/failure risk |
|---|---|---|---|
|  |  |  |  |

از این نوع‌ها استفاده کن: Structural، Data، Behavioral، Temporal، Change، Operational.

## بخش B — Cohesion و Authority

برای Lending، Deposits، Accounting، Notification و Channel یک جملهٔ مسئولیت و Factهای تحت Authority بنویس. سپس مشخص کن Orchestrator کدام Authorityها را تصاحب کرده است.

## بخش C — Encapsulation vs Information Hiding

دو مثال جدا بده:

1. Invariantی که Encapsulation آن شکسته شده است.
2. تصمیم داخلی‌ای که باید Information Hidden باشد ولی نشت کرده است.

## بخش D — Redesign

راه‌حل را بدون انتخاب Transport بازنویسی کن:

```text
Owner → Intent/Contract → Owner → Fact/Result
```

حداقل یک Failure را توضیح بده: Deposit Credit انجام شده ولی پاسخ به Lending گم شده است. فقط Expected safety property را بنویس؛ طراحی Idempotency/Saga به Weekهای بعد موکول است.

## Acceptance criteria

- حداقل پنج نوع Coupling با شاهد مشخص شود.
- Redesign به CRUD عمومی یا Database share متکی نباشد.
- مرز مدل از مرز Deployment جدا بماند.
- شماره سند باعث Coupling همگام بی‌دلیل عملیات اصلی نشود؛ Trade-off ثبت شود.
- یک Debt و یک Open question باقی بماند.

