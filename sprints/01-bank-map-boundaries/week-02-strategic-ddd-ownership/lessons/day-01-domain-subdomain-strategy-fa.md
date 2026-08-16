<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 01</span> — <span dir="ltr">Domain</span>، <span dir="ltr">Subdomain</span> و اهمیت راهبردی

- <span dir="ltr">Day budget: 50 minutes including exercise and exit ticket</span>
- <span dir="ltr">Level: intermediate</span>
- <span dir="ltr">Output: Subdomain Matrix v0.1</span>
- <span dir="ltr">Banking case:</span> زنجیرهٔ اعتبار از طراحی محصول تا وصول

## 1. هدف قابل سنجش

در پایان این درس باید بتوانی:

1. <span dir="ltr">Domain</span> را از <span dir="ltr">Capability</span>، <span dir="ltr">Application</span>، <span dir="ltr">Department</span> و <span dir="ltr">Bounded Context</span> جدا کنی.
2. یک حوزهٔ بزرگ بانکی را بر اساس دانش، قواعد و <span dir="ltr">Outcome</span> به <span dir="ltr">Subdomain</span>های معنادار بشکنی.
3. <span dir="ltr">Core</span>، <span dir="ltr">Supporting</span> و <span dir="ltr">Generic</span> را با شواهد راهبردی طبقه‌بندی کنی.
4. توضیح بدهی چرا این طبقه‌بندی برای دو بانک یا دو مقطع زمانی می‌تواند متفاوت باشد.
5. پیامد طبقه‌بندی را برای سرمایه‌گذاری، تیم، <span dir="ltr">Build/Buy</span> و کیفیت مدل بیان کنی.

## 2. پیش‌نیاز

از <span dir="ltr">Week 01</span> باید به یاد داشته باشی:

- <span dir="ltr">Capability</span> می‌گوید بانک چه کاری باید بتواند انجام دهد.
- <span dir="ltr">Domain</span> محل دانش و مسئله است.
- <span dir="ltr">Bounded Context</span> مرز اعتبار یک مدل و زبان است.
- هیچ‌کدام به‌طور خودکار <span dir="ltr">Deployable Service</span> نیستند.

اگر هنوز می‌گویی «سامانهٔ تسهیلات یک <span dir="ltr">Domain</span> است چون یک <span dir="ltr">Database</span> دارد»، این درس دقیقاً همان مدل ذهنی را اصلاح می‌کند.

## 3. مدل ذهنی اصلی

بانک را یک <span dir="ltr">Problem Space</span> بزرگ فرض کن. درون آن نواحی‌ای وجود دارند که:

- هدف‌های متفاوت دارند؛
- از واژگان و خبرگان متفاوت استفاده می‌کنند؛
- قواعد و چرخهٔ عمر متفاوت دارند؛
- با سرعت و دلیل متفاوت تغییر می‌کنند؛
- ارزش و ریسک متفاوتی برای راهبرد بانک دارند.

<span dir="ltr">Strategic DDD</span> پیش از آنکه دربارهٔ کلاس و <span dir="ltr">Aggregate</span> حرف بزند، می‌پرسد:

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


فلش آخر یک نگاشت یک‌به‌یک نیست. یک <span dir="ltr">Subdomain</span> می‌تواند در یک یا چند <span dir="ltr">Bounded Context</span> مدل شود و یک <span dir="ltr">Context</span> ممکن است در گذار <span dir="ltr">Legacy</span> بخشی از چند <span dir="ltr">Subdomain</span> را حمل کند؛ هرچند این اختلاط معمولاً نیازمند ثبت <span dir="ltr">Debt</span> و برنامهٔ اصلاح است.

## 4. تعریف‌های دقیق

### <span dir="ltr">4.1 Domain</span>

<span dir="ltr">Domain</span> حوزه‌ای از مسئله، دانش و فعالیت است که سازمان در آن ارزش ایجاد می‌کند یا تعهدی را انجام می‌دهد.

مثال‌ها در بانک:

- <span dir="ltr">Lending</span>
- <span dir="ltr">Deposits</span>
- <span dir="ltr">Payments</span>
- <span dir="ltr">Accounting</span>
- <span dir="ltr">Customer Management</span>

این نام‌ها هنوز اندازهٔ دقیق یا <span dir="ltr">Boundary</span> نهایی را ثابت نمی‌کنند. <span dir="ltr">`Lending`</span> می‌تواند برای یک بحث <span dir="ltr">Executive</span> یک <span dir="ltr">Domain</span> مناسب باشد، ولی برای طراحی مدل بسیار بزرگ است.

### <span dir="ltr">4.2 Subdomain</span>

<span dir="ltr">Subdomain</span> بخشی متمایز از <span dir="ltr">Domain</span> است که <span dir="ltr">Outcome</span>، قواعد، زبان یا تخصص نسبتاً منسجم دارد.

برای <span dir="ltr">Lending</span> می‌توان <span dir="ltr">Candidate</span>های زیر را کشف کرد:

- <span dir="ltr">Loan Origination</span>
- <span dir="ltr">Credit Assessment/Decision</span>
- <span dir="ltr">Product</span> & <span dir="ltr">Pricing</span>
- <span dir="ltr">Agreement Formation</span>
- <span dir="ltr">Loan Servicing</span>
- <span dir="ltr">Repayment</span>
- <span dir="ltr">Delinquency/Collections</span>

این فهرست نسخهٔ جهانی نیست. در یک بانک، <span dir="ltr">Credit Decision</span> ممکن است <span dir="ltr">Rule Engine</span> مرکزیِ چند محصول باشد؛ در بانک دیگر بخشی از <span dir="ltr">Lending Corporate</span> با دانش اختصاصی باشد. مرز باید از واقعیت کسب‌وکار کشف شود.

### <span dir="ltr">4.3 Core Subdomain</span>

<span dir="ltr">Core Subdomain</span> جایی است که بانک در مقطع فعلی می‌خواهد از طریق دانش، مدل یا شیوهٔ اجرای متمایز، مزیت راهبردی بسازد.

نشانه‌ها:

- مستقیماً به <span dir="ltr">Strategy</span> و <span dir="ltr">Outcome</span> کلیدی وصل است.
- قواعد آن برای بانک متمایز یا بسیار ارزشمندند.
- تغییر سریع و یادگیری مستمر در آن رخ می‌دهد.
- واگذاری کامل مدل آن، مزیت یا اختیار مهمی را از بانک می‌گیرد.
- خبرگان و تیم قوی‌تر باید در آن متمرکز شوند.

<span dir="ltr">`Core`</span> به معنی «هر چیز حیاتی» نیست. برق دیتاسنتر حیاتی است، ولی لزوماً <span dir="ltr">Core Subdomain</span> کسب‌وکار بانک نیست.

### <span dir="ltr">4.4 Supporting Subdomain</span>

<span dir="ltr">Supporting Subdomain</span> برای تحقق <span dir="ltr">Core</span> یا عملیات بانک لازم و دارای قواعد تخصصی است، ولی منبع اصلی تمایز راهبردی نیست.

ممکن است:

- سفارشی‌سازی لازم داشته باشد؛
- ریسک مالی یا مقرراتی بالایی داشته باشد؛
- به مدل دقیق و تیم متخصص نیاز داشته باشد؛
- با این حال مزیت رقابتی اصلی بانک نباشد.

برای بسیاری از بانک‌ها، <span dir="ltr">Accounting</span> عملیاتی دقیق و حیاتی است، اما الزاماً محلی نیست که بانک از طریق مدل منحصربه‌فرد آن با رقبا تفاوت بسازد. بنابراین می‌تواند <span dir="ltr">Supporting</span> باشد؛ اما این یک <span dir="ltr">Hypothesis</span> است، نه حکم جهانی.

### <span dir="ltr">4.5 Generic Subdomain</span>

<span dir="ltr">Generic Subdomain</span> مسئله‌ای است که راه‌حل استاندارد و قابل‌خرید/استفادهٔ مجدد برای آن وجود دارد و مدل اختصاصی بانک معمولاً مزیت ایجاد نمی‌کند.

نمونهٔ محتمل:

- عمومی‌ترین بخش‌های <span dir="ltr">IAM</span>
- ارسال <span dir="ltr">Email/SMS</span>
- مدیریت فایل عمومی
- <span dir="ltr">Scheduler</span> فنی

<span dir="ltr">Generic</span> به معنی بی‌اهمیت، کم‌ریسک یا بدون <span dir="ltr">Owner</span> نیست. <span dir="ltr">IAM</span> می‌تواند <span dir="ltr">Generic</span> باشد و هم‌زمان امنیتی و حیاتی باشد.

## 5. چهار تمایز ضروری

### <span dir="ltr">5.1 Subdomain</span> با <span dir="ltr">Capability</span> یکی نیست

<span dir="ltr">Capability</span> نمای توان سازمان است؛ <span dir="ltr">Subdomain</span> نمای ناحیهٔ دانش و مسئله. ممکن است <span dir="ltr">Capability</span> «اعطای اعتبار» به چند <span dir="ltr">Subdomain</span> مانند <span dir="ltr">Credit Decision</span>، <span dir="ltr">Agreement</span> و <span dir="ltr">Loan Servicing</span> وابسته باشد.

### <span dir="ltr">5.2 Subdomain</span> با <span dir="ltr">Bounded Context</span> یکی نیست

<span dir="ltr">Subdomain</span> در <span dir="ltr">Problem Space</span> است. <span dir="ltr">Bounded Context</span> یک مرز مدل در <span dir="ltr">Solution Space</span> است. هدف مطلوب، <span dir="ltr">Alignment</span> خوب میان آن‌هاست؛ اما <span dir="ltr">Legacy</span>، ساختار تیم و <span dir="ltr">Migration</span> ممکن است <span dir="ltr">Mapping</span> را پیچیده کند.

### <span dir="ltr">5.3 Subdomain</span> با سامانه یکی نیست

یک سامانهٔ <span dir="ltr">Legacy</span> ممکن است <span dir="ltr">Customer</span>، <span dir="ltr">Product</span>، <span dir="ltr">Lending</span> و <span dir="ltr">Accounting</span> را در یک <span dir="ltr">Database</span> مخلوط کرده باشد. این فقط وضع موجود را نشان می‌دهد، نه مرز دانش را.

### <span dir="ltr">5.4 Core</span> با <span dir="ltr">Main Core</span> زیرساختی یکی نیست

در ادبیات سازمانی ممکن است <span dir="ltr">`Main Core`</span> نام مجموعه‌ای از سامانه‌های مرکزی باشد. <span dir="ltr">`Core Subdomain`</span> در <span dir="ltr">Strategic DDD</span> دربارهٔ مزیت راهبردی و تمرکز مدل‌سازی است. تشابه واژه نباید این دو را یکی کند.

## 6. طبقه‌بندی یک ویژگی ذاتی و ابدی نیست

فرض کن راهبرد بانک در سال اول «رشد وام خرد دیجیتال با تصمیم زیر پنج دقیقه» است. در این مقطع:

- <span dir="ltr">Credit Decision</span> و <span dir="ltr">Digital Origination</span> احتمالاً <span dir="ltr">Core</span> هستند.
- <span dir="ltr">Loan Servicing</span> ممکن است <span dir="ltr">Supporting</span> باشد.
- <span dir="ltr">Email Notification</span> احتمالاً <span dir="ltr">Generic</span> است.

اگر دو سال بعد <span dir="ltr">Strategy</span> به «تأمین مالی زنجیرهٔ تأمین شرکت‌ها» تغییر کند، مدل <span dir="ltr">Exposure</span>، <span dir="ltr">Limit</span>، <span dir="ltr">Covenant</span> و <span dir="ltr">Relationship Pricing</span> ممکن است <span dir="ltr">Core</span> شود. همان <span dir="ltr">Subdomain</span> قبلی می‌تواند اهمیت متفاوتی پیدا کند.

پس در <span dir="ltr">Artifact</span> باید بنویسی:

- <span dir="ltr">Classification</span>
- <span dir="ltr">Evidence</span>
- <span dir="ltr">Confidence</span>
- <span dir="ltr">Review trigger/date</span>

نوشتن فقط یک رنگ روی <span dir="ltr">Domain Map</span>، تصمیم معماری قابل دفاع نیست.

## <span dir="ltr">7. Forces</span> طبقه‌بندی

برای هر <span dir="ltr">Candidate</span> حداقل این شش <span dir="ltr">Force</span> را بررسی کن:

| <span dir="ltr">Force</span> | سؤال |
|---|---|
| <span dir="ltr">Strategic differentiation</span> | آیا بهترشدن این مدل <span dir="ltr">Outcome</span> راهبردی و تمایز بانک را بالا می‌برد؟ |
| <span dir="ltr">Domain specificity</span> | قواعد چقدر بانکی و مختص مدل کسب‌وکار ما هستند؟ |
| <span dir="ltr">Change and learning</span> | چندبار و به چه دلیل تغییر می‌کند؟ |
| <span dir="ltr">Risk</span> | خطا چه اثر مالی، حقوقی، اعتباری یا عملیاتی دارد؟ |
| <span dir="ltr">Scarce knowledge</span> | آیا فهم عمیق و کمیاب خبرگان لازم است؟ |
| <span dir="ltr">Control/build-buy</span> | کدام بخش باید تحت کنترل بانک بماند و چرا؟ |

پیچیدگی به‌تنهایی <span dir="ltr">Core</span> بودن را ثابت نمی‌کند. یک مسئله ممکن است بسیار پیچیده ولی <span dir="ltr">Commodity</span> باشد. همچنین تعداد <span dir="ltr">Transaction</span> بالا به‌تنهایی <span dir="ltr">Classification</span> راهبردی نیست؛ آن یک <span dir="ltr">Force</span> فنی/<span dir="ltr">NFR</span> است.

## 8. مثال هدایت‌شده: «وام خرد دیجیتال»

### مرحلهٔ اول: <span dir="ltr">Outcome</span>

<span dir="ltr">Outcome</span> فرضی بانک:

> مشتری واجد شرایط بتواند با کنترل ریسک مصوب، وام خرد را در کمتر از پنج دقیقه دریافت کند.

### مرحلهٔ دوم: <span dir="ltr">Candidate Subdomain</span>ها

- <span dir="ltr">Customer Identification/KYC</span>
- <span dir="ltr">Eligibility and Credit Decision</span>
- <span dir="ltr">Product/Pricing</span>
- <span dir="ltr">Agreement Formation</span>
- <span dir="ltr">Disbursement</span>
- <span dir="ltr">Deposit Credit</span>
- <span dir="ltr">Loan Servicing</span>
- <span dir="ltr">Accounting</span>
- <span dir="ltr">Notification</span>

### مرحلهٔ سوم: تحلیل، نه اعلام حکم

<span dir="ltr">`Eligibility and Credit Decision`</span> ممکن است <span dir="ltr">Core</span> باشد، اگر بانک مدل داده و قواعد ریسک متمایزی دارد و <span dir="ltr">Strategy</span> روی سرعت/کیفیت تصمیم استوار است.

<span dir="ltr">`Notification`</span> احتمالاً <span dir="ltr">Generic</span> است، چون تفاوت در موتور ارسال پیام مزیت اصلی وام را نمی‌سازد؛ ولی محتوای حقوقی پیام ممکن است بخشی از <span dir="ltr">Supporting policy</span> باشد.

<span dir="ltr">`Accounting`</span> حیاتی و تخصصی است. شاید <span dir="ltr">Supporting</span> باشد، زیرا صحت و تطابق می‌خواهد اما مدل اختصاصی آن مزیت بازاری تولید نمی‌کند. بااین‌حال اگر بانک یک <span dir="ltr">Accounting Product/Platform</span> به دیگر مؤسسات عرضه کند، <span dir="ltr">Classification</span> می‌تواند تغییر کند.

<span dir="ltr">`Deposit Credit`</span> را نباید صرفاً زیر <span dir="ltr">Lending</span> قرار داد. دانش مانده، پذیرش واریز، محدودیت حساب و <span dir="ltr">Idempotency</span> عملیات متعلق به <span dir="ltr">Deposits</span> است. یک <span dir="ltr">Value Stream</span> می‌تواند چند <span dir="ltr">Subdomain</span> را عبور کند.

### مرحلهٔ چهارم: پیامد سرمایه‌گذاری

اگر <span dir="ltr">Credit Decision</span> واقعاً <span dir="ltr">Core</span> باشد:

- بهترین خبرگان <span dir="ltr">Domain</span> و <span dir="ltr">Engineer</span>ها باید روی آن متمرکز شوند.
- مدل و آزمایش‌های آن باید غنی‌تر باشند.
- واگذاری <span dir="ltr">Black-box</span> تصمیم ممکن است <span dir="ltr">Strategy</span> را تضعیف کند.
- چرخهٔ یادگیری و اندازه‌گیری <span dir="ltr">Outcome</span> مهم‌تر از تعداد <span dir="ltr">Feature</span> است.

اگر <span dir="ltr">Notification Generic</span> باشد:

- <span dir="ltr">Buy/Reuse</span> گزینهٔ قوی‌تری است.
- <span dir="ltr">Customization</span> باید حداقلی و در <span dir="ltr">Boundary</span> باشد.
- تیم <span dir="ltr">Core</span> نباید انرژی اصلی را صرف بازنویسی موتور پیام کند.

## <span dir="ltr">9. BIAN</span> در این مرحله

[<span dir="ltr">BIAN Service Landscape 14.0</span>](https://bian.org/deliverables/service-landscape/) یک <span dir="ltr">Reference Structure</span> برای مشاهدهٔ پوشش مسئولیت‌های بانکی است. روش استفاده:

1. ابتدا <span dir="ltr">Candidate</span>های خودت را از <span dir="ltr">Strategy</span> و <span dir="ltr">Discovery</span> بساز.
2. سپس نام و <span dir="ltr">Scope</span> را با <span dir="ltr">BIAN</span> مقایسه کن.
3. <span dir="ltr">Gap</span> را به سه دسته تقسیم کن: شکاف واقعی، تفاوت نام/<span dir="ltr">Granularity</span>، خارج از <span dir="ltr">Scope.</span>
4. هیچ <span dir="ltr">Service Domain</span> را خودکار <span dir="ltr">Subdomain</span>، <span dir="ltr">Context</span> یا <span dir="ltr">Microservice</span> اعلام نکن.

<span dir="ltr">BIAN</span> نمی‌داند بانک تو در این مقطع با چه چیزی متمایز می‌شود؛ بنابراین <span dir="ltr">Core/Supporting/Generic</span> را به‌جای تو تعیین نمی‌کند.

## 10. ضد‌مثال‌ها

### «همهٔ <span dir="ltr">Core Banking</span>، <span dir="ltr">Core Subdomain</span> است»

این جمله واژهٔ سازمانی <span dir="ltr">Core</span> را با <span dir="ltr">Strategic Core</span> مخلوط می‌کند و امکان تمرکز سرمایه را از بین می‌برد.

### «هر چیز پیچیده <span dir="ltr">Core</span> است»

پیچیدگی می‌تواند دلیل استفاده از محصول استاندارد یا تیم <span dir="ltr">Platform</span> باشد؛ نه الزاماً دلیل تمایز راهبردی.

### «<span dir="ltr">Generic</span> را به تیم ضعیف بدهیم»

<span dir="ltr">Generic</span> بودن مجوز کیفیت پایین نیست. <span dir="ltr">Security</span>، <span dir="ltr">Availability</span> و <span dir="ltr">Vendor Management</span> هنوز جدی‌اند.

### «یک جدول مستقل یعنی یک <span dir="ltr">Subdomain</span>»

جدول واحد ذخیره‌سازی است. <span dir="ltr">Subdomain</span> باید با <span dir="ltr">Outcome</span>، زبان و قواعد دفاع شود.

### «<span dir="ltr">BIAN</span> گفته، پس <span dir="ltr">Boundary</span> نهایی است»

<span dir="ltr">Reference Model</span> برای <span dir="ltr">Gap Check</span> است؛ <span dir="ltr">Boundary</span> محلی به <span dir="ltr">Strategy</span>، تیم، <span dir="ltr">Legacy</span>، <span dir="ltr">Transaction</span> و <span dir="ltr">NFR</span> وابسته است.

## 11. تمرین هدایت‌شدهٔ پنج‌دقیقه‌ای

برای <span dir="ltr">`Loan Servicing`</span> این چهار خط را بنویس:

1. <span dir="ltr">Outcome</span> آن چیست؟
2. سه قاعدهٔ متمایز آن چیست؟
3. اگر بانک <span dir="ltr">Strategy</span> وام خرد دیجیتال دارد، <span dir="ltr">Core/Supporting/Generic</span> کدام است؟
4. چه شاهدی می‌تواند <span dir="ltr">Classification</span> تو را رد کند؟

اگر در پاسخ فقط نام <span dir="ltr">Function</span> یا <span dir="ltr">Table</span> نوشتی، هنوز <span dir="ltr">Subdomain</span> را تحلیل نکرده‌ای.

## 12. تمرین مستقل

[<span dir="ltr">Day 01 Exercise</span> — <span dir="ltr">Subdomain Matrix</span>](../exercises/day-01-subdomain-matrix.md) را انجام بده و پاسخ را در <span dir="ltr">Workbook</span> ثبت کن. هدف «درست حدس‌زدن برچسب» نیست؛ هدف دفاع از <span dir="ltr">Classification</span> با <span dir="ltr">Forces</span> و <span dir="ltr">Evidence</span> است.

## 13. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تفکیک <span dir="ltr">Domain/Subdomain</span> از <span dir="ltr">System/Capability/Context</span> | ۲ |
| تجزیه بر مبنای <span dir="ltr">Outcome</span>، زبان و قواعد | ۲ |
| طبقه‌بندی راهبردی با شواهد | ۳ |
| بیان پیامد سرمایه‌گذاری و امکان تغییر <span dir="ltr">Classification</span> | ۲ |
| ثبت <span dir="ltr">Confidence/Open Question</span> | ۱ |
| **جمع** | **۱۰** |

حد عبور روز: ۷ از ۱۰. برچسب درست بدون استدلال حداکثر نصف امتیاز می‌گیرد.

## 14. آزمون خروج

درس را ببند و [<span dir="ltr">Day 01 Exit Ticket</span>](../quizzes/day-01-exit-ticket.md) را در پنج دقیقه پاسخ بده.

## 15. منابع اصلی

- [<span dir="ltr">Domain-Driven Design Reference</span>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf): زبان و الگوهای رسمی <span dir="ltr">Strategic DDD</span>
- [<span dir="ltr">BIAN Service Landscape 14.0</span>](https://bian.org/deliverables/service-landscape/): <span dir="ltr">Gap Check</span> مسئولیت‌های بانکی

این درس <span dir="ltr">Classification</span> بانک خاصی را <span dir="ltr">Fact</span> اعلام نمی‌کند. تمام برچسب‌های بانکی مثال، <span dir="ltr">Hypothesis</span> هستند و باید با <span dir="ltr">Strategy</span> و خبرگان همان بانک اعتبارسنجی شوند.

</div>
