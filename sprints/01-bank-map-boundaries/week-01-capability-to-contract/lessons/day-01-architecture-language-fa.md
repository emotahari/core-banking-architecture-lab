<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 01</span> — زبان مشترک معماری: از توانمندی بانک تا <span dir="ltr">Contract</span>

- زمان مطالعه: ۲۵ دقیقه
- سطح: میانی رو به پیشرفته
- مسئلهٔ نمونه: مسدودی قضایی سپرده
- خروجی: توانایی تشخیص سطح هر تصمیم و ساخت <span dir="ltr">Traceability Chain</span>

> اگر تمرین خط پایه را هنوز انجام نداده‌ای، این فایل را ببند. ابتدا ۱۲ دقیقه به
> [<span dir="ltr">Architecture Baseline</span>](../exercises/day-01-baseline.md) پاسخ بده. هدف ثبت مدل ذهنی واقعی تو پیش از آموزش است.

## ۱. امروز دقیقاً چه چیزی باید یاد بگیری؟

در پایان روز باید بتوانی:

1. <span dir="ltr">Business Architecture</span>، <span dir="ltr">Solution Architecture</span> و <span dir="ltr">Software Architecture</span> را از هم جدا کنی.
2. <span dir="ltr">Capability</span> را با <span dir="ltr">Process</span>، <span dir="ltr">Business Service</span>، <span dir="ltr">Application</span> و <span dir="ltr">API</span> اشتباه نگیری.
3. تفاوت <span dir="ltr">System</span>، <span dir="ltr">Domain</span>، <span dir="ltr">Subdomain</span>، <span dir="ltr">Bounded Context</span>، <span dir="ltr">Module</span> و <span dir="ltr">Deployable Service</span> را توضیح بدهی.
4. از یک نیاز بانکی این زنجیره را بسازی:


</div>

<div dir="ltr" align="left">

~~~text
Capability
→ Domain / Subdomain
→ Bounded Context
→ Module / Service Candidate
→ Use Case
→ Command / Query
→ API / Event
~~~

</div>

<div dir="rtl" align="right">


5. توضیح بدهی چرا این زنجیره «نگاشت یک‌به‌یک» نیست.
6. <span dir="ltr">BIAN</span> را به‌عنوان <span dir="ltr">Reference Architecture</span> به‌کار ببری، نه دستگاه تولید خودکار <span dir="ltr">Microservice.</span>

موضوع امروز انتخاب <span dir="ltr">Kafka</span>، دیتابیس، <span dir="ltr">REST</span> یا معماری <span dir="ltr">Microservice</span> نیست. اگر پیش از روشن‌شدن <span dir="ltr">Capability</span> و <span dir="ltr">Ownership</span> سراغ این انتخاب‌ها برویم، ممکن است پاسخ فنی خوبی برای مسئلهٔ اشتباه بسازیم.

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
| قواعد حیاتی | چه <span dir="ltr">Invariant</span>هایی حتی هنگام خطا و هم‌زمانی نباید شکسته شوند؟ |
| تغییر ایمن | تغییر در یک قاعده تا کجا موج ایجاد می‌کند؟ |

<span dir="ltr">Diagram</span>، <span dir="ltr">Framework</span>، <span dir="ltr">Cloud</span> و <span dir="ltr">Microservice</span> می‌توانند ابزار یا نتیجهٔ تصمیم معماری باشند؛ خود معماری نیستند. دو تیم ممکن است <span dir="ltr">Diagram</span> مشابه داشته باشند، ولی یکی مالکیت دادهٔ روشن و <span dir="ltr">Contract</span> پایدار داشته باشد و دیگری از دیتابیس مشترک، دانش پنهان و <span dir="ltr">Release</span> هماهنگ رنج ببرد. ظاهر آن‌ها یکی است، معماری آن‌ها نه.

### سه نشانهٔ یک تصمیم معماری

یک تصمیم معمولاً معماری است اگر دست‌کم یکی از این ویژگی‌ها را داشته باشد:

- تغییرش پرهزینه، پرریسک یا سازمان‌گستر است.
- چند جزء یا تیم باید آن را رعایت کنند.
- روی صحت مالی، امنیت، دسترس‌پذیری یا امکان تحول اثر جدی دارد.

نام‌گذاری یک متغیر معمولاً تصمیم معماری نیست. اینکه ماندهٔ قابل برداشت سپرده را <span dir="ltr">Deposits</span> مالک باشد یا <span dir="ltr">Accounting</span>، تصمیم معماری و دامینی است؛ چون روی تراکنش، <span dir="ltr">Locking</span>، <span dir="ltr">API</span>، عملیات و پاسخ‌گویی سازمانی اثر می‌گذارد.

---

## ۳. سه سطحی که نباید در یک <span dir="ltr">Diagram</span> مخلوط شوند

### ۳.۱ <span dir="ltr">Business Architecture</span>

<span dir="ltr">Business Architecture</span> توضیح می‌دهد بانک برای تحقق راهبردش **چه توانمندی‌هایی** لازم دارد، چگونه ارزش تولید می‌کند و اطلاعات و مسئولیت‌های کلیدی چگونه سازمان می‌یابند.

واحدهای معمول تحلیل:

- <span dir="ltr">Goal</span> و <span dir="ltr">Outcome</span>
- <span dir="ltr">Capability</span> و <span dir="ltr">Capability Map</span>
- <span dir="ltr">Value Stream</span>
- <span dir="ltr">Business Information</span>
- <span dir="ltr">Stakeholder</span> و <span dir="ltr">Responsibility</span>

نمونه پرسش‌ها:

- بانک برای اعطای اعتبار چه توانمندی‌هایی لازم دارد؟
- کدام <span dir="ltr">Capability</span> برای بانک راهبردی و کدام عمومی است؟
- مالک بلوغ «مدیریت سپرده» چه نقشی است؟
- کدام <span dir="ltr">Capability</span>ها مانع عرضهٔ سریع محصول جدیدند؟

<span dir="ltr">Business Architecture</span> نباید به نسخهٔ <span dir="ltr">Spring Boot</span>، نام جدول یا تعداد <span dir="ltr">Pod</span>ها پاسخ بدهد.

### ۳.۲ <span dir="ltr">Solution Architecture</span>

<span dir="ltr">Solution Architecture</span> برای یک مسئله یا تغییر مشخص، همکاری چند <span dir="ltr">Domain</span>، <span dir="ltr">Application</span>، <span dir="ltr">Data Store</span> و <span dir="ltr">Integration</span> را طراحی می‌کند.

واحدهای معمول تحلیل:

- <span dir="ltr">System/Context Boundary</span>
- <span dir="ltr">Component</span> یا <span dir="ltr">Service Candidate</span>
- <span dir="ltr">Data Flow</span> و <span dir="ltr">Contract</span>
- <span dir="ltr">Quality Attribute</span>
- <span dir="ltr">Integration</span>، <span dir="ltr">Security</span> و <span dir="ltr">Deployment Constraint</span>

نمونه پرسش‌ها:

- فرایند اعطای تسهیلات چگونه با <span dir="ltr">Deposits</span> و <span dir="ltr">Accounting</span> همکاری می‌کند؟
- پاسخ گم‌شده پس از واریز موفق چگونه مدیریت می‌شود؟
- مرز تراکنش محلی کجاست؟
- چه داده‌ای <span dir="ltr">Snapshot</span> و چه داده‌ای <span dir="ltr">Reference</span> است؟

<span dir="ltr">Solution Architecture</span> پل میان مسئلهٔ کسب‌وکار و چند سیستم درگیر است.

### ۳.۳ <span dir="ltr">Software Architecture</span>

<span dir="ltr">Software Architecture</span> ساختار درونی یک نرم‌افزار یا سرویس را تعیین می‌کند.

واحدهای معمول تحلیل:

- <span dir="ltr">Package</span> و <span dir="ltr">Module</span>
- <span dir="ltr">Layer</span>، <span dir="ltr">Port</span> و <span dir="ltr">Adapter</span>
- <span dir="ltr">Aggregate</span> و <span dir="ltr">Repository</span>
- <span dir="ltr">Interface</span> و <span dir="ltr">Dependency Rule</span>
- <span dir="ltr">Thread</span>، <span dir="ltr">Transaction</span> و <span dir="ltr">Runtime Component</span>

نمونه پرسش‌ها:

- <span dir="ltr">Domain Model</span> به <span dir="ltr">Spring</span> یا <span dir="ltr">JPA</span> وابسته است؟
- <span dir="ltr">Use Case</span> اعطای تسهیلات در <span dir="ltr">Application Layer</span> چگونه اجرا می‌شود؟
- چه <span dir="ltr">Package</span>هایی <span dir="ltr">Public API</span> ماژول‌اند و چه <span dir="ltr">Package</span>هایی <span dir="ltr">Internal</span>؟
- <span dir="ltr">Invariant</span> قرارداد تسهیلات کجا آزمون می‌شود؟

### جدول کنترل

| گزاره | سطح غالب |
|---|---|
| بانک باید توانایی مدیریت مسدودی وجوه را داشته باشد. | <span dir="ltr">Business Architecture</span> |
| <span dir="ltr">Legal Orders</span> و <span dir="ltr">Deposits</span> با <span dir="ltr">Contract</span> مشخص همکاری می‌کنند. | <span dir="ltr">Solution Architecture</span> |
| کلاس <span dir="ltr">DepositAccount</span> فقط از متد <span dir="ltr">placeHold</span> تغییر می‌کند. | <span dir="ltr">Software Architecture</span> |
| نرخ خطای عملیات مسدودی باید کمتر از حد مصوب باشد. | <span dir="ltr">Solution/Runtime Architecture</span> |
| واحد حقوقی زیرمجموعهٔ کدام معاونت باشد؟ | <span dir="ltr">Operating Model</span> / <span dir="ltr">Organization Design</span> |

<span dir="ltr">Enterprise Architecture</span> چتر بزرگ‌تری است که <span dir="ltr">Business</span>، <span dir="ltr">Data</span>، <span dir="ltr">Application</span> و <span dir="ltr">Technology Architecture</span> را در سطح بنگاه هم‌راستا می‌کند. در این دوره به‌اندازه‌ای از آن استفاده می‌کنیم که تصمیم نرم‌افزاری از <span dir="ltr">Portfolio</span>، <span dir="ltr">Capability</span> و <span dir="ltr">Operating Model</span> جدا نیفتد.

---

## ۴. <span dir="ltr">Capability</span>؛ نقطهٔ شروع پایدار

### تعریف عملیاتی

<span dir="ltr">Business Capability</span> یعنی **توان سازمان برای انجام یک کار کسب‌وکاری و تولید یک <span dir="ltr">Outcome</span>**.

<span dir="ltr">Capability</span> می‌گوید «چه کاری باید بتوانیم انجام دهیم؟» و عمداً دربارهٔ اینکه کدام واحد، فرایند، نرم‌افزار یا فناوری آن را انجام می‌دهد سکوت می‌کند.

نمونه‌های مناسب:

- مدیریت رابطه با مشتری
- مدیریت محصولات و شرایط
- نگهداری سپرده
- مدیریت اعتبار و تسهیلات
- جابه‌جایی و تسویهٔ وجوه
- ثبت و کنترل مالی
- پایش تقلب

نمونه‌های نامناسب:

- اجرای فرایند افتتاح حساب در <span dir="ltr">BPM</span>
- سامانهٔ سپرده
- تیم تسهیلات یک
- <span dir="ltr">API</span> واریز
- <span dir="ltr">Kafka Event Processing</span>

موارد نامناسب یا <span dir="ltr">Process</span> هستند، یا <span dir="ltr">Application/Organization/Technology.</span> ممکن است همگی برای تحقق <span dir="ltr">Capability</span> لازم باشند، ولی خود <span dir="ltr">Capability</span> نیستند.

### <span dir="ltr">Capability</span> در برابر <span dir="ltr">Process</span>

فرض کن بانک <span dir="ltr">Capability</span> «مدیریت مسدودی وجوه» را دارد.

این <span dir="ltr">Capability</span> ممکن است با <span dir="ltr">Process</span>های مختلف اجرا شود:

- مسدودی قضایی با دریافت نامه و تأیید حقوقی
- مسدودی وثیقه‌ای هنگام اعطای تسهیلات
- <span dir="ltr">Hold</span> کوتاه‌مدت هنگام پرداخت کارت
- مسدودی سیستمی به‌دلیل کنترل تقلب

<span dir="ltr">Capability</span> نسبتاً پایدار است؛ <span dir="ltr">Process</span> با مقررات، کانال و اتوماسیون تغییر می‌کند.

### <span dir="ltr">Capability</span> در برابر <span dir="ltr">Business Service</span>

<span dir="ltr">Capability</span> توان داخلی بانک است. <span dir="ltr">Business Service</span> شکل ارزش قابل‌مصرفی است که از آن توان ارائه می‌شود.

مثلاً:

- <span dir="ltr">Capability:</span> مدیریت پرداخت
- <span dir="ltr">Business Service:</span> انتقال وجه داخلی برای مشتری

یک <span dir="ltr">Capability</span> می‌تواند چند <span dir="ltr">Business Service</span> عرضه کند و یک <span dir="ltr">Business Service</span> ممکن است به چند <span dir="ltr">Capability</span> وابسته باشد.

### <span dir="ltr">Capability</span> در برابر <span dir="ltr">Application</span>

ممکن است امروز سه سامانه بخشی از «مدیریت مشتری» را انجام دهند و فردا در یک <span dir="ltr">Platform</span> ادغام شوند. <span dir="ltr">Capability</span> باقی است، <span dir="ltr">Application Landscape</span> تغییر می‌کند.

اگر <span dir="ltr">Capability Map</span> را از روی فهرست سامانه‌ها بسازیم، وضع موجود را با ماهیت کسب‌وکار اشتباه گرفته‌ایم و <span dir="ltr">Legacy</span> را به مدل هدف تحمیل کرده‌ایم.

### آزمون شش‌گانهٔ <span dir="ltr">Capability</span>

برای هر عنوان پیشنهادی بپرس:

1. آیا می‌گوید بانک چه کاری می‌تواند انجام دهد؟
2. آیا مستقل از فناوری و <span dir="ltr">Vendor</span> است؟
3. آیا مستقل از چارت سازمانی است؟
4. آیا از <span dir="ltr">Process</span>های اجرای آن پایدارتر است؟
5. آیا <span dir="ltr">Outcome</span> یا <span dir="ltr">KPI</span> برای آن قابل تصور است؟
6. آیا می‌توان <span dir="ltr">Owner</span> کسب‌وکاری برای بلوغ آن تعیین کرد؟

پاسخ منفی به چند سؤال نشانهٔ آن است که عنوان احتمالاً <span dir="ltr">Capability</span> نیست.

---

## ۵. از <span dir="ltr">Problem Space</span> تا <span dir="ltr">Solution Space</span>

بزرگ‌ترین خطای معماری سازمانی این است که عناصر سطوح مختلف را هم‌معنا فرض کنیم. برای جلوگیری از آن، هر مفهوم را دقیق در جای خود می‌گذاریم.

### <span dir="ltr">System</span>

<span dir="ltr">System</span> مجموعه‌ای از اجزای مرتبط با یک هدف و <span dir="ltr">Boundary</span> مشخص است. تعریف <span dir="ltr">System</span> به «<span dir="ltr">System of Interest</span>» وابسته است.

- کل بانک می‌تواند یک <span dir="ltr">System</span> باشد.
- <span dir="ltr">Core Banking Platform</span> می‌تواند <span dir="ltr">System</span> باشد.
- سرویس <span dir="ltr">Deposits</span> نیز در یک بررسی محدود می‌تواند <span dir="ltr">System</span> باشد.

پس «<span dir="ltr">System</span>» به‌تنهایی اندازه یا نوع معماری را تعیین نمی‌کند؛ <span dir="ltr">Boundary</span> بررسی را مشخص می‌کند.

### <span dir="ltr">Domain</span>

<span dir="ltr">Domain</span> حوزهٔ مسئله، دانش و فعالیتی است که می‌خواهیم برایش مدل بسازیم؛ مانند <span dir="ltr">Lending</span> یا <span dir="ltr">Payments.</span>

<span dir="ltr">Domain</span> به مسئله تعلق دارد، نه به <span dir="ltr">Repository</span> کد. ممکن است امروز هیچ سامانهٔ مناسبی برای <span dir="ltr">Domain</span> وجود نداشته باشد، ولی <span dir="ltr">Domain</span> همچنان واقعی است.

### <span dir="ltr">Subdomain</span>

<span dir="ltr">Domain</span> بزرگ به <span dir="ltr">Subdomain</span>های متمایز شکسته می‌شود. <span dir="ltr">Lending</span> می‌تواند شامل بخش‌هایی مانند:

- <span dir="ltr">Loan Origination</span>
- <span dir="ltr">Credit Decision</span>
- <span dir="ltr">Loan Servicing</span>
- <span dir="ltr">Repayment</span>
- <span dir="ltr">Delinquency Management</span>

باشد. مرز دقیق برای هر بانک با مدل کسب‌وکار، مقررات و تمایز راهبردی آن تعیین می‌شود؛ فهرست آماده جای <span dir="ltr">Discovery</span> را نمی‌گیرد.

### <span dir="ltr">Bounded Context</span>

<span dir="ltr">Bounded Context</span> مرزی است که درون آن یک <span dir="ltr">Model</span> و <span dir="ltr">Ubiquitous Language</span> مشخص معتبر است.

واژهٔ <span dir="ltr">Account</span> مثال مهمی است:

- در <span dir="ltr">Deposits:</span> قرارداد نگهداری وجوه و ماندهٔ عملیاتی
- در <span dir="ltr">Lending:</span> موقعیت بدهی و برنامهٔ بازپرداخت
- در <span dir="ltr">Accounting:</span> حساب دفتر کل یا معین
- در <span dir="ltr">IAM:</span> حساب کاربری

اگر همهٔ این معناها را در یک مدل مشترک <span dir="ltr">Account</span> ادغام کنیم، مدل مبهم و تغییرها کاپل می‌شوند. <span dir="ltr">Bounded Context</span> اجازه می‌دهد هر معنا در مرز خودش دقیق بماند و ترجمه در <span dir="ltr">Contract</span> رخ دهد.

### <span dir="ltr">Module</span>

<span dir="ltr">Module</span> واحد منطقی کد با:

- <span dir="ltr">API</span> آشکار
- جزئیات <span dir="ltr">Internal</span>
- مسئولیت منسجم
- <span dir="ltr">Dependency</span> کنترل‌شده

است. <span dir="ltr">Module</span> می‌تواند همراه چند <span dir="ltr">Module</span> دیگر در یک <span dir="ltr">Process</span> و یک <span dir="ltr">Deployment</span> اجرا شود.

### <span dir="ltr">Deployable Service</span>

<span dir="ltr">Deployable Service</span> واحد <span dir="ltr">Runtime</span> قابل استقرار است. وقتی آن را <span dir="ltr">Microservice</span> می‌نامیم، معمولاً انتظار داریم:

- <span dir="ltr">Lifecycle</span> استقرار مستقل داشته باشد.
- <span dir="ltr">Boundary</span> مسئولیت روشن باشد.
- داده و تغییرات <span dir="ltr">Schema</span> تحت مالکیت آن باشد.
- خرابی و عملیات مستقل مدیریت شود.
- هزینهٔ <span dir="ltr">Network</span>، <span dir="ltr">Observability</span> و <span dir="ltr">Consistency</span> توزیع‌شده پذیرفته شود.

هر <span dir="ltr">Module</span> خوب <span dir="ltr">Microservice</span> نیست. ابتدا <span dir="ltr">Module</span> خوب می‌سازیم؛ فقط اگر محرک‌های کسب‌وکاری و عملیاتی کافی وجود داشتند، استخراج فیزیکی را بررسی می‌کنیم.

### <span dir="ltr">API</span> و <span dir="ltr">Event</span>

<span dir="ltr">API</span> و <span dir="ltr">Event</span> شکل <span dir="ltr">Contract</span> در <span dir="ltr">Boundary</span> هستند، نه جایگزین <span dir="ltr">Boundary.</span>

- <span dir="ltr">Command</span> قصد انجام تغییر دارد: <span dir="ltr">PlaceLegalHold</span>
- <span dir="ltr">Query</span> اطلاعات می‌خواهد: <span dir="ltr">GetAvailableBalance</span>
- <span dir="ltr">Event</span> وقوع <span dir="ltr">Fact</span> را اعلام می‌کند: <span dir="ltr">LegalHoldPlaced</span>

نام <span dir="ltr">Event</span> باید رخداد گذشته را بگوید. <span dir="ltr">LoanGrantRequest</span> یک درخواست است، نه <span dir="ltr">Event. LoanGranted</span> یک <span dir="ltr">Fact</span> رخ‌داده است.

---

## ۶. زنجیرهٔ <span dir="ltr">Capability</span> تا <span dir="ltr">Contract</span>

این زنجیره ابزار <span dir="ltr">Traceability</span> است:


</div>

<div dir="ltr" align="left">

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

</div>

<div dir="rtl" align="right">


برای هر پله سؤال مشخصی داریم:

| پله | سؤال اصلی | خطای رایج |
|---|---|---|
| <span dir="ltr">Capability</span> | بانک چه کاری باید بتواند انجام دهد؟ | نام‌گذاری با سامانه یا واحد |
| <span dir="ltr">Domain/Subdomain</span> | این دانش و قواعد متعلق به کدام <span dir="ltr">Problem Space</span> است؟ | شروع از جدول |
| <span dir="ltr">Bounded Context</span> | این مدل و واژه‌ها در کدام مرز معتبرند؟ | مدل مشترک عظیم |
| <span dir="ltr">Module/Service Candidate</span> | کدام واحد منطقی تغییر و مسئولیت را محصور می‌کند؟ | <span dir="ltr">Microservice</span> پیش‌فرض |
| <span dir="ltr">Use Case</span> | چه قصد یا <span dir="ltr">Outcome</span> مشخصی اجرا می‌شود؟ | <span dir="ltr">CRUD</span> به‌جای رفتار |
| <span dir="ltr">Command/Query</span> | مصرف‌کننده چه قصدی را بیان می‌کند؟ | نام فنی و مبهم |
| <span dir="ltr">API/Event</span> | <span dir="ltr">Contract</span> بیرونی چگونه معنا، خطا و <span dir="ltr">Version</span> را منتقل می‌کند؟ | افشای <span dir="ltr">Entity</span> و <span dir="ltr">Schema</span> داخلی |

### این نگاشت یک‌به‌یک نیست

قواعد مهم:

- یک <span dir="ltr">Capability</span> می‌تواند به چند <span dir="ltr">Domain</span> وابسته باشد.
- یک <span dir="ltr">Domain</span> می‌تواند چند <span dir="ltr">Subdomain</span> و چند <span dir="ltr">Bounded Context</span> داشته باشد.
- یک <span dir="ltr">Bounded Context</span> می‌تواند ابتدا یک <span dir="ltr">Module</span> باشد و بعداً یک یا چند <span dir="ltr">Deployable Service</span> شود.
- یک <span dir="ltr">Service</span> می‌تواند چند <span dir="ltr">Use Case</span> عرضه کند.
- یک <span dir="ltr">Use Case</span> می‌تواند یک <span dir="ltr">Command</span> ورودی و چند <span dir="ltr">Event</span> خروجی داشته باشد.
- یک <span dir="ltr">API</span> می‌تواند بخشی از چند جریان کسب‌وکاری باشد.

هدف زنجیره این نیست که برای هر <span dir="ltr">Capability</span> یک <span dir="ltr">Microservice</span> بسازیم. هدف این است که هر جزء نرم‌افزاری دلیل کسب‌وکاری و مالکیت قابل ردیابی داشته باشد.

---

## ۷. مثال هدایت‌شده: مسدودی قضایی سپرده

برای آلوده‌نکردن تمرین خط پایه، مثال درس را از سناریوی دیگری می‌گیریم.

### صورت مسئله

بانک یک حکم معتبر دریافت می‌کند که باید مبلغ معینی از سپردهٔ مشتری مسدود شود. وضعیت حکم ممکن است بعداً لغو یا اصلاح شود. ماندهٔ قابل برداشت باید بلافاصله اثر <span dir="ltr">Hold</span> را نشان دهد.

### گام اول: <span dir="ltr">Capability</span>

حداقل دو <span dir="ltr">Capability</span> قابل تشخیص است:

1. مدیریت دستورهای حقوقی/نظارتی
2. مدیریت محدودیت و <span dir="ltr">Hold</span> وجوه سپرده

«سامانه نامه‌های قضایی» <span dir="ltr">Capability</span> نیست؛ نام راه‌حل یا <span dir="ltr">Application</span> است.

### گام دوم: <span dir="ltr">Domain/Subdomain</span>

- <span dir="ltr">Legal/Compliance:</span> اعتبار، مرجع، دامنه و چرخهٔ عمر حکم
- <span dir="ltr">Deposits:</span> اعمال و رفع <span dir="ltr">Hold</span> و محاسبهٔ ماندهٔ قابل برداشت

ممکن است <span dir="ltr">Customer/Party</span> برای تطبیق هویت مشارکت کند، ولی مالک حکم یا <span dir="ltr">Hold</span> نمی‌شود.

### گام سوم: <span dir="ltr">Bounded Context</span>

- <span dir="ltr">Legal Orders Context</span>
- <span dir="ltr">Deposit Accounts Context</span>

واژهٔ <span dir="ltr">Restriction</span> در <span dir="ltr">Context</span> حقوقی به الزام قانونی اشاره دارد؛ <span dir="ltr">Hold</span> در <span dir="ltr">Deposits</span> یک وضعیت عملیاتی روی حساب است. این دو مرتبط‌اند ولی یک مدل نیستند.

### گام چهارم: <span dir="ltr">Module/Service Candidate</span>

در شروع <span dir="ltr">Lab:</span>

- <span dir="ltr">legalorders module</span>
- <span dir="ltr">deposits module</span>

هر دو می‌توانند در یک <span dir="ltr">Modular Monolith</span> باشند. هنوز دلیل کافی برای دو <span dir="ltr">Microservice</span> مستقل نداریم.

### گام پنجم: <span dir="ltr">Use Case</span>

- <span dir="ltr">RegisterLegalOrder</span>
- <span dir="ltr">PlaceLegalHold</span>
- <span dir="ltr">RevokeLegalOrder</span>
- <span dir="ltr">ReleaseLegalHold</span>

### گام ششم: <span dir="ltr">Command/Query</span>

<span dir="ltr">Legal Orders</span> پس از تأیید حکم، قصد اعمال <span dir="ltr">Hold</span> را با <span dir="ltr">Command</span> بیان می‌کند. <span dir="ltr">Contract</span> باید دست‌کم مرجع حکم، حساب هدف، مبلغ/دامنه، تاریخ مؤثر و شناسهٔ <span dir="ltr">Idempotency</span> را حمل کند.

<span dir="ltr">Deposits</span> تصمیم می‌گیرد آیا عملیات با وضعیت حساب و قواعد خودش سازگار است. <span dir="ltr">Legal Orders</span> نباید مستقیم جدول <span dir="ltr">Hold</span> یا ماندهٔ <span dir="ltr">Deposits</span> را تغییر دهد.

### گام هفتم: <span dir="ltr">API/Event</span>

نمونهٔ معنایی:


</div>

<div dir="ltr" align="left">

~~~text
Command: PlaceLegalHold
Result: Accepted / Rejected with reason
Event: LegalHoldPlaced
Event: LegalHoldPlacementRejected
~~~

</div>

<div dir="rtl" align="right">


نام <span dir="ltr">Transport</span> هنوز تعیین نشده است. <span dir="ltr">Command</span> می‌تواند از طریق <span dir="ltr">API</span> همگام یا پیام پردازش شود. انتخاب آن به نیاز <span dir="ltr">Latency</span>، <span dir="ltr">Coupling</span>، <span dir="ltr">Failure Handling</span> و فرایند کسب‌وکاری بستگی دارد.

### مالکیت

| داده/تصمیم | مالک |
|---|---|
| اعتبار و چرخهٔ عمر حکم | <span dir="ltr">Legal Orders</span> |
| نگاشت حکم به حساب هدف | نیازمند <span dir="ltr">Contract</span> روشن؛ تصمیم مشترک مبهم ممنوع |
| <span dir="ltr">Hold</span> عملیاتی روی سپرده | <span dir="ltr">Deposits</span> |
| ماندهٔ قابل برداشت | <span dir="ltr">Deposits</span> |
| ثبت مالی ناشی از جابه‌جایی وجه | <span dir="ltr">Accounting</span> |

خود <span dir="ltr">Hold</span> الزاماً جابه‌جایی وجه و <span dir="ltr">Journal Entry</span> ایجاد نمی‌کند. ممکن است گزارش آماری یا ثبت کنترلی لازم باشد، اما <span dir="ltr">Accounting</span> نباید برای نمایش ماندهٔ قابل برداشت، مالک <span dir="ltr">Hold</span> شود.

این مثال نشان می‌دهد «مالک <span dir="ltr">Trigger</span>»، «مالک تصمیم» و «مالک <span dir="ltr">State</span>» همیشه یک <span dir="ltr">Context</span> نیستند.

---

## ۸. <span dir="ltr">BIAN</span> دقیقاً چه نقشی دارد؟

<span dir="ltr">BIAN</span> یک <span dir="ltr">Reference Architecture</span> تخصصی صنعت بانکداری است. در نسخهٔ 14.0، <span dir="ltr">Release Notes</span> رسمی ۳۲۲ <span dir="ltr">Service Domain</span>، ۳۸ <span dir="ltr">Business Domain</span>، ۵۸۶ <span dir="ltr">Business Capability</span> و ۲۴۲ <span dir="ltr">Semantic API</span> را گزارش می‌کند.

<span dir="ltr">BIAN</span> برای ما سه کاربرد اصلی دارد:

1. **زبان مشترک:** مقایسهٔ اصطلاحات سازمان با واژگان شناخته‌شدهٔ بانکی
2. **<span dir="ltr">Completeness Check:</span>** کشف <span dir="ltr">Capability</span> یا مسئولیت جاافتاده
3. **<span dir="ltr">Reference Contract:</span>** استفاده از <span dir="ltr">Service Operation</span>، <span dir="ltr">Business Object</span> و <span dir="ltr">Semantic API</span> به‌عنوان ورودی طراحی

<span dir="ltr">BIAN</span> برای ما این کارها را انجام نمی‌دهد:

- مرز تیم‌ها را خودکار تعیین نمی‌کند.
- هر <span dir="ltr">Service Domain</span> را به <span dir="ltr">Microservice</span> تبدیل نمی‌کند.
- مقررات، <span dir="ltr">Product Model</span> و <span dir="ltr">Legacy Constraints</span> بانک ما را کشف نمی‌کند.
- <span dir="ltr">Transaction Boundary</span> و <span dir="ltr">Data Ownership</span> نهایی را بدون تحلیل محلی تعیین نمی‌کند.
- جای مصاحبه با خبرگان و <span dir="ltr">Event/Domain Discovery</span> را نمی‌گیرد.

### چرا <span dir="ltr">Service Domain</span> مساوی <span dir="ltr">Microservice</span> نیست؟

<span dir="ltr">Service Domain</span> در <span dir="ltr">BIAN</span> یک پارتیشن منطقی استانداردشده از مسئولیت بانکی است. <span dir="ltr">Deployment Boundary</span> علاوه بر مسئولیت منطقی به نیروهای دیگری وابسته است:

- <span dir="ltr">Transactional Cohesion</span>
- <span dir="ltr">Change Coupling</span>
- نیاز استقرار و مقیاس مستقل
- ساختار و بلوغ تیم
- <span dir="ltr">Latency</span> و <span dir="ltr">Availability</span>
- <span dir="ltr">Data Ownership</span>
- هزینهٔ عملیات توزیع‌شده

ممکن است چند <span dir="ltr">Service Domain</span> در یک <span dir="ltr">Module</span> یا <span dir="ltr">Service</span> عملیاتی شوند؛ یا یک مسئولیت بزرگ برای مقیاس و تیم به چند <span dir="ltr">Deployable Component</span> شکسته شود. این تصمیم باید <span dir="ltr">ADR</span> و <span dir="ltr">Verification</span> داشته باشد.

### روش درست استفاده در <span dir="ltr">Day 05</span>

1. ابتدا بر اساس کسب‌وکار خودمان <span dir="ltr">Capability Map L1</span> را می‌سازیم.
2. نام‌ها، <span dir="ltr">Scope</span> و <span dir="ltr">Owner</span> را نقد می‌کنیم.
3. سپس با <span dir="ltr">BIAN 14 Gap Check</span> می‌کنیم.
4. تفاوت‌ها را به سه گروه تقسیم می‌کنیم:
   - <span dir="ltr">Gap</span> واقعی
   - تفاوت نام/سطح تجزیه
   - <span dir="ltr">Capability</span> نامرتبط با <span dir="ltr">Scope</span>

اگر از <span dir="ltr">BIAN</span> شروع و همهٔ خانه‌ها را کپی کنیم، یک <span dir="ltr">Reference Landscape</span> داریم، نه معماری بانک خودمان.

---

## ۹. چهار نیروی طراحی که این هفته عمیق‌تر می‌شوند

### <span dir="ltr">Cohesion</span>

چیزهایی که به یک دلیل تغییر می‌کنند، بهتر است کنار هم باشند.

اگر منطق اعتبار حکم قضایی، محاسبهٔ ماندهٔ قابل برداشت و ثبت دفتر کل در یک کلاس باشد، آن کلاس سه دلیل مستقل برای تغییر دارد و <span dir="ltr">Cohesion</span> ضعیف است.

### <span dir="ltr">Coupling</span>

هرچه یک جزء برای کارکردن جزئیات بیشتری از دیگری بداند، تغییرها بیشتر منتشر می‌شوند.

<span dir="ltr">Deposits</span> که جدول <span dir="ltr">Legal Orders</span> را مستقیم <span dir="ltr">Query</span> می‌کند، به <span dir="ltr">Schema</span> و معنای داخلی <span dir="ltr">Context</span> حقوقی کاپل شده است.

### <span dir="ltr">Encapsulation</span>

<span dir="ltr">State</span> و رفتار مرتبط از مسیر <span dir="ltr">Interface</span> کنترل می‌شوند.

اگر هر <span dir="ltr">Service</span> بتواند ستون <span dir="ltr">blocked_amount</span> را <span dir="ltr">Update</span> کند، <span dir="ltr">Deposits</span> مانده و <span dir="ltr">Hold</span> را <span dir="ltr">Encapsulate</span> نکرده است.

### <span dir="ltr">Information Hiding</span>

تصمیم طراحیِ محتمل‌التغییر پشت <span dir="ltr">Boundary</span> پنهان می‌شود.

مصرف‌کنندهٔ <span dir="ltr">PlaceLegalHold</span> نباید بداند <span dir="ltr">Hold</span> در یک جدول، چند <span dir="ltr">Ledger Entry</span> یا <span dir="ltr">State Machine</span> داخلی نگهداری می‌شود. <span dir="ltr">Contract</span> باید معنای کسب‌وکاری را بدهد، نه روش پیاده‌سازی را.

روز چهارم این مفاهیم را روی یک طراحی عمداً بد باز می‌کنیم.

---

## ۱۰. هفت خطای رایج که از امروز ممنوع‌اند

### خطای ۱: شروع از جدول

«جدول <span dir="ltr">LOAN</span> داریم، پس <span dir="ltr">LoanService</span> می‌سازیم.»

جدول شاهد وضع موجود است، نه اثبات <span dir="ltr">Boundary.</span> یک جدول ممکن است چند مفهوم را مخلوط کرده باشد یا فقط <span dir="ltr">Projection</span> باشد.

### خطای ۲: شروع از چارت

«چون یک ادارهٔ چک داریم، <span dir="ltr">Check</span> یک <span dir="ltr">Bounded Context</span> مستقل است.»

ساختار سازمان می‌تواند سرنخ باشد، ولی ممکن است تاریخی، سیاسی یا مبتنی بر سامانهٔ <span dir="ltr">Legacy</span> باشد.

### خطای ۳: هر اسم کسب‌وکاری یک <span dir="ltr">Microservice</span>

داشتن نام دامینی شرط لازم برای مرز خوب است، نه شرط کافی برای استقرار مستقل.

### خطای ۴: اشتراک <span dir="ltr">Entity</span>

<span dir="ltr">CustomerEntity</span> مشترک میان همهٔ سرویس‌ها ظاهراً <span dir="ltr">Duplicate</span> را کم می‌کند، ولی مدل و <span dir="ltr">Release</span> را کاپل می‌کند. <span dir="ltr">Context</span>ها معمولاً به <span dir="ltr">Contract</span> و شناسهٔ مشترک نیاز دارند، نه <span dir="ltr">Entity</span> داخلی مشترک.

### خطای ۵: مالکیت مشترک

عبارت «<span dir="ltr">Lending</span> و <span dir="ltr">Accounting</span> هر دو مالک ماندهٔ تسهیلات‌اند» مسئولیت را مبهم می‌کند. باید نوع مانده را تفکیک کنیم: ماندهٔ عملیاتی اصل در <span dir="ltr">Lending</span>، ماندهٔ دفتر معین/کل در <span dir="ltr">Accounting</span> و <span dir="ltr">Projection</span> گزارش‌گری در <span dir="ltr">Data.</span>

### خطای ۶: <span dir="ltr">API</span> به‌جای <span dir="ltr">Capability</span>

<span dir="ltr">API</span> افتتاح حساب توانمندی نیست؛ <span dir="ltr">Interface</span> یک <span dir="ltr">Use Case</span> است که <span dir="ltr">Capability</span> مدیریت سپرده را محقق می‌کند.

### خطای ۷: <span dir="ltr">Event</span> به‌جای <span dir="ltr">Fact</span>

<span dir="ltr">Event</span> با نام مبهم <span dir="ltr">ProcessLoan</span> یا <span dir="ltr">DoAccounting</span> نمی‌گوید چه <span dir="ltr">Fact</span>ی رخ داده است. نام، مالک، زمان و معنای <span dir="ltr">Event</span> باید روشن باشد.

---

## ۱۱. تمرین هدایت‌شدهٔ ۱۵ دقیقه‌ای

پس از مطالعه، قابلیت «مسدودی قضایی سپرده» را در این جدول بنویس:

| مرحله | پاسخ تو | چرا؟ |
|---|---|---|
| <span dir="ltr">Capability</span> |  |  |
| <span dir="ltr">Domain/Subdomain</span> |  |  |
| <span dir="ltr">Bounded Context</span> |  |  |
| <span dir="ltr">Module/Service Candidate</span> |  |  |
| <span dir="ltr">Use Case</span> |  |  |
| <span dir="ltr">Command/Query</span> |  |  |
| <span dir="ltr">API/Event</span> |  |  |
| <span dir="ltr">Data Owner</span> |  |  |
| <span dir="ltr">Decision Owner</span> |  |  |

سپس سه کنترل انجام بده:

1. آیا جایی نام سامانه یا جدول را به‌جای مفهوم کسب‌وکاری گذاشته‌ای؟
2. آیا یک <span dir="ltr">Context</span> را به‌دلیل وجود یک <span dir="ltr">API</span>، <span dir="ltr">Microservice</span> فرض کرده‌ای؟
3. آیا برای یک داده یا تصمیم بیش از یک <span dir="ltr">Owner</span> نوشته‌ای؟

---

## ۱۲. جمع‌بندی فشرده

مدل ذهنی روز اول:


</div>

<div dir="ltr" align="left">

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

</div>

<div dir="rtl" align="right">


این عناصر مرتبط‌اند ولی مساوی نیستند و نگاشت یک‌به‌یک ندارند.

<span dir="ltr">BIAN</span> برای نام‌گذاری، <span dir="ltr">Gap Check</span> و <span dir="ltr">Reference Contract</span> ارزشمند است. <span dir="ltr">BIAN</span> جای طراحی محلی <span dir="ltr">Boundary</span>، <span dir="ltr">Ownership</span>، <span dir="ltr">Transaction</span> و <span dir="ltr">Team</span> را نمی‌گیرد.

## کار بعد از درس

1. به <span dir="ltr">Submission</span> برگرد.
2. پاسخ خام را پاک نکن.
3. بخش «بازنگری پس از درس» و جدول <span dir="ltr">Traceability</span> را کامل کن.
4. <span dir="ltr">Exit Ticket</span> را بدون مراجعه به متن پاسخ بده.
5. فایل را برای <span dir="ltr">Review</span> ارائه کن.

منابع رسمی و زمان مطالعه در [<span dir="ltr">References</span>](../references/README.md) آمده است.

</div>
