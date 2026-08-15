# Day 04 — مالکیت داده، تصمیم و Source of Truth

- Day budget: 50 minutes including exercise and exit ticket
- Output: Data/Decision Ownership Matrix v1
- Banking case: اعطای تسهیلات، واریز به سپرده و ثبت مالی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. Data Authority، Decision Authority، State Owner و Process Owner را جدا کنی.
2. برای هر Fact با معنای دقیق، یک Authority مشخص کنی.
3. Reference، Snapshot، Cache، Projection و Derived Data را از مالکیت جدا کنی.
4. دو Balance ظاهراً مشابه را با Semantic و Purpose متفاوت تفکیک کنی.
5. Freshness، History، Correction و Reconciliation را در Ownership Matrix ثبت کنی.

## 2. چرا عبارت «مالک داده» کافی نیست؟

در جلسهٔ معماری معمولاً می‌شنویم:

> اطلاعات مشتری مال سامانهٔ مشتریان است.

این جمله جهت خوبی دارد، اما برای Contract و Failure کافی نیست. باید روشن کنیم:

- کدام اطلاعات؟ هویت Party، KYC، Segment یا Credit Exposure؟
- چه کسی تعریف Semantic را تعیین می‌کند؟
- چه کسی مجاز به ایجاد و اصلاح است؟
- چه کسی تاریخچه را نگه می‌دارد؟
- Context دیگر Reference، Snapshot یا Cache دارد؟
- اگر دو نسخه متفاوت شدند، چه کسی Reconcile می‌کند؟
- چه Decisionی از این Fact ساخته می‌شود و Authority آن کیست؟

Ownership یک Label روی Box نیست؛ مجموعه‌ای از حقوق و مسئولیت‌های قابل‌آزمون است.

## 3. مدل ذهنی

برای هر مورد این زنجیره را بنویس:

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

اگر عبارت `Customer Data` یا `Balance` آن‌قدر کلی است که چند معنای مستقل را پوشش می‌دهد، ابتدا ردیف را تجزیه کن. Ownership فقط پس از Semantic دقیق قابل تعیین است.

## 4. انواع Authority و Ownership

### 4.1 Data/Fact Authority

Contextی که معنای Fact، Lifecycle و تغییر معتبر آن را کنترل می‌کند.

مثال: Deposits برای `AvailableDepositBalance` تصمیم‌گیر و State Owner است. Accounting ممکن است اثر مالی متناظر داشته باشد، اما نمی‌تواند Available Balance را Update کند.

### 4.2 Decision Authority

Contextی که با شواهد ورودی و Ruleهای خودش مجاز است تصمیم بگیرد.

مثال:

- Customer/Compliance: آیا KYC معتبر است؟
- Lending/Credit Decision: آیا این متقاضی برای این محصول و مبلغ واجد شرایط است؟
- Deposits: آیا این حساب در وضعیت فعلی واریز را می‌پذیرد؟

این سه Decision به هم وابسته‌اند، ولی یک Boolean عمومی `isValid` نیستند.

### 4.3 State Owner

Contextی که State Machine و Transitionهای معتبر را نگه می‌دارد.

مثال: Payment Order State متعلق به Payments است؛ Channel درخواست می‌دهد و نمایش می‌دهد، ولی نباید Order را از `Submitted` به `Settled` ببرد.

### 4.4 Trigger Owner

Context یا Actorی که یک Intent را آغاز می‌کند. Trigger بودن Authority تصمیم را منتقل نمی‌کند.

Lending می‌تواند واریز مبلغ اعطا را درخواست کند، اما Deposits دربارهٔ اجرای Credit روی حساب خودش تصمیم می‌گیرد.

### 4.5 Process Owner/Process Manager

در جریان چنددامینی، یک Process Manager می‌تواند Correlation، Step Status، Timeout و Next Action را نگه دارد. این جزء نباید State داخلی Domainها را تصاحب کند.

مثلاً وضعیت `DisbursementProcess = WAITING_FOR_DEPOSIT_CREDIT` متعلق به Process است؛ ولی `DepositTransaction = POSTED` متعلق به Deposits و `Journal = POSTED` متعلق به Accounting است.

## 5. Source of Truth را دقیق‌تر کنیم

عبارت `Single Source of Truth` اغلب باعث دو خطا می‌شود:

1. تصور می‌کنیم برای تمام معناهای یک کلمه فقط یک Database باید وجود داشته باشد.
2. Replica یا Report را به‌دلیل داشتن داده، Owner می‌نامیم.

در این دوره از اصطلاح دقیق‌تر استفاده می‌کنیم:

> برای هر Fact با Semantic مشخص، یک Authoritative Context و یک Source of Record تعریف می‌شود.

### Authoritative Context

قواعد، معنای Business و تغییر معتبر را مالک است.

### Source of Record

رکورد پایدار و قابل استناد آن Fact را نگه می‌دارد. در طراحی ساده معمولاً داخل همان Context است؛ ولی Migration یا Legacy می‌تواند موقتاً پیچیدگی ایجاد کند و باید صریح ثبت شود.

### نکتهٔ مهم

ممکن است چند «Balance» معتبر داشته باشیم، چون معنا متفاوت است:

- Operational Principal Outstanding در Lending
- Accounting Receivable Balance در Subledger/Accounting
- Analytical Exposure Projection در Data Platform

این‌ها سه Owner برای یک Fact نیستند؛ سه Fact با Purpose، زمان و Rule متفاوت‌اند. باید نام و Reconciliation آن‌ها دقیق باشد.

## 6. نقش Copyها

داشتن یک مقدار در چند Context لزوماً Ownership مشترک نیست. نوع Copy را ثبت کن.

### Reference

فقط شناسهٔ Fact بیرونی را نگه می‌دارد.

مثال: Lending یک `CustomerId` نگه می‌دارد و هویت Party را مالک نمی‌شود.

### Snapshot

کپی تاریخی از Factها در زمان یک تعهد/تصمیم است و تغییر آیندهٔ Upstream نباید آن را خودکار تغییر دهد.

مثال: نرخ، مدت و شروط مؤثر قرارداد اعطاشده از ProductVersion Snapshot می‌شوند.

Snapshot باید داشته باشد:

- effective time
- source/version
- reason/use case
- correction policy

### Cache

کپی موقت برای Performance/Availability با TTL یا Invalidation Policy. Cache Fact جدیدی ایجاد نمی‌کند.

مثال: Channel ممکن است Customer Display Name را Cache کند، ولی اصلاح نام در Master را انجام نمی‌دهد.

### Projection

مدل Read که از Fact/Eventهای Authority ساخته و قابل بازسازی است.

مثال: داشبورد یکپارچهٔ تعهدات مشتری از Lending، Deposits و Accounting Projection می‌سازد؛ Owner عملیات پایه نیست.

### Derived Data

مقداری که از Sourceها و Formula مشخص محاسبه می‌شود.

مثال: `TotalCustomerExposure` ممکن است Derived باشد. باید Owner Formula، Source versions، as-of time و Recalculation مشخص باشد.

### Replica

کپی فنی برای Availability/Read scale است. Replica حتی اگر Read از آن انجام شود، Authority دامینی جدید نیست.

## 7. جدول کنترل Copy

| Copy type | Can change source fact? | Must have provenance? | Freshness rule | Historical role |
|---|---:|---:|---|---|
| Reference | no | yes | resolve policy | points to authority |
| Snapshot | no | yes | fixed at effective time | preserves past commitment |
| Cache | no | yes | TTL/invalidation | usually not authoritative history |
| Projection | no | yes | lag/rebuild policy | read history as designed |
| Derived | no, but owns formula/result | yes | recompute policy | as-of/version required |
| Replica | no | technical lineage | replication lag | same record technically |

## 8. مثال هدایت‌شده: اعطای تسهیلات مرابحه

### Fact 1: Party Identity

- Authority: Party & Customer
- Lending: Reference و Snapshot شواهد لازم تصمیم
- Accounting: Reference برای تفصیل/Audit در صورت نیاز
- Forbidden: Lending یا Accounting اصلاح نام و هویت Master را انجام دهند.

### Fact 2: Product Definition

- Authority: Product Catalog
- Agreement/Lending: Snapshot نسخه و شروط مؤثر
- نکته: تغییر ProductVersion آینده قرارداد گذشته را تغییر نمی‌دهد.

### Fact 3: Loan Grant State

- Authority: Lending
- Deposits: Consumer درخواست/Reference اعطا به‌اندازهٔ لازم
- Accounting: Consumer Business Fact برای ثبت مالی
- Forbidden: Accounting از روی وجود Journal، State اعطا را در Lending تغییر دهد.

### Fact 4: Operational Loan Principal Outstanding

- Authority: Lending
- Accounting: ماندهٔ مالی متناظر با Semantic حسابداری، نه کپی قابل‌تغییر از Operational State
- Reconciliation: اختلاف باید کشف و با Owner مشترک فرایند رسیدگی شود، اما هر سیستم اصلاح State خودش را طبق کنترل انجام می‌دهد.

### Fact 5: Deposit Credit Transaction و Available Balance

- Authority: Deposits
- Lending: Result/Fact و Process status
- Accounting: رویداد لازم برای Journal مربوط به اثر سپرده
- Forbidden: Orchestrator یا Lending مستقیماً ماندهٔ سپرده را Update کند.

### Fact 6: Journal Entry

- Authority: Accounting
- Business domains: Reference به `JournalId` یا Status در صورت نیاز
- Accounting تصمیم می‌گیرد کدام Template/Rules حسابداری روی Fact معتبر اعمال شود.
- Accounting مالک این نیست که آیا Deposit واقعاً available است یا Loan قابل وصول است.

## 9. دو ماندهٔ تسهیلات: تناقض یا دو Semantic؟

سؤال دقیق:

> اگر Lending ماندهٔ اصل را نگه می‌دارد و Accounting نیز ماندهٔ حساب تسهیلات را دارد، آیا دو Source of Truth داریم؟

پاسخ: ابتدا Semantic را جدا کن.

### Lending Principal Outstanding

- برای برنامهٔ اقساط، وصول، وضعیت Loan و تصمیم عملیاتی
- از عملیات دامینی Loan تغییر می‌کند
- Invariantهای قرارداد و بازپرداخت را اعمال می‌کند

### Accounting Receivable/Subledger Balance

- برای گزارش مالی، Journal، Trial Balance و تطبیق
- از Postingهای معتبر تغییر می‌کند
- قواعد دورهٔ مالی و حسابداری را اعمال می‌کند

این دو باید از نظر اقتصادی قابل Reconcile باشند، ولی الزاماً در هر لحظه و هر State فنی دقیقاً یک مقدار ندارند؛ Latency، Pending، Adjustment و Closing ممکن است تفاوت کنترل‌شده بسازد. معماری باید:

- معنای هر مانده را نام‌گذاری کند؛
- Event/Contract اتصال را روشن کند؛
- Expected lag را تعیین کند؛
- Reconciliation و Correction path داشته باشد.

راه‌حل اشتباه این است که هر دو سیستم یک جدول Balance مشترک را Update کنند تا «همیشه یکی» باشند. این کار Authority و Transaction Boundary را نابود می‌کند.

## 10. Trigger، Decision و Fact را جدا کن

نمونهٔ عملیات واریز اعطا:

| Role | Example |
|---|---|
| Trigger owner | Lending process decides it is time to request disbursement |
| Command | `CreditDepositAccount` |
| Decision authority | Deposits decides whether account can accept credit now |
| State owner | Deposits records transaction and updates its balance |
| Resulting fact | `DepositCredited` or explicit rejection fact/result |
| Process observer | Lending/Process Manager advances its own status |
| Financial consumer | Accounting produces relevant Journal from valid facts |

این تفکیک مانع آن می‌شود که Orchestrator به Super-Domain و مالک همه‌چیز تبدیل شود.

## 11. Correction و Reconciliation بخشی از Ownership است

Owner فقط Happy Path را مالک نیست. باید روشن باشد:

- چه کسی خطا را تشخیص می‌دهد؟
- چه کسی مجاز به Correction است؟
- Correction با Update، Reversal یا Compensating Fact انجام می‌شود؟
- Audit trail کجاست؟
- چه کسی اختلاف میان Operational و Accounting Projection را پیگیری می‌کند؟

جزئیات Accounting/Reversal در Sprintهای بعد می‌آید، اما در Matrix حداقل `Reconciliation owner` و `Open Question` باید ثبت شود.

## 12. خطاهای رایج

### مالکیت مشترک

«Lending و Accounting هر دو مالک ماندهٔ تسهیلات‌اند» ابهام Semantic را پنهان می‌کند. دو مانده را نام‌گذاری کن.

### Database برابر Owner

داشتن جدول یا Replica به معنی Authority نیست. در Migration ممکن است رکورد فیزیکی موقتاً جای دیگری باشد.

### Event Consumer برابر Owner

Accounting با مصرف `LoanGranted` مالک Loan نمی‌شود. Projection نیز Authority نمی‌سازد.

### Orchestrator برابر Owner

Process Manager Step Status را نگه می‌دارد؛ Factهای Domain را جعل یا تصاحب نمی‌کند.

### Snapshot بدون زمان و Version

کپی بدون Provenance به‌سرعت به Master پنهان و متناقض تبدیل می‌شود.

### «همه‌چیز را همگام Query کنیم»

Query زنده برای Product terms قرارداد گذشته یا شواهد تصمیم می‌تواند تاریخچه را خراب کند. Reference، Snapshot و Cache باید بر اساس Use Case انتخاب شوند.

### RACI به‌جای Data Authority

RACI سازمانی مفید است، ولی نمی‌گوید کدام Context مجاز به Transition State و انتشار Fact است. هر دو Artifact ممکن است لازم باشند.

## 13. روش تکمیل Ownership Matrix

برای هر ردیف:

1. Semantic را آن‌قدر دقیق کن که یک Fact باشد.
2. Context Authority را انتخاب کن.
3. دیگر Contextها را `Reference/Snapshot/Projection/Cache/Consumer/Not Allowed` علامت بزن.
4. Freshness و History rule را ثبت کن.
5. Decisionهای وابسته را جدا بنویس.
6. Reconciliation owner و Correction path را مشخص یا Open Question کن.
7. با یک Failure یا Change واقعی تصمیم را آزمایش کن.

## 14. تمرین هدایت‌شده

برای `Product Definition` و `Executed Agreement Terms` دو ردیف مستقل بساز. اگر Owner و Lifecycle هر دو را یکی نوشتی، سناریوی انتشار ProductVersion جدید پس از انعقاد قرارداد را اجرا کن و پاسخ را بازبینی کن.

## 15. تمرین مستقل

[Day 04 Exercise — Ownership Matrix](../exercises/day-04-ownership-matrix.md) را انجام بده. حداقل ۱۲ Fact و پنج Decision را تحلیل کن.

## 16. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| Semantic دقیق و یک Authority | ۳ |
| تفکیک Data/Decision/Process ownership | ۲ |
| استفادهٔ درست از Copy types | ۲ |
| Freshness/History/Reconciliation | ۲ |
| تشخیص Forbidden ownership | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. وجود Authority مشترک برای یک Fact با معنای یکسان Critical Error است.

## 17. آزمون خروج

درس را ببند و [Day 04 Exit Ticket](../quizzes/day-04-exit-ticket.md) را پاسخ بده.

## 18. منابع

- [DDD Reference — Bounded Context and Context Map](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- [BIAN Service Landscape 14.0](https://bian.org/deliverables/service-landscape/) برای Gap Check مسئولیت‌ها، نه واگذاری Ownership محلی

الگوی Copy و ماتریس Authority در این درس یک Synthesis معماری برای Lab است و باید با مقررات، خبرگان و Operating Model بانک اعتبارسنجی شود.
