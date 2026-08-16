<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 02 Exercise</span> — <span dir="ltr">Capability Distinction Matrix</span>

- <span dir="ltr">Timebox: 18 minutes</span>
- <span dir="ltr">Output:</span> [<span dir="ltr">Distinction Matrix</span>](../artifacts/distinction-matrix-template.md)
- <span dir="ltr">Rule:</span> برچسب بدون <span dir="ltr">Reason</span> امتیاز ندارد.

## بخش A — طبقه‌بندی ۱۵ عبارت

برای هر عبارت <span dir="ltr">`Primary type`</span>، دلیل، تفسیر جایگزین احتمالی و نسخهٔ اصلاح‌شده را ثبت کن:

1. سامانهٔ تسهیلات
2. مدیریت تعهدات اعتباری
3. از درخواست وام تا دریافت وجه
4. بررسی اهلیت متقاضی
5. کمیتهٔ اعتباری
6. خدمت افتتاح غیرحضوری سپرده
7. سپردهٔ قرض‌الحسنه جاری
8. سامانهٔ سپرده
9. اعمال مسدودی قضایی
10. <span dir="ltr">`POST /accounts/{id}/holds`</span>
11. <span dir="ltr">`FundsHeld`</span>
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


## بخش B — سه <span dir="ltr">Capability</span> کامل

سه موردی را که <span dir="ltr">Capability</span> دانستی با این کارت تکمیل کن:


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


## بخش C — <span dir="ltr">Reverse test</span>

سه <span dir="ltr">System/API/Event</span> فهرست را به <span dir="ltr">Capability</span> بالادست برگردان. زنجیره را کوتاه بنویس:


</div>

<div dir="ltr" align="left">

```text
technical/current element → use/process → capability
```

</div>

<div dir="rtl" align="right">


## <span dir="ltr">Acceptance criteria</span>

- حداقل ۱۲ مورد درست و مستدل طبقه‌بندی شده باشد.
- برای دست‌کم سه مورد <span dir="ltr">`Ambiguous`</span>، زاویهٔ دید توضیح داده شود.
- هیچ نام سامانه، تیم یا <span dir="ltr">API</span> به‌تنهایی <span dir="ltr">Capability</span> پذیرفته نشود.
- سه <span dir="ltr">Capability</span> دارای <span dir="ltr">Outcome</span>، <span dir="ltr">Owner</span> و <span dir="ltr">KPI</span> باشند.
- از طبقه‌بندی، تعداد <span dir="ltr">Microservice</span> نتیجه گرفته نشود.


</div>
