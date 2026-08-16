<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Week 01</span> — <span dir="ltr">Capability</span> تا <span dir="ltr">API/Event</span>

- <span dir="ltr">Status:</span> **<span dir="ltr">Ready</span> — پاسخ‌های <span dir="ltr">Day 01</span> حفظ شده‌اند؛ ادامه از <span dir="ltr">Day 02</span>**
- <span dir="ltr">Core time budget:</span> **<span dir="ltr">360 minutes</span> — <span dir="ltr">unchanged</span>**
- <span dir="ltr">Expansion budget:</span> **<span dir="ltr">150 minutes</span> — <span dir="ltr">105 Code Craft</span> + <span dir="ltr">45 Case File</span>**
- <span dir="ltr">Full expanded budget:</span> **<span dir="ltr">510 minutes</span>**
- <span dir="ltr">Banking lens:</span> اعطای تسهیلات، مسدودی قضایی سپرده، انتقال وجه و <span dir="ltr">UPI</span>
- <span dir="ltr">Main question:</span> چگونه از «بانک باید چه کاری بتواند انجام دهد؟» به <span dir="ltr">Contract</span> قابل اجرا و قابل‌ردیابی می‌رسیم؟
- <span dir="ltr">Technical outcome: Value Object</span>های بانکی، تست‌های <span dir="ltr">JUnit</span> و <span dir="ltr">Pipeline</span> سبز <span dir="ltr">`mvn verify`</span>

![برنامهٔ دقیق هفتهٔ اول](week-01-plan.svg)

## چرا این هفته وجود دارد؟

بیشتر خطاهای معماری <span dir="ltr">Core Banking</span> پیش از انتخاب <span dir="ltr">Kafka</span>، دیتابیس یا <span dir="ltr">Kubernetes</span> رخ می‌دهند: مسئله با نام سامانه، جدول، واحد سازمانی یا <span dir="ltr">Vendor</span> اشتباه گرفته می‌شود و سپس از روی همان نام‌ها <span dir="ltr">Service</span> ساخته می‌شود. <span dir="ltr">Week 01</span> یک زبان مشترک و یک زنجیرهٔ قابل‌ممیزی می‌سازد:


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


این زنجیره یک <span dir="ltr">Pipeline</span> مکانیکی یا نگاشت یک‌به‌یک نیست. در هر گام باید مسئله، مالک تصمیم، مالک داده، مرز تغییر و دلیل <span dir="ltr">Contract</span> روشن باشد.

## وضعیت فعلی تو

درس و <span dir="ltr">Exit Ticket</span> روز اول قبلاً شروع شده‌اند. پاسخ خام روز اول، حتی اگر ناقص یا نیازمند اصلاح باشد، **نباید پاک یا با پاسخ صیقلی جایگزین شود**؛ همان پاسخ خط پایه در <span dir="ltr">Week 24</span> برای سنجش رشد استفاده خواهد شد. ابتدا پرسش‌های باقی‌ماندهٔ <span dir="ltr">Day 01</span> را تمام کن، سپس از <span dir="ltr">Day 02</span> ادامه بده.

## قانون اجرای هر روز

1. بخش <span dir="ltr">`Before`</span> تمرین یا <span dir="ltr">Workbook</span> را بدون مراجعه به درس پاسخ بده، اگر برای آن روز تعریف شده است.
2. درس را یک‌بار پیوسته بخوان و مثال هدایت‌شده را خودت بازسازی کن.
3. تمرین مستقل را در [<span dir="ltr">Week 01 Workbook</span>](submissions/week-01-workbook.md) انجام بده.
4. درس و <span dir="ltr">Artifact</span> را ببند و <span dir="ltr">Exit Ticket</span> را بدون مراجعه پاسخ بده.
5. پاسخ خام را نگه دار؛ <span dir="ltr">Review</span> و <span dir="ltr">Revision</span> زیر آن اضافه می‌شوند.
6. روز فقط وقتی <span dir="ltr">`Done`</span> است که شاهد پایان آن قابل بازکردن باشد.

## ترتیب دقیق هستهٔ اصلی

| روز | زمان | درس | تمرین و شاهد پایان | آزمون خروج |
|---|---:|---|---|---|
| ۱ | ۶۰ دقیقه | [زبان معماری و خط پایه](lessons/day-01-architecture-language-fa.md) | [<span dir="ltr">Architecture Baseline</span>](exercises/day-01-baseline.md) و پاسخ موجود | [<span dir="ltr">Exit Ticket</span>](quizzes/day-01-exit-ticket.md) |
| ۲ | ۴۵ دقیقه | [<span dir="ltr">Capability</span> در برابر <span dir="ltr">Process</span>، <span dir="ltr">Service</span> و <span dir="ltr">System</span>](lessons/day-02-capability-distinction-fa.md) | [<span dir="ltr">Distinction Matrix</span>](exercises/day-02-capability-distinction.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-02-exit-ticket.md) |
| ۳ | ۵۰ دقیقه | [از <span dir="ltr">System</span> تا <span dir="ltr">Contract</span> و <span dir="ltr">Traceability</span>](lessons/day-03-traceability-chain-fa.md) | [دو <span dir="ltr">Traceability Chain</span>](exercises/day-03-traceability-chain.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-03-exit-ticket.md) |
| ۴ | ۵۵ دقیقه | [<span dir="ltr">Coupling</span>، <span dir="ltr">Cohesion</span>، <span dir="ltr">Encapsulation</span> و <span dir="ltr">Information Hiding</span>](lessons/day-04-design-forces-boundary-fa.md) | [<span dir="ltr">Coupling Review</span>](exercises/day-04-coupling-review.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-04-exit-ticket.md) |
| ۵ | ۷۰ دقیقه | [<span dir="ltr">Banking Capability Map</span> و <span dir="ltr">BIAN 14</span>](lessons/day-05-banking-capability-map-bian-fa.md) | [<span dir="ltr">Capability Map v1</span> + <span dir="ltr">Gap Check</span>](exercises/day-05-capability-map-bian-gap-check.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-05-exit-ticket.md) |
| ۶ | ۶۰ دقیقه | [<span dir="ltr">Value Object</span> و <span dir="ltr">Pipeline</span>](lessons/day-06-value-objects-pipeline-fa.md) | [<span dir="ltr">Money</span> و <span dir="ltr">Typed IDs</span>](exercises/day-06-value-objects.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-06-exit-ticket.md) |
| ۷ | ۲۰ دقیقه | [تثبیت و دفاع <span dir="ltr">Week 01</span>](lessons/day-07-week-defense-fa.md) | [دفاع ده‌دقیقه‌ای](exercises/day-07-week-defense.md) | <span dir="ltr">Rubric</span> داخل <span dir="ltr">Gate</span> |
| **جمع هسته** | **۳۶۰ دقیقه** |  |  |  |

ریزبودجه‌ها شامل درس، تمرین و <span dir="ltr">Exit Ticket</span> هستند. دفاع و <span dir="ltr">Review</span> استاد پس از <span dir="ltr">Submission</span> جزو بودجهٔ خودخوان حساب نشده‌اند.

## مسیر افزودهٔ <span dir="ltr">Week 01</span>

هفت روز بالا برنامهٔ اصلی‌اند و هیچ بخشی از آن‌ها با جلسات زیر جایگزین نمی‌شود. بعد از <span dir="ltr">Day 07</span> دو جلسهٔ افزوده را انجام بده:

| جلسه | زمان | محتوا | تمرین و شاهد پایان | آزمون/دفاع |
|---|---:|---|---|---|
| ۸ | ۱۰۵ دقیقه | [<span dir="ltr">Clean Code</span> و <span dir="ltr">Refactoring</span> از <span dir="ltr">Primitive</span> به <span dir="ltr">Value Object</span>](lessons/day-08-clean-code-value-object-refactoring-fa.md) | [<span dir="ltr">Runnable Money Refactoring Kata</span>](exercises/day-08-money-refactoring-kata.md) + [<span dir="ltr">Code Review Checklist</span>](artifacts/day-08-code-review-checklist.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-08-exit-ticket.md) |
| ۹ | ۴۵ دقیقه | [پروندهٔ <span dir="ltr">UPI</span> هند؛ از <span dir="ltr">Capability</span> تا شبکهٔ <span dir="ltr">API</span>](case-studies/week-01-upi-fa.md) | [<span dir="ltr">Capability/Contract Review</span>](exercises/day-09-upi-capability-contract-review.md) | دفاع پنج‌سؤالی داخل پرونده |
| **جمع افزوده** | **۱۵۰ دقیقه** |  |  |  |

<span dir="ltr">Starter</span> اجرایی <span dir="ltr">Day 08</span> در <span dir="ltr">Test scope</span> قرار دارد تا ابتدا رفتار موجود را تثبیت و سپس <span dir="ltr">Refactor</span> کنی:


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


قواعد دائمی دو ریل افزوده در [الحاقیهٔ <span dir="ltr">Code Craft</span> و <span dir="ltr">Case File</span>](../../../docs/course/expanded-weekly-tracks.md) آمده است.

## خروجی‌های اجباری پایان <span dir="ltr">Week 01</span>

### تحلیل و معماری

- [<span dir="ltr">Distinction Matrix</span>](artifacts/distinction-matrix-template.md) برای <span dir="ltr">Capability</span>، <span dir="ltr">Process</span>، <span dir="ltr">Business Service</span>، <span dir="ltr">System</span> و <span dir="ltr">Contract</span>
- دو [<span dir="ltr">Traceability Chain</span>](artifacts/traceability-chain-template.md) برای مسدودی قضایی و اعطای تسهیلات
- [<span dir="ltr">Coupling Review</span>](artifacts/coupling-review-template.md) یک طراحی کاپل‌شده
- [<span dir="ltr">Capability Map v1</span>](artifacts/capability-map-working-draft.md) در سطح <span dir="ltr">L1</span>
- [<span dir="ltr">BIAN Gap Check</span>](artifacts/bian-gap-check-template.md) با ثبت <span dir="ltr">Match</span>، <span dir="ltr">Gap</span> و <span dir="ltr">False Friend</span>
- [<span dir="ltr">Glossary</span>](artifacts/glossary.md) با حداقل ۴۰ اصطلاح
- پاسخ خط پایهٔ سه سناریوی نهایی، بدون پاک‌کردن نسخهٔ خام

### کد و تست

- <span dir="ltr">`Money`</span>، <span dir="ltr">`AccountId`</span>، <span dir="ltr">`CustomerId`</span> و <span dir="ltr">`BranchId`</span> بدون وابستگی به <span dir="ltr">Spring/JPA</span>
- تست <span dir="ltr">Equality</span> عددی <span dir="ltr">Money</span>، <span dir="ltr">Currency mismatch</span>، ورودی نامعتبر و <span dir="ltr">Rounding</span> صریح
- <span dir="ltr">Baseline</span> سبز و <span dir="ltr">Refactor</span> مرحله‌ای <span dir="ltr">Kata</span> روز هشتم
- حداقل یک <span dir="ltr">Edge Test</span> تازه و <span dir="ltr">Pattern Decision</span> دربارهٔ <span dir="ltr">Value Object</span> و <span dir="ltr">Static Factory</span>
- <span dir="ltr">Pipeline</span> اولیهٔ <span dir="ltr">`mvn verify`</span> سبز

### پرونده و دفاع

- [<span dir="ltr">Week 01 Report</span>](artifacts/week-01-report-template.md)
- دفاع حداکثر ده‌دقیقه‌ای از زنجیرهٔ <span dir="ltr">Capability</span> تا <span dir="ltr">Contract</span>
- <span dir="ltr">UPI Architecture Review</span> با تفکیک <span dir="ltr">`FACT`</span>، <span dir="ltr">`INFERENCE`</span> و <span dir="ltr">`UNKNOWN`</span>

## <span dir="ltr">Definition of Done</span>

<span dir="ltr">Week 01</span> زمانی <span dir="ltr">`Done — Expanded`</span> است که:

- تفاوت <span dir="ltr">Capability</span>، <span dir="ltr">Process</span>، <span dir="ltr">Business Service</span>، <span dir="ltr">System</span>، <span dir="ltr">API</span> و <span dir="ltr">Event</span> با مثال بانکی توضیح داده شود.
- زنجیرهٔ <span dir="ltr">Capability</span> تا <span dir="ltr">API/Event</span> برای دو سناریو قابل‌ردیابی باشد.
- هیچ <span dir="ltr">Service Candidate</span> بدون <span dir="ltr">Capability</span>، مسئولیت منسجم و مالک تصمیم معرفی نشده باشد.
- نقش <span dir="ltr">BIAN</span> به‌عنوان <span dir="ltr">Reference Model</span> و <span dir="ltr">Gap Check</span>، نه <span dir="ltr">Deployment Blueprint</span>، دفاع شود.
- <span dir="ltr">Capability Map</span> از نام نرم‌افزار، <span dir="ltr">Vendor</span>، جدول و چارت سازمانی مستقل باشد.
- <span dir="ltr">Value Object</span>ها <span dir="ltr">Equality</span> و ورودی نامعتبر را آزمون کنند و <span dir="ltr">Rounding</span> پنهان نداشته باشند.
- <span dir="ltr">Baseline</span> و نسخهٔ <span dir="ltr">Refactored Code Craft</span> هر دو سبز باشند و <span dir="ltr">Complexity</span> اضافه‌شده ثبت شود.
- پروندهٔ <span dir="ltr">UPI</span> دست‌کم یک شکست عملیاتی، <span dir="ltr">Timeline</span> مستند و <span dir="ltr">Current State</span> تاریخ‌دار داشته باشد.
- <span dir="ltr">`mvn verify`</span> سبز باشد.
- دفاع <span dir="ltr">Week 01</span> حداقل ۸ از ۱۰ بگیرد و <span dir="ltr">Critical Error</span> نداشته باشد.

## <span dir="ltr">Critical Error</span>های این هفته

هرکدام از موارد زیر <span dir="ltr">Gate</span> را متوقف می‌کند:

1. نام سامانه، تیم، جدول یا <span dir="ltr">API</span> به‌عنوان <span dir="ltr">Capability</span> معرفی شود.
2. <span dir="ltr">BIAN Service Domain</span> به‌طور خودکار یک <span dir="ltr">Microservice</span> یا <span dir="ltr">Bounded Context</span> قطعی فرض شود.
3. از وجود یک <span dir="ltr">Entity</span> مشترک، مالکیت مشترک نتیجه گرفته شود.
4. <span dir="ltr">API/Event</span> بدون <span dir="ltr">Use Case</span>، <span dir="ltr">Owner</span> و معنای کسب‌وکاری معرفی شود.
5. <span dir="ltr">Money</span> با <span dir="ltr">`double`</span> یا <span dir="ltr">Rounding</span> پنهان مدل شود.
6. <span dir="ltr">Pattern</span> صرفاً برای نمایش دانش اضافه شود و <span dir="ltr">Alternative</span> ساده‌تر بررسی نشود.

## خارج از محدوده

این موضوعات عمداً به هفته‌های بعد موکول شده‌اند:

- تعیین <span dir="ltr">Context Map</span> نهایی و طبقه‌بندی <span dir="ltr">Core/Supporting/Generic</span>
- استخراج <span dir="ltr">Microservice</span> و انتخاب مرز <span dir="ltr">Deployment</span>
- طراحی <span dir="ltr">Aggregate</span> و <span dir="ltr">Transaction Boundary</span> کامل
- انتخاب <span dir="ltr">REST</span> در برابر <span dir="ltr">Kafka</span>
- <span dir="ltr">Saga</span>، <span dir="ltr">Outbox</span>، <span dir="ltr">Idempotency</span> و <span dir="ltr">Reconciliation</span>
- طراحی سند حسابداری و مدل فیزیکی دیتابیس

در <span dir="ltr">Week 01</span> فقط واژه، <span dir="ltr">Traceability</span>، <span dir="ltr">Quality of Boundary</span> و <span dir="ltr">Type safety</span> را می‌سازیم؛ راه‌حل توزیع‌شده را زودتر از مسئله انتخاب نمی‌کنیم.

## منابع

مسیر مطالعهٔ محدود و هدفمند در [<span dir="ltr">References</span>](references/README.md) آمده است. برای <span dir="ltr">UPI</span>، <span dir="ltr">Source Register</span> تاریخ‌دار داخل خود پرونده نگهداری می‌شود.


</div>
