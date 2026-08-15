<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Week 01</bdi> — <bdi dir="ltr">Capability</bdi> تا <bdi dir="ltr">API/Event</bdi>

- <bdi dir="ltr">Status:</bdi> **<bdi dir="ltr">Ready</bdi> — پاسخ‌های <bdi dir="ltr">Day 01</bdi> حفظ شده‌اند؛ ادامه از <bdi dir="ltr">Day 02</bdi>**
- <bdi dir="ltr">Core time budget:</bdi> **<bdi dir="ltr">360 minutes</bdi> — <bdi dir="ltr">unchanged</bdi>**
- <bdi dir="ltr">Expansion budget:</bdi> **<bdi dir="ltr">150 minutes</bdi> — <bdi dir="ltr">105 Code Craft</bdi> + <bdi dir="ltr">45 Case File</bdi>**
- <bdi dir="ltr">Full expanded budget:</bdi> **<bdi dir="ltr">510 minutes</bdi>**
- <bdi dir="ltr">Banking lens:</bdi> اعطای تسهیلات، مسدودی قضایی سپرده، انتقال وجه و <bdi dir="ltr">UPI</bdi>
- <bdi dir="ltr">Main question:</bdi> چگونه از «بانک باید چه کاری بتواند انجام دهد؟» به <bdi dir="ltr">Contract</bdi> قابل اجرا و قابل‌ردیابی می‌رسیم؟
- <bdi dir="ltr">Technical outcome: Value Object</bdi>های بانکی، تست‌های <bdi dir="ltr">JUnit</bdi> و <bdi dir="ltr">Pipeline</bdi> سبز <bdi dir="ltr">`mvn verify`</bdi>

![برنامهٔ دقیق هفتهٔ اول](week-01-plan.svg)

## چرا این هفته وجود دارد؟

بیشتر خطاهای معماری <bdi dir="ltr">Core Banking</bdi> پیش از انتخاب <bdi dir="ltr">Kafka</bdi>، دیتابیس یا <bdi dir="ltr">Kubernetes</bdi> رخ می‌دهند: مسئله با نام سامانه، جدول، واحد سازمانی یا <bdi dir="ltr">Vendor</bdi> اشتباه گرفته می‌شود و سپس از روی همان نام‌ها <bdi dir="ltr">Service</bdi> ساخته می‌شود. <bdi dir="ltr">Week 01</bdi> یک زبان مشترک و یک زنجیرهٔ قابل‌ممیزی می‌سازد:


</div>

<div dir="ltr" align="left">

```text
Capability
  → Domain / Subdomain
  → Bounded Context
  → Module / Service Candidate
  → Use Case
  → Command / Query
  → API / Event
```

</div>

<div dir="rtl" align="right">


این زنجیره یک <bdi dir="ltr">Pipeline</bdi> مکانیکی یا نگاشت یک‌به‌یک نیست. در هر گام باید مسئله، مالک تصمیم، مالک داده، مرز تغییر و دلیل <bdi dir="ltr">Contract</bdi> روشن باشد.

## وضعیت فعلی تو

درس و <bdi dir="ltr">Exit Ticket</bdi> روز اول قبلاً شروع شده‌اند. پاسخ خام روز اول، حتی اگر ناقص یا نیازمند اصلاح باشد، **نباید پاک یا با پاسخ صیقلی جایگزین شود**؛ همان پاسخ خط پایه در <bdi dir="ltr">Week 24</bdi> برای سنجش رشد استفاده خواهد شد. ابتدا پرسش‌های باقی‌ماندهٔ <bdi dir="ltr">Day 01</bdi> را تمام کن، سپس از <bdi dir="ltr">Day 02</bdi> ادامه بده.

## قانون اجرای هر روز

1. بخش <bdi dir="ltr">`Before`</bdi> تمرین یا <bdi dir="ltr">Workbook</bdi> را بدون مراجعه به درس پاسخ بده، اگر برای آن روز تعریف شده است.
2. درس را یک‌بار پیوسته بخوان و مثال هدایت‌شده را خودت بازسازی کن.
3. تمرین مستقل را در [<bdi dir="ltr">Week 01 Workbook</bdi>](submissions/week-01-workbook.md) انجام بده.
4. درس و <bdi dir="ltr">Artifact</bdi> را ببند و <bdi dir="ltr">Exit Ticket</bdi> را بدون مراجعه پاسخ بده.
5. پاسخ خام را نگه دار؛ <bdi dir="ltr">Review</bdi> و <bdi dir="ltr">Revision</bdi> زیر آن اضافه می‌شوند.
6. روز فقط وقتی <bdi dir="ltr">`Done`</bdi> است که شاهد پایان آن قابل بازکردن باشد.

## ترتیب دقیق هستهٔ اصلی

| روز | زمان | درس | تمرین و شاهد پایان | آزمون خروج |
|---|---:|---|---|---|
| ۱ | ۶۰ دقیقه | [زبان معماری و خط پایه](lessons/day-01-architecture-language-fa.md) | [<bdi dir="ltr">Architecture Baseline</bdi>](exercises/day-01-baseline.md) و پاسخ موجود | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-01-exit-ticket.md) |
| ۲ | ۴۵ دقیقه | [<bdi dir="ltr">Capability</bdi> در برابر <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Service</bdi> و <bdi dir="ltr">System</bdi>](lessons/day-02-capability-distinction-fa.md) | [<bdi dir="ltr">Distinction Matrix</bdi>](exercises/day-02-capability-distinction.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-02-exit-ticket.md) |
| ۳ | ۵۰ دقیقه | [از <bdi dir="ltr">System</bdi> تا <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Traceability</bdi>](lessons/day-03-traceability-chain-fa.md) | [دو <bdi dir="ltr">Traceability Chain</bdi>](exercises/day-03-traceability-chain.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-03-exit-ticket.md) |
| ۴ | ۵۵ دقیقه | [<bdi dir="ltr">Coupling</bdi>، <bdi dir="ltr">Cohesion</bdi>، <bdi dir="ltr">Encapsulation</bdi> و <bdi dir="ltr">Information Hiding</bdi>](lessons/day-04-design-forces-boundary-fa.md) | [<bdi dir="ltr">Coupling Review</bdi>](exercises/day-04-coupling-review.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-04-exit-ticket.md) |
| ۵ | ۷۰ دقیقه | [<bdi dir="ltr">Banking Capability Map</bdi> و <bdi dir="ltr">BIAN 14</bdi>](lessons/day-05-banking-capability-map-bian-fa.md) | [<bdi dir="ltr">Capability Map v1</bdi> + <bdi dir="ltr">Gap Check</bdi>](exercises/day-05-capability-map-bian-gap-check.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-05-exit-ticket.md) |
| ۶ | ۶۰ دقیقه | [<bdi dir="ltr">Value Object</bdi> و <bdi dir="ltr">Pipeline</bdi>](lessons/day-06-value-objects-pipeline-fa.md) | [<bdi dir="ltr">Money</bdi> و <bdi dir="ltr">Typed IDs</bdi>](exercises/day-06-value-objects.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-06-exit-ticket.md) |
| ۷ | ۲۰ دقیقه | [تثبیت و دفاع <bdi dir="ltr">Week 01</bdi>](lessons/day-07-week-defense-fa.md) | [دفاع ده‌دقیقه‌ای](exercises/day-07-week-defense.md) | <bdi dir="ltr">Rubric</bdi> داخل <bdi dir="ltr">Gate</bdi> |
| **جمع هسته** | **۳۶۰ دقیقه** |  |  |  |

ریزبودجه‌ها شامل درس، تمرین و <bdi dir="ltr">Exit Ticket</bdi> هستند. دفاع و <bdi dir="ltr">Review</bdi> استاد پس از <bdi dir="ltr">Submission</bdi> جزو بودجهٔ خودخوان حساب نشده‌اند.

## مسیر افزودهٔ <bdi dir="ltr">Week 01</bdi>

هفت روز بالا برنامهٔ اصلی‌اند و هیچ بخشی از آن‌ها با جلسات زیر جایگزین نمی‌شود. بعد از <bdi dir="ltr">Day 07</bdi> دو جلسهٔ افزوده را انجام بده:

| جلسه | زمان | محتوا | تمرین و شاهد پایان | آزمون/دفاع |
|---|---:|---|---|---|
| ۸ | ۱۰۵ دقیقه | [<bdi dir="ltr">Clean Code</bdi> و <bdi dir="ltr">Refactoring</bdi> از <bdi dir="ltr">Primitive</bdi> به <bdi dir="ltr">Value Object</bdi>](lessons/day-08-clean-code-value-object-refactoring-fa.md) | [<bdi dir="ltr">Runnable Money Refactoring Kata</bdi>](exercises/day-08-money-refactoring-kata.md) + [<bdi dir="ltr">Code Review Checklist</bdi>](artifacts/day-08-code-review-checklist.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-08-exit-ticket.md) |
| ۹ | ۴۵ دقیقه | [پروندهٔ <bdi dir="ltr">UPI</bdi> هند؛ از <bdi dir="ltr">Capability</bdi> تا شبکهٔ <bdi dir="ltr">API</bdi>](case-studies/week-01-upi-fa.md) | [<bdi dir="ltr">Capability/Contract Review</bdi>](exercises/day-09-upi-capability-contract-review.md) | دفاع پنج‌سؤالی داخل پرونده |
| **جمع افزوده** | **۱۵۰ دقیقه** |  |  |  |

<bdi dir="ltr">Starter</bdi> اجرایی <bdi dir="ltr">Day 08</bdi> در <bdi dir="ltr">Test scope</bdi> قرار دارد تا ابتدا رفتار موجود را تثبیت و سپس <bdi dir="ltr">Refactor</bdi> کنی:


</div>

<div dir="ltr" align="left">

```text
backend/banking-modulith/src/test/java/
└── com/example/corebankinglab/craftsmanship/week01/
    ├── PrimitiveTransferRequest.java
    └── PrimitiveTransferRequestCharacterizationTest.java
```

</div>

<div dir="rtl" align="right">


قواعد دائمی دو ریل افزوده در [الحاقیهٔ <bdi dir="ltr">Code Craft</bdi> و <bdi dir="ltr">Case File</bdi>](../../../docs/course/expanded-weekly-tracks.md) آمده است.

## خروجی‌های اجباری پایان <bdi dir="ltr">Week 01</bdi>

### تحلیل و معماری

- [<bdi dir="ltr">Distinction Matrix</bdi>](artifacts/distinction-matrix-template.md) برای <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Business Service</bdi>، <bdi dir="ltr">System</bdi> و <bdi dir="ltr">Contract</bdi>
- دو [<bdi dir="ltr">Traceability Chain</bdi>](artifacts/traceability-chain-template.md) برای مسدودی قضایی و اعطای تسهیلات
- [<bdi dir="ltr">Coupling Review</bdi>](artifacts/coupling-review-template.md) یک طراحی کاپل‌شده
- [<bdi dir="ltr">Capability Map v1</bdi>](artifacts/capability-map-working-draft.md) در سطح <bdi dir="ltr">L1</bdi>
- [<bdi dir="ltr">BIAN Gap Check</bdi>](artifacts/bian-gap-check-template.md) با ثبت <bdi dir="ltr">Match</bdi>، <bdi dir="ltr">Gap</bdi> و <bdi dir="ltr">False Friend</bdi>
- [<bdi dir="ltr">Glossary</bdi>](artifacts/glossary.md) با حداقل ۴۰ اصطلاح
- پاسخ خط پایهٔ سه سناریوی نهایی، بدون پاک‌کردن نسخهٔ خام

### کد و تست

- <bdi dir="ltr">`Money`</bdi>، <bdi dir="ltr">`AccountId`</bdi>، <bdi dir="ltr">`CustomerId`</bdi> و <bdi dir="ltr">`BranchId`</bdi> بدون وابستگی به <bdi dir="ltr">Spring/JPA</bdi>
- تست <bdi dir="ltr">Equality</bdi> عددی <bdi dir="ltr">Money</bdi>، <bdi dir="ltr">Currency mismatch</bdi>، ورودی نامعتبر و <bdi dir="ltr">Rounding</bdi> صریح
- <bdi dir="ltr">Baseline</bdi> سبز و <bdi dir="ltr">Refactor</bdi> مرحله‌ای <bdi dir="ltr">Kata</bdi> روز هشتم
- حداقل یک <bdi dir="ltr">Edge Test</bdi> تازه و <bdi dir="ltr">Pattern Decision</bdi> دربارهٔ <bdi dir="ltr">Value Object</bdi> و <bdi dir="ltr">Static Factory</bdi>
- <bdi dir="ltr">Pipeline</bdi> اولیهٔ <bdi dir="ltr">`mvn verify`</bdi> سبز

### پرونده و دفاع

- [<bdi dir="ltr">Week 01 Report</bdi>](artifacts/week-01-report-template.md)
- دفاع حداکثر ده‌دقیقه‌ای از زنجیرهٔ <bdi dir="ltr">Capability</bdi> تا <bdi dir="ltr">Contract</bdi>
- <bdi dir="ltr">UPI Architecture Review</bdi> با تفکیک <bdi dir="ltr">`FACT`</bdi>، <bdi dir="ltr">`INFERENCE`</bdi> و <bdi dir="ltr">`UNKNOWN`</bdi>

## <bdi dir="ltr">Definition of Done</bdi>

<bdi dir="ltr">Week 01</bdi> زمانی <bdi dir="ltr">`Done — Expanded`</bdi> است که:

- تفاوت <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Business Service</bdi>، <bdi dir="ltr">System</bdi>، <bdi dir="ltr">API</bdi> و <bdi dir="ltr">Event</bdi> با مثال بانکی توضیح داده شود.
- زنجیرهٔ <bdi dir="ltr">Capability</bdi> تا <bdi dir="ltr">API/Event</bdi> برای دو سناریو قابل‌ردیابی باشد.
- هیچ <bdi dir="ltr">Service Candidate</bdi> بدون <bdi dir="ltr">Capability</bdi>، مسئولیت منسجم و مالک تصمیم معرفی نشده باشد.
- نقش <bdi dir="ltr">BIAN</bdi> به‌عنوان <bdi dir="ltr">Reference Model</bdi> و <bdi dir="ltr">Gap Check</bdi>، نه <bdi dir="ltr">Deployment Blueprint</bdi>، دفاع شود.
- <bdi dir="ltr">Capability Map</bdi> از نام نرم‌افزار، <bdi dir="ltr">Vendor</bdi>، جدول و چارت سازمانی مستقل باشد.
- <bdi dir="ltr">Value Object</bdi>ها <bdi dir="ltr">Equality</bdi> و ورودی نامعتبر را آزمون کنند و <bdi dir="ltr">Rounding</bdi> پنهان نداشته باشند.
- <bdi dir="ltr">Baseline</bdi> و نسخهٔ <bdi dir="ltr">Refactored Code Craft</bdi> هر دو سبز باشند و <bdi dir="ltr">Complexity</bdi> اضافه‌شده ثبت شود.
- پروندهٔ <bdi dir="ltr">UPI</bdi> دست‌کم یک شکست عملیاتی، <bdi dir="ltr">Timeline</bdi> مستند و <bdi dir="ltr">Current State</bdi> تاریخ‌دار داشته باشد.
- <bdi dir="ltr">`mvn verify`</bdi> سبز باشد.
- دفاع <bdi dir="ltr">Week 01</bdi> حداقل ۸ از ۱۰ بگیرد و <bdi dir="ltr">Critical Error</bdi> نداشته باشد.

## <bdi dir="ltr">Critical Error</bdi>های این هفته

هرکدام از موارد زیر <bdi dir="ltr">Gate</bdi> را متوقف می‌کند:

1. نام سامانه، تیم، جدول یا <bdi dir="ltr">API</bdi> به‌عنوان <bdi dir="ltr">Capability</bdi> معرفی شود.
2. <bdi dir="ltr">BIAN Service Domain</bdi> به‌طور خودکار یک <bdi dir="ltr">Microservice</bdi> یا <bdi dir="ltr">Bounded Context</bdi> قطعی فرض شود.
3. از وجود یک <bdi dir="ltr">Entity</bdi> مشترک، مالکیت مشترک نتیجه گرفته شود.
4. <bdi dir="ltr">API/Event</bdi> بدون <bdi dir="ltr">Use Case</bdi>، <bdi dir="ltr">Owner</bdi> و معنای کسب‌وکاری معرفی شود.
5. <bdi dir="ltr">Money</bdi> با <bdi dir="ltr">`double`</bdi> یا <bdi dir="ltr">Rounding</bdi> پنهان مدل شود.
6. <bdi dir="ltr">Pattern</bdi> صرفاً برای نمایش دانش اضافه شود و <bdi dir="ltr">Alternative</bdi> ساده‌تر بررسی نشود.

## خارج از محدوده

این موضوعات عمداً به هفته‌های بعد موکول شده‌اند:

- تعیین <bdi dir="ltr">Context Map</bdi> نهایی و طبقه‌بندی <bdi dir="ltr">Core/Supporting/Generic</bdi>
- استخراج <bdi dir="ltr">Microservice</bdi> و انتخاب مرز <bdi dir="ltr">Deployment</bdi>
- طراحی <bdi dir="ltr">Aggregate</bdi> و <bdi dir="ltr">Transaction Boundary</bdi> کامل
- انتخاب <bdi dir="ltr">REST</bdi> در برابر <bdi dir="ltr">Kafka</bdi>
- <bdi dir="ltr">Saga</bdi>، <bdi dir="ltr">Outbox</bdi>، <bdi dir="ltr">Idempotency</bdi> و <bdi dir="ltr">Reconciliation</bdi>
- طراحی سند حسابداری و مدل فیزیکی دیتابیس

در <bdi dir="ltr">Week 01</bdi> فقط واژه، <bdi dir="ltr">Traceability</bdi>، <bdi dir="ltr">Quality of Boundary</bdi> و <bdi dir="ltr">Type safety</bdi> را می‌سازیم؛ راه‌حل توزیع‌شده را زودتر از مسئله انتخاب نمی‌کنیم.

## منابع

مسیر مطالعهٔ محدود و هدفمند در [<bdi dir="ltr">References</bdi>](references/README.md) آمده است. برای <bdi dir="ltr">UPI</bdi>، <bdi dir="ltr">Source Register</bdi> تاریخ‌دار داخل خود پرونده نگهداری می‌شود.


</div>
