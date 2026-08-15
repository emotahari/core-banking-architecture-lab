# Day 02 Exercise — Capability Distinction Matrix

- Timebox: 18 minutes
- Output: [Distinction Matrix](../artifacts/distinction-matrix-template.md)
- Rule: برچسب بدون Reason امتیاز ندارد.

## بخش A — طبقه‌بندی ۱۵ عبارت

برای هر عبارت `Primary type`، دلیل، تفسیر جایگزین احتمالی و نسخهٔ اصلاح‌شده را ثبت کن:

1. سامانهٔ تسهیلات
2. مدیریت تعهدات اعتباری
3. از درخواست وام تا دریافت وجه
4. بررسی اهلیت متقاضی
5. کمیتهٔ اعتباری
6. خدمت افتتاح غیرحضوری سپرده
7. سپردهٔ قرض‌الحسنه جاری
8. سامانهٔ سپرده
9. اعمال مسدودی قضایی
10. `POST /accounts/{id}/holds`
11. `FundsHeld`
12. انتقال آنی وجه
13. فرایند انتقال بین‌شعبه‌ای
14. ادارهٔ چک
15. بانکداری باز

نوع‌های مجاز:

```text
Capability | Value Stream | Process | Business Service | Product
Organization Unit | System/Application | Use Case | API | Event | Ambiguous
```

## بخش B — سه Capability کامل

سه موردی را که Capability دانستی با این کارت تکمیل کن:

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

## بخش C — Reverse test

سه System/API/Event فهرست را به Capability بالادست برگردان. زنجیره را کوتاه بنویس:

```text
technical/current element → use/process → capability
```

## Acceptance criteria

- حداقل ۱۲ مورد درست و مستدل طبقه‌بندی شده باشد.
- برای دست‌کم سه مورد `Ambiguous`، زاویهٔ دید توضیح داده شود.
- هیچ نام سامانه، تیم یا API به‌تنهایی Capability پذیرفته نشود.
- سه Capability دارای Outcome، Owner و KPI باشند.
- از طبقه‌بندی، تعداد Microservice نتیجه گرفته نشود.

