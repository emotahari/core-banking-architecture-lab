<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 02</bdi> — <bdi dir="ltr">Bounded Context</bdi> و <bdi dir="ltr">Ubiquitous Language</bdi>

- <bdi dir="ltr">Day budget: 45 minutes including exercise and exit ticket</bdi>
- <bdi dir="ltr">Output: Language Conflicts v0.1</bdi> و <bdi dir="ltr">Boundary Hypotheses</bdi>
- <bdi dir="ltr">Banking case:</bdi> تفاوت معنای <bdi dir="ltr">Account</bdi>، <bdi dir="ltr">Customer</bdi>، <bdi dir="ltr">Product</bdi>، <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Balance</bdi>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Bounded Context</bdi> را به‌عنوان مرز اعتبار مدل و زبان تعریف کنی.
2. آن را از <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Subdomain</bdi>، <bdi dir="ltr">Application</bdi>، <bdi dir="ltr">Team</bdi>، <bdi dir="ltr">Module</bdi> و <bdi dir="ltr">Microservice</bdi> جدا کنی.
3. <bdi dir="ltr">Homonym</bdi>، <bdi dir="ltr">Synonym</bdi>، <bdi dir="ltr">Rule Conflict</bdi> و <bdi dir="ltr">Lifecycle Conflict</bdi> را به‌عنوان سرنخ مرز کشف کنی.
4. برای یک واژهٔ بانکی، معنای <bdi dir="ltr">Contextual</bdi> و ترجمهٔ لازم را بنویسی.
5. یک <bdi dir="ltr">Boundary Hypothesis</bdi> بسازی و شواهد موافق و مخالف آن را ثبت کنی.

## 2. مدل ذهنی

در بانک، کلمات مشترک الزاماً مفهوم مشترک ندارند. مشکل وقتی شروع می‌شود که یک واژهٔ واحد را به یک <bdi dir="ltr">Entity</bdi> سازمانی عظیم تبدیل کنیم.

واژهٔ <bdi dir="ltr">`Account`</bdi> را ببین:

- در <bdi dir="ltr">Deposits:</bdi> رابطهٔ عملیاتی نگهداری وجوه، وضعیت، مانده و محدودیت‌ها
- در <bdi dir="ltr">Lending:</bdi> موقعیت بدهی یا <bdi dir="ltr">Facility</bdi> و برنامهٔ بازپرداخت
- در <bdi dir="ltr">Accounting:</bdi> حساب دفتر کل، معین یا تفصیلی برای طبقه‌بندی آثار مالی
- در <bdi dir="ltr">IAM:</bdi> حساب کاربری و دسترسی

این‌ها چهار <bdi dir="ltr">View</bdi> از یک <bdi dir="ltr">Entity</bdi> واحد نیستند. مدل، رفتار، شناسه، <bdi dir="ltr">Lifecycle</bdi> و <bdi dir="ltr">Invariant</bdi> آن‌ها متفاوت است.

مدل ذهنی درست:


</div>

<div dir="ltr" align="left">

~~~text
large domain language
        ↓ ambiguity and contradiction
explicit Bounded Contexts
        ↓
internally consistent model + Ubiquitous Language
        ↓
translation through explicit contracts
~~~

</div>

<div dir="rtl" align="right">


## 3. تعریف دقیق <bdi dir="ltr">Bounded Context</bdi>

<bdi dir="ltr">Bounded Context</bdi> مرزی صریح است که **درون آن یک مدل مشخص و <bdi dir="ltr">Ubiquitous Language</bdi> مرتبط با آن، معنای سازگار و معتبر دارد**.

سه کلمهٔ تعریف مهم‌اند:

- <bdi dir="ltr">`Boundary`</bdi>: معلوم است مدل کجا معتبر است و کجا نیست.
- <bdi dir="ltr">`Model`</bdi>: فقط <bdi dir="ltr">Vocabulary</bdi> نیست؛ مفاهیم، روابط، رفتارها و قواعد را دربر می‌گیرد.
- <bdi dir="ltr">`Consistency`</bdi>: یک اصطلاح درون <bdi dir="ltr">Context</bdi> نباید چند معنای متناقض داشته باشد.

<bdi dir="ltr">Bounded Context</bdi> خودش «معنای یک واژه» نیست. مثلاً «معنای قرارداد در حسابداری» یک <bdi dir="ltr">Context</bdi> نیست؛ <bdi dir="ltr">`Financial Accounting Context`</bdi> مرزی است که در آن <bdi dir="ltr">Contract</bdi> ممکن است فقط <bdi dir="ltr">Reference</bdi> یا <bdi dir="ltr">Accounting Dimension</bdi> باشد.

## <bdi dir="ltr">4. Ubiquitous Language</bdi> چیست؟

<bdi dir="ltr">Ubiquitous Language</bdi> زبانی دقیق است که <bdi dir="ltr">Domain Expert</bdi>، <bdi dir="ltr">Analyst</bdi>، <bdi dir="ltr">Developer</bdi>، <bdi dir="ltr">Test</bdi> و <bdi dir="ltr">Code</bdi> **درون یک <bdi dir="ltr">Context</bdi>** از آن استفاده می‌کنند.

ویژگی‌های آن:

- در گفت‌وگو و کد یکسان است.
- از رفتار و <bdi dir="ltr">Rule</bdi> حرف می‌زند، نه صرفاً ستون و فرم.
- مثال و ضد‌مثال دارد.
- با کشف <bdi dir="ltr">Domain</bdi> تکامل می‌یابد.
- ابهام را پنهان نمی‌کند؛ آن را به سؤال تبدیل می‌کند.

نمونهٔ ضعیف:

> وضعیت تراکنش آپدیت شد.

پرسش‌های پنهان:

- تراکنش سپرده، <bdi dir="ltr">Payment Order</bdi> یا <bdi dir="ltr">Journal Posting</bdi>؟
- وضعیت از چه چیزی به چه چیزی؟
- چه <bdi dir="ltr">Context</bdi>ی مجاز به این <bdi dir="ltr">Transition</bdi> است؟
- رخداد <bdi dir="ltr">`Executed`</bdi>، <bdi dir="ltr">`Settled`</bdi> یا <bdi dir="ltr">`Posted`</bdi> است؟

نمونهٔ دقیق‌تر در <bdi dir="ltr">Payments:</bdi>

> <bdi dir="ltr">Payment Order</bdi> پس از پذیرش شبکه از <bdi dir="ltr">`Submitted`</bdi> به <bdi dir="ltr">`AcceptedForClearing`</bdi> رفت؛ <bdi dir="ltr">Settlement</bdi> هنوز رخ نداده است.

نام <bdi dir="ltr">State</bdi> و <bdi dir="ltr">Event</bdi> اکنون قابل مدل‌سازی و آزمون است.

## <bdi dir="ltr">5. Ubiquitous Language</bdi>، فرهنگ لغت سراسری نیست

بانک به واژه‌نامهٔ سازمانی برای هماهنگی نیاز دارد، اما یک <bdi dir="ltr">Enterprise Dictionary</bdi> نباید <bdi dir="ltr">Contextual Meaning</bdi> را حذف کند.

روش درست:

- اصطلاح مشترک و شناسهٔ مرجع در سطح سازمان ثبت می‌شود.
- هر <bdi dir="ltr">Context</bdi> معنای دقیق، <bdi dir="ltr">Lifecycle</bdi> و <bdi dir="ltr">Rule</bdi> خودش را اعلام می‌کند.
- تفاوت‌ها در <bdi dir="ltr">Translation Contract</bdi> آشکار می‌شوند.

روش نادرست:

> چون همه از کلمهٔ <bdi dir="ltr">Customer</bdi> استفاده می‌کنند، یک <bdi dir="ltr">`CustomerEntity`</bdi> مشترک در همهٔ سرویس‌ها می‌سازیم.

پیامد:

- تغییر <bdi dir="ltr">KYC</bdi>، <bdi dir="ltr">Marketing Segment</bdi>، <bdi dir="ltr">Borrower Role</bdi> و <bdi dir="ltr">Accounting Party</bdi> به یک <bdi dir="ltr">Schema</bdi> واحد کاپل می‌شود.
- <bdi dir="ltr">Context</bdi>ها فیلدهایی را حمل می‌کنند که معنای آن را نمی‌فهمند.
- <bdi dir="ltr">Owner</bdi> واقعی گم می‌شود.

معمولاً <bdi dir="ltr">Context</bdi>ها به <bdi dir="ltr">`PartyId`</bdi>، یک <bdi dir="ltr">Contract</bdi> و گاهی <bdi dir="ltr">Snapshot</bdi> نیاز دارند؛ نه <bdi dir="ltr">Entity</bdi> داخلی مشترک.

## 6. تفاوت مفاهیم مجاور

| مفهوم | متعلق به | پرسش اصلی | نگاشت با <bdi dir="ltr">Bounded Context</bdi> |
|---|---|---|---|
| <bdi dir="ltr">Domain</bdi> | <bdi dir="ltr">Problem Space</bdi> | حوزهٔ مسئله چیست؟ | می‌تواند چند <bdi dir="ltr">Context</bdi> داشته باشد |
| <bdi dir="ltr">Subdomain</bdi> | <bdi dir="ltr">Problem Space</bdi> | کدام ناحیهٔ دانش/<bdi dir="ltr">Outcome</bdi> متمایز است؟ | هدف، <bdi dir="ltr">Alignment</bdi> مناسب با <bdi dir="ltr">Context</bdi> است |
| <bdi dir="ltr">Bounded Context</bdi> | <bdi dir="ltr">Model/Solution boundary</bdi> | کجا این مدل و زبان معتبر است؟ | موضوع این درس |
| <bdi dir="ltr">Application</bdi> | <bdi dir="ltr">Landscape</bdi> | کدام نرم‌افزار اکنون کار را انجام می‌دهد؟ | می‌تواند چند <bdi dir="ltr">Context</bdi> را مخلوط کند |
| <bdi dir="ltr">Team</bdi> | <bdi dir="ltr">Organization</bdi> | چه کسانی تغییر را انجام می‌دهند؟ | بهتر است مالکیت روشن داشته باشد، ولی مساوی <bdi dir="ltr">Context</bdi> نیست |
| <bdi dir="ltr">Module</bdi> | <bdi dir="ltr">Code</bdi> | کدام مسئولیت در کد محصور است؟ | می‌تواند <bdi dir="ltr">Context</bdi> را در <bdi dir="ltr">Runtime</bdi> واحد پیاده کند |
| <bdi dir="ltr">Service</bdi> | <bdi dir="ltr">Runtime</bdi> | چه چیزی مستقل <bdi dir="ltr">Deploy/Operate</bdi> می‌شود؟ | تصمیم فیزیکی جداگانه است |

یک <bdi dir="ltr">Context</bdi> می‌تواند فعلاً <bdi dir="ltr">Module</bdi> باشد و بعداً <bdi dir="ltr">Service</bdi> شود. یک <bdi dir="ltr">Application Legacy</bdi> ممکن است چند <bdi dir="ltr">Context</bdi> نامنسجم را حمل کند. یک تیم می‌تواند موقتاً مالک چند <bdi dir="ltr">Context</bdi> باشد، ولی هر <bdi dir="ltr">Context</bdi> باید <bdi dir="ltr">Authority</bdi> روشن داشته باشد.

## 7. سرنخ‌های کشف <bdi dir="ltr">Boundary</bdi>

هیچ سرنخ به‌تنهایی اثبات نیست. چند <bdi dir="ltr">Force</bdi> باید کنار هم قرار گیرند.

### <bdi dir="ltr">7.1 Homonym:</bdi> واژهٔ یکسان، معنای متفاوت

<bdi dir="ltr">`Balance`</bdi>:

- <bdi dir="ltr">Available Balance</bdi> در <bdi dir="ltr">Deposits</bdi>
- <bdi dir="ltr">Principal Outstanding</bdi> در <bdi dir="ltr">Lending</bdi>
- <bdi dir="ltr">GL Balance</bdi> در <bdi dir="ltr">Accounting</bdi>
- <bdi dir="ltr">Settlement Position</bdi> در <bdi dir="ltr">Payments</bdi>

اگر همه را یک ستون <bdi dir="ltr">`BALANCE`</bdi> بدانیم، تصمیم‌های عملیاتی و مالی قاطی می‌شوند.

### <bdi dir="ltr">7.2 Synonym:</bdi> واژه‌های متفاوت، مفهوم یکسان

ممکن است دو تیم برای یک مفهوم از <bdi dir="ltr">`Loan Contract`</bdi> و <bdi dir="ltr">`Facility Agreement`</bdi> استفاده کنند. پیش از ساخت دو <bdi dir="ltr">Context</bdi> باید بررسی کنیم آیا واقعاً <bdi dir="ltr">Rule/Lifecycle</bdi> متفاوت است یا صرفاً اختلاف نام تاریخی است.

### <bdi dir="ltr">7.3 Rule Conflict</bdi>

در <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Account</bdi> بسته نباید <bdi dir="ltr">Debit</bdi> عملیاتی جدید بپذیرد. در <bdi dir="ltr">Accounting</bdi>، یک حساب <bdi dir="ltr">GL</bdi> بسته‌شده در دوره ممکن است هنوز برای <bdi dir="ltr">Adjustment</bdi> کنترل‌شده نیاز به <bdi dir="ltr">Posting</bdi> خاص داشته باشد. واژهٔ <bdi dir="ltr">`closed account`</bdi> قواعد متفاوت دارد.

### <bdi dir="ltr">7.4 Lifecycle Conflict</bdi>

<bdi dir="ltr">Product Definition</bdi> می‌تواند <bdi dir="ltr">Version</bdi> جدید بگیرد. <bdi dir="ltr">Agreement</bdi> منعقدشده نباید با تغییر <bdi dir="ltr">Product</bdi> آینده خودکار عوض شود. تفاوت <bdi dir="ltr">Lifecycle</bdi> نشانهٔ قوی جدایی مدل <bdi dir="ltr">Product</bdi> و <bdi dir="ltr">Executed Agreement</bdi> است.

### <bdi dir="ltr">7.5 Authority Conflict</bdi>

اگر <bdi dir="ltr">Lending</bdi> می‌گوید <bdi dir="ltr">Customer eligible</bdi> است و <bdi dir="ltr">Customer Context</bdi> می‌گوید <bdi dir="ltr">KYC</bdi> معتبر است، این‌ها شاید دو <bdi dir="ltr">Decision</bdi> متفاوت باشند:

- <bdi dir="ltr">KYC validity</bdi> متعلق به <bdi dir="ltr">Customer/Compliance</bdi>
- <bdi dir="ltr">Credit eligibility</bdi> متعلق به <bdi dir="ltr">Lending/Credit Decision</bdi>

تلاش برای یک <bdi dir="ltr">Boolean</bdi> مشترک <bdi dir="ltr">`isValidCustomer`</bdi> دو معنای تصمیم را پنهان می‌کند.

### <bdi dir="ltr">7.6 Change Coupling</bdi>

اگر تغییر یک <bdi dir="ltr">Rule</bdi> در <bdi dir="ltr">Product Pricing</bdi> همیشه مجبور است <bdi dir="ltr">Deposit Balance Model</bdi> را <bdi dir="ltr">Release</bdi> کند، <bdi dir="ltr">Boundary</bdi> یا <bdi dir="ltr">Contract</bdi> احتمالاً اطلاعات داخلی را نشت داده است.

## 8. مثال بانکی: <bdi dir="ltr">Product</bdi> و <bdi dir="ltr">Agreement</bdi>

فرض کن محصول مرابحه نسخهٔ 7 این ویژگی‌ها را دارد:

- دامنهٔ مبلغ مجاز
- نرخ/سود مصوب
- مدت‌های قابل انتخاب
- وثایق مجاز
- تاریخ اعتبار نسخه

مشتری در تاریخ مشخص قرارداد می‌بندد. پس از آن نسخهٔ 8 محصول منتشر می‌شود.

دو مدل داریم:

### <bdi dir="ltr">Product Catalog Model</bdi>

- <bdi dir="ltr">Product</bdi> و <bdi dir="ltr">ProductVersion</bdi>
- شرایط قابل عرضه
- <bdi dir="ltr">Eligibility policy</bdi> عمومی
- <bdi dir="ltr">Lifecycle</bdi> انتشار/بازنشستگی نسخه

### <bdi dir="ltr">Executed Agreement Model</bdi>

- طرفین قرارداد
- شرایط قطعی و <bdi dir="ltr">Snapshot</bdi>شده
- تاریخ مؤثر
- تعهدات و وضعیت حقوقی
- اصلاحیه‌های معتبر

اگر <bdi dir="ltr">Agreement</bdi> فقط <bdi dir="ltr">`productId`</bdi> را نگه دارد و هر بار شرایط فعلی <bdi dir="ltr">Product</bdi> را <bdi dir="ltr">Query</bdi> کند، قرارداد گذشته با تغییر آینده عوض می‌شود. <bdi dir="ltr">Boundary</bdi> مناسب، تفاوت بین **<bdi dir="ltr">Reference</bdi>** و **<bdi dir="ltr">Snapshot</bdi>** را آشکار می‌کند.

ممکن است این دو مدل فعلاً در یک <bdi dir="ltr">Deployable Application</bdi> یا حتی یک <bdi dir="ltr">Module</bdi> آموزشی باشند؛ اما زبان و <bdi dir="ltr">Lifecycle</bdi> آن‌ها باید جدا بماند. این مثال نشان می‌دهد <bdi dir="ltr">Mapping</bdi> میان <bdi dir="ltr">Context</bdi>، <bdi dir="ltr">Module</bdi> و <bdi dir="ltr">Service</bdi> الزاماً یک‌به‌یک نیست.

## 9. مثال بانکی: <bdi dir="ltr">Customer</bdi> در سه <bdi dir="ltr">Context</bdi>

### <bdi dir="ltr">Party</bdi> & <bdi dir="ltr">Customer Context</bdi>

- هویت <bdi dir="ltr">Party</bdi>
- نوع شخص حقیقی/حقوقی
- اطلاعات پایه
- وضعیت <bdi dir="ltr">KYC</bdi> و رابطهٔ مشتری

### <bdi dir="ltr">Lending Context</bdi>

- <bdi dir="ltr">Borrower/Obligor role</bdi>
- <bdi dir="ltr">Credit exposure</bdi>
- <bdi dir="ltr">Eligibility</bdi> و <bdi dir="ltr">Risk attributes</bdi> موردنیاز تصمیم
- <bdi dir="ltr">Snapshot</bdi> شواهد تصمیم در زمان اعطا

### <bdi dir="ltr">Accounting Context</bdi>

- <bdi dir="ltr">Party/Customer reference</bdi> برای تفصیل، گزارش یا <bdi dir="ltr">Audit</bdi>
- نه مالک <bdi dir="ltr">KYC</bdi>
- نه مالک <bdi dir="ltr">Credit Eligibility</bdi>

یک <bdi dir="ltr">`CustomerId`</bdi> مشترک می‌تواند <bdi dir="ltr">Correlation</bdi> ایجاد کند؛ اما مدل <bdi dir="ltr">Customer</bdi> در هر <bdi dir="ltr">Context</bdi> متفاوت است. <bdi dir="ltr">Lending</bdi> نباید اطلاعات هویتی را بدون <bdi dir="ltr">Contract</bdi> تغییر دهد و <bdi dir="ltr">Accounting</bdi> نباید از روی <bdi dir="ltr">Journal</bdi> تصمیم بگیرد <bdi dir="ltr">Customer</bdi> از نظر <bdi dir="ltr">KYC</bdi> معتبر است.

## <bdi dir="ltr">10. Boundary Hypothesis</bdi> چگونه نوشته می‌شود؟

یک <bdi dir="ltr">Boundary</bdi> خوب از روی اسم انتخاب نمی‌شود. قالب:

> به‌دلیل تفاوت در [<bdi dir="ltr">Language/Rules/Lifecycle/Authority/Change</bdi>]، فرض می‌کنیم مدل A و B در دو <bdi dir="ltr">Bounded Context</bdi> قرار گیرند. این فرض با [مصاحبه، مثال، تغییر واقعی، تست] اعتبارسنجی می‌شود. <bdi dir="ltr">Counter-evidence</bdi> فعلی [X] است.

نمونه:

> به‌دلیل تفاوت <bdi dir="ltr">Lifecycle</bdi> میان <bdi dir="ltr">ProductVersion</bdi> و <bdi dir="ltr">ExecutedAgreement</bdi> و نیاز به ثابت‌ماندن شروط قرارداد، فرض می‌کنیم <bdi dir="ltr">Product Catalog</bdi> و <bdi dir="ltr">Agreement Management</bdi> دو <bdi dir="ltr">Context</bdi> متمایزند. این فرض با بررسی سناریوی اصلاح محصول، الحاقیهٔ قرارداد و <bdi dir="ltr">Owner</bdi> تصمیم اعتبارسنجی می‌شود. <bdi dir="ltr">Counter-evidence:</bdi> در ساختار فعلی یک تیم و یک <bdi dir="ltr">Database</bdi> هر دو را نگه می‌دارند.

ساختار فعلی <bdi dir="ltr">Counter-evidence</bdi> یا <bdi dir="ltr">Constraint</bdi> است؛ ولی به‌تنهایی مدل مسئله را رد نمی‌کند.

## 11. خطاهای رایج

### <bdi dir="ltr">Context</bdi> را با <bdi dir="ltr">Namespace</bdi> یکی گرفتن

ساخت <bdi dir="ltr">Package</bdi> یک <bdi dir="ltr">Boundary</bdi> را <bdi dir="ltr">enforce</bdi> می‌کند، اما وجود <bdi dir="ltr">Package</bdi> دلیل دامینی آن نیست.

### <bdi dir="ltr">Context</bdi> را با تیم یکی گرفتن

<bdi dir="ltr">Team Topology</bdi> مهم است، ولی چارت تاریخی نمی‌تواند تعریف مدل را به‌تنهایی تعیین کند.

### یک مدل <bdi dir="ltr">Canonical</bdi> برای کل بانک

<bdi dir="ltr">Canonical Enterprise Model</bdi> اغلب تفاوت معناها را با فیلد <bdi dir="ltr">Optional</bdi> پنهان می‌کند. <bdi dir="ltr">Published Language</bdi> برای <bdi dir="ltr">Integration</bdi> با <bdi dir="ltr">Universal Domain Model</bdi> یکی نیست.

### مرز بر اساس <bdi dir="ltr">CRUD</bdi>

<bdi dir="ltr">`CustomerCRUDContext`</bdi> دربارهٔ رفتار و دانش چیزی نمی‌گوید. <bdi dir="ltr">Use Case</bdi> و <bdi dir="ltr">Rule</bdi> باید مرز را روشن کنند.

### هر تفاوت واژه یک <bdi dir="ltr">Context</bdi>

اختلاف نام ممکن است فقط <bdi dir="ltr">Synonym</bdi> باشد. <bdi dir="ltr">Context</bdi> جدید هزینهٔ ترجمه، <bdi dir="ltr">Governance</bdi> و <bdi dir="ltr">Integration</bdi> دارد و نیازمند چند شاهد است.

### یک <bdi dir="ltr">Context</bdi> برابر یک <bdi dir="ltr">Microservice</bdi>

<bdi dir="ltr">Bounded Context</bdi> یک <bdi dir="ltr">Boundary</bdi> مدل است؛ <bdi dir="ltr">Microservice Boundary</bdi> علاوه بر آن به <bdi dir="ltr">Scale</bdi>، <bdi dir="ltr">Team Autonomy</bdi>، <bdi dir="ltr">Availability</bdi>، <bdi dir="ltr">Data</bdi> و <bdi dir="ltr">Operations</bdi> پاسخ می‌دهد.

## 12. تمرین هدایت‌شده

برای واژهٔ <bdi dir="ltr">`Transaction`</bdi> سه معنا بنویس:

1. <bdi dir="ltr">Deposits</bdi>
2. <bdi dir="ltr">Payments</bdi>
3. <bdi dir="ltr">Accounting</bdi>

برای هرکدام پاسخ بده:

- <bdi dir="ltr">Trigger</bdi> چیست؟
- <bdi dir="ltr">Lifecycle</bdi> چیست؟
- <bdi dir="ltr">Completion</bdi> چه معنایی دارد؟
- <bdi dir="ltr">Owner</bdi> وضعیت کیست؟

اگر پاسخ‌ها یکسان نیستند، یک <bdi dir="ltr">Entity</bdi> مشترک <bdi dir="ltr">`Transaction`</bdi> احتمالاً مدل ضعیفی است.

## 13. تمرین مستقل

[<bdi dir="ltr">Day 02 Exercise</bdi> — <bdi dir="ltr">Language Conflicts</bdi>](../exercises/day-02-language-conflicts.md) را انجام بده. حداقل پنج اصطلاح را در دو یا چند <bdi dir="ltr">Context</bdi> تحلیل کن و برای دو <bdi dir="ltr">Boundary Hypothesis</bdi> شواهد موافق و مخالف بنویس.

## 14. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تعریف دقیق <bdi dir="ltr">Bounded Context</bdi> | ۲ |
| تشخیص معنای <bdi dir="ltr">Contextual</bdi> واژه‌ها | ۲ |
| تفکیک <bdi dir="ltr">Context</bdi> از <bdi dir="ltr">Domain/System/Module/Service</bdi> | ۲ |
| <bdi dir="ltr">Boundary Hypothesis</bdi> با چند <bdi dir="ltr">Force</bdi> | ۳ |
| ثبت <bdi dir="ltr">Counter-evidence/Open Question</bdi> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 15. آزمون خروج

درس را ببند و [<bdi dir="ltr">Day 02 Exit Ticket</bdi>](../quizzes/day-02-exit-ticket.md) را پاسخ بده.

## 16. منبع اصلی

- [<bdi dir="ltr">Domain-Driven Design Reference</bdi> — <bdi dir="ltr">Bounded Context and Ubiquitous Language</bdi>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

تعریف‌ها از مرجع <bdi dir="ltr">DDD</bdi> گرفته شده‌اند؛ مثال‌ها و <bdi dir="ltr">Boundary</bdi>های بانکی این درس، مدل آموزشی و <bdi dir="ltr">Hypothesis</bdi> هستند.

</div>
