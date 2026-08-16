<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 03 Exercise</span> — <span dir="ltr">Two Traceability Chains</span>

- <span dir="ltr">Timebox: 21 minutes</span>
- <span dir="ltr">Output:</span> دو نسخه از [<span dir="ltr">Traceability Chain Template</span>](../artifacts/traceability-chain-template.md)
- <span dir="ltr">Scenarios:</span> مسدودی قضایی سپرده و اعطای تسهیلات

## <span dir="ltr">Chain A</span> — مسدودی قضایی

فرض کن حکمی معتبر برای <span dir="ltr">Hold</span> مبلغ ۵۰٬۰۰۰٬۰۰۰ ریال روی یک سپرده دریافت شده است. مشتری ممکن است موجودی دفتری ۸۰٬۰۰۰٬۰۰۰ ریال داشته باشد، اما فقط مبلغ غیرمسدود قابل برداشت است.

زنجیره را از این عناصر عبور بده:


</div>

<div dir="ltr" align="left">

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

</div>

<div dir="rtl" align="right">


برای هر عنصر <span dir="ltr">Owner</span>، <span dir="ltr">Evidence</span> و یک <span dir="ltr">Open question</span> بنویس.

## <span dir="ltr">Chain B</span> — اعطا و واریز

قرارداد مرابحه مصوب است. مبلغ ۱۰۰٬۰۰۰٬۰۰۰ ریال باید دقیقاً یک‌بار به سپردهٔ جاری مشتری واریز شود و <span dir="ltr">Fact</span> مالی آن قابل ثبت باشد.

حداقل این <span dir="ltr">Ownership</span>ها را جدا کن:

- وضعیت و تصمیم اعطا
- ماندهٔ اصل تسهیلات
- ماندهٔ قابل برداشت سپرده
- نتیجهٔ <span dir="ltr">Credit</span>
- <span dir="ltr">Journal</span> مالی

هنوز <span dir="ltr">REST</span>، <span dir="ltr">Kafka</span>، <span dir="ltr">Saga</span> یا دیتابیس را انتخاب نکن.

## <span dir="ltr">Reverse trace</span>

برای این دو <span dir="ltr">Contract candidate</span> مسیر برگشت تا <span dir="ltr">Capability</span> را بنویس:

1. <span dir="ltr">`PlaceFundsHold`</span>
2. <span dir="ltr">`DepositCredited`</span>

اگر <span dir="ltr">Contract</span> به دو <span dir="ltr">Capability</span> نامرتبط برمی‌گردد، <span dir="ltr">Scope</span> یا نام آن را بازبینی کن.

## <span dir="ltr">Consistency checks</span>

- <span dir="ltr">Command</span> به زمان امر و <span dir="ltr">Event</span> به <span dir="ltr">Fact</span> گذشته نام‌گذاری شده است.
- هیچ <span dir="ltr">Context</span>ی جدول <span dir="ltr">Context</span> دیگر را <span dir="ltr">Update</span> نمی‌کند.
- <span dir="ltr">Service Candidate</span> به‌عنوان <span dir="ltr">Hypothesis</span> علامت خورده، نه تصمیم <span dir="ltr">Deployment.</span>
- <span dir="ltr">API/Event</span> حداقل دادهٔ معنایی لازم را دارد، نه <span dir="ltr">Entity dump.</span>
- <span dir="ltr">Unknown</span>های <span dir="ltr">Transport</span> و <span dir="ltr">Failure</span> پنهان نشده‌اند.

## <span dir="ltr">Acceptance criteria</span>

- هر دو <span dir="ltr">Chain</span> کامل و قابل <span dir="ltr">Reverse tracing</span> باشند.
- هر <span dir="ltr">Fact</span> دقیقاً یک <span dir="ltr">Authority</span> اولیه داشته باشد.
- تفاوت <span dir="ltr">Legal Order</span> با <span dir="ltr">Operational Hold</span> روشن باشد.
- <span dir="ltr">Accounting</span> مالک <span dir="ltr">available balance</span> معرفی نشود.
- حداقل چهار <span dir="ltr">Unknown</span> واقعی ثبت شود.


</div>
