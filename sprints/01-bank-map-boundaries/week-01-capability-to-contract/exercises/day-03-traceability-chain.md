# Day 03 Exercise — Two Traceability Chains

- Timebox: 21 minutes
- Output: دو نسخه از [Traceability Chain Template](../artifacts/traceability-chain-template.md)
- Scenarios: مسدودی قضایی سپرده و اعطای تسهیلات

## Chain A — مسدودی قضایی

فرض کن حکمی معتبر برای Hold مبلغ ۵۰٬۰۰۰٬۰۰۰ ریال روی یک سپرده دریافت شده است. مشتری ممکن است موجودی دفتری ۸۰٬۰۰۰٬۰۰۰ ریال داشته باشد، اما فقط مبلغ غیرمسدود قابل برداشت است.

زنجیره را از این عناصر عبور بده:

```text
Trigger/Outcome
→ Capability
→ Domain/Subdomain
→ Bounded Context hypothesis
→ Module/Service candidate
→ Use Case
→ Command/Query
→ Result/Event
```

برای هر عنصر Owner، Evidence و یک Open question بنویس.

## Chain B — اعطا و واریز

قرارداد مرابحه مصوب است. مبلغ ۱۰۰٬۰۰۰٬۰۰۰ ریال باید دقیقاً یک‌بار به سپردهٔ جاری مشتری واریز شود و Fact مالی آن قابل ثبت باشد.

حداقل این Ownershipها را جدا کن:

- وضعیت و تصمیم اعطا
- ماندهٔ اصل تسهیلات
- ماندهٔ قابل برداشت سپرده
- نتیجهٔ Credit
- Journal مالی

هنوز REST، Kafka، Saga یا دیتابیس را انتخاب نکن.

## Reverse trace

برای این دو Contract candidate مسیر برگشت تا Capability را بنویس:

1. `PlaceFundsHold`
2. `DepositCredited`

اگر Contract به دو Capability نامرتبط برمی‌گردد، Scope یا نام آن را بازبینی کن.

## Consistency checks

- Command به زمان امر و Event به Fact گذشته نام‌گذاری شده است.
- هیچ Contextی جدول Context دیگر را Update نمی‌کند.
- Service Candidate به‌عنوان Hypothesis علامت خورده، نه تصمیم Deployment.
- API/Event حداقل دادهٔ معنایی لازم را دارد، نه Entity dump.
- Unknownهای Transport و Failure پنهان نشده‌اند.

## Acceptance criteria

- هر دو Chain کامل و قابل Reverse tracing باشند.
- هر Fact دقیقاً یک Authority اولیه داشته باشد.
- تفاوت Legal Order با Operational Hold روشن باشد.
- Accounting مالک available balance معرفی نشود.
- حداقل چهار Unknown واقعی ثبت شود.

