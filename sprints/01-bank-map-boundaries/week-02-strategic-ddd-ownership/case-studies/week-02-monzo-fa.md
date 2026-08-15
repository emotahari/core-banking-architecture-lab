# پروندهٔ Week 02 — Monzo؛ از Mondo تا بانک ۳۰۰۰+ Microservice

- Case type: بانک دیجیتال با Core Banking داخلی؛ نه محصول Core Banking قابل خرید
- Relevance: Strategic DDD، Ownership، Team autonomy، Platform engineering و هزینهٔ مرزهای بسیار ریز
- Evidence checked: 15 August 2026
- Reading/analysis budget: 45 minutes
- Evidence rule: Factهای جاری از منابع رسمی Monzo یا FCA؛ Domain map این پرونده یک Inference تحلیلی است.

## 1. چرا Monzo برای Week 02؟

Monzo نمونهٔ سادهٔ «Cloud خوب، Mainframe بد» نیست. داستان آن تضادهای مهم‌تری دارد:

- با سه Backend developer، از روز اول Microservice-first شد.
- برای استقلال تیم‌ها و استقرار مستقل طراحی کرد، اما بعدها باید بیش از ۳۰۰۰ Service را استاندارد، مهاجرت و کنترل می‌کرد.
- معماری بسیار مدرن مانع عقب‌ماندن کنترل‌های Financial Crime از رشد نشد.
- برای تحمل خرابی کامل Cloud، یک Stand-in مستقل و کوچک در Cloud دوم ساخت.
- در بریتانیا به رشد و سودآوری بزرگ رسید، ولی تجربهٔ آمریکا را در ۲۰۲۶ بست.

این پرونده دقیقاً پرسش Week 02 را زنده می‌کند: **چه کسی مالک تصمیم است، مرزها چگونه اجرا می‌شوند و چه چیزی با زیادکردن Service حل نمی‌شود؟**

## 2. یک سوءبرداشت مهم

Monzo را نباید با Temenos Transact، FLEXCUBE، Finacle یا Mambu یکی گرفت. آن شرکت‌ها Platform/Core Banking را به مؤسسات مختلف عرضه می‌کنند؛ Monzo یک بانک است که بخش بزرگی از Banking platform خود را برای عملیات خودش ساخته است.

بنابراین:

- تعداد Microserviceهای Monzo الگوی مستقیم برای بانک دیگر نیست.
- نام Serviceهای Monzo معادل Bounded Contextهای ما نیست.
- موفقیت محصول، درستی تک‌تک Boundaryها را ثابت نمی‌کند.
- شکست Compliance نیز ثابت نمی‌کند Microservices علت آن بوده‌اند.

## 3. تولد: مسئله قبل از فناوری

Monzo در فوریهٔ ۲۰۱۵ با نام **Mondo** شروع شد. ایده فقط ساخت یک Mobile app روی Core قدیمی نبود؛ بنیان‌گذاران می‌خواستند بانک جدیدی بسازند که تجربهٔ مالی آن Real-time، شفاف و قابل کنترل از موبایل باشد. در مرحلهٔ Alpha/Beta از Prepaid card استفاده شد تا پیش از آماده‌شدن Full current account، محصول با مشتری واقعی آزموده شود.

تا اوت ۲۰۱۶ حدود ۳۰ هزار Prepaid card در گردش بود و بیش از ۲۰۰ هزار نفر برای مشارکت در مسیر محصول ثبت‌نام کرده بودند. همان ماه بانک مجوز محدود گرفت و وارد Mobilisation شد؛ مجوز محدود به آن اجازه می‌داد اتصال به Payment network و کنترل‌های عملیاتی را پیش از Launch عمومی آزمایش کند. [اعلام رسمی مجوز محدود و آغاز از فوریهٔ ۲۰۱۵](https://monzo.com/blog/2016/08/11/we-are-now-a-bank)، [توضیح Mobilisation و اتصال به Mastercard، Bacs و Faster Payments](https://monzo.com/blog/2016/08/15/launching-the-bank)

### اولین خطای پرهزینه اما قابل بازیابی: نام

Trademark نام Mondo با چالش حقوقی یک شرکت دیگر روبه‌رو شد. تیم به‌جای دعوای طولانی، Rebrand را انتخاب کرد و پس از دریافت بیش از ۱۲٬۵۰۰ پیشنهاد از جامعه، نام Monzo را برگزید. این خطا معماری نرم‌افزار نبود، اما یک درس معماری سازمانی دارد: **دارایی حیاتی فقط Code و Data نیست؛ Name، License، Contract و Regulatory permission نیز Dependency واقعی‌اند.** [شرح رسمی دلیل تغییر نام](https://monzo.com/blog/2016/08/26/how-we-picked-monzo)، [اعلام نام Monzo](https://monzo.com/blog/2016/08/25/monzo)

## 4. Timeline تحول

| دوره | رخداد مستند | تغییر مسئله و Capability |
|---|---|---|
| 2015 | شروع Mondo و ساخت Prepaid beta | آزمون Product/UX و Card processing پیش از بانک کامل |
| 2016 | مجوز بانکی محدود، Mobilisation و تغییر نام به Monzo | ورود جدی Risk، Compliance، Bacs، Faster Payments و Mastercard |
| Apr 2017 | رفع محدودیت‌های مجوز و تبدیل به بانک کاملاً مجاز | مسئولیت کامل Current Account و Deposit-taking؛ [اعلام رسمی](https://monzo.com/blog/2017/04/05/banking-licence) |
| Jul–Dec 2017 | Rollout تدریجی Current Account و Migration از Prepaid | Account lifecycle، Direct Debit، Standing Order، Overdraft و Migration؛ [برنامهٔ Rollout](https://monzo.com/blog/2017/07/17/current-account-preview) |
| 2018–2019 | عبور از یک میلیون مشتری، Joint account، Apple Pay، Savings partnership و Lending؛ شروع Business Banking | عبور از «کارت خوب» به بانک چندمحصولی؛ [مرور رسمی 2019](https://monzo.com/blog/2019/01/04/monzo-in-2019) |
| 2019 | Launch در آمریکا با Partner bank | آزمون Market/Regulatory model متفاوت؛ [گزارش رسمی 2019](https://monzo.com/blog/2019/06/27/monzo-2019-annual-report) |
| 2020–2022 | رشد بسیار سریع Customer و Product؛ ضعف جدی Financial Crime controls | کنترل‌های Onboarding، Risk assessment و Transaction monitoring از رشد عقب ماندند |
| 2022–2024 | Direct participation در Bacs، International Payments، Investments و رشد Business Banking | افزایش عمق Payment، Wealth و Business capabilities |
| 2024 | حدود ۲۸۰۰ تا ۳۰۰۰ Microservice؛ Migrationهای سراسری و Rate limiting توزیع‌شده | Platform consistency و Mass change به مسئلهٔ معماری درجه‌اول تبدیل شد |
| 2025 | معرفی Monzo Stand-in و جریمهٔ FCA | Cloud-level resilience رشد کرد؛ در مقابل Debt کنترل مالی رسمی شد |
| 2026 | Migration بیش از ۳۰۰۰ Service به EKS، Launch در Ireland و بستن حساب‌های آمریکا | Platform productization، تمرکز جغرافیایی جدید و خروج از آزمایش آمریکا |

Timeline بالا گزیده است؛ هدف اتصال تحول Capability به تحول معماری است، نه فهرست همهٔ Featureها.

## 5. معماری نسل اول: Microservice از روز اول

Monzo در ۲۰۱۶ نوشت Backend از ابتدا مجموعه‌ای از Microserviceهای توزیع‌شده بوده است؛ انتخابی غیرعادی برای Startup. استدلال اصلی، 24×7 بودن، Fault isolation، استقرار سریع و استقلال تیم‌های آینده بود. در شروع فقط سه Backend developer داشتند، اما هنگام Beta تعداد Serviceها نزدیک ۱۰۰ و سپس حدود ۱۵۰ شده بود. [شرح معماری اولیه توسط Head of Engineering](https://monzo.com/blog/2016/09/19/building-a-modern-bank-backend)

Technology/architecture اعلام‌شده در آن زمان:

- Go به‌عنوان زبان غالب Serviceها
- Containerization با Docker
- مهاجرت از Mesos/Marathon به Kubernetes روی AWS
- RPC برای ارتباط همگام و Linkerd/Finagle در نسل اولیه
- Kafka به‌عنوان Commit log/Message backbone با At-least-once delivery و Replay
- سرویس‌های کوچک برای Shared platform capabilities

### تصمیم درست یا Premature decomposition؟

از دادهٔ عمومی نمی‌توان حکم قطعی داد. این انتخاب دو اثر واقعی داشت:

**سودها**

- تیم‌ها می‌توانستند Build/Deploy/Scale مستقل‌تری داشته باشند.
- Failure isolation و Continuous delivery از ابتدا Design concern شد.
- Event و Replay برای عملیات بانکی بخشی از Platform بود، نه افزونهٔ دیرهنگام.

**هزینه‌ها**

- با تیم کوچک، تعداد Serviceها بسیار سریع بالا رفت.
- RPC، Queue، Service discovery، Deployment، Observability و Migration سراسری باید خیلی زود حل می‌شد.
- مرز کوچک Deployment الزاماً مرز دامینی خوب نیست و می‌تواند Cognitive load را زیاد کند.

نتیجه برای Lab ما «از روز اول Microservice بساز» نیست. نتیجه این است که اگر استقلال Deploy را زود انتخاب می‌کنی، باید هزینهٔ Platform و عملیات آن را نیز از روز اول بپردازی.

## 6. معماری در مقیاس: استانداردسازی برای مهار توزیع

تا ۲۰۲۴ Monzo از ۲۸۰۰ تا بیش از ۳۰۰۰ Microservice حرف می‌زد. نکتهٔ مهم این نیست که عدد بزرگ تحسین شود؛ مهم این است که چنین عددی چه Governanceای طلب می‌کند.

در پروندهٔ Migration از OpenTracing به OpenTelemetry، Monzo چند قابلیت کلیدی را اعلام کرد:

- همهٔ Serviceهای مورد بحث با Go و Technology version سازگار ساخته شده‌اند.
- کد Serviceها در یک Monorepo است.
- CI با ابزارهایی مانند Semgrep Conventionها را سراسری enforce می‌کند.
- Mass deployment و Automated rollback وجود دارد.
- Config service امکان Roll-forward تدریجی و Rollback سریع را می‌دهد.
- Migration بزرگ به‌صورت مرکزی هدایت می‌شود، زیرا واگذاری کامل به Ownerهای پراکنده قبلاً Migrationهای نیمه‌تمام و Coordination cost ایجاد کرده بود. [شرح Migration در ۲۸۰۰ Microservice](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)

این یک Trade-off جالب Ownership است:

```text
product behavior ownership       → decentralized squads
cross-cutting platform migration → centrally driven platform team
```

Ownership همیشه به معنی «هر تیم هر کاری خواست» نیست. استاندارد مشترک و تغییر سراسری نیز Owner لازم دارد.

## 7. معماری جاریِ قابل اثبات در ۲۰۲۶

جدول زیر فقط مواردی را قطعی می‌داند که در منابع رسمی ۲۰۲۴ تا ۲۰۲۶ آمده‌اند:

| حوزه | آنچه عمومی و قابل اثبات است | سطح اطمینان |
|---|---|---|
| Service architecture | بیش از ۳۰۰۰ Microservice؛ Backendها در Monorepo و Common patterns | FACT — primary |
| Application language | نوشتهٔ Migration ۲۰۲۴ می‌گوید Serviceهای آن‌ها با Go نوشته شده‌اند | FACT — primary، scope همان Backend fleet |
| Container platform | Kubernetes؛ Workloadها از Self-hosted Kubernetes به Amazon EKS مهاجرت کرده‌اند | FACT — primary |
| Primary cloud | Primary Platform روی AWS | FACT — primary |
| Stand-in cloud | Stand-in مستقل روی GCP با حدود ۱۸ Service | FACT — primary |
| Async/event | Kafka در Platform اصلی؛ GCP Pub/Sub برای Adviceهای Stand-in | FACT — primary |
| Platform interface | Platform operationها پشت Service/APIهای opinionated، با Multi-party authorization برای عملیات حساس | FACT — primary |
| Observability/migration | Central metrics/logging، OpenTelemetry migration، automated health checks و rollback | FACT — primary |
| Analytics | BigQuery + dbt؛ بیش از سه میلیارد Analytics event در روز در گزارش ۲۰۲۴ | FACT — primary |
| Primary operational datastore | نام فعلی در منابع بررسی‌شده اعلام نشده؛ مقالهٔ ۲۰۲۴ فقط از Migration پایگاه Core حرف می‌زند | UNKNOWN |
| Historic datastore | Cassandra در منابع قدیمی Monzo و آگهی‌های فنی آمده است، اما این پرونده آن را Database قطعی ۲۰۲۶ اعلام نمی‌کند | HISTORIC FACT / CURRENT UNKNOWN |
| Exact Bounded Context map | عمومی نشده است | UNKNOWN |

منابع: [Platform engineering و Migration بیش از ۳۰۰۰ Service به EKS در ۲۰۲۶](https://monzo.com/blog/the-engineering-behind-the-platform)، [Scale و Migration در ۲۰۲۴](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)، [Data platform و سه میلیارد Event روزانه](https://monzo.com/blog/how-we-use-incremental-modelling-to-handle-billions-of-events-every-day)

## 8. Monzo Stand-in: تاب‌آوری با استقلال، نه Clone کامل

یکی از مهم‌ترین دستاوردهای معماری Monzo، **Stand-in** است. Primary Platform روی AWS حدود ۳۰۰۰ Microservice دارد؛ Stand-in روی GCP فقط ۱۸ Service مستقل دارد و برای خرابی بزرگ، Capabilityهای حیاتی زیر را نگه می‌دارد:

- Card spend و Cash withdrawal
- Bank transferهای اصلی
- مشاهدهٔ Balance و Transaction
- Freeze/Unfreeze card

Stand-in کپی کامل Primary نیست. Software، Serviceها و Cloud جدا هستند تا یک Bug یا Process failure مشترک هر دو را هم‌زمان از کار نیندازد. داده از Primary به Stand-in به‌صورت Non-blocking و Eventually consistent می‌رود. Stand-in هنگام فعال‌بودن Decisionهای خودش را می‌گیرد و نتیجه را به شکل Advice durable برای Primary ثبت می‌کند؛ Primary پس از بازیابی، این Effects را اعمال و با Correlation ID تطبیق می‌دهد. Primary همچنان System of Record باقی می‌ماند. [شرح کامل Stand-in توسط Monzo](https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in)

### Trade-off آگاهانه

Monzo صریحاً می‌پذیرد که Stand-in ممکن است با View کمی قدیمی، پرداختی را تأیید کند که Primary آن را Insufficient funds می‌داند؛ نتیجه می‌تواند Unapproved overdraft باشد. این ریسک با Control و Reconciliation مدیریت می‌شود، نه با ادعای Consistency کامل.

درس معماری:

> Availability بالا همیشه حاصل Replication کامل نیست؛ گاهی حاصل کاهش Scope، استقلال Failure mode و پذیرش آگاهانهٔ Consistency محدود است.

## 9. Domain/Capability map تحلیلی

Monzo نقشهٔ رسمی Bounded Contextهای خود را عمومی نکرده است. جدول زیر از Productها، گزارش مالی و نوشته‌های فنی **استنتاج** شده و نباید به‌عنوان ساختار داخلی قطعی بازنشر شود.

| Capability cluster | شواهد عمومی | فرضیهٔ Ownership |
|---|---|---|
| Party, Customer & Onboarding | Account signup، KYC و FCA findings | هویت، Eligibility و Customer risk باید Authority روشن داشته باشد |
| Accounts & Deposits | Current account، Joint، Under-16، Pots و £25.7bn deposits در FY2026 | Operational account state و available balance در Banking platform |
| Cards & Cash | Mastercard، ATM، freeze/unfreeze و Stand-in card processor | Card lifecycle و Authorization جدا از Channel UI |
| Payments | Faster Payments، Bacs، Direct Debit، SWIFT/International payments | Payment instruction، processing state، scheme adapter و reconciliation |
| Ledger & Balance | Stand-in مقاله صریحاً از Ledger و System of Record حرف می‌زند | Primary Ledger Authority؛ Stand-in decision/effect موقت و reconciled |
| Borrowing | Loan، Overdraft و Flex | Credit decision، agreement و servicing با Lifecycle مستقل |
| Savings & Wealth | Savings، ISA، Investments و Pensions | Product/partner orchestration و customer holdings |
| Business Banking | Business current account، invoicing و expense cards | Party/business relationship و entitlements چندکاربره |
| Financial Crime & Fraud | Customer risk assessment، transaction monitoring، fraud controls | Policy/decision ownership باید همگام با Product growth مقیاس بگیرد |
| Customer Operations | Support و Ops Agent | Case/operation workflows بدون تصاحب Source of Truth دامین‌ها |
| Platform & Reliability | Kubernetes، EKS، deployment، MPA، Stand-in | Internal platform product با API و Owner مستقل |
| Data & Analytics | BigQuery، dbt و event ingestion | Analytical projection؛ نه مالک Operational facts |

نکتهٔ Week 02: وجود ۳۰۰۰ Service به معنی ۳۰۰۰ Domain نیست. بسیاری Platform service، Adapter، Workflow step یا Technical capability هستند.

## 10. اشتباه‌ها و شرط‌بندی‌های ناموفق

### 10.1 Financial Crime controls از رشد عقب ماند

FCA در ژوئیهٔ ۲۰۲۵ Monzo را ۲۱٬۰۹۱٬۳۰۰ پوند جریمه کرد. تخلف‌های اعلام‌شده شامل ناکافی‌بودن سیستم‌ها و کنترل‌های Financial Crime بین اکتبر ۲۰۱۸ تا اوت ۲۰۲۰ و نقض مکرر محدودیت Onboarding مشتریان High-risk بین اوت ۲۰۲۰ تا ژوئن ۲۰۲۲ بود. FCA گفت Customer base از حدود ۶۰۰ هزار در ۲۰۱۸ به بیش از ۵.۸ میلیون در ۲۰۲۲ رسید، اما کنترل‌ها هم‌پای رشد نکردند؛ بیش از ۳۴ هزار High-risk customer برخلاف Requirement ثبت شدند. Monzo پس از Review مستقل، Change programme مربوط را تکمیل کرد. [اعلام و جزئیات رسمی FCA](https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls)

این Failure را نباید به «Bug یک Microservice» تقلیل داد. حداقل چهار مالکیت باید هم‌راستا می‌بود:

- Product growth و Onboarding flow
- Customer risk policy
- Transaction monitoring capability
- Regulatory control، evidence و change governance

درس: **Compliance یک Non-functional afterthought نیست؛ مجموعه‌ای از Capability، Decision owner، Data quality، Control loop و Evidence است.**

### 10.2 Microservice scale خودش مسئله ساخت

Monzo در ۲۰۲۴ صریحاً نوشت معماری ۲۸۰۰ Service ارزش زیادی داده، اما Migration سراسری را دشوار کرده است. تجربهٔ Decentralized migration نیز به کار نیمه‌تمام و Coordination زیاد منجر شده بود؛ برای همین Standardization، Monorepo، central tooling و centrally driven migration تقویت شد. [منبع رسمی Migration](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)

این «اثبات شکست Microservices» نیست؛ اثبات این است که استقلال زیاد بدون Platform governance پایدار نمی‌ماند.

### 10.3 آزمایش آمریکا پایان یافت

Monzo در ۲۰۱۹ با Partner bank وارد آمریکا شد، اما از ۸ ژوئن ۲۰۲۶ همهٔ حساب‌های آمریکا بسته شدند و شرکت تمرکز خود را بر UK و Europe گذاشت. Monzo در صفحهٔ رسمی Closure دلیل فنی یا شکست معماری واحدی اعلام نمی‌کند؛ بنابراین پرونده نیز علت‌سازی نمی‌کند. Fact قطعی، پایان Product/market experiment است. [اطلاعیهٔ رسمی بستن حساب‌های آمریکا](https://monzo.com/help/us-account-closure-support/us-account-closure-support)

درس: Technology reuse به‌تنهایی Product-market fit، Regulation، Payment rails و Unit economics بازار جدید را حل نمی‌کند.

### 10.4 Self-hosted Kubernetes تا EKS

در ۲۰۱۶ اجرای Highly available Kubernetes روی AWS را دشوار اما ارزشمند توصیف کردند. در ۲۰۲۶ اعلام شد بیش از ۳۰۰۰ Service از Self-hosted Kubernetes به EKS مهاجرت کرده‌اند. این را نباید بدون شواهد «اشتباه اولیه» نامید؛ در ۲۰۱۶ Managed option امروز وجود نداشت. این یک نمونهٔ Revisit architecture decision با تغییر Technology landscape است.

## 11. دستاوردهای تازه تا FY2026

### Business/Product

گزارش سال مالی ۲۰۲۶ Monzo ارقام زیر را منتشر کرده است:

- درآمد ۱.۷ میلیارد پوند
- Adjusted profit before tax برابر ۱۷۲.۶ میلیون پوند
- سپردهٔ مشتریان ۲۵.۷ میلیارد پوند
- ۱۵.۲ میلیون مشتری و ۱۰.۴ میلیون Monthly active user
- ۷۳ میلیارد پوند Card spend
- رشد ۴۵ درصدی Business banking customers
- Launch در Ireland

[Monzo FY2026 Annual Report summary](https://monzo.com/annual-report)

### Technology/Architecture

- Stand-in مستقل روی GCP برای Critical banking capabilities
- Migration خودکار بیش از ۳۰۰۰ Microservice به EKS، همراه با Health check و Rollback؛ حتی Migrator service خودش را مهاجرت کرد
- Platform operationها به‌صورت API/Service با Multi-party authorization، به‌جای Runbook و Script دستی
- Standardized Go/Monorepo estate برای Migrationهای سراسری و کنترل Convention

این دستاوردها نشان می‌دهند Platform engineering در بانک فقط «زیرساخت» نیست؛ یک Product داخلی با API، User، Ownership، Test و Control است.

## 12. ارزیابی معماری

### نقاط قوت

1. **Boundary اجرایی واقعی:** Serviceها Build/Deploy/Scale مستقل دارند.
2. **Platform as product:** عملیات حساس پشت API و Approval قرار گرفته است.
3. **Change at scale:** Monorepo و Standard stack امکان Refactor سراسری می‌دهند.
4. **Event-driven durability:** Replay، At-least-once و Advice log از ابتدا/در تاب‌آوری مهم‌اند.
5. **Failure diversity:** Stand-in همان Software را در Cloud دوم کپی نمی‌کند.
6. **Transparency:** بسیاری از Trade-offها و محدودیت‌ها عمومی نوشته شده‌اند.

### هزینه‌ها و ریسک‌ها

1. ۳۰۰۰ Service نیازمند Platform team و Automation در سطح بسیار بالا هستند.
2. Deployment boundaryهای ریز می‌توانند Runtime coupling و Cognitive load بسازند.
3. Consistency و Authority در Stand-in نیازمند Advice، Correlation و Reconciliation دقیق است.
4. Technology excellence جای Financial Crime control و Regulatory ownership را نمی‌گیرد.
5. Standardization برای Migration سراسری، بخشی از آزادی تکنولوژیک تیم‌ها را محدود می‌کند.

## 13. چه چیزی را برای Core Banking Lab خودمان می‌گیریم؟

### می‌گیریم

- هر Module/Context API آشکار و Internal implementation محافظت‌شده داشته باشد.
- Product team autonomy همراه Platform standards و Architecture fitness test باشد.
- Event delivery با Duplicate و Replay طراحی شود، نه Happy path.
- Analytical data را با Operational Source of Truth اشتباه نگیریم.
- Compliance/Fraud را Capability و Owner واقعی بدانیم.
- برای Critical flow، Minimal viable continuity را از Full duplicate جدا کنیم.
- تصمیم‌های Technology با Revisit trigger تاریخ‌دار باشند.

### فعلاً نمی‌گیریم

- Microservice از روز اول
- Database/Queue برای هر Package
- سه‌هزار Deployable component
- Multi-cloud قبل از داشتن SLO و Failure model
- Eventual consistency برای Ledger اصلی
- تقلید Stack بدون Team/Scale/Regulatory context

تصمیم Lab همچنان درست است: ابتدا Modular Monolith، سپس استخراج فقط با Evidence.

## 14. پنج سؤال دفاعی

1. چرا ۳۰۰۰ Microservice را نمی‌توان معادل ۳۰۰۰ Bounded Context دانست؟
2. Monorepo و Migration مرکزی چگونه با Team autonomy جمع می‌شوند؟
3. در Stand-in، Owner نهایی Balance و Ledger کیست و Stand-in چه چیزی را موقتاً Authority می‌گیرد؟
4. شکست Financial Crime بیشتر شکست Technology بود، Ownership بود یا Governance؟ با شواهد دفاع کن.
5. اگر Monzo را برای بانک بزرگ خودت الگو بگیری، کدام تصمیم را Copy نمی‌کنی و چرا؟

## 15. Artifact چهل‌وپنج‌دقیقه‌ای

[Day 09 Architecture Review](../exercises/day-09-monzo-architecture-review.md) را کامل کن. خروجی باید یک صفحه باشد و شامل این سه بخش:

1. یک Timeline پنج‌نقطه‌ای
2. یک جدول `Fact / Inference / Unknown`
3. یک ADR-lite: «آیا Core Banking Lab باید Microservice-first شود؟»

## 16. Source register

### تاریخ و محصول

- [We Are Now a Bank — 2016](https://monzo.com/blog/2016/08/11/we-are-now-a-bank)
- [Launching the Bank — Mobilisation](https://monzo.com/blog/2016/08/15/launching-the-bank)
- [Welcome to Monzo Bank — unrestricted licence, 2017](https://monzo.com/blog/2017/04/05/banking-licence)
- [Monzo in 2019](https://monzo.com/blog/2019/01/04/monzo-in-2019)
- [FY2026 Annual Report](https://monzo.com/annual-report)
- [US account closure — 2026](https://monzo.com/help/us-account-closure-support/us-account-closure-support)

### فناوری و معماری

- [Building a Modern Bank Backend — 2016](https://monzo.com/blog/2016/09/19/building-a-modern-bank-backend)
- [How we run migrations across 2,800 microservices — 2024](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)
- [Tolerating full cloud outages with Monzo Stand-in — 2025](https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in)
- [The Engineering Behind the Platform — 2026](https://monzo.com/blog/the-engineering-behind-the-platform)
- [Incremental modelling and billions of events — 2024](https://monzo.com/blog/how-we-use-incremental-modelling-to-handle-billions-of-events-every-day)

### شکست و کنترل

- [FCA fine and findings — 2025](https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls)

## 17. محدودیت پرونده

- Source code، Service catalog، Data model و Context map کامل Monzo عمومی نیست.
- عدد Serviceها در زمان‌های مختلف ۲۸۰۰، نزدیک ۳۰۰۰ و بیش از ۳۰۰۰ گزارش شده؛ این تفاوت Timeline رشد است، نه تناقضی که باید با یک عدد ثابت پنهان شود.
- Product list را نباید Bounded Context list فرض کرد.
- Current primary database technology در منابع رسمی بررسی‌شده نام‌گذاری نشده است.
- تحلیل‌های «چرا آمریکا موفق نشد» بدون منبع رسمی در این پرونده عمداً حذف شده‌اند.
