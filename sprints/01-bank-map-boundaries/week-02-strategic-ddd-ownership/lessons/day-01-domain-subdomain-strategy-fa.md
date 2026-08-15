# Day 01 — Domain، Subdomain و اهمیت راهبردی

- Day budget: 50 minutes including exercise and exit ticket
- Level: intermediate
- Output: Subdomain Matrix v0.1
- Banking case: زنجیرهٔ اعتبار از طراحی محصول تا وصول

## 1. هدف قابل سنجش

در پایان این درس باید بتوانی:

1. Domain را از Capability، Application، Department و Bounded Context جدا کنی.
2. یک حوزهٔ بزرگ بانکی را بر اساس دانش، قواعد و Outcome به Subdomainهای معنادار بشکنی.
3. Core، Supporting و Generic را با شواهد راهبردی طبقه‌بندی کنی.
4. توضیح بدهی چرا این طبقه‌بندی برای دو بانک یا دو مقطع زمانی می‌تواند متفاوت باشد.
5. پیامد طبقه‌بندی را برای سرمایه‌گذاری، تیم، Build/Buy و کیفیت مدل بیان کنی.

## 2. پیش‌نیاز

از Week 01 باید به یاد داشته باشی:

- Capability می‌گوید بانک چه کاری باید بتواند انجام دهد.
- Domain محل دانش و مسئله است.
- Bounded Context مرز اعتبار یک مدل و زبان است.
- هیچ‌کدام به‌طور خودکار Deployable Service نیستند.

اگر هنوز می‌گویی «سامانهٔ تسهیلات یک Domain است چون یک Database دارد»، این درس دقیقاً همان مدل ذهنی را اصلاح می‌کند.

## 3. مدل ذهنی اصلی

بانک را یک Problem Space بزرگ فرض کن. درون آن نواحی‌ای وجود دارند که:

- هدف‌های متفاوت دارند؛
- از واژگان و خبرگان متفاوت استفاده می‌کنند؛
- قواعد و چرخهٔ عمر متفاوت دارند؛
- با سرعت و دلیل متفاوت تغییر می‌کنند؛
- ارزش و ریسک متفاوتی برای راهبرد بانک دارند.

Strategic DDD پیش از آنکه دربارهٔ کلاس و Aggregate حرف بزند، می‌پرسد:

> کدام قسمت مسئله برای ما مهم‌تر است، مرز دانش آن کجاست و بهترین انرژی طراحی را کجا خرج کنیم؟

نمای فشرده:

~~~text
Business strategy
      ↓
Domain → Subdomains → strategic classification
      ↓                     ↓
modeling focus         investment / team / build-buy
      ↓
Bounded Context hypotheses
~~~

فلش آخر یک نگاشت یک‌به‌یک نیست. یک Subdomain می‌تواند در یک یا چند Bounded Context مدل شود و یک Context ممکن است در گذار Legacy بخشی از چند Subdomain را حمل کند؛ هرچند این اختلاط معمولاً نیازمند ثبت Debt و برنامهٔ اصلاح است.

## 4. تعریف‌های دقیق

### 4.1 Domain

Domain حوزه‌ای از مسئله، دانش و فعالیت است که سازمان در آن ارزش ایجاد می‌کند یا تعهدی را انجام می‌دهد.

مثال‌ها در بانک:

- Lending
- Deposits
- Payments
- Accounting
- Customer Management

این نام‌ها هنوز اندازهٔ دقیق یا Boundary نهایی را ثابت نمی‌کنند. `Lending` می‌تواند برای یک بحث Executive یک Domain مناسب باشد، ولی برای طراحی مدل بسیار بزرگ است.

### 4.2 Subdomain

Subdomain بخشی متمایز از Domain است که Outcome، قواعد، زبان یا تخصص نسبتاً منسجم دارد.

برای Lending می‌توان Candidateهای زیر را کشف کرد:

- Loan Origination
- Credit Assessment/Decision
- Product & Pricing
- Agreement Formation
- Loan Servicing
- Repayment
- Delinquency/Collections

این فهرست نسخهٔ جهانی نیست. در یک بانک، Credit Decision ممکن است Rule Engine مرکزیِ چند محصول باشد؛ در بانک دیگر بخشی از Lending Corporate با دانش اختصاصی باشد. مرز باید از واقعیت کسب‌وکار کشف شود.

### 4.3 Core Subdomain

Core Subdomain جایی است که بانک در مقطع فعلی می‌خواهد از طریق دانش، مدل یا شیوهٔ اجرای متمایز، مزیت راهبردی بسازد.

نشانه‌ها:

- مستقیماً به Strategy و Outcome کلیدی وصل است.
- قواعد آن برای بانک متمایز یا بسیار ارزشمندند.
- تغییر سریع و یادگیری مستمر در آن رخ می‌دهد.
- واگذاری کامل مدل آن، مزیت یا اختیار مهمی را از بانک می‌گیرد.
- خبرگان و تیم قوی‌تر باید در آن متمرکز شوند.

`Core` به معنی «هر چیز حیاتی» نیست. برق دیتاسنتر حیاتی است، ولی لزوماً Core Subdomain کسب‌وکار بانک نیست.

### 4.4 Supporting Subdomain

Supporting Subdomain برای تحقق Core یا عملیات بانک لازم و دارای قواعد تخصصی است، ولی منبع اصلی تمایز راهبردی نیست.

ممکن است:

- سفارشی‌سازی لازم داشته باشد؛
- ریسک مالی یا مقرراتی بالایی داشته باشد؛
- به مدل دقیق و تیم متخصص نیاز داشته باشد؛
- با این حال مزیت رقابتی اصلی بانک نباشد.

برای بسیاری از بانک‌ها، Accounting عملیاتی دقیق و حیاتی است، اما الزاماً محلی نیست که بانک از طریق مدل منحصربه‌فرد آن با رقبا تفاوت بسازد. بنابراین می‌تواند Supporting باشد؛ اما این یک Hypothesis است، نه حکم جهانی.

### 4.5 Generic Subdomain

Generic Subdomain مسئله‌ای است که راه‌حل استاندارد و قابل‌خرید/استفادهٔ مجدد برای آن وجود دارد و مدل اختصاصی بانک معمولاً مزیت ایجاد نمی‌کند.

نمونهٔ محتمل:

- عمومی‌ترین بخش‌های IAM
- ارسال Email/SMS
- مدیریت فایل عمومی
- Scheduler فنی

Generic به معنی بی‌اهمیت، کم‌ریسک یا بدون Owner نیست. IAM می‌تواند Generic باشد و هم‌زمان امنیتی و حیاتی باشد.

## 5. چهار تمایز ضروری

### 5.1 Subdomain با Capability یکی نیست

Capability نمای توان سازمان است؛ Subdomain نمای ناحیهٔ دانش و مسئله. ممکن است Capability «اعطای اعتبار» به چند Subdomain مانند Credit Decision، Agreement و Loan Servicing وابسته باشد.

### 5.2 Subdomain با Bounded Context یکی نیست

Subdomain در Problem Space است. Bounded Context یک مرز مدل در Solution Space است. هدف مطلوب، Alignment خوب میان آن‌هاست؛ اما Legacy، ساختار تیم و Migration ممکن است Mapping را پیچیده کند.

### 5.3 Subdomain با سامانه یکی نیست

یک سامانهٔ Legacy ممکن است Customer، Product، Lending و Accounting را در یک Database مخلوط کرده باشد. این فقط وضع موجود را نشان می‌دهد، نه مرز دانش را.

### 5.4 Core با Main Core زیرساختی یکی نیست

در ادبیات سازمانی ممکن است `Main Core` نام مجموعه‌ای از سامانه‌های مرکزی باشد. `Core Subdomain` در Strategic DDD دربارهٔ مزیت راهبردی و تمرکز مدل‌سازی است. تشابه واژه نباید این دو را یکی کند.

## 6. طبقه‌بندی یک ویژگی ذاتی و ابدی نیست

فرض کن راهبرد بانک در سال اول «رشد وام خرد دیجیتال با تصمیم زیر پنج دقیقه» است. در این مقطع:

- Credit Decision و Digital Origination احتمالاً Core هستند.
- Loan Servicing ممکن است Supporting باشد.
- Email Notification احتمالاً Generic است.

اگر دو سال بعد Strategy به «تأمین مالی زنجیرهٔ تأمین شرکت‌ها» تغییر کند، مدل Exposure، Limit، Covenant و Relationship Pricing ممکن است Core شود. همان Subdomain قبلی می‌تواند اهمیت متفاوتی پیدا کند.

پس در Artifact باید بنویسی:

- Classification
- Evidence
- Confidence
- Review trigger/date

نوشتن فقط یک رنگ روی Domain Map، تصمیم معماری قابل دفاع نیست.

## 7. Forces طبقه‌بندی

برای هر Candidate حداقل این شش Force را بررسی کن:

| Force | سؤال |
|---|---|
| Strategic differentiation | آیا بهترشدن این مدل Outcome راهبردی و تمایز بانک را بالا می‌برد؟ |
| Domain specificity | قواعد چقدر بانکی و مختص مدل کسب‌وکار ما هستند؟ |
| Change and learning | چندبار و به چه دلیل تغییر می‌کند؟ |
| Risk | خطا چه اثر مالی، حقوقی، اعتباری یا عملیاتی دارد؟ |
| Scarce knowledge | آیا فهم عمیق و کمیاب خبرگان لازم است؟ |
| Control/build-buy | کدام بخش باید تحت کنترل بانک بماند و چرا؟ |

پیچیدگی به‌تنهایی Core بودن را ثابت نمی‌کند. یک مسئله ممکن است بسیار پیچیده ولی Commodity باشد. همچنین تعداد Transaction بالا به‌تنهایی Classification راهبردی نیست؛ آن یک Force فنی/NFR است.

## 8. مثال هدایت‌شده: «وام خرد دیجیتال»

### مرحلهٔ اول: Outcome

Outcome فرضی بانک:

> مشتری واجد شرایط بتواند با کنترل ریسک مصوب، وام خرد را در کمتر از پنج دقیقه دریافت کند.

### مرحلهٔ دوم: Candidate Subdomainها

- Customer Identification/KYC
- Eligibility and Credit Decision
- Product/Pricing
- Agreement Formation
- Disbursement
- Deposit Credit
- Loan Servicing
- Accounting
- Notification

### مرحلهٔ سوم: تحلیل، نه اعلام حکم

`Eligibility and Credit Decision` ممکن است Core باشد، اگر بانک مدل داده و قواعد ریسک متمایزی دارد و Strategy روی سرعت/کیفیت تصمیم استوار است.

`Notification` احتمالاً Generic است، چون تفاوت در موتور ارسال پیام مزیت اصلی وام را نمی‌سازد؛ ولی محتوای حقوقی پیام ممکن است بخشی از Supporting policy باشد.

`Accounting` حیاتی و تخصصی است. شاید Supporting باشد، زیرا صحت و تطابق می‌خواهد اما مدل اختصاصی آن مزیت بازاری تولید نمی‌کند. بااین‌حال اگر بانک یک Accounting Product/Platform به دیگر مؤسسات عرضه کند، Classification می‌تواند تغییر کند.

`Deposit Credit` را نباید صرفاً زیر Lending قرار داد. دانش مانده، پذیرش واریز، محدودیت حساب و Idempotency عملیات متعلق به Deposits است. یک Value Stream می‌تواند چند Subdomain را عبور کند.

### مرحلهٔ چهارم: پیامد سرمایه‌گذاری

اگر Credit Decision واقعاً Core باشد:

- بهترین خبرگان Domain و Engineerها باید روی آن متمرکز شوند.
- مدل و آزمایش‌های آن باید غنی‌تر باشند.
- واگذاری Black-box تصمیم ممکن است Strategy را تضعیف کند.
- چرخهٔ یادگیری و اندازه‌گیری Outcome مهم‌تر از تعداد Feature است.

اگر Notification Generic باشد:

- Buy/Reuse گزینهٔ قوی‌تری است.
- Customization باید حداقلی و در Boundary باشد.
- تیم Core نباید انرژی اصلی را صرف بازنویسی موتور پیام کند.

## 9. BIAN در این مرحله

[BIAN Service Landscape 14.0](https://bian.org/deliverables/service-landscape/) یک Reference Structure برای مشاهدهٔ پوشش مسئولیت‌های بانکی است. روش استفاده:

1. ابتدا Candidateهای خودت را از Strategy و Discovery بساز.
2. سپس نام و Scope را با BIAN مقایسه کن.
3. Gap را به سه دسته تقسیم کن: شکاف واقعی، تفاوت نام/Granularity، خارج از Scope.
4. هیچ Service Domain را خودکار Subdomain، Context یا Microservice اعلام نکن.

BIAN نمی‌داند بانک تو در این مقطع با چه چیزی متمایز می‌شود؛ بنابراین Core/Supporting/Generic را به‌جای تو تعیین نمی‌کند.

## 10. ضد‌مثال‌ها

### «همهٔ Core Banking، Core Subdomain است»

این جمله واژهٔ سازمانی Core را با Strategic Core مخلوط می‌کند و امکان تمرکز سرمایه را از بین می‌برد.

### «هر چیز پیچیده Core است»

پیچیدگی می‌تواند دلیل استفاده از محصول استاندارد یا تیم Platform باشد؛ نه الزاماً دلیل تمایز راهبردی.

### «Generic را به تیم ضعیف بدهیم»

Generic بودن مجوز کیفیت پایین نیست. Security، Availability و Vendor Management هنوز جدی‌اند.

### «یک جدول مستقل یعنی یک Subdomain»

جدول واحد ذخیره‌سازی است. Subdomain باید با Outcome، زبان و قواعد دفاع شود.

### «BIAN گفته، پس Boundary نهایی است»

Reference Model برای Gap Check است؛ Boundary محلی به Strategy، تیم، Legacy، Transaction و NFR وابسته است.

## 11. تمرین هدایت‌شدهٔ پنج‌دقیقه‌ای

برای `Loan Servicing` این چهار خط را بنویس:

1. Outcome آن چیست؟
2. سه قاعدهٔ متمایز آن چیست؟
3. اگر بانک Strategy وام خرد دیجیتال دارد، Core/Supporting/Generic کدام است؟
4. چه شاهدی می‌تواند Classification تو را رد کند؟

اگر در پاسخ فقط نام Function یا Table نوشتی، هنوز Subdomain را تحلیل نکرده‌ای.

## 12. تمرین مستقل

[Day 01 Exercise — Subdomain Matrix](../exercises/day-01-subdomain-matrix.md) را انجام بده و پاسخ را در Workbook ثبت کن. هدف «درست حدس‌زدن برچسب» نیست؛ هدف دفاع از Classification با Forces و Evidence است.

## 13. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تفکیک Domain/Subdomain از System/Capability/Context | ۲ |
| تجزیه بر مبنای Outcome، زبان و قواعد | ۲ |
| طبقه‌بندی راهبردی با شواهد | ۳ |
| بیان پیامد سرمایه‌گذاری و امکان تغییر Classification | ۲ |
| ثبت Confidence/Open Question | ۱ |
| **جمع** | **۱۰** |

حد عبور روز: ۷ از ۱۰. برچسب درست بدون استدلال حداکثر نصف امتیاز می‌گیرد.

## 14. آزمون خروج

درس را ببند و [Day 01 Exit Ticket](../quizzes/day-01-exit-ticket.md) را در پنج دقیقه پاسخ بده.

## 15. منابع اصلی

- [Domain-Driven Design Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf): زبان و الگوهای رسمی Strategic DDD
- [BIAN Service Landscape 14.0](https://bian.org/deliverables/service-landscape/): Gap Check مسئولیت‌های بانکی

این درس Classification بانک خاصی را Fact اعلام نمی‌کند. تمام برچسب‌های بانکی مثال، Hypothesis هستند و باید با Strategy و خبرگان همان بانک اعتبارسنجی شوند.
