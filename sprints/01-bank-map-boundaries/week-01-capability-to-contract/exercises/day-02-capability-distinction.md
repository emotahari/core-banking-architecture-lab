<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 02 Exercise</bdi> — <bdi dir="ltr">Capability Distinction Matrix</bdi>

- <bdi dir="ltr">Timebox: 18 minutes</bdi>
- <bdi dir="ltr">Output:</bdi> [<bdi dir="ltr">Distinction Matrix</bdi>](../artifacts/distinction-matrix-template.md)
- <bdi dir="ltr">Rule:</bdi> برچسب بدون <bdi dir="ltr">Reason</bdi> امتیاز ندارد.

## بخش A — طبقه‌بندی ۱۵ عبارت

برای هر عبارت <bdi dir="ltr">`Primary type`</bdi>، دلیل، تفسیر جایگزین احتمالی و نسخهٔ اصلاح‌شده را ثبت کن:

1. سامانهٔ تسهیلات
2. مدیریت تعهدات اعتباری
3. از درخواست وام تا دریافت وجه
4. بررسی اهلیت متقاضی
5. کمیتهٔ اعتباری
6. خدمت افتتاح غیرحضوری سپرده
7. سپردهٔ قرض‌الحسنه جاری
8. سامانهٔ سپرده
9. اعمال مسدودی قضایی
10. <bdi dir="ltr">`POST /accounts/{id}/holds`</bdi>
11. <bdi dir="ltr">`FundsHeld`</bdi>
12. انتقال آنی وجه
13. فرایند انتقال بین‌شعبه‌ای
14. ادارهٔ چک
15. بانکداری باز

نوع‌های مجاز:


</div>

<div dir="ltr" align="left">

```text
Capability | Value Stream | Process | Business Service | Product
Organization Unit | System/Application | Use Case | API | Event | Ambiguous
```

</div>

<div dir="rtl" align="right">


## بخش B — سه <bdi dir="ltr">Capability</bdi> کامل

سه موردی را که <bdi dir="ltr">Capability</bdi> دانستی با این کارت تکمیل کن:


</div>

<div dir="ltr" align="left">

```text
Name:
Definition:
Outcome:
Includes:
Excludes:
Proposed business owner:
KPI candidate:
Current systems (evidence only):
```

</div>

<div dir="rtl" align="right">


## بخش C — <bdi dir="ltr">Reverse test</bdi>

سه <bdi dir="ltr">System/API/Event</bdi> فهرست را به <bdi dir="ltr">Capability</bdi> بالادست برگردان. زنجیره را کوتاه بنویس:


</div>

<div dir="ltr" align="left">

```text
technical/current element → use/process → capability
```

</div>

<div dir="rtl" align="right">


## <bdi dir="ltr">Acceptance criteria</bdi>

- حداقل ۱۲ مورد درست و مستدل طبقه‌بندی شده باشد.
- برای دست‌کم سه مورد <bdi dir="ltr">`Ambiguous`</bdi>، زاویهٔ دید توضیح داده شود.
- هیچ نام سامانه، تیم یا <bdi dir="ltr">API</bdi> به‌تنهایی <bdi dir="ltr">Capability</bdi> پذیرفته نشود.
- سه <bdi dir="ltr">Capability</bdi> دارای <bdi dir="ltr">Outcome</bdi>، <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">KPI</bdi> باشند.
- از طبقه‌بندی، تعداد <bdi dir="ltr">Microservice</bdi> نتیجه گرفته نشود.


</div>
