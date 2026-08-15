<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 03 Exercise</bdi> — <bdi dir="ltr">Two Traceability Chains</bdi>

- <bdi dir="ltr">Timebox: 21 minutes</bdi>
- <bdi dir="ltr">Output:</bdi> دو نسخه از [<bdi dir="ltr">Traceability Chain Template</bdi>](../artifacts/traceability-chain-template.md)
- <bdi dir="ltr">Scenarios:</bdi> مسدودی قضایی سپرده و اعطای تسهیلات

## <bdi dir="ltr">Chain A</bdi> — مسدودی قضایی

فرض کن حکمی معتبر برای <bdi dir="ltr">Hold</bdi> مبلغ ۵۰٬۰۰۰٬۰۰۰ ریال روی یک سپرده دریافت شده است. مشتری ممکن است موجودی دفتری ۸۰٬۰۰۰٬۰۰۰ ریال داشته باشد، اما فقط مبلغ غیرمسدود قابل برداشت است.

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


برای هر عنصر <bdi dir="ltr">Owner</bdi>، <bdi dir="ltr">Evidence</bdi> و یک <bdi dir="ltr">Open question</bdi> بنویس.

## <bdi dir="ltr">Chain B</bdi> — اعطا و واریز

قرارداد مرابحه مصوب است. مبلغ ۱۰۰٬۰۰۰٬۰۰۰ ریال باید دقیقاً یک‌بار به سپردهٔ جاری مشتری واریز شود و <bdi dir="ltr">Fact</bdi> مالی آن قابل ثبت باشد.

حداقل این <bdi dir="ltr">Ownership</bdi>ها را جدا کن:

- وضعیت و تصمیم اعطا
- ماندهٔ اصل تسهیلات
- ماندهٔ قابل برداشت سپرده
- نتیجهٔ <bdi dir="ltr">Credit</bdi>
- <bdi dir="ltr">Journal</bdi> مالی

هنوز <bdi dir="ltr">REST</bdi>، <bdi dir="ltr">Kafka</bdi>، <bdi dir="ltr">Saga</bdi> یا دیتابیس را انتخاب نکن.

## <bdi dir="ltr">Reverse trace</bdi>

برای این دو <bdi dir="ltr">Contract candidate</bdi> مسیر برگشت تا <bdi dir="ltr">Capability</bdi> را بنویس:

1. <bdi dir="ltr">`PlaceFundsHold`</bdi>
2. <bdi dir="ltr">`DepositCredited`</bdi>

اگر <bdi dir="ltr">Contract</bdi> به دو <bdi dir="ltr">Capability</bdi> نامرتبط برمی‌گردد، <bdi dir="ltr">Scope</bdi> یا نام آن را بازبینی کن.

## <bdi dir="ltr">Consistency checks</bdi>

- <bdi dir="ltr">Command</bdi> به زمان امر و <bdi dir="ltr">Event</bdi> به <bdi dir="ltr">Fact</bdi> گذشته نام‌گذاری شده است.
- هیچ <bdi dir="ltr">Context</bdi>ی جدول <bdi dir="ltr">Context</bdi> دیگر را <bdi dir="ltr">Update</bdi> نمی‌کند.
- <bdi dir="ltr">Service Candidate</bdi> به‌عنوان <bdi dir="ltr">Hypothesis</bdi> علامت خورده، نه تصمیم <bdi dir="ltr">Deployment.</bdi>
- <bdi dir="ltr">API/Event</bdi> حداقل دادهٔ معنایی لازم را دارد، نه <bdi dir="ltr">Entity dump.</bdi>
- <bdi dir="ltr">Unknown</bdi>های <bdi dir="ltr">Transport</bdi> و <bdi dir="ltr">Failure</bdi> پنهان نشده‌اند.

## <bdi dir="ltr">Acceptance criteria</bdi>

- هر دو <bdi dir="ltr">Chain</bdi> کامل و قابل <bdi dir="ltr">Reverse tracing</bdi> باشند.
- هر <bdi dir="ltr">Fact</bdi> دقیقاً یک <bdi dir="ltr">Authority</bdi> اولیه داشته باشد.
- تفاوت <bdi dir="ltr">Legal Order</bdi> با <bdi dir="ltr">Operational Hold</bdi> روشن باشد.
- <bdi dir="ltr">Accounting</bdi> مالک <bdi dir="ltr">available balance</bdi> معرفی نشود.
- حداقل چهار <bdi dir="ltr">Unknown</bdi> واقعی ثبت شود.


</div>
