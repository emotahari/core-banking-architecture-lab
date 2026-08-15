# Day 03 — Context Map و الگوهای رابطه

- Day budget: 50 minutes including exercise and exit ticket
- Output: Context Map relationships v0.1
- Banking case: اعطای تسهیلات و واریز به سپرده

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. Context Map را از System Diagram، Sequence Diagram و Data Flow جدا کنی.
2. Upstream و Downstream را بر اساس وابستگی مدل و قدرت تغییر تشخیص بدهی؛ نه جهت فراخوانی HTTP.
3. Customer/Supplier، Conformist، Anticorruption Layer و Open Host Service/Published Language را درست انتخاب کنی.
4. برای هر رابطه Contract، Translation، Owner و Failure Impact ثبت کنی.
5. توضیح بدهی چرا نوشتن `REST` یا `Kafka` Pattern رابطهٔ Contextها نیست.

## 2. چرا Context Map لازم است؟

مرزبندی Contextها فقط نیمی از Strategic Design است. هیچ Context مهم بانکی در خلأ کار نمی‌کند. Customer facts وارد Lending می‌شوند، Lending از Deposits واریز می‌خواهد، Payments وضعیت شبکه را نگه می‌دارد و Accounting Factهای کسب‌وکار را به Journal تبدیل می‌کند.

اگر فقط Boxها را بکشیم و آن‌ها را با خط وصل کنیم، پرسش‌های اصلی پنهان می‌مانند:

- مدل کدام طرف بر دیگری اثر می‌گذارد؟
- چه تیمی برای تغییر Contract قدرت بیشتری دارد؟
- Downstream مدل Upstream را می‌پذیرد یا ترجمه می‌کند؟
- Contract برای یک Consumer خاص طراحی شده یا عمومی و Published است؟
- شکست یا تغییر Upstream چه اثری روی Downstream دارد؟

Context Map نقشهٔ **روابط مدل و همکاری** میان Bounded Contextهاست.

## 3. Context Map چه چیزی نیست؟

| Diagram/Artifact | سؤال اصلی | چرا جای Context Map را نمی‌گیرد؟ |
|---|---|---|
| System Context Diagram | چه سیستم‌ها و Actorهایی درگیرند؟ | مدل، زبان و رابطهٔ قدرت را الزاماً نشان نمی‌دهد |
| Sequence Diagram | پیام‌ها با چه ترتیب زمانی ردوبدل می‌شوند؟ | Upstream/Downstream دامینی را از روی Caller نمی‌توان فهمید |
| Data Flow | چه داده‌ای حرکت می‌کند؟ | Authority و Translation Policy ممکن است پنهان بماند |
| Deployment Diagram | Process/Node/Pod کجاست؟ | Boundary مدل با Deployment یکی نیست |
| Organization Chart | تیم‌ها کجا هستند؟ | رابطهٔ تاریخی سازمان الزاماً رابطهٔ مدل نیست |

این Artifactها مکمل یکدیگرند. Context Map به‌طور خاص می‌گوید Contextها چگونه با تفاوت مدل و قدرت تغییر کنار می‌آیند.

## 4. Upstream و Downstream

### تعریف عملیاتی

`Upstream` طرفی است که مدل یا Contract ارائه‌شدهٔ آن روی طرف دیگر اثر می‌گذارد و معمولاً اختیار بیشتری بر تکامل آن دارد.

`Downstream` برای کارکرد خود به آن Capability، Fact یا Contract وابسته است و باید با تغییرات Upstream کنار بیاید.

### دام رایج: Caller برابر Upstream

فرض کن Lending فرمان `CreditDepositAccount` را به Deposits می‌فرستد. Lending Caller است، اما دربارهٔ قواعد حساب، پذیرش واریز و مانده اختیار ندارد. Deposits قابلیت و مدل عملیاتی را ارائه می‌کند و Lending به آن وابسته است؛ بنابراین در این رابطه، Deposits می‌تواند Upstream و Lending Downstream باشد.

در مقابل، ممکن است Deposit تیم Contract خود را با نیازهای Lending تنظیم کند. این شیوهٔ همکاری Customer/Supplier است و Lending به‌عنوان Downstream Customer روی Backlog Upstream اثر می‌گذارد.

جهت Event نیز به‌تنهایی جهت مدل را ثابت نمی‌کند. Contextی که Event منتشر می‌کند معمولاً Fact خودش را منتشر می‌کند، اما Governance و Pattern باید جدا تحلیل شوند.

## 5. Pattern اول: Customer/Supplier

### معنا

دو تیم رابطهٔ Upstream/Downstream دارند و Upstream متعهد می‌شود نیازهای واقعی Downstream را در برنامه‌ریزی و Contract لحاظ کند. Downstream مشتری مدل/خدمت است، نه صرفاً مصرف‌کننده‌ای بی‌قدرت.

### چه زمانی مناسب است؟

- تیم‌ها امکان مذاکره و برنامه‌ریزی مشترک دارند.
- نیاز Downstream برای Outcome مهم است.
- Upstream می‌تواند Contract هدفمند ارائه کند.
- رابطه و SLA مالک روشن دارد.

### مثال بانکی

Party & Customer، اطلاعات هویتی معتبر را ارائه می‌کند و Lending برای تصمیم اعتباری به یک Customer Reference نیاز دارد. اگر تیم Customer نیازهای Versioning، KYC evidence و Bulk/latency موردنیاز Lending را در Product Backlog لحاظ کند، رابطه می‌تواند Customer/Supplier باشد.

### خطا

نوشتن C/S روی Diagram بدون مکانیزم Governance، Owner، Compatibility و مسیر Escalation فقط برچسب است.

## 6. Pattern دوم: Conformist

### معنا

Downstream مدل Upstream را همان‌گونه که هست می‌پذیرد و مدل مستقل یا Translation قابل‌توجهی نمی‌سازد.

### چه زمانی قابل دفاع است؟

- Downstream قدرت یا امکان تغییر Upstream را ندارد.
- مدل Upstream برای مسئلهٔ Downstream به‌اندازهٔ کافی مناسب است.
- هزینهٔ Translation از ارزش مدل مستقل بیشتر است.
- این بخش برای Downstream Core نیست یا خطر آلودگی مدل پایین است.

### مثال محتمل

یک ابزار گزارش‌گیری ساده ممکن است Classification و Codeهای رسمی Accounting را بدون مدل مستقل بپذیرد. اگر فقط نمایش می‌دهد و تصمیم دامینی متفاوتی ندارد، Conformist می‌تواند اقتصادی باشد.

### خطر

اگر Lending مدل Customer Legacy را با صدها Flag تاریخی وارد Domain Model خود کند، زبان و تصمیم اعتباری به Upstream آلوده می‌شود. کم‌شدن Mapper لزوماً کاهش Coupling نیست.

Conformist «Pattern بد» نیست؛ انتخابی آگاهانه با Trade-off است. برای Core Subdomain باید با احتیاط بیشتری استفاده شود.

## 7. Pattern سوم: Anticorruption Layer

### معنا

Downstream یک لایهٔ ترجمه می‌سازد تا مدل Upstream وارد مدل داخلی آن نشود. ACL می‌تواند شامل Adapter، Translator، Facade و Contract-specific Model باشد.

### هدف

هدف ACL صرفاً تبدیل JSON یا Rename فیلد نیست. باید **معنا** را ترجمه و مدل Downstream را محافظت کند.

### مثال بانکی: Legacy Deposits

فرض کن سامانهٔ قدیمی سپرده پاسخ زیر را می‌دهد:

~~~text
statusCode=17, accType=203, usableAmt=..., block1=..., block2=...
~~~

Lending نباید این Codeها و ساختار Legacy را در Ruleهای اعطا منتشر کند. ACL می‌تواند آن را به مدل محدود زیر ترجمه کند:

~~~text
DisbursementAccountAssessment
- accountId
- acceptsLoanDisbursement
- rejectionReason
- assessedAt
- sourceVersion
~~~

ACL مالک Available Balance نمی‌شود. فقط معنای موردنیاز Downstream را از Contract Upstream ترجمه می‌کند و Provenance را نگه می‌دارد.

### چه زمانی لازم است؟

- Upstream Legacy یا مدل نامتناسب دارد.
- Downstream Core است و باید مدلش محافظت شود.
- دو Context اصطلاح یا Invariant متفاوت دارند.
- تغییر Upstream نباید در مدل Downstream موج ایجاد کند.

### هزینه

- کد و تست ترجمه
- Mapping خطا و Version
- Risk از دست‌رفتن معنا
- Monitoring و Reconciliation

ACL را برای هر DTO کوچک نساز. باید خطری واقعی برای مدل وجود داشته باشد.

## 8. Pattern چهارم: Open Host Service و Published Language

### Open Host Service

Upstream مجموعه‌ای مشخص و پایدار از خدمات/Protocol را برای چند مصرف‌کننده عرضه می‌کند، به‌جای ساخت Integration اختصاصی و متفاوت برای هرکدام.

### Published Language

زبان Contract مستند، Versioned و قابل‌مصرفی است که دو یا چند Context برای تبادل از آن استفاده می‌کنند؛ مانند Schema یک Business Event یا Semantic API.

Published Language مدل داخلی Upstream یا یک Canonical Model برای کل بانک نیست. باید فقط معنای لازم در Boundary را منتقل کند.

### مثال بانکی

Deposits می‌تواند Contract عمومی عملیات سپرده را با Command/Resultهای مشخص عرضه کند و Eventهای Versioned مانند `DepositCredited` منتشر کند. Accounting، Notification و Reconciliation ممکن است از Published Language رخداد استفاده کنند، ولی هرکدام آن را به مدل خود ترجمه می‌کنند.

### کنترل‌های لازم

- Semantic naming
- Schema/contract version
- Compatibility policy
- Error taxonomy
- Idempotency/correlation semantics در صورت نیاز
- Owner و deprecation path

وجود OpenAPI یا AsyncAPI به‌تنهایی Published Language خوب نمی‌سازد؛ Contract باید معنای دامینی پایدار داشته باشد.

## 9. Patternهای مکمل

تمرکز آزمون روی چهار Pattern بالاست، ولی Context Map واقعی ممکن است این‌ها را هم نیاز داشته باشد.

### Partnership

دو Context/Team موفقیت مشترک و وابستگی متقابل قوی دارند و تغییرها را هماهنگ می‌کنند. این Pattern Coordination Cost بالایی دارد و استقلال Release را کاهش می‌دهد؛ باید آگاهانه باشد.

### Shared Kernel

بخش بسیار کوچک و صریحی از مدل/کد بین Contextها مشترک است و هر تغییر با هماهنگی انجام می‌شود. Shared Kernel نباید به `common` عظیم، Entityهای JPA مشترک یا Database مشترک تبدیل شود.

### Separate Ways

ارزش Integration کمتر از هزینه و Coupling است؛ Contextها مستقل می‌مانند، حتی اگر مقداری Duplication وجود داشته باشد.

## 10. مثال هدایت‌شده: اعطای تسهیلات

سناریو: پس از انعقاد قرارداد مرابحه، Lending مبلغ را به سپردهٔ مشتری واریز می‌کند و آثار مالی باید ثبت شوند.

### رابطهٔ Product Catalog → Lending

- Upstream: Product/Agreement reference provider
- Downstream: Lending
- Fact: ProductVersion و شروط لازم
- نکته: Lending برای قرارداد منعقدشده به Snapshot مؤثر نیاز دارد، نه Query دائمی نسخهٔ جاری.
- Pattern candidate: OHS/Published Language یا Customer/Supplier، بسته به Governance

### رابطهٔ Party & Customer → Lending

- Upstream: Party & Customer
- Downstream: Lending
- Fact: Party identity و KYC evidence
- Decision distinction: KYC validity با Credit Eligibility یکی نیست.
- Pattern candidate: Customer/Supplier + Published Language

### رابطهٔ Deposits → Lending

- Upstream model authority: Deposits برای عملیات واریز/حساب
- Downstream: Lending که Outcome اعطا به واریز وابسته است
- Command direction: Lending → Deposits
- Result/Event direction: Deposits → Lending/consumers
- Pattern candidate: Customer/Supplier اگر Contract با نیاز اعطا طراحی شود؛ ACL اگر مدل Legacy Deposits نامتناسب باشد.

### رابطهٔ Lending → Accounting

- Upstream fact producer: Lending برای Factهای خودش
- Downstream: Accounting برای ترجمهٔ Fact به Journal
- Accounting نباید State داخلی Loan را مالک شود.
- Pattern candidate: OHS/Published Language در Boundary رخداد + ACL/Translator داخل Accounting

نکته: ممکن است برای یک Pair چند Contract با Patternهای متفاوت وجود داشته باشد. آن‌ها را در یک خط مبهم ادغام نکن.

## 11. انتخاب Pattern با پنج سؤال

برای هر رابطه بپرس:

1. چه کسی Authority مدل/Fact است؟
2. کدام طرف از تغییر دیگری آسیب می‌بیند؟
3. Downstream چقدر قدرت اثرگذاری بر Roadmap Upstream دارد؟
4. مدل Upstream برای مسئلهٔ Downstream مناسب است یا باید ترجمه شود؟
5. Contract یک Consumer خاص دارد یا باید برای چند مصرف‌کننده Published باشد؟

سپس Pattern، Owner قرارداد، Translation location و Failure impact را ثبت کن.

## 12. خطاهای رایج

### `REST` یا `Kafka` به‌عنوان Pattern

این‌ها Transport/Technology هستند. C/S، ACL و Conformist دربارهٔ رابطهٔ مدل و تیم‌اند و می‌توانند روی HTTP یا Messaging اجرا شوند.

### فلش بدون جهت معنایی

فلش باید بگوید Upstream/Downstream چیست. Call direction را جداگانه در Sequence Diagram نشان بده.

### ACL در Upstream

ACL معمولاً از مدل Downstream محافظت می‌کند و تحت کنترل Downstream است. اگر Translator را Upstream تحمیل کند، ممکن است باز هم مدل Upstream غالب بماند.

### Published Language برابر Shared Entity

Published Contract باید Boundary DTO/Event باشد؛ Entity داخلی و Schema دیتابیس نیست.

### Conformist بدون ثبت Risk

پذیرفتن مدل Upstream ممکن است اقتصادی باشد، اما Coupling و محدودیت تکامل باید ثبت شود.

### یک رابطهٔ دوطرفهٔ مبهم

اگر Payments از Deposits Debit می‌خواهد و Deposits رخداد به Payments می‌دهد، Intent، Fact و Authority را جدا تحلیل کن؛ یک فلش دوسر اطلاعات کافی ندارد.

## 13. تمرین هدایت‌شده

رابطهٔ `Legacy Customer → New Lending` را در یک ردیف کامل کن:

| Upstream | Downstream | Pattern | Contract | Translation | Failure impact |
|---|---|---|---|---|---|
| Legacy Customer | New Lending | ؟ | ؟ | ؟ | ؟ |

سپس یک Alternative Pattern بنویس و توضیح بده چه Forceای انتخاب را تغییر می‌دهد.

## 14. تمرین مستقل

[Day 03 Exercise — Context Map](../exercises/day-03-context-map.md) را انجام بده. حداقل شش رابطه بنویس و برای هرکدام Pattern را با Forces دفاع کن.

## 15. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تشخیص درست Upstream/Downstream | ۲ |
| انتخاب Pattern با استدلال | ۳ |
| Contract و Translation روشن | ۲ |
| Authority و Failure impact | ۲ |
| ثبت Alternative/Open Question | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. خط بدون Pattern و Contract امتیاز ندارد.

## 16. آزمون خروج

درس را ببند و [Day 03 Exit Ticket](../quizzes/day-03-exit-ticket.md) را پاسخ بده.

## 17. منبع اصلی

- [Domain-Driven Design Reference — Context Mapping Patterns](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

Patternها از مرجع Eric Evans گرفته شده‌اند؛ انتخاب هر Pattern در مثال بانکی یک Design Hypothesis وابسته به رابطهٔ واقعی تیم‌ها و Contractهاست.
