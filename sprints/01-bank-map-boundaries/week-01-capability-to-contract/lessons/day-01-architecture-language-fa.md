<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 01</bdi> — زبان مشترک معماری: از توانمندی بانک تا <bdi dir="ltr">Contract</bdi>

- زمان مطالعه: ۲۵ دقیقه
- سطح: میانی رو به پیشرفته
- مسئلهٔ نمونه: مسدودی قضایی سپرده
- خروجی: توانایی تشخیص سطح هر تصمیم و ساخت <bdi dir="ltr">Traceability Chain</bdi>

> اگر تمرین خط پایه را هنوز انجام نداده‌ای، این فایل را ببند. ابتدا ۱۲ دقیقه به
> [<bdi dir="ltr">Architecture Baseline</bdi>](../exercises/day-01-baseline.md) پاسخ بده. هدف ثبت مدل ذهنی واقعی تو پیش از آموزش است.

## ۱. امروز دقیقاً چه چیزی باید یاد بگیری؟

در پایان روز باید بتوانی:

1. <bdi dir="ltr">Business Architecture</bdi>، <bdi dir="ltr">Solution Architecture</bdi> و <bdi dir="ltr">Software Architecture</bdi> را از هم جدا کنی.
2. <bdi dir="ltr">Capability</bdi> را با <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Business Service</bdi>، <bdi dir="ltr">Application</bdi> و <bdi dir="ltr">API</bdi> اشتباه نگیری.
3. تفاوت <bdi dir="ltr">System</bdi>، <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Subdomain</bdi>، <bdi dir="ltr">Bounded Context</bdi>، <bdi dir="ltr">Module</bdi> و <bdi dir="ltr">Deployable Service</bdi> را توضیح بدهی.
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
6. <bdi dir="ltr">BIAN</bdi> را به‌عنوان <bdi dir="ltr">Reference Architecture</bdi> به‌کار ببری، نه دستگاه تولید خودکار <bdi dir="ltr">Microservice.</bdi>

موضوع امروز انتخاب <bdi dir="ltr">Kafka</bdi>، دیتابیس، <bdi dir="ltr">REST</bdi> یا معماری <bdi dir="ltr">Microservice</bdi> نیست. اگر پیش از روشن‌شدن <bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Ownership</bdi> سراغ این انتخاب‌ها برویم، ممکن است پاسخ فنی خوبی برای مسئلهٔ اشتباه بسازیم.

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
| قواعد حیاتی | چه <bdi dir="ltr">Invariant</bdi>هایی حتی هنگام خطا و هم‌زمانی نباید شکسته شوند؟ |
| تغییر ایمن | تغییر در یک قاعده تا کجا موج ایجاد می‌کند؟ |

<bdi dir="ltr">Diagram</bdi>، <bdi dir="ltr">Framework</bdi>، <bdi dir="ltr">Cloud</bdi> و <bdi dir="ltr">Microservice</bdi> می‌توانند ابزار یا نتیجهٔ تصمیم معماری باشند؛ خود معماری نیستند. دو تیم ممکن است <bdi dir="ltr">Diagram</bdi> مشابه داشته باشند، ولی یکی مالکیت دادهٔ روشن و <bdi dir="ltr">Contract</bdi> پایدار داشته باشد و دیگری از دیتابیس مشترک، دانش پنهان و <bdi dir="ltr">Release</bdi> هماهنگ رنج ببرد. ظاهر آن‌ها یکی است، معماری آن‌ها نه.

### سه نشانهٔ یک تصمیم معماری

یک تصمیم معمولاً معماری است اگر دست‌کم یکی از این ویژگی‌ها را داشته باشد:

- تغییرش پرهزینه، پرریسک یا سازمان‌گستر است.
- چند جزء یا تیم باید آن را رعایت کنند.
- روی صحت مالی، امنیت، دسترس‌پذیری یا امکان تحول اثر جدی دارد.

نام‌گذاری یک متغیر معمولاً تصمیم معماری نیست. اینکه ماندهٔ قابل برداشت سپرده را <bdi dir="ltr">Deposits</bdi> مالک باشد یا <bdi dir="ltr">Accounting</bdi>، تصمیم معماری و دامینی است؛ چون روی تراکنش، <bdi dir="ltr">Locking</bdi>، <bdi dir="ltr">API</bdi>، عملیات و پاسخ‌گویی سازمانی اثر می‌گذارد.

---

## ۳. سه سطحی که نباید در یک <bdi dir="ltr">Diagram</bdi> مخلوط شوند

### ۳.۱ <bdi dir="ltr">Business Architecture</bdi>

<bdi dir="ltr">Business Architecture</bdi> توضیح می‌دهد بانک برای تحقق راهبردش **چه توانمندی‌هایی** لازم دارد، چگونه ارزش تولید می‌کند و اطلاعات و مسئولیت‌های کلیدی چگونه سازمان می‌یابند.

واحدهای معمول تحلیل:

- <bdi dir="ltr">Goal</bdi> و <bdi dir="ltr">Outcome</bdi>
- <bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Capability Map</bdi>
- <bdi dir="ltr">Value Stream</bdi>
- <bdi dir="ltr">Business Information</bdi>
- <bdi dir="ltr">Stakeholder</bdi> و <bdi dir="ltr">Responsibility</bdi>

نمونه پرسش‌ها:

- بانک برای اعطای اعتبار چه توانمندی‌هایی لازم دارد؟
- کدام <bdi dir="ltr">Capability</bdi> برای بانک راهبردی و کدام عمومی است؟
- مالک بلوغ «مدیریت سپرده» چه نقشی است؟
- کدام <bdi dir="ltr">Capability</bdi>ها مانع عرضهٔ سریع محصول جدیدند؟

<bdi dir="ltr">Business Architecture</bdi> نباید به نسخهٔ <bdi dir="ltr">Spring Boot</bdi>، نام جدول یا تعداد <bdi dir="ltr">Pod</bdi>ها پاسخ بدهد.

### ۳.۲ <bdi dir="ltr">Solution Architecture</bdi>

<bdi dir="ltr">Solution Architecture</bdi> برای یک مسئله یا تغییر مشخص، همکاری چند <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Application</bdi>، <bdi dir="ltr">Data Store</bdi> و <bdi dir="ltr">Integration</bdi> را طراحی می‌کند.

واحدهای معمول تحلیل:

- <bdi dir="ltr">System/Context Boundary</bdi>
- <bdi dir="ltr">Component</bdi> یا <bdi dir="ltr">Service Candidate</bdi>
- <bdi dir="ltr">Data Flow</bdi> و <bdi dir="ltr">Contract</bdi>
- <bdi dir="ltr">Quality Attribute</bdi>
- <bdi dir="ltr">Integration</bdi>، <bdi dir="ltr">Security</bdi> و <bdi dir="ltr">Deployment Constraint</bdi>

نمونه پرسش‌ها:

- فرایند اعطای تسهیلات چگونه با <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">Accounting</bdi> همکاری می‌کند؟
- پاسخ گم‌شده پس از واریز موفق چگونه مدیریت می‌شود؟
- مرز تراکنش محلی کجاست؟
- چه داده‌ای <bdi dir="ltr">Snapshot</bdi> و چه داده‌ای <bdi dir="ltr">Reference</bdi> است؟

<bdi dir="ltr">Solution Architecture</bdi> پل میان مسئلهٔ کسب‌وکار و چند سیستم درگیر است.

### ۳.۳ <bdi dir="ltr">Software Architecture</bdi>

<bdi dir="ltr">Software Architecture</bdi> ساختار درونی یک نرم‌افزار یا سرویس را تعیین می‌کند.

واحدهای معمول تحلیل:

- <bdi dir="ltr">Package</bdi> و <bdi dir="ltr">Module</bdi>
- <bdi dir="ltr">Layer</bdi>، <bdi dir="ltr">Port</bdi> و <bdi dir="ltr">Adapter</bdi>
- <bdi dir="ltr">Aggregate</bdi> و <bdi dir="ltr">Repository</bdi>
- <bdi dir="ltr">Interface</bdi> و <bdi dir="ltr">Dependency Rule</bdi>
- <bdi dir="ltr">Thread</bdi>، <bdi dir="ltr">Transaction</bdi> و <bdi dir="ltr">Runtime Component</bdi>

نمونه پرسش‌ها:

- <bdi dir="ltr">Domain Model</bdi> به <bdi dir="ltr">Spring</bdi> یا <bdi dir="ltr">JPA</bdi> وابسته است؟
- <bdi dir="ltr">Use Case</bdi> اعطای تسهیلات در <bdi dir="ltr">Application Layer</bdi> چگونه اجرا می‌شود؟
- چه <bdi dir="ltr">Package</bdi>هایی <bdi dir="ltr">Public API</bdi> ماژول‌اند و چه <bdi dir="ltr">Package</bdi>هایی <bdi dir="ltr">Internal</bdi>؟
- <bdi dir="ltr">Invariant</bdi> قرارداد تسهیلات کجا آزمون می‌شود؟

### جدول کنترل

| گزاره | سطح غالب |
|---|---|
| بانک باید توانایی مدیریت مسدودی وجوه را داشته باشد. | <bdi dir="ltr">Business Architecture</bdi> |
| <bdi dir="ltr">Legal Orders</bdi> و <bdi dir="ltr">Deposits</bdi> با <bdi dir="ltr">Contract</bdi> مشخص همکاری می‌کنند. | <bdi dir="ltr">Solution Architecture</bdi> |
| کلاس <bdi dir="ltr">DepositAccount</bdi> فقط از متد <bdi dir="ltr">placeHold</bdi> تغییر می‌کند. | <bdi dir="ltr">Software Architecture</bdi> |
| نرخ خطای عملیات مسدودی باید کمتر از حد مصوب باشد. | <bdi dir="ltr">Solution/Runtime Architecture</bdi> |
| واحد حقوقی زیرمجموعهٔ کدام معاونت باشد؟ | <bdi dir="ltr">Operating Model</bdi> / <bdi dir="ltr">Organization Design</bdi> |

<bdi dir="ltr">Enterprise Architecture</bdi> چتر بزرگ‌تری است که <bdi dir="ltr">Business</bdi>، <bdi dir="ltr">Data</bdi>، <bdi dir="ltr">Application</bdi> و <bdi dir="ltr">Technology Architecture</bdi> را در سطح بنگاه هم‌راستا می‌کند. در این دوره به‌اندازه‌ای از آن استفاده می‌کنیم که تصمیم نرم‌افزاری از <bdi dir="ltr">Portfolio</bdi>، <bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Operating Model</bdi> جدا نیفتد.

---

## ۴. <bdi dir="ltr">Capability</bdi>؛ نقطهٔ شروع پایدار

### تعریف عملیاتی

<bdi dir="ltr">Business Capability</bdi> یعنی **توان سازمان برای انجام یک کار کسب‌وکاری و تولید یک <bdi dir="ltr">Outcome</bdi>**.

<bdi dir="ltr">Capability</bdi> می‌گوید «چه کاری باید بتوانیم انجام دهیم؟» و عمداً دربارهٔ اینکه کدام واحد، فرایند، نرم‌افزار یا فناوری آن را انجام می‌دهد سکوت می‌کند.

نمونه‌های مناسب:

- مدیریت رابطه با مشتری
- مدیریت محصولات و شرایط
- نگهداری سپرده
- مدیریت اعتبار و تسهیلات
- جابه‌جایی و تسویهٔ وجوه
- ثبت و کنترل مالی
- پایش تقلب

نمونه‌های نامناسب:

- اجرای فرایند افتتاح حساب در <bdi dir="ltr">BPM</bdi>
- سامانهٔ سپرده
- تیم تسهیلات یک
- <bdi dir="ltr">API</bdi> واریز
- <bdi dir="ltr">Kafka Event Processing</bdi>

موارد نامناسب یا <bdi dir="ltr">Process</bdi> هستند، یا <bdi dir="ltr">Application/Organization/Technology.</bdi> ممکن است همگی برای تحقق <bdi dir="ltr">Capability</bdi> لازم باشند، ولی خود <bdi dir="ltr">Capability</bdi> نیستند.

### <bdi dir="ltr">Capability</bdi> در برابر <bdi dir="ltr">Process</bdi>

فرض کن بانک <bdi dir="ltr">Capability</bdi> «مدیریت مسدودی وجوه» را دارد.

این <bdi dir="ltr">Capability</bdi> ممکن است با <bdi dir="ltr">Process</bdi>های مختلف اجرا شود:

- مسدودی قضایی با دریافت نامه و تأیید حقوقی
- مسدودی وثیقه‌ای هنگام اعطای تسهیلات
- <bdi dir="ltr">Hold</bdi> کوتاه‌مدت هنگام پرداخت کارت
- مسدودی سیستمی به‌دلیل کنترل تقلب

<bdi dir="ltr">Capability</bdi> نسبتاً پایدار است؛ <bdi dir="ltr">Process</bdi> با مقررات، کانال و اتوماسیون تغییر می‌کند.

### <bdi dir="ltr">Capability</bdi> در برابر <bdi dir="ltr">Business Service</bdi>

<bdi dir="ltr">Capability</bdi> توان داخلی بانک است. <bdi dir="ltr">Business Service</bdi> شکل ارزش قابل‌مصرفی است که از آن توان ارائه می‌شود.

مثلاً:

- <bdi dir="ltr">Capability:</bdi> مدیریت پرداخت
- <bdi dir="ltr">Business Service:</bdi> انتقال وجه داخلی برای مشتری

یک <bdi dir="ltr">Capability</bdi> می‌تواند چند <bdi dir="ltr">Business Service</bdi> عرضه کند و یک <bdi dir="ltr">Business Service</bdi> ممکن است به چند <bdi dir="ltr">Capability</bdi> وابسته باشد.

### <bdi dir="ltr">Capability</bdi> در برابر <bdi dir="ltr">Application</bdi>

ممکن است امروز سه سامانه بخشی از «مدیریت مشتری» را انجام دهند و فردا در یک <bdi dir="ltr">Platform</bdi> ادغام شوند. <bdi dir="ltr">Capability</bdi> باقی است، <bdi dir="ltr">Application Landscape</bdi> تغییر می‌کند.

اگر <bdi dir="ltr">Capability Map</bdi> را از روی فهرست سامانه‌ها بسازیم، وضع موجود را با ماهیت کسب‌وکار اشتباه گرفته‌ایم و <bdi dir="ltr">Legacy</bdi> را به مدل هدف تحمیل کرده‌ایم.

### آزمون شش‌گانهٔ <bdi dir="ltr">Capability</bdi>

برای هر عنوان پیشنهادی بپرس:

1. آیا می‌گوید بانک چه کاری می‌تواند انجام دهد؟
2. آیا مستقل از فناوری و <bdi dir="ltr">Vendor</bdi> است؟
3. آیا مستقل از چارت سازمانی است؟
4. آیا از <bdi dir="ltr">Process</bdi>های اجرای آن پایدارتر است؟
5. آیا <bdi dir="ltr">Outcome</bdi> یا <bdi dir="ltr">KPI</bdi> برای آن قابل تصور است؟
6. آیا می‌توان <bdi dir="ltr">Owner</bdi> کسب‌وکاری برای بلوغ آن تعیین کرد؟

پاسخ منفی به چند سؤال نشانهٔ آن است که عنوان احتمالاً <bdi dir="ltr">Capability</bdi> نیست.

---

## ۵. از <bdi dir="ltr">Problem Space</bdi> تا <bdi dir="ltr">Solution Space</bdi>

بزرگ‌ترین خطای معماری سازمانی این است که عناصر سطوح مختلف را هم‌معنا فرض کنیم. برای جلوگیری از آن، هر مفهوم را دقیق در جای خود می‌گذاریم.

### <bdi dir="ltr">System</bdi>

<bdi dir="ltr">System</bdi> مجموعه‌ای از اجزای مرتبط با یک هدف و <bdi dir="ltr">Boundary</bdi> مشخص است. تعریف <bdi dir="ltr">System</bdi> به «<bdi dir="ltr">System of Interest</bdi>» وابسته است.

- کل بانک می‌تواند یک <bdi dir="ltr">System</bdi> باشد.
- <bdi dir="ltr">Core Banking Platform</bdi> می‌تواند <bdi dir="ltr">System</bdi> باشد.
- سرویس <bdi dir="ltr">Deposits</bdi> نیز در یک بررسی محدود می‌تواند <bdi dir="ltr">System</bdi> باشد.

پس «<bdi dir="ltr">System</bdi>» به‌تنهایی اندازه یا نوع معماری را تعیین نمی‌کند؛ <bdi dir="ltr">Boundary</bdi> بررسی را مشخص می‌کند.

### <bdi dir="ltr">Domain</bdi>

<bdi dir="ltr">Domain</bdi> حوزهٔ مسئله، دانش و فعالیتی است که می‌خواهیم برایش مدل بسازیم؛ مانند <bdi dir="ltr">Lending</bdi> یا <bdi dir="ltr">Payments.</bdi>

<bdi dir="ltr">Domain</bdi> به مسئله تعلق دارد، نه به <bdi dir="ltr">Repository</bdi> کد. ممکن است امروز هیچ سامانهٔ مناسبی برای <bdi dir="ltr">Domain</bdi> وجود نداشته باشد، ولی <bdi dir="ltr">Domain</bdi> همچنان واقعی است.

### <bdi dir="ltr">Subdomain</bdi>

<bdi dir="ltr">Domain</bdi> بزرگ به <bdi dir="ltr">Subdomain</bdi>های متمایز شکسته می‌شود. <bdi dir="ltr">Lending</bdi> می‌تواند شامل بخش‌هایی مانند:

- <bdi dir="ltr">Loan Origination</bdi>
- <bdi dir="ltr">Credit Decision</bdi>
- <bdi dir="ltr">Loan Servicing</bdi>
- <bdi dir="ltr">Repayment</bdi>
- <bdi dir="ltr">Delinquency Management</bdi>

باشد. مرز دقیق برای هر بانک با مدل کسب‌وکار، مقررات و تمایز راهبردی آن تعیین می‌شود؛ فهرست آماده جای <bdi dir="ltr">Discovery</bdi> را نمی‌گیرد.

### <bdi dir="ltr">Bounded Context</bdi>

<bdi dir="ltr">Bounded Context</bdi> مرزی است که درون آن یک <bdi dir="ltr">Model</bdi> و <bdi dir="ltr">Ubiquitous Language</bdi> مشخص معتبر است.

واژهٔ <bdi dir="ltr">Account</bdi> مثال مهمی است:

- در <bdi dir="ltr">Deposits:</bdi> قرارداد نگهداری وجوه و ماندهٔ عملیاتی
- در <bdi dir="ltr">Lending:</bdi> موقعیت بدهی و برنامهٔ بازپرداخت
- در <bdi dir="ltr">Accounting:</bdi> حساب دفتر کل یا معین
- در <bdi dir="ltr">IAM:</bdi> حساب کاربری

اگر همهٔ این معناها را در یک مدل مشترک <bdi dir="ltr">Account</bdi> ادغام کنیم، مدل مبهم و تغییرها کاپل می‌شوند. <bdi dir="ltr">Bounded Context</bdi> اجازه می‌دهد هر معنا در مرز خودش دقیق بماند و ترجمه در <bdi dir="ltr">Contract</bdi> رخ دهد.

### <bdi dir="ltr">Module</bdi>

<bdi dir="ltr">Module</bdi> واحد منطقی کد با:

- <bdi dir="ltr">API</bdi> آشکار
- جزئیات <bdi dir="ltr">Internal</bdi>
- مسئولیت منسجم
- <bdi dir="ltr">Dependency</bdi> کنترل‌شده

است. <bdi dir="ltr">Module</bdi> می‌تواند همراه چند <bdi dir="ltr">Module</bdi> دیگر در یک <bdi dir="ltr">Process</bdi> و یک <bdi dir="ltr">Deployment</bdi> اجرا شود.

### <bdi dir="ltr">Deployable Service</bdi>

<bdi dir="ltr">Deployable Service</bdi> واحد <bdi dir="ltr">Runtime</bdi> قابل استقرار است. وقتی آن را <bdi dir="ltr">Microservice</bdi> می‌نامیم، معمولاً انتظار داریم:

- <bdi dir="ltr">Lifecycle</bdi> استقرار مستقل داشته باشد.
- <bdi dir="ltr">Boundary</bdi> مسئولیت روشن باشد.
- داده و تغییرات <bdi dir="ltr">Schema</bdi> تحت مالکیت آن باشد.
- خرابی و عملیات مستقل مدیریت شود.
- هزینهٔ <bdi dir="ltr">Network</bdi>، <bdi dir="ltr">Observability</bdi> و <bdi dir="ltr">Consistency</bdi> توزیع‌شده پذیرفته شود.

هر <bdi dir="ltr">Module</bdi> خوب <bdi dir="ltr">Microservice</bdi> نیست. ابتدا <bdi dir="ltr">Module</bdi> خوب می‌سازیم؛ فقط اگر محرک‌های کسب‌وکاری و عملیاتی کافی وجود داشتند، استخراج فیزیکی را بررسی می‌کنیم.

### <bdi dir="ltr">API</bdi> و <bdi dir="ltr">Event</bdi>

<bdi dir="ltr">API</bdi> و <bdi dir="ltr">Event</bdi> شکل <bdi dir="ltr">Contract</bdi> در <bdi dir="ltr">Boundary</bdi> هستند، نه جایگزین <bdi dir="ltr">Boundary.</bdi>

- <bdi dir="ltr">Command</bdi> قصد انجام تغییر دارد: <bdi dir="ltr">PlaceLegalHold</bdi>
- <bdi dir="ltr">Query</bdi> اطلاعات می‌خواهد: <bdi dir="ltr">GetAvailableBalance</bdi>
- <bdi dir="ltr">Event</bdi> وقوع <bdi dir="ltr">Fact</bdi> را اعلام می‌کند: <bdi dir="ltr">LegalHoldPlaced</bdi>

نام <bdi dir="ltr">Event</bdi> باید رخداد گذشته را بگوید. <bdi dir="ltr">LoanGrantRequest</bdi> یک درخواست است، نه <bdi dir="ltr">Event. LoanGranted</bdi> یک <bdi dir="ltr">Fact</bdi> رخ‌داده است.

---

## ۶. زنجیرهٔ <bdi dir="ltr">Capability</bdi> تا <bdi dir="ltr">Contract</bdi>

این زنجیره ابزار <bdi dir="ltr">Traceability</bdi> است:


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
| <bdi dir="ltr">Capability</bdi> | بانک چه کاری باید بتواند انجام دهد؟ | نام‌گذاری با سامانه یا واحد |
| <bdi dir="ltr">Domain/Subdomain</bdi> | این دانش و قواعد متعلق به کدام <bdi dir="ltr">Problem Space</bdi> است؟ | شروع از جدول |
| <bdi dir="ltr">Bounded Context</bdi> | این مدل و واژه‌ها در کدام مرز معتبرند؟ | مدل مشترک عظیم |
| <bdi dir="ltr">Module/Service Candidate</bdi> | کدام واحد منطقی تغییر و مسئولیت را محصور می‌کند؟ | <bdi dir="ltr">Microservice</bdi> پیش‌فرض |
| <bdi dir="ltr">Use Case</bdi> | چه قصد یا <bdi dir="ltr">Outcome</bdi> مشخصی اجرا می‌شود؟ | <bdi dir="ltr">CRUD</bdi> به‌جای رفتار |
| <bdi dir="ltr">Command/Query</bdi> | مصرف‌کننده چه قصدی را بیان می‌کند؟ | نام فنی و مبهم |
| <bdi dir="ltr">API/Event</bdi> | <bdi dir="ltr">Contract</bdi> بیرونی چگونه معنا، خطا و <bdi dir="ltr">Version</bdi> را منتقل می‌کند؟ | افشای <bdi dir="ltr">Entity</bdi> و <bdi dir="ltr">Schema</bdi> داخلی |

### این نگاشت یک‌به‌یک نیست

قواعد مهم:

- یک <bdi dir="ltr">Capability</bdi> می‌تواند به چند <bdi dir="ltr">Domain</bdi> وابسته باشد.
- یک <bdi dir="ltr">Domain</bdi> می‌تواند چند <bdi dir="ltr">Subdomain</bdi> و چند <bdi dir="ltr">Bounded Context</bdi> داشته باشد.
- یک <bdi dir="ltr">Bounded Context</bdi> می‌تواند ابتدا یک <bdi dir="ltr">Module</bdi> باشد و بعداً یک یا چند <bdi dir="ltr">Deployable Service</bdi> شود.
- یک <bdi dir="ltr">Service</bdi> می‌تواند چند <bdi dir="ltr">Use Case</bdi> عرضه کند.
- یک <bdi dir="ltr">Use Case</bdi> می‌تواند یک <bdi dir="ltr">Command</bdi> ورودی و چند <bdi dir="ltr">Event</bdi> خروجی داشته باشد.
- یک <bdi dir="ltr">API</bdi> می‌تواند بخشی از چند جریان کسب‌وکاری باشد.

هدف زنجیره این نیست که برای هر <bdi dir="ltr">Capability</bdi> یک <bdi dir="ltr">Microservice</bdi> بسازیم. هدف این است که هر جزء نرم‌افزاری دلیل کسب‌وکاری و مالکیت قابل ردیابی داشته باشد.

---

## ۷. مثال هدایت‌شده: مسدودی قضایی سپرده

برای آلوده‌نکردن تمرین خط پایه، مثال درس را از سناریوی دیگری می‌گیریم.

### صورت مسئله

بانک یک حکم معتبر دریافت می‌کند که باید مبلغ معینی از سپردهٔ مشتری مسدود شود. وضعیت حکم ممکن است بعداً لغو یا اصلاح شود. ماندهٔ قابل برداشت باید بلافاصله اثر <bdi dir="ltr">Hold</bdi> را نشان دهد.

### گام اول: <bdi dir="ltr">Capability</bdi>

حداقل دو <bdi dir="ltr">Capability</bdi> قابل تشخیص است:

1. مدیریت دستورهای حقوقی/نظارتی
2. مدیریت محدودیت و <bdi dir="ltr">Hold</bdi> وجوه سپرده

«سامانه نامه‌های قضایی» <bdi dir="ltr">Capability</bdi> نیست؛ نام راه‌حل یا <bdi dir="ltr">Application</bdi> است.

### گام دوم: <bdi dir="ltr">Domain/Subdomain</bdi>

- <bdi dir="ltr">Legal/Compliance:</bdi> اعتبار، مرجع، دامنه و چرخهٔ عمر حکم
- <bdi dir="ltr">Deposits:</bdi> اعمال و رفع <bdi dir="ltr">Hold</bdi> و محاسبهٔ ماندهٔ قابل برداشت

ممکن است <bdi dir="ltr">Customer/Party</bdi> برای تطبیق هویت مشارکت کند، ولی مالک حکم یا <bdi dir="ltr">Hold</bdi> نمی‌شود.

### گام سوم: <bdi dir="ltr">Bounded Context</bdi>

- <bdi dir="ltr">Legal Orders Context</bdi>
- <bdi dir="ltr">Deposit Accounts Context</bdi>

واژهٔ <bdi dir="ltr">Restriction</bdi> در <bdi dir="ltr">Context</bdi> حقوقی به الزام قانونی اشاره دارد؛ <bdi dir="ltr">Hold</bdi> در <bdi dir="ltr">Deposits</bdi> یک وضعیت عملیاتی روی حساب است. این دو مرتبط‌اند ولی یک مدل نیستند.

### گام چهارم: <bdi dir="ltr">Module/Service Candidate</bdi>

در شروع <bdi dir="ltr">Lab:</bdi>

- <bdi dir="ltr">legalorders module</bdi>
- <bdi dir="ltr">deposits module</bdi>

هر دو می‌توانند در یک <bdi dir="ltr">Modular Monolith</bdi> باشند. هنوز دلیل کافی برای دو <bdi dir="ltr">Microservice</bdi> مستقل نداریم.

### گام پنجم: <bdi dir="ltr">Use Case</bdi>

- <bdi dir="ltr">RegisterLegalOrder</bdi>
- <bdi dir="ltr">PlaceLegalHold</bdi>
- <bdi dir="ltr">RevokeLegalOrder</bdi>
- <bdi dir="ltr">ReleaseLegalHold</bdi>

### گام ششم: <bdi dir="ltr">Command/Query</bdi>

<bdi dir="ltr">Legal Orders</bdi> پس از تأیید حکم، قصد اعمال <bdi dir="ltr">Hold</bdi> را با <bdi dir="ltr">Command</bdi> بیان می‌کند. <bdi dir="ltr">Contract</bdi> باید دست‌کم مرجع حکم، حساب هدف، مبلغ/دامنه، تاریخ مؤثر و شناسهٔ <bdi dir="ltr">Idempotency</bdi> را حمل کند.

<bdi dir="ltr">Deposits</bdi> تصمیم می‌گیرد آیا عملیات با وضعیت حساب و قواعد خودش سازگار است. <bdi dir="ltr">Legal Orders</bdi> نباید مستقیم جدول <bdi dir="ltr">Hold</bdi> یا ماندهٔ <bdi dir="ltr">Deposits</bdi> را تغییر دهد.

### گام هفتم: <bdi dir="ltr">API/Event</bdi>

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


نام <bdi dir="ltr">Transport</bdi> هنوز تعیین نشده است. <bdi dir="ltr">Command</bdi> می‌تواند از طریق <bdi dir="ltr">API</bdi> همگام یا پیام پردازش شود. انتخاب آن به نیاز <bdi dir="ltr">Latency</bdi>، <bdi dir="ltr">Coupling</bdi>، <bdi dir="ltr">Failure Handling</bdi> و فرایند کسب‌وکاری بستگی دارد.

### مالکیت

| داده/تصمیم | مالک |
|---|---|
| اعتبار و چرخهٔ عمر حکم | <bdi dir="ltr">Legal Orders</bdi> |
| نگاشت حکم به حساب هدف | نیازمند <bdi dir="ltr">Contract</bdi> روشن؛ تصمیم مشترک مبهم ممنوع |
| <bdi dir="ltr">Hold</bdi> عملیاتی روی سپرده | <bdi dir="ltr">Deposits</bdi> |
| ماندهٔ قابل برداشت | <bdi dir="ltr">Deposits</bdi> |
| ثبت مالی ناشی از جابه‌جایی وجه | <bdi dir="ltr">Accounting</bdi> |

خود <bdi dir="ltr">Hold</bdi> الزاماً جابه‌جایی وجه و <bdi dir="ltr">Journal Entry</bdi> ایجاد نمی‌کند. ممکن است گزارش آماری یا ثبت کنترلی لازم باشد، اما <bdi dir="ltr">Accounting</bdi> نباید برای نمایش ماندهٔ قابل برداشت، مالک <bdi dir="ltr">Hold</bdi> شود.

این مثال نشان می‌دهد «مالک <bdi dir="ltr">Trigger</bdi>»، «مالک تصمیم» و «مالک <bdi dir="ltr">State</bdi>» همیشه یک <bdi dir="ltr">Context</bdi> نیستند.

---

## ۸. <bdi dir="ltr">BIAN</bdi> دقیقاً چه نقشی دارد؟

<bdi dir="ltr">BIAN</bdi> یک <bdi dir="ltr">Reference Architecture</bdi> تخصصی صنعت بانکداری است. در نسخهٔ 14.0، <bdi dir="ltr">Release Notes</bdi> رسمی ۳۲۲ <bdi dir="ltr">Service Domain</bdi>، ۳۸ <bdi dir="ltr">Business Domain</bdi>، ۵۸۶ <bdi dir="ltr">Business Capability</bdi> و ۲۴۲ <bdi dir="ltr">Semantic API</bdi> را گزارش می‌کند.

<bdi dir="ltr">BIAN</bdi> برای ما سه کاربرد اصلی دارد:

1. **زبان مشترک:** مقایسهٔ اصطلاحات سازمان با واژگان شناخته‌شدهٔ بانکی
2. **<bdi dir="ltr">Completeness Check:</bdi>** کشف <bdi dir="ltr">Capability</bdi> یا مسئولیت جاافتاده
3. **<bdi dir="ltr">Reference Contract:</bdi>** استفاده از <bdi dir="ltr">Service Operation</bdi>، <bdi dir="ltr">Business Object</bdi> و <bdi dir="ltr">Semantic API</bdi> به‌عنوان ورودی طراحی

<bdi dir="ltr">BIAN</bdi> برای ما این کارها را انجام نمی‌دهد:

- مرز تیم‌ها را خودکار تعیین نمی‌کند.
- هر <bdi dir="ltr">Service Domain</bdi> را به <bdi dir="ltr">Microservice</bdi> تبدیل نمی‌کند.
- مقررات، <bdi dir="ltr">Product Model</bdi> و <bdi dir="ltr">Legacy Constraints</bdi> بانک ما را کشف نمی‌کند.
- <bdi dir="ltr">Transaction Boundary</bdi> و <bdi dir="ltr">Data Ownership</bdi> نهایی را بدون تحلیل محلی تعیین نمی‌کند.
- جای مصاحبه با خبرگان و <bdi dir="ltr">Event/Domain Discovery</bdi> را نمی‌گیرد.

### چرا <bdi dir="ltr">Service Domain</bdi> مساوی <bdi dir="ltr">Microservice</bdi> نیست؟

<bdi dir="ltr">Service Domain</bdi> در <bdi dir="ltr">BIAN</bdi> یک پارتیشن منطقی استانداردشده از مسئولیت بانکی است. <bdi dir="ltr">Deployment Boundary</bdi> علاوه بر مسئولیت منطقی به نیروهای دیگری وابسته است:

- <bdi dir="ltr">Transactional Cohesion</bdi>
- <bdi dir="ltr">Change Coupling</bdi>
- نیاز استقرار و مقیاس مستقل
- ساختار و بلوغ تیم
- <bdi dir="ltr">Latency</bdi> و <bdi dir="ltr">Availability</bdi>
- <bdi dir="ltr">Data Ownership</bdi>
- هزینهٔ عملیات توزیع‌شده

ممکن است چند <bdi dir="ltr">Service Domain</bdi> در یک <bdi dir="ltr">Module</bdi> یا <bdi dir="ltr">Service</bdi> عملیاتی شوند؛ یا یک مسئولیت بزرگ برای مقیاس و تیم به چند <bdi dir="ltr">Deployable Component</bdi> شکسته شود. این تصمیم باید <bdi dir="ltr">ADR</bdi> و <bdi dir="ltr">Verification</bdi> داشته باشد.

### روش درست استفاده در <bdi dir="ltr">Day 05</bdi>

1. ابتدا بر اساس کسب‌وکار خودمان <bdi dir="ltr">Capability Map L1</bdi> را می‌سازیم.
2. نام‌ها، <bdi dir="ltr">Scope</bdi> و <bdi dir="ltr">Owner</bdi> را نقد می‌کنیم.
3. سپس با <bdi dir="ltr">BIAN 14 Gap Check</bdi> می‌کنیم.
4. تفاوت‌ها را به سه گروه تقسیم می‌کنیم:
   - <bdi dir="ltr">Gap</bdi> واقعی
   - تفاوت نام/سطح تجزیه
   - <bdi dir="ltr">Capability</bdi> نامرتبط با <bdi dir="ltr">Scope</bdi>

اگر از <bdi dir="ltr">BIAN</bdi> شروع و همهٔ خانه‌ها را کپی کنیم، یک <bdi dir="ltr">Reference Landscape</bdi> داریم، نه معماری بانک خودمان.

---

## ۹. چهار نیروی طراحی که این هفته عمیق‌تر می‌شوند

### <bdi dir="ltr">Cohesion</bdi>

چیزهایی که به یک دلیل تغییر می‌کنند، بهتر است کنار هم باشند.

اگر منطق اعتبار حکم قضایی، محاسبهٔ ماندهٔ قابل برداشت و ثبت دفتر کل در یک کلاس باشد، آن کلاس سه دلیل مستقل برای تغییر دارد و <bdi dir="ltr">Cohesion</bdi> ضعیف است.

### <bdi dir="ltr">Coupling</bdi>

هرچه یک جزء برای کارکردن جزئیات بیشتری از دیگری بداند، تغییرها بیشتر منتشر می‌شوند.

<bdi dir="ltr">Deposits</bdi> که جدول <bdi dir="ltr">Legal Orders</bdi> را مستقیم <bdi dir="ltr">Query</bdi> می‌کند، به <bdi dir="ltr">Schema</bdi> و معنای داخلی <bdi dir="ltr">Context</bdi> حقوقی کاپل شده است.

### <bdi dir="ltr">Encapsulation</bdi>

<bdi dir="ltr">State</bdi> و رفتار مرتبط از مسیر <bdi dir="ltr">Interface</bdi> کنترل می‌شوند.

اگر هر <bdi dir="ltr">Service</bdi> بتواند ستون <bdi dir="ltr">blocked_amount</bdi> را <bdi dir="ltr">Update</bdi> کند، <bdi dir="ltr">Deposits</bdi> مانده و <bdi dir="ltr">Hold</bdi> را <bdi dir="ltr">Encapsulate</bdi> نکرده است.

### <bdi dir="ltr">Information Hiding</bdi>

تصمیم طراحیِ محتمل‌التغییر پشت <bdi dir="ltr">Boundary</bdi> پنهان می‌شود.

مصرف‌کنندهٔ <bdi dir="ltr">PlaceLegalHold</bdi> نباید بداند <bdi dir="ltr">Hold</bdi> در یک جدول، چند <bdi dir="ltr">Ledger Entry</bdi> یا <bdi dir="ltr">State Machine</bdi> داخلی نگهداری می‌شود. <bdi dir="ltr">Contract</bdi> باید معنای کسب‌وکاری را بدهد، نه روش پیاده‌سازی را.

روز چهارم این مفاهیم را روی یک طراحی عمداً بد باز می‌کنیم.

---

## ۱۰. هفت خطای رایج که از امروز ممنوع‌اند

### خطای ۱: شروع از جدول

«جدول <bdi dir="ltr">LOAN</bdi> داریم، پس <bdi dir="ltr">LoanService</bdi> می‌سازیم.»

جدول شاهد وضع موجود است، نه اثبات <bdi dir="ltr">Boundary.</bdi> یک جدول ممکن است چند مفهوم را مخلوط کرده باشد یا فقط <bdi dir="ltr">Projection</bdi> باشد.

### خطای ۲: شروع از چارت

«چون یک ادارهٔ چک داریم، <bdi dir="ltr">Check</bdi> یک <bdi dir="ltr">Bounded Context</bdi> مستقل است.»

ساختار سازمان می‌تواند سرنخ باشد، ولی ممکن است تاریخی، سیاسی یا مبتنی بر سامانهٔ <bdi dir="ltr">Legacy</bdi> باشد.

### خطای ۳: هر اسم کسب‌وکاری یک <bdi dir="ltr">Microservice</bdi>

داشتن نام دامینی شرط لازم برای مرز خوب است، نه شرط کافی برای استقرار مستقل.

### خطای ۴: اشتراک <bdi dir="ltr">Entity</bdi>

<bdi dir="ltr">CustomerEntity</bdi> مشترک میان همهٔ سرویس‌ها ظاهراً <bdi dir="ltr">Duplicate</bdi> را کم می‌کند، ولی مدل و <bdi dir="ltr">Release</bdi> را کاپل می‌کند. <bdi dir="ltr">Context</bdi>ها معمولاً به <bdi dir="ltr">Contract</bdi> و شناسهٔ مشترک نیاز دارند، نه <bdi dir="ltr">Entity</bdi> داخلی مشترک.

### خطای ۵: مالکیت مشترک

عبارت «<bdi dir="ltr">Lending</bdi> و <bdi dir="ltr">Accounting</bdi> هر دو مالک ماندهٔ تسهیلات‌اند» مسئولیت را مبهم می‌کند. باید نوع مانده را تفکیک کنیم: ماندهٔ عملیاتی اصل در <bdi dir="ltr">Lending</bdi>، ماندهٔ دفتر معین/کل در <bdi dir="ltr">Accounting</bdi> و <bdi dir="ltr">Projection</bdi> گزارش‌گری در <bdi dir="ltr">Data.</bdi>

### خطای ۶: <bdi dir="ltr">API</bdi> به‌جای <bdi dir="ltr">Capability</bdi>

<bdi dir="ltr">API</bdi> افتتاح حساب توانمندی نیست؛ <bdi dir="ltr">Interface</bdi> یک <bdi dir="ltr">Use Case</bdi> است که <bdi dir="ltr">Capability</bdi> مدیریت سپرده را محقق می‌کند.

### خطای ۷: <bdi dir="ltr">Event</bdi> به‌جای <bdi dir="ltr">Fact</bdi>

<bdi dir="ltr">Event</bdi> با نام مبهم <bdi dir="ltr">ProcessLoan</bdi> یا <bdi dir="ltr">DoAccounting</bdi> نمی‌گوید چه <bdi dir="ltr">Fact</bdi>ی رخ داده است. نام، مالک، زمان و معنای <bdi dir="ltr">Event</bdi> باید روشن باشد.

---

## ۱۱. تمرین هدایت‌شدهٔ ۱۵ دقیقه‌ای

پس از مطالعه، قابلیت «مسدودی قضایی سپرده» را در این جدول بنویس:

| مرحله | پاسخ تو | چرا؟ |
|---|---|---|
| <bdi dir="ltr">Capability</bdi> |  |  |
| <bdi dir="ltr">Domain/Subdomain</bdi> |  |  |
| <bdi dir="ltr">Bounded Context</bdi> |  |  |
| <bdi dir="ltr">Module/Service Candidate</bdi> |  |  |
| <bdi dir="ltr">Use Case</bdi> |  |  |
| <bdi dir="ltr">Command/Query</bdi> |  |  |
| <bdi dir="ltr">API/Event</bdi> |  |  |
| <bdi dir="ltr">Data Owner</bdi> |  |  |
| <bdi dir="ltr">Decision Owner</bdi> |  |  |

سپس سه کنترل انجام بده:

1. آیا جایی نام سامانه یا جدول را به‌جای مفهوم کسب‌وکاری گذاشته‌ای؟
2. آیا یک <bdi dir="ltr">Context</bdi> را به‌دلیل وجود یک <bdi dir="ltr">API</bdi>، <bdi dir="ltr">Microservice</bdi> فرض کرده‌ای؟
3. آیا برای یک داده یا تصمیم بیش از یک <bdi dir="ltr">Owner</bdi> نوشته‌ای؟

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

<bdi dir="ltr">BIAN</bdi> برای نام‌گذاری، <bdi dir="ltr">Gap Check</bdi> و <bdi dir="ltr">Reference Contract</bdi> ارزشمند است. <bdi dir="ltr">BIAN</bdi> جای طراحی محلی <bdi dir="ltr">Boundary</bdi>، <bdi dir="ltr">Ownership</bdi>، <bdi dir="ltr">Transaction</bdi> و <bdi dir="ltr">Team</bdi> را نمی‌گیرد.

## کار بعد از درس

1. به <bdi dir="ltr">Submission</bdi> برگرد.
2. پاسخ خام را پاک نکن.
3. بخش «بازنگری پس از درس» و جدول <bdi dir="ltr">Traceability</bdi> را کامل کن.
4. <bdi dir="ltr">Exit Ticket</bdi> را بدون مراجعه به متن پاسخ بده.
5. فایل را برای <bdi dir="ltr">Review</bdi> ارائه کن.

منابع رسمی و زمان مطالعه در [<bdi dir="ltr">References</bdi>](../references/README.md) آمده است.

</div>
