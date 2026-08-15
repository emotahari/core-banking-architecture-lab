# نقشهٔ راه نهایی ۲۴ هفته‌ای معماری نرم‌افزار و Core Banking

نسخه: ۱٫۰  
تاریخ مبنا: ۱۲ مرداد ۱۴۰۵ / ۳ اوت ۲۰۲۶  
مخاطب: مسیر شخصی‌سازی‌شدهٔ معماری Core Banking  
مدت: ۲۴ هفته، ۱۲ اسپرینت دوهفته‌ای، هفته‌ای ۴ تا ۶ ساعت

> الحاقیهٔ ۲۴ مرداد ۱۴۰۵ / ۱۵ اوت ۲۰۲۶: از Week 02 دو ریل Code Craft و Core Banking Case File به برنامه افزوده شده‌اند. برنامهٔ ۴ تا ۶ ساعتهٔ قبلی «ریل اصلی» باقی می‌ماند و نسخهٔ کامل توسعه‌یافته ۵۱۰ دقیقه در هفته است؛ هیچ سرفصل، Gate یا Artifact قبلی حذف یا فشرده نشده است.

## ۱. تصمیم نهایی برنامه

این برنامه یک دورهٔ واحد با دو محور هم‌زمان است:

- محور فنی: طراحی کد، معماری سرویس، معماری توزیع‌شده، داده و تراکنش، معماری اجرایی و سازمانی
- محور دامینی: شناخت Core Banking، مرزبندی دامین‌ها، مالکیت داده و تصمیم، سرویس‌ها و روابط میان آن‌ها

پروژهٔ ثابت دوره یک Core Banking آموزشی با شش دامین اصلی است:

1. Party & Customer
2. Product & Agreement
3. Deposits
4. Lending
5. Payments
6. Accounting

سه برش عمودی پروژه واقعاً پیاده‌سازی، تست و دفاع می‌شوند:

1. اعطای تسهیلات و واریز مبلغ به سپرده
2. انتقال وجه بین‌شعبه‌ای
3. شکست سپردهٔ بلندمدت و اصلاح سود

هدف ساخت یک Core Banking کامل تولیدی در ۲۴ هفته نیست. هدف، ساخت معماری کامل و پیاده‌سازی سه جریان باریک اما انتها‌به‌انتهاست؛ به‌اندازه‌ای که بتوان صحت مرزها، تراکنش‌ها، Eventها، حسابداری، شکست‌ها و الزامات اجرایی را اثبات کرد.

## ۲. نتیجه‌ای که در پایان باید حاصل شود

در پایان هفتهٔ ۲۴ باید بتوانی:

- زنجیرهٔ `Capability → Domain → Subdomain → Bounded Context → Module/Service → API/Event` را برای یک قابلیت بانکی طی کنی.
- برای هر تصمیم و داده یک مالک صریح تعیین کنی و مشخص کنی چه دامین‌هایی نباید مالک آن باشند.
- میان Modular Monolith و Microservice با معیارهای تغییر، تراکنش، تیم، استقرار، مقیاس و ریسک انتخاب کنی.
- Aggregate، Invariant و Transaction Boundary را در کد Java/Spring پیاده‌سازی و آزمون کنی.
- API همگام و قرارداد Event را همراه با Idempotency، Versioning و Error Model طراحی کنی.
- Outbox، Inbox، Kafka، Saga/Process Manager، Retry، Timeout، Compensation، Reversal و Reconciliation را در یک جریان مالی به‌درستی به‌کار ببری.
- ماندهٔ عملیاتی، Ledger، Subledger و GL را از هم تفکیک کنی.
- مدل دادهٔ Oracle و PostgreSQL را براساس Query Pattern، Locking، Partitioning، Indexing و Retention طراحی کنی.
- برای سرویس حیاتی SLI/SLO، Trace، Metric، Log، Runbook، RTO/RPO و مالک Build/Run تعیین کنی.
- معماری را در برابر محصول، توسعه، زیرساخت، عملیات و حسابداری با ADR و شواهد اجرایی دفاع کنی.

## ۳. پنج لایهٔ فنی و جای قطعی آن‌ها

| لایه | پوشش اصلی | تمرین مستمر | شاهد نهایی |
|---|---|---|---|
| ۱. طراحی کد | هفته‌های ۱ تا ۶ | Refactoring، Unit Test و Code Review در تمام ۲۴ هفته | Domain Model تمیز، Patternهای موجه، تست‌های قواعد و Architecture Test |
| ۲. معماری سرویس | هفته‌های ۲ تا ۶ و ۹ | بازبینی Boundary در هر ADR و هر API/Event | Modular Monolith معتبر، Service Candidate Map و تصمیم‌های استخراج |
| ۳. معماری توزیع‌شده | هفته‌های ۹ تا ۱۲ و ۲۳ | تست Duplicate، Out-of-order و Failure در جریان‌های بعدی | Outbox/Inbox، Kafka، Process Manager، Failure Matrix و سه جریان E2E |
| ۴. داده و تراکنش | هفته‌های ۷، ۸ و ۱۳ تا ۱۶ | بررسی مالکیت و Consistency در همهٔ دامین‌ها | مدل Oracle/PostgreSQL، Ledger/Subledger، CQRS، Locking و Performance Test |
| ۵. معماری اجرایی و سازمانی | هفته‌های ۵، ۶، ۱۲ و ۲۱ تا ۲۴ | Security، Observability و Ownership از میانهٔ دوره | IAM، Micro-frontend، Kubernetes، SLO/DR، Team/Service Ownership و Migration Roadmap |

محور دامین بانکی در همهٔ هفته‌ها فعال است؛ موضوعات فنی هیچ‌گاه روی مثال فروشگاه یا سفارش عمومی تمرین نمی‌شوند.

## ۴. اصلاحات قطعی نسبت به نسخهٔ قبلی

1. کدنویسی، تست و Refactoring یک ریل دائمی است، نه موضوع دو هفتهٔ خاص.
2. PostgreSQL به‌صورت عملی استفاده می‌شود و Oracle به‌صورت مقایسه‌ای و در طراحی فیزیکی عمیق می‌شود.
3. CQRS فقط یک اصطلاح یا Projection ساده نیست؛ Command Model، Read Model، Lag، Rebuild و Reconciliation پیاده می‌شوند.
4. IAM از هفتهٔ ۶، Observability از هفتهٔ ۱۲ و SLO از هفتهٔ ۲۲ وارد می‌شوند؛ همگی در یک هفته فشرده نشده‌اند.
5. Micro-frontend یک تمرین مستقل در هفتهٔ ۲۱ دارد و با نیاز «افزودن Widget توسط سامانه‌ها و تکنولوژی‌های مختلف» طراحی می‌شود.
6. BIAN فهرست آمادهٔ Microservice نیست؛ برای کنترل پوشش Capabilityها و زبان مشترک استفاده می‌شود.
7. ابتدا Modular Monolith ساخته می‌شود؛ استخراج سرویس فقط پس از مشاهدهٔ مرز، وابستگی و نیاز استقرار مستقل انجام می‌گیرد.
8. سه سناریوی نهایی از ابتدا ثابت می‌مانند تا همهٔ موضوعات روی یک پروژه انباشته شوند.

## ۵. سطح هدف و حدود برنامه

این برنامه برای سطح فعلی تو طراحی شده است: تجربهٔ طولانی تحلیل و طراحی سامانه‌های بانکی، مدیریت محصول و توسعه، و آشنایی عملی با Java، Spring، Oracle، DB2، Kafka و Docker. بنابراین آموزش Syntax جاوا، CRUD مقدماتی یا مبانی عمومی بانکداری در آن جایی ندارد.

در ۹۶ تا ۱۴۴ ساعت، خروجی واقع‌بینانه «معمار راهکار بانکیِ قادر به طراحی و نمونه‌سازی» است؛ نه DBA اوراکل، مدیر Kubernetes، متخصص امنیت یا توسعه‌دهندهٔ ارشد Frontend. در موضوعات تخصصی، باید بتوانی تصمیم درست بگیری، سؤال درست بپرسی و طرح را اعتبارسنجی کنی؛ تسلط عملی عمیق هر تخصص یک مسیر مستقل است.

## ۶. ریتم اجرایی هر هفته

### برنامهٔ استاندارد شش‌ساعته

| فعالیت | زمان |
|---|---:|
| مطالعهٔ هدایت‌شده و بحث مفهومی | ۹۰ دقیقه |
| تحلیل دامین و ترسیم مدل | ۷۵ دقیقه |
| کدنویسی و تست | ۱۳۵ دقیقه |
| Failure/Performance/Security Exercise | ۳۰ دقیقه |
| تکمیل ADR، Catalog یا پروندهٔ دامین | ۳۰ دقیقه |

### نسخهٔ حداقلی چهارساعته

| فعالیت | زمان |
|---|---:|
| مفهوم و منبع اصلی | ۶۰ دقیقه |
| تحلیل دامین | ۴۵ دقیقه |
| کدنویسی و تست | ۱۰۵ دقیقه |
| مستندسازی و دفاع کوتاه | ۳۰ دقیقه |

اگر یک هفته فقط چهار ساعت زمان وجود داشت، دامنهٔ پیاده‌سازی کوچک می‌شود؛ تست، خروجی و Gate حذف نمی‌شوند.

### چرخهٔ ثابت کار

1. یادگیری مفهوم روی یک مسئلهٔ بانکی مشخص
2. مدل‌سازی و تصمیم معماری
3. پیاده‌سازی یک Vertical Slice کوچک
4. شکستن عمدی راه‌حل با تست شکست یا هم‌زمانی
5. Refactor، ثبت ADR و دفاع ده‌دقیقه‌ای

### دو ریل افزوده از Week 02

پس از تکمیل چرخهٔ اصلی، هر هفته دو جلسهٔ مستقل اجرا می‌شود:

| ریل افزوده | زمان | خروجی |
|---|---:|---|
| Code Craft Lab | ۱۰۵ دقیقه | Baseline، Smell Map، Characterization Test، Refactor، Pattern Decision، Edge Test و Self-review |
| Core Banking Case File | ۴۵ دقیقه | Timeline، معماری/فناوری جاری، Domain hypothesis، شکست‌ها، دستاورد تازه و درس انتقالی |

نقشهٔ Patternها و پرونده‌های پیشنهادی Week 02 تا Week 24 در [الحاقیهٔ ثابت هفتگی](docs/course/expanded-weekly-tracks.md) نگهداری می‌شود. موضوع هر پرونده هنگام شروع هفته با منابع جاری دوباره کنترل خواهد شد.

## ۷. Definition of Done هفتگی

هیچ هفته‌ای صرفاً با «خواندن مطالب» تمام‌شده محسوب نمی‌شود. خروجی هفتگی باید شرایط زیر را داشته باشد:

- Artifact یا کد در Git ثبت و با شمارهٔ هفته Tag شده باشد.
- `mvn verify` موفق باشد.
- قواعد دامینی جدید Unit Test داشته باشند.
- مرزهای جدید Architecture Test یا Module Verification داشته باشند.
- تغییر قرارداد با OpenAPI یا AsyncAPI ثبت شده باشد.
- دست‌کم یک مسیر منفی، Failure یا Edge Case آزموده شده باشد.
- تصمیم غیر بدیهی در ADR ثبت شده باشد.
- بتوانی در ده دقیقه توضیح بدهی: مالک داده کیست، مرز تراکنش کجاست و در شکست چه رخ می‌دهد.

در هفته‌هایی که یک مورد موضوعیت ندارد، در گزارش هفته با عبارت `Not Applicable` و دلیل صریح ثبت می‌شود؛ خالی گذاشته نمی‌شود.

### قرارداد مستندسازی

- Capability Map برای سلسله‌مراتب قابلیت‌ها
- Context Map برای رابطهٔ دامین‌ها
- C4 System/Container/Component برای معماری ایستا
- Sequence Diagram برای جریان بین سرویس‌ها
- State Machine برای چرخهٔ عمر و Process Manager
- ERD برای مدل داده
- ADR با قالب ثابت: Context، Forces، Options، Decision، Consequences، Verification و Revisit Trigger

هر Diagram باید Version، Scope و مالک اجزای اصلی را نشان دهد. Diagramی که مرز، مالکیت یا هدف تصمیم را روشن نکند، خروجی معماری محسوب نمی‌شود.

## ۸. خط پایهٔ فنی پروژه

### فناوری‌ها

- Java 21 LTS؛ انتخابی محافظه‌کارانه برای تمرکز بر معماری و سازگاری سازمانی
- Spring Boot 4.1 و Spring Modulith 2.1
- Maven
- PostgreSQL برای اجرای روزانه و تست‌های Integration/Concurrency
- Oracle 23ai برای DDL، Partitioning، Query Plan و تفاوت‌های فیزیکی
- Apache Kafka 4.1
- Testcontainers برای PostgreSQL، Kafka و تست Integration
- OpenAPI 3.1 برای APIهای همگام
- AsyncAPI 3.1 برای قراردادهای پیام
- Docker Compose برای محیط توسعه
- OpenTelemetry برای Trace، Metric و Log Correlation
- Prometheus و Grafana؛ یک Backend سازگار با OpenTelemetry برای Trace
- Kubernetes Manifest در هفتهٔ ۲۲؛ ادارهٔ کلاستر خارج از محدودهٔ دوره است
- React/Vite برای Shell و Widget نمونه؛ قرارداد اتصال Micro-frontend مبتنی بر Runtime Manifest و Web Component خواهد بود تا به یک Framework محدود نشود

Spring Boot 4.1 حداقل Java 17 می‌خواهد و با Java 26 نیز سازگار است؛ بنابراین Java 21 انتخاب محدودکننده‌ای برای این پروژه نیست. این انتخاب عمدی است تا زمان دوره صرف قابلیت‌های زبان جدید نشود.

### ساختار مخزن

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

تا پایان هفتهٔ ۸، راه‌حل اصلی Modular Monolith است. در هفته‌های ۹ و ۱۰ فقط ماژول‌هایی استخراج می‌شوند که ADR آن‌ها استخراج را توجیه کرده باشد. Tag مخزن امکان مقایسهٔ قبل و بعد را نگه می‌دارد.

## ۹. مدل خروجی دامین‌ها

### عمق بررسی

| سطح | دامین‌ها | خروجی مورد انتظار |
|---|---|---|
| عمیق | Deposits، Lending، Payments، Accounting | مدل، کد، داده، API/Event، شکست، حسابداری و کارایی |
| تفصیلی | Party/Customer، Product/Agreement، Teller/Cash، Collateral، Collections | پروندهٔ کامل، مرزبندی، Catalog و نمونهٔ قرارداد |
| معماری کلان | Cards، Channels، Checks، Fees، Limits، AML، Fraud، Risk، IFRS، Regulatory Reporting | Capability Card، مالکیت، نوع ارتباط و وابستگی |

### پروندهٔ ثابت ۱۲‌بخشی هر دامین

1. هدف، دامنه و موارد خارج از دامنه
2. Capabilityها و Use Caseهای اصلی
3. زبان مشترک و مفاهیم دامینی
4. Aggregateها، State Machineها و Invariantها
5. داده‌ها و تصمیم‌های تحت مالکیت
6. داده‌ها و تصمیم‌هایی که نباید مالک آن‌ها باشد
7. Module/Service Candidateها و دلیل مرزبندی
8. APIهای ورودی و خروجی
9. Domain Eventها و Integration Eventهای تولیدی/مصرفی
10. Context Map، Upstream/Downstream و نوع وابستگی
11. Transaction، Consistency، Idempotency، نقاط شکست و Reconciliation
12. تیم مالک، SLO، Security، Audit، Retention و سایر NFRها

### فرضیهٔ اولیهٔ مالکیت

| موضوع | مالک اولیه | نکته |
|---|---|---|
| هویت Party و وضعیت Customer | Customer | Lending یا Deposits فقط Reference/Snapshot لازم را نگه می‌دارند. |
| تعریف و نسخهٔ Product/Pricing | Product | شرایط قرارداد منعقدشده با تغییر Product عوض نمی‌شود. |
| شرایط قطعی قرارداد | Agreement در دامین صاحب قرارداد | Lending/Deposits Snapshot مؤثر را مالک است. |
| ماندهٔ قابل برداشت و Hold سپرده | Deposits | Accounting نباید ماندهٔ عملیاتی سپرده را کنترل کند. |
| ماندهٔ اصل، برنامه و بدهی تسهیلات | Lending | Accounting دفتر مالی متناظر را نگه می‌دارد، نه تصمیم وصول را. |
| Payment Order، Clearing و Settlement State | Payments | Channel فقط درخواست و نمایش را مالک است. |
| Journal، Subledger و GL | Accounting | رویداد کسب‌وکار را ترجمه می‌کند؛ منطق عملیاتی دامین را مالک نمی‌شود. |
| وضعیت یک فرایند چنددامینی | Process Manager | نباید داده یا قواعد داخلی دامین‌ها را تصاحب کند. |

این جدول تصمیم نهایی معماری نیست؛ فرضیه‌ای است که در طول دوره با سناریو و شواهد اصلاح می‌شود.

---

# برنامهٔ ۲۴ هفته‌ای

## اسپرینت ۱ — نقشهٔ بانک، زبان و مرزها

### هفتهٔ ۱: Capability تا API/Event

**فنی**

- تفاوت Business Architecture، Solution Architecture و Software Architecture
- Coupling، Cohesion، Encapsulation و Information Hiding
- تفاوت System، Domain، Subdomain، Bounded Context، Module و Service
- زنجیرهٔ کامل `Capability → … → API/Event`

**دامینی**

- ترسیم Capability Map سطح ۱ بانک
- طبقه‌بندی «هستهٔ بانکداری»، «عملیات و خدمات بانکداری»، «سامانه‌های سازمانی» و «اکوسیستم دیجیتال»
- استفاده از BIAN 14.0 برای یافتن شکاف‌ها، نه تبدیل هر Service Domain به Microservice

**کد و تمرین**

- ایجاد مخزن و Pipeline اولیهٔ `mvn verify`
- ساخت Value Objectهای `Money`، `AccountId`، `CustomerId` و `BranchId`
- آزمون برابری، Currency، گردکردن و ورودی نامعتبر

**تحویل‌دادنی**

- Capability Map نسخهٔ ۱
- واژه‌نامهٔ حداقل ۴۰ اصطلاح کلیدی
- پاسخ معماری اولیه به سه سناریوی نهایی برای ثبت خط پایه

**معیار قبولی**

- هیچ Service Candidate بدون Capability و مالک کسب‌وکار معرفی نشده باشد.
- بتوان تفاوت BIAN Service Domain با Deployable Microservice را روشن توضیح داد.

### هفتهٔ ۲: Strategic DDD و مالکیت

**فنی**

- Domain/Subdomain، Core/Supporting/Generic
- Bounded Context و Ubiquitous Language
- Context Map: Customer/Supplier، Conformist، ACL و Published Language
- Source of Truth و Ownership of Decision

**دامینی**

- مرزبندی اولیهٔ شش دامین اصلی
- تعیین «مالک چه چیزی است؟»، «چه چیزی را نباید مالک باشد؟» و «از چه کسی می‌گیرد؟»

**کد و تمرین**

- ساخت شش ماژول منطقی در Spring Modulith
- اجرای Module Verification برای Cycle و دسترسی به Package داخلی
- ثبت Dependency مجاز بین ماژول‌ها

**تحویل‌دادنی**

- Domain Map و Context Map نسخهٔ ۱
- Data/Decision Ownership Matrix نسخهٔ ۱
- اسکلت شش پروندهٔ دامینی
- Architecture Fitness Test اولیه

**Gate اسپرینت**

یک قابلیت جدید مانند «مسدودی قضایی سپرده» داده می‌شود. باید زنجیرهٔ Capability تا API/Event، مالک داده و مرزهای Context را بدون شروع از نام جدول یا سرویس طراحی کنی.

---

## اسپرینت ۲ — Domain Model و معماری داخلی کد

### هفتهٔ ۳: Tactical DDD روی Deposits

**فنی**

- Entity، Value Object، Aggregate Root، Invariant و Domain Event
- Repository، Domain Service و Application Service
- SOLID روی کد واقعی، نه تعریف حفظی
- Strategy، Factory، Specification و State؛ تشخیص زمان نامناسب استفاده از Pattern

**دامینی**

- `DepositAccount`، `Balance`، `Hold` و Lifecycle حساب
- قواعد برداشت، مسدودی، رفع مسدودی و ماندهٔ قابل برداشت

**کد و تمرین**

- پیاده‌سازی `credit`، `debit`، `placeHold` و `releaseHold`
- Strategy محاسبهٔ سود و Specification احراز شرایط عملیات
- Unit Test برای کمبود موجودی، Hold تکراری، مبلغ منفی و State نامعتبر

**تحویل‌دادنی**

- مدل دامینی Deposits نسخهٔ ۱
- فهرست Aggregate و Transaction Boundary
- Code Review Checklist برای Domain Model

**معیار قبولی**

- Controller یا Entity دیتابیس منطق کسب‌وکار را نگه ندارد.
- هیچ Setter عمومی برای دورزدن Invariant وجود نداشته باشد.

### هفتهٔ ۴: Hexagonal Architecture روی Lending

**فنی**

- Layered، Clean و Hexagonal Architecture
- Inbound/Outbound Port و Adapter
- Dependency Inversion، Unit of Work و تست‌پذیری
- Refactoring یک کلاس بزرگ به Strategy/Factory/Policy

**دامینی**

- `LoanAgreement`، `Disbursement`، `RepaymentSchedule` و `Installment`
- قواعد تصویب، قرارداد، اعطا، گردکردن مبلغ و پرداخت قسط

**کد و تمرین**

- Use Case اولیهٔ `GrantLoan`
- Persistence Adapter روی PostgreSQL
- Integration Test با Testcontainers
- بازطراحی یک نمونهٔ Java 8 از Mapping تراکنش‌های مالی برای حفظ ارتباط با محیط واقعی

**تحویل‌دادنی**

- اسکلت Hexagonal قابل اجرا
- ADR-001: معماری داخلی سرویس
- تست معماری برای ممنوعیت وابستگی Domain به Spring/JPA/Kafka

**Gate اسپرینت**

- تمام Invariantها Unit Test دارند.
- Domain بدون Spring Context آزمون می‌شود.
- Adapter دیتابیس با PostgreSQL واقعیِ Testcontainers آزمون شده است.

---

## اسپرینت ۳ — قراردادها، مرز سرویس و امنیت

### هفتهٔ ۵: API و Source of Truth

**فنی**

- Command/Query و تفاوت API دامینی با CRUD
- REST Semantics، OpenAPI، Error Model و Validation
- Idempotency Key، Optimistic Version و API Versioning
- Temporal Data، Effective Dating و Snapshot

**دامینی**

- Party در برابر Customer
- Product Definition، Pricing، Eligibility و Agreement
- مشخص‌کردن داده‌های Reference و Snapshotشونده در قرارداد

**کد و تمرین**

- API ایجاد/مشاهدهٔ Loan Agreement
- ذخیرهٔ Snapshot شرایط Product هنگام انعقاد قرارداد
- تست Contract، Idempotency و تغییر هم‌زمان Version

**تحویل‌دادنی**

- OpenAPI نسخهٔ ۱
- Command/Query Catalog
- ماتریس Source of Truth/Snapshot/Cache

**معیار قبولی**

- تغییر Product، قرارداد قبلی را تغییر ندهد.
- Retry یک Request با Idempotency Key یکسان اثر مالی دوم نسازد.

### هفتهٔ ۶: Modular Monolith یا Microservice و Security by Design

**فنی**

- Transactional Cohesion، Change Coupling، Independent Deployment و Team Boundary
- Shared Database، Shared Library و Distributed Monolith
- AuthN، AuthZ، Scope/Role، Object-level Authorization و Audit
- Threat Modeling سبک و کنترل‌های OWASP API Security

**دامینی**

- تصمیم Module/Service برای Deposits، Lending، Payments و Accounting
- تعیین API Gateway Policy در برابر Business Policy

**کد و تمرین**

- تست مجوز روی Account/Loan متعلق به مشتری دیگر
- Audit Context شامل Actor، Channel، Branch و Correlation ID
- Architecture Test برای جلوگیری از Shared Entity/Repository میان دامین‌ها

**تحویل‌دادنی**

- Service Candidate Map
- ADR-002: معماری Lending
- ADR-003: معماری Accounting
- ADR-004: مرز Deposits و Payments
- Threat Model و Security Checklist اولیه

**Gate اسپرینت**

هیچ Microservice صرفاً به‌دلیل «مدرن‌بودن»، تعداد Entity یا وجود یک BIAN Service Domain ایجاد نشده باشد. هر استخراج باید حداقل دو محرک مستقل و هزینه‌های توزیع را ثبت کند.

---

## اسپرینت ۴ — تراکنش، مانده و CQRS

### هفتهٔ ۷: Isolation، Locking و Concurrency

**فنی**

- ACID و Isolation Level
- Lost Update، Non-repeatable Read، Phantom و Write Skew
- Optimistic/Pessimistic Lock، Atomic Update و Lock Ordering
- Deadlock، Retry Budget و Transaction Boundary

**دامینی**

- برداشت هم‌زمان از سپرده
- Hold و برداشت هم‌زمان
- وصول هم‌زمان قسط
- پرداخت از چند Channel

**کد و تمرین**

- بازتولید Lost Update
- سه راه‌حل: Optimistic Lock، `SELECT FOR UPDATE` و Atomic Conditional Update
- تست هم‌زمانی با تقاضای بیش از موجودی و اثبات عدم منفی‌شدن مانده
- مقایسهٔ رفتار PostgreSQL و Oracle

**تحویل‌دادنی**

- Concurrency Decision Matrix
- Lock Ordering Policy
- تست خودکار Deadlock/Retry و Oversubscription

**معیار قبولی**

- صحت با Sleep تصادفی یا اجرای تک‌Thread اثبات نشده باشد.
- Retry محدود، قابل مشاهده و فقط برای خطاهای Retryable باشد.

### هفتهٔ ۸: Operational Balance، Ledger، Subledger و CQRS

**فنی**

- Source of Truth، Derived Data، Snapshot و Projection
- Command Model، Read Model، Projection Lag و Rebuild
- Operational Ledger، Accounting Subledger و General Ledger
- Reconciliation و Proof of Balance

**دامینی**

- مالک ماندهٔ قابل برداشت، ماندهٔ اصل و اقساط
- تفکیک دفتر معین تسهیلات از وضعیت عملیاتی تسهیلات

**کد و تمرین**

- Read Model صورت‌حساب سپرده
- Projection مصرف‌کنندهٔ رویداد و Rebuild کامل
- Job مغایرت‌گیری بین Operational Transactions و Read Model
- مقایسهٔ Event Sourcing با Event-driven/CQRS و ثبت دلیل استفاده‌نکردن از Event Sourcing به‌عنوان پیش‌فرض

**تحویل‌دادنی**

- مدل دادهٔ ماندهٔ عملیاتی
- مدل اولیهٔ Subledger
- CQRS Consistency Contract شامل Lag مجاز و رفتار در Stale Read
- Reconciliation Specification

**Gate اسپرینت**

برای هر مانده باید مشخص باشد: مالک، روش تغییر، مرز ACID، امکان Rebuild، منبع مغایرت‌گیری و رفتار در تأخیر Projection چیست.

---

## اسپرینت ۵ — Event-driven Architecture قابل اتکا

### هفتهٔ ۹: Command، Domain Event و Integration Event

**فنی**

- تفاوت Command، Domain Event، Integration Event و Query
- Event Notification در برابر Event-Carried State Transfer
- Semantic Event، Schema Evolution و Compatibility
- Correlation ID، Causation ID و Business Transaction ID

**دامینی**

- طراحی پیام‌های فرایند اعطا و واریز به سپرده
- تعیین اینکه چه کسی Command می‌دهد و چه دامین صاحب Event است

**کد و تمرین**

- تعریف Event Envelope استاندارد با این فیلدها:
  `eventId`، `eventType`، `eventVersion`، `occurredAt`، `producer`، `aggregateId`، `aggregateVersion`، `businessTransactionId`، `correlationId`، `causationId`، `partitionKey` و `payload`
- نگارش AsyncAPI برای جریان اعطا
- Contract Compatibility Test

**تحویل‌دادنی**

- Event Catalog نسخهٔ ۱
- AsyncAPI نسخهٔ ۱
- Sequence Diagram اعطای تسهیلات

**معیار قبولی**

- نام Event رخداد گذشته باشد، نه دستور مبهم.
- Consumer برای فهم Payload مجبور به Query همگام غیرضروری نشود.

### هفتهٔ ۱۰: Kafka، Outbox، Inbox و Idempotency

**فنی**

- Topic، Partition، Offset و Consumer Group
- Ordering در محدودهٔ Partition و انتخاب Partition Key
- At-least-once Delivery و محدودهٔ واقعی Kafka Exactly-once
- Transactional Outbox، Inbox، Deduplication و Replay

**کد و تمرین**

- ذخیرهٔ Aggregate و Outbox در یک تراکنش
- انتشار به Kafka و مصرف در سرویس دوم
- Unique Constraint روی `event_id` و Business Idempotency Key
- تست Crash بعد از Commit، پیام تکراری و Replay

**تحویل‌دادنی**

- Outbox/Inbox Schema
- Topic/Partition/Retention Catalog
- Idempotency Policy برای عملیات مالی
- ADR-005: روش انتشار Event

**Gate اسپرینت**

- مصرف دوباره اثر مالی دوم نسازد.
- Replay، Projection را بازسازی کند.
- Ordering مورد نیاز با Aggregate/Business Key مستند و آزموده شود.

---

## اسپرینت ۶ — Saga، شکست و مشاهده‌پذیری

### هفتهٔ ۱۱: Process Manager و State Machine

**فنی**

- Saga، Orchestration، Choreography و Process Manager
- Long-running State Machine، Timeout و Retry Policy
- Business Correlation و وضعیت‌های میانی

**دامینی**

- فرایند اعطای تسهیلات:
  1. ثبت درخواست اعطا در Lending
  2. درخواست Credit به Deposits
  3. دریافت نتیجهٔ واریز
  4. قطعی‌کردن وضعیت Disbursement
  5. پردازش حسابداری و Reconciliation

**کد و تمرین**

- پیاده‌سازی Process Instance پایدار و Versioned
- Handlerهای Idempotent و Timer/Timeout
- جداکردن وضعیت تکمیل عملیات کسب‌وکار از وضعیت Pending حسابداری

**تحویل‌دادنی**

- State Machine و State Transition Table
- ADR-006: Orchestration یا Choreography
- Process Data Model

**معیار قبولی**

- Orchestrator مستقیماً جدول یا منطق داخلی دامین‌ها را تغییر ندهد.
- Restart سرویس وضعیت فرایند را از بین نبرد.

### هفتهٔ ۱۲: Failure، Compensation، Reconciliation و Observability

**فنی**

- Business Failure در برابر Technical Failure
- Retryable/Non-retryable، Backoff/Jitter، DLQ و Poison Message
- Timeout Budget، Circuit Breaker و Bulkhead برای وابستگی‌های همگام
- Rollback، Compensation، Reversal و Correction
- Trace، Metric، Log و Context Propagation

**آزمایش‌های اجباری**

1. Deposits در دسترس نیست.
2. واریز انجام شده ولی پاسخ گم می‌شود.
3. Event دوبار تحویل می‌شود.
4. Accounting موقتاً قطع است.
5. Eventها خارج از ترتیب می‌رسند.
6. سرویس بعد از DB Commit و قبل از Publish متوقف می‌شود.

**کد و تمرین**

- تزریق شش خطا و ثبت نتیجهٔ مورد انتظار
- Trace سراسری با Correlation/Causation
- Metric برای Pending Process، Retry، Duplicate و Reconciliation Mismatch

**تحویل‌دادنی**

- Failure Matrix و Compensation Matrix
- Runbook تعمیر دستی و Reconciliation
- داشبورد اولیهٔ جریان اعطا

**Gate اسپرینت**

هر شکست باید دقیقاً یکی از این پایان‌ها را داشته باشد: Retry کنترل‌شده، Compensation/Reversal، توقف کسب‌وکاری، یا Manual Repair قابل ممیزی. وضعیت «نامعلوم و بدون مالک» مردود است.

---

## اسپرینت ۷ — معماری حسابداری بانکی

### هفتهٔ ۱۳: Accounting Fact و Translator

**فنی و دامینی**

معماری مرجع:

```text
Domain Event
  → Domain-specific Accounting Translator
  → Accounting Fact
  → Effective-dated Accounting Rule
  → Journal + Subledger Entry
```

- تفاوت رخداد کسب‌وکار با Fact حسابداری
- Published Language میان دامین و Accounting
- Rule Version، Effective Date و Rule Selection
- جلوگیری از ورود منطق «اعطای مرابحه» یا «شکست سپرده» به هستهٔ عمومی Journal

**کد و تمرین**

- Fact Schema و Translator برای پنج Event
- Rule Engine ساده و قابل نسخه‌بندی
- تست اینکه Replay با همان نسخهٔ Rule همان نتیجه را می‌دهد

**تحویل‌دادنی**

- Accounting Fact Catalog
- Event-to-Fact Mapping
- ADR-007: مرز Translator و Accounting Engine

**معیار قبولی**

- Accounting Fact اطلاعات لازم برای ثبت و Audit را دارد.
- Event اصلی، Fact و نسخهٔ Rule قابل رهگیری متقابل‌اند.

### هفتهٔ ۱۴: Journal، Subledger، GL و قواعد مالی

**فنی و دامینی**

- Double-entry، Chart of Accounts، Journal و Journal Line
- GL، SL و Auxiliary Dimensions
- Cost Center، Branch، Currency، Fiscal Year و Financial Period
- Accrual، Reversal، Correction و Back-dated Posting
- حفظ جزئیات Event/Subledger و تجمیع فقط در Projection یا GL مناسب

**ده رویداد مرجع**

1. `LoanDisbursed`
2. `LoanPrincipalRepaid`
3. `LoanInterestAccrued`
4. `LatePenaltyAssessed`
5. `DepositCredited`
6. `DepositDebited`
7. `DepositInterestAccrued`
8. `DepositInterestPaid`
9. `PaymentSettled`
10. `TermDepositBroken`

**کد و تمرین**

- ثبت Idempotent Journal
- کنترل `Sum(Debit) = Sum(Credit)`
- رد Period بسته و ثبت Reversal با Link به سند مبنا
- تولید Subledger Entry بدون حذف جزئیات رخداد

**تحویل‌دادنی**

- قواعد ثبت ده Event
- نمونه‌سندهای سپرده، تسهیلات و انتقال وجه
- مدل Rule Versioning و Period Control

**معیار قبولی**

- هیچ Journal نامتوازن ثبت نشود.
- سند اصلاحی سابقهٔ سند اصلی را حذف یا بازنویسی نکند.

---

## اسپرینت ۸ — طراحی فیزیکی و کارایی مالی

### هفتهٔ ۱۵: Oracle/PostgreSQL Physical Design

**فنی**

- طراحی براساس Query Pattern و حجم/Retention
- Primary/Business Key، Foreign Key و Unique Constraint
- Composite/Partial/Local/Global Index
- Range/List/Hash/Composite Partitioning
- Oracle Reference Partitioning و Partition Pruning
- Archive، Purge، Compression و Tablespace Policy

**جداول مرجع**

- `accounting_event`
- `journal`
- `journal_line`
- `subledger_entry`
- `balance_snapshot`
- `outbox_event`
- `inbox_message`
- `process_instance`

**کد و تمرین**

- DDL اجرایی برای PostgreSQL و Oracle
- Reference Partitioning فرزند Journal در Oracle
- Explain Plan برای پنج Query حیاتی

**تحویل‌دادنی**

- Logical و Physical Data Model
- Partition/Index/Retention Matrix
- Critical Query Catalog
- ADR-008: سیاست Partitioning

**معیار قبولی**

- هیچ جدولی فقط به‌دلیل «بزرگ‌بودن احتمالی» Partition نشده باشد.
- کلید Partition با Query، Retention و عملیات نگهداری توجیه شود.

### هفتهٔ ۱۶: Hot Row، Batch، EOD و Performance

**فنی و دامینی**

- Hot Account/Hot GL Row
- Atomic Increment، Optimistic Retry و Event Serialization
- Balance Snapshot و Rebuild
- Batch Chunking، Checkpoint و Restartability
- Interest Accrual/EOD و Business Calendar
- Performance و Capacity Test

**کد و تمرین**

- Load Test روی Debit/Credit و Journal Posting
- ثبت Baseline و یک دور Tuning قابل اندازه‌گیری
- Restart آزمون EOD از Checkpoint بدون ثبت تکراری
- Reconciliation بعد از Load

**تحویل‌دادنی**

- Performance Test Plan و Report
- Hot-row Mitigation Decision
- EOD Runbook
- Snapshot/Rebuild Policy

**Gate اسپرینت**

- صحت مالی در Load صددرصد حفظ شود و Duplicate مالی صفر باشد.
- p50/p95/p99، Throughput، Error Rate و Lock Wait ثبت شوند.
- بهبود پس از Tuning با عدد و Query Plan اثبات شود، نه با احساس.

---

## اسپرینت ۹ — عمق دامین: Customer، Product، Deposits و Teller

### هفتهٔ ۱۷: Party/Customer، Product و Agreement

**فنی و دامینی**

- Party، Customer، KYC و Customer Relationship
- Product Definition، Pricing، Eligibility و Bundle
- Temporal Data و Effective-dated Rate
- Agreement، Contract Terms و Immutable Snapshot
- ACL و Reference Data Cache

**کد و تمرین**

- انتخاب نرخ مؤثر بر تاریخ قرارداد
- Snapshot غیرقابل‌تغییر Product Terms
- Eventهای `CustomerStatusChanged` و `ProductVersionActivated`

**تحویل‌دادنی**

- سه پروندهٔ دامینی کامل
- API/Event Catalog و Context Map مرتبط
- Temporal Data Model

**معیار قبولی**

- سابقهٔ قرارداد با تغییر اطلاعات Master از بین نرود.
- Cache هیچ‌گاه به‌جای Source of Truth معرفی نشود.

### هفتهٔ ۱۸: Deposits، Teller و Cash

**فنی و دامینی**

- چرخهٔ افتتاح، فعال‌سازی، واریز، برداشت، Hold، Dormancy و بستن
- سود، تمدید، شکست سپرده و Business Calendar
- Cut-off، Back Value Date و Monetary Precision
- Teller Session، Cashbox، Branch Vault، Shortage/Overage و Cash Transfer

**کد و تمرین**

- برش کامل `BreakTermDeposit`
- محاسبهٔ سود مستحق، تفاوت سود پرداختی و مبلغ اصلاح
- Event و Accounting Factهای لازم
- تست Duplicate، Back-dated و شکست پس از محاسبه/قبل از ثبت

**تحویل‌دادنی**

- پروندهٔ کامل Deposits و Teller/Cash
- Deposit Lifecycle State Machine
- Deposit Event Catalog
- سناریوی نهایی شمارهٔ ۳ در وضعیت Beta

**معیار قبولی**

- Deposits مالک محاسبه و وضعیت عملیاتی است؛ Accounting فقط اثر مالی را ثبت می‌کند.
- Reversal/Correction با Rollback ساده اشتباه نشود.

---

## اسپرینت ۱۰ — عمق دامین: Lending، Collections و Payments

### هفتهٔ ۱۹: Lending، Collateral و Collections

**فنی و دامینی**

- Application، Credit Decision، Approval، Agreement و Disbursement
- Schedule Generation، Accrual، Payment Allocation و Settlement
- Collateral Valuation/Allocation/Release
- Delinquency Detection، Collection Case، Restructuring، Write-off و Recovery
- Decision Table و Long-running Workflow

**کد و تمرین**

- Schedule Generator با قواعد گردکردن
- Projection تشخیص Delinquency
- تکمیل برش اعطا و ارتباط آن با Collateral/Collections بدون تصاحب مالکیت

**تحویل‌دادنی**

- پرونده‌های Lending، Collateral و Collections
- Decision/Data Ownership Matrix
- سناریوی نهایی شمارهٔ ۱ در وضعیت Beta

**معیار قبولی**

- Lending مالک بدهی است؛ Collections مالک پرونده و اقدام وصول؛ Collateral مالک وضعیت وثیقه؛ Accounting مالک دفتر مالی.

### هفتهٔ ۲۰: Payments، Cards، Channels و Checks

**فنی و دامینی**

- Payment Order و Payment State Machine
- Authorization، Clearing و Settlement
- Reversal، Refund و Return
- Internal Transfer، پایا/ساتنا، Card Transaction و Cheque Lifecycle
- Duplicate Payment Prevention و External Network Adapter
- جایگاه ISO 20022 در مرز تبادل و Anti-Corruption Layer، بدون تحمیل مستقیم مدل پیام بیرونی به Domain Model داخلی

**کد و تمرین**

- `PaymentOrder` برای انتقال بین‌شعبه‌ای
- Debit/Credit Idempotent در Deposits
- Branch/Inter-branch Accounting Facts
- تست گم‌شدن پاسخ، Reversal و Settlement دیرهنگام

**تحویل‌دادنی**

- پروندهٔ کامل Payments و Capability Cardهای Cards/Channels/Checks
- مرزبندی Payments و Deposits
- سناریوی نهایی شمارهٔ ۲ در وضعیت Beta

**Gate اسپرینت**

یک پروندهٔ تسهیلات معوق و یک انتقال بین‌شعبه‌ای دفاع می‌شوند. هر State، داده و تصمیم باید دقیقاً یک مالک داشته باشد و Channel نباید مالک مانده یا فرایند پرداخت شود.

---

## اسپرینت ۱۱ — Micro-frontend و Production Architecture

### هفتهٔ ۲۱: Micro-frontend Platform برای Widgetهای مستقل

**فنی**

- App Shell، Runtime Discovery و Widget Manifest
- Web Component Contract و Framework Isolation
- Independent Build/Version/Deployment
- Shared Design Tokens در برابر Shared Runtime State
- BFF، API Gateway، Auth Propagation و Feature Flag
- Failure Isolation و Compatibility Policy

**کد و تمرین**

- Portal Shell با Runtime Manifest
- `deposit-widget` و `lending-widget` با Build و Version مستقل
- بارگذاری تنبل، انتقال Context مجاز و جلوگیری از دسترسی مستقیم به State داخلی Widget دیگر
- ازکارانداختن عمدی یک Widget و اثبات سلامت Shell و Widget دیگر

**تحویل‌دادنی**

- Micro-frontend Architecture
- Widget Manifest Schema
- UI Ownership/Compatibility Matrix
- ADR-009: Web Components/Module Federation/سایر گزینه‌ها

**معیار قبولی**

- افزودن Widget جدید نیازمند Build مجدد همهٔ Widgetها نباشد.
- Contract و Design System مشترک باشد، ولی Business State مشترک و پنهان ایجاد نشود.

### هفتهٔ ۲۲: Runtime، SLO، DR و Service Ownership

**فنی**

- Container Image، Kubernetes Deployment/Service/Config/Secret
- Readiness/Liveness/Startup Probe، Resource Request/Limit و HPA
- CI/CD، Migration سازگار دیتابیس، Rolling/Blue-Green/Canary و Rollback Policy
- OpenTelemetry، Dashboard و Alert
- SLI/SLO/Error Budget
- Database HA، Backup/Restore، RTO/RPO، DR و Production Readiness Review
- Secret Management، Network Policy و Least Privilege

**سازمانی**

- Service Owner، Technical Owner، Product Owner و Run Owner
- تعهد مشترک PO و Engineering Lead؛ جلوگیری از جدایی اختیار تولید از تعهد محصول
- Build-and-Run Ownership و نقش Platform/SRE

**کد و تمرین**

- Manifestهای Kubernetes برای سرویس‌های اصلی
- Pipeline با Gateهای Build، Test، Contract Compatibility، Security Scan و Migration Check
- سه SLO اولیه: اعطا، انتقال وجه و ثبت حسابداری
- توقف یک Pod/Consumer و مشاهدهٔ Recovery و Backlog
- Restore آزمایشی دیتابیس/Projection در محیط Lab

**تحویل‌دادنی**

- Runtime Architecture
- NFR Catalog و SLO Document
- Backup/DR Plan و Runbook
- Service Ownership Map و Team Topology
- Production Readiness Checklist

**Gate اسپرینت**

- Secret در مخزن نباشد.
- Alert به SLI و اثر کاربر متصل باشد، نه فقط CPU.
- RTO/RPO فرضیهٔ کسب‌وکاریِ قابل تصویب معرفی شود، نه عدد تزئینی معماری.

---

## اسپرینت ۱۲ — یکپارچه‌سازی، مهاجرت و دفاع

### هفتهٔ ۲۳: اثبات سه سناریو و Migration Roadmap

**کار اصلی**

- اجرای End-to-End هر سه سناریو
- تکمیل Trace، Event Timeline، Journal، Reconciliation و Failure Evidence
- Contract Test میان سرویس‌ها
- Load/Failure Test نهایی
- طراحی مهاجرت تدریجی از وضع موجود با Strangler، Parallel Run، Data Migration و Cutover

**برای هر سناریو باید ثبت شود**

1. مالک هر تصمیم
2. مالک هر داده
3. Command، API و Eventها
4. Aggregate و Transaction Boundary
5. Ordering و Consistency
6. Duplicate و Out-of-order
7. Timeout، Retry و Failure State
8. Compensation/Reversal/Correction
9. Accounting Fact و Journal
10. Reconciliation و Manual Repair
11. SLO و Observability
12. تیم مالک و مسیر Escalation

**تحویل‌دادنی**

- Evidence Pack سه سناریو
- Migration Roadmap در موج‌های ۰ تا ۴
- Cutover/Reconciliation Checklist
- ADRهای نهایی

**معیار قبولی**

- هیچ Dual Write بدون الگوی کنترل و مغایرت‌گیری وجود نداشته باشد.
- Rollback مهاجرت و مالک تصمیم Go/No-Go روشن باشد.

### هفتهٔ ۲۴: دفاع نهایی معماری

**ساختار دفاع ۹۰ دقیقه‌ای**

- ۱۵ دقیقه: Capability، Domain و Context Map
- ۱۵ دقیقه: معماری کد و سرویس‌ها
- ۳۰ دقیقه: سه سناریو، هرکدام ۱۰ دقیقه
- ۱۵ دقیقه: داده، حسابداری، شکست و Reconciliation
- ۱۰ دقیقه: Runtime، SLO، Security، DR و Ownership
- ۵ دقیقه: Migration Roadmap و تصمیم‌های باز

**خروجی نهایی**

1. Banking Capability Map
2. Domain/Subdomain Map
3. Bounded Context Map
4. پرونده‌های ۱۲‌بخشی دامین‌ها
5. Data/Decision Ownership Matrix
6. Service Catalog
7. OpenAPI Catalog
8. AsyncAPI/Event Catalog
9. Accounting Fact/Rule Catalog
10. Logical/Physical Data Model
11. Saga/Failure/Compensation Matrix
12. Runtime/NFR/SLO/DR Architecture
13. ADR Log
14. Service/Team Ownership Map
15. Migration Roadmap
16. کد و تست سه Vertical Slice

**خروجی پس از دفاع**

- Gap List اولویت‌بندی‌شده
- برنامهٔ ۹۰ روزهٔ بعدی
- تصمیم دربارهٔ عمق بعدی: Architecture Leadership، Data/Performance، Platform/SRE یا Banking Domain Specialization

---

## ۱۰. مدل ارزیابی

| حوزه | امتیاز |
|---|---:|
| Capability، Domain Boundary و Ownership | ۲۰ |
| طراحی کد، Aggregate، Refactoring و Test | ۱۵ |
| API/Event Contract و Evolution | ۱۵ |
| Transaction، Consistency، Failure و Reconciliation | ۲۰ |
| Accounting، Data Model و Performance | ۱۵ |
| Security، Observability، SLO و DR | ۱۰ |
| ADR، Team Ownership و کیفیت دفاع | ۵ |
| **جمع** | **۱۰۰** |

### شرط عبور

- امتیاز کل حداقل ۷۵
- هیچ‌یک از چهار حوزهٔ Boundary، Financial Correctness، Failure Handling و Accounting کمتر از ۶۰٪ امتیاز خود نباشد.
- هر سه سناریوی نهایی واقعاً اجرا شوند؛ اسلاید یا Diagram به‌تنهایی کافی نیست.

### Gateهای رسمی

| Gate | پایان هفته | پرسش اصلی |
|---|---:|---|
| ۱ | ۴ | آیا Domain Model و مرز کد واقعاً مستقل و قابل آزمون است؟ |
| ۲ | ۸ | آیا مالکیت مانده، تراکنش و Read Model روشن و صحیح است؟ |
| ۳ | ۱۲ | آیا جریان توزیع‌شده بدون Global Transaction و فرض Exactly-once ایمن است؟ |
| ۴ | ۱۶ | آیا مدل حسابداری/داده تحت هم‌زمانی و بار، قابل دفاع است؟ |
| ۵ | ۲۰ | آیا مرز دامین‌های بانکی در سناریوهای واقعی حفظ شده است؟ |
| ۶ | ۲۴ | آیا معماری از Business Capability تا Runtime و Team Ownership کامل است؟ |

## ۱۱. قواعد جلوگیری از پراکندگی

- در طول دوره پروژهٔ دوم ایجاد نمی‌شود.
- Kubernetes پیش از هفتهٔ ۲۲ موضوع اصلی نمی‌شود.
- Kafka پیش از روشن‌شدن مالک و مرز Event در هفتهٔ ۹ وارد طراحی نمی‌شود.
- Microservice بدون ADR و شواهد استخراج نمی‌شود.
- BIAN، نام جدول و ساختار سازمانی جای Domain Discovery را نمی‌گیرند.
- برای نمایش معماری از Diagram بدون Ownership/Decision/Failure استفاده نمی‌شود.
- درصد Code Coverage هدف اصلی نیست؛ پوشش Invariant، Failure و Contract هدف است.
- ابزار جدید فقط وقتی اضافه می‌شود که یک خروجی اجباری برنامه را ممکن کند.
- کد تولیدی بانک در Lab کپی نمی‌شود؛ مسئله و قید آن با دادهٔ ساختگی بازآفرینی می‌شود.

## ۱۲. منابع رسمی حداقلی و ترتیب استفاده

این‌ها مرجع کنترل برنامه‌اند، نه فهرست کتاب‌هایی که باید کامل خوانده شوند.

- هفته‌های ۱ و ۲: [BIAN Service Landscape 14.0](https://bian.org/deliverables/service-landscape/)
- هفته‌های ۲ تا ۴: [Spring Modulith Fundamentals](https://docs.spring.io/spring-modulith/reference/fundamentals.html)، [Module Verification](https://docs.spring.io/spring-modulith/reference/verification.html) و [Module Integration Testing](https://docs.spring.io/spring-modulith/reference/testing.html)
- هفته‌های ۴ تا ۱۰: [Spring Boot Testcontainers](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html)
- هفتهٔ ۶: [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- هفتهٔ ۷: [PostgreSQL Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- هفته‌های ۹ و ۱۰: [AsyncAPI 3.1 Specification](https://www.asyncapi.com/docs/reference/specification/latest)، [Apache Kafka Design](https://kafka.apache.org/41/design/design/)، [Producer Configuration](https://kafka.apache.org/41/configuration/producer-configs/) و [Debezium Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
- هفتهٔ ۱۲: [OpenTelemetry Signals](https://opentelemetry.io/docs/concepts/signals/) و [Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- هفتهٔ ۱۵: [PostgreSQL Declarative Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html) و [Oracle Reference Partitioning](https://docs.oracle.com/en/database/oracle/oracle-database/26/vldbg/partition-admin.html)
- هفتهٔ ۲۱: [Webpack Module Federation Concepts](https://webpack.js.org/concepts/module-federation/) برای مقایسه با قرارداد Web Component/Manifest
- هفتهٔ ۲۲: [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)، [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)، [Google SRE: Implementing SLOs](https://sre.google/workbook/implementing-slos/) و [Example SLO Document](https://sre.google/workbook/slo-document/)

## ۱۳. ممیزی نهایی پوشش موارد جاافتادهٔ قبلی

| مورد جاافتاده | محل قطعی در نسخهٔ نهایی |
|---|---|
| SOLID و Patternهای کاربردی | هفته‌های ۳ و ۴؛ Refactoring مستمر در Definition of Done |
| Code Smell و Refactoring واقعی | هفتهٔ ۴ و Code Review هر هفته |
| Unit/Integration/Architecture/Contract Test | هفته‌های ۱ تا ۱۰ و سپس به‌صورت مستمر |
| Concurrency/Failure/Performance Test | هفته‌های ۷، ۱۲، ۱۶ و ۲۳ |
| PostgreSQL عملی | هفته‌های ۴، ۷، ۸، ۱۰، ۱۵ و ۱۶ |
| Oracle عمیق | هفته‌های ۷، ۱۵ و ۱۶ |
| CQRS کامل | هفته‌های ۸، ۱۰ و ۱۶ |
| Micro-frontend | هفتهٔ ۲۱ با Shell و دو Widget مستقل |
| IAM و API Security | هفتهٔ ۶؛ تکمیل در هفته‌های ۲۱ و ۲۲ |
| Observability | هفتهٔ ۱۲؛ Production Dashboard/SLO در هفتهٔ ۲۲ |
| Kubernetes و Runtime | هفتهٔ ۲۲ پس از آماده‌شدن نرم‌افزار |
| SLO، DR و Runbook | هفته‌های ۱۲، ۲۲ و ۲۳ |
| Team Topology و اختیار PO/Engineering | هفتهٔ ۲۲ و دفاع هفتهٔ ۲۴ |
| Migration از وضع موجود | هفتهٔ ۲۳ |

## ۱۴. پیش‌هفتهٔ شروع؛ خارج از ۲۴ هفته

این آماده‌سازی یک‌باره حداکثر دو ساعت زمان می‌برد:

1. نصب/کنترل Java 21، Maven، Docker و Git
2. ایجاد مخزن با ساختار پایه
3. اجرای `mvn verify`
4. اجرای PostgreSQL و Kafka با Docker/Testcontainers
5. ثبت پاسخ اولیهٔ خودت به سناریوی «اعطا و واریز به سپرده» بدون مطالعهٔ جدید
6. نمره‌گذاری خط پایه با Rubric نهایی

پاسخ خط پایه در هفتهٔ ۲۴ دوباره ارائه می‌شود تا رشد واقعی قابل مقایسه باشد.

## ۱۵. قرارداد اجرای برنامه در همین گفت‌وگو

### قالب گزارش هر هفته

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

Board دوره فقط این وضعیت‌ها را دارد: `Backlog → Ready → Doing → Review → Gate → Done`. در هر زمان فقط خروجی یک هفته در `Doing` است تا مطالعهٔ چند موضوع جای تکمیل Artifact را نگیرد.

در آغاز هر هفته:

1. درس فشرده و مسئلهٔ بانکی همان هفته ارائه می‌شود.
2. قالب خروجی و Acceptance Test مشخص می‌شود.
3. کد، Diagram، DDL یا تصمیم تو بررسی و نقد می‌شود.
4. خطاها و Failure Scenarioها روی خروجی اعمال می‌شوند.
5. فقط بعد از عبور از Definition of Done، هفته بسته می‌شود.

در Gateها، ضعف مهم با جلو رفتن صوری پوشانده نمی‌شود. همان بخش با تمرین کوچک‌تر تکرار می‌شود؛ اما نقشهٔ ۲۴ هفته‌ای تغییر مسیر نمی‌دهد مگر اینکه شواهد اجرای واقعی نشان دهد بار زمانی یا پیش‌نیاز فنی اشتباه برآورد شده است.

این سند نقشهٔ راه مرجع است. شروع واقعی از «پیش‌هفته» و سپس هفتهٔ ۱، Capability Map بانک، خواهد بود.
