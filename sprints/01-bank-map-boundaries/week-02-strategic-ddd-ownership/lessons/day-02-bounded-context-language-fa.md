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

### <bdi dir="ltr">7.3 Rule Conflict</bdu�6����k�w��y</bdi> | <bdi dir="ltr">Deposits decides whether account can accept credit now</bdi> |
| <bdi dir="ltr">State owner</bdi> | <bdi dir="ltr">Deposits records transaction and updates its balance</bdi> |
| <bdi dir="ltr">Resulting fact</bdi> | <bdi dir="ltr">`DepositCredited`</bdi> <bdi dir="ltr">or explicit rejection fact/result</bdi> |
| <bdi dir="ltr">Process observer</bdi> | <bdi dir="ltr">Lending/Process Manager advances its own status</bdi> |
| <bdi dir="ltr">Financial consumer</bdi> | <bdi dir="ltr">Accounting produces relevant Journal from valid facts</bdi> |

این تفکیک مانع آن می‌شود که <bdi dir="ltr">Orchestrator</bdi> به <bdi dir="ltr">Super-Domain</bdi> و مالک همه‌چیز تبدیل شود.

## <bdi dir="ltr">11. Correction</bdi> و <bdi dir="ltr">Reconciliation</bdi> بخشی از <bdi dir="ltr">Ownership</bdi> است

<bdi dir="ltr">Owner</bdi> فقط <bdi dir="ltr">Happy Path</bdi> را مالک نیست. باید روشن باشد:

- چه کسی خطا را تشخیص می‌دهد؟
- چه کسی مجاز به <bdi dir="ltr">Correction</bdi> است؟
- <bdi dir="ltr">Correction</bdi> با <bdi dir="ltr">Update</bdi>، <bdi dir="ltr">Reversal</bdi> یا <bdi dir="ltr">Compensating Fact</bdi> انجام می‌شود؟
- <bdi dir="ltr">Audit trail</bdi> کجاست؟
- چه کسی اختلاف میان <bdi dir="ltr">Operational</bdi> و <bdi dir="ltr">Accounting Projection</bdi> را پیگیری می‌کند؟

جزئیات <bdi dir="ltr">Accounting/Reversal</bdi> در <bdi dir="ltr">Sprint</bdi>های بعد می‌آید، اما در <bdi dir="ltr">Matrix</bdi> حداقل <bdi dir="ltr">`Reconciliation owner`</bdi> و <bdi dir="ltr">`Open Question`</bdi> باید ثبت شود.

## 12. خطاهای رایج

### مالکیت مشترک

«<bdi dir="ltr">Lending</bdi> و <bdi dir="ltr">Accounting</bdi> هر دو مالک ماندهٔ تسهیلات‌اند» ابهام <bdi dir="ltr">Semantic</bdi> را پنهان می‌کند. دو مانده را نام‌گذاری کن.

### <bdi dir="ltr">Database</bdi> برابر <bdi dir="ltr">Owner</bdi>

داشتن جدول یا <bdi dir="ltr">Replica</bdi> به معنی <bdi dir="ltr">Authority</bdi> نیست. در <bdi dir="ltr">Migration</bdi> ممکن است رکورد فیزیکی موقتاً جای دیگری باشد.

### <bdi dir="ltr">Event Consumer</bdi> برابر <bdi dir="ltr">Owner</bdi>

<bdi dir="ltr">Accounting</bdi> با مصرف <bdi dir="ltr">`LoanGranted`</bdi> مالک <bdi dir="ltr">Loan</bdi> نمی‌شود. <bdi dir="ltr">Projection</bdi> نیز <bdi dir="ltr">Authority</bdi> نمی‌سازد.

### <bdi dir="ltr">Orchestrator</bdi> برابر <bdi dir="ltr">Owner</bdi>

<bdi dir="ltr">Process Manager Step Status</bdi> را نگه می‌دارد؛ <bdi dir="ltr">Fact</bdi>های <bdi dir="ltr">Domain</bdi> را جعل یا تصاحب نمی‌کند.

### <bdi dir="ltr">Snapshot</bdi> بدون زمان و <bdi dir="ltr">Version</bdi>

کپی بدون <bdi dir="ltr">Provenance</bdi> به‌سرعت به <bdi dir="ltr">Master</bdi> پنهان و متناقض تبدیل می‌شود.

### «همه‌چیز را همگام <bdi dir="ltr">Query</bdi> کنیم»

<bdi dir="ltr">Query</bdi> زنده برای <bdi dir="ltr">Product terms</bdi> قرارداد گذشته یا شواهد تصمیم می‌تواند تاریخچه را خراب کند. <bdi dir="ltr">Reference</bdi>، <bdi dir="ltr">Snapshot</bdi> و <bdi dir="ltr">Cache</bdi> باید بر اساس <bdi dir="ltr">Use Case</bdi> انتخاب شوند.

### <bdi dir="ltr">RACI</bdi> به‌جای <bdi dir="ltr">Data Authority</bdi>

<bdi dir="ltr">RACI</bdi> سازمانی مفید است، ولی نمی‌گوید کدام <bdi dir="ltr">Context</bdi> مجاز به <bdi dir="ltr">Transition State</bdi> و انتشار <bdi dir="ltr">Fact</bdi> است. هر دو <bdi dir="ltr">Artifact</bdi> ممکن است لازم باشند.

## 13. روش تکمیل <bdi dir="ltr">Ownership Matrix</bdi>

برای هر ردیف:

1. <bdi dir="ltr">Semantic</bdi> را آن‌قدر دقیق کن که یک <bdi dir="ltr">Fact</bdi> باشد.
2. <bdi dir="ltr">Context Authority</bdi> را انتخاب کن.
3. دیگر <bdi dir="ltr">Context</bdi>ها را <bdi dir="ltr">`Reference/Snapshot/Projection/Cache/Consumer/Not Allowed`</bdi> علامت بزن.
4. <bdi dir="ltr">Freshness</bdi> و <bdi dir="ltr">History rule</bdi> را ثبت کن.
5. <bdi dir="ltr">Decision</bdi>های وابسته را جدا بنویس.
6. <bdi dir="ltr">Reconciliation owner</bdi> و <bdi dir="ltr">Correction path</bdi> را مشخص یا <bdi dir="ltr">Open Question</bdi> کن.
7. با یک <bdi dir="ltr">Failure</bdi> یا <bdi dir="ltr">Change</bdi> واقعی تصمیم را آزمایش کن.

## 14. تمرین هدایت‌شده

برای <bdi dir="ltr">`Product Definition`</bdi> و <bdi dir="ltr">`Executed Agreement Terms`</bdi> دو ردیف مستقل بساز. اگر <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">Lifecycle</bdi> هر دو را یکی نوشتی، سناریوی انتشار <bdi dir="ltr">ProductVersion</bdi> جدید پس از انعقاد قرارداد را اجرا کن و پاسخ را بازبینی کن.

## 15. تمرین مستقل

[<bdi dir="ltr">Day 04 Exercise</bdi> — <bdi dir="ltr">Ownership Matrix</bdi>](../exercises/day-04-ownership-matrix.md) را انجام بده. حداقل ۱۲ <bdi dir="ltr">Fact</bdi> و پنج <bdi dir="ltr">Decision</bdi> را تحلیل کن.

## 16. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| <bdi dir="ltr">Semantic</bdi> دقیق و یک <bdi dir="ltr">Authority</bdi> | ۳ |
| تفکیک <bdi dir="ltr">Data/Decision/Process ownership</bdi> | ۲ |
| استفادهٔ درست از <bdi dir="ltr">Copy types</bdi> | ۲ |
| <bdi dir="ltr">Freshness/History/Reconciliation</bdi> | ۲ |
| تشخیص <bdi dir="ltr">Forbidden ownership</bdi> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. وجود <bdi dir="ltr">Authority</bdi> مشترک برای یک <bdi dir="ltr">Fact</bdi> با معنای یکسان <bdi dir="ltr">Critical Error</bdi> است.

## 17. آزمون خروج

درس را ببند و [<bdi dir="ltr">Day 04 Exit Ticket</bdi>](../quizzes/day-04-exit-ticket.md) را پاسخ بده.

## 18. منابع

- [<bdi dir="ltr">DDD Reference</bdi> — <bdi dir="ltr">Bounded Context and Context Map</bdi>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- [<bdi dir="ltr">BIAN Service Landscape 14.0</bdi>](https://bian.org/deliverables/service-landscape/) برای <bdi dir="ltr">Gap Check</bdi> مسئولیت‌ها، نه واگذاری <bdi dir="ltr">Ownership</bdi> محلی

الگوی <bdi dir="ltr">Copy</bdi> و ماتریس <bdi dir="ltr">Authority</bdi> در این درس یک <bdi dir="ltr">Synthesis</bdi> معماری برای <bdi dir="ltr">Lab</bdi> است و باید با مقررات، خبرگان و <bdi dir="ltr">Operating Model</bdi> بانک اعتبارسنجی شود.

</div>
