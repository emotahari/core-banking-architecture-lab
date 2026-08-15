<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Week 02</bdi> — <bdi dir="ltr">Strategic DDD</bdi> و مالکیت

- <bdi dir="ltr">Status:</bdi> **<bdi dir="ltr">Ready</bdi>**
- <bdi dir="ltr">Core time budget:</bdi> **<bdi dir="ltr">360 minutes</bdi> — <bdi dir="ltr">unchanged</bdi>**
- <bdi dir="ltr">Expansion budget:</bdi> **<bdi dir="ltr">150 minutes</bdi> — <bdi dir="ltr">105 Code Craft</bdi> + <bdi dir="ltr">45 Case File</bdi>**
- <bdi dir="ltr">Full expanded budget:</bdi> **<bdi dir="ltr">510 minutes</bdi>**
- <bdi dir="ltr">Banking lens:</bdi> اعطای تسهیلات، واریز به سپرده و مسدودی قضایی
- <bdi dir="ltr">Main question:</bdi> هر مدل، داده و تصمیم در کدام <bdi dir="ltr">Bounded Context</bdi> معنا و مالک دارد؟
- <bdi dir="ltr">Technical outcome:</bdi> شش <bdi dir="ltr">Application Module</bdi> قابل <bdi dir="ltr">Verification</bdi> در <bdi dir="ltr">Spring Modulith</bdi>

![برنامهٔ دقیق هفتهٔ دوم](week-02-plan.svg)

## چرا این هفته وجود دارد؟

در <bdi dir="ltr">Week 01</bdi> یاد گرفتیم از <bdi dir="ltr">Capability</bdi> و مسئلهٔ کسب‌وکاری به <bdi dir="ltr">Contract</bdi> برسیم و نباید از جدول، سامانه یا <bdi dir="ltr">Microservice</bdi> شروع کنیم. <bdi dir="ltr">Week 02</bdi> پاسخ می‌دهد که **مرزهای مدل کجا هستند، رابطهٔ آن‌ها چیست و چه کسی حق تصمیم‌گیری و تغییر هر <bdi dir="ltr">Fact</bdi> را دارد**.

این هفته هنوز طراحی <bdi dir="ltr">Microservice</bdi> یا تراکنش توزیع‌شده نیست. شش ماژول <bdi dir="ltr">Java</bdi> یک **فرضیهٔ اجرایی و قابل‌آزمون دربارهٔ مرزها** هستند؛ نه اثبات اینکه بانک باید دقیقاً شش سرویس مستقل داشته باشد.

## پیش‌نیاز واقعی

پیش از شروع، باید بتوانی بدون مراجعه به <bdi dir="ltr">Week 01</bdi> توضیح بدهی:

1. <bdi dir="ltr">Capability</bdi> با <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Application</bdi> و <bdi dir="ltr">API</bdi> یکی نیست.
2. <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Bounded Context</bdi>، <bdi dir="ltr">Module</bdi> و <bdi dir="ltr">Deployable Service</bdi> چهار مفهوم متفاوت‌اند.
3. <bdi dir="ltr">BIAN Service Domain</bdi> به‌طور خودکار <bdi dir="ltr">Microservice</bdi> نمی‌شود.
4. <bdi dir="ltr">Command</bdi> قصد انجام کار و <bdi dir="ltr">Event</bdi> واقعیت رخ‌داده را بیان می‌کند.

اگر <bdi dir="ltr">Exit Ticket</bdi> روز اول <bdi dir="ltr">Week 01</bdi> هنوز <bdi dir="ltr">Review</bdi> نشده است، می‌توانی محتوای این هفته را ببینی، اما <bdi dir="ltr">Gate</bdi> اسپرینت را انجام نده.

## قانون اجرای هفته

برای هر روز همین ترتیب را رعایت کن:

1. درس همان روز را یک‌بار پیوسته بخوان.
2. مثال هدایت‌شده را با کاغذ یا فایل بازسازی کن.
3. تمرین مستقل را در <bdi dir="ltr">Workbook</bdi> انجام بده.
4. درس را ببند و <bdi dir="ltr">Exit Ticket</bdi> را بدون مراجعه پاسخ بده.
5. فقط پس از <bdi dir="ltr">Review</bdi> استاد، <bdi dir="ltr">Artifact</bdi> را <bdi dir="ltr">`Accepted`</bdi> یا روز را <bdi dir="ltr">`Done`</bdi> اعلام کن.

پاسخ‌های مستقل را در [<bdi dir="ltr">Week 02 Workbook</bdi>](submissions/week-02-workbook.md) ثبت کن؛ پاسخ خام را بعد از <bdi dir="ltr">Review</bdi> پاک نکن.

## ترتیب دقیق روزها

| روز | زمان | درس | تمرین و شاهد پایان | آزمون خروج |
|---|---:|---|---|---|
| ۱ | ۵۰ دقیقه | [<bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Subdomain</bdi> و اهمیت راهبردی](lessons/day-01-domain-subdomain-strategy-fa.md) | [<bdi dir="ltr">Subdomain Matrix</bdi>](exercises/day-01-subdomain-matrix.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-01-exit-ticket.md) |
| ۲ | ۴۵ دقیقه | [<bdi dir="ltr">Bounded Context</bdi> و <bdi dir="ltr">Ubiquitous Language</bdi>](lessons/day-02-bounded-context-language-fa.md) | [<bdi dir="ltr">Language Conflicts</bdi>](exercises/day-02-language-conflicts.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-02-exit-ticket.md) |
| ۳ | ۵۰ دقیقه | [<bdi dir="ltr">Context Map</bdi> و الگوهای رابطه](lessons/day-03-context-map-patterns-fa.md) | [<bdi dir="ltr">Context Relations</bdi>](exercises/day-03-context-map.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-03-exit-ticket.md) |
| ۴ | ۵۰ دقیقه | [مالکیت داده و تصمیم](lessons/day-04-ownership-source-of-truth-fa.md) | [<bdi dir="ltr">Ownership Matrix v1</bdi>](exercises/day-04-ownership-matrix.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-04-exit-ticket.md) |
| ۵ | ۱۰۰ دقیقه | [تبدیل فرضیهٔ مرزها به <bdi dir="ltr">Spring Modulith</bdi>](lessons/day-05-spring-modulith-modules-fa.md) | [<bdi dir="ltr">Six-module Skeleton</bdi>](exercises/day-05-module-skeleton.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-05-exit-ticket.md) |
| ۶ | ۴۵ دقیقه | [<bdi dir="ltr">Architecture Fitness Test</bdi>](lessons/day-06-architecture-fitness-test-fa.md) | [<bdi dir="ltr">Module Verification</bdi>](exercises/day-06-module-verification.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-06-exit-ticket.md) |
| ۷ | ۲۰ دقیقه | [<bdi dir="ltr">Gate</bdi> اسپرینت اول](lessons/day-07-sprint-gate-defense-fa.md) | [دفاع مسدودی قضایی](exercises/day-07-sprint-gate.md) | <bdi dir="ltr">Rubric</bdi> داخل <bdi dir="ltr">Gate</bdi> |
| **جمع** | **۳۶۰ دقیقه** |  |  |  |

ریزبودجهٔ پیشنهادی: روزهای ۱ تا ۴ شامل ۲۰ تا ۲۵ دقیقه درس، ۱۵ تا ۲۰ دقیقه تمرین و ۵ دقیقه آزمون/مرجع‌اند؛ روز ۵ شامل ۲۰ دقیقه درس، ۷۵ دقیقه کدنویسی و ۵ دقیقه آزمون است؛ روز ۶ شامل ۱۰ دقیقه مرور، ۳۰ دقیقه <bdi dir="ltr">Verification</bdi> و ۵ دقیقه آزمون است. دفاع استاد پس از <bdi dir="ltr">Submission</bdi> جزو بودجهٔ خودخوان ۳۶۰ دقیقه‌ای حساب نشده است.

## مسیر افزودهٔ این هفته

هفت روز و <bdi dir="ltr">Gate</bdi> بالا همان برنامهٔ اصلی‌اند و هیچ بخشی از آن‌ها با جلسات زیر جایگزین نمی‌شود. پس از <bdi dir="ltr">Day 07</bdi>، دو جلسهٔ افزوده را انجام بده:

| جلسه | زمان | محتوا | تمرین و شاهد پایان | آزمون/دفاع |
|---|---:|---|---|---|
| ۸ | ۱۰۵ دقیقه | [<bdi dir="ltr">Clean Code</bdi> و <bdi dir="ltr">Strategy/Factory</bdi> روی <bdi dir="ltr">Transfer Fee</bdi>](lessons/day-08-clean-code-strategy-refactoring-fa.md) | [<bdi dir="ltr">Runnable Refactoring Lab</bdi>](exercises/day-08-transfer-fee-refactoring.md) + [<bdi dir="ltr">Code Review Checklist</bdi>](artifacts/day-08-code-review-checklist.md) | [<bdi dir="ltr">Exit Ticket</bdi>](quizzes/day-08-exit-ticket.md) |
| ۹ | ۴۵ دقیقه | [پروندهٔ <bdi dir="ltr">Monzo:</bdi> از <bdi dir="ltr">Mondo</bdi> تا بانک ۳۰۰۰+ <bdi dir="ltr">Microservice</bdi>](case-studies/week-02-monzo-fa.md) | [<bdi dir="ltr">Architecture Review</bdi>](exercises/day-09-monzo-architecture-review.md) | دفاع پنج‌سؤالی داخل پرونده |

<bdi dir="ltr">Session 08</bdi> یک <bdi dir="ltr">Baseline</bdi> اجرایی در <bdi dir="ltr">Test scope</bdi> دارد تا ابتدا رفتار را تثبیت و سپس <bdi dir="ltr">Refactor</bdi> کنی:


</div>

<div dir="ltr" align="left">

~~~text
backend/banking-modulith/src/test/java/
└── com/example/corebankinglab/craftsmanship/week02/
    ├── LegacyTransferFeeCalculator.java
    └── LegacyTransferFeeCalculatorCharacterizationTest.java
~~~

</div>

<div dir="rtl" align="right">


قواعد، بودجه و نقشهٔ این دو ریل برای همهٔ هفته‌های بعد در [الحاقیهٔ ثابت هفتگی](../../../docs/course/expanded-weekly-tracks.md) آمده است.

## خروجی‌های اجباری

### تحلیل و مدل

- [<bdi dir="ltr">Subdomain Matrix working draft</bdi>](artifacts/subdomain-matrix-working-draft.md)
- [<bdi dir="ltr">Language Conflicts working draft</bdi>](artifacts/language-conflicts-working-draft.md)
- [<bdi dir="ltr">Domain Map v1</bdi>](artifacts/domain-map-working-draft.md)
- [<bdi dir="ltr">Context Map v1</bdi>](artifacts/context-map-template.md)
- [<bdi dir="ltr">Data/Decision Ownership Matrix v1</bdi>](artifacts/ownership-matrix-template.md)
- شش [<bdi dir="ltr">Domain Dossier</bdi>](artifacts/domain-dossiers/README.md) اولیه

### کد و <bdi dir="ltr">Verification</bdi>

- شش <bdi dir="ltr">Application Module</bdi> منطقی: <bdi dir="ltr">`partycustomer`</bdi>، <bdi dir="ltr">`productagreement`</bdi>، <bdi dir="ltr">`deposits`</bdi>، <bdi dir="ltr">`lending`</bdi>، <bdi dir="ltr">`payments`</bdi> و <bdi dir="ltr">`accounting`</bdi>
- <bdi dir="ltr">API</bdi> آشکار و <bdi dir="ltr">Package</bdi> داخلی برای هر <bdi dir="ltr">Module</bdi>
- [<bdi dir="ltr">Dependency Policy</bdi>](artifacts/module-dependency-policy.md) با دلیل هر وابستگی
- <bdi dir="ltr">`ApplicationModules.verify()`</bdi> سبز
- یک آزمایش منفی برای <bdi dir="ltr">Cycle</bdi> یا دسترسی به <bdi dir="ltr">Internal</bdi> و ثبت شاهد شکست
- <bdi dir="ltr">Refactor</bdi> کاتای <bdi dir="ltr">Transfer Fee</bdi> از <bdi dir="ltr">Baseline</bdi> سبز با <bdi dir="ltr">Characterization Test</bdi>
- <bdi dir="ltr">Pattern Decision</bdi> برای <bdi dir="ltr">Strategy/Factory</bdi> و ثبت گزینهٔ ساده‌تر
- <bdi dir="ltr">Code Review</bdi> شامل <bdi dir="ltr">Complexity</bdi> اضافه‌شده و <bdi dir="ltr">Debt</bdi> باقی‌مانده

### دفاع و گزارش

- [<bdi dir="ltr">Sprint 01 Gate Evidence</bdi>](artifacts/sprint-01-gate-evidence-template.md)
- [<bdi dir="ltr">Week 02 Report</bdi>](artifacts/week-02-report-template.md)
- دفاع حداکثر ده‌دقیقه‌ای از <bdi dir="ltr">Boundary</bdi> و <bdi dir="ltr">Ownership</bdi>
- <bdi dir="ltr">Architecture Review</bdi> پروندهٔ <bdi dir="ltr">Monzo</bdi> با تفکیک <bdi dir="ltr">Fact</bdi>، <bdi dir="ltr">Inference</bdi> و <bdi dir="ltr">Unknown</bdi>

## <bdi dir="ltr">Definition of Done</bdi>

<bdi dir="ltr">Week 02</bdi> زمانی <bdi dir="ltr">Done</bdi> است که:

- هر <bdi dir="ltr">Subdomain</bdi> با شواهد و <bdi dir="ltr">Forces</bdi> طبقه‌بندی شده باشد؛ نه با سلیقه یا نام سامانه.
- برای اصطلاحات مهم، <bdi dir="ltr">Context</bdi> و معنای دقیق ثبت شده باشد.
- هر رابطه در <bdi dir="ltr">Context Map</bdi> جهت، <bdi dir="ltr">Pattern</bdi>، <bdi dir="ltr">Contract</bdi> و اثر شکست داشته باشد.
- برای هر <bdi dir="ltr">Fact</bdi> یا <bdi dir="ltr">Decision</bdi> دقیقاً یک <bdi dir="ltr">Authority</bdi> مشخص باشد.
- <bdi dir="ltr">Copy</bdi>، <bdi dir="ltr">Snapshot</bdi>، <bdi dir="ltr">Cache</bdi> و <bdi dir="ltr">Projection</bdi> با <bdi dir="ltr">Owner</bdi> اشتباه نشده باشند.
- هیچ <bdi dir="ltr">Module</bdi> از <bdi dir="ltr">Package</bdi> داخلی <bdi dir="ltr">Module</bdi> دیگر استفاده نکند.
- <bdi dir="ltr">Dependency</bdi>های مجاز صریح باشند و <bdi dir="ltr">Cycle</bdi> وجود نداشته باشد.
- <bdi dir="ltr">`mvn verify`</bdi> سبز باشد.
- <bdi dir="ltr">Gate</bdi> اسپرینت حداقل ۸ از ۱۰ بگیرد و هیچ <bdi dir="ltr">Critical Error</bdi> نداشته باشد.
- <bdi dir="ltr">Baseline</bdi> و نسخهٔ <bdi dir="ltr">Refactored</bdi> کاتای <bdi dir="ltr">Code Craft</bdi> هر دو تست سبز و <bdi dir="ltr">Edge Case</bdi> صریح داشته باشند.
- انتخاب یا رد <bdi dir="ltr">Strategy/Factory</bdi> با <bdi dir="ltr">Forces</bdi> و <bdi dir="ltr">Cost</bdi> دفاع شده باشد؛ صرف استفاده از <bdi dir="ltr">Pattern</bdi> کافی نیست.
- پروندهٔ <bdi dir="ltr">Monzo</bdi> خوانده و <bdi dir="ltr">Artifact</bdi> پنج‌سؤالی آن در <bdi dir="ltr">Workbook</bdi> ثبت شده باشد.

## <bdi dir="ltr">Critical Error</bdi>های این هفته

هرکدام از موارد زیر <bdi dir="ltr">Gate</bdi> را مستقل از جمع امتیاز متوقف می‌کند:

1. دو <bdi dir="ltr">Context</bdi> هم‌زمان <bdi dir="ltr">Owner</bdi> یک <bdi dir="ltr">Fact</bdi> با معنای یکسان معرفی شوند.
2. <bdi dir="ltr">Accounting</bdi> مالک ماندهٔ قابل برداشت یا <bdi dir="ltr">Hold</bdi> عملیاتی سپرده معرفی شود.
3. <bdi dir="ltr">Legal Orders</bdi> مجاز به <bdi dir="ltr">Update</bdi> مستقیم <bdi dir="ltr">Hold</bdi> یا ماندهٔ <bdi dir="ltr">Deposits</bdi> باشد.
4. وجود جدول، <bdi dir="ltr">API</bdi>، تیم یا <bdi dir="ltr">BIAN Service Domain</bdi> به‌تنهایی دلیل <bdi dir="ltr">Boundary</bdi> دانسته شود.
5. دسترسی مستقیم به <bdi dir="ltr">Package</bdi> داخلی یا دیتابیس مشترک به‌عنوان <bdi dir="ltr">Contract</bdi> پذیرفته شود.
6. <bdi dir="ltr">Context Map</bdi> فقط چند خط بدون جهت، <bdi dir="ltr">Pattern</bdi> و <bdi dir="ltr">Contract</bdi> باشد.

## خارج از محدوده

این موارد عمداً به هفته‌های بعد موکول شده‌اند:

- طراحی <bdi dir="ltr">Aggregate</bdi> و <bdi dir="ltr">Invariant</bdi>های کامل <bdi dir="ltr">Deposits</bdi>
- <bdi dir="ltr">Hexagonal Architecture</bdi> و <bdi dir="ltr">Port/Adapter</bdi>های <bdi dir="ltr">Lending</bdi>
- انتخاب <bdi dir="ltr">REST</bdi> در برابر <bdi dir="ltr">Kafka</bdi>
- <bdi dir="ltr">Saga</bdi>، <bdi dir="ltr">Outbox</bdi>، <bdi dir="ltr">Exactly-once</bdi> و <bdi dir="ltr">Reconciliation</bdi>
- طراحی فیزیکی جدول، <bdi dir="ltr">Partitioning</bdi> و <bdi dir="ltr">Locking</bdi>
- سند حسابداری دقیق هر رویداد

در <bdi dir="ltr">Week 02</bdi> فقط به‌اندازه‌ای از این موضوعات حرف می‌زنیم که <bdi dir="ltr">Boundary</bdi> و <bdi dir="ltr">Ownership</bdi> قابل دفاع شوند.

## منابع

مسیر مطالعهٔ محدود و هدفمند در [<bdi dir="ltr">References</bdi>](references/README.md) آمده است. خواندن کل کتاب <bdi dir="ltr">DDD</bdi> یا تمام مستند <bdi dir="ltr">Spring Modulith</bdi> پیش‌نیاز نیست.

</div>
