<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 01</bdi> — <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Subdomain</bdi> و اهمیت راهبردی

- <bdi dir="ltr">Day budget: 50 minutes including exercise and exit ticket</bdi>
- <bdi dir="ltr">Level: intermediate</bdi>
- <bdi dir="ltr">Output: Subdomain Matrix v0.1</bdi>
- <bdi dir="ltr">Banking case:</bdi> زنجیرهٔ اعتبار از طراحی محصول تا وصول

## 1. هدف قابل سنجش

در پایان این درس باید بتوانی:

1. <bdi dir="ltr">Domain</bdi> را از <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Application</bdi>، <bdi dir="ltr">Department</bdi> و <bdi dir="ltr">Bounded Context</bdi> جدا کنی.
2. یک حوزهٔ بزرگ بانکی را بر اساس دانش، قواعد و <bdi dir="ltr">Outcome</bdi> به <bdi dir="ltr">Subdomain</bdi>های معنادار بشکنی.
3. <bdi dir="ltr">Core</bdi>، <bdi dir="ltr">Supporting</bdi> و <bdi dir="ltr">Generic</bdi> را با شواهد راهبردی طبقه‌بندی کنی.
4. توضیح بدهی چرا این طبقه‌بندی برای دو بانک یا دو مقطع زمانی می‌تواند متفاوت باشد.
5. پیامد طبقه‌بندی را برای سرمایه‌گذاری، تیم، <bdi dir="ltr">Build/Buy</bdi> و کیفیت مدل بیان کنی.

## 2. پیش‌نیاز

از <bdi dir="ltr">Week 01</bdi> باید به یاد داشته باشی:

- <bdi dir="ltr">Capability</bdi> می‌گوید بانک چه کاری باید بتواند انجام دهد.
- <bdi dir="ltr">Domain</bdi> محل دانش و مسئله است.
- <bdi dir="ltr">Bounded Context</bdi> مرز اعتبار یک مدل و زبان است.
- هیچ‌کدام به‌طور خودکار <bdi dir="ltr">Deployable Service</bdi> نیستند.

اگر هنوز می‌گویی «سامانهٔ تسهیلات یک <bdi dir="ltr">Domain</bdi> است چون یک <bdi dir="ltr">Database</bdi> دارد»، این درس دقیقاً همان مدل ذهنی را اصلاح می‌کند.

## 3. مدل ذهنی اصلی

بانک را یک <bdi dir="ltr">Problem Space</bdi> بزرگ فرض کن. درون آن نواحی‌ای وجود دارند که:

- هدف‌های متفاوت دارند؛
- از واژگان و خبرگان متفاوت استفاده می‌کنند؛
- قواعد و چرخهٔ عمر متفاوت دارند؛
- با سرعت و دلیل متفاوت تغییر می‌کنند؛
- ارزش و ریسک متفاوتی برای راهبرد بانک دارند.

<bdi dir="ltr">Strategic DDD</bdi> پیش از آنکه دربارهٔ کلاس و <bdi dir="ltr">Aggregate</bdi> حرف بزند، می‌پرسد:

> کدام قسمت مسئله برای ما مهم‌تر است، مرز دانش آن کجاست و بهترین انرژی طراحی را کجا خرج کنیم؟

نمای فشرده:


</div>

<div dir="ltr" align="left">

~~~text
Business strategy
      ↓
Domain → Subdomains → strategic classification
      ↓                     ↓
modeling focus         investment / team / build-buy
      ↓
Bounded Context hypotheses
~~~

</div>

<div dir="rtl" align="right">


فلش آخر یک نگاشت یک‌به‌یک نیست. یک <bdi dir="ltr">Subdomain</bdi> می‌تواند در یک یا چند <bdi dir="ltr">Bounded Context</bdi> مدل شود و یک <bdi dir="ltr">Context</bdi> ممکن است در گذار <bdi dir="ltr">Legacy</bdi> بخشی از چند <bdi dir="ltr">Subdomain</bdi> را حمل کند؛ هرچند این اختلاط معمولاً نیازمند ثبت <bdi dir="ltr">Debt</bdi> و برنامهٔ اصلاح است.

## 4. تعریف‌های دقیق

### <bdi dir="ltr">4.1 Domain</bdi>

<bdi dir="ltr">Domain</bdi> حوزه‌ای از مسئله، دانش و فعالیت است که سازمان در آن ارزش ایجاد می‌کند یا تعهدی را انجام می‌دهد.

مثال‌ها در بانک:

- <bdi dir="ltr">Lending</bdi>
- <bdi dir="ltr">Deposits</bdi>
- <bdi dir="ltr">Payments</bdi>
- <bdi dir="ltr">Accounting</bdi>
- <bdi dir="ltr">Customer Management</bdi>

این نام‌ها هنوز اندازهٔ دقیق یا <bdi dir="ltr">Boundary</bdi> نهایی را ثابت نمی‌کنند. <bdi dir="ltr">`Lending`</bdi> می‌تواند برای یک بحث <bdi dir="ltr">Executive</bdi> یک <bdi dir="ltr">Domain</bdi> مناسب باشد، ولی برای طراحی مدل بسیار بزرگ است.

### <bdi dir="ltr">4.2 Subdomain</bdi>

<bdi dir="ltr">Subdomain</bdi> بخشی متمایز از <bdi dir="ltr">Domain</bdi> است که <bdi dir="ltr">Outcome</bdi>، قواعد، زبان یا تخصص نسبتاً منسجم دارد.

برای <bdi dir="ltr">Lending</bdi> می‌توان <bdi dir="ltr">Candidate</bdi>های زیر را کشف کرد:

- <bdi dir="ltr">Loan Origination</bdi>
- <bdi dir="ltr">Credit Assessment/Decision</bdi>
- <bdi dir="ltr">Product</bdi> & <bdi dir="ltr">Pricing</bdi>
- <bdi dir="ltr">Agreement Formation</bdi>
- <bdi dir="ltr">Loan Servicing</bdi>
- <bdi dir="ltr">Repayment</bdi>
- <bdi dir="ltr">Delinquency/Collections</bdi>

این فهرست نسخهٔ جهانی نیست. در یک بانک، <bdi dir="ltr">Credit Decision</bdi> ممکن است <bdi dir="ltr">Rule Engine</bdi> مرکزیِ چند محصول باشد؛ در بانک دیگر بخشی از <bdi dir="ltr">Lending Corporate</bdi> با دانش اختصاصی باشد. مرز باید از واقعیت کسب‌وکار کشف شود.

### <bdi dir="ltr">4.3 Core Subdomain</bdi>

<bdi dir="ltr">Core Subdomain</bdi> جایی است که بانک در مقطع فعلی می‌خواهد از طریق دانش، مدل یا شیوهٔ اجرای متمایز، مزیت راهبردی بسازد.

نشانه‌ها:

- مستقیماً به <bdi dir="ltr">Strategy</bdi> و <bdi dir="ltr">Outcome</bdi> کلیدی وصل است.
- قواعد آن برای بانک متمایز یا بسیار ارزشمندند.
- تغییر سریع و یادگیری مستمر در آن رخ می‌دهد.
- واگذاری کامل مدل آن، مزیت یا اختیار مهمی را از بانک می‌گیرد.
- خبرگان و تیم قوی‌تر باید در آن متمرکز شوند.

<bdi dir="ltr">`Core`</bdi> به معنی «هر چیز حیاتی» نیست. برق دیتاسنتر حیاتی است، ولی لزوماً <bdi dir="ltr">Core Subdomain</bdi> کسب‌وکار بانک نیست.

### <bdi dir="ltr">4.4 Supporting Subdomain</bdi>

<bdi dir="ltr">Supporting Subdomain</bdi> برای تحقق <bdi dir="ltr">Core</bdi> یا عملیات بانک لازم و دارای قواعد تخصصی است، ولی منبع اصلی تمایز راهبردی نیست.

ممکن است:

- سفارشی‌سازی لازم داشته باشد؛
- ریسک مالی یا مقرراتی بالایی داشته باشد؛
- به مدل دقیق و تیم متخصص نیاز داشته باشد؛
- با این حال مزیت رقابتی اصلی بانک نباشد.

برای بسیاری از بانک‌ها، <bdi dir="ltr">Accounting</bdi> عملیاتی دقیق و حیاتی است، اما الزاماً محلی نیست که بانک از طریق مدل منحصربه‌فرد آن با رقبا تفاوت بسازد. بنابراین می‌تواند <bdi dir="ltr">Supporting</bdi> باشد؛ اما این یک <bdi dir="ltr">Hypothesis</bdi> است، نه حکم جهانی.

### <bdi dir="ltr">4.5 Generic Subdomain</bdi>

<bdi dir="ltr">Generic Subdomain</bdi> مسئله‌ای است که راه‌حل استاندارد و قابل‌خرید/استفادهٔ مجدد برای آن وجود دارد و مدل اختصاصی بانک معمولاً مزیت ایجاد نمی‌کند.

نمونهٔ محتمل:

- عمومی‌ترین بخش‌های <bdi dir="ltr">IAM</bdi>
- ارسال <bdi dir="ltr">Email/SMS</bdi>
- مدیریت فایل عمومی
- <bdi dir="ltr">Scheduler</bdi> فنی

<bdi dir="ltr">Generic</bdi> به معنی بی‌اهمیت، کم‌ریسک یا بدون <bdi dir="ltr">Owner</bdi> نیست. <bdi dir="ltr">IAM</bdi> می‌تواند <bdi dir="ltr">Generic</bdi> باشد و هم‌زمان امنیتی و حیاتی باشد.

## 5. چهار تمایز ضروری

### <bdi dir="ltr">5.1 Subdomain</bdi> با <bdi dir="ltr">Capability</bdi> یکی نیست

<bdi dir="ltr">Capability</bdi> نمای توان سازمان است؛ <bdi dir="ltr">Subdomain</bdi> نمای ناحیهٔ دانش و مسئله. ممکن است <bdi dir="ltr">Capability</bdi> «اعطای اعتبار» به چند <bdi dir="ltr">Subdomain</bdi> مانند <bdi dir="ltr">Credit Decision</bdi>، <bdi dir="ltr">Agreement</bdi> و <bdi dir="ltr">Loan Servicing</bdi> وابسته باشد.

### <bdi dir="ltr">5.2 Subdomain</bdi> با <bdi dir="ltr">Bounded Context</bdi> یکی نیست

<bdi dir="ltr">Subdomain</bdi> در <bdi dir="ltr">Problem Space</bdi> است. <bdi dir="ltr">Bounded Context</bdi> یک مرز مدل در <bdi dir="ltr">Solution Space</bdi> است. هدف مطلوب، <bdi dir="ltr">Alignment</bdi> خوب میان آن‌هاست؛ اما <bdi dir="ltr">Legacy</bdi>، ساختار تیم و <bdi dir="ltr">Migration</bdi> ممکن است <bdi dir="ltr">Mapping</bdi> را پیچیده کند.

### <bdi dir="ltr">5.3 Subdomain</bdi> با سامانه یکی نیست

یک سامانهٔ <bdi dir="ltr">Legacy</bdi> ممکن است <bdi dir="ltr">Customer</bdi>، <bdi dir="ltr">Product</bdi>، <bdi dir="ltr">Lending</bdi> و <bdi dir="ltr">Accounting</bdi> را در یک <bdi dir="ltr">Database</bdi> مخلوط کرده باشد. این فقط وضع موجود را نشان می‌دهد، نه مرز دانش را.

### <bdi dir="ltr">5.4 Core</bdi> با <bdi dir="ltr">Main Core</bdi> زیرساختی یکی نیست

در ادبیات سازمانی ممکن است <bdi dir="ltr">`Main Core`</bdi> نام مجموعه‌ای از سامانه‌های مرکزی باشد. <bdi dir="ltr">`Core Subdomain`</bdi> در <bdi dir="ltr">Strategic DDD</bdi> دربارهٔ مزیت راهبردی و تمرکز مدل‌سازی است. تشابه واژه نباید این دو را یکی کند.

## 6. طبقه‌بندی یک ویژگی ذاتی و ابدی نیست

فرض کن راهبرد بانک در سال اول «رشد وام خرد دیجیتال با تصمیم زیر پنج دقیقه» است. در این مقطع:

- <bdi dir="ltr">Credit Decision</bdi> و <bdi dir="ltr">Digital Origination</bdi> احتمالاً <bdi dir="ltr">Core</bdi> هستند.
- <bdi dir="ltr">Loan Servicing</bdi> ممکن است <bdi dir="ltr">Supporting</bdi> باشد.
- <bdi dir="ltr">Email Notification</bdi> احتمالاً <bdi dir="ltr">Generic</bdi> است.

اگر دو سال بعد <bdi dir="ltr">Strategy</bdi> به «تأمین مالی زنجیرهٔ تأمین شرکت‌ها» تغییر کند، مدل <bdi dir="ltr">Exposure</bdi>، <bdi dir="ltr">Limit</bdi>، <bdi dir="ltr">Covenant</bdi> و <bdi dir="ltr">Relationship Pricing</bdi> ممکن است <bdi dir="ltr">Core</bdi> شود. همان <bdi dir="ltr">Subdomain</bdi> قبلی می‌تواند اهمیت متفاوتی پیدا کند.

پس در <bdi dir="ltr">Artifact</bdi> باید بنویسی:

- <bdi dir="ltr">Classification</bdi>
- <bdi dir="ltr">Evidence</bdi>
- <bdi dir="ltr">Confidence</bdi>
- <bdi dir="ltr">Review trigger/date</bdi>

نوشتن فقط یک رنگ روی <bdi dir="ltr">Domain Map</bdi>، تصمیم معماری قابل دفاع نیست.

## <bdi dir="ltr">7. Forces</bdi> طبقه‌بندی

برای هر <bdi dir="ltr">Candidate</bdi> حداقل این شش <bdi dir="ltr">Force</bdi> را بررسی کن:

| <bdi dir="ltr">Force</bdi> | سؤال |
|---|---|
| <bdi dir="ltr">Strategic differentiation</bdi> | آیا بهترشدن این مدل <bdi dir="ltr">Outcome</bdi> راهبردی و تمایز بانک را بالا می‌برد؟ |
| <bdi dir="ltr">Domain specificity</bdi> | قواعد چقدر بانکی و مختص مدل کسب‌وکار ما هستند؟ |
| <bdi dir="ltr">Change and learning</bdi> | چندبار و به چه دلیل تغییر می‌کند؟ |
| <bdi dir="ltr">Risk</bdi> | خطا چه اثر مالی، حقوقی، اعتباری یا عملیاتی دارد؟ |
| <bdi dir="ltr">Scarce knowledge</bdi> | آیا فهم عمیق و کمیاب خبرگان لازم است؟ |
| <bdi dir="ltr">Control/build-buy</bdi> | کدام بخش باید تحت کنترل بانک بماند و چرا؟ |

پیچیدگی به‌تنهایی <bdi dir="ltr">Core</bdi> بودن را ثابت نمی‌کند. یک مسئله ممکن است بسیار پیچیده ولی <bdi dir="ltr">Commodity</bdi> باشد. همچنین تعداد <bdi dir="ltr">Transaction</bdi> بالا به‌تنهایی <bdi dir="ltr">Classification</bdi> راهبردی نیست؛ آن یک <bdi dir="ltr">Force</bdi> فنی/<bdi dir="ltr">NFR</bdi> است.

## 8. مثال هدایت‌شده: «وام خرد دیجیتال»

### مرحلهٔ اول: <bdi dir="ltr">Outcome</bdi>

<bdi dir="ltr">Outcome</bdi> فرضی بانک:

> مشتری واجد شرایط بتواند با کنترل ریسک مصوب، وام خرد را در کمتر از پنج دقیقه دریافت کند.

### مرحلهٔ دوم: <bdi dir="ltr">Candidate Subdomain</bdi>ها

- <bdi dir="ltr">Customer Identification/KYC</bdi>
- <bdi dir="ltr">Eligibility and Credit Decision</bdi>
- <bdi dir="ltr">Product/Pricing</bdi>
- <bdi dir="ltr">Agreement Formation</bdi>
- <bdi dir="ltr">Disbursement</bdi>
- <bdi dir="ltr">Deposit Credit</bdi>
- <bdi dir="ltr">Loan Servicing</bdi>
- <bdi dir="ltr">Accounting</bdi>
- <bdi dir="ltr">Notification</bdi>

### مرحلهٔ سوم: تحلیل، نه اعلام حکم

<bdi dir="ltr">`Eligibility and Credit Decision`</bdi> ممکن است <bdi dir="ltr">Core</bdi> باشد، اگر بانک مدل داده و قواعد ریسک متمایزی دارد و <bdi dir="ltr">Strategy</bdi> روی سرعت/کیفیت تصمیم استوار است.

<bdi dir="ltr">`Notification`</bdi> احتمالاً <bdi dir="ltr">Generic</bdi> است، چون تفاوت در موتور ارسال پیام مزیت اصلی وام را نمی‌سازد؛ ولی محتوای حقوقی پیام ممکن است بخشی از <bdi dir="ltr">Supporting policy</bdi> باشد.

<bdi dir="ltr">`Accounting`</bdi> حیاتی و تخصصی است. شاید <bdi dir="ltr">Supporting</bdi> باشد، زیرا صحت و تطابق می‌خواهد اما مدل اختصاصی آن مزیت بازاری تولید نمی‌کند. بااین‌حال اگر بانک یک <bdi dir="ltr">Accounting Product/Platform</bdi> به دیگر مؤسسات عرضه کند، <bdi dir="ltr">Classification</bdi> می‌تواند تغییر کند.

<bdi dir="ltr">`Deposit Credit`</bdi> را نباید صرفاً زیر <bdi dir="ltr">Lending</bdi> قرار داد. دانش مانده، پذیرش واریز، محدودیت حساب و <bdi dir="ltr">Idempotency</bdi> عملیات متعلق به <bdi dir="ltr">Deposits</bdi> است. یک <bdi dir="ltr">Value Stream</bdi> می‌تواند چند <bdi dir="ltr">Subdomain</bdi> را عبور کند.

### مرحلهٔ چهارم: پیامد سرمایه‌گذاری

اگر <bdi dir="ltr">Credit Decision</bdi> واقعاً <bdi dir="ltr">Core</bdi> باشد:

- بهترین خبرگان <bdi dir="ltr">Domain</bdi> و <bdi dir="ltr">Engineer</bdi>ها باید روی آن متمرکز شوند.
- مدل و آزمایش‌های آن باید غنی‌تر باشند.
- واگذاری <bdi dir="ltr">Black-box</bdi> تصمیم ممکن است <bdi dir="ltr">Strategy</bdi> را تضعیف کند.
- چرخهٔ یادگیری و اندازه‌گیری <bdi dir="ltr">Outcome</bdi> مهم‌تر از تعداد <bdi dir="ltr">Feature</bdi> است.

اگر <bdi dir="ltr">Notification Generic</bdi> باشد:

- <bdi dir="ltr">Buy/Reuse</bdi> گزینهٔ قوی‌تری است.
- <bdi dir="ltr">Customization</bdi> باید حداقلی و در <bdi dir="ltr">Boundary</bdi> باشد.
- تیم <bdi dir="ltr">Core</bdi> نباید انرژی اصلی را صرف بازنویسی موتور پیام کند.

## <bdi dir="ltr">9. BIAN</bdi> در این مرحله

[<bdi dir="ltr">BIAN Service Landscape 14.0</bdi>](https://bian.org/deliverables/service-landscape/) یک <bdi dir="ltr">Reference Structure</bdi> برای مشاهدهٔ پوشش مسئولیت‌های بانکی است. روش استفاده:

1. ابتدا <bdi dir="ltr">Candidate</bdi>های خودت را از <bdi dir="ltr">Strategy</bdi> و <bdi dir="ltr">Discovery</bdi> بساز.
2. سپس نام و <bdi dir="ltr">Scope</bdi> را با <bdi dir="ltr">BIAN</bdi> مقایسه کن.
3. <bdi dir="ltr">Gap</bdi> را به سه دسته تقسیم کن: شکاف واقعی، تفاوت نام/<bdi dir="ltr">Granularity</bdi>، خارج از <bdi dir="ltr">Scope.</bdi>
4. هیچ <bdi dir="ltr">Service Domain</bdi> را خودکار <bdi dir="ltr">Subdomain</bdi>، <bdi dir="ltr">Context</bdi> یا <bdi dir="ltr">Microservice</bdi> اعلام نکن.

<bdi dir="ltr">BIAN</bdi> نمی‌داند بانک تو در این مقطع با چه چیزی متمایز می‌شود؛ بنابراین <bdi dir="ltr">Core/Supporting/Generic</bdi> را به‌جای تو تعیین نمی‌کند.

## 10. ضد‌مثال‌ها

### «همهٔ <bdi dir="ltr">Core Banking</bdi>، <bdi dir="ltr">Core Subdomain</bdi> است»

این جمله واژهٔ سازمانی <bdi dir="ltr">Core</bdi> را با <bdi dir="ltr">Strategic Core</bdi> مخلوط می‌کند و امکان تمرکز سرمایه را از بین می‌برد.

### «هر چیز پیچیده <bdi dir="ltr">Core</bdi> است»

پیچیدگی می‌تواند دلیل استفاده از محصول استاندارد یا تیم <bdi dir="ltr">Platform</bdi> باشد؛ نه الزاماً دلیل تمایز راهبردی.

### «<bdi dir="ltr">Generic</bdi> را به تیم ضعیف بدهیم»

<bdi dir="ltr">Generic</bdi> بودن مجوز کیفیت پایین نیست. <bdi dir="ltr">Security</bdi>، <bdi dir="ltr">Availability</bdi> و <bdi dir="ltr">Vendor Management</bdi> هنوز جدی‌اند.

### «یک جدول مستقل یعنی یک <bdi dir="ltr">Subdomain</bdi>»

جدول واحد ذخیره‌سازی است. <bdi dir="ltr">Subdomain</bdi> باید با <bdi dir="ltr">Outcome</bdi>، زبان و قواعد دفاع شود.

### «<bdi dir="ltr">BIAN</bdi> گفته، پس <bdi dir="ltr">Boundary</bdi> نهایی است»

<bdi dir="ltr">Reference Model</bdi> برای <bdi dir="ltr">Gap Check</bdi> است؛ <bdi dir="ltr">Boundary</bdi> محلی به <bdi dir="ltr">Strategy</bdi>، تیم، <bdi dir="ltr">Legacy</bdi>، <bdi dir="ltr">Transaction</bdi> و <bdi dir="ltr">NFR</bdi> وابسته است.

## 11. تمرین هدایت‌شدهٔ پنج‌دقیقه‌ای

برای <bdi dir="ltr">`Loan Servicing`</bdi> این چهار خط را بنویس:

1. <bdi dir="ltr">Outcome</bdi> آن چیست؟
2. سه قاعدهٔ متمایز آن چیست؟
3. اگر بانک <bdi dir="ltr">Strategy</bdi> وام خرد دیجیتال دارد، <bdi dir="ltr">Core/Supporting/Generic</bdi> کدام است؟
4. چه شاهدی می‌تواند <bdi dir="ltr">Classification</bdi> تو را رد کند؟

اگر در پاسخ فقط نام <bdi dir="ltr">Function</bdi> یا <bdi dir="ltr">Table</bdi> نوشتی، هنوز <bdi dir="ltr">Subdomain</bdi> را تحلیل نکرده‌ای.

## 12. تمرین مستقل

[<bdi dir="ltr">Day 01 Exercise</bdi> — <bdi dir="ltr">Subdomain Matrix</bdi>](../exercises/day-01-subdomain-matrix.md) را انجام بده و پاسخ را در <bdi dir="ltr">Workbook</bdi> ثبت کن. هدف «درست حدس‌زدن برچسب» نیست؛ هدف دفاع از <bdi dir="ltr">Classification</bdi> با <bdi dir="ltr">Forces</bdi> و <bdi dir="ltr">Evidence</bdi> است.

## 13. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تفکیک <bdi dir="ltr">Domain/Subdomain</bdi> از <bdi dir="ltr">System/Capability/Context</bdi> | ۲ |
| تجزیه بر مبنای <bdi dir="ltr">Outcome</bdi>، زبان و قواعد | ۲ |
| طبقه‌بندی راهبردی با شواهد | ۳ |
| بیان پیامد سرمایه‌گذاری و امکان تغییر <bdi dir="ltr">Classification</bdi> | ۲ |
| ثبت <bdi dir="ltr">Confidence/Open Question</bdi> | ۱ |
| **جمع** | **۱۰** |

حد عبور روز: ۷ از ۱۰. برچسب درست بدون استدلال حداکثر نصف امتیاز می‌گیرد.

## 14. آزمون خروج

درس را ببند و [<bdi dir="ltr">Day 01 Exit Ticket</bdi>](../quizzes/day-01-exit-ticket.md) را در پنج دقیقه پاسخ بده.

## 15. منابع اصلی

- [<bdi dir="ltr">Domain-Driven Design Reference</bdi>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf): زبان و الگوهای رسمی <bdi dir="ltr">Strategic DDD</bdi>
- [<bdi dir="ltr">BIAN Service Landscape 14.0</bdi>](https://bian.org/deliverables/service-landscape/): <bdi dir="ltr">Gap Check</bdi> مسئولیت‌های بانکی

این درس <bdi dir="ltr">Classification</bdi> بانک خاصی را <bdi dir="ltr">Fact</bdi> اعلام نمی‌کند. تمام برچسب‌های بانکی مثال، <bdi dir="ltr">Hypothesis</bdi> هستند و باید با <bdi dir="ltr">Strategy</bdi> و خبرگان همان بانک اعتبارسنجی شوند.

</div>
