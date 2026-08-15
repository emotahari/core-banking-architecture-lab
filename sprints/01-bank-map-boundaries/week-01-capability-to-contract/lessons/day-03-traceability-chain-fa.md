# Day 03 — از System تا Contract؛ ساخت Traceability Chain

- Day budget: 50 minutes — 24 lesson + 21 exercise + 5 exit ticket
- Output: دو زنجیرهٔ قابل‌ردیابی برای مسدودی قضایی و اعطای تسهیلات
- Main skill: رفت‌وبرگشت از Outcome کسب‌وکاری تا API/Event بدون پرش مفهومی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. زنجیرهٔ `Capability → Domain → Bounded Context → Module/Service Candidate → Use Case → Contract` را مرحله‌به‌مرحله بسازی.
2. برای هر گام سؤال، Evidence و Owner مناسب ثبت کنی.
3. تشخیص بدهی کجا از نام جدول یا سامانه به Service پریده‌ای.
4. Command، Query، Result و Event را در سطح مفهومی از هم جدا کنی.
5. یک Contract Candidate را به Capability و Outcome اولیه بازگردانی و توجیه کنی.

## 2. Traceability چرا معماری است؟

معماری فقط مجموعه‌ای از Box و Arrow نیست. هر Box و Contract باید بتواند به یک مسئله و تصمیم کسب‌وکاری برگردد. اگر برای یک API نتوانیم پاسخ دهیم «کدام Use Case، در کدام مدل، برای کدام Capability و تحت مالکیت چه کسی؟»، احتمالاً Contract از روی پیاده‌سازی موجود طراحی شده است.

Traceability دو جهت دارد:

```text
Top-down:  Business outcome → capability → model → executable contract
Bottom-up: API/event/table → use case → owner → business justification
```

Top-down از ساخت Service بی‌مسئله جلوگیری می‌کند. Bottom-up برای ممیزی Legacy و حذف Contractهای بی‌مالک لازم است.

## 3. زنجیرهٔ مرجع

### 3.1 Outcome/Driver

قبل از Capability، Trigger و Outcome را روشن کن.

نمونه: «حکم معتبر قضایی باید بدون تغییر ماندهٔ دفتری، امکان برداشت مبلغ مشخص را متوقف کند و نتیجه قابل‌ممیزی باشد.»

### 3.2 Capability

بانک چه کاری باید بتواند انجام دهد؟

نمونه: `اعمال و مدیریت محدودیت روی وجوه مشتری`.

### 3.3 Domain/Subdomain

دانش اصلی و قواعد مسئله کجاست؟ ممکن است حکم و Hold در دو Subdomain متفاوت باشند:

- Legal/Compliance: اعتبار، متن، مرجع و دامنهٔ حکم
- Deposits: اثر عملیاتی Hold بر available balance و برداشت

### 3.4 Bounded Context

در کدام مرز مدل، واژه‌ها و قواعد سازگارند؟ نام Context یک Hypothesis است و باید Owner، اصطلاحات و قواعد کلیدی داشته باشد.

### 3.5 Module/Service Candidate

مسئولیت در کد کجا محصور می‌شود؟ در Week 01 پیش‌فرض `Module` است. Service Candidate فقط نامزدی برای بررسی بعدی است، نه تصمیم استقرار.

### 3.6 Use Case

یک قصد مشخص کسب‌وکاری که Actor یا سیستم همکار آغاز می‌کند:

- RegisterLegalOrder
- PlaceFundsHold
- ReleaseFundsHold
- GetHoldStatus

### 3.7 Command/Query

- Command قصد تغییر وضعیت دارد و ممکن است رد شود.
- Query اطلاعات می‌خواهد و نباید اثر کسب‌وکاری پنهان داشته باشد.

Command برابر Event نیست. `PlaceFundsHold` درخواست انجام کار است؛ `FundsHeld` واقعیتی است که پس از موفقیت رخ داده است.

### 3.8 API/Event

Contract بیرونی باید Intent یا Fact را با زبان مرز منتشر کند. نوع Transport هنوز تصمیم ثانویه است. می‌توان ابتدا Contract Card ساخت و بعد در Week 05/09 دربارهٔ REST یا Messaging تصمیم گرفت.

## 4. کارت ردیابی هر گام

برای هر ردیف زنجیره این ستون‌ها را ثبت کن:

| فیلد | سؤال |
|---|---|
| Element | نام دقیق چیست؟ |
| Type | Capability، Context، Use Case، Command، Event و...؟ |
| Owner | چه نقش/Contextی حق تغییر تصمیم را دارد؟ |
| Input evidence | چه سند، Rule یا نیاز واقعی این مورد را توجیه می‌کند؟ |
| Output/Outcome | چه چیزی پس از آن قابل مشاهده است؟ |
| Boundary rule | این عنصر چه چیزی را عمداً پنهان یا رد می‌کند؟ |
| Open question | کدام فرض هنوز اثبات نشده است؟ |

## 5. مثال کامل اول: مسدودی قضایی سپرده

### Trigger و Outcome

- Trigger: دریافت حکم قضایی معتبر با شناسه و دامنهٔ مشخص
- Outcome: مبلغ مشمول Hold قابل برداشت نباشد؛ اصل مانده و Journal مستقل باقی بمانند؛ وضعیت قابل‌پیگیری باشد.

### زنجیره

| مرحله | Candidate | دلیل |
|---|---|---|
| Capability | Manage Legal Restrictions on Funds | توانایی پایدار، مستقل از نرم‌افزار |
| Domain | Compliance/Legal + Deposits | اعتبار حکم و اعمال Hold دو دانش متفاوت‌اند |
| Subdomain | Legal Order Management / Deposit Availability Control | قواعد و Lifecycle مستقل دارند |
| Bounded Context | Legal Orders / Deposits | واژهٔ Order در یکی سند معتبر و در دیگری Reference است |
| Module | `legalorders` / `deposits` | مسئولیت و مدل داخلی جدا |
| Use Case | RegisterLegalOrder / PlaceFundsHold | دو قصد با دو Owner تصمیم |
| Command | `PlaceFundsHold(orderRef, accountId, amount)` | درخواست تغییر available funds |
| Result | Accepted / Rejected with reason | Command ممکن است رد شود |
| Event | `FundsHeld` | Fact پس از تغییر موفق |
| Query | `GetHoldStatus(holdId)` | مشاهدهٔ وضعیت بدون تغییر |

### مالکیت

- Legal Orders مالک متن، اعتبار و Lifecycle حکم است.
- Deposits مالک امکان اعمال Hold، مبلغ Held و available balance است.
- Accounting مالک Journal مالی است، نه تصمیم اجازهٔ برداشت.
- Channel فقط درخواست/نمایش را انجام می‌دهد.

این تفکیک به معنی الزام دو Microservice نیست. می‌تواند دو Module در یک Deployable باشد.

## 6. مثال کامل دوم: اعطای تسهیلات و واریز به سپرده

### Trigger و Outcome

- Trigger: قرارداد تسهیلات مصوب، امضاشده و آمادهٔ اعطا
- Outcome: تعهد Lending قطعی شود، وجه دقیقاً یک‌بار به سپرده واریز گردد و Fact مالی قابل ثبت باشد.

### زنجیرهٔ اولیه

| مرحله | Candidate | Owner اولیه |
|---|---|---|
| Capability | Execute Credit Disbursement | Lending business |
| Related capability | Credit Customer Funds | Deposits |
| Domains | Lending، Deposits، Accounting | هرکدام مدل خودش را دارد |
| Context | Loan Servicing / Deposit Account / Financial Accounting | معانی Amount/Balance/Completion متفاوت‌اند |
| Use case | DisburseLoan | Lending |
| Outbound command | CreditDeposit | Deposits تصمیم به پذیرش/رد اثر روی حساب را دارد |
| Business result | Deposit credit reference | نتیجهٔ قابل‌همبستگی |
| Events | LoanDisbursementStarted، DepositCredited، LoanDisbursed | هر Fact توسط Owner خودش |
| Accounting input | Business fact/Accounting fact candidate | نحوهٔ دقیق در Week 13 تصمیم می‌شود |

این جدول هنوز Saga، Kafka یا تراکنش توزیع‌شده را انتخاب نمی‌کند. Week 01 فقط Intent، Fact و Ownership را از هم جدا می‌کند.

## 7. Contract Card قبل از OpenAPI/AsyncAPI

قبل از نوشتن YAML این کارت را کامل کن:

```text
Contract name:
Contract type: Command | Query | Event
Business intent/fact:
Producer/owner:
Consumer role:
Preconditions:
Required inputs and meaning:
Success outcome:
Business rejections:
Identity/correlation candidate:
Sensitive data:
Versioning concern:
Unknowns:
```

این کارت جلوی دو خطا را می‌گیرد: Contract بزرگ بر اساس Entity داخلی و Event مبهمی که Consumer را مجبور به Query همگام می‌کند.

## 8. Command، Query، Result و Event

| نوع | زمان دستوری | می‌تواند رد شود؟ | Owner نام‌گذاری | نمونه |
|---|---|---:|---|---|
| Command | حال/امر | بله | Context دریافت‌کننده | `PlaceFundsHold` |
| Query | درخواست مشاهده | ممکن است Not Found | Owner داده | `GetAvailableBalance` |
| Result | پاسخ به درخواست | نتیجهٔ اجرا | Context اجراکننده | `HoldAccepted` result |
| Event | گذشته | Fact رخ داده | Context تولیدکننده | `FundsHeld` |

Event با نام `ProcessLoan` یا `DoAccounting` نه Fact روشن دارد، نه معلوم می‌کند چه چیزی کامل شده است.

## 9. نگاشت یک‌به‌یک ممنوع

این برابری‌ها معمولاً غلط‌اند:

```text
1 Capability = 1 Bounded Context
1 Bounded Context = 1 Module
1 Module = 1 Microservice
1 Use Case = 1 REST endpoint
1 Table = 1 Aggregate
1 Event = 1 Topic
```

هر نگاشت باید Forces داشته باشد. یک Capability مانند Execute Payments ممکن است Contextهای Payment Order، Fraud Control و Settlement را درگیر کند. یک Context ممکن است فعلاً چند Module داشته باشد یا برعکس، یک Module آموزشی نمایندهٔ یک Hypothesis Context باشد.

## 10. تست سازگاری زنجیره

پس از ساخت زنجیره، این هشت کنترل را انجام بده:

1. آیا نام Capability Outcome محور است؟
2. آیا Domain به دانش مسئله اشاره دارد یا نام تیم؟
3. آیا Context مرز زبان و Rule دارد؟
4. آیا Module مسئولیت منسجم دارد؟
5. آیا Use Case فقط یک قصد اصلی دارد؟
6. آیا Command توسط Owner درست دریافت می‌شود؟
7. آیا Event واقعیت گذشته و مالک روشن دارد؟
8. آیا می‌توان Contract را به Outcome اول برگرداند؟

اگر یک ردیف حذف شود و هیچ‌چیز تغییر نکند، احتمالاً تزئینی است. اگر بین دو ردیف چند تصمیم پنهان باشد، زنجیره ناقص است.

## 11. Anti-patternهای Traceability

### Database-first chain

```text
LOAN table → LoanService → CRUD API
```

Capability، Rule، Owner و Use Case حذف شده‌اند. Table فقط شاهد وضع موجود است.

### Organization-first chain

```text
ادارهٔ چک → Check microservice
```

ساختار سازمان دلیل کافی برای Boundary یا Deployment نیست.

### Vendor-first chain

```text
BIAN Current Account Service Domain → CurrentAccount microservice
```

Reference model به Blueprint محلی تبدیل شده است.

### Channel-owned business rule

```text
Mobile app → calculate available balance
```

Channel Rule دامینی را تصاحب کرده و Contract به رفتار داخلی نشت کرده است.

## 12. تمرین هدایت‌شده

برای `ReleaseFundsHold` سه سؤال پاسخ بده:

1. آیا Actor مجاز است مستقیماً Deposits را صدا بزند یا Legal Orders باید ابتدا اعتبار Release را تأیید کند؟ این تصمیم هنوز `OPEN` است.
2. Event نهایی `HoldReleaseRequested` است یا `FundsHoldReleased`؟ اولی Fact درخواست، دومی Fact اثر موفق است؛ هر دو ممکن‌اند ولی Owner متفاوت دارند.
3. آیا Release یک API همگام است یا Event؟ هنوز از روی Capability نمی‌توان Transport را تعیین کرد.

تمرین نشان می‌دهد Traceability پاسخ همه‌چیز را از پیش نمی‌دهد؛ محل تصمیم و Unknown را آشکار می‌کند.

## 13. تمرین مستقل و Rubric

[Day 03 Exercise](../exercises/day-03-traceability-chain.md) را انجام بده و از [Template](../artifacts/traceability-chain-template.md) استفاده کن.

| معیار | امتیاز |
|---|---:|
| Trigger/Outcome و Capability درست | ۲ |
| Context/Owner قابل‌دفاع | ۲ |
| Use Case و Contract بدون پرش | ۲ |
| تمایز Command/Query/Event | ۲ |
| Unknown و Reverse trace | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. وجود یک Service Candidate بدون Capability یا Owner، Critical Error است.

## 14. آزمون خروج

درس را ببند و [Exit Ticket](../quizzes/day-03-exit-ticket.md) را پاسخ بده. فردا کیفیت Boundaryهای این زنجیره را با چهار نیروی طراحی نقد می‌کنیم.

