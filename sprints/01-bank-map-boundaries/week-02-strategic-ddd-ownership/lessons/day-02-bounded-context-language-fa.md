<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 02</span> — <span dir="ltr">Bounded Context</span> و <span dir="ltr">Ubiquitous Language</span>

- <span dir="ltr">Day budget: 45 minutes including exercise and exit ticket</span>
- <span dir="ltr">Output: Language Conflicts v0.1</span> و <span dir="ltr">Boundary Hypotheses</span>
- <span dir="ltr">Banking case:</span> تفاوت معنای <span dir="ltr">Account</span>، <span dir="ltr">Customer</span>، <span dir="ltr">Product</span>، <span dir="ltr">Contract</span> و <span dir="ltr">Balance</span>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Bounded Context</span> را به‌عنوان مرز اعتبار مدل و زبان تعریف کنی.
2. آن را از <span dir="ltr">Domain</span>، <span dir="ltr">Subdomain</span>، <span dir="ltr">Application</span>، <span dir="ltr">Team</span>، <span dir="ltr">Module</span> و <span dir="ltr">Microservice</span> جدا کنی.
3. <span dir="ltr">Homonym</span>، <span dir="ltr">Synonym</span>، <span dir="ltr">Rule Conflict</span> و <span dir="ltr">Lifecycle Conflict</span> را به‌عنوان سرنخ مرز کشف کنی.
4. برای یک واژهٔ بانکی، معنای <span dir="ltr">Contextual</span> و ترجمهٔ لازم را بنویسی.
5. یک <span dir="ltr">Boundary Hypothesis</span> بسازی و شواهد موافق و مخالف آن را ثبت کنی.

## 2. مدل ذهنی

در بانک، کلمات مشترک الزاماً مفهوم مشترک ندارند. مشکل وقتی شروع می‌شود که یک واژهٔ واحد را به یک <span dir="ltr">Entity</span> سازمانی عظیم تبدیل کنیم.

واژهٔ <span dir="ltr">`Account`</span> را ببین:

- در <span dir="ltr">Deposits:</span> رابطهٔ عملیاتی نگهداری وجوه، وضعیت، مانده و محدودیت‌ها
- در <span dir="ltr">Lending:</span> موقعیت بدهی یا <span dir="ltr">Facility</span> و برنامهٔ بازپرداخت
- در <span dir="ltr">Accounting:</span> حساب دفتر کل، معین یا تفصیلی برای طبقه‌بندی آثار مالی
- در <span dir="ltr">IAM:</span> حساب کاربری و دسترسی

این‌ها چهار <span dir="ltr">View</span> از یک <span dir="ltr">Entity</span> واحد نیستند. مدل، رفتار، شناسه، <span dir="ltr">Lifecycle</span> و <span dir="ltr">Invariant</span> آن‌ها متفاوت است.

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


## 3. تعریف دقیق <span dir="ltr">Bounded Context</span>

<span dir="ltr">Bounded Context</span> مرزی صریح است که **درون آن یک مدل مشخص و <span dir="ltr">Ubiquitous Language</span> مرتبط با آن، معنای سازگار و معتبر دارد**.

سه کلمهٔ تعریف مهم‌اند:

- <span dir="ltr">`Boundary`</span>: معلوم است مدل کجا معتبر است و کجا نیست.
- <span dir="ltr">`Model`</span>: فقط <span dir="ltr">Vocabulary</span> نیست؛ مفاهیم، روابط، رفتارها و قواعد را دربر می‌گیرد.
- <span dir="ltr">`Consistency`</span>: یک اصطلاح درون <span dir="ltr">Context</span> نباید چند معنای متناقض داشته باشد.

<span dir="ltr">Bounded Context</span> خودش «معنای یک واژه» نیست. مثلاً «معنای قرارداد در حسابداری» یک <span dir="ltr">Context</span> نیست؛ <span dir="ltr">`Financial Accounting Context`</span> مرزی است که در آن <span dir="ltr">Contract</span> ممکن است فقط <span dir="ltr">Reference</span> یا <span dir="ltr">Accounting Dimension</span> باشد.

## <span dir="ltr">4. Ubiquitous Language</span> چیست؟

<span dir="ltr">Ubiquitous Language</span> زبانی دقیق است که <span dir="ltr">Domain Expert</span>، <span dir="ltr">Analyst</span>، <span dir="ltr">Developer</span>، <span dir="ltr">Test</span> و <span dir="ltr">Code</span> **درون یک <span dir="ltr">Context</span>** از آن استفاده می‌کنند.

ویژگی‌های آن:

- در گفت‌وگو و کد یکسان است.
- از رفتار و <span dir="ltr">Rule</span> حرف می‌زند، نه صرفاً ستون و فرم.
- مثال و ضد‌مثال دارد.
- با کشف <span dir="ltr">Domain</span> تکامل می‌یابد.
- ابهام را پنهان نمی‌کند؛ آن را به سؤال تبدیل می‌کند.

نمونهٔ ضعیف:

> وضعیت تراکنش آپدیت شد.

پرسش‌های پنهان:

- تراکنش سپرده، <span dir="ltr">Payment Order</span> یا <span dir="ltr">Journal Posting</span>؟
- وضعیت از چه چیزی به چه چیزی؟
- چه <span dir="ltr">Context</span>ی مجاز به این <span dir="ltr">Transition</span> است؟
- رخداد <span dir="ltr">`Executed`</span>، <span dir="ltr">`Settled`</span> یا <span dir="ltr">`Posted`</span> است؟

نمونهٔ دقیق‌تر در <span dir="ltr">Payments:</span>

> <span dir="ltr">Payment Order</span> پس از پذیرش شبکه از <span dir="ltr">`Submitted`</span> به <span dir="ltr">`AcceptedForClearing`</span> رفت؛ <span dir="ltr">Settlement</span> هنوز رخ نداده است.

نام <span dir="ltr">State</span> و <span dir="ltr">Event</span> اکنون قابل مدل‌سازی و آزمون است.

## <span dir="ltr">5. Ubiquitous Language</span>، فرهنگ لغت سراسری نیست

بانک به واژه‌نامهٔ سازمانی برای هماهنگی نیاز دارد، اما یک <span dir="ltr">Enterprise Dictionary</span> نباید <span dir="ltr">Contextual Meaning</span> را حذف کند.

روش درست:

- اصطلاح مشترک و شناسهٔ مرجع در سطح سازمان ثبت می‌شود.
- هر <span dir="ltr">Context</span> معنای دقیق، <span dir="ltr">Lifecycle</span> و <span dir="ltr">Rule</span> خودش را اعلام می‌کند.
- تفاوت‌ها در <span dir="ltr">Translation Contract</span> آشکار می‌شوند.

روش نادرست:

> چون همه از کلمهٔ <span dir="ltr">Customer</span> استفاده می‌کنند، یک <span dir="ltr">`CustomerEntity`</span> مشترک در همهٔ سرویس‌ها می‌سازیم.

پیامد:

- تغییر <span dir="ltr">KYC</span>، <span dir="ltr">Marketing Segment</span>، <span dir="ltr">Borrower Role</span> و <span dir="ltr">Accounting Party</span> به یک <span dir="ltr">Schema</span> واحد کاپل می‌شود.
- <span dir="ltr">Context</span>ها فیلدهایی را حمل می‌کنند که معنای آن را نمی‌فهمند.
- <span dir="ltr">Owner</span> واقعی گم می‌شود.

معمولاً <span dir="ltr">Context</span>ها به <span dir="ltr">`PartyId`</span>، یک <span dir="ltr">Contract</span> و گاهی <span dir="ltr">Snapshot</span> نیاز دارند؛ نه <span dir="ltr">Entity</span> داخلی مشترک.

## 6. تفاوت مفاهیم مجاور

| مفهوم | متعلق به | پرسش اصلی | نگاشت با <span dir="ltr">Bounded Context</span> |
|---|---|---|---|
| <span dir="ltr">Domain</span> | <span dir="ltr">Problem Space</span> | حوزهٔ مسئله چیست؟ | می‌تواند چند <span dir="ltr">Context</span> داشته باشد |
| <span dir="ltr">Subdomain</span> | <span dir="ltr">Problem Space</span> | کدام ناحیهٔ دانش/<span dir="ltr">Outcome</span> متمایز است؟ | هدف، <span dir="ltr">Alignment</span> مناسب با <span dir="ltr">Context</span> است |
| <span dir="ltr">Bounded Context</span> | <span dir="ltr">Model/Solution boundary</span> | کجا این مدل و زبان معتبر است؟ | موضوع این درس |
| <span dir="ltr">Application</span> | <span dir="ltr">Landscape</span> | کدام نرم‌افزار اکنون کار را انجام می‌دهد؟ | می‌تواند چند <span dir="ltr">Context</span> را مخلوط کند |
| <span dir="ltr">Team</span> | <span dir="ltr">Organization</span> | چه کسانی تغییر را انجام می‌دهند؟ | بهتر است مالکیت روشن داشته باشد، ولی مساوی <span dir="ltr">Context</span> نیست |
| <span dir="ltr">Module</span> | <span dir="ltr">Code</span> | کدام مسئولیت در کد محصور است؟ | می‌تواند <span dir="ltr">Context</span> را در <span dir="ltr">Runtime</span> واحد پیاده کند |
| <span dir="ltr">Service</span> | <span dir="ltr">Runtime</span> | چه چیزی مستقل <span dir="ltr">Deploy/Operate</span> می‌شود؟ | تصمیم فیزیکی جداگانه است |

یک <span dir="ltr">Context</span> می‌تواند فعلاً <span dir="ltr">Module</span> باشد و بعداً <span dir="ltr">Service</span> شود. یک <span dir="ltr">Application Legacy</span> ممکن است چند <span dir="ltr">Context</span> نامنسجم را حمل کند. یک تیم می‌تواند موقتاً مالک چند <span dir="ltr">Context</span> باشد، ولی هر <span dir="ltr">Context</span> باید <span dir="ltr">Authority</span> روشن داشته باشد.

## 7. سرنخ‌های کشف <span dir="ltr">Boundary</span>

هیچ سرنخ به‌تنهایی اثبات نیست. چند <span dir="ltr">Force</span> باید کنار هم قرار گیرند.

### <span dir="ltr">7.1 Homonym:</span> واژهٔ یکسان، معنای متفاوت

<span dir="ltr">`Balance`</span>:

- <span dir="ltr">Available Balance</span> در <span dir="ltr">Deposits</span>
- <span dir="ltr">Principal Outstanding</span> در <span dir="ltr">Lending</span>
- <span dir="ltr">GL Balance</span> در <span dir="ltr">Accounting</span>
- <span dir="ltr">Settlement Position</span> در <span dir="ltr">Payments</span>

اگر همه را یک ستون <span dir="ltr">`BALANCE`</span> بدانیم، تصمیم‌های عملیاتی و مالی قاطی می‌شوند.

### <span dir="ltr">7.2 Synonym:</span> واژه‌های متفاوت، مفهوم یکسان

ممکن است دو تیم برای یک مفهوم از <span dir="ltr">`Loan Contract`</span> و <span dir="ltr">`Facility Agreement`</span> استفاده کنند. پیش از ساخت دو <span dir="ltr">Context</span> باید بررسی کنیم آیا واقعاً <span dir="ltr">Rule/Lifecycle</span> متفاوت است یا صرفاً اختلاف نام تاریخی است.

### <span dir="ltr">7.3 Rule Conflict</span>

در <span dir="ltr">Deposits</span>، <span dir="ltr">Account</span> بسته نباید <span dir="ltr">Debit</span> عملیاتی جدید بپذیرد. در <span dir="ltr">Accounting</span>، یک حساب <span dir="ltr">GL</span> بسته‌شده در دوره ممکن است هنوز برای <span dir="ltr">Adjustment</span> کنترل‌شده نیاز به <span dir="ltr">Posting</span> خاص داشته باشد. واژهٔ <span dir="ltr">`closed account`</span> قواعد متفاوت دارد.

### <span dir="ltr">7.4 Lifecycle Conflict</span>

<span dir="ltr">Product Definition</span> می‌تواند <span dir="ltr">Version</span> جدید بگیرد. <span dir="ltr">Agreement</span> منعقدشده نباید با تغییر <span dir="ltr">Product</span> آینده خودکار عوض شود. تفاوت <span dir="ltr">Lifecycle</span> نشانهٔ قوی جدایی مدل <span dir="ltr">Product</span> و <span dir="ltr">Executed Agreement</span> است.

### <span dir="ltr">7.5 Authority Conflict</span>

اگر <span dir="ltr">Lending</span> می‌گوید <span dir="ltr">Customer eligible</span> است و <span dir="ltr">Customer Context</span> می‌گوید <span dir="ltr">KYC</span> معتبر است، این‌ها شاید دو <span dir="ltr">Decision</span> متفاوت باشند:

- <span dir="ltr">KYC validity</span> متعلق به <span dir="ltr">Customer/Compliance</span>
- <span dir="ltr">Credit eligibility</span> متعلق به <span dir="ltr">Lending/Credit Decision</span>

تلاش برای یک <span dir="ltr">Boolean</span> مشترک <span dir="ltr">`isValidCustomer`</span> دو معنای تصمیم را پنهان می‌کند.

### <span dir="ltr">7.6 Change Coupling</span>

اگر تغییر یک <span dir="ltr">Rule</span> در <span dir="ltr">Product Pricing</span> همیشه مجبور است <span dir="ltr">Deposit Balance Model</span> را <span dir="ltr">Release</span> کند، <span dir="ltr">Boundary</span> یا <span dir="ltr">Contract</span> احتمالاً اطلاعات داخلی را نشت داده است.

## 8. مثال بانکی: <span dir="ltr">Product</span> و <span dir="ltr">Agreement</span>

فرض کن محصول مرابحه نسخهٔ 7 این ویژگی‌ها را دارد:

- دامنهٔ مبلغ مجاز
- نرخ/سود مصوب
- مدت‌های قابل انتخاب
- وثایق مجاز
- تاریخ اعتبار نسخه

مشتری در تاریخ مشخص قرارداد می‌بندد. پس از آن نسخهٔ 8 محصول منتشر می‌شود.

دو مدل داریم:

### <span dir="ltr">Product Catalog Model</span>

- <span dir="ltr">Product</span> و <span dir="ltr">ProductVersion</span>
- شرایط قابل عرضه
- <span dir="ltr">Eligibility policy</span> عمومی
- <span dir="ltr">Lifecycle</span> انتشار/بازنشستگی نسخه

### <span dir="ltr">Executed Agreement Model</span>

- طرفین قرارداد
- شرایط قطعی و <span dir="ltr">Snapshot</span>شده
- تاریخ مؤثر
- تعهدات و وضعیت حقوقی
- اصلاحیه‌های معتبر

اگر <span dir="ltr">Agreement</span> فقط <span dir="ltr">`productId`</span> را نگه دارد و هر بار شرایط فعلی <span dir="ltr">Product</span> را <span dir="ltr">Query</span> کند، قرارداد گذشته با تغییر آینده عوض می‌شود. <span dir="ltr">Boundary</span> مناسب، تفاوت بین **<span dir="ltr">Reference</span>** و **<span dir="ltr">Snapshot</span>** را آشکار می‌کند.

ممکن است این دو مدل فعلاً در یک <span dir="ltr">Deployable Application</span> یا حتی یک <span dir="ltr">Module</span> آموزشی باشند؛ اما زبان و <span dir="ltr">Lifecycle</span> آن‌ها باید جدا بماند. این مثال نشان می‌دهد <span dir="ltr">Mapping</span> میان <span dir="ltr">Context</span>، <span dir="ltr">Module</span> و <span dir="ltr">Service</span> الزاماً یک‌به‌یک نیست.

## 9. مثال بانکی: <span dir="ltr">Customer</span> در سه <span dir="ltr">Context</span>

### <span dir="ltr">Party</span> & <span dir="ltr">Customer Context</span>

- هویت <span dir="ltr">Party</span>
- نوع شخص حقیقی/حقوقی
- اطلاعات پایه
- وضعیت <span dir="ltr">KYC</span> و رابطهٔ مشتری

### <span dir="ltr">Lending Context</span>

- <span dir="ltr">Borrower/Obligor role</span>
- <span dir="ltr">Credit exposure</span>
- <span dir="ltr">Eligibility</span> و <span dir="ltr">Risk attributes</span> موردنیاز تصمیم
- <span dir="ltr">Snapshot</span> شواهد تصمیم در زمان اعطا

### <span dir="ltr">Accounting Context</span>

- <span dir="ltr">Party/Customer reference</span> برای تفصیل، گزارش یا <span dir="ltr">Audit</span>
- نه مالک <span dir="ltr">KYC</span>
- نه مالک <span dir="ltr">Credit Eligibility</span>

یک <span dir="ltr">`CustomerId`</span> مشترک می‌تواند <span dir="ltr">Correlation</span> ایجاد کند؛ اما مدل <span dir="ltr">Customer</span> در هر <span dir="ltr">Context</span> متفاوت است. <span dir="ltr">Lending</span> نباید اطلاعات هویتی را بدون <span dir="ltr">Contract</span> تغییر دهد و <span dir="ltr">Accounting</span> نباید از روی <span dir="ltr">Journal</span> تصمیم بگیرد <span dir="ltr">Customer</span> از نظر <span dir="ltr">KYC</span> معتبر است.

## <span dir="ltr">10. Boundary Hypothesis</span> چگونه نوشته می‌شود؟

یک <span dir="ltr">Boundary</span> خوب از روی اسم انتخاب نمی‌شود. قالب:

> به‌دلیل تفاوت در [<span dir="ltr">Language/Rules/Lifecycle/Authority/Change</span>]، فرض می‌کنیم مدل A و B در دو <span dir="ltr">Bounded Context</span> قرار گیرند. این فرض با [مصاحبه، مثال، تغییر واقعی، تست] اعتبارسنجی می‌شود. <span dir="ltr">Counter-evidence</span> فعلی [X] است.

نمونه:

> به‌دلیل تفاوت <span dir="ltr">Lifecycle</span> میان <span dir="ltr">ProductVersion</span> و <span dir="ltr">ExecutedAgreement</span> و نیاز به ثابت‌ماندن شروط قرارداد، فرض می‌کنیم <span dir="ltr">Product Catalog</span> و <span dir="ltr">Agreement Management</span> دو <span dir="ltr">Context</span> متمایزند. این فرض با بررسی سناریوی اصلاح محصول، الحاقیهٔ قرارداد و <span dir="ltr">Owner</span> تصمیم اعتبارسنجی می‌شود. <span dir="ltr">Counter-evidence:</span> در ساختار فعلی یک تیم و یک <span dir="ltr">Database</span> هر دو را نگه می‌دارند.

ساختار فعلی <span dir="ltr">Counter-evidence</span> یا <span dir="ltr">Constraint</span> است؛ ولی به‌تنهایی مدل مسئله را رد نمی‌کند.

## 11. خطاهای رایج

### <span dir="ltr">Context</span> را با <span dir="ltr">Namespace</span> یکی گرفتن

ساخت <span dir="ltr">Package</span> یک <span dir="ltr">Boundary</span> را <span dir="ltr">enforce</span> می‌کند، اما وجود <span dir="ltr">Package</span> دلیل دامینی آن نیست.

### <span dir="ltr">Context</span> را با تیم یکی گرفتن

<span dir="ltr">Team Topology</span> مهم است، ولی چارت تاریخی نمی‌تواند تعریف مدل را به‌تنهایی تعیین کند.

### یک مدل <span dir="ltr">Canonical</span> برای کل بانک

<span dir="ltr">Canonical Enterprise Model</span> اغلب تفاوت معناها را با فیلد <span dir="ltr">Optional</span> پنهان می‌کند. <span dir="ltr">Published Language</span> برای <span dir="ltr">Integration</span> با <span dir="ltr">Universal Domain Model</span> یکی نیست.

### مرز بر اساس <span dir="ltr">CRUD</span>

<span dir="ltr">`CustomerCRUDContext`</span> دربارهٔ رفتار و دانش چیزی نمی‌گوید. <span dir="ltr">Use Case</span> و <span dir="ltr">Rule</span> باید مرز را روشن کنند.

### هر تفاوت واژه یک <span dir="ltr">Context</span>

اختلاف نام ممکن است فقط <span dir="ltr">Synonym</span> باشد. <span dir="ltr">Context</span> جدید هزینهٔ ترجمه، <span dir="ltr">Governance</span> و <span dir="ltr">Integration</span> دارد و نیازمند چند شاهد است.

### یک <span dir="ltr">Context</span> برابر یک <span dir="ltr">Microservice</span>

<span dir="ltr">Bounded Context</span> یک <span dir="ltr">Boundary</span> مدل است؛ <span dir="ltr">Microservice Boundary</span> علاوه بر آن به <span dir="ltr">Scale</span>، <span dir="ltr">Team Autonomy</span>، <span dir="ltr">Availability</span>، <span dir="ltr">Data</span> و <span dir="ltr">Operations</span> پاسخ می‌دهد.

## 12. تمرین هدایت‌شده

برای واژهٔ <span dir="ltr">`Transaction`</span> سه معنا بنویس:

1. <span dir="ltr">Deposits</span>
2. <span dir="ltr">Payments</span>
3. <span dir="ltr">Accounting</span>

برای هرکدام پاسخ بده:

- <span dir="ltr">Trigger</span> چیست؟
- <span dir="ltr">Lifecycle</span> چیست؟
- <span dir="ltr">Completion</span> چه معنایی دارد؟
- <span dir="ltr">Owner</span> وضعیت کیست؟

اگر پاسخ‌ها یکسان نیستند، یک <span dir="ltr">Entity</span> مشترک <span dir="ltr">`Transaction`</span> احتمالاً مدل ضعیفی است.

## 13. تمرین مستقل

[<span dir="ltr">Day 02 Exercise</span> — <span dir="ltr">Language Conflicts</span>](../exercises/day-02-language-conflicts.md) را انجام بده. حداقل پنج اصطلاح را در دو یا چند <span dir="ltr">Context</span> تحلیل کن و برای دو <span dir="ltr">Boundary Hypothesis</span> شواهد موافق و مخالف بنویس.

## 14. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تعریف دقیق <span dir="ltr">Bounded Context</span> | ۲ |
| تشخیص معنای <span dir="ltr">Contextual</span> واژه‌ها | ۲ |
| تفکیک <span dir="ltr">Context</span> از <span dir="ltr">Domain/System/Module/Service</span> | ۲ |
| <span dir="ltr">Boundary Hypothesis</span> با چند <span dir="ltr">Force</span> | ۳ |
| ثبت <span dir="ltr">Counter-evidence/Open Question</span> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 15. آزمون خروج

درس را ببند و [<span dir="ltr">Day 02 Exit Ticket</span>](../quizzes/day-02-exit-ticket.md) را پاسخ بده.

## 16. منبع اصلی

- [<span dir="ltr">Domain-Driven Design Reference</span> — <span dir="ltr">Bounded Context and Ubiquitous Language</span>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

تعریف‌ها از مرجع <span dir="ltr">DDD</span> گرفته شده‌اند؛ مثال‌ها و <span dir="ltr">Boundary</span>های بانکی این درس، مدل آموزشی و <span dir="ltr">Hypothesis</span> هستند.

</div>
