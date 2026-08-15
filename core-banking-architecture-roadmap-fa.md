<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# نقشهٔ راه نهایی ۲۴ هفته‌ای معماری نرم‌افزار و <bdi dir="ltr">Core Banking</bdi>

نسخه: ۱٫۰  
تاریخ مبنا: ۱۲ مرداد ۱۴۰۵ / ۳ اوت ۲۰۲۶  
مخاطب: مسیر شخصی‌سازی‌شدهٔ معماری <bdi dir="ltr">Core Banking</bdi>  
مدت: ۲۴ هفته، ۱۲ اسپرینت دوهفته‌ای، هفته‌ای ۴ تا ۶ ساعت

> الحاقیهٔ ۲۴ مرداد ۱۴۰۵ / ۱۵ اوت ۲۰۲۶: از <bdi dir="ltr">Week 02</bdi> دو ریل <bdi dir="ltr">Code Craft</bdi> و <bdi dir="ltr">Core Banking Case File</bdi> به برنامه افزوده شده‌اند. برنامهٔ ۴ تا ۶ ساعتهٔ قبلی «ریل اصلی» باقی می‌ماند و نسخهٔ کامل توسعه‌یافته ۵۱۰ دقیقه در هفته است؛ هیچ سرفصل، <bdi dir="ltr">Gate</bdi> یا <bdi dir="ltr">Artifact</bdi> قبلی حذف یا فشرده نشده است.

## ۱. تصمیم نهایی برنامه

این برنامه یک دورهٔ واحد با دو محور هم‌زمان است:

- محور فنی: طراحی کد، معماری سرویس، معماری توزیع‌شده، داده و تراکنش، معماری اجرایی و سازمانی
- محور دامینی: شناخت <bdi dir="ltr">Core Banking</bdi>، مرزبندی دامین‌ها، مالکیت داده و تصمیم، سرویس‌ها و روابط میان آن‌ها

پروژهٔ ثابت دوره یک <bdi dir="ltr">Core Banking</bdi> آموزشی با شش دامین اصلی است:

1. <bdi dir="ltr">Party</bdi> & <bdi dir="ltr">Customer</bdi>
2. <bdi dir="ltr">Product</bdi> & <bdi dir="ltr">Agreement</bdi>
3. <bdi dir="ltr">Deposits</bdi>
4. <bdi dir="ltr">Lending</bdi>
5. <bdi dir="ltr">Payments</bdi>
6. <bdi dir="ltr">Accounting</bdi>

سه برش عمودی پروژه واقعاً پیاده‌سازی، تست و دفاع می‌شوند:

1. اعطای تسهیلات و واریز مبلغ به سپرده
2. انتقال وجه بین‌شعبه‌ای
3. شکست سپردهٔ بلندمدت و اصلاح سود

هدف ساخت یک <bdi dir="ltr">Core Banking</bdi> کامل تولیدی در ۲۴ هفته نیست. هدف، ساخت معماری کامل و پیاده‌سازی سه جریان باریک اما انتها‌به‌انتهاست؛ به‌اندازه‌ای که بتوان صحت مرزها، تراکنش‌ها، <bdi dir="ltr">Event</bdi>ها، حسابداری، شکست‌ها و الزامات اجرایی را اثبات کرد.

## ۲. نتیجه‌ای که در پایان باید حاصل شود

در پایان هفتهٔ ۲۴ باید بتوانی:

- زنجیرهٔ <bdi dir="ltr">`Capability → Domain → Subdomain → Bounded Context → Module/Service → API/Event`</bdi> را برای یک قابلیت بانکی طی کنی.
- برای هر تصمیم و داده یک مالک صریح تعیین کنی و مشخص کنی چه دامین‌هایی نباید مالک آن باشند.
- میان <bdi dir="ltr">Modular Monolith</bdi> و <bdi dir="ltr">Microservice</bdi> با معیارهای تغییر، تراکنش، تیم، استقرار، مقیاس و ریسک انتخاب کنی.
- <bdi dir="ltr">Aggregate</bdi>، <bdi dir="ltr">Invariant</bdi> و <bdi dir="ltr">Transaction Boundary</bdi> را در کد <bdi dir="ltr">Java/Spring</bdi> پیاده‌سازی و آزمون کنی.
- <bdi dir="ltr">API</bdi> همگام و قرارداد <bdi dir="ltr">Event</bdi> را همراه با <bdi dir="ltr">Idempotency</bdi>، <bdi dir="ltr">Versioning</bdi> و <bdi dir="ltr">Error Model</bdi> طراحی کنی.
- <bdi dir="ltr">Outbox</bdi>، <bdi dir="ltr">Inbox</bdi>، <bdi dir="ltr">Kafka</bdi>، <bdi dir="ltr">Saga/Process Manager</bdi>، <bdi dir="ltr">Retry</bdi>، <bdi dir="ltr">Timeout</bdi>، <bdi dir="ltr">Compensation</bdi>، <bdi dir="ltr">Reversal</bdi> و <bdi dir="ltr">Reconciliation</bdi> را در یک جریان مالی به‌درستی به‌کار ببری.
- ماندهٔ عملیاتی، <bdi dir="ltr">Ledger</bdi>، <bdi dir="ltr">Subledger</bdi> و <bdi dir="ltr">GL</bdi> را از هم تفکیک کنی.
- مدل دادهٔ <bdi dir="ltr">Oracle</bdi> و <bdi dir="ltr">PostgreSQL</bdi> را براساس <bdi dir="ltr">Query Pattern</bdi>، <bdi dir="ltr">Locking</bdi>، <bdi dir="ltr">Partitioning</bdi>، <bdi dir="ltr">Indexing</bdi> و <bdi dir="ltr">Retention</bdi> طراحی کنی.
- برای سرویس حیاتی <bdi dir="ltr">SLI/SLO</bdi>، <bdi dir="ltr">Trace</bdi>، <bdi dir="ltr">Metric</bdi>، <bdi dir="ltr">Log</bdi>، <bdi dir="ltr">Runbook</bdi>، <bdi dir="ltr">RTO/RPO</bdi> و مالک <bdi dir="ltr">Build/Run</bdi> تعیین کنی.
- معماری را در برابر محصول، توسعه، زیرساخت، عملیات و حسابداری با <bdi dir="ltr">ADR</bdi> و شواهد اجرایی دفاع کنی.

## ۳. پنج لایهٔ فنی و جای قطعی آن‌ها

| لایه | پوشش اصلی | تمرین مستمر | شاهد نهایی |
|---|---|---|---|
| ۱. طراحی کد | هفته‌های ۱ تا ۶ | <bdi dir="ltr">Refactoring</bdi>، <bdi dir="ltr">Unit Test</bdi> و <bdi dir="ltr">Code Review</bdi> در تمام ۲۴ هفته | <bdi dir="ltr">Domain Model</bdi> تمیز، <bdi dir="ltr">Pattern</bdi>های موجه، تست‌های قواعد و <bdi dir="ltr">Architecture Test</bdi> |
| ۲. معماری سرویس | هفته‌های ۲ تا ۶ و ۹ | بازبینی <bdi dir="ltr">Boundary</bdi> در هر <bdi dir="ltr">ADR</bdi> و هر <bdi dir="ltr">API/Event</bdi> | <bdi dir="ltr">Modular Monolith</bdi> معتبر، <bdi dir="ltr">Service Candidate Map</bdi> و تصمیم‌های استخراج |
| ۳. معماری توزیع‌شده | هفته‌های ۹ تا ۱۲ و ۲۳ | تست <bdi dir="ltr">Duplicate</bdi>، <bdi dir="ltr">Out-of-order</bdi> و <bdi dir="ltr">Failure</bdi> در جریان‌های بعدی | <bdi dir="ltr">Outbox/Inbox</bdi>، <bdi dir="ltr">Kafka</bdi>، <bdi dir="ltr">Process Manager</bdi>، <bdi dir="ltr">Failure Matrix</bdi> و سه جریان <bdi dir="ltr">E2E</bdi> |
| ۴. داده و تراکنش | هفته‌های ۷، ۸ و ۱۳ تا ۱۶ | بررسی مالکیت و <bdi dir="ltr">Consistency</bdi> در همهٔ دامین‌ها | مدل <bdi dir="ltr">Oracle/PostgreSQL</bdi>، <bdi dir="ltr">Ledger/Subledger</bdi>، <bdi dir="ltr">CQRS</bdi>، <bdi dir="ltr">Locking</bdi> و <bdi dir="ltr">Performance Test</bdi> |
| ۵. معماری اجرایی و سازمانی | هفته‌های ۵، ۶، ۱۲ و ۲۱ تا ۲۴ | <bdi dir="ltr">Security</bdi>، <bdi dir="ltr">Observability</bdi> و <bdi dir="ltr">Ownership</bdi> از میانهٔ دوره | <bdi dir="ltr">IAM</bdi>، <bdi dir="ltr">Micro-frontend</bdi>، <bdi dir="ltr">Kubernetes</bdi>، <bdi dir="ltr">SLO/DR</bdi>، <bdi dir="ltr">Team/Service Ownership</bdi> و <bdi dir="ltr">Migration Roadmap</bdi> |

محور دامین بانکی در همهٔ هفته‌ها فعال است؛ موضوعات فنی هیچ‌گاه روی مثال فروشگاه یا سفارش عمومی تمرین نمی‌شوند.

## ۴. اصلاحات قطعی نسبت به نسخهٔ قبلی

1. کدنویسی، تست و <bdi dir="ltr">Refactoring</bdi> یک ریل دائمی است، نه موضوع دو هفتهٔ خاص.
2. <bdi dir="ltr">PostgreSQL</bdi> به‌صورت عملی استفاده می‌شود و <bdi dir="ltr">Oracle</bdi> به‌صورت مقایسه‌ای و در طراحی فیزیکی عمیق می‌شود.
3. <bdi dir="ltr">CQRS</bdi> فقط یک اصطلاح یا <bdi dir="ltr">Projection</bdi> ساده نیست؛ <bdi dir="ltr">Command Model</bdi>، <bdi dir="ltr">Read Model</bdi>، <bdi dir="ltr">Lag</bdi>، <bdi dir="ltr">Rebuild</bdi> و <bdi dir="ltr">Reconciliation</bdi> پیاده می‌شوند.
4. <bdi dir="ltr">IAM</bdi> از هفتهٔ ۶، <bdi dir="ltr">Observability</bdi> از هفتهٔ ۱۲ و <bdi dir="ltr">SLO</bdi> از هفتهٔ ۲۲ وارد می‌شوند؛ همگی در یک هفته فشرده نشده‌اند.
5. <bdi dir="ltr">Micro-frontend</bdi> یک تمرین مستقل در هفتهٔ ۲۱ دارد و با نیاز «افزودن <bdi dir="ltr">Widget</bdi> توسط سامانه‌ها و تکنولوژی‌های مختلف» طراحی می‌شود.
6. <bdi dir="ltr">BIAN</bdi> فهرست آمادهٔ <bdi dir="ltr">Microservice</bdi> نیست؛ برای کنترل پوشش <bdi dir="ltr">Capability</bdi>ها و زبان مشترک استفاده می‌شود.
7. ابتدا <bdi dir="ltr">Modular Monolith</bdi> ساخته می‌شود؛ استخراج سرویس فقط پس از مشاهدهٔ مرز، وابستگی و نیاز استقرار مستقل انجام می‌گیرد.
8. سه سناریوی نهایی از ابتدا ثابت می‌مانند تا همهٔ موضوعات روی یک پروژه انباشته شوند.

## ۵. سطح هدف و حدود برنامه

این برنامه برای سطح فعلی تو طراحی شده است: تجربهٔ طولانی تحلیل و طراحی سامانه‌های بانکی، مدیریت محصول و توسعه، و آشنایی عملی با <bdi dir="ltr">Java</bdi>، <bdi dir="ltr">Spring</bdi>، <bdi dir="ltr">Oracle</bdi>، <bdi dir="ltr">DB2</bdi>، <bdi dir="ltr">Kafka</bdi> و <bdi dir="ltr">Docker.</bdi> بنابراین آموزش <bdi dir="ltr">Syntax</bdi> جاوا، <bdi dir="ltr">CRUD</bdi> مقدماتی یا مبانی عمومی بانکداری در آن جایی ندارد.

در ۹۶ تا ۱۴۴ ساعت، خروجی واقع‌بینانه «معمار راهکار بانکیِ قادر به طراحی و نمونه‌سازی» است؛ نه <bdi dir="ltr">DBA</bdi> اوراکل، مدیر <bdi dir="ltr">Kubernetes</bdi>، متخصص امنیت یا توسعه‌دهندهٔ ارشد <bdi dir="ltr">Frontend.</bdi> در موضوعات تخصصی، باید بتوانی تصمیم درست بگیری، سؤال درست بپرسی و طرح را اعتبارسنجی کنی؛ تسلط عملی عمیق هر تخصص یک مسیر مستقل است.

## ۶. ریتم اجرایی هر هفته

### برنامهٔ استاندارد شش‌ساعته

| فعالیت | زمان |
|---|---:|
| مطالعهٔ هدایت‌شده و بحث مفهومی | ۹۰ دقیقه |
| تحلیل دامین و ترسیم مدل | ۷۵ دقیقه |
| کدنویسی و تست | ۱۳۵ دقیقه |
| <bdi dir="ltr">Failure/Performance/Security Exercise</bdi> | ۳۰ دقیقه |
| تکمیل <bdi dir="ltr">ADR</bdi>، <bdi dir="ltr">Catalog</bdi> یا پروندهٔ دامین | ۳۰ دقیقه |

### نسخهٔ حداقلی چهارساعته

| فعالیت | زمان |
|---|---:|
| مفهوم و منبع اصلی | ۶۰ دقیقه |
| تحلیل دامین | ۴۵ دقیقه |
| کدنویسی و تست | ۱۰۵ دقیقه |
| مستندسازی و دفاع کوتاه | ۳۰ دقیقه |

اگر یک هفته فقط چهار ساعت زمان وجود داشت، دامنهٔ پیاده‌سازی کوچک می‌شود؛ تست، خروجی و <bdi dir="ltr">Gate</bdi> حذف نمی‌شوند.

### چرخهٔ ثابت کار

1. یادگیری مفهوم روی یک مسئلهٔ بانکی مشخص
2. مدل‌سازی و تصمیم معماری
3. پیاده‌سازی یک <bdi dir="ltr">Vertical Slice</bdi> کوچک
4. شکستن عمدی راه‌حل با تست شکست یا هم‌زمانی
5. <bdi dir="ltr">Refactor</bdi>، ثبت <bdi dir="ltr">ADR</bdi> و دفاع ده‌دقیقه‌ای

### دو ریل افزوده از <bdi dir="ltr">Week 01</bdi>

پس از تکمیل چرخهٔ اصلی، هر هفته دو جلسهٔ مستقل اجرا می‌شود:

| ریل افزوده | زمان | خروجی |
|---|---:|---|
| <bdi dir="ltr">Code Craft Lab</bdi> | ۱۰۵ دقیقه | <bdi dir="ltr">Baseline</bdi>، <bdi dir="ltr">Smell Map</bdi>، <bdi dir="ltr">Characterization Test</bdi>، <bdi dir="ltr">Refactor</bdi>، <bdi dir="ltr">Pattern Decision</bdi>، <bdi dir="ltr">Edge Test</bdi> و <bdi dir="ltr">Self-review</bdi> |
| <bdi dir="ltr">Core Banking Case File</bdi> | ۴۵ دقیقه | <bdi dir="ltr">Timeline</bdi>، معماری/فناوری جاری، <bdi dir="ltr">Domain hypothesis</bdi>، شکست‌ها، دستاورد تازه و درس انتقالی |

نقشهٔ <bdi dir="ltr">Pattern</bdi>ها و پرونده‌های پیشنهادی <bdi dir="ltr">Week 01</bdi> تا <bdi dir="ltr">Week 24</bdi> در [الحاقیهٔ ثابت هفتگی](docs/course/expanded-weekly-tracks.md) نگهداری می‌شود. موضوع هر پرونده هنگام شروع هفته با منابع جاری دوباره کنترل خواهد شد.

## ۷. <bdi dir="ltr">Definition of Done</bdi> هفتگی

هیچ هفته‌ای صرفاً با «خواندن مطالب» تمام‌شده محسوب نمی‌شود. خروجی هفتگی باید شرایط زیر را داشته باشد:

- <bdi dir="ltr">Artifact</bdi> یا کد در <bdi dir="ltr">Git</bdi> ثبت و با شمارهٔ هفته <bdi dir="ltr">Tag</bdi> شده باشد.
- <bdi dir="ltr">`mvn verify`</bdi> موفق باشد.
- قواعد دامینی جدید <bdi dir="ltr">Unit Test</bdi> داشته باشند.
- مرزهای جدید <bdi dir="ltr">Architecture Test</bdi> یا <bdi dir="ltr">Module Verification</bdi> داشته باشند.
- تغییر قرارداد با <bdi dir="ltr">OpenAPI</bdi> یا <bdi dir="ltr">AsyncAPI</bdi> ثبت شده باشد.
- دست‌کم یک مسیر منفی، <bdi dir="ltr">Failure</bdi> یا <bdi dir="ltr">Edge Case</bdi> آزموده شده باشد.
- تصمیم غیر بدیهی در <bdi dir="ltr">ADR</bdi> ثبت شده باشد.
- بتوانی در ده دقیقه توضیح بدهی: مالک داده کیست، مرز تراکنش کجاست و در شکست چه رخ می‌دهد.

در هفته‌هایی که یک مورد موضوعیت ندارد، در گزارش هفته با عبارت <bdi dir="ltr">`Not Applicable`</bdi> و دلیل صریح ثبت می‌شود؛ خالی گذاشته نمی‌شود.

### قرارداد مستندسازی

- <bdi dir="ltr">Capability Map</bdi> برای سلسله‌مراتب قابلیت‌ها
- <bdi dir="ltr">Context Map</bdi> برای رابطهٔ دامین‌ها
- <bdi dir="ltr">C4 System/Container/Component</bdi> برای معماری ایستا
- <bdi dir="ltr">Sequence Diagram</bdi> برای جریان بین سرویس‌ها
- <bdi dir="ltr">State Machine</bdi> برای چرخهٔ عمر و <bdi dir="ltr">Process Manager</bdi>
- <bdi dir="ltr">ERD</bdi> برای مدل داده
- <bdi dir="ltr">ADR</bdi> با قالب ثابت: <bdi dir="ltr">Context</bdi>، <bdi dir="ltr">Forces</bdi>، <bdi dir="ltr">Options</bdi>، <bdi dir="ltr">Decision</bdi>، <bdi dir="ltr">Consequences</bdi>، <bdi dir="ltr">Verification</bdi> و <bdi dir="ltr">Revisit Trigger</bdi>

هر <bdi dir="ltr">Diagram</bdi> باید <bdi dir="ltr">Version</bdi>، <bdi dir="ltr">Scope</bdi> و مالک اجزای اصلی را نشان دهد. <bdi dir="ltr">Diagram</bdi>ی که مرز، مالکیت یا هدف تصمیم را روشن نکند، خروجی معماری محسوب نمی‌شود.

## ۸. خط پایهٔ فنی پروژه

### فناوری‌ها

- <bdi dir="ltr">Java 21 LTS</bdi>؛ انتخابی محافظه‌کارانه برای تمرکز بر معماری و سازگاری سازمانی
- <bdi dir="ltr">Spring Boot 4.1</bdi> و <bdi dir="ltr">Spring Modulith 2.1</bdi>
- <bdi dir="ltr">Maven</bdi>
- <bdi dir="ltr">PostgreSQL</bdi> برای اجرای روزانه و تست‌های <bdi dir="ltr">Integration/Concurrency</bdi>
- <bdi dir="ltr">Oracle 23ai</bdi> برای <bdi dir="ltr">DDL</bdi>، <bdi dir="ltr">Partitioning</bdi>، <bdi dir="ltr">Query Plan</bdi> و تفاوت‌های فیزیکی
- <bdi dir="ltr">Apache Kafka 4.1</bdi>
- <bdi dir="ltr">Testcontainers</bdi> برای <bdi dir="ltr">PostgreSQL</bdi>، <bdi dir="ltr">Kafka</bdi> و تست <bdi dir="ltr">Integration</bdi>
- <bdi dir="ltr">OpenAPI 3.1</bdi> برای <bdi dir="ltr">API</bdi>های همگام
- <bdi dir="ltr">AsyncAPI 3.1</bdi> برای قراردادهای پیام
- <bdi dir="ltr">Docker Compose</bdi> برای محیط توسعه
- <bdi dir="ltr">OpenTelemetry</bdi> برای <bdi dir="ltr">Trace</bdi>، <bdi dir="ltr">Metric</bdi> و <bdi dir="ltr">Log Correlation</bdi>
- <bdi dir="ltr">Prometheus</bdi> و <bdi dir="ltr">Grafana</bdi>؛ یک <bdi dir="ltr">Backend</bdi> سازگار با <bdi dir="ltr">OpenTelemetry</bdi> برای <bdi dir="ltr">Trace</bdi>
- <bdi dir="ltr">Kubernetes Manifest</bdi> در هفتهٔ ۲۲؛ ادارهٔ کلاستر خارج از محدودهٔ دوره است
- <bdi dir="ltr">React/Vite</bdi> برای <bdi dir="ltr">Shell</bdi> و <bdi dir="ltr">Widget</bdi> نمونه؛ قرارداد اتصال <bdi dir="ltr">Micro-frontend</bdi> مبتنی بر <bdi dir="ltr">Runtime Manifest</bdi> و <bdi dir="ltr">Web Component</bdi> خواهد بود تا به یک <bdi dir="ltr">Framework</bdi> محدود نشود

<bdi dir="ltr">Spring Boot 4.1</bdi> حداقل <bdi dir="ltr">Java 17</bdi> می‌خواهد و با <bdi dir="ltr">Java 26</bdi> نیز سازگار است؛ بنابراین <bdi dir="ltr">Java 21</bdi> انتخاب محدودکننده‌ای برای این پروژه نیست. این انتخاب عمدی است تا زمان دوره صرف قابلیت‌های زبان جدید نشود.

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


تا پایان هفتهٔ ۸، راه‌حل اصلی <bdi dir="ltr">Modular Monolith</bdi> است. در هفته‌های ۹ و ۱۰ فقط ماژول‌هایی استخراج می‌شوند که <bdi dir="ltr">ADR</bdi> آن‌ها استخراج را توجیه کرده باشد. <bdi dir="ltr">Tag</bdi> مخزن امکان مقایسهٔ قبل و بعد را نگه می‌دارد.

## ۹. مدل خروجی دامین‌ها

### عمق بررسی

| سطح | دامین‌ها | خروجی مورد انتظار |
|---|---|---|
| عمیق | <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Payments</bdi>، <bdi dir="ltr">Accounting</bdi> | مدل، کد، داده، <bdi dir="ltr">API/Event</bdi>، شکست، حسابداری و کارایی |
| تفصیلی | <bdi dir="ltr">Party/Customer</bdi>، <bdi dir="ltr">Product/Agreement</bdi>، <bdi dir="ltr">Teller/Cash</bdi>، <bdi dir="ltr">Collateral</bdi>، <bdi dir="ltr">Collections</bdi> | پروندهٔ کامل، مرزبندی، <bdi dir="ltr">Catalog</bdi> و نمونهٔ قرارداد |
| معماری کلان | <bdi dir="ltr">Cards</bdi>، <bdi dir="ltr">Channels</bdi>، <bdi dir="ltr">Checks</bdi>، <bdi dir="ltr">Fees</bdi>، <bdi dir="ltr">Limits</bdi>، <bdi dir="ltr">AML</bdi>، <bdi dir="ltr">Fraud</bdi>، <bdi dir="ltr">Risk</bdi>، <bdi dir="ltr">IFRS</bdi>، <bdi dir="ltr">Regulatory Reporting</bdi> | <bdi dir="ltr">Capability Card</bdi>، مالکیت، نوع ارتباط و وابستگی |

### پروندهٔ ثابت ۱۲‌بخشی هر دامین

1. هدف، دامنه و موارد خارج از دامنه
2. <bdi dir="ltr">Capability</bdi>ها و <bdi dir="ltr">Use Case</bdi>های اصلی
3. زبان مشترک و مفاهیم دامینی
4. <bdi dir="ltr">Aggregate</bdi>ها، <bdi dir="ltr">State Machine</bdi>ها و <bdi dir="ltr">Invariant</bdi>ها
5. داده‌ها و تصمیم‌های تحت مالکیت
6. داده‌ها و تصمیم‌هایی که نباید مالک آن‌ها باشد
7. <bdi dir="ltr">Module/Service Candidate</bdi>ها و دلیل مرزبندی
8. <bdi dir="ltr">API</bdi>های ورودی و خروجی
9. <bdi dir="ltr">Domain Event</bdi>ها و <bdi dir="ltr">Integration Event</bdi>های تولیدی/مصرفی
10. <bdi dir="ltr">Context Map</bdi>، <bdi dir="ltr">Upstream/Downstream</bdi> و نوع وابستگی
11. <bdi dir="ltr">Transaction</bdi>، <bdi dir="ltr">Consistency</bdi>، <bdi dir="ltr">Idempotency</bdi>، نقاط شکست و <bdi dir="ltr">Reconciliation</bdi>
12. تیم مالک، <bdi dir="ltr">SLO</bdi>، <bdi dir="ltr">Security</bdi>، <bdi dir="ltr">Audit</bdi>، <bdi dir="ltr">Retention</bdi> و سایر <bdi dir="ltr">NFR</bdi>ها

### فرضیهٔ اولیهٔ مالکیت

| موضوع | مالک اولیه | نکته |
|---|---|---|
| هویت <bdi dir="ltr">Party</bdi> و وضعیت <bdi dir="ltr">Customer</bdi> | <bdi dir="ltr">Customer</bdi> | <bdi dir="ltr">Lending</bdi> یا <bdi dir="ltr">Deposits</bdi> فقط <bdi dir="ltr">Reference/Snapshot</bdi> لازم را نگه می‌دارند. |
| تعریف و نسخهٔ <bdi dir="ltr">Product/Pricing</bdi> | <bdi dir="ltr">Product</bdi> | شرایط قرارداد منعقدشده با تغییر <bdi dir="ltr">Product</bdi> عوض نمی‌شود. |
| شرایط قطعی قرارداد | <bdi dir="ltr">Agreement</bdi> در دامین صاحب قرارداد | <bdi dir="ltr">Lending/Deposits Snapshot</bdi> مؤثر را مالک است. |
| ماندهٔ قابل برداشت و <bdi dir="ltr">Hold</bdi> سپرده | <bdi dir="ltr">Deposits</bdi> | <bdi dir="ltr">Accounting</bdi> نباید ماندهٔ عملیاتی سپرده را کنترل کند. |
| ماندهٔ اصل، برنامه و بدهی تسهیلات | <bdi dir="ltr">Lending</bdi> | <bdi dir="ltr">Accounting</bdi> دفتر مالی متناظر را نگه می‌دارد، نه تصمیم وصول را. |
| <bdi dir="ltr">Payment Order</bdi>، <bdi dir="ltr">Clearing</bdi> و <bdi dir="ltr">Settlement State</bdi> | <bdi dir="ltr">Payments</bdi> | <bdi dir="ltr">Channel</bdi> فقط درخواست و نمایش را مالک است. |
| <bdi dir="ltr">Journal</bdi>، <bdi dir="ltr">Subledger</bdi> و <bdi dir="ltr">GL</bdi> | <bdi dir="ltr">Accounting</bdi> | رویداد کسب‌وکار را ترجمه می‌کند؛ منطق عملیاتی دامین را مالک نمی‌شود. |
| وضعیت یک فرایند چنددامینی | <bdi dir="ltr">Process Manager</bdi> | نباید داده یا قواعد داخلی دامین‌ها را تصاحب کند. |

این جدول تصمیم نهایی معماری نیست؛ فرضیه‌ای است که در طول دوره با سناریو و شواهد اصلاح می‌شود.

---

# برنامهٔ ۲۴ هفته‌ای

## اسپرینت ۱ — نقشهٔ بانک، زبان و مرزها

### هفتهٔ ۱: <bdi dir="ltr">Capability</bdi> تا <bdi dir="ltr">API/Event</bdi>

**فنی**

- تفاوت <bdi dir="ltr">Business Architecture</bdi>، <bdi dir="ltr">Solution Architecture</bdi> و <bdi dir="ltr">Software Architecture</bdi>
- <bdi dir="ltr">Coupling</bdi>، <bdi dir="ltr">Cohesion</bdi>، <bdi dir="ltr">Encapsulation</bdi> و <bdi dir="ltr">Information Hiding</bdi>
- تفاوت <bdi dir="ltr">System</bdi>، <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Subdomain</bdi>، <bdi dir="ltr">Bounded Context</bdi>، <bdi dir="ltr">Module</bdi> و <bdi dir="ltr">Service</bdi>
- زنجیرهٔ کامل <bdi dir="ltr">`Capability → … → API/Event`</bdi>

**دامینی**

- ترسیم <bdi dir="ltr">Capability Map</bdi> سطح ۱ بانک
- طبقه‌بندی «هستهٔ بانکداری»، «عملیات و خدمات بانکداری»، «سامانه‌های سازمانی» و «اکوسیستم دیجیتال»
- استفاده از <bdi dir="ltr">BIAN 14.0</bdi> برای یافتن شکاف‌ها، نه تبدیل هر <bdi dir="ltr">Service Domain</bdi> به <bdi dir="ltr">Microservice</bdi>

**کد و تمرین**

- ایجاد مخزن و <bdi dir="ltr">Pipeline</bdi> اولیهٔ <bdi dir="ltr">`mvn verify`</bdi>
- ساخت <bdi dir="ltr">Value Object</bdi>های <bdi dir="ltr">`Money`</bdi>، <bdi dir="ltr">`AccountId`</bdi>، <bdi dir="ltr">`CustomerId`</bdi> و <bdi dir="ltr">`BranchId`</bdi>
- آزمون برابری، <bdi dir="ltr">Currency</bdi>، گردکردن و ورودی نامعتبر

**تحویل‌دادنی**

- <bdi dir="ltr">Capability Map</bdi> نسخهٔ ۱
- واژه‌نامهٔ حداقل ۴۰ اصطلاح کلیدی
- پاسخ معماری اولیه به سه سناریوی نهایی برای ثبت خط پایه

**معیار قبولی**

- هیچ <bdi dir="ltr">Service Candidate</bdi> بدون <bdi dir="ltr">Capability</bdi> و مالک کسب‌وکار معرفی نشده باشد.
- بتوان تفاوت <bdi dir="ltr">BIAN Service Domain</bdi> با <bdi dir="ltr">Deployable Microservice</bdi> را روشن توضیح داد.

**ریل‌های افزودهٔ <bdi dir="ltr">Week 01</bdi>**

- <bdi dir="ltr">Code Craft Lab: Refactor</bdi> مرحله‌ای <bdi dir="ltr">Primitive Transfer Request</bdi> به <bdi dir="ltr">Money</bdi> و <bdi dir="ltr">Typed ID</bdi> با <bdi dir="ltr">Characterization Test</bdi>، <bdi dir="ltr">Edge Test</bdi> و تصمیم مستدل دربارهٔ <bdi dir="ltr">Static Factory</bdi>
- <bdi dir="ltr">Core Banking Case File: UPI</bdi> هند؛ تفکیک <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">App</bdi>، <bdi dir="ltr">PSP</bdi>، شبکه، بانک و <bdi dir="ltr">API Contract</bdi> همراه با <bdi dir="ltr">Timeline</bdi>، <bdi dir="ltr">Failure</bdi> سال ۲۰۲۵ و <bdi dir="ltr">Current state</bdi> تاریخ‌دار
- محتوای کامل، تمرین و <bdi dir="ltr">Gate</bdi> در [<bdi dir="ltr">Week 01</bdi>](sprints/01-bank-map-boundaries/week-01-capability-to-contract/README.md) قرار دارد.

### هفتهٔ ۲: <bdi dir="ltr">Strategic DDD</bdi> و مالکیت

**فنی**

- <bdi dir="ltr">Domain/Subdomain</bdi>، <bdi dir="ltr">Core/Supporting/Generic</bdi>
- <bdi dir="ltr">Bounded Context</bdi> و <bdi dir="ltr">Ubiquitous Language</bdi>
- <bdi dir="ltr">Context Map: Customer/Supplier</bdi>، <bdi dir="ltr">Conformist</bdi>، <bdi dir="ltr">ACL</bdi> و <bdi dir="ltr">Published Language</bdi>
- <bdi dir="ltr">Source of Truth</bdi> و <bdi dir="ltr">Ownership of Decision</bdi>

**دامینی**

- مرزبندی اولیهٔ شش دامین اصلی
- تعیین «مالک چه چیزی است؟»، «چه چیزی را نباید مالک باشد؟» و «از چه کسی می‌گیرد؟»

**کد و تمرین**

- ساخت شش ماژول منطقی در <bdi dir="ltr">Spring Modulith</bdi>
- اجرای <bdi dir="ltr">Module Verification</bdi> برای <bdi dir="ltr">Cycle</bdi> و دسترسی به <bdi dir="ltr">Package</bdi> داخلی
- ثبت <bdi dir="ltr">Dependency</bdi> مجاز بین ماژول‌ها

**تحویل‌دادنی**

- <bdi dir="ltr">Domain Map</bdi> و <bdi dir="ltr">Context Map</bdi> نسخهٔ ۱
- <bdi dir="ltr">Data/Decision Ownership Matrix</bdi> نسخهٔ ۱
- اسکلت شش پروندهٔ دامینی
- <bdi dir="ltr">Architecture Fitness Test</bdi> اولیه

**<bdi dir="ltr">Gate</bdi> اسپرینت**

یک قابلیت جدید مانند «مسدودی قضایی سپرده» داده می‌شود. باید زنجیرهٔ <bdi dir="ltr">Capability</bdi> تا <bdi dir="ltr">API/Event</bdi>، مالک داده و مرزهای <bdi dir="ltr">Context</bdi> را بدون شروع از نام جدول یا سرویس طراحی کنی.

---

## اسپرینت ۲ — <bdi dir="ltr">Domain Model</bdi> و معماری داخلی کد

### هفتهٔ ۳: <bdi dir="ltr">Tactical DDD</bdi> روی <bdi dir="ltr">Deposits</bdi>

**فنی**

- <bdi dir="ltr">Entity</bdi>، <bdi dir="ltr">Value Object</bdi>، <bdi dir="ltr">Aggregate Root</bdi>، <bdi dir="ltr">Invariant</bdi> و <bdi dir="ltr">Domain Event</bdi>
- <bdi dir="ltr">Repository</bdi>، <bdi dir="ltr">Domain Service</bdi> و <bdi dir="ltr">Application Service</bdi>
- <bdi dir="ltr">SOLID</bdi> روی کد واقعی، نه تعریف حفظی
- <bdi dir="ltr">Strategy</bdi>، <bdi dir="ltr">Factory</bdi>، <bdi dir="ltr">Specification</bdi> و <bdi dir="ltr">State</bdi>؛ تشخیص زمان نامناسب استفاده از <bdi dir="ltr">Pattern</bdi>

**دامینی**

- <bdi dir="ltr">`DepositAccount`</bdi>، <bdi dir="ltr">`Balance`</bdi>، <bdi dir="ltr">`Hold`</bdi> و <bdi dir="ltr">Lifecycle</bdi> حساب
- قواعد برداشت، مسدودی، رفع مسدودی و ماندهٔ قابل برداشت

**کد و تمرین**

- پیاده‌سازی <bdi dir="ltr">`credit`</bdi>، <bdi dir="ltr">`debit`</bdi>، <bdi dir="ltr">`placeHold`</bdi> و <bdi dir="ltr">`releaseHold`</bdi>
- <bdi dir="ltr">Strategy</bdi> محاسبهٔ سود و <bdi dir="ltr">Specification</bdi> احراز شرایط عملیات
- <bdi dir="ltr">Unit Test</bdi> برای کمبود موجودی، <bdi dir="ltr">Hold</bdi> تکراری، مبلغ منفی و <bdi dir="ltr">State</bdi> نامعتبر

**تحویل‌دادنی**

- مدل دامینی <bdi dir="ltr">Deposits</bdi> نسخهٔ ۱
- فهرست <bdi dir="ltr">Aggregate</bdi> و <bdi dir="ltr">Transaction Boundary</bdi>
- <bdi dir="ltr">Code Review Checklist</bdi> برای <bdi dir="ltr">Domain Model</bdi>

**معیار قبولی**

- <bdi dir="ltr">Controller</bdi> یا <bdi dir="ltr">Entity</bdi> دیتابیس منطق کسب‌وکار را نگه ندارد.
- هیچ <bdi dir="ltr">Setter</bdi> عمومی برای دورزدن <bdi dir="ltr">Invariant</bdi> وجود نداشته باشد.

### هفتهٔ ۴: <bdi dir="ltr">Hexagonal Architecture</bdi> روی <bdi dir="ltr">Lending</bdi>

**فنی**

- <bdi dir="ltr">Layered</bdi>، <bdi dir="ltr">Clean</bdi> و <bdi dir="ltr">Hexagonal Architecture</bdi>
- <bdi dir="ltr">Inbound/Outbound Port</bdi> و <bdi dir="ltr">Adapter</bdi>
- <bdi dir="ltr">Dependency Inversion</bdi>، <bdi dir="ltr">Unit of Work</bdi> و تست‌پذیری
- <bdi dir="ltr">Refactoring</bdi> یک کلاس بزرگ به <bdi dir="ltr">Strategy/Factory/Policy</bdi>

**دامینی**

- <bdi dir="ltr">`LoanAgreement`</bdi>، <bdi dir="ltr">`Disbursement`</bdi>، <bdi dir="ltr">`RepaymentSchedule`</bdi> و <bdi dir="ltr">`Installment`</bdi>
- قواعد تصویب، قرارداد، اعطا، گردکردن مبلغ و پرداخت قسط

**کد و تمرین**

- <bdi dir="ltr">Use Case</bdi> اولیهٔ <bdi dir="ltr">`GrantLoan`</bdi>
- <bdi dir="ltr">Persistence Adapter</bdi> روی <bdi dir="ltr">PostgreSQL</bdi>
- <bdi dir="ltr">Integration Test</bdi> با <bdi dir="ltr">Testcontainers</bdi>
- بازطراحی یک نمونهٔ <bdi dir="ltr">Java 8</bdi> از <bdi dir="ltr">Mapping</bdi> تراکنش‌های مالی برای حفظ ارتباط با محیط واقعی

**تحویل‌دادنی**

- اسکلت <bdi dir="ltr">Hexagonal</bdi> قابل اجرا
- <bdi dir="ltr">ADR-001:</bdi> معماری داخلی سرویس
- تست معماری برای ممنوعیت وابستگی <bdi dir="ltr">Domain</bdi> به <bdi dir="ltr">Spring/JPA/Kafka</bdi>

**<bdi dir="ltr">Gate</bdi> اسپرینت**

- تمام <bdi dir="ltr">Invariant</bdi>ها <bdi dir="ltr">Unit Test</bdi> دارند.
- <bdi dir="ltr">Domain</bdi> بدون <bdi dir="ltr">Spring Context</bdi> آزمون می‌شود.
- <bdi dir="ltr">Adapter</bdi> دیتابیس با <bdi dir="ltr">PostgreSQL</bdi> واقعیِ <bdi dir="ltr">Testcontainers</bdi> آزمون شده است.

---

## اسپرینت ۳ — قراردادها، مرز سرویس و امنیت

### هفتهٔ ۵: <bdi dir="ltr">API</bdi> و <bdi dir="ltr">Source of Truth</bdi>

**فنی**

- <bdi dir="ltr">Command/Query</bdi> و تفاوت <bdi dir="ltr">API</bdi> دامینی با <bdi dir="ltr">CRUD</bdi>
- <bdi dir="ltr">REST Semantics</bdi>، <bdi dir="ltr">OpenAPI</bdi>، <bdi dir="ltr">Error Model</bdi> و <bdi dir="ltr">Validation</bdi>
- <bdi dir="ltr">Idempotency Key</bdi>، <bdi dir="ltr">Optimistic Version</bdi> و <bdi dir="ltr">API Versioning</bdi>
- <bdi dir="ltr">Temporal Data</bdi>، <bdi dir="ltr">Effective Dating</bdi> و <bdi dir="ltr">Snapshot</bdi>

**دامینی**

- <bdi dir="ltr">Party</bdi> در برابر <bdi dir="ltr">Customer</bdi>
- <bdi dir="ltr">Product Definition</bdi>، <bdi dir="ltr">Pricing</bdi>، <bdi dir="ltr">Eligibility</bdi> و <bdi dir="ltr">Agreement</bdi>
- مشخص‌کردن داده‌های <bdi dir="ltr">Reference</bdi> و <bdi dir="ltr">Snapshot</bdi>شونده در قرارداد

**کد و تمرین**

- <bdi dir="ltr">API</bdi> ایجاد/مشاهدهٔ <bdi dir="ltr">Loan Agreement</bdi>
- ذخیرهٔ <bdi dir="ltr">Snapshot</bdi> شرایط <bdi dir="ltr">Product</bdi> هنگام انعقاد قرارداد
- تست <bdi dir="ltr">Contract</bdi>، <bdi dir="ltr">Idempotency</bdi> و تغییر هم‌زمان <bdi dir="ltr">Version</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">OpenAPI</bdi> نسخهٔ ۱
- <bdi dir="ltr">Command/Query Catalog</bdi>
- ماتریس <bdi dir="ltr">Source of Truth/Snapshot/Cache</bdi>

**معیار قبولی**

- تغییر <bdi dir="ltr">Product</bdi>، قرارداد قبلی را تغییر ندهد.
- <bdi dir="ltr">Retry</bdi> یک <bdi dir="ltr">Request</bdi> با <bdi dir="ltr">Idempotency Key</bdi> یکسان اثر مالی دوم نسازد.

### هفتهٔ ۶: <bdi dir="ltr">Modular Monolith</bdi> یا <bdi dir="ltr">Microservice</bdi> و <bdi dir="ltr">Security by Design</bdi>

**فنی**

- <bdi dir="ltr">Transactional Cohesion</bdi>، <bdi dir="ltr">Change Coupling</bdi>، <bdi dir="ltr">Independent Deployment</bdi> و <bdi dir="ltr">Team Boundary</bdi>
- <bdi dir="ltr">Shared Database</bdi>، <bdi dir="ltr">Shared Library</bdi> و <bdi dir="ltr">Distributed Monolith</bdi>
- <bdi dir="ltr">AuthN</bdi>، <bdi dir="ltr">AuthZ</bdi>، <bdi dir="ltr">Scope/Role</bdi>، <bdi dir="ltr">Object-level Authorization</bdi> و <bdi dir="ltr">Audit</bdi>
- <bdi dir="ltr">Threat Modeling</bdi> سبک و کنترل‌های <bdi dir="ltr">OWASP API Security</bdi>

**دامینی**

- تصمیم <bdi dir="ltr">Module/Service</bdi> برای <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Payments</bdi> و <bdi dir="ltr">Accounting</bdi>
- تعیین <bdi dir="ltr">API Gateway Policy</bdi> در برابر <bdi dir="ltr">Business Policy</bdi>

**کد و تمرین**

- تست مجوز روی <bdi dir="ltr">Account/Loan</bdi> متعلق به مشتری دیگر
- <bdi dir="ltr">Audit Context</bdi> شامل <bdi dir="ltr">Actor</bdi>، <bdi dir="ltr">Channel</bdi>، <bdi dir="ltr">Branch</bdi> و <bdi dir="ltr">Correlation ID</bdi>
- <bdi dir="ltr">Architecture Test</bdi> برای جلوگیری از <bdi dir="ltr">Shared Entity/Repository</bdi> میان دامین‌ها

**تحویل‌دادنی**

- <bdi dir="ltr">Service Candidate Map</bdi>
- <bdi dir="ltr">ADR-002:</bdi> معماری <bdi dir="ltr">Lending</bdi>
- <bdi dir="ltr">ADR-003:</bdi> معماری <bdi dir="ltr">Accounting</bdi>
- <bdi dir="ltr">ADR-004:</bdi> مرز <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">Payments</bdi>
- <bdi dir="ltr">Threat Model</bdi> و <bdi dir="ltr">Security Checklist</bdi> اولیه

**<bdi dir="ltr">Gate</bdi> اسپرینت**

هیچ <bdi dir="ltr">Microservice</bdi> صرفاً به‌دلیل «مدرن‌بودن»، تعداد <bdi dir="ltr">Entity</bdi> یا وجود یک <bdi dir="ltr">BIAN Service Domain</bdi> ایجاد نشده باشد. هر استخراج باید حداقل دو محرک مستقل و هزینه‌های توزیع را ثبت کند.

---

## اسپرینت ۴ — تراکنش، مانده و <bdi dir="ltr">CQRS</bdi>

### هفتهٔ ۷: <bdi dir="ltr">Isolation</bdi>، <bdi dir="ltr">Locking</bdi> و <bdi dir="ltr">Concurrency</bdi>

**فنی**

- <bdi dir="ltr">ACID</bdi> و <bdi dir="ltr">Isolation Level</bdi>
- <bdi dir="ltr">Lost Update</bdi>، <bdi dir="ltr">Non-repeatable Read</bdi>، <bdi dir="ltr">Phantom</bdi> و <bdi dir="ltr">Write Skew</bdi>
- <bdi dir="ltr">Optimistic/Pessimistic Lock</bdi>، <bdi dir="ltr">Atomic Update</bdi> و <bdi dir="ltr">Lock Ordering</bdi>
- <bdi dir="ltr">Deadlock</bdi>، <bdi dir="ltr">Retry Budget</bdi> و <bdi dir="ltr">Transaction Boundary</bdi>

**دامینی**

- برداشت هم‌زمان از سپرده
- <bdi dir="ltr">Hold</bdi> و برداشت هم‌زمان
- وصول هم‌زمان قسط
- پرداخت از چند <bdi dir="ltr">Channel</bdi>

**کد و تمرین**

- بازتولید <bdi dir="ltr">Lost Update</bdi>
- سه راه‌حل: <bdi dir="ltr">Optimistic Lock</bdi>، <bdi dir="ltr">`SELECT FOR UPDATE`</bdi> و <bdi dir="ltr">Atomic Conditional Update</bdi>
- تست هم‌زمانی با تقاضای بیش از موجودی و اثبات عدم منفی‌شدن مانده
- مقایسهٔ رفتار <bdi dir="ltr">PostgreSQL</bdi> و <bdi dir="ltr">Oracle</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">Concurrency Decision Matrix</bdi>
- <bdi dir="ltr">Lock Ordering Policy</bdi>
- تست خودکار <bdi dir="ltr">Deadlock/Retry</bdi> و <bdi dir="ltr">Oversubscription</bdi>

**معیار قبولی**

- صحت با <bdi dir="ltr">Sleep</bdi> تصادفی یا اجرای تک‌<bdi dir="ltr">Thread</bdi> اثبات نشده باشد.
- <bdi dir="ltr">Retry</bdi> محدود، قابل مشاهده و فقط برای خطاهای <bdi dir="ltr">Retryable</bdi> باشد.

### هفتهٔ ۸: <bdi dir="ltr">Operational Balance</bdi>، <bdi dir="ltr">Ledger</bdi>، <bdi dir="ltr">Subledger</bdi> و <bdi dir="ltr">CQRS</bdi>

**فنی**

- <bdi dir="ltr">Source of Truth</bdi>، <bdi dir="ltr">Derived Data</bdi>، <bdi dir="ltr">Snapshot</bdi> و <bdi dir="ltr">Projection</bdi>
- <bdi dir="ltr">Command Model</bdi>، <bdi dir="ltr">Read Model</bdi>، <bdi dir="ltr">Projection Lag</bdi> و <bdi dir="ltr">Rebuild</bdi>
- <bdi dir="ltr">Operational Ledger</bdi>، <bdi dir="ltr">Accounting Subledger</bdi> و <bdi dir="ltr">General Ledger</bdi>
- <bdi dir="ltr">Reconciliation</bdi> و <bdi dir="ltr">Proof of Balance</bdi>

**دامینی**

- مالک ماندهٔ قابل برداشت، ماندهٔ اصل و اقساط
- تفکیک دفتر معین تسهیلات از وضعیت عملیاتی تسهیلات

**کد و تمرین**

- <bdi dir="ltr">Read Model</bdi> صورت‌حساب سپرده
- <bdi dir="ltr">Projection</bdi> مصرف‌کنندهٔ رویداد و <bdi dir="ltr">Rebuild</bdi> کامل
- <bdi dir="ltr">Job</bdi> مغایرت‌گیری بین <bdi dir="ltr">Operational Transactions</bdi> و <bdi dir="ltr">Read Model</bdi>
- مقایسهٔ <bdi dir="ltr">Event Sourcing</bdi> با <bdi dir="ltr">Event-driven/CQRS</bdi> و ثبت دلیل استفاده‌نکردن از <bdi dir="ltr">Event Sourcing</bdi> به‌عنوان پیش‌فرض

**تحویل‌دادنی**

- مدل دادهٔ ماندهٔ عملیاتی
- مدل اولیهٔ <bdi dir="ltr">Subledger</bdi>
- <bdi dir="ltr">CQRS Consistency Contract</bdi> شامل <bdi dir="ltr">Lag</bdi> مجاز و رفتار در <bdi dir="ltr">Stale Read</bdi>
- <bdi dir="ltr">Reconciliation Specification</bdi>

**<bdi dir="ltr">Gate</bdi> اسپرینت**

برای هر مانده باید مشخص باشد: مالک، روش تغییر، مرز <bdi dir="ltr">ACID</bdi>، امکان <bdi dir="ltr">Rebuild</bdi>، منبع مغایرت‌گیری و رفتار در تأخیر <bdi dir="ltr">Projection</bdi> چیست.

---

## اسپرینت ۵ — <bdi dir="ltr">Event-driven Architecture</bdi> قابل اتکا

### هفتهٔ ۹: <bdi dir="ltr">Command</bdi>، <bdi dir="ltr">Domain Event</bdi> و <bdi dir="ltr">Integration Event</bdi>

**فنی**

- تفاوت <bdi dir="ltr">Command</bdi>، <bdi dir="ltr">Domain Event</bdi>، <bdi dir="ltr">Integration Event</bdi> و <bdi dir="ltr">Query</bdi>
- <bdi dir="ltr">Event Notification</bdi> در برابر <bdi dir="ltr">Event-Carried State Transfer</bdi>
- <bdi dir="ltr">Semantic Event</bdi>، <bdi dir="ltr">Schema Evolution</bdi> و <bdi dir="ltr">Compatibility</bdi>
- <bdi dir="ltr">Correlation ID</bdi>، <bdi dir="ltr">Causation ID</bdi> و <bdi dir="ltr">Business Transaction ID</bdi>

**دامینی**

- طراحی پیام‌های فرایند اعطا و واریز به سپرده
- تعیین اینکه چه کسی <bdi dir="ltr">Command</bdi> می‌دهد و چه دامین صاحب <bdi dir="ltr">Event</bdi> است

**کد و تمرین**

- تعریف <bdi dir="ltr">Event Envelope</bdi> استاندارد با این فیلدها:
  <bdi dir="ltr">`eventId`</bdi>، <bdi dir="ltr">`eventType`</bdi>، <bdi dir="ltr">`eventVersion`</bdi>، <bdi dir="ltr">`occurredAt`</bdi>، <bdi dir="ltr">`producer`</bdi>، <bdi dir="ltr">`aggregateId`</bdi>، <bdi dir="ltr">`aggregateVersion`</bdi>، <bdi dir="ltr">`businessTransactionId`</bdi>، <bdi dir="ltr">`correlationId`</bdi>، <bdi dir="ltr">`causationId`</bdi>، <bdi dir="ltr">`partitionKey`</bdi> و <bdi dir="ltr">`payload`</bdi>
- نگارش <bdi dir="ltr">AsyncAPI</bdi> برای جریان اعطا
- <bdi dir="ltr">Contract Compatibility Test</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">Event Catalog</bdi> نسخهٔ ۱
- <bdi dir="ltr">AsyncAPI</bdi> نسخهٔ ۱
- <bdi dir="ltr">Sequence Diagram</bdi> اعطای تسهیلات

**معیار قبولی**

- نام <bdi dir="ltr">Event</bdi> رخداد گذشته باشد، نه دستور مبهم.
- <bdi dir="ltr">Consumer</bdi> برای فهم <bdi dir="ltr">Payload</bdi> مجبور به <bdi dir="ltr">Query</bdi> همگام غیرضروری نشود.

### هفتهٔ ۱۰: <bdi dir="ltr">Kafka</bdi>، <bdi dir="ltr">Outbox</bdi>، <bdi dir="ltr">Inbox</bdi> و <bdi dir="ltr">Idempotency</bdi>

**فنی**

- <bdi dir="ltr">Topic</bdi>، <bdi dir="ltr">Partition</bdi>، <bdi dir="ltr">Offset</bdi> و <bdi dir="ltr">Consumer Group</bdi>
- <bdi dir="ltr">Ordering</bdi> در محدودهٔ <bdi dir="ltr">Partition</bdi> و انتخاب <bdi dir="ltr">Partition Key</bdi>
- <bdi dir="ltr">At-least-once Delivery</bdi> و محدودهٔ واقعی <bdi dir="ltr">Kafka Exactly-once</bdi>
- <bdi dir="ltr">Transactional Outbox</bdi>، <bdi dir="ltr">Inbox</bdi>، <bdi dir="ltr">Deduplication</bdi> و <bdi dir="ltr">Replay</bdi>

**کد و تمرین**

- ذخیرهٔ <bdi dir="ltr">Aggregate</bdi> و <bdi dir="ltr">Outbox</bdi> در یک تراکنش
- انتشار به <bdi dir="ltr">Kafka</bdi> و مصرف در سرویس دوم
- <bdi dir="ltr">Unique Constraint</bdi> روی <bdi dir="ltr">`event_id`</bdi> و <bdi dir="ltr">Business Idempotency Key</bdi>
- تست <bdi dir="ltr">Crash</bdi> بعد از <bdi dir="ltr">Commit</bdi>، پیام تکراری و <bdi dir="ltr">Replay</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">Outbox/Inbox Schema</bdi>
- <bdi dir="ltr">Topic/Partition/Retention Catalog</bdi>
- <bdi dir="ltr">Idempotency Policy</bdi> برای عملیات مالی
- <bdi dir="ltr">ADR-005:</bdi> روش انتشار <bdi dir="ltr">Event</bdi>

**<bdi dir="ltr">Gate</bdi> اسپرینت**

- مصرف دوباره اثر مالی دوم نسازد.
- <bdi dir="ltr">Replay</bdi>، <bdi dir="ltr">Projection</bdi> را بازسازی کند.
- <bdi dir="ltr">Ordering</bdi> مورد نیاز با <bdi dir="ltr">Aggregate/Business Key</bdi> مستند و آزموده شود.

---

## اسپرینت ۶ — <bdi dir="ltr">Saga</bdi>، شکست و مشاهده‌پذیری

### هفتهٔ ۱۱: <bdi dir="ltr">Process Manager</bdi> و <bdi dir="ltr">State Machine</bdi>

**فنی**

- <bdi dir="ltr">Saga</bdi>، <bdi dir="ltr">Orchestration</bdi>، <bdi dir="ltr">Choreography</bdi> و <bdi dir="ltr">Process Manager</bdi>
- <bdi dir="ltr">Long-running State Machine</bdi>، <bdi dir="ltr">Timeout</bdi> و <bdi dir="ltr">Retry Policy</bdi>
- <bdi dir="ltr">Business Correlation</bdi> و وضعیت‌های میانی

**دامینی**

- فرایند اعطای تسهیلات:
  1. ثبت درخواست اعطا در <bdi dir="ltr">Lending</bdi>
  2. درخواست <bdi dir="ltr">Credit</bdi> به <bdi dir="ltr">Deposits</bdi>
  3. دریافت نتیجهٔ واریز
  4. قطعی‌کردن وضعیت <bdi dir="ltr">Disbursement</bdi>
  5. پردازش حسابداری و <bdi dir="ltr">Reconciliation</bdi>

**کد و تمرین**

- پیاده‌سازی <bdi dir="ltr">Process Instance</bdi> پایدار و <bdi dir="ltr">Versioned</bdi>
- <bdi dir="ltr">Handler</bdi>های <bdi dir="ltr">Idempotent</bdi> و <bdi dir="ltr">Timer/Timeout</bdi>
- جداکردن وضعیت تکمیل عملیات کسب‌وکار از وضعیت <bdi dir="ltr">Pending</bdi> حسابداری

**تحویل‌دادنی**

- <bdi dir="ltr">State Machine</bdi> و <bdi dir="ltr">State Transition Table</bdi>
- <bdi dir="ltr">ADR-006: Orchestration</bdi> یا <bdi dir="ltr">Choreography</bdi>
- <bdi dir="ltr">Process Data Model</bdi>

**معیار قبولی**

- <bdi dir="ltr">Orchestrator</bdi> مستقیماً جدول یا منطق داخلی دامین‌ها را تغییر ندهد.
- <bdi dir="ltr">Restart</bdi> سرویس وضعیت فرایند را از بین نبرد.

### هفتهٔ ۱۲: <bdi dir="ltr">Failure</bdi>، <bdi dir="ltr">Compensation</bdi>، <bdi dir="ltr">Reconciliation</bdi> و <bdi dir="ltr">Observability</bdi>

**فنی**

- <bdi dir="ltr">Business Failure</bdi> در برابر <bdi dir="ltr">Technical Failure</bdi>
- <bdi dir="ltr">Retryable/Non-retryable</bdi>، <bdi dir="ltr">Backoff/Jitter</bdi>، <bdi dir="ltr">DLQ</bdi> و <bdi dir="ltr">Poison Message</bdi>
- <bdi dir="ltr">Timeout Budget</bdi>، <bdi dir="ltr">Circuit Breaker</bdi> و <bdi dir="ltr">Bulkhead</bdi> برای وابستگی‌های همگام
- <bdi dir="ltr">Rollback</bdi>، <bdi dir="ltr">Compensation</bdi>، <bdi dir="ltr">Reversal</bdi> و <bdi dir="ltr">Correction</bdi>
- <bdi dir="ltr">Trace</bdi>، <bdi dir="ltr">Metric</bdi>، <bdi dir="ltr">Log</bdi> و <bdi dir="ltr">Context Propagation</bdi>

**آزمایش‌های اجباری**

1. <bdi dir="ltr">Deposits</bdi> در دسترس نیست.
2. واریز انجام شده ولی پاسخ گم می‌شود.
3. <bdi dir="ltr">Event</bdi> دوبار تحویل می‌شود.
4. <bdi dir="ltr">Accounting</bdi> موقتاً قطع است.
5. <bdi dir="ltr">Event</bdi>ها خارج از ترتیب می‌رسند.
6. سرویس بعد از <bdi dir="ltr">DB Commit</bdi> و قبل از <bdi dir="ltr">Publish</bdi> متوقف می‌شود.

**کد و تمرین**

- تزریق شش خطا و ثبت نتیجهٔ مورد انتظار
- <bdi dir="ltr">Trace</bdi> سراسری با <bdi dir="ltr">Correlation/Causation</bdi>
- <bdi dir="ltr">Metric</bdi> برای <bdi dir="ltr">Pending Process</bdi>، <bdi dir="ltr">Retry</bdi>، <bdi dir="ltr">Duplicate</bdi> و <bdi dir="ltr">Reconciliation Mismatch</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">Failure Matrix</bdi> و <bdi dir="ltr">Compensation Matrix</bdi>
- <bdi dir="ltr">Runbook</bdi> تعمیر دستی و <bdi dir="ltr">Reconciliation</bdi>
- داشبورد اولیهٔ جریان اعطا

**<bdi dir="ltr">Gate</bdi> اسپرینت**

هر شکست باید دقیقاً یکی از این پایان‌ها را داشته باشد: <bdi dir="ltr">Retry</bdi> کنترل‌شده، <bdi dir="ltr">Compensation/Reversal</bdi>، توقف کسب‌وکاری، یا <bdi dir="ltr">Manual Repair</bdi> قابل ممیزی. وضعیت «نامعلوم و بدون مالک» مردود است.

---

## اسپرینت ۷ — معماری حسابداری بانکی

### هفتهٔ ۱۳: <bdi dir="ltr">Accounting Fact</bdi> و <bdi dir="ltr">Translator</bdi>

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


- تفاوت رخداد کسب‌وکار با <bdi dir="ltr">Fact</bdi> حسابداری
- <bdi dir="ltr">Published Language</bdi> میان دامین و <bdi dir="ltr">Accounting</bdi>
- <bdi dir="ltr">Rule Version</bdi>، <bdi dir="ltr">Effective Date</bdi> و <bdi dir="ltr">Rule Selection</bdi>
- جلوگیری از ورود منطق «اعطای مرابحه» یا «شکست سپرده» به هستهٔ عمومی <bdi dir="ltr">Journal</bdi>

**کد و تمرین**

- <bdi dir="ltr">Fact Schema</bdi> و <bdi dir="ltr">Translator</bdi> برای پنج <bdi dir="ltr">Event</bdi>
- <bdi dir="ltr">Rule Engine</bdi> ساده و قابل نسخه‌بندی
- تست اینکه <bdi dir="ltr">Replay</bdi> با همان نسخهٔ <bdi dir="ltr">Rule</bdi> همان نتیجه را می‌دهد

**تحویل‌دادنی**

- <bdi dir="ltr">Accounting Fact Catalog</bdi>
- <bdi dir="ltr">Event-to-Fact Mapping</bdi>
- <bdi dir="ltr">ADR-007:</bdi> مرز <bdi dir="ltr">Translator</bdi> و <bdi dir="ltr">Accounting Engine</bdi>

**معیار قبولی**

- <bdi dir="ltr">Accounting Fact</bdi> اطلاعات لازم برای ثبت و <bdi dir="ltr">Audit</bdi> را دارد.
- <bdi dir="ltr">Event</bdi> اصلی، <bdi dir="ltr">Fact</bdi> و نسخهٔ <bdi dir="ltr">Rule</bdi> قابل رهگیری متقابل‌اند.

### هفتهٔ ۱۴: <bdi dir="ltr">Journal</bdi>، <bdi dir="ltr">Subledger</bdi>، <bdi dir="ltr">GL</bdi> و قواعد مالی

**فنی و دامینی**

- <bdi dir="ltr">Double-entry</bdi>، <bdi dir="ltr">Chart of Accounts</bdi>، <bdi dir="ltr">Journal</bdi> و <bdi dir="ltr">Journal Line</bdi>
- <bdi dir="ltr">GL</bdi>، <bdi dir="ltr">SL</bdi> و <bdi dir="ltr">Auxiliary Dimensions</bdi>
- <bdi dir="ltr">Cost Center</bdi>، <bdi dir="ltr">Branch</bdi>، <bdi dir="ltr">Currency</bdi>، <bdi dir="ltr">Fiscal Year</bdi> و <bdi dir="ltr">Financial Period</bdi>
- <bdi dir="ltr">Accrual</bdi>، <bdi dir="ltr">Reversal</bdi>، <bdi dir="ltr">Correction</bdi> و <bdi dir="ltr">Back-dated Posting</bdi>
- حفظ جزئیات <bdi dir="ltr">Event/Subledger</bdi> و تجمیع فقط در <bdi dir="ltr">Projection</bdi> یا <bdi dir="ltr">GL</bdi> مناسب

**ده رویداد مرجع**

1. <bdi dir="ltr">`LoanDisbursed`</bdi>
2. <bdi dir="ltr">`LoanPrincipalRepaid`</bdi>
3. <bdi dir="ltr">`LoanInterestAccrued`</bdi>
4. <bdi dir="ltr">`LatePenaltyAssessed`</bdi>
5. <bdi dir="ltr">`DepositCredited`</bdi>
6. <bdi dir="ltr">`DepositDebited`</bdi>
7. <bdi dir="ltr">`DepositInterestAccrued`</bdi>
8. <bdi dir="ltr">`DepositInterestPaid`</bdi>
9. <bdi dir="ltr">`PaymentSettled`</bdi>
10. <bdi dir="ltr">`TermDepositBroken`</bdi>

**کد و تمرین**

- ثبت <bdi dir="ltr">Idempotent Journal</bdi>
- کنترل <bdi dir="ltr">`Sum(Debit) = Sum(Credit)`</bdi>
- رد <bdi dir="ltr">Period</bdi> بسته و ثبت <bdi dir="ltr">Reversal</bdi> با <bdi dir="ltr">Link</bdi> به سند مبنا
- تولید <bdi dir="ltr">Subledger Entry</bdi> بدون حذف جزئیات رخداد

**تحویل‌دادنی**

- قواعد ثبت ده <bdi dir="ltr">Event</bdi>
- نمونه‌سندهای سپرده، تسهیلات و انتقال وجه
- مدل <bdi dir="ltr">Rule Versioning</bdi> و <bdi dir="ltr">Period Control</bdi>

**معیار قبولی**

- هیچ <bdi dir="ltr">Journal</bdi> نامتوازن ثبت نشود.
- سند اصلاحی سابقهٔ سند اصلی را حذف یا بازنویسی نکند.

---

## اسپرینت ۸ — طراحی فیزیکی و کارایی مالی

### هفتهٔ ۱۵: <bdi dir="ltr">Oracle/PostgreSQL Physical Design</bdi>

**فنی**

- طراحی براساس <bdi dir="ltr">Query Pattern</bdi> و حجم/<bdi dir="ltr">Retention</bdi>
- <bdi dir="ltr">Primary/Business Key</bdi>، <bdi dir="ltr">Foreign Key</bdi> و <bdi dir="ltr">Unique Constraint</bdi>
- <bdi dir="ltr">Composite/Partial/Local/Global Index</bdi>
- <bdi dir="ltr">Range/List/Hash/Composite Partitioning</bdi>
- <bdi dir="ltr">Oracle Reference Partitioning</bdi> و <bdi dir="ltr">Partition Pruning</bdi>
- <bdi dir="ltr">Archive</bdi>، <bdi dir="ltr">Purge</bdi>، <bdi dir="ltr">Compression</bdi> و <bdi dir="ltr">Tablespace Policy</bdi>

**جداول مرجع**

- <bdi dir="ltr">`accounting_event`</bdi>
- <bdi dir="ltr">`journal`</bdi>
- <bdi dir="ltr">`journal_line`</bdi>
- <bdi dir="ltr">`subledger_entry`</bdi>
- <bdi dir="ltr">`balance_snapshot`</bdi>
- <bdi dir="ltr">`outbox_event`</bdi>
- <bdi dir="ltr">`inbox_message`</bdi>
- <bdi dir="ltr">`process_instance`</bdi>

**کد و تمرین**

- <bdi dir="ltr">DDL</bdi> اجرایی برای <bdi dir="ltr">PostgreSQL</bdi> و <bdi dir="ltr">Oracle</bdi>
- <bdi dir="ltr">Reference Partitioning</bdi> فرزند <bdi dir="ltr">Journal</bdi> در <bdi dir="ltr">Oracle</bdi>
- <bdi dir="ltr">Explain Plan</bdi> برای پنج <bdi dir="ltr">Query</bdi> حیاتی

**تحویل‌دادنی**

- <bdi dir="ltr">Logical</bdi> و <bdi dir="ltr">Physical Data Model</bdi>
- <bdi dir="ltr">Partition/Index/Retention Matrix</bdi>
- <bdi dir="ltr">Critical Query Catalog</bdi>
- <bdi dir="ltr">ADR-008:</bdi> سیاست <bdi dir="ltr">Partitioning</bdi>

**معیار قبولی**

- هیچ جدولی فقط به‌دلیل «بزرگ‌بودن احتمالی» <bdi dir="ltr">Partition</bdi> نشده باشد.
- کلید <bdi dir="ltr">Partition</bdi> با <bdi dir="ltr">Query</bdi>، <bdi dir="ltr">Retention</bdi> و عملیات نگهداری توجیه شود.

### هفتهٔ ۱۶: <bdi dir="ltr">Hot Row</bdi>، <bdi dir="ltr">Batch</bdi>، <bdi dir="ltr">EOD</bdi> و <bdi dir="ltr">Performance</bdi>

**فنی و دامینی**

- <bdi dir="ltr">Hot Account/Hot GL Row</bdi>
- <bdi dir="ltr">Atomic Increment</bdi>، <bdi dir="ltr">Optimistic Retry</bdi> و <bdi dir="ltr">Event Serialization</bdi>
- <bdi dir="ltr">Balance Snapshot</bdi> و <bdi dir="ltr">Rebuild</bdi>
- <bdi dir="ltr">Batch Chunking</bdi>، <bdi dir="ltr">Checkpoint</bdi> و <bdi dir="ltr">Restartability</bdi>
- <bdi dir="ltr">Interest Accrual/EOD</bdi> و <bdi dir="ltr">Business Calendar</bdi>
- <bdi dir="ltr">Performance</bdi> و <bdi dir="ltr">Capacity Test</bdi>

**کد و تمرین**

- <bdi dir="ltr">Load Test</bdi> روی <bdi dir="ltr">Debit/Credit</bdi> و <bdi dir="ltr">Journal Posting</bdi>
- ثبت <bdi dir="ltr">Baseline</bdi> و یک دور <bdi dir="ltr">Tuning</bdi> قابل اندازه‌گیری
- <bdi dir="ltr">Restart</bdi> آزمون <bdi dir="ltr">EOD</bdi> از <bdi dir="ltr">Checkpoint</bdi> بدون ثبت تکراری
- <bdi dir="ltr">Reconciliation</bdi> بعد از <bdi dir="ltr">Load</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">Performance Test Plan</bdi> و <bdi dir="ltr">Report</bdi>
- <bdi dir="ltr">Hot-row Mitigation Decision</bdi>
- <bdi dir="ltr">EOD Runbook</bdi>
- <bdi dir="ltr">Snapshot/Rebuild Policy</bdi>

**<bdi dir="ltr">Gate</bdi> اسپرینت**

- صحت مالی در <bdi dir="ltr">Load</bdi> صددرصد حفظ شود و <bdi dir="ltr">Duplicate</bdi> مالی صفر باشد.
- <bdi dir="ltr">p50/p95/p99</bdi>، <bdi dir="ltr">Throughput</bdi>، <bdi dir="ltr">Error Rate</bdi> و <bdi dir="ltr">Lock Wait</bdi> ثبت شوند.
- بهبود پس از <bdi dir="ltr">Tuning</bdi> با عدد و <bdi dir="ltr">Query Plan</bdi> اثبات شود، نه با احساس.

---

## اسپرینت ۹ — عمق دامین: <bdi dir="ltr">Customer</bdi>، <bdi dir="ltr">Product</bdi>، <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">Teller</bdi>

### هفتهٔ ۱۷: <bdi dir="ltr">Party/Customer</bdi>، <bdi dir="ltr">Product</bdi> و <bdi dir="ltr">Agreement</bdi>

**فنی و دامینی**

- <bdi dir="ltr">Party</bdi>، <bdi dir="ltr">Customer</bdi>، <bdi dir="ltr">KYC</bdi> و <bdi dir="ltr">Customer Relationship</bdi>
- <bdi dir="ltr">Product Definition</bdi>، <bdi dir="ltr">Pricing</bdi>، <bdi dir="ltr">Eligibility</bdi> و <bdi dir="ltr">Bundle</bdi>
- <bdi dir="ltr">Temporal Data</bdi> و <bdi dir="ltr">Effective-dated Rate</bdi>
- <bdi dir="ltr">Agreement</bdi>، <bdi dir="ltr">Contract Terms</bdi> و <bdi dir="ltr">Immutable Snapshot</bdi>
- <bdi dir="ltr">ACL</bdi> و <bdi dir="ltr">Reference Data Cache</bdi>

**کد و تمرین**

- انتخاب نرخ مؤثر بر تاریخ قرارداد
- <bdi dir="ltr">Snapshot</bdi> غیرقابل‌تغییر <bdi dir="ltr">Product Terms</bdi>
- <bdi dir="ltr">Event</bdi>های <bdi dir="ltr">`CustomerStatusChanged`</bdi> و <bdi dir="ltr">`ProductVersionActivated`</bdi>

**تحویل‌دادنی**

- سه پروندهٔ دامینی کامل
- <bdi dir="ltr">API/Event Catalog</bdi> و <bdi dir="ltr">Context Map</bdi> مرتبط
- <bdi dir="ltr">Temporal Data Model</bdi>

**معیار قبولی**

- سابقهٔ قرارداد با تغییر اطلاعات <bdi dir="ltr">Master</bdi> از بین نرود.
- <bdi dir="ltr">Cache</bdi> هیچ‌گاه به‌جای <bdi dir="ltr">Source of Truth</bdi> معرفی نشود.

### هفتهٔ ۱۸: <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Teller</bdi> و <bdi dir="ltr">Cash</bdi>

**فنی و دامینی**

- چرخهٔ افتتاح، فعال‌سازی، واریز، برداشت، <bdi dir="ltr">Hold</bdi>، <bdi dir="ltr">Dormancy</bdi> و بستن
- سود، تمدید، شکست سپرده و <bdi dir="ltr">Business Calendar</bdi>
- <bdi dir="ltr">Cut-off</bdi>، <bdi dir="ltr">Back Value Date</bdi> و <bdi dir="ltr">Monetary Precision</bdi>
- <bdi dir="ltr">Teller Session</bdi>، <bdi dir="ltr">Cashbox</bdi>، <bdi dir="ltr">Branch Vault</bdi>، <bdi dir="ltr">Shortage/Overage</bdi> و <bdi dir="ltr">Cash Transfer</bdi>

**کد و تمرین**

- برش کامل <bdi dir="ltr">`BreakTermDeposit`</bdi>
- محاسبهٔ سود مستحق، تفاوت سود پرداختی و مبلغ اصلاح
- <bdi dir="ltr">Event</bdi> و <bdi dir="ltr">Accounting Fact</bdi>های لازم
- تست <bdi dir="ltr">Duplicate</bdi>، <bdi dir="ltr">Back-dated</bdi> و شکست پس از محاسبه/قبل از ثبت

**تحویل‌دادنی**

- پروندهٔ کامل <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">Teller/Cash</bdi>
- <bdi dir="ltr">Deposit Lifecycle State Machine</bdi>
- <bdi dir="ltr">Deposit Event Catalog</bdi>
- سناریوی نهایی شمارهٔ ۳ در وضعیت <bdi dir="ltr">Beta</bdi>

**معیار قبولی**

- <bdi dir="ltr">Deposits</bdi> مالک محاسبه و وضعیت عملیاتی است؛ <bdi dir="ltr">Accounting</bdi> فقط اثر مالی را ثبت می‌کند.
- <bdi dir="ltr">Reversal/Correction</bdi> با <bdi dir="ltr">Rollback</bdi> ساده اشتباه نشود.

---

## اسپرینت ۱۰ — عمق دامین: <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Collections</bdi> و <bdi dir="ltr">Payments</bdi>

### هفتهٔ ۱۹: <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Collateral</bdi> و <bdi dir="ltr">Collections</bdi>

**فنی و دامینی**

- <bdi dir="ltr">Application</bdi>، <bdi dir="ltr">Credit Decision</bdi>، <bdi dir="ltr">Approval</bdi>، <bdi dir="ltr">Agreement</bdi> و <bdi dir="ltr">Disbursement</bdi>
- <bdi dir="ltr">Schedule Generation</bdi>، <bdi dir="ltr">Accrual</bdi>، <bdi dir="ltr">Payment Allocation</bdi> و <bdi dir="ltr">Settlement</bdi>
- <bdi dir="ltr">Collateral Valuation/Allocation/Release</bdi>
- <bdi dir="ltr">Delinquency Detection</bdi>، <bdi dir="ltr">Collection Case</bdi>، <bdi dir="ltr">Restructuring</bdi>، <bdi dir="ltr">Write-off</bdi> و <bdi dir="ltr">Recovery</bdi>
- <bdi dir="ltr">Decision Table</bdi> و <bdi dir="ltr">Long-running Workflow</bdi>

**کد و تمرین**

- <bdi dir="ltr">Schedule Generator</bdi> با قواعد گردکردن
- <bdi dir="ltr">Projection</bdi> تشخیص <bdi dir="ltr">Delinquency</bdi>
- تکمیل برش اعطا و ارتباط آن با <bdi dir="ltr">Collateral/Collections</bdi> بدون تصاحب مالکیت

**تحویل‌دادنی**

- پرونده‌های <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Collateral</bdi> و <bdi dir="ltr">Collections</bdi>
- <bdi dir="ltr">Decision/Data Ownership Matrix</bdi>
- سناریوی نهایی شمارهٔ ۱ در وضعیت <bdi dir="ltr">Beta</bdi>

**معیار قبولی**

- <bdi dir="ltr">Lending</bdi> مالک بدهی است؛ <bdi dir="ltr">Collections</bdi> مالک پرونده و اقدام وصول؛ <bdi dir="ltr">Collateral</bdi> مالک وضعیت وثیقه؛ <bdi dir="ltr">Accounting</bdi> مالک دفتر مالی.

### هفتهٔ ۲۰: <bdi dir="ltr">Payments</bdi>، <bdi dir="ltr">Cards</bdi>، <bdi dir="ltr">Channels</bdi> و <bdi dir="ltr">Checks</bdi>

**فنی و دامینی**

- <bdi dir="ltr">Payment Order</bdi> و <bdi dir="ltr">Payment State Machine</bdi>
- <bdi dir="ltr">Authorization</bdi>، <bdi dir="ltr">Clearing</bdi> و <bdi dir="ltr">Settlement</bdi>
- <bdi dir="ltr">Reversal</bdi>، <bdi dir="ltr">Refund</bdi> و <bdi dir="ltr">Return</bdi>
- <bdi dir="ltr">Internal Transfer</bdi>، پایا/ساتنا، <bdi dir="ltr">Card Transaction</bdi> و <bdi dir="ltr">Cheque Lifecycle</bdi>
- <bdi dir="ltr">Duplicate Payment Prevention</bdi> و <bdi dir="ltr">External Network Adapter</bdi>
- جایگاه <bdi dir="ltr">ISO 20022</bdi> در مرز تبادل و <bdi dir="ltr">Anti-Corruption Layer</bdi>، بدون تحمیل مستقیم مدل پیام بیرونی به <bdi dir="ltr">Domain Model</bdi> داخلی

**کد و تمرین**

- <bdi dir="ltr">`PaymentOrder`</bdi> برای انتقال بین‌شعبه‌ای
- <bdi dir="ltr">Debit/Credit Idempotent</bdi> در <bdi dir="ltr">Deposits</bdi>
- <bdi dir="ltr">Branch/Inter-branch Accounting Facts</bdi>
- تست گم‌شدن پاسخ، <bdi dir="ltr">Reversal</bdi> و <bdi dir="ltr">Settlement</bdi> دیرهنگام

**تحویل‌دادنی**

- پروندهٔ کامل <bdi dir="ltr">Payments</bdi> و <bdi dir="ltr">Capability Card</bdi>های <bdi dir="ltr">Cards/Channels/Checks</bdi>
- مرزبندی <bdi dir="ltr">Payments</bdi> و <bdi dir="ltr">Deposits</bdi>
- سناریوی نهایی شمارهٔ ۲ در وضعیت <bdi dir="ltr">Beta</bdi>

**<bdi dir="ltr">Gate</bdi> اسپرینت**

یک پروندهٔ تسهیلات معوق و یک انتقال بین‌شعبه‌ای دفاع می‌شوند. هر <bdi dir="ltr">State</bdi>، داده و تصمیم باید دقیقاً یک مالک داشته باشد و <bdi dir="ltr">Channel</bdi> نباید مالک مانده یا فرایند پرداخت شود.

---

## اسپرینت ۱۱ — <bdi dir="ltr">Micro-frontend</bdi> و <bdi dir="ltr">Production Architecture</bdi>

### هفتهٔ ۲۱: <bdi dir="ltr">Micro-frontend Platform</bdi> برای <bdi dir="ltr">Widget</bdi>های مستقل

**فنی**

- <bdi dir="ltr">App Shell</bdi>، <bdi dir="ltr">Runtime Discovery</bdi> و <bdi dir="ltr">Widget Manifest</bdi>
- <bdi dir="ltr">Web Component Contract</bdi> و <bdi dir="ltr">Framework Isolation</bdi>
- <bdi dir="ltr">Independent Build/Version/Deployment</bdi>
- <bdi dir="ltr">Shared Design Tokens</bdi> در برابر <bdi dir="ltr">Shared Runtime State</bdi>
- <bdi dir="ltr">BFF</bdi>، <bdi dir="ltr">API Gateway</bdi>، <bdi dir="ltr">Auth Propagation</bdi> و <bdi dir="ltr">Feature Flag</bdi>
- <bdi dir="ltr">Failure Isolation</bdi> و <bdi dir="ltr">Compatibility Policy</bdi>

**کد و تمرین**

- <bdi dir="ltr">Portal Shell</bdi> با <bdi dir="ltr">Runtime Manifest</bdi>
- <bdi dir="ltr">`deposit-widget`</bdi> و <bdi dir="ltr">`lending-widget`</bdi> با <bdi dir="ltr">Build</bdi> و <bdi dir="ltr">Version</bdi> مستقل
- بارگذاری تنبل، انتقال <bdi dir="ltr">Context</bdi> مجاز و جلوگیری از دسترسی مستقیم به <bdi dir="ltr">State</bdi> داخلی <bdi dir="ltr">Widget</bdi> دیگر
- ازکارانداختن عمدی یک <bdi dir="ltr">Widget</bdi> و اثبات سلامت <bdi dir="ltr">Shell</bdi> و <bdi dir="ltr">Widget</bdi> دیگر

**تحویل‌دادنی**

- <bdi dir="ltr">Micro-frontend Architecture</bdi>
- <bdi dir="ltr">Widget Manifest Schema</bdi>
- <bdi dir="ltr">UI Ownership/Compatibility Matrix</bdi>
- <bdi dir="ltr">ADR-009: Web Components/Module Federation/</bdi>سایر گزینه‌ها

**معیار قبولی**

- افزودن <bdi dir="ltr">Widget</bdi> جدید نیازمند <bdi dir="ltr">Build</bdi> مجدد همهٔ <bdi dir="ltr">Widget</bdi>ها نباشد.
- <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Design System</bdi> مشترک باشد، ولی <bdi dir="ltr">Business State</bdi> مشترک و پنهان ایجاد نشود.

### هفتهٔ ۲۲: <bdi dir="ltr">Runtime</bdi>، <bdi dir="ltr">SLO</bdi>، <bdi dir="ltr">DR</bdi> و <bdi dir="ltr">Service Ownership</bdi>

**فنی**

- <bdi dir="ltr">Container Image</bdi>، <bdi dir="ltr">Kubernetes Deployment/Service/Config/Secret</bdi>
- <bdi dir="ltr">Readiness/Liveness/Startup Probe</bdi>، <bdi dir="ltr">Resource Request/Limit</bdi> و <bdi dir="ltr">HPA</bdi>
- <bdi dir="ltr">CI/CD</bdi>، <bdi dir="ltr">Migration</bdi> سازگار دیتابیس، <bdi dir="ltr">Rolling/Blue-Green/Canary</bdi> و <bdi dir="ltr">Rollback Policy</bdi>
- <bdi dir="ltr">OpenTelemetry</bdi>، <bdi dir="ltr">Dashboard</bdi> و <bdi dir="ltr">Alert</bdi>
- <bdi dir="ltr">SLI/SLO/Error Budget</bdi>
- <bdi dir="ltr">Database HA</bdi>، <bdi dir="ltr">Backup/Restore</bdi>، <bdi dir="ltr">RTO/RPO</bdi>، <bdi dir="ltr">DR</bdi> و <bdi dir="ltr">Production Readiness Review</bdi>
- <bdi dir="ltr">Secret Management</bdi>، <bdi dir="ltr">Network Policy</bdi> و <bdi dir="ltr">Least Privilege</bdi>

**سازمانی**

- <bdi dir="ltr">Service Owner</bdi>، <bdi dir="ltr">Technical Owner</bdi>، <bdi dir="ltr">Product Owner</bdi> و <bdi dir="ltr">Run Owner</bdi>
- تعهد مشترک <bdi dir="ltr">PO</bdi> و <bdi dir="ltr">Engineering Lead</bdi>؛ جلوگیری از جدایی اختیار تولید از تعهد محصول
- <bdi dir="ltr">Build-and-Run Ownership</bdi> و نقش <bdi dir="ltr">Platform/SRE</bdi>

**کد و تمرین**

- <bdi dir="ltr">Manifest</bdi>های <bdi dir="ltr">Kubernetes</bdi> برای سرویس‌های اصلی
- <bdi dir="ltr">Pipeline</bdi> با <bdi dir="ltr">Gate</bdi>های <bdi dir="ltr">Build</bdi>، <bdi dir="ltr">Test</bdi>، <bdi dir="ltr">Contract Compatibility</bdi>، <bdi dir="ltr">Security Scan</bdi> و <bdi dir="ltr">Migration Check</bdi>
- سه <bdi dir="ltr">SLO</bdi> اولیه: اعطا، انتقال وجه و ثبت حسابداری
- توقف یک <bdi dir="ltr">Pod/Consumer</bdi> و مشاهدهٔ <bdi dir="ltr">Recovery</bdi> و <bdi dir="ltr">Backlog</bdi>
- <bdi dir="ltr">Restore</bdi> آزمایشی دیتابیس/<bdi dir="ltr">Projection</bdi> در محیط <bdi dir="ltr">Lab</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">Runtime Architecture</bdi>
- <bdi dir="ltr">NFR Catalog</bdi> و <bdi dir="ltr">SLO Document</bdi>
- <bdi dir="ltr">Backup/DR Plan</bdi> و <bdi dir="ltr">Runbook</bdi>
- <bdi dir="ltr">Service Ownership Map</bdi> و <bdi dir="ltr">Team Topology</bdi>
- <bdi dir="ltr">Production Readiness Checklist</bdi>

**<bdi dir="ltr">Gate</bdi> اسپرینت**

- <bdi dir="ltr">Secret</bdi> در مخزن نباشد.
- <bdi dir="ltr">Alert</bdi> به <bdi dir="ltr">SLI</bdi> و اثر کاربر متصل باشد، نه فقط <bdi dir="ltr">CPU.</bdi>
- <bdi dir="ltr">RTO/RPO</bdi> فرضیهٔ کسب‌وکاریِ قابل تصویب معرفی شود، نه عدد تزئینی معماری.

---

## اسپرینت ۱۲ — یکپارچه‌سازی، مهاجرت و دفاع

### هفتهٔ ۲۳: اثبات سه سناریو و <bdi dir="ltr">Migration Roadmap</bdi>

**کار اصلی**

- اجرای <bdi dir="ltr">End-to-End</bdi> هر سه سناریو
- تکمیل <bdi dir="ltr">Trace</bdi>، <bdi dir="ltr">Event Timeline</bdi>، <bdi dir="ltr">Journal</bdi>، <bdi dir="ltr">Reconciliation</bdi> و <bdi dir="ltr">Failure Evidence</bdi>
- <bdi dir="ltr">Contract Test</bdi> میان سرویس‌ها
- <bdi dir="ltr">Load/Failure Test</bdi> نهایی
- طراحی مهاجرت تدریجی از وضع موجود با <bdi dir="ltr">Strangler</bdi>، <bdi dir="ltr">Parallel Run</bdi>، <bdi dir="ltr">Data Migration</bdi> و <bdi dir="ltr">Cutover</bdi>

**برای هر سناریو باید ثبت شود**

1. مالک هر تصمیم
2. مالک هر داده
3. <bdi dir="ltr">Command</bdi>، <bdi dir="ltr">API</bdi> و <bdi dir="ltr">Event</bdi>ها
4. <bdi dir="ltr">Aggregate</bdi> و <bdi dir="ltr">Transaction Boundary</bdi>
5. <bdi dir="ltr">Ordering</bdi> و <bdi dir="ltr">Consistency</bdi>
6. <bdi dir="ltr">Duplicate</bdi> و <bdi dir="ltr">Out-of-order</bdi>
7. <bdi dir="ltr">Timeout</bdi>، <bdi dir="ltr">Retry</bdi> و <bdi dir="ltr">Failure State</bdi>
8. <bdi dir="ltr">Compensation/Reversal/Correction</bdi>
9. <bdi dir="ltr">Accounting Fact</bdi> و <bdi dir="ltr">Journal</bdi>
10. <bdi dir="ltr">Reconciliation</bdi> و <bdi dir="ltr">Manual Repair</bdi>
11. <bdi dir="ltr">SLO</bdi> و <bdi dir="ltr">Observability</bdi>
12. تیم مالک و مسیر <bdi dir="ltr">Escalation</bdi>

**تحویل‌دادنی**

- <bdi dir="ltr">Evidence Pack</bdi> سه سناریو
- <bdi dir="ltr">Migration Roadmap</bdi> در موج‌های ۰ تا ۴
- <bdi dir="ltr">Cutover/Reconciliation Checklist</bdi>
- <bdi dir="ltr">ADR</bdi>های نهایی

**معیار قبولی**

- هیچ <bdi dir="ltr">Dual Write</bdi> بدون الگوی کنترل و مغایرت‌گیری وجود نداشته باشد.
- <bdi dir="ltr">Rollback</bdi> مهاجرت و مالک تصمیم <bdi dir="ltr">Go/No-Go</bdi> روشن باشد.

### هفتهٔ ۲۴: دفاع نهایی معماری

**ساختار دفاع ۹۰ دقیقه‌ای**

- ۱۵ دقیقه: <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Domain</bdi> و <bdi dir="ltr">Context Map</bdi>
- ۱۵ دقیقه: معماری کد و سرویس‌ها
- ۳۰ دقیقه: سه سناریو، هرکدام ۱۰ دقیقه
- ۱۵ دقیقه: داده، حسابداری، شکست و <bdi dir="ltr">Reconciliation</bdi>
- ۱۰ دقیقه: <bdi dir="ltr">Runtime</bdi>، <bdi dir="ltr">SLO</bdi>، <bdi dir="ltr">Security</bdi>، <bdi dir="ltr">DR</bdi> و <bdi dir="ltr">Ownership</bdi>
- ۵ دقیقه: <bdi dir="ltr">Migration Roadmap</bdi> و تصمیم‌های باز

**خروجی نهایی**

1. <bdi dir="ltr">Banking Capability Map</bdi>
2. <bdi dir="ltr">Domain/Subdomain Map</bdi>
3. <bdi dir="ltr">Bounded Context Map</bdi>
4. پرونده‌های ۱۲‌بخشی دامین‌ها
5. <bdi dir="ltr">Data/Decision Ownership Matrix</bdi>
6. <bdi dir="ltr">Service Catalog</bdi>
7. <bdi dir="ltr">OpenAPI Catalog</bdi>
8. <bdi dir="ltr">AsyncAPI/Event Catalog</bdi>
9. <bdi dir="ltr">Accounting Fact/Rule Catalog</bdi>
10. <bdi dir="ltr">Logical/Physical Data Model</bdi>
11. <bdi dir="ltr">Saga/Failure/Compensation Matrix</bdi>
12. <bdi dir="ltr">Runtime/NFR/SLO/DR Architecture</bdi>
13. <bdi dir="ltr">ADR Log</bdi>
14. <bdi dir="ltr">Service/Team Ownership Map</bdi>
15. <bdi dir="ltr">Migration Roadmap</bdi>
16. کد و تست سه <bdi dir="ltr">Vertical Slice</bdi>

**خروجی پس از دفاع**

- <bdi dir="ltr">Gap List</bdi> اولویت‌بندی‌شده
- برنامهٔ ۹۰ روزهٔ بعدی
- تصمیم دربارهٔ عمق بعدی: <bdi dir="ltr">Architecture Leadership</bdi>، <bdi dir="ltr">Data/Performance</bdi>، <bdi dir="ltr">Platform/SRE</bdi> یا <bdi dir="ltr">Banking Domain Specialization</bdi>

---

## ۱۰. مدل ارزیابی

| حوزه | امتیاز |
|---|---:|
| <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Domain Boundary</bdi> و <bdi dir="ltr">Ownership</bdi> | ۲۰ |
| طراحی کد، <bdi dir="ltr">Aggregate</bdi>، <bdi dir="ltr">Refactoring</bdi> و <bdi dir="ltr">Test</bdi> | ۱۵ |
| <bdi dir="ltr">API/Event Contract</bdi> و <bdi dir="ltr">Evolution</bdi> | ۱۵ |
| <bdi dir="ltr">Transaction</bdi>، <bdi dir="ltr">Consistency</bdi>، <bdi dir="ltr">Failure</bdi> و <bdi dir="ltr">Reconciliation</bdi> | ۲۰ |
| <bdi dir="ltr">Accounting</bdi>، <bdi dir="ltr">Data Model</bdi> و <bdi dir="ltr">Performance</bdi> | ۱۵ |
| <bdi dir="ltr">Security</bdi>، <bdi dir="ltr">Observability</bdi>، <bdi dir="ltr">SLO</bdi> و <bdi dir="ltr">DR</bdi> | ۱۰ |
| <bdi dir="ltr">ADR</bdi>، <bdi dir="ltr">Team Ownership</bdi> و کیفیت دفاع | ۵ |
| **جمع** | **۱۰۰** |

### شرط عبور

- امتیاز کل حداقل ۷۵
- هیچ‌یک از چهار حوزهٔ <bdi dir="ltr">Boundary</bdi>، <bdi dir="ltr">Financial Correctness</bdi>، <bdi dir="ltr">Failure Handling</bdi> و <bdi dir="ltr">Accounting</bdi> کمتر از ۶۰٪ امتیاز خود نباشد.
- هر سه سناریوی نهایی واقعاً اجرا شوند؛ اسلاید یا <bdi dir="ltr">Diagram</bdi> به‌تنهایی کافی نیست.

### <bdi dir="ltr">Gate</bdi>های رسمی

| <bdi dir="ltr">Gate</bdi> | پایان هفته | پرسش اصلی |
|---|---:|---|
| ۱ | ۴ | آیا <bdi dir="ltr">Domain Model</bdi> و مرز کد واقعاً مستقل و قابل آزمون است؟ |
| ۲ | ۸ | آیا مالکیت مانده، تراکنش و <bdi dir="ltr">Read Model</bdi> روشن و صحیح است؟ |
| ۳ | ۱۲ | آیا جریان توزیع‌شده بدون <bdi dir="ltr">Global Transaction</bdi> و فرض <bdi dir="ltr">Exactly-once</bdi> ایمن است؟ |
| ۴ | ۱۶ | آیا مدل حسابداری/داده تحت هم‌زمانی و بار، قابل دفاع است؟ |
| ۵ | ۲۰ | آیا مرز دامین‌های بانکی در سناریوهای واقعی حفظ شده است؟ |
| ۶ | ۲۴ | آیا معماری از <bdi dir="ltr">Business Capability</bdi> تا <bdi dir="ltr">Runtime</bdi> و <bdi dir="ltr">Team Ownership</bdi> کامل است؟ |

## ۱۱. قواعد جلوگیری از پراکندگی

- در طول دوره پروژهٔ دوم ایجاد نمی‌شود.
- <bdi dir="ltr">Kubernetes</bdi> پیش از هفتهٔ ۲۲ موضوع اصلی نمی‌شود.
- <bdi dir="ltr">Kafka</bdi> پیش از روشن‌شدن مالک و مرز <bdi dir="ltr">Event</bdi> در هفتهٔ ۹ وارد طراحی نمی‌شود.
- <bdi dir="ltr">Microservice</bdi> بدون <bdi dir="ltr">ADR</bdi> و شواهد استخراج نمی‌شود.
- <bdi dir="ltr">BIAN</bdi>، نام جدول و ساختار سازمانی جای <bdi dir="ltr">Domain Discovery</bdi> را نمی‌گیرند.
- برای نمایش معماری از <bdi dir="ltr">Diagram</bdi> بدون <bdi dir="ltr">Ownership/Decision/Failure</bdi> استفاده نمی‌شود.
- درصد <bdi dir="ltr">Code Coverage</bdi> هدف اصلی نیست؛ پوشش <bdi dir="ltr">Invariant</bdi>، <bdi dir="ltr">Failure</bdi> و <bdi dir="ltr">Contract</bdi> هدف است.
- ابزار جدید فقط وقتی اضافه می‌شود که یک خروجی اجباری برنامه را ممکن کند.
- کد تولیدی بانک در <bdi dir="ltr">Lab</bdi> کپی نمی‌شود؛ مسئله و قید آن با دادهٔ ساختگی بازآفرینی می‌شود.

## ۱۲. منابع رسمی حداقلی و ترتیب استفاده

این‌ها مرجع کنترل برنامه‌اند، نه فهرست کتاب‌هایی که باید کامل خوانده شوند.

- هفته‌های ۱ و ۲: [<bdi dir="ltr">BIAN Service Landscape 14.0</bdi>](https://bian.org/deliverables/service-landscape/)
- هفته‌های ۲ تا ۴: [<bdi dir="ltr">Spring Modulith Fundamentals</bdi>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)، [<bdi dir="ltr">Module Verification</bdi>](https://docs.spring.io/spring-modulith/reference/verification.html) و [<bdi dir="ltr">Module Integration Testing</bdi>](https://docs.spring.io/spring-modulith/reference/testing.html)
- هفته‌های ۴ تا ۱۰: [<bdi dir="ltr">Spring Boot Testcontainers</bdi>](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html)
- هفتهٔ ۶: [<bdi dir="ltr">OWASP API Security Top 10</bdi>](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- هفتهٔ ۷: [<bdi dir="ltr">PostgreSQL Transaction Isolation</bdi>](https://www.postgresql.org/docs/current/transaction-iso.html)
- هفته‌های ۹ و ۱۰: [<bdi dir="ltr">AsyncAPI 3.1 Specification</bdi>](https://www.asyncapi.com/docs/reference/specification/latest)، [<bdi dir="ltr">Apache Kafka Design</bdi>](https://kafka.apache.org/41/design/design/)، [<bdi dir="ltr">Producer Configuration</bdi>](https://kafka.apache.org/41/configuration/producer-configs/) و [<bdi dir="ltr">Debezium Outbox Event Router</bdi>](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
- هفتهٔ ۱۲: [<bdi dir="ltr">OpenTelemetry Signals</bdi>](https://opentelemetry.io/docs/concepts/signals/) و [<bdi dir="ltr">Context Propagation</bdi>](https://opentelemetry.io/docs/concepts/context-propagation/)
- هفتهٔ ۱۵: [<bdi dir="ltr">PostgreSQL Declarative Partitioning</bdi>](https://www.postgresql.org/docs/current/ddl-partitioning.html) و [<bdi dir="ltr">Oracle Reference Partitioning</bdi>](https://docs.oracle.com/en/database/oracle/oracle-database/26/vldbg/partition-admin.html)
- هفتهٔ ۲۱: [<bdi dir="ltr">Webpack Module Federation Concepts</bdi>](https://webpack.js.org/concepts/module-federation/) برای مقایسه با قرارداد <bdi dir="ltr">Web Component/Manifest</bdi>
- هفتهٔ ۲۲: [<bdi dir="ltr">Kubernetes Deployments</bdi>](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)، [<bdi dir="ltr">Horizontal Pod Autoscaling</bdi>](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)، [<bdi dir="ltr">Google SRE: Implementing SLOs</bdi>](https://sre.google/workbook/implementing-slos/) و [<bdi dir="ltr">Example SLO Document</bdi>](https://sre.google/workbook/slo-document/)

## ۱۳. ممیزی نهایی پوشش موارد جاافتادهٔ قبلی

| مورد جاافتاده | محل قطعی در نسخهٔ نهایی |
|---|---|
| <bdi dir="ltr">SOLID</bdi> و <bdi dir="ltr">Pattern</bdi>های کاربردی | هفته‌های ۳ و ۴؛ <bdi dir="ltr">Refactoring</bdi> مستمر در <bdi dir="ltr">Definition of Done</bdi> |
| <bdi dir="ltr">Code Smell</bdi> و <bdi dir="ltr">Refactoring</bdi> واقعی | هفتهٔ ۴ و <bdi dir="ltr">Code Review</bdi> هر هفته |
| <bdi dir="ltr">Unit/Integration/Architecture/Contract Test</bdi> | هفته‌های ۱ تا ۱۰ و سپس به‌صورت مستمر |
| <bdi dir="ltr">Concurrency/Failure/Performance Test</bdi> | هفته‌های ۷، ۱۲، ۱۶ و ۲۳ |
| <bdi dir="ltr">PostgreSQL</bdi> عملی | هفته‌های ۴، ۷، ۸، ۱۰، ۱۵ و ۱۶ |
| <bdi dir="ltr">Oracle</bdi> عمیق | هفته‌های ۷، ۱۵ و ۱۶ |
| <bdi dir="ltr">CQRS</bdi> کامل | هفته‌های ۸، ۱۰ و ۱۶ |
| <bdi dir="ltr">Micro-frontend</bdi> | هفتهٔ ۲۱ با <bdi dir="ltr">Shell</bdi> و دو <bdi dir="ltr">Widget</bdi> مستقل |
| <bdi dir="ltr">IAM</bdi> و <bdi dir="ltr">API Security</bdi> | هفتهٔ ۶؛ تکمیل در هفته‌های ۲۱ و ۲۲ |
| <bdi dir="ltr">Observability</bdi> | هفتهٔ ۱۲؛ <bdi dir="ltr">Production Dashboard/SLO</bdi> در هفتهٔ ۲۲ |
| <bdi dir="ltr">Kubernetes</bdi> و <bdi dir="ltr">Runtime</bdi> | هفتهٔ ۲۲ پس از آماده‌شدن نرم‌افزار |
| <bdi dir="ltr">SLO</bdi>، <bdi dir="ltr">DR</bdi> و <bdi dir="ltr">Runbook</bdi> | هفته‌های ۱۲، ۲۲ و ۲۳ |
| <bdi dir="ltr">Team Topology</bdi> و اختیار <bdi dir="ltr">PO/Engineering</bdi> | هفتهٔ ۲۲ و دفاع هفتهٔ ۲۴ |
| <bdi dir="ltr">Migration</bdi> از وضع موجود | هفتهٔ ۲۳ |

## ۱۴. پیش‌هفتهٔ شروع؛ خارج از ۲۴ هفته

این آماده‌سازی یک‌باره حداکثر دو ساعت زمان می‌برد:

1. نصب/کنترل <bdi dir="ltr">Java 21</bdi>، <bdi dir="ltr">Maven</bdi>، <bdi dir="ltr">Docker</bdi> و <bdi dir="ltr">Git</bdi>
2. ایجاد مخزن با ساختار پایه
3. اجرای <bdi dir="ltr">`mvn verify`</bdi>
4. اجرای <bdi dir="ltr">PostgreSQL</bdi> و <bdi dir="ltr">Kafka</bdi> با <bdi dir="ltr">Docker/Testcontainers</bdi>
5. ثبت پاسخ اولیهٔ خودت به سناریوی «اعطا و واریز به سپرده» بدون مطالعهٔ جدید
6. نمره‌گذاری خط پایه با <bdi dir="ltr">Rubric</bdi> نهایی

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


<bdi dir="ltr">Board</bdi> دوره فقط این وضعیت‌ها را دارد: <bdi dir="ltr">`Backlog → Ready → Doing → Review → Gate → Done`</bdi>. در هر زمان فقط خروجی یک هفته در <bdi dir="ltr">`Doing`</bdi> است تا مطالعهٔ چند موضوع جای تکمیل <bdi dir="ltr">Artifact</bdi> را نگیرد.

در آغاز هر هفته:

1. درس فشرده و مسئلهٔ بانکی همان هفته ارائه می‌شود.
2. قالب خروجی و <bdi dir="ltr">Acceptance Test</bdi> مشخص می‌شود.
3. کد، <bdi dir="ltr">Diagram</bdi>، <bdi dir="ltr">DDL</bdi> یا تصمیم تو بررسی و نقد می‌شود.
4. خطاها و <bdi dir="ltr">Failure Scenario</bdi>ها روی خروجی اعمال می‌شوند.
5. فقط بعد از عبور از <bdi dir="ltr">Definition of Done</bdi>، هفته بسته می‌شود.

در <bdi dir="ltr">Gate</bdi>ها، ضعف مهم با جلو رفتن صوری پوشانده نمی‌شود. همان بخش با تمرین کوچک‌تر تکرار می‌شود؛ اما نقشهٔ ۲۴ هفته‌ای تغییر مسیر نمی‌دهد مگر اینکه شواهد اجرای واقعی نشان دهد بار زمانی یا پیش‌نیاز فنی اشتباه برآورد شده است.

این سند نقشهٔ راه مرجع است. شروع واقعی از «پیش‌هفته» و سپس هفتهٔ ۱، <bdi dir="ltr">Capability Map</bdi> بانک، خواهد بود.

</div>
