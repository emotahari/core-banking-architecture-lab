# Day 05 — Banking Capability Map و استفادهٔ درست از BIAN 14

- Day budget: 70 minutes — 25 lesson + 20 map + 20 BIAN gap check + 5 exit ticket
- Output: Capability Map v1 سطح L1 و BIAN Gap Check
- Source date: 15 August 2026

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. Capability Map سطح L1 بانک را مستقل از چارت و Application Portfolio بسازی.
2. چهار لایهٔ «هسته»، «عملیات و خدمات»، «سازمانی» و «اکوسیستم دیجیتال» را به‌عنوان Portfolio lens استفاده کنی، نه Boundary قطعی.
3. L1 را فقط در نقاط لازم به L2 بشکنی و Levelها را مخلوط نکنی.
4. BIAN 14 را برای Vocabulary، Coverage و Gap Check استفاده کنی.
5. Service Domain، Business Capability، Control Record، API و Microservice را یکی نگیری.

## 2. Capability Map چیست؟

Capability Map نمای سلسله‌مراتبی و نسبتاً پایدار از توانایی‌های سازمان است. Map خوب به سه پرسش کمک می‌کند:

- برای تحقق Strategy چه توانایی‌هایی لازم داریم؟
- کدام Capability ضعیف، تکراری، پرریسک یا بی‌مالک است؟
- Applicationها، داده‌ها، تیم‌ها و Investmentها روی کدام Capabilityها قرار می‌گیرند؟

Capability Map پاسخ مستقیم این پرسش‌ها نیست:

- چند Microservice بسازیم؟
- مرز تراکنش کجاست؟
- کدام جدول به کدام Schema برود؟
- کدام تیم دقیقاً چند نفر داشته باشد؟

این تصمیم‌ها Evidenceهای دیگری می‌خواهند.

## 3. قواعد Leveling

### L1

توانایی کلان و پایدار بانک؛ برای Portfolio و Heatmap. تعداد معمولاً محدود است و همهٔ بانک را پوشش می‌دهد.

نمونه: `مدیریت رابطه با مشتری`، `مدیریت منابع و سپرده‌ها`، `مدیریت اعتبار`، `اجرای پرداخت`.

### L2

تفکیک معنادار درون L1 بر اساس Outcome/Rule/Owner.

```text
مدیریت منابع و سپرده‌ها
├── طراحی و عرضهٔ محصول سپرده
├── ایجاد و نگهداری قرارداد سپرده
├── کنترل مانده و دسترسی به وجوه
├── محاسبه و اعمال سود
└── خاتمه و شکست قرارداد
```

### L3

توانایی دقیق‌تر برای تحلیل Investment و Process، بدون سقوط به Activity یا API.

مثلاً زیر «کنترل دسترسی به وجوه»: مدیریت Hold، کنترل حدود برداشت، مدیریت وضعیت حساب.

### خطای Level mixing

اگر کنار «مدیریت اعتبار» مورد «چاپ دفترچه» قرار گیرد، Map L1 و Activity را مخلوط کرده است. هر ردیف خواهر باید تقریباً در یک سطح از Granularity باشد.

## 4. روش ساخت Map از صفر

### گام 1 — Scope و Stakeholder

Scope این هفته «بانک جامع» و مخاطب Business/Architecture Portfolio است. نسخه 1.0 هنوز تصمیم اجرایی نیست.

### گام 2 — Outcomeهای اصلی

تعهدهای بانک را از دید مشتری، رگولاتور، سهام‌دار و عملیات فهرست کن:

- شناخت طرف و رابطه
- طراحی و اجرای قرارداد مالی
- نگهداری وجوه و تعهدات
- اعطای اعتبار و وصول
- انتقال و تسویه
- ثبت و کنترل مالی
- مدیریت ریسک و انطباق
- ادارهٔ سازمان و اکوسیستم

### گام 3 — نام‌گذاری مستقل از وضع موجود

نام سامانه، Vendor، شعبه، Mobile، Mainframe، Oracle و Kafka حذف شود. اگر با حذف فناوری مفهوم از بین رفت، احتمالاً Capability نیست.

### گام 4 — Level و هم‌پوشانی

برای هر Capability، Definition و `Includes/Excludes` بنویس. دو نام مشابه بدون Definition به سرعت هم‌پوشان می‌شوند.

### گام 5 — Owner و KPI اولیه

Owner فعلی ممکن است مبهم باشد؛ `Proposed owner` و `Ownership gap` را جدا ثبت کن. KPI باید Outcome را بسنجد، نه فقط تعداد تراکنش.

### گام 6 — Heatmap اختیاری

پس از تثبیت Map می‌توان Strategy importance، maturity، risk و change demand را Overlay کرد. رنگ زیبا جای Definition و Evidence را نمی‌گیرد.

## 5. چهار لایهٔ Portfolio این دوره

| لایه | پرسش | نمونه‌ها |
|---|---|---|
| هستهٔ بانکداری | چه چیزی رابطه، قرارداد، مانده و تعهد اصلی بانک/مشتری را نگه می‌دارد؟ | Customer، Product/Agreement، Deposits، Lending، Accounting core facts |
| عملیات و خدمات بانکداری | خدمت و اجرای عملیات چگونه به شبکه، شعبه و بازار متصل می‌شود؟ | Payments، Cards، Checks، Teller، Cash، Collections، Treasury |
| توانمندی‌های سازمانی | خود بنگاه چگونه اداره می‌شود؟ | HR، Procurement، Budget، Asset/Fleet، Portfolio governance |
| اکوسیستم دیجیتال | بانک چگونه با Partner و کانال بیرونی ترکیب می‌شود؟ | Open Banking، API partnership، Marketplace، Embedded Finance |

این تقسیم‌بندی برای اولویت و Portfolio مفید است؛ هیچ ردیف آن Bounded Context یا Deployable boundary را ثابت نمی‌کند. Payments ممکن است برای یک بانک Near Core و برای بانک پرداخت‌محور بخشی از Differentiating Core باشد.

## 6. Draft سطح L1

Working Draft موجود چهار شاخه دارد. امروز باید آن را نقد، Definitionها را تکمیل و به نسخهٔ 1.0 تبدیل کنی:

```text
Bank Capabilities
├── Core Banking
│   ├── Party & Customer Relationship
│   ├── Product, Pricing & Agreement
│   ├── Funds & Deposit Obligations
│   ├── Credit & Financing Obligations
│   └── Financial Control & Accounting
├── Banking Operations & Services
│   ├── Payments, Clearing & Settlement
│   ├── Treasury, Markets & Securities
│   ├── Branch, Teller & Cash
│   ├── Collections & Recovery
│   └── Risk, Compliance & Supervision
├── Enterprise Capabilities
│   ├── Governance & Portfolio
│   ├── Data, Reporting & Decision Support
│   ├── People, Procurement & Assets
│   └── Security & Access Management
└── Digital Ecosystem
    ├── Open Banking & API Partnership
    ├── Partner/Fintech Management
    └── Marketplace & Embedded Finance
```

این Map پاسخ نهایی صنعت نیست؛ فرضیهٔ دوره است و با Domain Dossierهای هفته‌های بعد اصلاح می‌شود.

## 7. BIAN چیست و چه چیزی نیست؟

BIAN یک انجمن و Reference Architecture برای صنعت بانکداری است که Service Landscape، Business Capabilityها، Service Domainها، الگوهای رفتاری و Semantic APIها را ارائه می‌کند. ارزش اصلی برای این هفته:

- واژگان استاندارد برای گفت‌وگو
- Coverage check و یافتن Capabilityهای جاافتاده
- مقایسهٔ Scope و مسئولیت
- سرنخ برای Contract و Semantic alignment

BIAN این‌ها نیست:

- نقشهٔ محرمانهٔ بانک تو
- چارت سازمانی
- فهرست Microserviceهای آمادهٔ استقرار
- جایگزین Event Storming و تحلیل Rule/Ownership
- نسخهٔ قطعی Data ownership یا Transaction boundary محلی

## 8. اعداد نسخهٔ 14 و معنای درست آن‌ها

طبق Release Notes نسخهٔ 14، BIAN مجموعه‌ای بزرگ از Service Domain، Business Domain، Business Capability و Semantic API دارد. اعداد مرجع ثبت‌شده برای این دوره عبارت‌اند از ۳۲۲ Service Domain، ۳۸ Business Domain، ۵۸۶ Business Capability و ۲۴۲ Semantic API.

این اعداد دلیل ساخت صدها سرویس نیستند. اندازهٔ Landscape نشان‌دهندهٔ Coverage مرجع است، نه Topology Runtime بانک. هر Fact نسخه‌ای باید با [Release Notes](../references/README.md) کنترل شود.

## 9. Service Domain چرا Microservice نیست؟

Service Domain یک Partion منطقی استاندارد از Function/Behavior بانکی در مدل BIAN است. برای تبدیل آن به Deployable Service هنوز باید پاسخ دهیم:

- آیا مدل و زبان محلی واقعاً یک Boundary مستقل می‌سازند؟
- Aggregate و Transaction boundary چیست؟
- Change cadence و Team ownership مستقل است؟
- Scaling و Availability profile متفاوت است؟
- هزینهٔ Network، Consistency و Operations توجیه دارد؟
- Contractهای لازم و Failure semantics روشن‌اند؟

تا وقتی این Forces بررسی نشده‌اند، Service Domain فقط Reference candidate است.

## 10. روش درست Gap Check

### مرحله A — Map خودمان اول

بر اساس Strategy، محصولات، مقررات و مسئله‌های واقعی Map را بساز. از Landscape شروع نکن؛ وگرنه Map به ترجمهٔ فهرست Vendor تبدیل می‌شود.

### مرحله B — Search و Mapping

برای هر Capability محلی در BIAN جست‌وجو کن و یکی از این وضعیت‌ها را بده:

- `MATCH`: Scope نزدیک و واژگان مفید
- `PARTIAL`: بخشی از Scope مشترک است
- `GAP-LOCAL`: نیاز محلی در BIAN مستقیم پیدا نشد
- `GAP-OUR-MAP`: BIAN موردی نشان داد که در Map ما جا افتاده بود
- `FALSE-FRIEND`: نام شبیه ولی معنا/Scope متفاوت
- `NOT-APPLICABLE`: در Scope بانک/نسخهٔ ما لازم نیست

### مرحله C — Evidence، نه Copy

نام BIAN، Definition کوتاه، تفاوت Scope و تصمیم محلی را ثبت کن. Match به معنی پذیرش خودکار نیست.

### مرحله D — Change log

هر تغییر Map باید Reason داشته باشد: «افزودن Fraud Management پس از Gap Check» معتبرتر از «مطابق BIAN شد» است.

## 11. سه نمونهٔ Gap Check

### Current Account

ممکن است نام با محصول جاری محلی شبیه باشد، اما باید Scope Service Domain، Control Record و Behavior Qualifierها بررسی شوند. نتیجه می‌تواند `PARTIAL` باشد، نه Copy مستقیم.

### Customer Relationship Management

CRM Application موجود ممکن است Sales/Lead را انجام دهد، در حالی که Capability رابطه و وضعیت Customer گسترده‌تر یا متفاوت است. نام مشترک False Friend محتمل است.

### Financial Accounting

وجود Service Domain حسابداری به معنی مالکیت ماندهٔ قابل برداشت سپرده نیست. BIAN mapping، نوع Balance و Authority محلی را تعیین نمی‌کند.

## 12. آزمون کیفیت Capability Map v1

برای هر Node بررسی کن:

1. Outcome و Definition دارد؟
2. نام Technology/Org/Application ندارد؟
3. در Level مناسب کنار خواهرهایش است؟
4. Includes/Excludes هم‌پوشانی را کنترل می‌کند؟
5. Owner پیشنهادی و Gap مالکیت ثبت شده؟
6. BIAN status و Evidence دارد؟
7. از Node به Context یا Microservice پرش نشده؟

## 13. تمرین مستقل و Rubric

[Day 05 Exercise](../exercises/day-05-capability-map-bian-gap-check.md) را انجام بده و [Gap Check Template](../artifacts/bian-gap-check-template.md) را کامل کن.

| معیار | امتیاز |
|---|---:|
| L1 کامل و هم‌سطح | ۲ |
| Definition و Includes/Excludes | ۲ |
| چهارلایه با توضیح غیرقطعی | ۱ |
| حداقل ۱۰ Mapping مستند BIAN | ۲ |
| تشخیص Gap/Partial/False Friend | ۲ |
| عدم تبدیل Service Domain به Microservice | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰.

## 14. آزمون خروج و منابع

درس را ببند و [Exit Ticket](../quizzes/day-05-exit-ticket.md) را پاسخ بده.

- [BIAN Service Landscape](https://bian.org/deliverables/service-landscape/)
- [BIAN 14 Architecture Portal](https://bian.org/servicelandscape-14-0-0/)
- [References Week 01](../references/README.md)

اعداد و نام‌های نسخه‌ای با تاریخ کنترل می‌شوند؛ Domain Map و چهارلایهٔ این درس `INFERENCE/LOCAL DECISION` هستند.

