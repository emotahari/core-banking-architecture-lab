# Day 01 — زبان مشترک معماری: از توانمندی بانک تا Contract

- زمان مطالعه: ۲۵ دقیقه
- سطح: میانی رو به پیشرفته
- مسئلهٔ نمونه: مسدودی قضایی سپرده
- خروجی: توانایی تشخیص سطح هر تصمیم و ساخت Traceability Chain

> اگر تمرین خط پایه را هنوز انجام نداده‌ای، این فایل را ببند. ابتدا ۱۲ دقیقه به
> [Architecture Baseline](../exercises/day-01-baseline.md) پاسخ بده. هدف ثبت مدل ذهنی واقعی تو پیش از آموزش است.

## ۱. امروز دقیقاً چه چیزی باید یاد بگیری؟

در پایان روز باید بتوانی:

1. Business Architecture، Solution Architecture و Software Architecture را از هم جدا کنی.
2. Capability را با Process، Business Service، Application و API اشتباه نگیری.
3. تفاوت System، Domain، Subdomain، Bounded Context، Module و Deployable Service را توضیح بدهی.
4. از یک نیاز بانکی این زنجیره را بسازی:

~~~text
Capability
→ Domain / Subdomain
→ Bounded Context
→ Module / Service Candidate
→ Use Case
→ Command / Query
→ API / Event
~~~

5. توضیح بدهی چرا این زنجیره «نگاشت یک‌به‌یک» نیست.
6. BIAN را به‌عنوان Reference Architecture به‌کار ببری، نه دستگاه تولید خودکار Microservice.

موضوع امروز انتخاب Kafka، دیتابیس، REST یا معماری Microservice نیست. اگر پیش از روشن‌شدن Capability و Ownership سراغ این انتخاب‌ها برویم، ممکن است پاسخ فنی خوبی برای مسئلهٔ اشتباه بسازیم.

---

## ۲. معماری در این دوره یعنی چه؟

برای این دوره، معماری را این‌طور عملیاتی تعریف می‌کنیم:

**معماری مجموعه‌ای از تصمیم‌های قابل دفاع دربارهٔ مرزها، مالکیت، وابستگی‌ها، قواعد حیاتی و ویژگی‌های کیفی است که امکان تغییر ایمن سیستم را تعیین می‌کند.**

این تعریف پنج جزء دارد:

| جزء | سؤال |
|---|---|
| مرز | چه چیزی داخل این جزء است و چه چیزی بیرون آن؟ |
| مالکیت | چه کسی مجاز است این داده یا تصمیم را ایجاد و تغییر دهد؟ |
| وابستگی | این جزء برای کارکردن چه دانشی از دیگری دارد؟ |
| قواعد حیاتی | چه Invariantهایی حتی هنگام خطا و هم‌زمانی نباید شکسته شوند؟ |
| تغییر ایمن | تغییر در یک قاعده تا کجا موج ایجاد می‌کند؟ |

Diagram، Framework، Cloud و Microservice می‌توانند ابزار یا نتیجهٔ تصمیم معماری باشند؛ خود معماری نیستند. دو تیم ممکن است Diagram مشابه داشته باشند، ولی یکی مالکیت دادهٔ روشن و Contract پایدار داشته باشد و دیگری از دیتابیس مشترک، دانش پنهان و Release هماهنگ رنج ببرد. ظاهر آن‌ها یکی است، معماری آن‌ها نه.

### سه نشانهٔ یک تصمیم معماری

یک تصمیم معمولاً معماری است اگر دست‌کم یکی از این ویژگی‌ها را داشته باشد:

- تغییرش پرهزینه، پرریسک یا سازمان‌گستر است.
- چند جزء یا تیم باید آن را رعایت کنند.
- روی صحت مالی، امنیت، دسترس‌پذیری یا امکان تحول اثر جدی دارد.

نام‌گذاری یک متغیر معمولاً تصمیم معماری نیست. اینکه ماندهٔ قابل برداشت سپرده را Deposits مالک باشد یا Accounting، تصمیم معماری و دامینی است؛ چون روی تراکنش، Locking، API، عملیات و پاسخ‌گویی سازمانی اثر می‌گذارد.

---

## ۳. سه سطحی که نباید در یک Diagram مخلوط شوند

### ۳.۱ Business Architecture

Business Architecture توضیح می‌دهد بانک برای تحقق راهبردش **چه توانمندی‌هایی** لازم دارد، چگونه ارزش تولید می‌کند و اطلاعات و مسئولیت‌های کلیدی چگونه سازمان می‌یابند.

واحدهای معمول تحلیل:

- Goal و Outcome
- Capability و Capability Map
- Value Stream
- Business Information
- Stakeholder و Responsibility

نمونه پرسش‌ها:

- بانک برای اعطای اعتبار چه توانمندی‌هایی لازم دارد؟
- کدام Capability برای بانک راهبردی و کدام عمومی است؟
- مالک بلوغ «مدیریت سپرده» چه نقشی است؟
- کدام Capabilityها مانع عرضهٔ سریع محصول جدیدند؟

Business Architecture نباید به نسخهٔ Spring Boot، نام جدول یا تعداد Podها پاسخ بدهد.

### ۳.۲ Solution Architecture

Solution Architecture برای یک مسئله یا تغییر مشخص، همکاری چند Domain، Application، Data Store و Integration را طراحی می‌کند.

واحدهای معمول تحلیل:

- System/Context Boundary
- Component یا Service Candidate
- Data Flow و Contract
- Quality Attribute
- Integration، Security و Deployment Constraint

نمونه پرسش‌ها:

- فرایند اعطای تسهیلات چگونه با Deposits و Accounting همکاری می‌کند؟
- پاسخ گم‌شده پس از واریز موفق چگونه مدیریت می‌شود؟
- مرز تراکنش محلی کجاست؟
- چه داده‌ای Snapshot و چه داده‌ای Reference است؟

Solution Architecture پل میان مسئلهٔ کسب‌وکار و چند سیستم درگیر است.

### ۳.۳ Software Architecture

Software Architecture ساختار درونی یک نرم‌افزار یا سرویس را تعیین می‌کند.

واحدهای معمول تحلیل:

- Package و Module
- Layer، Port و Adapter
- Aggregate و Repository
- Interface و Dependency Rule
- Thread، Transaction و Runtime Component

نمونه پرسش‌ها:

- Domain Model به Spring یا JPA وابسته است؟
- Use Case اعطای تسهیلات در Application Layer چگونه اجرا می‌شود؟
- چه Packageهایی Public API ماژول‌اند و چه Packageهایی Internal؟
- Invariant قرارداد تسهیلات کجا آزمون می‌شود؟

### جدول کنترل

| گزاره | سطح غالب |
|---|---|
| بانک باید توانایی مدیریت مسدودی وجوه را داشته باشد. | Business Architecture |
| Legal Orders و Deposits با Contract مشخص همکاری می‌کنند. | Solution Architecture |
| کلاس DepositAccount فقط از متد placeHold تغییر می‌کند. | Software Architecture |
| نرخ خطای عملیات مسدودی باید کمتر از حد مصوب باشد. | Solution/Runtime Architecture |
| واحد حقوقی زیرمجموعهٔ کدام معاونت باشد؟ | Operating Model / Organization Design |

Enterprise Architecture چتر بزرگ‌تری است که Business، Data، Application و Technology Architecture را در سطح بنگاه هم‌راستا می‌کند. در این دوره به‌اندازه‌ای از آن استفاده می‌کنیم که تصمیم نرم‌افزاری از Portfolio، Capability و Operating Model جدا نیفتد.

---

## ۴. Capability؛ نقطهٔ شروع پایدار

### تعریف عملیاتی

Business Capability یعنی **توان سازمان برای انجام یک کار کسب‌وکاری و تولید یک Outcome**.

Capability می‌گوید «چه کاری باید بتوانیم انجام دهیم؟» و عمداً دربارهٔ اینکه کدام واحد، فرایند، نرم‌افزار یا فناوری آن را انجام می‌دهد سکوت می‌کند.

نمونه‌های مناسب:

- مدیریت رابطه با مشتری
- مدیریت محصولات و شرایط
- نگهداری سپرده
- مدیریت اعتبار و تسهیلات
- جابه‌جایی و تسویهٔ وجوه
- ثبت و کنترل مالی
- پایش تقلب

نمونه‌های نامناسب:

- اجرای فرایند افتتاح حساب در BPM
- سامانهٔ سپرده
- تیم تسهیلات یک
- API واریز
- Kafka Event Processing

موارد نامناسب یا Process هستند، یا Application/Organization/Technology. ممکن است همگی برای تحقق Capability لازم باشند، ولی خود Capability نیستند.

### Capability در برابر Process

فرض کن بانک Capability «مدیریت مسدودی وجوه» را دارد.

این Capability ممکن است با Processهای مختلف اجرا شود:

- مسدودی قضایی با دریافت نامه و تأیید حقوقی
- مسدودی وثیقه‌ای هنگام اعطای تسهیلات
- Hold کوتاه‌مدت هنگام پرداخت کارت
- مسدودی سیستمی به‌دلیل کنترل تقلب

Capability نسبتاً پایدار است؛ Process با مقررات، کانال و اتوماسیون تغییر می‌کند.

### Capability در برابر Business Service

Capability توان داخلی بانک است. Business Service شکل ارزش قابل‌مصرفی است که از آن توان ارائه می‌شود.

مثلاً:

- Capability: مدیریت پرداخت
- Business Service: انتقال وجه داخلی برای مشتری

یک Capability می‌تواند چند Business Service عرضه کند و یک Business Service ممکن است به چند Capability وابسته باشد.

### Capability در برابر Application

ممکن است امروز سه سامانه بخشی از «مدیریت مشتری» را انجام دهند و فردا در یک Platform ادغام شوند. Capability باقی است، Application Landscape تغییر می‌کند.

اگر Capability Map را از روی فهرست سامانه‌ها بسازیم، وضع موجود را با ماهیت کسب‌وکار اشتباه گرفته‌ایم و Legacy را به مدل هدف تحمیل کرده‌ایم.

### آزمون شش‌گانهٔ Capability

برای هر عنوان پیشنهادی بپرس:

1. آیا می‌گوید بانک چه کاری می‌تواند انجام دهد؟
2. آیا مستقل از فناوری و Vendor است؟
3. آیا مستقل از چارت سازمانی است؟
4. آیا از Processهای اجرای آن پایدارتر است؟
5. آیا Outcome یا KPI برای آن قابل تصور است؟
6. آیا می‌توان Owner کسب‌وکاری برای بلوغ آن تعیین کرد؟

پاسخ منفی به چند سؤال نشانهٔ آن است که عنوان احتمالاً Capability نیست.

---

## ۵. از Problem Space تا Solution Space

بزرگ‌ترین خطای معماری سازمانی این است که عناصر سطوح مختلف را هم‌معنا فرض کنیم. برای جلوگیری از آن، هر مفهوم را دقیق در جای خود می‌گذاریم.

### System

System مجموعه‌ای از اجزای مرتبط با یک هدف و Boundary مشخص است. تعریف System به «System of Interest» وابسته است.

- کل بانک می‌تواند یک System باشد.
- Core Banking Platform می‌تواند System باشد.
- سرویس Deposits نیز در یک بررسی محدود می‌تواند System باشد.

پس «System» به‌تنهایی اندازه یا نوع معماری را تعیین نمی‌کند؛ Boundary بررسی را مشخص می‌کند.

### Domain

Domain حوزهٔ مسئله، دانش و فعالیتی است که می‌خواهیم برایش مدل بسازیم؛ مانند Lending یا Payments.

Domain به مسئله تعلق دارد، نه به Repository کد. ممکن است امروز هیچ سامانهٔ مناسبی برای Domain وجود نداشته باشد، ولی Domain همچنان واقعی است.

### Subdomain

Domain بزرگ به Subdomainهای متمایز شکسته می‌شود. Lending می‌تواند شامل بخش‌هایی مانند:

- Loan Origination
- Credit Decision
- Loan Servicing
- Repayment
- Delinquency Management

باشد. مرز دقیق برای هر بانک با مدل کسب‌وکار، مقررات و تمایز راهبردی آن تعیین می‌شود؛ فهرست آماده جای Discovery را نمی‌گیرد.

### Bounded Context

Bounded Context مرزی است که درون آن یک Model و Ubiquitous Language مشخص معتبر است.

واژهٔ Account مثال مهمی است:

- در Deposits: قرارداد نگهداری وجوه و ماندهٔ عملیاتی
- در Lending: موقعیت بدهی و برنامهٔ بازپرداخت
- در Accounting: حساب دفتر کل یا معین
- در IAM: حساب کاربری

اگر همهٔ این معناها را در یک مدل مشترک Account ادغام کنیم، مدل مبهم و تغییرها کاپل می‌شوند. Bounded Context اجازه می‌دهد هر معنا در مرز خودش دقیق بماند و ترجمه در Contract رخ دهد.

### Module

Module واحد منطقی کد با:

- API آشکار
- جزئیات Internal
- مسئولیت منسجم
- Dependency کنترل‌شده

است. Module می‌تواند همراه چند Module دیگر در یک Process و یک Deployment اجرا شود.

### Deployable Service

Deployable Service واحد Runtime قابل استقرار است. وقتی آن را Microservice می‌نامیم، معمولاً انتظار داریم:

- Lifecycle استقرار مستقل داشته باشد.
- Boundary مسئولیت روشن باشد.
- داده و تغییرات Schema تحت مالکیت آن باشد.
- خرابی و عملیات مستقل مدیریت شود.
- هزینهٔ Network، Observability و Consistency توزیع‌شده پذیرفته شود.

هر Module خوب Microservice نیست. ابتدا Module خوب می‌سازیم؛ فقط اگر محرک‌های کسب‌وکاری و عملیاتی کافی وجود داشتند، استخراج فیزیکی را بررسی می‌کنیم.

### API و Event

API و Event شکل Contract در Boundary هستند، نه جایگزین Boundary.

- Command قصد انجام تغییر دارد: PlaceLegalHold
- Query اطلاعات می‌خواهد: GetAvailableBalance
- Event وقوع Fact را اعلام می‌کند: LegalHoldPlaced

نام Event باید رخداد گذشته را بگوید. LoanGrantRequest یک درخواست است، نه Event. LoanGranted یک Fact رخ‌داده است.

---

## ۶. زنجیرهٔ Capability تا Contract

این زنجیره ابزار Traceability است:

~~~text
چرا این جزء وجود دارد؟
      ↑
Capability
→ Domain/Subdomain
→ Bounded Context
→ Module/Service Candidate
→ Use Case
→ Command/Query
→ API/Event
      ↓
چگونه قابلیت در نرم‌افزار قابل استفاده می‌شود؟
~~~

برای هر پله سؤال مشخصی داریم:

| پله | سؤال اصلی | خطای رایج |
|---|---|---|
| Capability | بانک چه کاری باید بتواند انجام دهد؟ | نام‌گذاری با سامانه یا واحد |
| Domain/Subdomain | این دانش و قواعد متعلق به کدام Problem Space است؟ | شروع از جدول |
| Bounded Context | این مدل و واژه‌ها در کدام مرز معتبرند؟ | مدل مشترک عظیم |
| Module/Service Candidate | کدام واحد منطقی تغییر و مسئولیت را محصور می‌کند؟ | Microservice پیش‌فرض |
| Use Case | چه قصد یا Outcome مشخصی اجرا می‌شود؟ | CRUD به‌جای رفتار |
| Command/Query | مصرف‌کننده چه قصدی را بیان می‌کند؟ | نام فنی و مبهم |
| API/Event | Contract بیرونی چگونه معنا، خطا و Version را منتقل می‌کند؟ | افشای Entity و Schema داخلی |

### این نگاشت یک‌به‌یک نیست

قواعد مهم:

- یک Capability می‌تواند به چند Domain وابسته باشد.
- یک Domain می‌تواند چند Subdomain و چند Bounded Context داشته باشد.
- یک Bounded Context می‌تواند ابتدا یک Module باشد و بعداً یک یا چند Deployable Service شود.
- یک Service می‌تواند چند Use Case عرضه کند.
- یک Use Case می‌تواند یک Command ورودی و چند Event خروجی داشته باشد.
- یک API می‌تواند بخشی از چند جریان کسب‌وکاری باشد.

هدف زنجیره این نیست که برای هر Capability یک Microservice بسازیم. هدف این است که هر جزء نرم‌افزاری دلیل کسب‌وکاری و مالکیت قابل ردیابی داشته باشد.

---

## ۷. مثال هدایت‌شده: مسدودی قضایی سپرده

برای آلوده‌نکردن تمرین خط پایه، مثال درس را از سناریوی دیگری می‌گیریم.

### صورت مسئله

بانک یک حکم معتبر دریافت می‌کند که باید مبلغ معینی از سپردهٔ مشتری مسدود شود. وضعیت حکم ممکن است بعداً لغو یا اصلاح شود. ماندهٔ قابل برداشت باید بلافاصله اثر Hold را نشان دهد.

### گام اول: Capability

حداقل دو Capability قابل تشخیص است:

1. مدیریت دستورهای حقوقی/نظارتی
2. مدیریت محدودیت و Hold وجوه سپرده

«سامانه نامه‌های قضایی» Capability نیست؛ نام راه‌حل یا Application است.

### گام دوم: Domain/Subdomain

- Legal/Compliance: اعتبار، مرجع، دامنه و چرخهٔ عمر حکم
- Deposits: اعمال و رفع Hold و محاسبهٔ ماندهٔ قابل برداشت

ممکن است Customer/Party برای تطبیق هویت مشارکت کند، ولی مالک حکم یا Hold نمی‌شود.

### گام سوم: Bounded Context

- Legal Orders Context
- Deposit Accounts Context

واژهٔ Restriction در Context حقوقی به الزام قانونی اشاره دارد؛ Hold در Deposits یک وضعیت عملیاتی روی حساب است. این دو مرتبط‌اند ولی یک مدل نیستند.

### گام چهارم: Module/Service Candidate

در شروع Lab:

- legalorders module
- deposits module

هر دو می‌توانند در یک Modular Monolith باشند. هنوز دلیل کافی برای دو Microservice مستقل نداریم.

### گام پنجم: Use Case

- RegisterLegalOrder
- PlaceLegalHold
- RevokeLegalOrder
- ReleaseLegalHold

### گام ششم: Command/Query

Legal Orders پس از تأیید حکم، قصد اعمال Hold را با Command بیان می‌کند. Contract باید دست‌کم مرجع حکم، حساب هدف، مبلغ/دامنه، تاریخ مؤثر و شناسهٔ Idempotency را حمل کند.

Deposits تصمیم می‌گیرد آیا عملیات با وضعیت حساب و قواعد خودش سازگار است. Legal Orders نباید مستقیم جدول Hold یا ماندهٔ Deposits را تغییر دهد.

### گام هفتم: API/Event

نمونهٔ معنایی:

~~~text
Command: PlaceLegalHold
Result: Accepted / Rejected with reason
Event: LegalHoldPlaced
Event: LegalHoldPlacementRejected
~~~

نام Transport هنوز تعیین نشده است. Command می‌تواند از طریق API همگام یا پیام پردازش شود. انتخاب آن به نیاز Latency، Coupling، Failure Handling و فرایند کسب‌وکاری بستگی دارد.

### مالکیت

| داده/تصمیم | مالک |
|---|---|
| اعتبار و چرخهٔ عمر حکم | Legal Orders |
| نگاشت حکم به حساب هدف | نیازمند Contract روشن؛ تصمیم مشترک مبهم ممنوع |
| Hold عملیاتی روی سپرده | Deposits |
| ماندهٔ قابل برداشت | Deposits |
| ثبت مالی ناشی از جابه‌جایی وجه | Accounting |

خود Hold الزاماً جابه‌جایی وجه و Journal Entry ایجاد نمی‌کند. ممکن است گزارش آماری یا ثبت کنترلی لازم باشد، اما Accounting نباید برای نمایش ماندهٔ قابل برداشت، مالک Hold شود.

این مثال نشان می‌دهد «مالک Trigger»، «مالک تصمیم» و «مالک State» همیشه یک Context نیستند.

---

## ۸. BIAN دقیقاً چه نقشی دارد؟

BIAN یک Reference Architecture تخصصی صنعت بانکداری است. در نسخهٔ 14.0، Release Notes رسمی ۳۲۲ Service Domain، ۳۸ Business Domain، ۵۸۶ Business Capability و ۲۴۲ Semantic API را گزارش می‌کند.

BIAN برای ما سه کاربرد اصلی دارد:

1. **زبان مشترک:** مقایسهٔ اصطلاحات سازمان با واژگان شناخته‌شدهٔ بانکی
2. **Completeness Check:** کشف Capability یا مسئولیت جاافتاده
3. **Reference Contract:** استفاده از Service Operation، Business Object و Semantic API به‌عنوان ورودی طراحی

BIAN برای ما این کارها را انجام نمی‌دهد:

- مرز تیم‌ها را خودکار تعیین نمی‌کند.
- هر Service Domain را به Microservice تبدیل نمی‌کند.
- مقررات، Product Model و Legacy Constraints بانک ما را کشف نمی‌کند.
- Transaction Boundary و Data Ownership نهایی را بدون تحلیل محلی تعیین نمی‌کند.
- جای مصاحبه با خبرگان و Event/Domain Discovery را نمی‌گیرد.

### چرا Service Domain مساوی Microservice نیست؟

Service Domain در BIAN یک پارتیشن منطقی استانداردشده از مسئولیت بانکی است. Deployment Boundary علاوه بر مسئولیت منطقی به نیروهای دیگری وابسته است:

- Transactional Cohesion
- Change Coupling
- نیاز استقرار و مقیاس مستقل
- ساختار و بلوغ تیم
- Latency و Availability
- Data Ownership
- هزینهٔ عملیات توزیع‌شده

ممکن است چند Service Domain در یک Module یا Service عملیاتی شوند؛ یا یک مسئولیت بزرگ برای مقیاس و تیم به چند Deployable Component شکسته شود. این تصمیم باید ADR و Verification داشته باشد.

### روش درست استفاده در Day 05

1. ابتدا بر اساس کسب‌وکار خودمان Capability Map L1 را می‌سازیم.
2. نام‌ها، Scope و Owner را نقد می‌کنیم.
3. سپس با BIAN 14 Gap Check می‌کنیم.
4. تفاوت‌ها را به سه گروه تقسیم می‌کنیم:
   - Gap واقعی
   - تفاوت نام/سطح تجزیه
   - Capability نامرتبط با Scope

اگر از BIAN شروع و همهٔ خانه‌ها را کپی کنیم، یک Reference Landscape داریم، نه معماری بانک خودمان.

---

## ۹. چهار نیروی طراحی که این هفته عمیق‌تر می‌شوند

### Cohesion

چیزهایی که به یک دلیل تغییر می‌کنند، بهتر است کنار هم باشند.

اگر منطق اعتبار حکم قضایی، محاسبهٔ ماندهٔ قابل برداشت و ثبت دفتر کل در یک کلاس باشد، آن کلاس سه دلیل مستقل برای تغییر دارد و Cohesion ضعیف است.

### Coupling

هرچه یک جزء برای کارکردن جزئیات بیشتری از دیگری بداند، تغییرها بیشتر منتشر می‌شوند.

Deposits که جدول Legal Orders را مستقیم Query می‌کند، به Schema و معنای داخلی Context حقوقی کاپل شده است.

### Encapsulation

State و رفتار مرتبط از مسیر Interface کنترل می‌شوند.

اگر هر Service بتواند ستون blocked_amount را Update کند، Deposits مانده و Hold را Encapsulate نکرده است.

### Information Hiding

تصمیم طراحیِ محتمل‌التغییر پشت Boundary پنهان می‌شود.

مصرف‌کنندهٔ PlaceLegalHold نباید بداند Hold در یک جدول، چند Ledger Entry یا State Machine داخلی نگهداری می‌شود. Contract باید معنای کسب‌وکاری را بدهد، نه روش پیاده‌سازی را.

روز چهارم این مفاهیم را روی یک طراحی عمداً بد باز می‌کنیم.

---

## ۱۰. هفت خطای رایج که از امروز ممنوع‌اند

### خطای ۱: شروع از جدول

«جدول LOAN داریم، پس LoanService می‌سازیم.»

جدول شاهد وضع موجود است، نه اثبات Boundary. یک جدول ممکن است چند مفهوم را مخلوط کرده باشد یا فقط Projection باشد.

### خطای ۲: شروع از چارت

«چون یک ادارهٔ چک داریم، Check یک Bounded Context مستقل است.»

ساختار سازمان می‌تواند سرنخ باشد، ولی ممکن است تاریخی، سیاسی یا مبتنی بر سامانهٔ Legacy باشد.

### خطای ۳: هر اسم کسب‌وکاری یک Microservice

داشتن نام دامینی شرط لازم برای مرز خوب است، نه شرط کافی برای استقرار مستقل.

### خطای ۴: اشتراک Entity

CustomerEntity مشترک میان همهٔ سرویس‌ها ظاهراً Duplicate را کم می‌کند، ولی مدل و Release را کاپل می‌کند. Contextها معمولاً به Contract و شناسهٔ مشترک نیاز دارند، نه Entity داخلی مشترک.

### خطای ۵: مالکیت مشترک

عبارت «Lending و Accounting هر دو مالک ماندهٔ تسهیلات‌اند» مسئولیت را مبهم می‌کند. باید نوع مانده را تفکیک کنیم: ماندهٔ عملیاتی اصل در Lending، ماندهٔ دفتر معین/کل در Accounting و Projection گزارش‌گری در Data.

### خطای ۶: API به‌جای Capability

API افتتاح حساب توانمندی نیست؛ Interface یک Use Case است که Capability مدیریت سپرده را محقق می‌کند.

### خطای ۷: Event به‌جای Fact

Event با نام مبهم ProcessLoan یا DoAccounting نمی‌گوید چه Factی رخ داده است. نام، مالک، زمان و معنای Event باید روشن باشد.

---

## ۱۱. تمرین هدایت‌شدهٔ ۱۵ دقیقه‌ای

پس از مطالعه، قابلیت «مسدودی قضایی سپرده» را در این جدول بنویس:

| مرحله | پاسخ تو | چرا؟ |
|---|---|---|
| Capability |  |  |
| Domain/Subdomain |  |  |
| Bounded Context |  |  |
| Module/Service Candidate |  |  |
| Use Case |  |  |
| Command/Query |  |  |
| API/Event |  |  |
| Data Owner |  |  |
| Decision Owner |  |  |

سپس سه کنترل انجام بده:

1. آیا جایی نام سامانه یا جدول را به‌جای مفهوم کسب‌وکاری گذاشته‌ای؟
2. آیا یک Context را به‌دلیل وجود یک API، Microservice فرض کرده‌ای؟
3. آیا برای یک داده یا تصمیم بیش از یک Owner نوشته‌ای؟

---

## ۱۲. جمع‌بندی فشرده

مدل ذهنی روز اول:

~~~text
Capability می‌گوید بانک چه کاری باید بتواند انجام دهد.
Domain/Subdomain محل دانش و مسئله را مشخص می‌کند.
Bounded Context مرز اعتبار مدل و زبان است.
Module مسئولیت را در کد محصور می‌کند.
Deployable Service تصمیم Runtime و عملیاتی است.
Use Case قصد مشخص کسب‌وکاری را اجرا می‌کند.
Command/Query قصد مصرف‌کننده را بیان می‌کند.
API/Event قرارداد تعامل در مرز است.
~~~

این عناصر مرتبط‌اند ولی مساوی نیستند و نگاشت یک‌به‌یک ندارند.

BIAN برای نام‌گذاری، Gap Check و Reference Contract ارزشمند است. BIAN جای طراحی محلی Boundary، Ownership، Transaction و Team را نمی‌گیرد.

## کار بعد از درس

1. به Submission برگرد.
2. پاسخ خام را پاک نکن.
3. بخش «بازنگری پس از درس» و جدول Traceability را کامل کن.
4. Exit Ticket را بدون مراجعه به متن پاسخ بده.
5. فایل را برای Review ارائه کن.

منابع رسمی و زمان مطالعه در [References](../references/README.md) آمده است.
