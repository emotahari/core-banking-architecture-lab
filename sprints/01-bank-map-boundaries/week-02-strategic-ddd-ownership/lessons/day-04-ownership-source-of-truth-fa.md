<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 04</span> — مالکیت داده، تصمیم و <span dir="ltr">Source of Truth</span>

- <span dir="ltr">Day budget: 50 minutes including exercise and exit ticket</span>
- <span dir="ltr">Output: Data/Decision Ownership Matrix v1</span>
- <span dir="ltr">Banking case:</span> اعطای تسهیلات، واریز به سپرده و ثبت مالی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Data Authority</span>، <span dir="ltr">Decision Authority</span>، <span dir="ltr">State Owner</span> و <span dir="ltr">Process Owner</span> را جدا کنی.
2. برای هر <span dir="ltr">Fact</span> با معنای دقیق، یک <span dir="ltr">Authority</span> مشخص کنی.
3. <span dir="ltr">Reference</span>، <span dir="ltr">Snapshot</span>، <span dir="ltr">Cache</span>، <span dir="ltr">Projection</span> و <span dir="ltr">Derived Data</span> را از مالکیت جدا کنی.
4. دو <span dir="ltr">Balance</span> ظاهراً مشابه را با <span dir="ltr">Semantic</span> و <span dir="ltr">Purpose</span> متفاوت تفکیک کنی.
5. <span dir="ltr">Freshness</span>، <span dir="ltr">History</span>، <span dir="ltr">Correction</span> و <span dir="ltr">Reconciliation</span> را در <span dir="ltr">Ownership Matrix</span> ثبت کنی.

## 2. چرا عبارت «مالک داده» کافی نیست؟

در جلسهٔ معماری معمولاً می‌شنویم:

> اطلاعات مشتری مال سامانهٔ مشتریان است.

این جمله جهت خوبی دارد، اما برای <span dir="ltr">Contract</span> و <span dir="ltr">Failure</span> کافی نیست. باید روشن کنیم:

- کدام اطلاعات؟ هویت <span dir="ltr">Party</span>، <span dir="ltr">KYC</span>، <span dir="ltr">Segment</span> یا <span dir="ltr">Credit Exposure</span>؟
- چه کسی تعریف <span dir="ltr">Semantic</span> را تعیین می‌کند؟
- چه کسی مجاز به ایجاد و اصلاح است؟
- چه کسی تاریخچه را نگه می‌دارد؟
- <span dir="ltr">Context</span> دیگر <span dir="ltr">Reference</span>، <span dir="ltr">Snapshot</span> یا <span dir="ltr">Cache</span> دارد؟
- اگر دو نسخه متفاوت شدند، چه کسی <span dir="ltr">Reconcile</span> می‌کند؟
- چه <span dir="ltr">Decision</span>ی از این <span dir="ltr">Fact</span> ساخته می‌شود و <span dir="ltr">Authority</span> آن کیست؟

<span dir="ltr">Ownership</span> یک <span dir="ltr">Label</span> روی <span dir="ltr">Box</span> نیست؛ مجموعه‌ای از حقوق و مسئولیت‌های قابل‌آزمون است.

## 3. مدل ذهنی

برای هر مورد این زنجیره را بنویس:


</div>

<div dir="ltr" align="left">

~~~text
semantic fact or decision
        ↓
definition authority
        ↓
create/change authority + lifecycle/history
        ↓
published contract
        ↓
references / snapshots / projections / caches
        ↓
freshness + reconciliation
~~~

</div>

<div dir="rtl" align="right">


اگر عبارت <span dir="ltr">`Customer Data`</span> یا <span dir="ltr">`Balance`</span> آن‌قدر کلی است که چند معنای مستقل را پوشش می‌دهد، ابتدا ردیف را تجزیه کن. <span dir="ltr">Ownership</span> فقط پس از <span dir="ltr">Semantic</span> دقیق قابل تعیین است.

## 4. انواع <span dir="ltr">Authority</span> و <span dir="ltr">Ownership</span>

### <span dir="ltr">4.1 Data/Fact Authority</span>

<span dir="ltr">Context</span>ی که معنای <span dir="ltr">Fact</span>، <span dir="ltr">Lifecycle</span> و تغییر معتبر آن را کنترل می‌کند.

مثال: <span dir="ltr">Deposits</span> برای <span dir="ltr">`AvailableDepositBalance`</span> تصمیم‌گیر و <span dir="ltr">State Owner</span> است. <span dir="ltr">Accounting</span> ممکن است اثر مالی متناظر داشته باشد، اما نمی‌تواند <span dir="ltr">Available Balance</span> را <span dir="ltr">Update</span> کند.

### <span dir="ltr">4.2 Decision Authority</span>

<span dir="ltr">Context</span>ی که با شواهد ورودی و <span dir="ltr">Rule</span>های خودش مجاز است تصمیم بگیرد.

مثال:

- <span dir="ltr">Customer/Compliance:</span> آیا <span dir="ltr">KYC</span> معتبر است؟
- <span dir="ltr">Lending/Credit Decision:</span> آیا این متقاضی برای این محصول و مبلغ واجد شرایط است؟
- <span dir="ltr">Deposits:</span> آیا این حساب در وضعیت فعلی واریز را می‌پذیرد؟

این سه <span dir="ltr">Decision</span> به هم وابسته‌اند، ولی یک <span dir="ltr">Boolean</span> عمومی <span dir="ltr">`isValid`</span> نیستند.

### <span dir="ltr">4.3 State Owner</span>

<span dir="ltr">Context</span>ی که <span dir="ltr">State Machine</span> و <span dir="ltr">Transition</span>های معتبر را نگه می‌دارد.

مثال: <span dir="ltr">Payment Order State</span> متعلق به <span dir="ltr">Payments</span> است؛ <span dir="ltr">Channel</span> درخواست می‌دهد و نمایش می‌دهد، ولی نباید <span dir="ltr">Order</span> را از <span dir="ltr">`Submitted`</span> به <span dir="ltr">`Settled`</span> ببرد.

### <span dir="ltr">4.4 Trigger Owner</span>

<span dir="ltr">Context</span> یا <span dir="ltr">Actor</span>ی که یک <span dir="ltr">Intent</span> را آغاز می‌کند. <span dir="ltr">Trigger</span> بودن <span dir="ltr">Authority</span> تصمیم را منتقل نمی‌کند.

<span dir="ltr">Lending</span> می‌تواند واریز مبلغ اعطا را درخواست کند، اما <span dir="ltr">Deposits</span> دربارهٔ اجرای <span dir="ltr">Credit</span> روی حساب خودش تصمیم می‌گیرد.

### <span dir="ltr">4.5 Process Owner/Process Manager</span>

در جریان چنددامینی، یک <span dir="ltr">Process Manager</span> می‌تواند <span dir="ltr">Correlation</span>، <span dir="ltr">Step Status</span>، <span dir="ltr">Timeout</span> و <span dir="ltr">Next Action</span> را نگه دارد. این جزء نباید <span dir="ltr">State</span> داخلی <span dir="ltr">Domain</span>ها را تصاحب کند.

مثلاً وضعیت <span dir="ltr">`DisbursementProcess = WAITING_FOR_DEPOSIT_CREDIT`</span> متعلق به <span dir="ltr">Process</span> است؛ ولی <span dir="ltr">`DepositTransaction = POSTED`</span> متعلق به <span dir="ltr">Deposits</span> و <span dir="ltr">`Journal = POSTED`</span> متعلق به <span dir="ltr">Accounting</span> است.

## <span dir="ltr">5. Source of Truth</span> را دقیق‌تر کنیم

عبارت <span dir="ltr">`Single Source of Truth`</span> اغلب باعث دو خطا می‌شود:

1. تصور می‌کنیم برای تمام معناهای یک کلمه فقط یک <span dir="ltr">Database</span> باید وجود داشته باشد.
2. <span dir="ltr">Replica</span> یا <span dir="ltr">Report</span> را به‌دلیل داشتن داده، <span dir="ltr">Owner</span> می‌نامیم.

در این دوره از اصطلاح دقیق‌تر استفاده می‌کنیم:

> برای هر <span dir="ltr">Fact</span> با <span dir="ltr">Semantic</span> مشخص، یک <span dir="ltr">Authoritative Context</span> و یک <span dir="ltr">Source of Record</span> تعریف می‌شود.

### <span dir="ltr">Authoritative Context</span>

قواعد، معنای <span dir="ltr">Business</span> و تغییر معتبر را مالک است.

### <span dir="ltr">Source of Record</span>

رکورد پایدار و قابل استناد آن <span dir="ltr">Fact</span> را نگه می‌دارد. در طراحی ساده معمولاً داخل همان <span dir="ltr">Context</span> است؛ ولی <span dir="ltr">Migration</span> یا <span dir="ltr">Legacy</span> می‌تواند موقتاً پیچیدگی ایجاد کند و باید صریح ثبت شود.

### نکتهٔ مهم

ممکن است چند «<span dir="ltr">Balance</span>» معتبر داشته باشیم، چون معنا متفاوت است:

- <span dir="ltr">Operational Principal Outstanding</span> در <span dir="ltr">Lending</span>
- <span dir="ltr">Accounting Receivable Balance</span> در <span dir="ltr">Subledger/Accounting</span>
- <span dir="ltr">Analytical Exposure Projection</span> در <span dir="ltr">Data Platform</span>

این‌ها سه <span dir="ltr">Owner</span> برای یک <span dir="ltr">Fact</span> نیستند؛ سه <span dir="ltr">Fact</span> با <span dir="ltr">Purpose</span>، زمان و <span dir="ltr">Rule</span> متفاوت‌اند. باید نام و <span dir="ltr">Reconciliation</span> آن‌ها دقیق باشد.

## 6. نقش <span dir="ltr">Copy</span>ها

داشتن یک مقدار در چند <span dir="ltr">Context</span> لزوماً <span dir="ltr">Ownership</span> مشترک نیست. نوع <span dir="ltr">Copy</span> را ثبت کن.

### <span dir="ltr">Reference</span>

فقط شناسهٔ <span dir="ltr">Fact</span> بیرونی را نگه می‌دارد.

مثال: <span dir="ltr">Lending</span> یک <span dir="ltr">`CustomerId`</span> نگه می‌دارد و هویت <span dir="ltr">Party</span> را مالک نمی‌شود.

### <span dir="ltr">Snapshot</span>

کپی تاریخی از <span dir="ltr">Fact</span>ها در زمان یک تعهد/تصمیم است و تغییر آیندهٔ <span dir="ltr">Upstream</span> نباید آن را خودکار تغییر دهد.

مثال: نرخ، مدت و شروط مؤثر قرارداد اعطاشده از <span dir="ltr">ProductVersion Snapshot</span> می‌شوند.

<span dir="ltr">Snapshot</span> باید داشته باشد:

- <span dir="ltr">effective time</span>
- <span dir="ltr">source/version</span>
- <span dir="ltr">reason/use case</span>
- <span dir="ltr">correction policy</span>

### <span dir="ltr">Cache</span>

کپی موقت برای <span dir="ltr">Performance/Availability</span> با <span dir="ltr">TTL</span> یا <span dir="ltr">Invalidation Policy. Cache Fact</span> جدیدی ایجاد نمی‌کند.

مثال: <span dir="ltr">Channel</span> ممکن است <span dir="ltr">Customer Display Name</span> را <span dir="ltr">Cache</span> کند، ولی اصلاح نام در <span dir="ltr">Master</span> را انجام نمی‌دهد.

### <span dir="ltr">Projection</span>

مدل <span dir="ltr">Read</span> که از <span dir="ltr">Fact/Event</span>های <span dir="ltr">Authority</span> ساخته و قابل بازسازی است.

مثال: داشبورد یکپارچهٔ تعهدات مشتری از <span dir="ltr">Lending</span>، <span dir="ltr">Deposits</span> و <span dir="ltr">Accounting Projection</span> می‌سازد؛ <span dir="ltr">Owner</span> عملیات پایه نیست.

### <span dir="ltr">Derived Data</span>

مقداری که از <span dir="ltr">Source</span>ها و <span dir="ltr">Formula</span> مشخص محاسبه می‌شود.

مثال: <span dir="ltr">`TotalCustomerExposure`</span> ممکن است <span dir="ltr">Derived</span> باشد. باید <span dir="ltr">Owner Formula</span>، <span dir="ltr">Source versions</span>، <span dir="ltr">as-of time</span> و <span dir="ltr">Recalculation</span> مشخص باشد.

### <span dir="ltr">Replica</span>

کپی فنی برای <span dir="ltr">Availability/Read scale</span> است. <span dir="ltr">Replica</span> حتی اگر <span dir="ltr">Read</span> از آن انجام شود، <span dir="ltr">Authority</span> دامینی جدید نیست.

## 7. جدول کنترل <span dir="ltr">Copy</span>

| <span dir="ltr">Copy type</span> | <span dir="ltr">Can change source fact</span>? | <span dir="ltr">Must have provenance</span>? | <span dir="ltr">Freshness rule</span> | <span dir="ltr">Historical role</span> |
|---|---:|---:|---|---|
| <span dir="ltr">Reference</span> | <span dir="ltr">no</span> | <span dir="ltr">yes</span> | <span dir="ltr">resolve policy</span> | <span dir="ltr">points to authority</span> |
| <span dir="ltr">Snapshot</span> | <span dir="ltr">no</span> | <span dir="ltr">yes</span> | <span dir="ltr">fixed at effective time</span> | <span dir="ltr">preserves past commitment</span> |
| <span dir="ltr">Cache</span> | <span dir="ltr">no</span> | <span dir="ltr">yes</span> | <span dir="ltr">TTL/invalidation</span> | <span dir="ltr">usually not authoritative history</span> |
| <span dir="ltr">Projection</span> | <span dir="ltr">no</span> | <span dir="ltr">yes</span> | <span dir="ltr">lag/rebuild policy</span> | <span dir="ltr">read history as designed</span> |
| <span dir="ltr">Derived</span> | <span dir="ltr">no</span>, <span dir="ltr">but owns formula/result</span> | <span dir="ltr">yes</span> | <span dir="ltr">recompute policy</span> | <span dir="ltr">as-of/version required</span> |
| <span dir="ltr">Replica</span> | <span dir="ltr">no</span> | <span dir="ltr">technical lineage</span> | <span dir="ltr">replication lag</span> | <span dir="ltr">same record technically</span> |

## 8. مثال هدایت‌شده: اعطای تسهیلات مرابحه

### <span dir="ltr">Fact 1: Party Identity</span>

- <span dir="ltr">Authority: Party</span> & <span dir="ltr">Customer</span>
- <span dir="ltr">Lending: Reference</span> و <span dir="ltr">Snapshot</span> شواهد لازم تصمیم
- <span dir="ltr">Accounting: Reference</span> برای تفصیل/<span dir="ltr">Audit</span> در صورت نیاز
- <span dir="ltr">Forbidden: Lending</span> یا <span dir="ltr">Accounting</span> اصلاح نام و هویت <span dir="ltr">Master</span> را انجام دهند.

### <span dir="ltr">Fact 2: Product Definition</span>

- <span dir="ltr">Authority: Product Catalog</span>
- <span dir="ltr">Agreement/Lending: Snapshot</span> نسخه و شروط مؤثر
- نکته: تغییر <span dir="ltr">ProductVersion</span> آینده قرارداد گذشته را تغییر نمی‌دهد.

### <span dir="ltr">Fact 3: Loan Grant State</span>

- <span dir="ltr">Authority: Lending</span>
- <span dir="ltr">Deposits: Consumer</span> درخواست/<span dir="ltr">Reference</span> اعطا به‌اندازهٔ لازم
- <span dir="ltr">Accounting: Consumer Business Fact</span> برای ثبت مالی
- <span dir="ltr">Forbidden: Accounting</span> از روی وجود <span dir="ltr">Journal</span>، <span dir="ltr">State</span> اعطا را در <span dir="ltr">Lending</span> تغییر دهد.

### <span dir="ltr">Fact 4: Operational Loan Principal Outstanding</span>

- <span dir="ltr">Authority: Lending</span>
- <span dir="ltr">Accounting:</span> ماندهٔ مالی متناظر با <span dir="ltr">Semantic</span> حسابداری، نه کپی قابل‌تغییر از <span dir="ltr">Operational State</span>
- <span dir="ltr">Reconciliation:</span> اختلاف باید کشف و با <span dir="ltr">Owner</span> مشترک فرایند رسیدگی شود، اما هر سیستم اصلاح <span dir="ltr">State</span> خودش را طبق کنترل انجام می‌دهد.

### <span dir="ltr">Fact 5: Deposit Credit Transaction</span> و <span dir="ltr">Available Balance</span>

- <span dir="ltr">Authority: Deposits</span>
- <span dir="ltr">Lending: Result/Fact</span> و <span dir="ltr">Process status</span>
- <span dir="ltr">Accounting:</span> رویداد لازم برای <span dir="ltr">Journal</span> مربوط به اثر سپرده
- <span dir="ltr">Forbidden: Orchestrator</span> یا <span dir="ltr">Lending</span> مستقیماً ماندهٔ سپرده را <span dir="ltr">Update</span> کند.

### <span dir="ltr">Fact 6: Journal Entry</span>

- <span dir="ltr">Authority: Accounting</span>
- <span dir="ltr">Business domains: Reference</span> به <span dir="ltr">`JournalId`</span> یا <span dir="ltr">Status</span> در صورت نیاز
- <span dir="ltr">Accounting</span> تصمیم می‌گیرد کدام <span dir="ltr">Template/Rules</span> حسابداری روی <span dir="ltr">Fact</span> معتبر اعمال شود.
- <span dir="ltr">Accounting</span> مالک این نیست که آیا <span dir="ltr">Deposit</span> واقعاً <span dir="ltr">available</span> است یا <span dir="ltr">Loan</span> قابل وصول است.

## 9. دو ماندهٔ تسهیلات: تناقض یا دو <span dir="ltr">Semantic</span>؟

سؤال دقیق:

> اگر <span dir="ltr">Lending</span> ماندهٔ اصل را نگه می‌دارد و <span dir="ltr">Accounting</span> نیز ماندهٔ حساب تسهیلات را دارد، آیا دو <span dir="ltr">Source of Truth</span> داریم؟

پاسخ: ابتدا <span dir="ltr">Semantic</span> را جدا کن.

### <span dir="ltr">Lending Principal Outstanding</span>

- برای برنامهٔ اقساط، وصول، وضعیت <span dir="ltr">Loan</span> و تصمیم عملیاتی
- از عملیات دامینی <span dir="ltr">Loan</span> تغییر می‌کند
- <span dir="ltr">Invariant</span>های قرارداد و بازپرداخت را اعمال می‌کند

### <span dir="ltr">Accounting Receivable/Subledger Balance</span>

- برای گزارش مالی، <span dir="ltr">Journal</span>، <span dir="ltr">Trial Balance</span> و تطبیق
- از <span dir="ltr">Posting</span>های معتبر تغییر می‌کند
- قواعد دورهٔ مالی و حسابداری را اعمال می‌کند

این دو باید از نظر اقتصادی قابل <span dir="ltr">Reconcile</span> باشند، ولی الزاماً در هر لحظه و هر <span dir="ltr">State</span> فنی دقیقاً یک مقدار ندارند؛ <span dir="ltr">Latency</span>، <span dir="ltr">Pending</span>، <span dir="ltr">Adjustment</span> و <span dir="ltr">Closing</span> ممکن است تفاوت کنترل‌شده بسازد. معماری باید:

- معنای هر مانده را نام‌گذاری کند؛
- <span dir="ltr">Event/Contract</span> اتصال را روشن کند؛
- <span dir="ltr">Expected lag</span> را تعیین کند؛
- <span dir="ltr">Reconciliation</span> و <span dir="ltr">Correction path</span> داشته باشد.

راه‌حل اشتباه این است که هر دو سیستم یک جدول <span dir="ltr">Balance</span> مشترک را <span dir="ltr">Update</span> کنند تا «همیشه یکی» باشند. این کار <span dir="ltr">Authority</span> و <span dir="ltr">Transaction Boundary</span> را نابود می‌کند.

## <span dir="ltr">10. Trigger</span>، <span dir="ltr">Decision</span> و <span dir="ltr">Fact</span> را جدا کن

نمونهٔ عملیات واریز اعطا:

| <span dir="ltr">Role</span> | <span dir="ltr">Example</span> |
|---|---|
| <span dir="ltr">Trigger owner</span> | <span dir="ltr">Lending process decides it is time to request disbursement</span> |
| <span dir="ltr">Command</span> | <span dir="ltr">`CreditDepositAccount`</span> |
| <span dir="ltr">Decision authority</span> | <span dir="ltr">Deposits decides whether account can accept credit now</span> |
| <span dir="ltr">State owner</span> | <span dir="ltr">Deposits records transaction and updates its balance</span> |
| <span dir="ltr">Resulting fact</span> | <span dir="ltr">`DepositCredited`</span> <span dir="ltr">or explicit rejection fact/result</span> |
| <span dir="ltr">Process observer</span> | <span dir="ltr">Lending/Process Manager advances its own status</span> |
| <span dir="ltr">Financial consumer</span> | <span dir="ltr">Accounting produces relevant Journal from valid facts</span> |

این تفکیک مانع آن می‌شود که <span dir="ltr">Orchestrator</span> به <span dir="ltr">Super-Domain</span> و مالک همه‌چیز تبدیل شود.

## <span dir="ltr">11. Correction</span> و <span dir="ltr">Reconciliation</span> بخشی از <span dir="ltr">Ownership</span> است

<span dir="ltr">Owner</span> فقط <span dir="ltr">Happy Path</span> را مالک نیست. باید روشن باشد:

- چه کسی خطا را تشخیص می‌دهد؟
- چه کسی مجاز به <span dir="ltr">Correction</span> است؟
- <span dir="ltr">Correction</span> با <span dir="ltr">Update</span>، <span dir="ltr">Reversal</span> یا <span dir="ltr">Compensating Fact</span> انجام می‌شود؟
- <span dir="ltr">Audit trail</span> کجاست؟
- چه کسی اختلاف میان <span dir="ltr">Operational</span> و <span dir="ltr">Accounting Projection</span> را پیگیری می‌کند؟

جزئیات <span dir="ltr">Accounting/Reversal</span> در <span dir="ltr">Sprint</span>های بعد می‌آید، اما در <span dir="ltr">Matrix</span> حداقل <span dir="ltr">`Reconciliation owner`</span> و <span dir="ltr">`Open Question`</span> باید ثبت شود.

## 12. خطاهای رایج

### مالکیت مشترک

«<span dir="ltr">Lending</span> و <span dir="ltr">Accounting</span> هر دو مالک ماندهٔ تسهیلات‌اند» ابهام <span dir="ltr">Semantic</span> را پنهان می‌کند. دو مانده را نام‌گذاری کن.

### <span dir="ltr">Database</span> برابر <span dir="ltr">Owner</span>

داشتن جدول یا <span dir="ltr">Replica</span> به معنی <span dir="ltr">Authority</span> نیست. در <span dir="ltr">Migration</span> ممکن است رکورد فیزیکی موقتاً جای دیگری باشد.

### <span dir="ltr">Event Consumer</span> برابر <span dir="ltr">Owner</span>

<span dir="ltr">Accounting</span> با مصرف <span dir="ltr">`LoanGranted`</span> مالک <span dir="ltr">Loan</span> نمی‌شود. <span dir="ltr">Projection</span> نیز <span dir="ltr">Authority</span> نمی‌سازد.

### <span dir="ltr">Orchestrator</span> برابر <span dir="ltr">Owner</span>

<span dir="ltr">Process Manager Step Status</span> را نگه می‌دارد؛ <span dir="ltr">Fact</span>های <span dir="ltr">Domain</span> را جعل یا تصاحب نمی‌کند.

### <span dir="ltr">Snapshot</span> بدون زمان و <span dir="ltr">Version</span>

کپی بدون <span dir="ltr">Provenance</span> به‌سرعت به <span dir="ltr">Master</span> پنهان و متناقض تبدیل می‌شود.

### «همه‌چیز را همگام <span dir="ltr">Query</span> کنیم»

<span dir="ltr">Query</span> زنده برای <span dir="ltr">Product terms</span> قرارداد گذشته یا شواهد تصمیم می‌تواند تاریخچه را خراب کند. <span dir="ltr">Reference</span>، <span dir="ltr">Snapshot</span> و <span dir="ltr">Cache</span> باید بر اساس <span dir="ltr">Use Case</span> انتخاب شوند.

### <span dir="ltr">RACI</span> به‌جای <span dir="ltr">Data Authority</span>

<span dir="ltr">RACI</span> سازمانی مفید است، ولی نمی‌گوید کدام <span dir="ltr">Context</span> مجاز به <span dir="ltr">Transition State</span> و انتشار <span dir="ltr">Fact</span> است. هر دو <span dir="ltr">Artifact</span> ممکن است لازم باشند.

## 13. روش تکمیل <span dir="ltr">Ownership Matrix</span>

برای هر ردیف:

1. <span dir="ltr">Semantic</span> را آن‌قدر دقیق کن که یک <span dir="ltr">Fact</span> باشد.
2. <span dir="ltr">Context Authority</span> را انتخاب کن.
3. دیگر <span dir="ltr">Context</span>ها را <span dir="ltr">`Reference/Snapshot/Projection/Cache/Consumer/Not Allowed`</span> علامت بزن.
4. <span dir="ltr">Freshness</span> و <span dir="ltr">History rule</span> را ثبت کن.
5. <span dir="ltr">Decision</span>های وابسته را جدا بنویس.
6. <span dir="ltr">Reconciliation owner</span> و <span dir="ltr">Correction path</span> را مشخص یا <span dir="ltr">Open Question</span> کن.
7. با یک <span dir="ltr">Failure</span> یا <span dir="ltr">Change</span> واقعی تصمیم را آزمایش کن.

## 14. تمرین هدایت‌شده

برای <span dir="ltr">`Product Definition`</span> و <span dir="ltr">`Executed Agreement Terms`</span> دو ردیف مستقل بساز. اگر <span dir="ltr">Owner</span> و <span dir="ltr">Lifecycle</span> هر دو را یکی نوشتی، سناریوی انتشار <span dir="ltr">ProductVersion</span> جدید پس از انعقاد قرارداد را اجرا کن و پاسخ را بازبینی کن.

## 15. تمرین مستقل

[<span dir="ltr">Day 04 Exercise</span> — <span dir="ltr">Ownership Matrix</span>](../exercises/day-04-ownership-matrix.md) را انجام بده. حداقل ۱۲ <span dir="ltr">Fact</span> و پنج <span dir="ltr">Decision</span> را تحلیل کن.

## 16. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| <span dir="ltr">Semantic</span> دقیق و یک <span dir="ltr">Authority</span> | ۳ |
| تفکیک <span dir="ltr">Data/Decision/Process ownership</span> | ۲ |
| استفادهٔ درست از <span dir="ltr">Copy types</span> | ۲ |
| <span dir="ltr">Freshness/History/Reconciliation</span> | ۲ |
| تشخیص <span dir="ltr">Forbidden ownership</span> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. وجود <span dir="ltr">Authority</span> مشترک برای یک <span dir="ltr">Fact</span> با معنای یکسان <span dir="ltr">Critical Error</span> است.

## 17. آزمون خروج

درس را ببند و [<span dir="ltr">Day 04 Exit Ticket</span>](../quizzes/day-04-exit-ticket.md) را پاسخ بده.

## 18. منابع

- [<span dir="ltr">DDD Reference</span> — <span dir="ltr">Bounded Context and Context Map</span>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- [<span dir="ltr">BIAN Service Landscape 14.0</span>](https://bian.org/deliverables/service-landscape/) برای <span dir="ltr">Gap Check</span> مسئولیت‌ها، نه واگذاری <span dir="ltr">Ownership</span> محلی

الگوی <span dir="ltr">Copy</span> و ماتریس <span dir="ltr">Authority</span> در این درس یک <span dir="ltr">Synthesis</span> معماری برای <span dir="ltr">Lab</span> است و باید با مقررات، خبرگان و <span dir="ltr">Operating Model</span> بانک اعتبارسنجی شود.

</div>
