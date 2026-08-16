<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Week 02</span> — <span dir="ltr">Strategic DDD</span> و مالکیت

- <span dir="ltr">Status:</span> **<span dir="ltr">Ready</span>**
- <span dir="ltr">Core time budget:</span> **<span dir="ltr">360 minutes</span> — <span dir="ltr">unchanged</span>**
- <span dir="ltr">Expansion budget:</span> **<span dir="ltr">150 minutes</span> — <span dir="ltr">105 Code Craft</span> + <span dir="ltr">45 Case File</span>**
- <span dir="ltr">Full expanded budget:</span> **<span dir="ltr">510 minutes</span>**
- <span dir="ltr">Banking lens:</span> اعطای تسهیلات، واریز به سپرده و مسدودی قضایی
- <span dir="ltr">Main question:</span> هر مدل، داده و تصمیم در کدام <span dir="ltr">Bounded Context</span> معنا و مالک دارد؟
- <span dir="ltr">Technical outcome:</span> شش <span dir="ltr">Application Module</span> قابل <span dir="ltr">Verification</span> در <span dir="ltr">Spring Modulith</span>

![برنامهٔ دقیق هفتهٔ دوم](week-02-plan.svg)

## چرا این هفته وجود دارد؟

در <span dir="ltr">Week 01</span> یاد گرفتیم از <span dir="ltr">Capability</span> و مسئلهٔ کسب‌وکاری به <span dir="ltr">Contract</span> برسیم و نباید از جدول، سامانه یا <span dir="ltr">Microservice</span> شروع کنیم. <span dir="ltr">Week 02</span> پاسخ می‌دهد که **مرزهای مدل کجا هستند، رابطهٔ آن‌ها چیست و چه کسی حق تصمیم‌گیری و تغییر هر <span dir="ltr">Fact</span> را دارد**.

این هفته هنوز طراحی <span dir="ltr">Microservice</span> یا تراکنش توزیع‌شده نیست. شش ماژول <span dir="ltr">Java</span> یک **فرضیهٔ اجرایی و قابل‌آزمون دربارهٔ مرزها** هستند؛ نه اثبات اینکه بانک باید دقیقاً شش سرویس مستقل داشته باشد.

## پیش‌نیاز واقعی

پیش از شروع، باید بتوانی بدون مراجعه به <span dir="ltr">Week 01</span> توضیح بدهی:

1. <span dir="ltr">Capability</span> با <span dir="ltr">Process</span>، <span dir="ltr">Application</span> و <span dir="ltr">API</span> یکی نیست.
2. <span dir="ltr">Domain</span>، <span dir="ltr">Bounded Context</span>، <span dir="ltr">Module</span> و <span dir="ltr">Deployable Service</span> چهار مفهوم متفاوت‌اند.
3. <span dir="ltr">BIAN Service Domain</span> به‌طور خودکار <span dir="ltr">Microservice</span> نمی‌شود.
4. <span dir="ltr">Command</span> قصد انجام کار و <span dir="ltr">Event</span> واقعیت رخ‌داده را بیان می‌کند.

اگر <span dir="ltr">Exit Ticket</span> روز اول <span dir="ltr">Week 01</span> هنوز <span dir="ltr">Review</span> نشده است، می‌توانی محتوای این هفته را ببینی، اما <span dir="ltr">Gate</span> اسپرینت را انجام نده.

## قانون اجرای هفته

برای هر روز همین ترتیب را رعایت کن:

1. درس همان روز را یک‌بار پیوسته بخوان.
2. مثال هدایت‌شده را با کاغذ یا فایل بازسازی کن.
3. تمرین مستقل را در <span dir="ltr">Workbook</span> انجام بده.
4. درس را ببند و <span dir="ltr">Exit Ticket</span> را بدون مراجعه پاسخ بده.
5. فقط پس از <span dir="ltr">Review</span> استاد، <span dir="ltr">Artifact</span> را <span dir="ltr">`Accepted`</span> یا روز را <span dir="ltr">`Done`</span> اعلام کن.

پاسخ‌های مستقل را در [<span dir="ltr">Week 02 Workbook</span>](submissions/week-02-workbook.md) ثبت کن؛ پاسخ خام را بعد از <span dir="ltr">Review</span> پاک نکن.

## ترتیب دقیق روزها

| روز | زمان | درس | تمرین و شاهد پایان | آزمون خروج |
|---|---:|---|---|---|
| ۱ | ۵۰ دقیقه | [<span dir="ltr">Domain</span>، <span dir="ltr">Subdomain</span> و اهمیت راهبردی](lessons/day-01-domain-subdomain-strategy-fa.md) | [<span dir="ltr">Subdomain Matrix</span>](exercises/day-01-subdomain-matrix.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-01-exit-ticket.md) |
| ۲ | ۴۵ دقیقه | [<span dir="ltr">Bounded Context</span> و <span dir="ltr">Ubiquitous Language</span>](lessons/day-02-bounded-context-language-fa.md) | [<span dir="ltr">Language Conflicts</span>](exercises/day-02-language-conflicts.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-02-exit-ticket.md) |
| ۳ | ۵۰ دقیقه | [<span dir="ltr">Context Map</span> و الگوهای رابطه](lessons/day-03-context-map-patterns-fa.md) | [<span dir="ltr">Context Relations</span>](exercises/day-03-context-map.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-03-exit-ticket.md) |
| ۴ | ۵۰ دقیقه | [مالکیت داده و تصمیم](lessons/day-04-ownership-source-of-truth-fa.md) | [<span dir="ltr">Ownership Matrix v1</span>](exercises/day-04-ownership-matrix.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-04-exit-ticket.md) |
| ۵ | ۱۰۰ دقیقه | [تبدیل فرضیهٔ مرزها به <span dir="ltr">Spring Modulith</span>](lessons/day-05-spring-modulith-modules-fa.md) | [<span dir="ltr">Six-module Skeleton</span>](exercises/day-05-module-skeleton.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-05-exit-ticket.md) |
| ۶ | ۴۵ دقیقه | [<span dir="ltr">Architecture Fitness Test</span>](lessons/day-06-architecture-fitness-test-fa.md) | [<span dir="ltr">Module Verification</span>](exercises/day-06-module-verification.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-06-exit-ticket.md) |
| ۷ | ۲۰ دقیقه | [<span dir="ltr">Gate</span> اسپرینت اول](lessons/day-07-sprint-gate-defense-fa.md) | [دفاع مسدودی قضایی](exercises/day-07-sprint-gate.md) | <span dir="ltr">Rubric</span> داخل <span dir="ltr">Gate</span> |
| **جمع** | **۳۶۰ دقیقه** |  |  |  |

ریزبودجهٔ پیشنهادی: روزهای ۱ تا ۴ شامل ۲۰ تا ۲۵ دقیقه درس، ۱۵ تا ۲۰ دقیقه تمرین و ۵ دقیقه آزمون/مرجع‌اند؛ روز ۵ شامل ۲۰ دقیقه درس، ۷۵ دقیقه کدنویسی و ۵ دقیقه آزمون است؛ روز ۶ شامل ۱۰ دقیقه مرور، ۳۰ دقیقه <span dir="ltr">Verification</span> و ۵ دقیقه آزمون است. دفاع استاد پس از <span dir="ltr">Submission</span> جزو بودجهٔ خودخوان ۳۶۰ دقیقه‌ای حساب نشده است.

## مسیر افزودهٔ این هفته

هفت روز و <span dir="ltr">Gate</span> بالا همان برنامهٔ اصلی‌اند و هیچ بخشی از آن‌ها با جلسات زیر جایگزین نمی‌شود. پس از <span dir="ltr">Day 07</span>، دو جلسهٔ افزوده را انجام بده:

| جلسه | زمان | محتوا | تمرین و شاهد پایان | آزمون/دفاع |
|---|---:|---|---|---|
| ۸ | ۱۰۵ دقیقه | [<span dir="ltr">Clean Code</span> و <span dir="ltr">Strategy/Factory</span> روی <span dir="ltr">Transfer Fee</span>](lessons/day-08-clean-code-strategy-refactoring-fa.md) | [<span dir="ltr">Runnable Refactoring Lab</span>](exercises/day-08-transfer-fee-refactoring.md) + [<span dir="ltr">Code Review Checklist</span>](artifacts/day-08-code-review-checklist.md) | [<span dir="ltr">Exit Ticket</span>](quizzes/day-08-exit-ticket.md) |
| ۹ | ۴۵ دقیقه | [پروندهٔ <span dir="ltr">Monzo:</span> از <span dir="ltr">Mondo</span> تا بانک ۳۰۰۰+ <span dir="ltr">Microservice</span>](case-studies/week-02-monzo-fa.md) | [<span dir="ltr">Architecture Review</span>](exercises/day-09-monzo-architecture-review.md) | دفاع پنج‌سؤالی داخل پرونده |

<span dir="ltr">Session 08</span> یک <span dir="ltr">Baseline</span> اجرایی در <span dir="ltr">Test scope</span> دارد تا ابتدا رفتار را تثبیت و سپس <span dir="ltr">Refactor</span> کنی:


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

- [<span dir="ltr">Subdomain Matrix working draft</span>](artifacts/subdomain-matrix-working-draft.md)
- [<span dir="ltr">Language Conflicts working draft</span>](artifacts/language-conflicts-working-draft.md)
- [<span dir="ltr">Domain Map v1</span>](artifacts/domain-map-working-draft.md)
- [<span dir="ltr">Context Map v1</span>](artifacts/context-map-template.md)
- [<span dir="ltr">Data/Decision Ownership Matrix v1</span>](artifacts/ownership-matrix-template.md)
- شش [<span dir="ltr">Domain Dossier</span>](artifacts/domain-dossiers/README.md) اولیه

### کد و <span dir="ltr">Verification</span>

- شش <span dir="ltr">Application Module</span> منطقی: <span dir="ltr">`partycustomer`</span>، <span dir="ltr">`productagreement`</span>، <span dir="ltr">`deposits`</span>، <span dir="ltr">`lending`</span>، <span dir="ltr">`payments`</span> و <span dir="ltr">`accounting`</span>
- <span dir="ltr">API</span> آشکار و <span dir="ltr">Package</span> داخلی برای هر <span dir="ltr">Module</span>
- [<span dir="ltr">Dependency Policy</span>](artifacts/module-dependency-policy.md) با دلیل هر وابستگی
- <span dir="ltr">`ApplicationModules.verify()`</span> سبز
- یک آزمایش منفی برای <span dir="ltr">Cycle</span> یا دسترسی به <span dir="ltr">Internal</span> و ثبت شاهد شکست
- <span dir="ltr">Refactor</span> کاتای <span dir="ltr">Transfer Fee</span> از <span dir="ltr">Baseline</span> سبز با <span dir="ltr">Characterization Test</span>
- <span dir="ltr">Pattern Decision</span> برای <span dir="ltr">Strategy/Factory</span> و ثبت گزینهٔ ساده‌تر
- <span dir="ltr">Code Review</span> شامل <span dir="ltr">Complexity</span> اضافه‌شده و <span dir="ltr">Debt</span> باقی‌مانده

### دفاع و گزارش

- [<span dir="ltr">Sprint 01 Gate Evidence</span>](artifacts/sprint-01-gate-evidence-template.md)
- [<span dir="ltr">Week 02 Report</span>](artifacts/week-02-report-template.md)
- دفاع حداکثر ده‌دقیقه‌ای از <span dir="ltr">Boundary</span> و <span dir="ltr">Ownership</span>
- <span dir="ltr">Architecture Review</span> پروندهٔ <span dir="ltr">Monzo</span> با تفکیک <span dir="ltr">Fact</span>، <span dir="ltr">Inference</span> و <span dir="ltr">Unknown</span>

## <span dir="ltr">Definition of Done</span>

<span dir="ltr">Week 02</span> زمانی <span dir="ltr">Done</span> است که:

- هر <span dir="ltr">Subdomain</span> با شواهد و <span dir="ltr">Forces</span> طبقه‌بندی شده باشد؛ نه با سلیقه یا نام سامانه.
- برای اصطلاحات مهم، <span dir="ltr">Context</span> و معنای دقیق ثبت شده باشد.
- هر رابطه در <span dir="ltr">Context Map</span> جهت، <span dir="ltr">Pattern</span>، <span dir="ltr">Contract</span> و اثر شکست داشته باشد.
- برای هر <span dir="ltr">Fact</span> یا <span dir="ltr">Decision</span> دقیقاً یک <span dir="ltr">Authority</span> مشخص باشد.
- <span dir="ltr">Copy</span>، <span dir="ltr">Snapshot</span>، <span dir="ltr">Cache</span> و <span dir="ltr">Projection</span> با <span dir="ltr">Owner</span> اشتباه نشده باشند.
- هیچ <span dir="ltr">Module</span> از <span dir="ltr">Package</span> داخلی <span dir="ltr">Module</span> دیگر استفاده نکند.
- <span dir="ltr">Dependency</span>های مجاز صریح باشند و <span dir="ltr">Cycle</span> وجود نداشته باشد.
- <span dir="ltr">`mvn verify`</span> سبز باشد.
- <span dir="ltr">Gate</span> اسپرینت حداقل ۸ از ۱۰ بگیرد و هیچ <span dir="ltr">Critical Error</span> نداشته باشد.
- <span dir="ltr">Baseline</span> و نسخهٔ <span dir="ltr">Refactored</span> کاتای <span dir="ltr">Code Craft</span> هر دو تست سبز و <span dir="ltr">Edge Case</span> صریح داشته باشند.
- انتخاب یا رد <span dir="ltr">Strategy/Factory</span> با <span dir="ltr">Forces</span> و <span dir="ltr">Cost</span> دفاع شده باشد؛ صرف استفاده از <span dir="ltr">Pattern</span> کافی نیست.
- پروندهٔ <span dir="ltr">Monzo</span> خوانده و <span dir="ltr">Artifact</span> پنج‌سؤالی آن در <span dir="ltr">Workbook</span> ثبت شده باشد.

## <span dir="ltr">Critical Error</span>های این هفته

هرکدام از موارد زیر <span dir="ltr">Gate</span> را مستقل از جمع امتیاز متوقف می‌کند:

1. دو <span dir="ltr">Context</span> هم‌زمان <span dir="ltr">Owner</span> یک <span dir="ltr">Fact</span> با معنای یکسان معرفی شوند.
2. <span dir="ltr">Accounting</span> مالک ماندهٔ قابل برداشت یا <span dir="ltr">Hold</span> عملیاتی سپرده معرفی شود.
3. <span dir="ltr">Legal Orders</span> مجاز به <span dir="ltr">Update</span> مستقیم <span dir="ltr">Hold</span> یا ماندهٔ <span dir="ltr">Deposits</span> باشد.
4. وجود جدول، <span dir="ltr">API</span>، تیم یا <span dir="ltr">BIAN Service Domain</span> به‌تنهایی دلیل <span dir="ltr">Boundary</span> دانسته شود.
5. دسترسی مستقیم به <span dir="ltr">Package</span> داخلی یا دیتابیس مشترک به‌عنوان <span dir="ltr">Contract</span> پذیرفته شود.
6. <span dir="ltr">Context Map</span> فقط چند خط بدون جهت، <span dir="ltr">Pattern</span> و <span dir="ltr">Contract</span> باشد.

## خارج از محدوده

این موارد عمداً به هفته‌های بعد موکول شده‌اند:

- طراحی <span dir="ltr">Aggregate</span> و <span dir="ltr">Invariant</span>های کامل <span dir="ltr">Deposits</span>
- <span dir="ltr">Hexagonal Architecture</span> و <span dir="ltr">Port/Adapter</span>های <span dir="ltr">Lending</span>
- انتخاب <span dir="ltr">REST</span> در برابر <span dir="ltr">Kafka</span>
- <span dir="ltr">Saga</span>، <span dir="ltr">Outbox</span>، <span dir="ltr">Exactly-once</span> و <span dir="ltr">Reconciliation</span>
- طراحی فیزیکی جدول، <span dir="ltr">Partitioning</span> و <span dir="ltr">Locking</span>
- سند حسابداری دقیق هر رویداد

در <span dir="ltr">Week 02</span> فقط به‌اندازه‌ای از این موضوعات حرف می‌زنیم که <span dir="ltr">Boundary</span> و <span dir="ltr">Ownership</span> قابل دفاع شوند.

## منابع

مسیر مطالعهٔ محدود و هدفمند در [<span dir="ltr">References</span>](references/README.md) آمده است. خواندن کل کتاب <span dir="ltr">DDD</span> یا تمام مستند <span dir="ltr">Spring Modulith</span> پیش‌نیاز نیست.

</div>
