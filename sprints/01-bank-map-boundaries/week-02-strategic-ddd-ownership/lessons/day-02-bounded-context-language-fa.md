# Day 02 — Bounded Context و Ubiquitous Language

- Day budget: 45 minutes including exercise and exit ticket
- Output: Language Conflicts v0.1 و Boundary Hypotheses
- Banking case: تفاوت معنای Account، Customer، Product، Contract و Balance

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. Bounded Context را به‌عنوان مرز اعتبار مدل و زبان تعریف کنی.
2. آن را از Domain، Subdomain، Application، Team، Module و Microservice جدا کنی.
3. Homonym، Synonym، Rule Conflict و Lifecycle Conflict را به‌عنوان سرنخ مرز کشف کنی.
4. برای یک واژهٔ بانکی، معنای Contextual و ترجمهٔ لازم را بنویسی.
5. یک Boundary Hypothesis بسازی و شواهد موافق و مخالف آن را ثبت کنی.

## 2. مدل ذهنی

در بانک، کلمات مشترک الزاماً مفهوم مشترک ندارند. مشکل وقتی شروع می‌شود که یک واژهٔ واحد را به یک Entity سازمانی عظیم تبدیل کنیم.

واژهٔ `Account` را ببین:

- در Deposits: رابطهٔ عملیاتی نگهداری وجوه، وضعیت، مانده و محدودیت‌ها
- در Lending: موقعیت بدهی یا Facility و برنامهٔ بازپرداخت
- در Accounting: حساب دفتر کل، معین یا تفصیلی برای طبقه‌بندی آثار مالی
- در IAM: حساب کاربری و دسترسی

این‌ها چهار View از یک Entity واحد نیستند. مدل، رفتار، شناسه، Lifecycle و Invariant آن‌ها متفاوت است.

مدل ذهنی درست:

~~~text
large domain language
        ↓ ambiguity and contradiction
explicit Bounded Contexts
        ↓
internally consistent model + Ubiquitous Language
        ↓
translation through explicit contracts
~~~

## 3. تعریف دقیق Bounded Context

Bounded Context مرزی صریح است که **درون آن یک مدل مشخص و Ubiquitous Language مرتبط با آن، معنای سازگار و معتبر دارد**.

سه کلمهٔ تعریف مهم‌اند:

- `Boundary`: معلوم است مدل کجا معتبر است و کجا نیست.
- `Model`: فقط Vocabulary نیست؛ مفاهیم، روابط، رفتارها و قواعد را دربر می‌گیرد.
- `Consistency`: یک اصطلاح درون Context نباید چند معنای متناقض داشته باشد.

Bounded Context خودش «معنای یک واژه» نیست. مثلاً «معنای قرارداد در حسابداری» یک Context نیست؛ `Financial Accounting Context` مرزی است که در آن Contract ممکن است فقط Reference یا Accounting Dimension باشد.

## 4. Ubiquitous Language چیست؟

Ubiquitous Language زبانی دقیق است که Domain Expert، Analyst، Developer، Test و Code **درون یک Context** از آن استفاده می‌کنند.

ویژگی‌های آن:

- در گفت‌وگو و کد یکسان است.
- از رفتار و Rule حرف می‌زند، نه صرفاً ستون و فرم.
- مثال و ضد‌مثال دارد.
- با کشف Domain تکامل می‌یابد.
- ابهام را پنهان نمی‌کند؛ آن را به سؤال تبدیل می‌کند.

نمونهٔ ضعیف:

> وضعیت تراکنش آپدیت شد.

پرسش‌های پنهان:

- تراکنش سپرده، Payment Order یا Journal Posting؟
- وضعیت از چه چیزی به چه چیزی؟
- چه Contextی مجاز به این Transition است؟
- رخداد `Executed`، `Settled` یا `Posted` است؟

نمونهٔ دقیق‌تر در Payments:

> Payment Order پس از پذیرش شبکه از `Submitted` به `AcceptedForClearing` رفت؛ Settlement هنوز رخ نداده است.

نام State و Event اکنون قابل مدل‌سازی و آزمون است.

## 5. Ubiquitous Language، فرهنگ لغت سراسری نیست

بانک به واژه‌نامهٔ سازمانی برای هماهنگی نیاز دارد، اما یک Enterprise Dictionary نباید Contextual Meaning را حذف کند.

روش درست:

- اصطلاح مشترک و شناسهٔ مرجع در سطح سازمان ثبت می‌شود.
- هر Context معنای دقیق، Lifecycle و Rule خودش را اعلام می‌کند.
- تفاوت‌ها در Translation Contract آشکار می‌شوند.

روش نادرست:

> چون همه از کلمهٔ Customer استفاده می‌کنند، یک `CustomerEntity` مشترک در همهٔ سرویس‌ها می‌سازیم.

پیامد:

- تغییر KYC، Marketing Segment، Borrower Role و Accounting Party به یک Schema واحد کاپل می‌شود.
- Contextها فیلدهایی را حمل می‌کنند که معنای آن را نمی‌فهمند.
- Owner واقعی گم می‌شود.

معمولاً Contextها به `PartyId`، یک Contract و گاهی Snapshot نیاز دارند؛ نه Entity داخلی مشترک.

## 6. تفاوت مفاهیم مجاور

| مفهوم | متعلق به | پرسش اصلی | نگاشت با Bounded Context |
|---|---|---|---|
| Domain | Problem Space | حوزهٔ مسئله چیست؟ | می‌تواند چند Context داشته باشد |
| Subdomain | Problem Space | کدام ناحیهٔ دانش/Outcome متمایز است؟ | هدف، Alignment مناسب با Context است |
| Bounded Context | Model/Solution boundary | کجا این مدل و زبان معتبر است؟ | موضوع این درس |
| Application | Landscape | کدام نرم‌افزار اکنون کار را انجام می‌دهد؟ | می‌تواند چند Context را مخلوط کند |
| Team | Organization | چه کسانی تغییر را انجام می‌دهند؟ | بهتر است مالکیت روشن داشته باشد، ولی مساوی Context نیست |
| Module | Code | کدام مسئولیت در کد محصور است؟ | می‌تواند Context را در Runtime واحد پیاده کند |
| Service | Runtime | چه چیزی مستقل Deploy/Operate می‌شود؟ | تصمیم فیزیکی جداگانه است |

یک Context می‌تواند فعلاً Module باشد و بعداً Service شود. یک Application Legacy ممکن است چند Context نامنسجم را حمل کند. یک تیم می‌تواند موقتاً مالک چند Context باشد، ولی هر Context باید Authority روشن داشته باشد.

## 7. سرنخ‌های کشف Boundary

هیچ سرنخ به‌تنهایی اثبات نیست. چند Force باید کنار هم قرار گیرند.

### 7.1 Homonym: واژهٔ یکسان، معنای متفاوت

`Balance`:

- Available Balance در Deposits
- Principal Outstanding در Lending
- GL Balance در Accounting
- Settlement Position در Payments

اگر همه را یک ستون `BALANCE` بدانیم، تصمیم‌های عملیاتی و مالی قاطی می‌شوند.

### 7.2 Synonym: واژه‌های متفاوت، مفهوم یکسان

ممکن است دو تیم برای یک مفهوم از `Loan Contract` و `Facility Agreement` استفاده کنند. پیش از ساخت دو Context باید بررسی کنیم آیا واقعاً Rule/Lifecycle متفاوت است یا صرفاً اختلاف نام تاریخی است.

### 7.3 Rule Conflict

در Deposits، Account بسته نباید Debit عملیاتی جدید بپذیرد. در Accounting، یک حساب GL بسته‌شده در دوره ممکن است هنوز برای Adjustment کنترل‌شده نیاز به Posting خاص داشته باشد. واژهٔ `closed account` قواعد متفاوت دارد.

### 7.4 Lifecycle Conflict

Product Definition می‌تواند Version جدید بگیرد. Agreement منعقدشده نباید با تغییر Product آینده خودکار عوض شود. تفاوت Lifecycle نشانهٔ قوی جدایی مدل Product و Executed Agreement است.

### 7.5 Authority Conflict

اگر Lending می‌گوید Customer eligible است و Customer Context می‌گوید KYC معتبر است، این‌ها شاید دو Decision متفاوت باشند:

- KYC validity متعلق به Customer/Compliance
- Credit eligibility متعلق به Lending/Credit Decision

تلاش برای یک Boolean مشترک `isValidCustomer` دو معنای تصمیم را پنهان می‌کند.

### 7.6 Change Coupling

اگر تغییر یک Rule در Product Pricing همیشه مجبور است Deposit Balance Model را Release کند، Boundary یا Contract احتمالاً اطلاعات داخلی را نشت داده است.

## 8. مثال بانکی: Product و Agreement

فرض کن محصول مرابحه نسخهٔ 7 این ویژگی‌ها را دارد:

- دامنهٔ مبلغ مجاز
- نرخ/سود مصوب
- مدت‌های قابل انتخاب
- وثایق مجاز
- تاریخ اعتبار نسخه

مشتری در تاریخ مشخص قرارداد می‌بندد. پس از آن نسخهٔ 8 محصول منتشر می‌شود.

دو مدل داریم:

### Product Catalog Model

- Product و ProductVersion
- شرایط قابل عرضه
- Eligibility policy عمومی
- Lifecycle انتشار/بازنشستگی نسخه

### Executed Agreement Model

- طرفین قرارداد
- شرایط قطعی و Snapshotشده
- تاریخ مؤثر
- تعهدات و وضعیت حقوقی
- اصلاحیه‌های معتبر

اگر Agreement فقط `productId` را نگه دارد و هر بار شرایط فعلی Product را Query کند، قرارداد گذشته با تغییر آینده عوض می‌شود. Boundary مناسب، تفاوت بین **Reference** و **Snapshot** را آشکار می‌کند.

ممکن است این دو مدل فعلاً در یک Deployable Application یا حتی یک Module آموزشی باشند؛ اما زبان و Lifecycle آن‌ها باید جدا بماند. این مثال نشان می‌دهد Mapping میان Context، Module و Service الزاماً یک‌به‌یک نیست.

## 9. مثال بانکی: Customer در سه Context

### Party & Customer Context

- هویت Party
- نوع شخص حقیقی/حقوقی
- اطلاعات پایه
- وضعیت KYC و رابطهٔ مشتری

### Lending Context

- Borrower/Obligor role
- Credit exposure
- Eligibility و Risk attributes موردنیاز تصمیم
- Snapshot شواهد تصمیم در زمان اعطا

### Accounting Context

- Party/Customer reference برای تفصیل، گزارش یا Audit
- نه مالک KYC
- نه مالک Credit Eligibility

یک `CustomerId` مشترک می‌تواند Correlation ایجاد کند؛ اما مدل Customer در هر Context متفاوت است. Lending نباید اطلاعات هویتی را بدون Contract تغییر دهد و Accounting نباید از روی Journal تصمیم بگیرد Customer از نظر KYC معتبر است.

## 10. Boundary Hypothesis چگونه نوشته می‌شود؟

یک Boundary خوب از روی اسم انتخاب نمی‌شود. قالب:

> به‌دلیل تفاوت در [Language/Rules/Lifecycle/Authority/Change]، فرض می‌کنیم مدل A و B در دو Bounded Context قرار گیرند. این فرض با [مصاحبه، مثال، تغییر واقعی، تست] اعتبارسنجی می‌شود. Counter-evidence فعلی [X] است.

نمونه:

> به‌دلیل تفاوت Lifecycle میان ProductVersion و ExecutedAgreement و نیاز به ثابت‌ماندن شروط قرارداد، فرض می‌کنیم Product Catalog و Agreement Management دو Context متمایزند. این فرض با بررسی سناریوی اصلاح محصول، الحاقیهٔ قرارداد و Owner تصمیم اعتبارسنجی می‌شود. Counter-evidence: در ساختار فعلی یک تیم و یک Database هر دو را نگه می‌دارند.

ساختار فعلی Counter-evidence یا Constraint است؛ ولی به‌تنهایی مدل مسئله را رد نمی‌کند.

## 11. خطاهای رایج

### Context را با Namespace یکی گرفتن

ساخت Package یک Boundary را enforce می‌کند، اما وجود Package دلیل دامینی آن نیست.

### Context را با تیم یکی گرفتن

Team Topology مهم است، ولی چارت تاریخی نمی‌تواند تعریف مدل را به‌تنهایی تعیین کند.

### یک مدل Canonical برای کل بانک

Canonical Enterprise Model اغلب تفاوت معناها را با فیلد Optional پنهان می‌کند. Published Language برای Integration با Universal Domain Model یکی نیست.

### مرز بر اساس CRUD

`CustomerCRUDContext` دربارهٔ رفتار و دانش چیزی نمی‌گوید. Use Case و Rule باید مرز را روشن کنند.

### هر تفاوت واژه یک Context

اختلاف نام ممکن است فقط Synonym باشد. Context جدید هزینهٔ ترجمه، Governance و Integration دارد و نیازمند چند شاهد است.

### یک Context برابر یک Microservice

Bounded Context یک Boundary مدل است؛ Microservice Boundary علاوه بر آن به Scale، Team Autonomy، Availability، Data و Operations پاسخ می‌دهد.

## 12. تمرین هدایت‌شده

برای واژهٔ `Transaction` سه معنا بنویس:

1. Deposits
2. Payments
3. Accounting

برای هرکدام پاسخ بده:

- Trigger چیست؟
- Lifecycle چیست؟
- Completion چه معنایی دارد؟
- Owner وضعیت کیست؟

اگر پاسخ‌ها یکسان نیستند، یک Entity مشترک `Transaction` احتمالاً مدل ضعیفی است.

## 13. تمرین مستقل

[Day 02 Exercise — Language Conflicts](../exercises/day-02-language-conflicts.md) را انجام بده. حداقل پنج اصطلاح را در دو یا چند Context تحلیل کن و برای دو Boundary Hypothesis شواهد موافق و مخالف بنویس.

## 14. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تعریف دقیق Bounded Context | ۲ |
| تشخیص معنای Contextual واژه‌ها | ۲ |
| تفکیک Context از Domain/System/Module/Service | ۲ |
| Boundary Hypothesis با چند Force | ۳ |
| ثبت Counter-evidence/Open Question | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 15. آزمون خروج

درس را ببند و [Day 02 Exit Ticket](../quizzes/day-02-exit-ticket.md) را پاسخ بده.

## 16. منبع اصلی

- [Domain-Driven Design Reference — Bounded Context and Ubiquitous Language](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

تعریف‌ها از مرجع DDD گرفته شده‌اند؛ مثال‌ها و Boundaryهای بانکی این درس، مدل آموزشی و Hypothesis هستند.
