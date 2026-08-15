<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 04</bdi> — مالکیت داده، تصمیم و <bdi dir="ltr">Source of Truth</bdi>

- <bdi dir="ltr">Day budget: 50 minutes including exercise and exit ticket</bdi>
- <bdi dir="ltr">Output: Data/Decision Ownership Matrix v1</bdi>
- <bdi dir="ltr">Banking case:</bdi> اعطای تسهیلات، واریز به سپرده و ثبت مالی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Data Authority</bdi>، <bdi dir="ltr">Decision Authority</bdi>، <bdi dir="ltr">State Owner</bdi> و <bdi dir="ltr">Process Owner</bdi> را جدا کنی.
2. برای هر <bdi dir="ltr">Fact</bdi> با معنای دقیق، یک <bdi dir="ltr">Authority</bdi> مشخص کنی.
3. <bdi dir="ltr">Reference</bdi>، <bdi dir="ltr">Snapshot</bdi>، <bdi dir="ltr">Cache</bdi>، <bdi dir="ltr">Projection</bdi> و <bdi dir="ltr">Derived Data</bdi> را از مالکیت جدا کنی.
4. دو <bdi dir="ltr">Balance</bdi> ظاهراً مشابه را با <bdi dir="ltr">Semantic</bdi> و <bdi dir="ltr">Purpose</bdi> متفاوت تفکیک کنی.
5. <bdi dir="ltr">Freshness</bdi>، <bdi dir="ltr">History</bdi>، <bdi dir="ltr">Correction</bdi> و <bdi dir="ltr">Reconciliation</bdi> را در <bdi dir="ltr">Ownership Matrix</bdi> ثبت کنی.

## 2. چرا عبارت «مالک داده» کافی نیست؟

در جلسهٔ معماری معمولاً می‌شنویم:

> اطلاعات مشتری مال سامانهٔ مشتریان است.

این جمله جهت خوبی دارد، اما برای <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Failure</bdi> کافی نیست. باید روشن کنیم:

- کدام اطلاعات؟ هویت <bdi dir="ltr">Party</bdi>، <bdi dir="ltr">KYC</bdi>، <bdi dir="ltr">Segment</bdi> یا <bdi dir="ltr">Credit Exposure</bdi>؟
- چه کسی تعریف <bdi dir="ltr">Semantic</bdi> را تعیین می‌کند؟
- چه کسی مجاز به ایجاد و اصلاح است؟
- چه کسی تاریخچه را نگه می‌دارد؟
- <bdi dir="ltr">Context</bdi> دیگر <bdi dir="ltr">Reference</bdi>، <bdi dir="ltr">Snapshot</bdi> یا <bdi dir="ltr">Cache</bdi> دارد؟
- اگر دو نسخه متفاوت شدند، چه کسی <bdi dir="ltr">Reconcile</bdi> می‌کند؟
- چه <bdi dir="ltr">Decision</bdi>ی از این <bdi dir="ltr">Fact</bdi> ساخته می‌شود و <bdi dir="ltr">Authority</bdi> آن کیست؟

<bdi dir="ltr">Ownership</bdi> یک <bdi dir="ltr">Label</bdi> روی <bdi dir="ltr">Box</bdi> نیست؛ مجموعه‌ای از حقوق و مسئولیت‌های قابل‌آزمون است.

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


اگر عبارت <bdi dir="ltr">`Customer Data`</bdi> یا <bdi dir="ltr">`Balance`</bdi> آن‌قدر کلی است که چند معنای مستقل را پوشش می‌دهد، ابتدا ردیف را تجزیه کن. <bdi dir="ltr">Ownership</bdi> فقط پس از <bdi dir="ltr">Semantic</bdi> دقیق قابل تعیین است.

## 4. انواع <bdi dir="ltr">Authority</bdi> و <bdi dir="ltr">Ownership</bdi>

### <bdi dir="ltr">4.1 Data/Fact Authority</bdi>

<bdi dir="ltr">Context</bdi>ی که معنای <bdi dir="ltr">Fact</bdi>، <bdi dir="ltr">Lifecycle</bdi> و تغییر معتبر آن را کنترل می‌کند.

مثال: <bdi dir="ltr">Deposits</bdi> برای <bdi dir="ltr">`AvailableDepositBalance`</bdi> تصمیم‌گیر و <bdi dir="ltr">State Owner</bdi> است. <bdi dir="ltr">Accounting</bdi> ممکن است اثر مالی متناظر داشته باشد، اما نمی‌تواند <bdi dir="ltr">Available Balance</bdi> را <bdi dir="ltr">Update</bdi> کند.

### <bdi dir="ltr">4.2 Decision Authority</bdi>

<bdi dir="ltr">Context</bdi>ی که با شواهد ورودی و <bdi dir="ltr">Rule</bdi>های خودش مجاز است تصمیم بگیرد.

مثال:

- <bdi dir="ltr">Customer/Compliance:</bdi> آیا <bdi dir="ltr">KYC</bdi> معتبر است؟
- <bdi dir="ltr">Lending/Credit Decision:</bdi> آیا این متقاضی برای این محصول و مبلغ واجد شرایط است؟
- <bdi dir="ltr">Deposits:</bdi> آیا این حساب در وضعیت فعلی واریز را می‌پذیرد؟

این سه <bdi dir="ltr">Decision</bdi> به هم وابسته‌اند، ولی یک <bdi dir="ltr">Boolean</bdi> عمومی <bdi dir="ltr">`isValid`</bdi> نیستند.

### <bdi dir="ltr">4.3 State Owner</bdi>

<bdi dir="ltr">Context</bdi>ی که <bdi dir="ltr">State Machine</bdi> و <bdi dir="ltr">Transition</bdi>های معتبر را نگه می‌دارد.

مثال: <bdi dir="ltr">Payment Order State</bdi> متعلق به <bdi dir="ltr">Payments</bdi> است؛ <bdi dir="ltr">Channel</bdi> درخواست می‌دهد و نمایش می‌دهد، ولی نباید <bdi dir="ltr">Order</bdi> را از <bdi dir="ltr">`Submitted`</bdi> به <bdi dir="ltr">`Settled`</bdi> ببرد.

### <bdi dir="ltr">4.4 Trigger Owner</bdi>

<bdi dir="ltr">Context</bdi> یا <bdi dir="ltr">Actor</bdi>ی که یک <bdi dir="ltr">Intent</bdi> را آغاز می‌کند. <bdi dir="ltr">Trigger</bdi> بودن <bdi dir="ltr">Authority</bdi> تصمیم را منتقل نمی‌کند.

<bdi dir="ltr">Lending</bdi> می‌تواند واریز مبلغ اعطا را درخواست کند، اما <bdi dir="ltr">Deposits</bdi> دربارهٔ اجرای <bdi dir="ltr">Credit</bdi> روی حساب خودش تصمیم می‌گیرد.

### <bdi dir="ltr">4.5 Process Owner/Process Manager</bdi>

در جریان چنددامینی، یک <bdi dir="ltr">Process Manager</bdi> می‌تواند <bdi dir="ltr">Correlation</bdi>، <bdi dir="ltr">Step Status</bdi>، <bdi dir="ltr">Timeout</bdi> و <bdi dir="ltr">Next Action</bdi> را نگه دارد. این جزء نباید <bdi dir="ltr">State</bdi> داخلی <bdi dir="ltr">Domain</bdi>ها را تصاحب کند.

مثلاً وضعیت <bdi dir="ltr">`DisbursementProcess = WAITING_FOR_DEPOSIT_CREDIT`</bdi> متعلق به <bdi dir="ltr">Process</bdi> است؛ ولی <bdi dir="ltr">`DepositTransaction = POSTED`</bdi> متعلق به <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">`Journal = POSTED`</bdi> متعلق به <bdi dir="ltr">Accounting</bdi> است.

## <bdi dir="ltr">5. Source of Truth</bdi> را دقیق‌تر کنیم

عبارت <bdi dir="ltr">`Single Source of Truth`</bdi> اغلب باعث دو خطا می‌شود:

1. تصور می‌کنیم برای تمام معناهای یک کلمه فقط یک <bdi dir="ltr">Database</bdi> باید وجود داشته باشد.
2. <bdi dir="ltr">Replica</bdi> یا <bdi dir="ltr">Report</bdi> را به‌دلیل داشتن داده، <bdi dir="ltr">Owner</bdi> می‌نامیم.

در این دوره از اصطلاح دقیق‌تر استفاده می‌کنیم:

> برای هر <bdi dir="ltr">Fact</bdi> با <bdi dir="ltr">Semantic</bdi> مشخص، یک <bdi dir="ltr">Authoritative Context</bdi> و یک <bdi dir="ltr">Source of Record</bdi> تعریف می‌شود.

### <bdi dir="ltr">Authoritative Context</bdi>

قواعد، معنای <bdi dir="ltr">Business</bdi> و تغییر معتبر را مالک است.

### <bdi dir="ltr">Source of Record</bdi>

رکورد پایدار و قابل استناد آن <bdi dir="ltr">Fact</bdi> را نگه می‌دارد. در طراحی ساده معمولاً داخل همان <bdi dir="ltr">Context</bdi> است؛ ولی <bdi dir="ltr">Migration</bdi> یا <bdi dir="ltr">Legacy</bdi> می‌تواند موقتاً پیچیدگی ایجاد کند و باید صریح ثبت شود.

### نکتهٔ مهم

ممکن است چند «<bdi dir="ltr">Balance</bdi>» معتبر داشته باشیم، چون معنا متفاوت است:

- <bdi dir="ltr">Operational Principal Outstanding</bdi> در <bdi dir="ltr">Lending</bdi>
- <bdi dir="ltr">Accounting Receivable Balance</bdi> در <bdi dir="ltr">Subledger/Accounting</bdi>
- <bdi dir="ltr">Analytical Exposure Projection</bdi> در <bdi dir="ltr">Data Platform</bdi>

این‌ها سه <bdi dir="ltr">Owner</bdi> برای یک <bdi dir="ltr">Fact</bdi> نیستند؛ سه <bdi dir="ltr">Fact</bdi> با <bdi dir="ltr">Purpose</bdi>، زمان و <bdi dir="ltr">Rule</bdi> متفاوت‌اند. باید نام و <bdi dir="ltr">Reconciliation</bdi> آن‌ها دقیق باشد.

## 6. نقش <bdi dir="ltr">Copy</bdi>ها

داشتن یک مقدار در چند <bdi dir="ltr">Context</bdi> لزوماً <bdi dir="ltr">Ownership</bdi> مشترک نیست. نوع <bdi dir="ltr">Copy</bdi> را ثبت کن.

### <bdi dir="ltr">Reference</bdi>

فقط شناسهٔ <bdi dir="ltr">Fact</bdi> بیرونی را نگه می‌دارد.

مثال: <bdi dir="ltr">Lending</bdi> یک <bdi dir="ltr">`CustomerId`</bdi> نگه می‌دارد و هویت <bdi dir="ltr">Party</bdi> را مالک نمی‌شود.

### <bdi dir="ltr">Snapshot</bdi>

کپی تاریخی از <bdi dir="ltr">Fact</bdi>ها در زمان یک تعهد/تصمیم است و تغییر آیندهٔ <bdi dir="ltr">Upstream</bdi> نباید آن را خودکار تغییر دهد.

مثال: نرخ، مدت و شروط مؤثر قرارداد اعطاشده از <bdi dir="ltr">ProductVersion Snapshot</bdi> می‌شوند.

<bdi dir="ltr">Snapshot</bdi> باید داشته باشد:

- <bdi dir="ltr">effective time</bdi>
- <bdi dir="ltr">source/version</bdi>
- <bdi dir="ltr">reason/use case</bdi>
- <bdi dir="ltr">correction policy</bdi>

### <bdi dir="ltr">Cache</bdi>

کپی موقت برای <bdi dir="ltr">Performance/Availability</bdi> با <bdi dir="ltr">TTL</bdi> یا <bdi dir="ltr">Invalidation Policy. Cache Fact</bdi> جدیدی ایجاد نمی‌کند.

مثال: <bdi dir="ltr">Channel</bdi> ممکن است <bdi dir="ltr">Customer Display Name</bdi> را <bdi dir="ltr">Cache</bdi> کند، ولی اصلاح نام در <bdi dir="ltr">Master</bdi> را انجام نمی‌دهد.

### <bdi dir="ltr">Projection</bdi>

مدل <bdi dir="ltr">Read</bdi> که از <bdi dir="ltr">Fact/Event</bdi>های <bdi dir="ltr">Authority</bdi> ساخته و قابل بازسازی است.

مثال: داشبورد یکپارچهٔ تعهدات مشتری از <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">Accounting Projection</bdi> می‌سازد؛ <bdi dir="ltr">Owner</bdi> عملیات پایه نیست.

### <bdi dir="ltr">Derived Data</bdi>

مقداری که از <bdi dir="ltr">Source</bdi>ها و <bdi dir="ltr">Formula</bdi> مشخص محاسبه می‌شود.

مثال: <bdi dir="ltr">`TotalCustomerExposure`</bdi> ممکن است <bdi dir="ltr">Derived</bdi> باشد. باید <bdi dir="ltr">Owner Formula</bdi>، <bdi dir="ltr">Source versions</bdi>، <bdi dir="ltr">as-of time</bdi> و <bdi dir="ltr">Recalculation</bdi> مشخص باشد.

### <bdi dir="ltr">Replica</bdi>

کپی فنی برای <bdi dir="ltr">Availability/Read scale</bdi> است. <bdi dir="ltr">Replica</bdi> حتی اگر <bdi dir="ltr">Read</bdi> از آن انجام شود، <bdi dir="ltr">Authority</bdi> دامینی جدید نیست.

## 7. جدول کنترل <bdi dir="ltr">Copy</bdi>

| <bdi dir="ltr">Copy type</bdi> | <bdi dir="ltr">Can change source fact</bdi>? | <bdi dir="ltr">Must have provenance</bdi>? | <bdi dir="ltr">Freshness rule</bdi> | <bdi dir="ltr">Historical role</bdi> |
|---|---:|---:|---|---|
| <bdi dir="ltr">Reference</bdi> | <bdi dir="ltr">no</bdi> | <bdi dir="ltr">yes</bdi> | <bdi dir="ltr">resolve policy</bdi> | <bdi dir="ltr">points to authority</bdi> |
| <bdi dir="ltr">Snapshot</bdi> | <bdi dir="ltr">no</bdi> | <bdi dir="ltr">yes</bdi> | <bdi dir="ltr">fixed at effective time</bdi> | <bdi dir="ltr">preserves past commitment</bdi> |
| <bdi dir="ltr">Cache</bdi> | <bdi dir="ltr">no</bdi> | <bdi dir="ltr">yes</bdi> | <bdi dir="ltr">TTL/invalidation</bdi> | <bdi dir="ltr">usually not authoritative history</bdi> |
| <bdi dir="ltr">Projection</bdi> | <bdi dir="ltr">no</bdi> | <bdi dir="ltr">yes</bdi> | <bdi dir="ltr">lag/rebuild policy</bdi> | <bdi dir="ltr">read history as designed</bdi> |
| <bdi dir="ltr">Derived</bdi> | <bdi dir="ltr">no</bdi>, <bdi dir="ltr">but owns formula/result</bdi> | <bdi dir="ltr">yes</bdi> | <bdi dir="ltr">recompute policy</bdi> | <bdi dir="ltr">as-of/version required</bdi> |
| <bdi dir="ltr">Replica</bdi> | <bdi dir="ltr">no</bdi> | <bdi dir="ltr">technical lineage</bdi> | <bdi dir="ltr">replication lag</bdi> | <bdi dir="ltr">same record technically</bdi> |

## 8. مثال هدایت‌شده: اعطای تسهیلات مرابحه

### <bdi dir="ltr">Fact 1: Party Identity</bdi>

- <bdi dir="ltr">Authority: Party</bdi> & <bdi dir="ltr">Customer</bdi>
- <bdi dir="ltr">Lending: Reference</bdi> و <bdi dir="ltr">Snapshot</bdi> شواهد لازم تصمیم
- <bdi dir="ltr">Accounting: Reference</bdi> برای تفصیل/<bdi dir="ltr">Audit</bdi> در صورت نیاز
- <bdi dir="ltr">Forbidden: Lending</bdi> یا <bdi dir="ltr">Accounting</bdi> اصلاح نام و هویت <bdi dir="ltr">Master</bdi> را انجام دهند.

### <bdi dir="ltr">Fact 2: Product Definition</bdi>

- <bdi dir="ltr">Authority: Product Catalog</bdi>
- <bdi dir="ltr">Agreement/Lending: Snapshot</bdi> نسخه و شروط مؤثر
- نکته: تغییر <bdi dir="ltr">ProductVersion</bdi> آینده قرارداد گذشته را تغییر نمی‌دهد.

### <bdi dir="ltr">Fact 3: Loan Grant State</bdi>

- <bdi dir="ltr">Authority: Lending</bdi>
- <bdi dir="ltr">Deposits: Consumer</bdi> درخواست/<bdi dir="ltr">Reference</bdi> اعطا به‌اندازهٔ لازم
- <bdi dir="ltr">Accounting: Consumer Business Fact</bdi> برای ثبت مالی
- <bdi dir="ltr">Forbidden: Accounting</bdi> از روی وجود <bdi dir="ltr">Journal</bdi>، <bdi dir="ltr">State</bdi> اعطا را در <bdi dir="ltr">Lending</bdi> تغییر دهد.

### <bdi dir="ltr">Fact 4: Operational Loan Principal Outstanding</bdi>

- <bdi dir="ltr">Authority: Lending</bdi>
- <bdi dir="ltr">Accounting:</bdi> ماندهٔ مالی متناظر با <bdi dir="ltr">Semantic</bdi> حسابداری، نه کپی قابل‌تغییر از <bdi dir="ltr">Operational State</bdi>
- <bdi dir="ltr">Reconciliation:</bdi> اختلاف باید کشف و با <bdi dir="ltr">Owner</bdi> مشترک فرایند رسیدگی شود، اما هر سیستم اصلاح <bdi dir="ltr">State</bdi> خودش را طبق کنترل انجام می‌دهد.

### <bdi dir="ltr">Fact 5: Deposit Credit Transaction</bdi> و <bdi dir="ltr">Available Balance</bdi>

- <bdi dir="ltr">Authority: Deposits</bdi>
- <bdi dir="ltr">Lending: Result/Fact</bdi> و <bdi dir="ltr">Process status</bdi>
- <bdi dir="ltr">Accounting:</bdi> رویداد لازم برای <bdi dir="ltr">Journal</bdi> مربوط به اثر سپرده
- <bdi dir="ltr">Forbidden: Orchestrator</bdi> یا <bdi dir="ltr">Lending</bdi> مستقیماً ماندهٔ سپرده را <bdi dir="ltr">Update</bdi> کند.

### <bdi dir="ltr">Fact 6: Journal Entry</bdi>

- <bdi dir="ltr">Authority: Accounting</bdi>
- <bdi dir="ltr">Business domains: Reference</bdi> به <bdi dir="ltr">`JournalId`</bdi> یا <bdi dir="ltr">Status</bdi> در صورت نیاز
- <bdi dir="ltr">Accounting</bdi> تصمیم می‌گیرد کدام <bdi dir="ltr">Template/Rules</bdi> حسابداری روی <bdi dir="ltr">Fact</bdi> معتبر اعمال شود.
- <bdi dir="ltr">Accounting</bdi> مالک این نیست که آیا <bdi dir="ltr">Deposit</bdi> واقعاً <bdi dir="ltr">available</bdi> است یا <bdi dir="ltr">Loan</bdi> قابل وصول است.

## 9. دو ماندهٔ تسهیلات: تناقض یا دو <bdi dir="ltr">Semantic</bdi>؟

سؤال دقیق:

> اگر <bdi dir="ltr">Lending</bdi> ماندهٔ اصل را نگه می‌دارد و <bdi dir="ltr">Accounting</bdi> نیز ماندهٔ حساب تسهیلات را دارد، آیا دو <bdi dir="ltr">Source of Truth</bdi> داریم؟

پاسخ: ابتدا <bdi dir="ltr">Semantic</bdi> را جدا کن.

### <bdi dir="ltr">Lending Principal Outstanding</bdi>

- برای برنامهٔ اقساط، وصول، وضعیت <bdi dir="ltr">Loan</bdi> و تصمیم عملیاتی
- از عملیات دامینی <bdi dir="ltr">Loan</bdi> تغییر می‌کند
- <bdi dir="ltr">Invariant</bdi>های قرارداد و بازپرداخت را اعمال می‌کند

### <bdi dir="ltr">Accounting Receivable/Subledger Balance</bdi>

- برای گزارش مالی، <bdi dir="ltr">Journal</bdi>، <bdi dir="ltr">Trial Balance</bdi> و تطبیق
- از <bdi dir="ltr">Posting</bdi>های معتبر تغییر می‌کند
- قواعد دورهٔ مالی و حسابداری را اعمال می‌کند

این دو باید از نظر اقتصادی قابل <bdi dir="ltr">Reconcile</bdi> باشند، ولی الزاماً در هر لحظه و هر <bdi dir="ltr">State</bdi> فنی دقیقاً یک مقدار ندارند؛ <bdi dir="ltr">Latency</bdi>، <bdi dir="ltr">Pending</bdi>، <bdi dir="ltr">Adjustment</bdi> و <bdi dir="ltr">Closing</bdi> ممکن است تفاوت کنترل‌شده بسازد. معماری باید:

- معنای هر مانده را نام‌گذاری کند؛
- <bdi dir="ltr">Event/Contract</bdi> اتصال را روشن کند؛
- <bdi dir="ltr">Expected lag</bdi> را تعیین کند؛
- <bdi dir="ltr">Reconciliation</bdi> و <bdi dir="ltr">Correction path</bdi> داشته باشد.

راه‌حل اشتباه این است که هر دو سیستم یک جدول <bdi dir="ltr">Balance</bdi> مشترک را <bdi dir="ltr">Update</bdi> کنند تا «همیشه یکی» باشند. این کار <bdi dir="ltr">Authority</bdi> و <bdi dir="ltr">Transaction Boundary</bdi> را نابود می‌کند.

## <bdi dir="ltr">10. Trigger</bdi>، <bdi dir="ltr">Decision</bdi> و <bdi dir="ltr">Fact</bdi> را جدا کن

نمونهٔ عملیات واریز اعطا:

| <bdi dir="ltr">Role</bdi> | <bdi dir="ltr">Example</bdi> |
|---|---|
| <bdi dir="ltr">Trigger owner</bdi> | <bdi dir="ltr">Lending process decides it is time to request disbursement</bdi> |
| <bdi dir="ltr">Command</bdi> | <bdi dir="ltr">`CreditDepositAccount`</bdi> |
| <bdi dir="ltr">Decision authority</bdi> | <bdi dir="ltr">Deposits decides whether account can accept credit now</bdi> |
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
