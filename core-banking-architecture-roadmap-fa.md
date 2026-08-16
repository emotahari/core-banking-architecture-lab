<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# نقشهٔ راه نهایی ۲۴ هفته‌ای معماری نرم‌افزار و <span dir="ltr">Core Banking</span>

نسخه: ۱٫۰  
تاریخ مبنا: ۱۲ مرداد ۱۴۰۵ / ۳ اوت ۲۰۲۶  
مخاطب: مسیر شخصی‌سازی‌شدهٔ معماری <span dir="ltr">Core Banking</span>  
مدت: ۲۴ هفته، ۱۲ اسپرینت دوهفته‌ای، هفته‌ای ۴ تا ۶ ساعت

> الحاقیهٔ ۲۴ مرداد ۱۴۰۵ / ۱۵ اوت ۲۰۲۶: از <span dir="ltr">Week 02</span> دو ریل <span dir="ltr">Code Craft</span> و <span dir="ltr">Core Banking Case File</span> به برنامه افزوده شده‌اند. برنامهٔ ۴ تا ۶ ساعتهٔ قبلی «ریل اصلی» باقی می‌ماند و نسخهٔ کامل توسعه‌یافته ۵۱۰ دقیقه در هفته است؛ هیچ سرفصل، <span dir="ltr">Gate</span> یا <span dir="ltr">Artifact</span> قبلی حذف یا فشرده نشده است.

## ۱. تصمیم نهایی برنامه

این برنامه یک دورهٔ واحد با دو محور هم‌زمان است:

- محور فنی: طراحی کد، معماری سرویس، معماری توزیع‌شده، داده و تراکنش، معماری اجرایی و سازمانی
- محور دامینی: شناخت <span dir="ltr">Core Banking</span>، مرزبندی دامین‌ها، مالکیت داده و تصمیم، سرویس‌ها و روابط میان آن‌ها

پروژهٔ ثابت دوره یک <span dir="ltr">Core Banking</span> آموزشی با شش دامین اصلی است:

1. <span dir="ltr">Party</span> & <span dir="ltr">Customer</span>
2. <span dir="ltr">Product</span> & <span dir="ltr">Agreement</span>
3. <span dir="ltr">Deposits</span>
4. <span dir="ltr">Lending</span>
5. <span dir="ltr">Payments</span>
6. <span dir="ltr">Accounting</span>

سه برش عمودی پروژه واقعاً پیاده‌سازی، تست و دفاع می‌شوند:

1. اعطای تسهیلات و واریز مبلغ به سپرده
2. انتقال وجه بین‌شعبه‌ای
3. شکست سپردهٔ بلندمدت و اصلاح سود

هدف ساخت یک <span dir="ltr">Core Banking</span> کامل تولیدی در ۲۴ هفته نیست. هدف، ساخت معماری کامل و پیاده‌سازی سه جریان باریک اما انتها‌به‌انتهاست؛ به‌اندازه‌ای که بتوان صحت مرزها، تراکنش‌ها، <span dir="ltr">Event</span>ها، حسابداری، شکست‌ها و الزامات اجرایی را اثبات کرد.

## ۲. نتیجه‌ای که در پایان باید حاصل شود

در پایان هفتهٔ ۲۴ باید بتوانی:

- زنجیرهٔ <span dir="ltr">`Capability → Domain → Subdomain → Bounded Context → Module/Service → API/Event`</span> را برای یک قابلیت بانکی طی کنی.
- برای هر تصمیم و داده یک مالک صریح تعیین کنی و مشخص کنی چه دامین‌هایی نباید مالک آن باشند.
- میان <span dir="ltr">Modular Monolith</span> و <span dir="ltr">Microservice</span> با معیارهای تغییر، تراکنش، تیم، استقرار، مقیاس و ریسک انتخاب کنی.
- <span dir="ltr">Aggregate</span>، <span dir="ltr">Invariant</span> و <span dir="ltr">Transaction Boundary</span> را در کد <span dir="ltr">Java/Spring</span> پیاده‌سازی و آزمون کنی.
- <span dir="ltr">API</span> همگام و قرارداد <span dir="ltr">Event</span> را همراه با <span dir="ltr">Idempotency</span>، <span dir="ltr">Versioning</span> و <span dir="ltr">Error Model</span> طراحی کنی.
- <span dir="ltr">Outbox</span>، <span dir="ltr">Inbox</span>، <span dir="ltr">Kafka</span>، <span dir="ltr">Saga/Process Manager</span>، <span dir="ltr">Retry</span>، <span dir="ltr">Timeout</span>، <span dir="ltr">Compensation</span>، <span dir="ltr">Reversal</span> و <span dir="ltr">Reconciliation</span> را در یک جریان مالی به‌درستی به‌کار ببری.
- ماندهٔ عملیاتی، <span dir="ltr">Ledger</span>، <span dir="ltr">Subledger</span> و <span dir="ltr">GL</span> را از هم تفکیک کنی.
- مدل دادهٔ <span dir="ltr">Oracle</span> و <span dir="ltr">PostgreSQL</span> را براساس <span dir="ltr">Query Pattern</span>، <span dir="ltr">Locking</span>، <span dir="ltr">Partitioning</span>، <span dir="ltr">Indexing</span> و <span dir="ltr">Retention</span> طراحی کنی.
- برای سرویس حیاتی <span dir="ltr">SLI/SLO</span>، <span dir="ltr">Trace</span>، <span dir="ltr">Metric</span>، <span dir="ltr">Log</span>، <span dir="ltr">Runbook</span>، <span dir="ltr">RTO/RPO</span> و مالک <span dir="ltr">Build/Run</span> تعیین کنی.
- معماری را در برابر محصول، توسعه، زیرساخت، عملیات و حسابداری با <span dir="ltr">ADR</span> و شواهد اجرایی دفاع کنی.

## ۳. پنج لایهٔ فنی و جای قطعی آن‌ها

| لایه | پوشش اصلی | تمرین مستمر | شاهد نهایی |
|---|---|---|---|
| ۱. طراحی کد | هفته‌های ۱ تا ۶ | <span dir="ltr">Refactoring</span>، <span dir="ltr">Unit Test</span> و <span dir="ltr">Code Review</span> در تمام ۲۴ هفته | <span dir="ltr">Domain Model</span> تمیز، <span dir="ltr">Pattern</span>های موجه، تست‌های قواعد و <span dir="ltr">Architecture Test</span> |
| ۲. معماری سرویس | هفته‌های ۲ تا ۶ و ۹ | بازبینی <span dir="ltr">Boundary</span> در هر <span dir="ltr">ADR</span> و هر <span dir="ltr">API/Event</span> | <span dir="ltr">Modular Monolith</span> معتبر، <span dir="ltr">Service Candidate Map</span> و تصمیم‌های استخراج |
| ۳. معماری توزیع‌شده | هفته‌های ۹ تا ۱۲ و ۲۳ | تست <span dir="ltr">Duplicate</span>، <span dir="ltr">Out-of-order</span> و <span dir="ltr">Failure</span> در جریان‌های بعدی | <span dir="ltr">Outbox/Inbox</span>، <span dir="ltr">Kafka</span>، <span dir="ltr">Process Manager</span>، <span dir="ltr">Failure Matrix</span> و سه جریان <span dir="ltr">E2E</span> |
| ۴. داده و تراکنش | هفته‌های ۷، ۸ و ۱۳ تا ۱۶ | بررسی مالکیت و <span dir="ltr">Consistency</span> در همهٔ دامین‌ها | مدل <span dir="ltr">Oracle/PostgreSQL</span>، <span dir="ltr">Ledger/Subledger</span>، <span dir="ltr">CQRS</span>، <span dir="ltr">Locking</span> و <span dir="ltr">Performance Test</span> |
| ۵. معماری اجرایی و سازمانی | هفته‌های ۵، ۶، ۱۲ و ۲۱ تا ۲۴ | <span dir="ltr">Security</span>، <span dir="ltr">Observability</span> و <span dir="ltr">Ownership</span> از میانهٔ دوره | <span dir="ltr">IAM</span>، <span dir="ltr">Micro-frontend</span>، <span dir="ltr">Kubernetes</span>، <span dir="ltr">SLO/DR</span>، <span dir="ltr">Team/Service Ownership</span> و <span dir="ltr">Migration Roadmap</span> |

محور دامین بانکی در همهٔ هفته‌ها فعال است؛ موضوعات فنی هیچ‌گاه روی مثال فروشگاه یا سفارش عمومی تمرین نمی‌شوند.

## ۴. اصلاحات قطعی نسبت به نسخهٔ قبلی

1. کدنویسی، تست و <span dir="ltr">Refactoring</span> یک ریل دائمی است، نه موضوع دو هفتهٔ خاص.
2. <span dir="ltr">PostgreSQL</span> به‌صورت عملی استفاده می‌شود و <span dir="ltr">Oracle</span> به‌صورت مقایسه‌ای و در طراحی فیزیکی عمیق می‌شود.
3. <span dir="ltr">CQRS</span> فقط یک اصطلاح یا <span dir="ltr">Projection</span> ساده نیست؛ <span dir="ltr">Command Model</span>، <span dir="ltr">Read Model</span>، <span dir="ltr">Lag</span>، <span dir="ltr">Rebuild</span> و <span dir="ltr">Reconciliation</span> پیاده می‌شوند.
4. <span dir="ltr">IAM</span> از هفتهٔ ۶، <span dir="ltr">Observability</span> از هفتهٔ ۱۲ و <span dir="ltr">SLO</span> از هفتهٔ ۲۲ وارد می‌شوند؛ همگی در یک هفته فشرده نشده‌اند.
5. <span dir="ltr">Micro-frontend</span> یک تمرین مستقل در هفتهٔ ۲۱ دارد و با نیاز «افزودن <span dir="ltr">Widget</span> توسط سامانه‌ها و تکنولوژی‌های مختلف» طراحی می‌شود.
6. <span dir="ltr">BIAN</span> فهرست آمادهٔ <span dir="ltr">Microservice</span> نیست؛ برای کنترل پوشش <span dir="ltr">Capability</span>ها و زبان مشترک استفاده می‌شود.
7. ابتدا <span dir="ltr">Modular Monolith</span> ساخته می‌شود؛ استخراج سرویس فقط پس از مشاهدهٔ مرز، وابستگی و نیاز استقرار مستقل انجام می‌گیرد.
8. سه سناریوی نهایی از ابتدا ثابت می‌مانند تا همهٔ موضوعات روی یک پروژه انباشته شوند.

## ۵. سطح هدف و حدود برنامه

این برنامه برای سطح فعلی تو طراحی شده است: تجربهٔ طولانی تحلیل و طراحی سامانه‌های بانکی، مدیریت محصول و توسعه، و آشنایی عملی با <span dir="ltr">Java</span>، <span dir="ltr">Spring</span>، <span dir="ltr">Oracle</span>، <span dir="ltr">DB2</span>، <span dir="ltr">Kafka</span> و <span dir="ltr">Docker.</span> بنابراین آموزش <span dir="ltr">Syntax</span> جاوا، <span dir="ltr">CRUD</span> مقدماتی یا مبانی عمومی بانکداری در آن جایی ندارد.

در ۹۶ تا ۱۴۴ ساعت، خروجی واقع‌بینانه «معمار راهکار بانکیِ قادر به طراحی و نمونه‌سازی» است؛ نه <span dir="ltr">DBA</span> اوراکل، مدیر <span dir="ltr">Kubernetes</span>، متخصص امنیت یا توسعه‌دهندهٔ ارشد <span dir="ltr">Frontend.</span> در موضوعات تخصصی، باید بتوانی تصمیم درست بگیری، سؤال درست بپرسی و طرح را اعتبارسنجی کنی؛ تسلط عملی عمیق هر تخصص یک مسیر مستقل است.

## ۶. ریتم اجرایی هر هفته

### برنامهٔ استاندارد شش‌ساعته

| فعالیت | زمان |
|---|---:|
| مطالعهٔ هدایت‌شده و بحث مفهومی | ۹۰ دقیقه |
| تحلیل دامین و ترسیم مدل | ۷۵ دقیقه |
| کدنویسی و تست | ۱۳۵ دقیقه |
| <span dir="ltr">Failure/Performance/Security Exercise</span> | ۳۰ دقیقه |
| تکمیل <span dir="ltr">ADR</span>، <span dir="ltr">Catalog</span> یا پروندهٔ دامین | ۳۰ دقیقه |

### نسخهٔ حداقلی چهارساعته

| فعالیت | زمان |
|---|---:|
| مفهوم و منبع اصلی | ۶۰ دقیقه |
| تحلیل دامین | ۴۵ دقیقه |
| کدنویسی و تست | ۱۰۵ دقیقه |
| مستندسازی و دفاع کوتاه | ۳۰ دقیقه |

اگر یک هفته فقط چهار ساعت زمان وجود داشت، دامنهٔ پیاده‌سازی کوچک می‌شود؛ تست، خروجی و <span dir="ltr">Gate</span> حذف نمی‌شوند.

### چرخهٔ ثابت کار

1. یادگیری مفهوم روی یک مسئلهٔ بانکی مشخص
2. مدل‌سازی و تصمیم معماری
3. پیاده‌سازی یک <span dir="ltr">Vertical Slice</span> کوچک
4. شکستن عمدی راه‌حل با تست شکست یا هم‌زمانی
5. <span dir="ltr">Refactor</span>، ثبت <span dir="ltr">ADR</span> و دفاع ده‌دقیقه‌ای

### دو ریل افزوده از <span dir="ltr">Week 01</span>

پس از تکمیل چرخهٔ اصلی، هر هفته دو جلسهٔ مستقل اجرا می‌شود:

| ریل افزوده | زمان | خروجی |
|---|---:|---|
| <span dir="ltr">Code Craft Lab</span> | ۱۰۵ دقیقه | <span dir="ltr">Baseline</span>، <span dir="ltr">Smell Map</span>، <span dir="ltr">Characterization Test</span>، <span dir="ltr">Refactor</span>، <span dir="ltr">Pattern Decision</span>، <span dir="ltr">Edge Test</span> و <span dir="ltr">Self-review</span> |
| <span dir="ltr">Core Banking Case File</span> | ۴۵ دقیقه | <span dir="ltr">Timeline</span>، معماری/فناوری جاری، <span dir="ltr">Domain hypothesis</span>، شکست‌ها، دستاورد تازه و درس انتقالی |

نقشهٔ <span dir="ltr">Pattern</span>ها و پرونده‌های پیشنهادی <span dir="ltr">Week 01</span> تا <span dir="ltr">Week 24</span> در [الحاقیهٔ ثابت هفتگی](docs/course/expanded-weekly-tracks.md) نگهداری می‌شود. موضوع هر پرونده هنگام شروع هفته با منابع جاری دوباره کنترل خواهد شد.

## ۷. <span dir="ltr">Definition of Done</span> هفتگی

هیچ هفته‌ای صرفاً با «خواندن مطالب» تمام‌شده محسوب نمی‌شود. خروجی هفتگی باید شرایط زیر را داشته باشد:

- <span dir="ltr">Artifact</span> یا کد در <span dir="ltr">Git</span> ثبت و با شمارهٔ هفته <span dir="ltr">Tag</span> شده باشد.
- <span dir="ltr">`mvn verify`</span> موفق باشد.
- قواعد دامینی جدید <span dir="ltr">Unit Test</span> داشته باشند.
- مرزهای جدید <span dir="ltr">Architecture Test</span> یا <span dir="ltr">Module Verification</span> داشته باشند.
- تغییر قرارداد با <span dir="ltr">OpenAPI</span> یا <span dir="ltr">AsyncAPI</span> ثبت شده باشد.
- دست‌کم یک مسیر منفی، <span dir="ltr">Failure</span> یا <span dir="ltr">Edge Case</span> آزموده شده باشد.
- تصمیم غیر بدیهی در <span dir="ltr">ADR</span> ثبت شده باشد.
- بتوانی در ده دقیقه توضیح بدهی: مالک داده کیست، مرز تراکنش کجاست و در شکست چه رخ می‌دهد.

در هفته‌هایی که یک مورد موضوعیت ندارد، در گزارش هفته با عبارت <span dir="ltr">`Not Applicable`</span> و دلیل صریح ثبت می‌شود؛ خالی گذاشته نمی‌شود.

### قرارداد مستندسازی

- <span dir="ltr">Capability Map</span> برای سلسله‌مراتب قابلیت‌ها
- <span dir="ltr">Context Map</span> برای رابطهٔ دامین‌ها
- <span dir="ltr">C4 System/Container/Component</span> برای معماری ایستا
- <span dir="ltr">Sequence Diagram</span> برای جریان بین سرویس‌ها
- <span dir="ltr">State Machine</span> برای چرخهٔ عمر و <span dir="ltr">Process Manager</span>
- <span dir="ltr">ERD</span> برای مدل داده
- <span dir="ltr">ADR</span> با قالب ثابت: <span dir="ltr">Context</span>، <span dir="ltr">Forces</span>، <span dir="ltr">Options</span>، <span dir="ltr">Decision</span>، <span dir="ltr">Consequences</span>، <span dir="ltr">Verification</span> و <span dir="ltr">Revisit Trigger</span>

هر <span dir="ltr">Diagram</span> باید <span dir="ltr">Version</span>، <span dir="ltr">Scope</span> و مالک اجزای اصلی را نشان دهد. <span dir="ltr">Diagram</span>ی که مرز، مالکیت یا هدف تصمیم را روشن نکند، خروجی معماری محسوب نمی‌شود.

## ۸. خط پایهٔ فنی پروژه

### فناوری‌ها

- <span dir="ltr">Java 21 LTS</span>؛ انتخابی محافظه‌کارانه برای تمرکز بر معماری و سازگاری سازمانی
- <span dir="ltr">Spring Boot 4.1</span> و <span dir="ltr">Spring Modulith 2.1</span>
- <span dir="ltr">Maven</span>
- <span dir="ltr">PostgreSQL</span> برای اجرای روزانه و تست‌های <span dir="ltr">Integration/Concurrency</span>
- <span dir="ltr">Oracle 23ai</span> برای <span dir="ltr">DDL</span>، <span dir="ltr">Partitioning</span>، <span dir="ltr">Query Plan</span> و تفاوت‌های فیزیکی
- <span dir="ltr">Apache Kafka 4.1</span>
- <span dir="ltr">Testcontainers</span> برای <span dir="ltr">PostgreSQL</span>، <span dir="ltr">Kafka</span> و تست <span dir="ltr">Integration</span>
- <span dir="ltr">OpenAPI 3.1</span> برای <span dir="ltr">API</span>های همگام
- <span dir="ltr">AsyncAPI 3.1</span> برای قراردادهای پیام
- <span dir="ltr">Docker Compose</span> برای محیط توسعه
- <span dir="ltr">OpenTelemetry</span> برای <span dir="ltr">Trace</span>، <span dir="ltr">Metric</span> و <span dir="ltr">Log Correlation</span>
- <span dir="ltr">Prometheus</span> و <span dir="ltr">Grafana</span>؛ یک <span dir="ltr">Backend</span> سازگار با <span dir="ltr">OpenTelemetry</span> برای <span dir="ltr">Trace</span>
- <span dir="ltr">Kubernetes Manifest</span> در هفتهٔ ۲۲؛ ادارهٔ کلاستر خارج از محدودهٔ دوره است
- <span dir="ltr">React/Vite</span> برای <span dir="ltr">Shell</span> و <span dir="ltr">Widget</span> نمونه؛ قرارداد اتصال <span dir="ltr">Micro-frontend</span> مبتنی بر <span dir="ltr">Runtime Manifest</span> و <span dir="ltr">Web Component</span> خواهد بود تا به یک <span dir="ltr">Framework</span> محدود نشود

<span dir="ltr">Spring Boot 4.1</span> حداقل <span dir="ltr">Java 17</span> می‌خواهد و با <span dir="ltr">Java 26</span> نیز سازگار است؛ بنابراین <span dir="ltr">Java 21</span> انتخاب محدودکننده‌ای برای این پروژه نیست. این انتخاب عمدی است تا زمان دوره صرف قابلیت‌های زبان جدید نشود.

### ساختار مخزن


</div>

<div dir="ltr" align="left">

```text
core-banking-lab/
├── backend/
│   ├── banking-modulith/          # نقطهٔ شروع؛ Tag پیش از استخراج
│   ├── deposit-service/
│   ├── lending-service/
│   ├── payment-service/
│   ├── accounting-service/
│   └── process-manager/
├── frontend/
│   ├── portal-shell/
│   ├── deposit-widget/
│   └── lending-widget/
├── contracts/
│   ├── openapi/
│   ├── asyncapi/
│   └── schemas/
├── docs/
│   ├── capability-map/
│   ├── domains/
│   ├── context-map/
│   ├── adr/
│   ├── data/
│   ├── nfr/
│   └── runbooks/
├── platform/
│   ├── compose/
│   ├── kubernetes/
│   └── observability/
└── tests/
    ├── end-to-end/
    ├── performance/
    └── failure/
```

</div>

<div dir="rtl" align="right">


تا پایان هفتهٔ ۸، راه‌حل اصلی <span dir="ltr">Modular Monolith</span> است. در هفته‌های ۹ و ۱۰ فقط ماژول‌هایی استخراج می‌شوند که <span dir="ltr">ADR</span> آن‌ها استخراج را توجیه کرده باشد. <span dir="ltr">Tag</span> مخزن امکان مقایسهٔ قبل و بعد را نگه می‌دارد.

## ۹. مدل خروجی دامین‌ها

### عمق بررسی

| سطح | دامین‌ها | خروجی مورد انتظار |
|---|---|---|
| عمیق | <span dir="ltr">Deposits</span>، <span dir="ltr">Lending</span>، <span dir="ltr">Payments</span>، <span dir="ltr">Accounting</span> | مدل، کد، داده، <span dir="ltr">API/Event</span>، شکست، حسابداری و کارایی |
| تفصیلی | <span dir="ltr">Party/Customer</span>، <span dir="ltr">Product/Agreement</span>، <span dir="ltr">Teller/Cash</span>، <span dir="ltr">Collateral</span>، <span dir="ltr">Collections</span> | پروندهٔ کامل، مرزبندی، <span dir="ltr">Catalog</span> و نمونهٔ قرارداد |
| معماری کلان | <span dir="ltr">Cards</span>، <span dir="ltr">Channels</span>، <span dir="ltr">Checks</span>، <span dir="ltr">Fees</span>، <span dir="ltr">Limits</span>، <span dir="ltr">AML</span>، <span dir="ltr">Fraud</span>، <span dir="ltr">Risk</span>، <span dir="ltr">IFRS</span>، <span dir="ltr">Regulatory Reporting</span> | <span dir="ltr">Capability Card</span>، مالکیت، نوع ارتباط و وابستگی |

### پروندهٔ ثابت ۱۲‌بخشی هر دامین

1. هدف، دامنه و موارد خارج از دامنه
2. <span dir="ltr">Capability</span>ها و <span dir="ltr">Use Case</span>های اصلی
3. زبان مشترک و مفاهیم دامینی
4. <span dir="ltr">Aggregate</span>ها، <span dir="ltr">State Machine</span>ها و <span dir="ltr">Invariant</span>ها
5. داده‌ها و تصمیم‌های تحت مالکیت
6. داده‌ها و تصمیم‌هایی که نباید مالک آن‌ها باشد
7. <span dir="ltr">Module/Service Candidate</span>ها و دلیل مرزبندی
8. <span dir="ltr">API</span>های ورودی و خروجی
9. <span dir="ltr">Domain Event</span>ها و <span dir="ltr">Integration Event</span>های تولیدی/مصرفی
10. <span dir="ltr">Context Map</span>، <span dir="ltr">Upstream/Downstream</span> و نوع وابستگی
11. <span dir="ltr">Transaction</span>، <span dir="ltr">Consistency</span>، <span dir="ltr">Idempotency</span>، نقاط شکست و <span dir="ltr">Reconciliation</span>
12. تیم مالک، <span dir="ltr">SLO</span>، <span dir="ltr">Security</span>، <span dir="ltr">Audit</span>، <span dir="ltr">Retention</span> و سایر <span dir="ltr">NFR</span>ها

### فرضیهٔ اولیهٔ مالکیت

| موضوع | مالک اولیه | نکته |
|---|---|---|
| هویت <span dir="ltr">Party</span> و وضعیت <span dir="ltr">Customer</span> | <span dir="ltr">Customer</span> | <span dir="ltr">Lending</span> یا <span dir="ltr">Deposits</span> فقط <span dir="ltr">Reference/Snapshot</span> لازم را نگه می‌دارند. |
| تعریف و نسخهٔ <span dir="ltr">Product/Pricing</span> | <span dir="ltr">Product</span> | شرایط قرارداد منعقدشده با تغییر <span dir="ltr">Product</span> عوض نمی‌شود. |
| شرایط قطعی قرارداد | <span dir="ltr">Agreement</span> در دامین صاحب قرارداد | <span dir="ltr">Lending/Deposits Snapshot</span> مؤثر را مالک است. |
| ماندهٔ قابل برداشت و <span dir="ltr">Hold</span> سپرده | <span dir="ltr">Deposits</span> | <span dir="ltr">Accounting</span> نباید ماندهٔ عملیاتی سپرده را کنترل کند. |
| ماندهٔ اصل، برنامه و بدهی تسهیلات | <span dir="ltr">Lending</span> | <span dir="ltr">Accounting</span> دفتر مالی متناظر را نگه می‌دارد، نه تصمیم وصول را. |
| <span dir="ltr">Payment Order</span>، <span dir="ltr">Clearing</span> و <span dir="ltr">Settlement State</span> | <span dir="ltr">Payments</span> | <span dir="ltr">Channel</span> فقط درخواست و نمایش را مالک است. |
| <span dir="ltr">Journal</span>، <span dir="ltr">Subledger</span> و <span dir="ltr">GL</span> | <span dir="ltr">Accounting</span> | رویداد کسب‌وکار را ترجمه می‌کند؛ منطق عملیاتی دامین را مالک نمی‌شود. |
| وضعیت یک فرایند چنددامینی | <span dir="ltr">Process Manager</span> | نباید داده یا قواعد داخلی دامین‌ها را تصاحب کند. |

این جدول تصمیم نهایی معماری نیست؛ فرضیه‌ای است که در طول دوره با سناریو و شواهد اصلاح می‌شود.

---

# برنامهٔ ۲۴ هفته‌ای

## اسپرینت ۱ — نقشهٔ بانک، زبان و مرزها

### هفتهٔ ۱: <span dir="ltr">Capability</span> تا <span dir="ltr">API/Event</span>

**فنی**

- تفاوت <span dir="ltr">Business Architecture</span>، <span dir="ltr">Solution Architecture</span> و <span dir="ltr">Software Architecture</span>
- <span dir="ltr">Coupling</span>، <span dir="ltr">Cohesion</span>، <span dir="ltr">Encapsulation</span> و <span dir="ltr">Information Hiding</span>
- تفاوت <span dir="ltr">System</span>، <span dir="ltr">Domain</span>، <span dir="ltr">Subdomain</span>، <span dir="ltr">Bounded Context</span>، <span dir="ltr">Module</span> و <span dir="ltr">Service</span>
- زنجیرهٔ کامل <span dir="ltr">`Capability → … → API/Event`</span>

**دامینی**

- ترسیم <span dir="ltr">Capability Map</span> سطح ۱ بانک
- طبقه‌بندی «هستهٔ بانکداری»، «عملیات و خدمات بانکداری»، «سامانه‌های سازمانی» و «اکوسیستم دیجیتال»
- استفاده از <span dir="ltr">BIAN 14.0</span> برای یافتن شکاف‌ها، نه تبدیل هر <span dir="ltr">Service Domain</span> به <span dir="ltr">Microservice</span>

**کد و تمرین**

- ایجاد مخزن و <span dir="ltr">Pipeline</span> اولیهٔ <span dir="ltr">`mvn verify`</span>
- ساخت <span dir="ltr">Value Object</span>های <span dir="ltr">`Money`</span>، <span dir="ltr">`AccountId`</span>، <span dir="ltr">`CustomerId`</span> و <span dir="ltr">`BranchId`</span>
- آزمون برابری، <span dir="ltr">Currency</span>، گردکردن و ورودی نامعتبر

**تحویل‌دادنی**

- <span dir="ltr">Capability Map</span> نسخهٔ ۱
- واژه‌نامهٔ حداقل ۴۰ اصطلاح کلیدی
- پاسخ معماری اولیه به سه سناریوی نهایی برای ثبت خط پایه

**معیار قبولی**

- هیچ <span dir="ltr">Service Candidate</span> بدون <span dir="ltr">Capability</span> و مالک کسب‌وکار معرفی نشده باشد.
- بتوان تفاوت <span dir="ltr">BIAN Service Domain</span> با <span dir="ltr">Deployable Microservice</span> را روشن توضیح داد.

**ریل‌های افزودهٔ <span dir="ltr">Week 01</span>**

- <span dir="ltr">Code Craft Lab: Refactor</span> مرحله‌ای <span dir="ltr">Primitive Transfer Request</span> به <span dir="ltr">Money</span> و <span dir="ltr">Typed ID</span> با <span dir="ltr">Characterization Test</span>، <span dir="ltr">Edge Test</span> و تصمیم مستدل دربارهٔ <span dir="ltr">Static Factory</span>
- <span dir="ltr">Core Banking Case File: UPI</span> هند؛ تفکیک <span dir="ltr">Capability</span>، <span dir="ltr">App</span>، <span dir="ltr">PSP</span>، شبکه، بانک و <span dir="ltr">API Contract</span> همراه با <span dir="ltr">Timeline</span>، <span dir="ltr">Failure</span> سال ۲۰۲۵ و <span dir="ltr">Current state</span> تاریخ‌دار
- محتوای کامل، تمرین و <span dir="ltr">Gate</span> در [<span dir="ltr">Week 01</span>](sprints/01-bank-map-boundaries/week-01-capability-to-contract/README.md) قرار دارد.

### هفتهٔ ۲: <span dir="ltr">Strategic DDD</span> و مالکیت

**فنی**

- <span dir="ltr">Domain/Subdomain</span>، <span dir="ltr">Core/Supporting/Generic</span>
- <span dir="ltr">Bounded Context</span> و <span dir="ltr">Ubiquitous Language</span>
- <span dir="ltr">Context Map: Customer/Supplier</span>، <span dir="ltr">Conformist</span>، <span dir="ltr">ACL</span> و <span dir="ltr">Published Language</span>
- <span dir="ltr">Source of Truth</span> و <span dir="ltr">Ownership of Decision</span>

**دامینی**

- مرزبندی اولیهٔ شش دامین اصلی
- تعیین «مالک چه چیزی است؟»، «چه چیزی را نباید مالک باشد؟» و «از چه کسی می‌گیرد؟»

**کد و تمرین**

- ساخت شش ماژول منطقی در <span dir="ltr">Spring Modulith</span>
- اجرای <span dir="ltr">Module Verification</span> برای <span dir="ltr">Cycle</span> و دسترسی به <span dir="ltr">Package</span> داخلی
- ثبت <span dir="ltr">Dependency</span> مجاز بین ماژول‌ها

**تحویل‌دادنی**

- <span dir="ltr">Domain Map</span> و <span dir="ltr">Context Map</span> نسخهٔ ۱
- <span dir="ltr">Data/Decision Ownership Matrix</span> نسخهٔ ۱
- اسکلت شش پروندهٔ دامینی
- <span dir="ltr">Architecture Fitness Test</span> اولیه

**<span dir="ltr">Gate</span> اسپرینت**

یک قابلیت جدید مانند «مسدودی قضایی سپرده» داده می‌شود. باید زنجیرهٔ <span dir="ltr">Capability</span> تا <span dir="ltr">API/Event</span>، مالک داده و مرزهای <span dir="ltr">Context</span> را بدون شروع از نام جدول یا سرویس طراحی کنی.

---

## اسپرینت ۲ — <span dir="ltr">Domain Model</span> و معماری داخلی کد

### هفتهٔ ۳: <span dir="ltr">Tactical DDD</span> روی <span dir="ltr">Deposits</span>

**فنی**

- <span dir="ltr">Entity</span>، <span dir="ltr">Value Object</span>، <span dir="ltr">Aggregate Root</span>، <span dir="ltr">Invariant</span> و <span dir="ltr">Domain Event</span>
- <span dir="ltr">Repository</span>، <span dir="ltr">Domain Service</span> و <span dir="ltr">Application Service</span>
- <span dir="ltr">SOLID</span> روی کد واقعی، نه تعریف حفظی
- <span dir="ltr">Strategy</span>، <span dir="ltr">Factory</span>، <span dir="ltr">Specification</span> و <span dir="ltr">State</span>؛ تشخیص زمان نامناسب استفاده از <span dir="ltr">Pattern</span>

**دامینی**

- <span dir="ltr">`DepositAccount`</span>، <span dir="ltr">`Balance`</span>، <span dir="ltr">`Hold`</span> و <span dir="ltr">Lifecycle</span> حساب
- قواعد برداشت، مسدودی، رفع مسدودی و ماندهٔ قابل برداشت

**کد و تمرین**

- پیاده‌سازی <span dir="ltr">`credit`</span>، <span dir="ltr">`debit`</span>، <span dir="ltr">`placeHold`</span> و <span dir="ltr">`releaseHold`</span>
- <span dir="ltr">Strategy</span> محاسبهٔ سود و <span dir="ltr">Specification</span> احراز شرایط عملیات
- <span dir="ltr">Unit Test</span> برای کمبود موجودی، <span dir="ltr">Hold</span> تکراری، مبلغ منفی و <span dir="ltr">State</span> نامعتبر

**تحویل‌دادنی**

- مدل دامینی <span dir="ltr">Deposits</span> نسخهٔ ۱
- فهرست <span dir="ltr">Aggregate</span> و <span dir="ltr">Transaction Boundary</span>
- <span dir="ltr">Code Review Checklist</span> برای <span dir="ltr">Domain Model</span>

**معیار قبولی**

- <span dir="ltr">Controller</span> یا <span dir="ltr">Entity</span> دیتابیس منطق کسب‌وکار را نگه ندارد.
- هیچ <span dir="ltr">Setter</span> عمومی برای دورزدن <span dir="ltr">Invariant</span> وجود نداشته باشد.

### هفتهٔ ۴: <span dir="ltr">Hexagonal Architecture</span> روی <span dir="ltr">Lending</span>

**فنی**

- <span dir="ltr">Layered</span>، <span dir="ltr">Clean</span> و <span dir="ltr">Hexagonal Architecture</span>
- <span dir="ltr">Inbound/Outbound Port</span> و <span dir="ltr">Adapter</span>
- <span dir="ltr">Dependency Inversion</span>، <span dir="ltr">Unit of Work</span> و تست‌پذیری
- <span dir="ltr">Refactoring</span> یک کلاس بزرگ به <span dir="ltr">Strategy/Factory/Policy</span>

**دامینی**

- <span dir="ltr">`LoanAgreement`</span>، <span dir="ltr">`Disbursement`</span>، <span dir="ltr">`RepaymentSchedule`</span> و <span dir="ltr">`Installment`</span>
- قواعد تصویب، قرارداد، اعطا، گردکردن مبلغ و پرداخت قسط

**کد و تمرین**

- <span dir="ltr">Use Case</span> اولیهٔ <span dir="ltr">`GrantLoan`</span>
- <span dir="ltr">Persistence Adapter</span> روی <span dir="ltr">PostgreSQL</span>
- <span dir="ltr">Integration Test</span> با <span dir="ltr">Testcontainers</span>
- بازطراحی یک نمونهٔ <span dir="ltr">Java 8</span> از <span dir="ltr">Mapping</span> تراکنش‌های مالی برای حفظ ارتباط با محیط واقعی

**تحویل‌دادنی**

- اسکلت <span dir="ltr">Hexagonal</span> قابل اجرا
- <span dir="ltr">ADR-001:</span> معماری داخلی سرویس
- تست معماری برای ممنوعیت وابستگی <span dir="ltr">Domain</span> به <span dir="ltr">Spring/JPA/Kafka</span>

**<span dir="ltr">Gate</span> اسپرینت**

- تمام <span dir="ltr">Invariant</span>ها <span dir="ltr">Unit Test</span> دارند.
- <span dir="ltr">Domain</span> بدون <span dir="ltr">Spring Context</span> آزمون می‌شود.
- <span dir="ltr">Adapter</span> دیتابیس با <span dir="ltr">PostgreSQL</span> واقعیِ <span dir="ltr">Testcontainers</span> آزمون شده است.

---

## اسپرینت ۳ — قراردادها، مرز سرویس و امنیت

### هفتهٔ ۵: <span dir="ltr">API</span> و <span dir="ltr">Source of Truth</span>

**فنی**

- <span dir="ltr">Command/Query</span> و تفاوت <span dir="ltr">API</span> دامینی با <span dir="ltr">CRUD</span>
- <span dir="ltr">REST Semantics</span>، <span dir="ltr">OpenAPI</span>، <span dir="ltr">Error Model</span> و <span dir="ltr">Validation</span>
- <span dir="ltr">Idempotency Key</span>، <span dir="ltr">Optimistic Version</span> و <span dir="ltr">API Versioning</span>
- <span dir="ltr">Temporal Data</span>، <span dir="ltr">Effective Dating</span> و <span dir="ltr">Snapshot</span>

**دامینی**

- <span dir="ltr">Party</span> در برابر <span dir="ltr">Customer</span>
- <span dir="ltr">Product Definition</span>، <span dir="ltr">Pricing</span>، <span dir="ltr">Eligibility</span> و <span dir="ltr">Agreement</span>
- مشخص‌کردن داده‌های <span dir="ltr">Reference</span> و <span dir="ltr">Snapshot</span>شونده در قرارداد

**کد و تمرین**

- <span dir="ltr">API</span> ایجاد/مشاهدهٔ <span dir="ltr">Loan Agreement</span>
- ذخیرهٔ <span dir="ltr">Snapshot</span> شرایط <span dir="ltr">Product</span> هنگام انعقاد قرارداد
- تست <span dir="ltr">Contract</span>، <span dir="ltr">Idempotency</span> و تغییر هم‌زمان <span dir="ltr">Version</span>

**تحویل‌دادنی**

- <span dir="ltr">OpenAPI</span> نسخهٔ ۱
- <span dir="ltr">Command/Query Catalog</span>
- ماتریس <span dir="ltr">Source of Truth/Snapshot/Cache</span>

**معیار قبولی**

- تغییر <span dir="ltr">Product</span>، قرارداد قبلی را تغییر ندهد.
- <span dir="ltr">Retry</span> یک <span dir="ltr">Request</span> با <span dir="ltr">Idempotency Key</span> یکسان اثر مالی دوم نسازد.

### هفتهٔ ۶: <span dir="ltr">Modular Monolith</span> یا <span dir="ltr">Microservice</span> و <span dir="ltr">Security by Design</span>

**فنی**

- <span dir="ltr">Transactional Cohesion</span>، <span dir="ltr">Change Coupling</span>، <span dir="ltr">Independent Deployment</span> و <span dir="ltr">Team Boundary</span>
- <span dir="ltr">Shared Database</span>، <span dir="ltr">Shared Library</span> و <span dir="ltr">Distributed Monolith</span>
- <span dir="ltr">AuthN</span>، <span dir="ltr">AuthZ</span>، <span dir="ltr">Scope/Role</span>، <span dir="ltr">Object-level Authorization</span> و <span dir="ltr">Audit</span>
- <span dir="ltr">Threat Modeling</span> سبک و کنترل‌های <span dir="ltr">OWASP API Security</span>

**دامینی**

- تصمیم <span dir="ltr">Module/Service</span> برای <span dir="ltr">Deposits</span>، <span dir="ltr">Lending</span>، <span dir="ltr">Payments</span> و <span dir="ltr">Accounting</span>
- تعیین <span dir="ltr">API Gateway Policy</span> در برابر <span dir="ltr">Business Policy</span>

**کد و تمرین**

- تست مجوز روی <span dir="ltr">Account/Loan</span> متعلق به مشتری دیگر
- <span dir="ltr">Audit Context</span> شامل <span dir="ltr">Actor</span>، <span dir="ltr">Channel</span>، <span dir="ltr">Branch</span> و <span dir="ltr">Correlation ID</span>
- <span dir="ltr">Architecture Test</span> برای جلوگیری از <span dir="ltr">Shared Entity/Repository</span> میان دامین‌ها

**تحویل‌دادنی**

- <span dir="ltr">Service Candidate Map</span>
- <span dir="ltr">ADR-002:</span> معماری <span dir="ltr">Lending</span>
- <span dir="ltr">ADR-003:</span> معماری <span dir="ltr">Accounting</span>
- <span dir="ltr">ADR-004:</span> مرز <span dir="ltr">Deposits</span> و <span dir="ltr">Payments</span>
- <span dir="ltr">Threat Model</span> و <span dir="ltr">Security Checklist</span> اولیه

**<span dir="ltr">Gate</span> اسپرینت**

هیچ <span dir="ltr">Microservice</span> صرفاً به‌دلیل «مدرن‌بودن»، تعداد <span dir="ltr">Entity</span> یا وجود یک <span dir="ltr">BIAN Service Domain</span> ایجاد نشده باشد. هر استخراج باید حداقل دو محرک مستقل و هزینه‌های توزیع را ثبت کند.

---

## اسپرینت ۴ — تراکنش، مانده و <span dir="ltr">CQRS</span>

### هفتهٔ ۷: <span dir="ltr">Isolation</span>، <span dir="ltr">Locking</span> و <span dir="ltr">Concurrency</span>

**فنی**

- <span dir="ltr">ACID</span> و <span dir="ltr">Isolation Level</span>
- <span dir="ltr">Lost Update</span>، <span dir="ltr">Non-repeatable Read</span>، <span dir="ltr">Phantom</span> و <span dir="ltr">Write Skew</span>
- <span dir="ltr">Optimistic/Pessimistic Lock</span>، <span dir="ltr">Atomic Update</span> و <span dir="ltr">Lock Ordering</span>
- <span dir="ltr">Deadlock</span>، <span dir="ltr">Retry Budget</span> و <span dir="ltr">Transaction Boundary</span>

**دامینی**

- برداشت هم‌زمان از سپرده
- <span dir="ltr">Hold</span> و برداشت هم‌زمان
- وصول هم‌زمان قسط
- پرداخت از چند <span dir="ltr">Channel</span>

**کد و تمرین**

- بازتولید <span dir="ltr">Lost Update</span>
- سه راه‌حل: <span dir="ltr">Optimistic Lock</span>، <span dir="ltr">`SELECT FOR UPDATE`</span> و <span dir="ltr">Atomic Conditional Update</span>
- تست هم‌زمانی با تقاضای بیش از موجودی و اثبات عدم منفی‌شدن مانده
- مقایسهٔ رفتار <span dir="ltr">PostgreSQL</span> و <span dir="ltr">Oracle</span>

**تحویل‌دادنی**

- <span dir="ltr">Concurrency Decision Matrix</span>
- <span dir="ltr">Lock Ordering Policy</span>
- تست خودکار <span dir="ltr">Deadlock/Retry</span> و <span dir="ltr">Oversubscription</span>

**معیار قبولی**

- صحت با <span dir="ltr">Sleep</span> تصادفی یا اجرای تک‌<span dir="ltr">Thread</span> اثبات نشده باشد.
- <span dir="ltr">Retry</span> محدود، قابل مشاهده و فقط برای خطاهای <span dir="ltr">Retryable</span> باشد.

### هفتهٔ ۸: <span dir="ltr">Operational Balance</span>، <span dir="ltr">Ledger</span>، <span dir="ltr">Subledger</span> و <span dir="ltr">CQRS</span>

**فنی**

- <span dir="ltr">Source of Truth</span>، <span dir="ltr">Derived Data</span>، <span dir="ltr">Snapshot</span> و <span dir="ltr">Projection</span>
- <span dir="ltr">Command Model</span>، <span dir="ltr">Read Model</span>، <span dir="ltr">Projection Lag</span> و <span dir="ltr">Rebuild</span>
- <span dir="ltr">Operational Ledger</span>، <span dir="ltr">Accounting Subledger</span> و <span dir="ltr">General Ledger</span>
- <span dir="ltr">Reconciliation</span> و <span dir="ltr">Proof of Balance</span>

**دامینی**

- مالک ماندهٔ قابل برداشت، ماندهٔ اصل و اقساط
- تفکیک دفتر معین تسهیلات از وضعیت عملیاتی تسهیلات

**کد و تمرین**

- <span dir="ltr">Read Model</span> صورت‌حساب سپرده
- <span dir="ltr">Projection</span> مصرف‌کنندهٔ رویداد و <span dir="ltr">Rebuild</span> کامل
- <span dir="ltr">Job</span> مغایرت‌گیری بین <span dir="ltr">Operational Transactions</span> و <span dir="ltr">Read Model</span>
- مقایسهٔ <span dir="ltr">Event Sourcing</span> با <span dir="ltr">Event-driven/CQRS</span> و ثبت دلیل استفاده‌نکردن از <span dir="ltr">Event Sourcing</span> به‌عنوان پیش‌فرض

**تحویل‌دادنی**

- مدل دادهٔ ماندهٔ عملیاتی
- مدل اولیهٔ <span dir="ltr">Subledger</span>
- <span dir="ltr">CQRS Consistency Contract</span> شامل <span dir="ltr">Lag</span> مجاز و رفتار در <span dir="ltr">Stale Read</span>
- <span dir="ltr">Reconciliation Specification</span>

**<span dir="ltr">Gate</span> اسپرینت**

برای هر مانده باید مشخص باشد: مالک، روش تغییر، مرز <span dir="ltr">ACID</span>، امکان <span dir="ltr">Rebuild</span>، منبع مغایرت‌گیری و رفتار در تأخیر <span dir="ltr">Projection</span> چیست.

---

## اسپرینت ۵ — <span dir="ltr">Event-driven Architecture</span> قابل اتکا

### هفتهٔ ۹: <span dir="ltr">Command</span>، <span dir="ltr">Domain Event</span> و <span dir="ltr">Integration Event</span>

**فنی**

- تفاوت <span dir="ltr">Command</span>، <span dir="ltr">Domain Event</span>، <span dir="ltr">Integration Event</span> و <span dir="ltr">Query</span>
- <span dir="ltr">Event Notification</span> در برابر <span dir="ltr">Event-Carried State Transfer</span>
- <span dir="ltr">Semantic Event</span>، <span dir="ltr">Schema Evolution</span> و <span dir="ltr">Compatibility</span>
- <span dir="ltr">Correlation ID</span>، <span dir="ltr">Causation ID</span> و <span dir="ltr">Business Transaction ID</span>

**دامینی**

- طراحی پیام‌های فرایند اعطا و واریز به سپرده
- تعیین اینکه چه کسی <span dir="ltr">Command</span> می‌دهد و چه دامین صاحب <span dir="ltr">Event</span> است

**کد و تمرین**

- تعریف <span dir="ltr">Event Envelope</span> استاندارد با این فیلدها:
  <span dir="ltr">`eventId`</span>، <span dir="ltr">`eventType`</span>، <span dir="ltr">`eventVersion`</span>، <span dir="ltr">`occurredAt`</span>، <span dir="ltr">`producer`</span>، <span dir="ltr">`aggregateId`</span>، <span dir="ltr">`aggregateVersion`</span>، <span dir="ltr">`businessTransactionId`</span>، <span dir="ltr">`correlationId`</span>، <span dir="ltr">`causationId`</span>، <span dir="ltr">`partitionKey`</span> و <span dir="ltr">`payload`</span>
- نگارش <span dir="ltr">AsyncAPI</span> برای جریان اعطا
- <span dir="ltr">Contract Compatibility Test</span>

**تحویل‌دادنی**

- <span dir="ltr">Event Catalog</span> نسخهٔ ۱
- <span dir="ltr">AsyncAPI</span> نسخهٔ ۱
- <span dir="ltr">Sequence Diagram</span> اعطای تسهیلات

**معیار قبولی**

- نام <span dir="ltr">Event</span> رخداد گذشته باشد، نه دستور مبهم.
- <span dir="ltr">Consumer</span> برای فهم <span dir="ltr">Payload</span> مجبور به <span dir="ltr">Query</span> همگام غیرضروری نشود.

### هفتهٔ ۱۰: <span dir="ltr">Kafka</span>، <span dir="ltr">Outbox</span>، <span dir="ltr">Inbox</span> و <span dir="ltr">Idempotency</span>

**فنی**

- <span dir="ltr">Topic</span>، <span dir="ltr">Partition</span>، <span dir="ltr">Offset</span> و <span dir="ltr">Consumer Group</span>
- <span dir="ltr">Ordering</span> در محدودهٔ <span dir="ltr">Partition</span> و انتخاب <span dir="ltr">Partition Key</span>
- <span dir="ltr">At-least-once Delivery</span> و محدودهٔ واقعی <span dir="ltr">Kafka Exactly-once</span>
- <span dir="ltr">Transactional Outbox</span>، <span dir="ltr">Inbox</span>، <span dir="ltr">Deduplication</span> و <span dir="ltr">Replay</span>

**کد و تمرین**

- ذخیرهٔ <span dir="ltr">Aggregate</span> و <span dir="ltr">Outbox</span> در یک تراکنش
- انتشار به <span dir="ltr">Kafka</span> و مصرف در سرویس دوم
- <span dir="ltr">Unique Constraint</span> روی <span dir="ltr">`event_id`</span> و <span dir="ltr">Business Idempotency Key</span>
- تست <span dir="ltr">Crash</span> بعد از <span dir="ltr">Commit</span>، پیام تکراری و <span dir="ltr">Replay</span>

**تحویل‌دادنی**

- <span dir="ltr">Outbox/Inbox Schema</span>
- <span dir="ltr">Topic/Partition/Retention Catalog</span>
- <span dir="ltr">Idempotency Policy</span> برای عملیات مالی
- <span dir="ltr">ADR-005:</span> روش انتشار <span dir="ltr">Event</span>

**<span dir="ltr">Gate</span> اسپرینت**

- مصرف دوباره اثر مالی دوم نسازد.
- <span dir="ltr">Replay</span>، <span dir="ltr">Projection</span> را بازسازی کند.
- <span dir="ltr">Ordering</span> مورد نیاز با <span dir="ltr">Aggregate/Business Key</span> مستند و آزموده شود.

---

## اسپرینت ۶ — <span dir="ltr">Saga</span>، شکست و مشاهده‌پذیری

### هفتهٔ ۱۱: <span dir="ltr">Process Manager</span> و <span dir="ltr">State Machine</span>

**فنی**

- <span dir="ltr">Saga</span>، <span dir="ltr">Orchestration</span>، <span dir="ltr">Choreography</span> و <span dir="ltr">Process Manager</span>
- <span dir="ltr">Long-running State Machine</span>، <span dir="ltr">Timeout</span> و <span dir="ltr">Retry Policy</span>
- <span dir="ltr">Business Correlation</span> و وضعیت‌های میانی

**دامینی**

- فرایند اعطای تسهیلات:
  1. ثبت درخواست اعطا در <span dir="ltr">Lending</span>
  2. درخواست <span dir="ltr">Credit</span> به <span dir="ltr">Deposits</span>
  3. دریافت نتیجهٔ واریز
  4. قطعی‌کردن وضعیت <span dir="ltr">Disbursement</span>
  5. پردازش حسابداری و <span dir="ltr">Reconciliation</span>

**کد و تمرین**

- پیاده‌سازی <span dir="ltr">Process Instance</span> پایدار و <span dir="ltr">Versioned</span>
- <span dir="ltr">Handler</span>های <span dir="ltr">Idempotent</span> و <span dir="ltr">Timer/Timeout</span>
- جداکردن وضعیت تکمیل عملیات کسب‌وکار از وضعیت <span dir="ltr">Pending</span> حسابداری

**تحویل‌دادنی**

- <span dir="ltr">State Machine</span> و <span dir="ltr">State Transition Table</span>
- <span dir="ltr">ADR-006: Orchestration</span> یا <span dir="ltr">Choreography</span>
- <span dir="ltr">Process Data Model</span>

**معیار قبولی**

- <span dir="ltr">Orchestrator</span> مستقیماً جدول یا منطق داخلی دامین‌ها را تغییر ندهد.
- <span dir="ltr">Restart</span> سرویس وضعیت فرایند را از بین نبرد.

### هفتهٔ ۱۲: <span dir="ltr">Failure</span>، <span dir="ltr">Compensation</span>، <span dir="ltr">Reconciliation</span> و <span dir="ltr">Observability</span>

**فنی**

- <span dir="ltr">Business Failure</span> در برابر <span dir="ltr">Technical Failure</span>
- <span dir="ltr">Retryable/Non-retryable</span>، <span dir="ltr">Backoff/Jitter</span>، <span dir="ltr">DLQ</span> و <span dir="ltr">Poison Message</span>
- <span dir="ltr">Timeout Budget</span>، <span dir="ltr">Circuit Breaker</span> و <span dir="ltr">Bulkhead</span> برای وابستگی‌های همگام
- <span dir="ltr">Rollback</span>، <span dir="ltr">Compensation</span>، <span dir="ltr">Reversal</span> و <span dir="ltr">Correction</span>
- <span dir="ltr">Trace</span>، <span dir="ltr">Metric</span>، <span dir="ltr">Log</span> و <span dir="ltr">Context Propagation</span>

**آزمایش‌های اجباری**

1. <span dir="ltr">Deposits</span> در دسترس نیست.
2. واریز انجام شده ولی پاسخ گم می‌شود.
3. <span dir="ltr">Event</span> دوبار تحویل می‌شود.
4. <span dir="ltr">Accounting</span> موقتاً قطع است.
5. <span dir="ltr">Event</span>ها خارج از ترتیب می‌رسند.
6. سرویس بعد از <span dir="ltr">DB Commit</span> و قبل از <span dir="ltr">Publish</span> متوقف می‌شود.

**کد و تمرین**

- تزریق شش خطا و ثبت نتیجهٔ مورد انتظار
- <span dir="ltr">Trace</span> سراسری با <span dir="ltr">Correlation/Causation</span>
- <span dir="ltr">Metric</span> برای <span dir="ltr">Pending Process</span>، <span dir="ltr">Retry</span>، <span dir="ltr">Duplicate</span> و <span dir="ltr">Reconciliation Mismatch</span>

**تحویل‌دادنی**

- <span dir="ltr">Failure Matrix</span> و <span dir="ltr">Compensation Matrix</span>
- <span dir="ltr">Runbook</span> تعمیر دستی و <span dir="ltr">Reconciliation</span>
- داشبورد اولیهٔ جریان اعطا

**<span dir="ltr">Gate</span> اسپرینت**

هر شکست باید دقیقاً یکی از این پایان‌ها را داشته باشد: <span dir="ltr">Retry</span> کنترل‌شده، <span dir="ltr">Compensation/Reversal</span>، توقف کسب‌وکاری، یا <span dir="ltr">Manual Repair</span> قابل ممیزی. وضعیت «نامعلوم و بدون مالک» مردود است.

---

## اسپرینت ۷ — معماری حسابداری بانکی

### هفتهٔ ۱۳: <span dir="ltr">Accounting Fact</span> و <span dir="ltr">Translator</span>

**فنی و دامینی**

معماری مرجع:


</div>

<div dir="ltr" align="left">

```text
Domain Event
  → Domain-specific Accounting Translator
  → Accounting Fact
  → Effective-dated Accounting Rule
  → Journal + Subledger Entry
```

</div>

<div dir="rtl" align="right">


- تفاوت رخداد کسب‌وکار با <span dir="ltr">Fact</span> حسابداری
- <span dir="ltr">Published Language</span> میان دامین و <span dir="ltr">Accounting</span>
- <span dir="ltr">Rule Version</span>، <span dir="ltr">Effective Date</span> و <span dir="ltr">Rule Selection</span>
- جلوگیری از ورود منطق «اعطای مرابحه» یا «شکست سپرده» به هستهٔ عمومی <span dir="ltr">Journal</span>

**کد و تمرین**

- <span dir="ltr">Fact Schema</span> و <span dir="ltr">Translator</span> برای پنج <span dir="ltr">Event</span>
- <span dir="ltr">Rule Engine</span> ساده و قابل نسخه‌بندی
- تست اینکه <span dir="ltr">Replay</span> با همان نسخهٔ <span dir="ltr">Rule</span> همان نتیجه را می‌دهد

**تحویل‌دادنی**

- <span dir="ltr">Accounting Fact Catalog</span>
- <span dir="ltr">Event-to-Fact Mapping</span>
- <span dir="ltr">ADR-007:</span> مرز <span dir="ltr">Translator</span> و <span dir="ltr">Accounting Engine</span>

**معیار قبولی**

- <span dir="ltr">Accounting Fact</span> اطلاعات لازم برای ثبت و <span dir="ltr">Audit</span> را دارد.
- <span dir="ltr">Event</span> اصلی، <span dir="ltr">Fact</span> و نسخهٔ <span dir="ltr">Rule</span> قابل رهگیری متقابل‌اند.

### هفتهٔ ۱۴: <span dir="ltr">Journal</span>، <span dir="ltr">Subledger</span>، <span dir="ltr">GL</span> و قواعد مالی

**فنی و دامینی**

- <span dir="ltr">Double-entry</span>، <span dir="ltr">Chart of Accounts</span>، <span dir="ltr">Journal</span> و <span dir="ltr">Journal Line</span>
- <span dir="ltr">GL</span>، <span dir="ltr">SL</span> و <span dir="ltr">Auxiliary Dimensions</span>
- <span dir="ltr">Cost Center</span>، <span dir="ltr">Branch</span>، <span dir="ltr">Currency</span>، <span dir="ltr">Fiscal Year</span> و <span dir="ltr">Financial Period</span>
- <span dir="ltr">Accrual</span>، <span dir="ltr">Reversal</span>، <span dir="ltr">Correction</span> و <span dir="ltr">Back-dated Posting</span>
- حفظ جزئیات <span dir="ltr">Event/Subledger</span> و تجمیع فقط در <span dir="ltr">Projection</span> یا <span dir="ltr">GL</span> مناسب

**ده رویداد مرجع**

1. <span dir="ltr">`LoanDisbursed`</span>
2. <span dir="ltr">`LoanPrincipalRepaid`</span>
3. <span dir="ltr">`LoanInterestAccrued`</span>
4. <span dir="ltr">`LatePenaltyAssessed`</span>
5. <span dir="ltr">`DepositCredited`</span>
6. <span dir="ltr">`DepositDebited`</span>
7. <span dir="ltr">`DepositInterestAccrued`</span>
8. <span dir="ltr">`DepositInterestPaid`</span>
9. <span dir="ltr">`PaymentSettled`</span>
10. <span dir="ltr">`TermDepositBroken`</span>

**کد و تمرین**

- ثبت <span dir="ltr">Idempotent Journal</span>
- کنترل <span dir="ltr">`Sum(Debit) = Sum(Credit)`</span>
- رد <span dir="ltr">Period</span> بسته و ثبت <span dir="ltr">Reversal</span> با <span dir="ltr">Link</span> به سند مبنا
- تولید <span dir="ltr">Subledger Entry</span> بدون حذف جزئیات رخداد

**تحویل‌دادنی**

- قواعد ثبت ده <span dir="ltr">Event</span>
- نمونه‌سندهای سپرده، تسهیلات و انتقال وجه
- مدل <span dir="ltr">Rule Versioning</span> و <span dir="ltr">Period Control</span>

**معیار قبولی**

- هیچ <span dir="ltr">Journal</span> نامتوازن ثبت نشود.
- سند اصلاحی سابقهٔ سند اصلی را حذف یا بازنویسی نکند.

---

## اسپرینت ۸ — طراحی فیزیکی و کارایی مالی

### هفتهٔ ۱۵: <span dir="ltr">Oracle/PostgreSQL Physical Design</span>

**فنی**

- طراحی براساس <span dir="ltr">Query Pattern</span> و حجم/<span dir="ltr">Retention</span>
- <span dir="ltr">Primary/Business Key</span>، <span dir="ltr">Foreign Key</span> و <span dir="ltr">Unique Constraint</span>
- <span dir="ltr">Composite/Partial/Local/Global Index</span>
- <span dir="ltr">Range/List/Hash/Composite Partitioning</span>
- <span dir="ltr">Oracle Reference Partitioning</span> و <span dir="ltr">Partition Pruning</span>
- <span dir="ltr">Archive</span>، <span dir="ltr">Purge</span>، <span dir="ltr">Compression</span> و <span dir="ltr">Tablespace Policy</span>

**جداول مرجع**

- <span dir="ltr">`accounting_event`</span>
- <span dir="ltr">`journal`</span>
- <span dir="ltr">`journal_line`</span>
- <span dir="ltr">`subledger_entry`</span>
- <span dir="ltr">`balance_snapshot`</span>
- <span dir="ltr">`outbox_event`</span>
- <span dir="ltr">`inbox_message`</span>
- <span dir="ltr">`process_instance`</span>

**کد و تمرین**

- <span dir="ltr">DDL</span> اجرایی برای <span dir="ltr">PostgreSQL</span> و <span dir="ltr">Oracle</span>
- <span dir="ltr">Reference Partitioning</span> فرزند <span dir="ltr">Journal</span> در <span dir="ltr">Oracle</span>
- <span dir="ltr">Explain Plan</span> برای پنج <span dir="ltr">Query</span> حیاتی

**تحویل‌دادنی**

- <span dir="ltr">Logical</span> و <span dir="ltr">Physical Data Model</span>
- <span dir="ltr">Partition/Index/Retention Matrix</span>
- <span dir="ltr">Critical Query Catalog</span>
- <span dir="ltr">ADR-008:</span> سیاست <span dir="ltr">Partitioning</span>

**معیار قبولی**

- هیچ جدولی فقط به‌دلیل «بزرگ‌بودن احتمالی» <span dir="ltr">Partition</span> نشده باشد.
- کلید <span dir="ltr">Partition</span> با <span dir="ltr">Query</span>، <span dir="ltr">Retention</span> و عملیات نگهداری توجیه شود.

### هفتهٔ ۱۶: <span dir="ltr">Hot Row</span>، <span dir="ltr">Batch</span>، <span dir="ltr">EOD</span> و <span dir="ltr">Performance</span>

**فنی و دامینی**

- <span dir="ltr">Hot Account/Hot GL Row</span>
- <span dir="ltr">Atomic Increment</span>، <span dir="ltr">Optimistic Retry</span> و <span dir="ltr">Event Serialization</span>
- <span dir="ltr">Balance Snapshot</span> و <span dir="ltr">Rebuild</span>
- <span dir="ltr">Batch Chunking</span>، <span dir="ltr">Checkpoint</span> و <span dir="ltr">Restartability</span>
- <span dir="ltr">Interest Accrual/EOD</span> و <span dir="ltr">Business Calendar</span>
- <span dir="ltr">Performance</span> و <span dir="ltr">Capacity Test</span>

**کد و تمرین**

- <span dir="ltr">Load Test</span> روی <span dir="ltr">Debit/Credit</span> و <span dir="ltr">Journal Posting</span>
- ثبت <span dir="ltr">Baseline</span> و یک دور <span dir="ltr">Tuning</span> قابل اندازه‌گیری
- <span dir="ltr">Restart</span> آزمون <span dir="ltr">EOD</span> از <span dir="ltr">Checkpoint</span> بدون ثبت تکراری
- <span dir="ltr">Reconciliation</span> بعد از <span dir="ltr">Load</span>

**تحویل‌دادنی**

- <span dir="ltr">Performance Test Plan</span> و <span dir="ltr">Report</span>
- <span dir="ltr">Hot-row Mitigation Decision</span>
- <span dir="ltr">EOD Runbook</span>
- <span dir="ltr">Snapshot/Rebuild Policy</span>

**<span dir="ltr">Gate</span> اسپرینت**

- صحت مالی در <span dir="ltr">Load</span> صددرصد حفظ شود و <span dir="ltr">Duplicate</span> مالی صفر باشد.
- <span dir="ltr">p50/p95/p99</span>، <span dir="ltr">Throughput</span>، <span dir="ltr">Error Rate</span> و <span dir="ltr">Lock Wait</span> ثبت شوند.
- بهبود پس از <span dir="ltr">Tuning</span> با عدد و <span dir="ltr">Query Plan</span> اثبات شود، نه با احساس.

---

## اسپرینت ۹ — عمق دامین: <span dir="ltr">Customer</span>، <span dir="ltr">Product</span>، <span dir="ltr">Deposits</span> و <span dir="ltr">Teller</span>

### هفتهٔ ۱۷: <span dir="ltr">Party/Customer</span>، <span dir="ltr">Product</span> و <span dir="ltr">Agreement</span>

**فنی و دامینی**

- <span dir="ltr">Party</span>، <span dir="ltr">Customer</span>، <span dir="ltr">KYC</span> و <span dir="ltr">Customer Relationship</span>
- <span dir="ltr">Product Definition</span>، <span dir="ltr">Pricing</span>، <span dir="ltr">Eligibility</span> و <span dir="ltr">Bundle</span>
- <span dir="ltr">Temporal Data</span> و <span dir="ltr">Effective-dated Rate</span>
- <span dir="ltr">Agreement</span>، <span dir="ltr">Contract Terms</span> و <span dir="ltr">Immutable Snapshot</span>
- <span dir="ltr">ACL</span> و <span dir="ltr">Reference Data Cache</span>

**کد و تمرین**

- انتخاب نرخ مؤثر بر تاریخ قرارداد
- <span dir="ltr">Snapshot</span> غیرقابل‌تغییر <span dir="ltr">Product Terms</span>
- <span dir="ltr">Event</span>های <span dir="ltr">`CustomerStatusChanged`</span> و <span dir="ltr">`ProductVersionActivated`</span>

**تحویل‌دادنی**

- سه پروندهٔ دامینی کامل
- <span dir="ltr">API/Event Catalog</span> و <span dir="ltr">Context Map</span> مرتبط
- <span dir="ltr">Temporal Data Model</span>

**معیار قبولی**

- سابقهٔ قرارداد با تغییر اطلاعات <span dir="ltr">Master</span> از بین نرود.
- <span dir="ltr">Cache</span> هیچ‌گاه به‌جای <span dir="ltr">Source of Truth</span> معرفی نشود.

### هفتهٔ ۱۸: <span dir="ltr">Deposits</span>، <span dir="ltr">Teller</span> و <span dir="ltr">Cash</span>

**فنی و دامینی**

- چرخهٔ افتتاح، فعال‌سازی، واریز، برداشت، <span dir="ltr">Hold</span>، <span dir="ltr">Dormancy</span> و بستن
- سود، تمدید، شکست سپرده و <span dir="ltr">Business Calendar</span>
- <span dir="ltr">Cut-off</span>، <span dir="ltr">Back Value Date</span> و <span dir="ltr">Monetary Precision</span>
- <span dir="ltr">Teller Session</span>، <span dir="ltr">Cashbox</span>، <span dir="ltr">Branch Vault</span>، <span dir="ltr">Shortage/Overage</span> و <span dir="ltr">Cash Transfer</span>

**کد و تمرین**

- برش کامل <span dir="ltr">`BreakTermDeposit`</span>
- محاسبهٔ سود مستحق، تفاوت سود پرداختی و مبلغ اصلاح
- <span dir="ltr">Event</span> و <span dir="ltr">Accounting Fact</span>های لازم
- تست <span dir="ltr">Duplicate</span>، <span dir="ltr">Back-dated</span> و شکست پس از محاسبه/قبل از ثبت

**تحویل‌دادنی**

- پروندهٔ کامل <span dir="ltr">Deposits</span> و <span dir="ltr">Teller/Cash</span>
- <span dir="ltr">Deposit Lifecycle State Machine</span>
- <span dir="ltr">Deposit Event Catalog</span>
- سناریوی نهایی شمارهٔ ۳ در وضعیت <span dir="ltr">Beta</span>

**معیار قبولی**

- <span dir="ltr">Deposits</span> مالک محاسبه و وضعیت عملیاتی است؛ <span dir="ltr">Accounting</span> فقط اثر مالی را ثبت می‌کند.
- <span dir="ltr">Reversal/Correction</span> با <span dir="ltr">Rollback</span> ساده اشتباه نشود.

---

## اسپرینت ۱۰ — عمق دامین: <span dir="ltr">Lending</span>، <span dir="ltr">Collections</span> و <span dir="ltr">Payments</span>

### هفتهٔ ۱۹: <span dir="ltr">Lending</span>، <span dir="ltr">Collateral</span> و <span dir="ltr">Collections</span>

**فنی و دامینی**

- <span dir="ltr">Application</span>، <span dir="ltr">Credit Decision</span>، <span dir="ltr">Approval</span>، <span dir="ltr">Agreement</span> و <span dir="ltr">Disbursement</span>
- <span dir="ltr">Schedule Generation</span>، <span dir="ltr">Accrual</span>، <span dir="ltr">Payment Allocation</span> و <span dir="ltr">Settlement</span>
- <span dir="ltr">Collateral Valuation/Allocation/Release</span>
- <span dir="ltr">Delinquency Detection</span>، <span dir="ltr">Collection Case</span>، <span dir="ltr">Restructuring</span>، <span dir="ltr">Write-off</span> و <span dir="ltr">Recovery</span>
- <span dir="ltr">Decision Table</span> و <span dir="ltr">Long-running Workflow</span>

**کد و تمرین**

- <span dir="ltr">Schedule Generator</span> با قواعد گردکردن
- <span dir="ltr">Projection</span> تشخیص <span dir="ltr">Delinquency</span>
- تکمیل برش اعطا و ارتباط آن با <span dir="ltr">Collateral/Collections</span> بدون تصاحب مالکیت

**تحویل‌دادنی**

- پرونده‌های <span dir="ltr">Lending</span>، <span dir="ltr">Collateral</span> و <span dir="ltr">Collections</span>
- <span dir="ltr">Decision/Data Ownership Matrix</span>
- سناریوی نهایی شمارهٔ ۱ در وضعیت <span dir="ltr">Beta</span>

**معیار قبولی**

- <span dir="ltr">Lending</span> مالک بدهی است؛ <span dir="ltr">Collections</span> مالک پرونده و اقدام وصول؛ <span dir="ltr">Collateral</span> مالک وضعیت وثیقه؛ <span dir="ltr">Accounting</span> مالک دفتر مالی.

### هفتهٔ ۲۰: <span dir="ltr">Payments</span>، <span dir="ltr">Cards</span>، <span dir="ltr">Channels</span> و <span dir="ltr">Checks</span>

**فنی و دامینی**

- <span dir="ltr">Payment Order</span> و <span dir="ltr">Payment State Machine</span>
- <span dir="ltr">Authorization</span>، <span dir="ltr">Clearing</span> و <span dir="ltr">Settlement</span>
- <span dir="ltr">Reversal</span>، <span dir="ltr">Refund</span> و <span dir="ltr">Return</span>
- <span dir="ltr">Internal Transfer</span>، پایا/ساتنا، <span dir="ltr">Card Transaction</span> و <span dir="ltr">Cheque Lifecycle</span>
- <span dir="ltr">Duplicate Payment Prevention</span> و <span dir="ltr">External Network Adapter</span>
- جایگاه <span dir="ltr">ISO 20022</span> در مرز تبادل و <span dir="ltr">Anti-Corruption Layer</span>، بدون تحمیل مستقیم مدل پیام بیرونی به <span dir="ltr">Domain Model</span> داخلی

**کد و تمرین**

- <span dir="ltr">`PaymentOrder`</span> برای انتقال بین‌شعبه‌ای
- <span dir="ltr">Debit/Credit Idempotent</span> در <span dir="ltr">Deposits</span>
- <span dir="ltr">Branch/Inter-branch Accounting Facts</span>
- تست گم‌شدن پاسخ، <span dir="ltr">Reversal</span> و <span dir="ltr">Settlement</span> دیرهنگام

**تحویل‌دادنی**

- پروندهٔ کامل <span dir="ltr">Payments</span> و <span dir="ltr">Capability Card</span>های <span dir="ltr">Cards/Channels/Checks</span>
- مرزبندی <span dir="ltr">Payments</span> و <span dir="ltr">Deposits</span>
- سناریوی نهایی شمارهٔ ۲ در وضعیت <span dir="ltr">Beta</span>

**<span dir="ltr">Gate</span> اسپرینت**

یک پروندهٔ تسهیلات معوق و یک انتقال بین‌شعبه‌ای دفاع می‌شوند. هر <span dir="ltr">State</span>، داده و تصمیم باید دقیقاً یک مالک داشته باشد و <span dir="ltr">Channel</span> نباید مالک مانده یا فرایند پرداخت شود.

---

## اسپرینت ۱۱ — <span dir="ltr">Micro-frontend</span> و <span dir="ltr">Production Architecture</span>

### هفتهٔ ۲۱: <span dir="ltr">Micro-frontend Platform</span> برای <span dir="ltr">Widget</span>های مستقل

**فنی**

- <span dir="ltr">App Shell</span>، <span dir="ltr">Runtime Discovery</span> و <span dir="ltr">Widget Manifest</span>
- <span dir="ltr">Web Component Contract</span> و <span dir="ltr">Framework Isolation</span>
- <span dir="ltr">Independent Build/Version/Deployment</span>
- <span dir="ltr">Shared Design Tokens</span> در برابر <span dir="ltr">Shared Runtime State</span>
- <span dir="ltr">BFF</span>، <span dir="ltr">API Gateway</span>، <span dir="ltr">Auth Propagation</span> و <span dir="ltr">Feature Flag</span>
- <span dir="ltr">Failure Isolation</span> و <span dir="ltr">Compatibility Policy</span>

**کد و تمرین**

- <span dir="ltr">Portal Shell</span> با <span dir="ltr">Runtime Manifest</span>
- <span dir="ltr">`deposit-widget`</span> و <span dir="ltr">`lending-widget`</span> با <span dir="ltr">Build</span> و <span dir="ltr">Version</span> مستقل
- بارگذاری تنبل، انتقال <span dir="ltr">Context</span> مجاز و جلوگیری از دسترسی مستقیم به <span dir="ltr">State</span> داخلی <span dir="ltr">Widget</span> دیگر
- ازکارانداختن عمدی یک <span dir="ltr">Widget</span> و اثبات سلامت <span dir="ltr">Shell</span> و <span dir="ltr">Widget</span> دیگر

**تحویل‌دادنی**

- <span dir="ltr">Micro-frontend Architecture</span>
- <span dir="ltr">Widget Manifest Schema</span>
- <span dir="ltr">UI Ownership/Compatibility Matrix</span>
- <span dir="ltr">ADR-009: Web Components/Module Federation/</span>سایر گزینه‌ها

**معیار قبولی**

- افزودن <span dir="ltr">Widget</span> جدید نیازمند <span dir="ltr">Build</span> مجدد همهٔ <span dir="ltr">Widget</span>ها نباشد.
- <span dir="ltr">Contract</span> و <span dir="ltr">Design System</span> مشترک باشد، ولی <span dir="ltr">Business State</span> مشترک و پنهان ایجاد نشود.

### هفتهٔ ۲۲: <span dir="ltr">Runtime</span>، <span dir="ltr">SLO</span>، <span dir="ltr">DR</span> و <span dir="ltr">Service Ownership</span>

**فنی**

- <span dir="ltr">Container Image</span>، <span dir="ltr">Kubernetes Deployment/Service/Config/Secret</span>
- <span dir="ltr">Readiness/Liveness/Startup Probe</span>، <span dir="ltr">Resource Request/Limit</span> و <span dir="ltr">HPA</span>
- <span dir="ltr">CI/CD</span>، <span dir="ltr">Migration</span> سازگار دیتابیس، <span dir="ltr">Rolling/Blue-Green/Canary</span> و <span dir="ltr">Rollback Policy</span>
- <span dir="ltr">OpenTelemetry</span>، <span dir="ltr">Dashboard</span> و <span dir="ltr">Alert</span>
- <span dir="ltr">SLI/SLO/Error Budget</span>
- <span dir="ltr">Database HA</span>، <span dir="ltr">Backup/Restore</span>، <span dir="ltr">RTO/RPO</span>، <span dir="ltr">DR</span> و <span dir="ltr">Production Readiness Review</span>
- <span dir="ltr">Secret Management</span>، <span dir="ltr">Network Policy</span> و <span dir="ltr">Least Privilege</span>

**سازمانی**

- <span dir="ltr">Service Owner</span>، <span dir="ltr">Technical Owner</span>، <span dir="ltr">Product Owner</span> و <span dir="ltr">Run Owner</span>
- تعهد مشترک <span dir="ltr">PO</span> و <span dir="ltr">Engineering Lead</span>؛ جلوگیری از جدایی اختیار تولید از تعهد محصول
- <span dir="ltr">Build-and-Run Ownership</span> و نقش <span dir="ltr">Platform/SRE</span>

**کد و تمرین**

- <span dir="ltr">Manifest</span>های <span dir="ltr">Kubernetes</span> برای سرویس‌های اصلی
- <span dir="ltr">Pipeline</span> با <span dir="ltr">Gate</span>های <span dir="ltr">Build</span>، <span dir="ltr">Test</span>، <span dir="ltr">Contract Compatibility</span>، <span dir="ltr">Security Scan</span> و <span dir="ltr">Migration Check</span>
- سه <span dir="ltr">SLO</span> اولیه: اعطا، انتقال وجه و ثبت حسابداری
- توقف یک <span dir="ltr">Pod/Consumer</span> و مشاهدهٔ <span dir="ltr">Recovery</span> و <span dir="ltr">Backlog</span>
- <span dir="ltr">Restore</span> آزمایشی دیتابیس/<span dir="ltr">Projection</span> در محیط <span dir="ltr">Lab</span>

**تحویل‌دادنی**

- <span dir="ltr">Runtime Architecture</span>
- <span dir="ltr">NFR Catalog</span> و <span dir="ltr">SLO Document</span>
- <span dir="ltr">Backup/DR Plan</span> و <span dir="ltr">Runbook</span>
- <span dir="ltr">Service Ownership Map</span> و <span dir="ltr">Team Topology</span>
- <span dir="ltr">Production Readiness Checklist</span>

**<span dir="ltr">Gate</span> اسپرینت**

- <span dir="ltr">Secret</span> در مخزن نباشد.
- <span dir="ltr">Alert</span> به <span dir="ltr">SLI</span> و اثر کاربر متصل باشد، نه فقط <span dir="ltr">CPU.</span>
- <span dir="ltr">RTO/RPO</span> فرضیهٔ کسب‌وکاریِ قابل تصویب معرفی شود، نه عدد تزئینی معماری.

---

## اسپرینت ۱۲ — یکپارچه‌سازی، مهاجرت و دفاع

### هفتهٔ ۲۳: اثبات سه سناریو و <span dir="ltr">Migration Roadmap</span>

**کار اصلی**

- اجرای <span dir="ltr">End-to-End</span> هر سه سناریو
- تکمیل <span dir="ltr">Trace</span>، <span dir="ltr">Event Timeline</span>، <span dir="ltr">Journal</span>، <span dir="ltr">Reconciliation</span> و <span dir="ltr">Failure Evidence</span>
- <span dir="ltr">Contract Test</span> میان سرویس‌ها
- <span dir="ltr">Load/Failure Test</span> نهایی
- طراحی مهاجرت تدریجی از وضع موجود با <span dir="ltr">Strangler</span>، <span dir="ltr">Parallel Run</span>، <span dir="ltr">Data Migration</span> و <span dir="ltr">Cutover</span>

**برای هر سناریو باید ثبت شود**

1. مالک هر تصمیم
2. مالک هر داده
3. <span dir="ltr">Command</span>، <span dir="ltr">API</span> و <span dir="ltr">Event</span>ها
4. <span dir="ltr">Aggregate</span> و <span dir="ltr">Transaction Boundary</span>
5. <span dir="ltr">Ordering</span> و <span dir="ltr">Consistency</span>
6. <span dir="ltr">Duplicate</span> و <span dir="ltr">Out-of-order</span>
7. <span dir="ltr">Timeout</span>، <span dir="ltr">Retry</span> و <span dir="ltr">Failure State</span>
8. <span dir="ltr">Compensation/Reversal/Correction</span>
9. <span dir="ltr">Accounting Fact</span> و <span dir="ltr">Journal</span>
10. <span dir="ltr">Reconciliation</span> و <span dir="ltr">Manual Repair</span>
11. <span dir="ltr">SLO</span> و <span dir="ltr">Observability</span>
12. تیم مالک و مسیر <span dir="ltr">Escalation</span>

**تحویل‌دادنی**

- <span dir="ltr">Evidence Pack</span> سه سناریو
- <span dir="ltr">Migration Roadmap</span> در موج‌های ۰ تا ۴
- <span dir="ltr">Cutover/Reconciliation Checklist</span>
- <span dir="ltr">ADR</span>های نهایی

**معیار قبولی**

- هیچ <span dir="ltr">Dual Write</span> بدون الگوی کنترل و مغایرت‌گیری وجود نداشته باشد.
- <span dir="ltr">Rollback</span> مهاجرت و مالک تصمیم <span dir="ltr">Go/No-Go</span> روشن باشد.

### هفتهٔ ۲۴: دفاع نهایی معماری

**ساختار دفاع ۹۰ دقیقه‌ای**

- ۱۵ دقیقه: <span dir="ltr">Capability</span>، <span dir="ltr">Domain</span> و <span dir="ltr">Context Map</span>
- ۱۵ دقیقه: معماری کد و سرویس‌ها
- ۳۰ دقیقه: سه سناریو، هرکدام ۱۰ دقیقه
- ۱۵ دقیقه: داده، حسابداری، شکست و <span dir="ltr">Reconciliation</span>
- ۱۰ دقیقه: <span dir="ltr">Runtime</span>، <span dir="ltr">SLO</span>، <span dir="ltr">Security</span>، <span dir="ltr">DR</span> و <span dir="ltr">Ownership</span>
- ۵ دقیقه: <span dir="ltr">Migration Roadmap</span> و تصمیم‌های باز

**خروجی نهایی**

1. <span dir="ltr">Banking Capability Map</span>
2. <span dir="ltr">Domain/Subdomain Map</span>
3. <span dir="ltr">Bounded Context Map</span>
4. پرونده‌های ۱۲‌بخشی دامین‌ها
5. <span dir="ltr">Data/Decision Ownership Matrix</span>
6. <span dir="ltr">Service Catalog</span>
7. <span dir="ltr">OpenAPI Catalog</span>
8. <span dir="ltr">AsyncAPI/Event Catalog</span>
9. <span dir="ltr">Accounting Fact/Rule Catalog</span>
10. <span dir="ltr">Logical/Physical Data Model</span>
11. <span dir="ltr">Saga/Failure/Compensation Matrix</span>
12. <span dir="ltr">Runtime/NFR/SLO/DR Architecture</span>
13. <span dir="ltr">ADR Log</span>
14. <span dir="ltr">Service/Team Ownership Map</span>
15. <span dir="ltr">Migration Roadmap</span>
16. کد و تست سه <span dir="ltr">Vertical Slice</span>

**خروجی پس از دفاع**

- <span dir="ltr">Gap List</span> اولویت‌بندی‌شده
- برنامهٔ ۹۰ روزهٔ بعدی
- تصمیم دربارهٔ عمق بعدی: <span dir="ltr">Architecture Leadership</span>، <span dir="ltr">Data/Performance</span>، <span dir="ltr">Platform/SRE</span> یا <span dir="ltr">Banking Domain Specialization</span>

---

## ۱۰. مدل ارزیابی

| حوزه | امتیاز |
|---|---:|
| <span dir="ltr">Capability</span>، <span dir="ltr">Domain Boundary</span> و <span dir="ltr">Ownership</span> | ۲۰ |
| طراحی کد، <span dir="ltr">Aggregate</span>، <span dir="ltr">Refactoring</span> و <span dir="ltr">Test</span> | ۱۵ |
| <span dir="ltr">API/Event Contract</span> و <span dir="ltr">Evolution</span> | ۱۵ |
| <span dir="ltr">Transaction</span>، <span dir="ltr">Consistency</span>، <span dir="ltr">Failure</span> و <span dir="ltr">Reconciliation</span> | ۲۰ |
| <span dir="ltr">Accounting</span>، <span dir="ltr">Data Model</span> و <span dir="ltr">Performance</span> | ۱۵ |
| <span dir="ltr">Security</span>، <span dir="ltr">Observability</span>، <span dir="ltr">SLO</span> و <span dir="ltr">DR</span> | ۱۰ |
| <span dir="ltr">ADR</span>، <span dir="ltr">Team Ownership</span> و کیفیت دفاع | ۵ |
| **جمع** | **۱۰۰** |

### شرط عبور

- امتیاز کل حداقل ۷۵
- هیچ‌یک از چهار حوزهٔ <span dir="ltr">Boundary</span>، <span dir="ltr">Financial Correctness</span>، <span dir="ltr">Failure Handling</span> و <span dir="ltr">Accounting</span> کمتر از ۶۰٪ امتیاز خود نباشد.
- هر سه سناریوی نهایی واقعاً اجرا شوند؛ اسلاید یا <span dir="ltr">Diagram</span> به‌تنهایی کافی نیست.

### <span dir="ltr">Gate</span>های رسمی

| <span dir="ltr">Gate</span> | پایان هفته | پرسش اصلی |
|---|---:|---|
| ۱ | ۴ | آیا <span dir="ltr">Domain Model</span> و مرز کد واقعاً مستقل و قابل آزمون است؟ |
| ۲ | ۸ | آیا مالکیت مانده، تراکنش و <span dir="ltr">Read Model</span> روشن و صحیح است؟ |
| ۳ | ۱۲ | آیا جریان توزیع‌شده بدون <span dir="ltr">Global Transaction</span> و فرض <span dir="ltr">Exactly-once</span> ایمن است؟ |
| ۴ | ۱۶ | آیا مدل حسابداری/داده تحت هم‌زمانی و بار، قابل دفاع است؟ |
| ۵ | ۲۰ | آیا مرز دامین‌های بانکی در سناریوهای واقعی حفظ شده است؟ |
| ۶ | ۲۴ | آیا معماری از <span dir="ltr">Business Capability</span> تا <span dir="ltr">Runtime</span> و <span dir="ltr">Team Ownership</span> کامل است؟ |

## ۱۱. قواعد جلوگیری از پراکندگی

- در طول دوره پروژهٔ دوم ایجاد نمی‌شود.
- <span dir="ltr">Kubernetes</span> پیش از هفتهٔ ۲۲ موضوع اصلی نمی‌شود.
- <span dir="ltr">Kafka</span> پیش از روشن‌شدن مالک و مرز <span dir="ltr">Event</span> در هفتهٔ ۹ وارد طراحی نمی‌شود.
- <span dir="ltr">Microservice</span> بدون <span dir="ltr">ADR</span> و شواهد استخراج نمی‌شود.
- <span dir="ltr">BIAN</span>، نام جدول و ساختار سازمانی جای <span dir="ltr">Domain Discovery</span> را نمی‌گیرند.
- برای نمایش معماری از <span dir="ltr">Diagram</span> بدون <span dir="ltr">Ownership/Decision/Failure</span> استفاده نمی‌شود.
- درصد <span dir="ltr">Code Coverage</span> هدف اصلی نیست؛ پوشش <span dir="ltr">Invariant</span>، <span dir="ltr">Failure</span> و <span dir="ltr">Contract</span> هدف است.
- ابزار جدید فقط وقتی اضافه می‌شود که یک خروجی اجباری برنامه را ممکن کند.
- کد تولیدی بانک در <span dir="ltr">Lab</span> کپی نمی‌شود؛ مسئله و قید آن با دادهٔ ساختگی بازآفرینی می‌شود.

## ۱۲. منابع رسمی حداقلی و ترتیب استفاده

این‌ها مرجع کنترل برنامه‌اند، نه فهرست کتاب‌هایی که باید کامل خوانده شوند.

- هفته‌های ۱ و ۲: [<span dir="ltr">BIAN Service Landscape 14.0</span>](https://bian.org/deliverables/service-landscape/)
- هفته‌های ۲ تا ۴: [<span dir="ltr">Spring Modulith Fundamentals</span>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)، [<span dir="ltr">Module Verification</span>](https://docs.spring.io/spring-modulith/reference/verification.html) و [<span dir="ltr">Module Integration Testing</span>](https://docs.spring.io/spring-modulith/reference/testing.html)
- هفته‌های ۴ تا ۱۰: [<span dir="ltr">Spring Boot Testcontainers</span>](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html)
- هفتهٔ ۶: [<span dir="ltr">OWASP API Security Top 10</span>](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- هفتهٔ ۷: [<span dir="ltr">PostgreSQL Transaction Isolation</span>](https://www.postgresql.org/docs/current/transaction-iso.html)
- هفته‌های ۹ و ۱۰: [<span dir="ltr">AsyncAPI 3.1 Specification</span>](https://www.asyncapi.com/docs/reference/specification/latest)، [<span dir="ltr">Apache Kafka Design</span>](https://kafka.apache.org/41/design/design/)، [<span dir="ltr">Producer Configuration</span>](https://kafka.apache.org/41/configuration/producer-configs/) و [<span dir="ltr">Debezium Outbox Event Router</span>](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
- هفتهٔ ۱۲: [<span dir="ltr">OpenTelemetry Signals</span>](https://opentelemetry.io/docs/concepts/signals/) و [<span dir="ltr">Context Propagation</span>](https://opentelemetry.io/docs/concepts/context-propagation/)
- هفتهٔ ۱۵: [<span dir="ltr">PostgreSQL Declarative Partitioning</span>](https://www.postgresql.org/docs/current/ddl-partitioning.html) و [<span dir="ltr">Oracle Reference Partitioning</span>](https://docs.oracle.com/en/database/oracle/oracle-database/26/vldbg/partition-admin.html)
- هفتهٔ ۲۱: [<span dir="ltr">Webpack Module Federation Concepts</span>](https://webpack.js.org/concepts/module-federation/) برای مقایسه با قرارداد <span dir="ltr">Web Component/Manifest</span>
- هفتهٔ ۲۲: [<span dir="ltr">Kubernetes Deployments</span>](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)، [<span dir="ltr">Horizontal Pod Autoscaling</span>](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)، [<span dir="ltr">Google SRE: Implementing SLOs</span>](https://sre.google/workbook/implementing-slos/) و [<span dir="ltr">Example SLO Document</span>](https://sre.google/workbook/slo-document/)

## ۱۳. ممیزی نهایی پوشش موارد جاافتادهٔ قبلی

| مورد جاافتاده | محل قطعی در نسخهٔ نهایی |
|---|---|
| <span dir="ltr">SOLID</span> و <span dir="ltr">Pattern</span>های کاربردی | هفته‌های ۳ و ۴؛ <span dir="ltr">Refactoring</span> مستمر در <span dir="ltr">Definition of Done</span> |
| <span dir="ltr">Code Smell</span> و <span dir="ltr">Refactoring</span> واقعی | هفتهٔ ۴ و <span dir="ltr">Code Review</span> هر هفته |
| <span dir="ltr">Unit/Integration/Architecture/Contract Test</span> | هفته‌های ۱ تا ۱۰ و سپس به‌صورت مستمر |
| <span dir="ltr">Concurrency/Failure/Performance Test</span> | هفته‌های ۷، ۱۲، ۱۶ و ۲۳ |
| <span dir="ltr">PostgreSQL</span> عملی | هفته‌های ۴، ۷، ۸، ۱۰، ۱۵ و ۱۶ |
| <span dir="ltr">Oracle</span> عمیق | هفته‌های ۷، ۱۵ و ۱۶ |
| <span dir="ltr">CQRS</span> کامل | هفته‌های ۸، ۱۰ و ۱۶ |
| <span dir="ltr">Micro-frontend</span> | هفتهٔ ۲۱ با <span dir="ltr">Shell</span> و دو <span dir="ltr">Widget</span> مستقل |
| <span dir="ltr">IAM</span> و <span dir="ltr">API Security</span> | هفتهٔ ۶؛ تکمیل در هفته‌های ۲۱ و ۲۲ |
| <span dir="ltr">Observability</span> | هفتهٔ ۱۲؛ <span dir="ltr">Production Dashboard/SLO</span> در هفتهٔ ۲۲ |
| <span dir="ltr">Kubernetes</span> و <span dir="ltr">Runtime</span> | هفتهٔ ۲۲ پس از آماده‌شدن نرم‌افزار |
| <span dir="ltr">SLO</span>، <span dir="ltr">DR</span> و <span dir="ltr">Runbook</span> | هفته‌های ۱۲، ۲۲ و ۲۳ |
| <span dir="ltr">Team Topology</span> و اختیار <span dir="ltr">PO/Engineering</span> | هفتهٔ ۲۲ و دفاع هفتهٔ ۲۴ |
| <span dir="ltr">Migration</span> از وضع موجود | هفتهٔ ۲۳ |

## ۱۴. پیش‌هفتهٔ شروع؛ خارج از ۲۴ هفته

این آماده‌سازی یک‌باره حداکثر دو ساعت زمان می‌برد:

1. نصب/کنترل <span dir="ltr">Java 21</span>، <span dir="ltr">Maven</span>، <span dir="ltr">Docker</span> و <span dir="ltr">Git</span>
2. ایجاد مخزن با ساختار پایه
3. اجرای <span dir="ltr">`mvn verify`</span>
4. اجرای <span dir="ltr">PostgreSQL</span> و <span dir="ltr">Kafka</span> با <span dir="ltr">Docker/Testcontainers</span>
5. ثبت پاسخ اولیهٔ خودت به سناریوی «اعطا و واریز به سپرده» بدون مطالعهٔ جدید
6. نمره‌گذاری خط پایه با <span dir="ltr">Rubric</span> نهایی

پاسخ خط پایه در هفتهٔ ۲۴ دوباره ارائه می‌شود تا رشد واقعی قابل مقایسه باشد.

## ۱۵. قرارداد اجرای برنامه در همین گفت‌وگو

### قالب گزارش هر هفته


</div>

<div dir="ltr" align="left">

```text
Week:
Objective:
Banking scenario:
Decisions made:
Code/artifacts produced:
Tests passed/failed:
Failure injected and observed result:
ADR/API/Event/Data changes:
Known risks and open questions:
Definition of Done status:
Self-score (0-100):
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Board</span> دوره فقط این وضعیت‌ها را دارد: <span dir="ltr">`Backlog → Ready → Doing → Review → Gate → Done`</span>. در هر زمان فقط خروجی یک هفته در <span dir="ltr">`Doing`</span> است تا مطالعهٔ چند موضوع جای تکمیل <span dir="ltr">Artifact</span> را نگیرد.

در آغاز هر هفته:

1. درس فشرده و مسئلهٔ بانکی همان هفته ارائه می‌شود.
2. قالب خروجی و <span dir="ltr">Acceptance Test</span> مشخص می‌شود.
3. کد، <span dir="ltr">Diagram</span>، <span dir="ltr">DDL</span> یا تصمیم تو بررسی و نقد می‌شود.
4. خطاها و <span dir="ltr">Failure Scenario</span>ها روی خروجی اعمال می‌شوند.
5. فقط بعد از عبور از <span dir="ltr">Definition of Done</span>، هفته بسته می‌شود.

در <span dir="ltr">Gate</span>ها، ضعف مهم با جلو رفتن صوری پوشانده نمی‌شود. همان بخش با تمرین کوچک‌تر تکرار می‌شود؛ اما نقشهٔ ۲۴ هفته‌ای تغییر مسیر نمی‌دهد مگر اینکه شواهد اجرای واقعی نشان دهد بار زمانی یا پیش‌نیاز فنی اشتباه برآورد شده است.

این سند نقشهٔ راه مرجع است. شروع واقعی از «پیش‌هفته» و سپس هفتهٔ ۱، <span dir="ltr">Capability Map</span> بانک، خواهد بود.

</div>
