<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 03</span> — از <span dir="ltr">System</span> تا <span dir="ltr">Contract</span>؛ ساخت <span dir="ltr">Traceability Chain</span>

- <span dir="ltr">Day budget: 50 minutes</span> — <span dir="ltr">24 lesson</span> + <span dir="ltr">21 exercise</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output:</span> دو زنجیرهٔ قابل‌ردیابی برای مسدودی قضایی و اعطای تسهیلات
- <span dir="ltr">Main skill:</span> رفت‌وبرگشت از <span dir="ltr">Outcome</span> کسب‌وکاری تا <span dir="ltr">API/Event</span> بدون پرش مفهومی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. زنجیرهٔ <span dir="ltr">`Capability → Domain → Bounded Context → Module/Service Candidate → Use Case → Contract`</span> را مرحله‌به‌مرحله بسازی.
2. برای هر گام سؤال، <span dir="ltr">Evidence</span> و <span dir="ltr">Owner</span> مناسب ثبت کنی.
3. تشخیص بدهی کجا از نام جدول یا سامانه به <span dir="ltr">Service</span> پریده‌ای.
4. <span dir="ltr">Command</span>، <span dir="ltr">Query</span>، <span dir="ltr">Result</span> و <span dir="ltr">Event</span> را در سطح مفهومی از هم جدا کنی.
5. یک <span dir="ltr">Contract Candidate</span> را به <span dir="ltr">Capability</span> و <span dir="ltr">Outcome</span> اولیه بازگردانی و توجیه کنی.

## <span dir="ltr">2. Traceability</span> چرا معماری است؟

معماری فقط مجموعه‌ای از <span dir="ltr">Box</span> و <span dir="ltr">Arrow</span> نیست. هر <span dir="ltr">Box</span> و <span dir="ltr">Contract</span> باید بتواند به یک مسئله و تصمیم کسب‌وکاری برگردد. اگر برای یک <span dir="ltr">API</span> نتوانیم پاسخ دهیم «کدام <span dir="ltr">Use Case</span>، در کدام مدل، برای کدام <span dir="ltr">Capability</span> و تحت مالکیت چه کسی؟»، احتمالاً <span dir="ltr">Contract</span> از روی پیاده‌سازی موجود طراحی شده است.

<span dir="ltr">Traceability</span> دو جهت دارد:


</div>

<div dir="ltr" align="left">

```text
Top-down:  Business outcome → capability → model → executable contract
Bottom-up: API/event/table → use case → owner → business justification
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Top-down</span> از ساخت <span dir="ltr">Service</span> بی‌مسئله جلوگیری می‌کند. <span dir="ltr">Bottom-up</span> برای ممیزی <span dir="ltr">Legacy</span> و حذف <span dir="ltr">Contract</span>های بی‌مالک لازم است.

## 3. زنجیرهٔ مرجع

### <span dir="ltr">3.1 Outcome/Driver</span>

قبل از <span dir="ltr">Capability</span>، <span dir="ltr">Trigger</span> و <span dir="ltr">Outcome</span> را روشن کن.

نمونه: «حکم معتبر قضایی باید بدون تغییر ماندهٔ دفتری، امکان برداشت مبلغ مشخص را متوقف کند و نتیجه قابل‌ممیزی باشد.»

### <span dir="ltr">3.2 Capability</span>

بانک چه کاری باید بتواند انجام دهد؟

نمونه: <span dir="ltr">`اعمال و مدیریت محدودیت روی وجوه مشتری`</span>.

### <span dir="ltr">3.3 Domain/Subdomain</span>

دانش اصلی و قواعد مسئله کجاست؟ ممکن است حکم و <span dir="ltr">Hold</span> در دو <span dir="ltr">Subdomain</span> متفاوت باشند:

- <span dir="ltr">Legal/Compliance:</span> اعتبار، متن، مرجع و دامنهٔ حکم
- <span dir="ltr">Deposits:</span> اثر عملیاتی <span dir="ltr">Hold</span> بر <span dir="ltr">available balance</span> و برداشت

### <span dir="ltr">3.4 Bounded Context</span>

در کدام مرز مدل، واژه‌ها و قواعد سازگارند؟ نام <span dir="ltr">Context</span> یک <span dir="ltr">Hypothesis</span> است و باید <span dir="ltr">Owner</span>، اصطلاحات و قواعد کلیدی داشته باشد.

### <span dir="ltr">3.5 Module/Service Candidate</span>

مسئولیت در کد کجا محصور می‌شود؟ در <span dir="ltr">Week 01</span> پیش‌فرض <span dir="ltr">`Module`</span> است. <span dir="ltr">Service Candidate</span> فقط نامزدی برای بررسی بعدی است، نه تصمیم استقرار.

### <span dir="ltr">3.6 Use Case</span>

یک قصد مشخص کسب‌وکاری که <span dir="ltr">Actor</span> یا سیستم همکار آغاز می‌کند:

- <span dir="ltr">RegisterLegalOrder</span>
- <span dir="ltr">PlaceFundsHold</span>
- <span dir="ltr">ReleaseFundsHold</span>
- <span dir="ltr">GetHoldStatus</span>

### <span dir="ltr">3.7 Command/Query</span>

- <span dir="ltr">Command</span> قصد تغییر وضعیت دارد و ممکن است رد شود.
- <span dir="ltr">Query</span> اطلاعات می‌خواهد و نباید اثر کسب‌وکاری پنهان داشته باشد.

<span dir="ltr">Command</span> برابر <span dir="ltr">Event</span> نیست. <span dir="ltr">`PlaceFundsHold`</span> درخواست انجام کار است؛ <span dir="ltr">`FundsHeld`</span> واقعیتی است که پس از موفقیت رخ داده است.

### <span dir="ltr">3.8 API/Event</span>

<span dir="ltr">Contract</span> بیرونی باید <span dir="ltr">Intent</span> یا <span dir="ltr">Fact</span> را با زبان مرز منتشر کند. نوع <span dir="ltr">Transport</span> هنوز تصمیم ثانویه است. می‌توان ابتدا <span dir="ltr">Contract Card</span> ساخت و بعد در <span dir="ltr">Week 05/09</span> دربارهٔ <span dir="ltr">REST</span> یا <span dir="ltr">Messaging</span> تصمیم گرفت.

## 4. کارت ردیابی هر گام

برای هر ردیف زنجیره این ستون‌ها را ثبت کن:

| فیلد | سؤال |
|---|---|
| <span dir="ltr">Element</span> | نام دقیق چیست؟ |
| <span dir="ltr">Type</span> | <span dir="ltr">Capability</span>، <span dir="ltr">Context</span>، <span dir="ltr">Use Case</span>، <span dir="ltr">Command</span>، <span dir="ltr">Event</span> و...؟ |
| <span dir="ltr">Owner</span> | چه نقش/<span dir="ltr">Context</span>ی حق تغییر تصمیم را دارد؟ |
| <span dir="ltr">Input evidence</span> | چه سند، <span dir="ltr">Rule</span> یا نیاز واقعی این مورد را توجیه می‌کند؟ |
| <span dir="ltr">Output/Outcome</span> | چه چیزی پس از آن قابل مشاهده است؟ |
| <span dir="ltr">Boundary rule</span> | این عنصر چه چیزی را عمداً پنهان یا رد می‌کند؟ |
| <span dir="ltr">Open question</span> | کدام فرض هنوز اثبات نشده است؟ |

## 5. مثال کامل اول: مسدودی قضایی سپرده

### <span dir="ltr">Trigger</span> و <span dir="ltr">Outcome</span>

- <span dir="ltr">Trigger:</span> دریافت حکم قضایی معتبر با شناسه و دامنهٔ مشخص
- <span dir="ltr">Outcome:</span> مبلغ مشمول <span dir="ltr">Hold</span> قابل برداشت نباشد؛ اصل مانده و <span dir="ltr">Journal</span> مستقل باقی بمانند؛ وضعیت قابل‌پیگیری باشد.

### زنجیره

| مرحله | <span dir="ltr">Candidate</span> | دلیل |
|---|---|---|
| <span dir="ltr">Capability</span> | <span dir="ltr">Manage Legal Restrictions on Funds</span> | توانایی پایدار، مستقل از نرم‌افزار |
| <span dir="ltr">Domain</span> | <span dir="ltr">Compliance/Legal</span> + <span dir="ltr">Deposits</span> | اعتبار حکم و اعمال <span dir="ltr">Hold</span> دو دانش متفاوت‌اند |
| <span dir="ltr">Subdomain</span> | <span dir="ltr">Legal Order Management</span> / <span dir="ltr">Deposit Availability Control</span> | قواعد و <span dir="ltr">Lifecycle</span> مستقل دارند |
| <span dir="ltr">Bounded Context</span> | <span dir="ltr">Legal Orders</span> / <span dir="ltr">Deposits</span> | واژهٔ <span dir="ltr">Order</span> در یکی سند معتبر و در دیگری <span dir="ltr">Reference</span> است |
| <span dir="ltr">Module</span> | <span dir="ltr">`legalorders`</span> / <span dir="ltr">`deposits`</span> | مسئولیت و مدل داخلی جدا |
| <span dir="ltr">Use Case</span> | <span dir="ltr">RegisterLegalOrder</span> / <span dir="ltr">PlaceFundsHold</span> | دو قصد با دو <span dir="ltr">Owner</span> تصمیم |
| <span dir="ltr">Command</span> | <span dir="ltr">`PlaceFundsHold(orderRef, accountId, amount)`</span> | درخواست تغییر <span dir="ltr">available funds</span> |
| <span dir="ltr">Result</span> | <span dir="ltr">Accepted</span> / <span dir="ltr">Rejected with reason</span> | <span dir="ltr">Command</span> ممکن است رد شود |
| <span dir="ltr">Event</span> | <span dir="ltr">`FundsHeld`</span> | <span dir="ltr">Fact</span> پس از تغییر موفق |
| <span dir="ltr">Query</span> | <span dir="ltr">`GetHoldStatus(holdId)`</span> | مشاهدهٔ وضعیت بدون تغییر |

### مالکیت

- <span dir="ltr">Legal Orders</span> مالک متن، اعتبار و <span dir="ltr">Lifecycle</span> حکم است.
- <span dir="ltr">Deposits</span> مالک امکان اعمال <span dir="ltr">Hold</span>، مبلغ <span dir="ltr">Held</span> و <span dir="ltr">available balance</span> است.
- <span dir="ltr">Accounting</span> مالک <span dir="ltr">Journal</span> مالی است، نه تصمیم اجازهٔ برداشت.
- <span dir="ltr">Channel</span> فقط درخواست/نمایش را انجام می‌دهد.

این تفکیک به معنی الزام دو <span dir="ltr">Microservice</span> نیست. می‌تواند دو <span dir="ltr">Module</span> در یک <span dir="ltr">Deployable</span> باشد.

## 6. مثال کامل دوم: اعطای تسهیلات و واریز به سپرده

### <span dir="ltr">Trigger</span> و <span dir="ltr">Outcome</span>

- <span dir="ltr">Trigger:</span> قرارداد تسهیلات مصوب، امضاشده و آمادهٔ اعطا
- <span dir="ltr">Outcome:</span> تعهد <span dir="ltr">Lending</span> قطعی شود، وجه دقیقاً یک‌بار به سپرده واریز گردد و <span dir="ltr">Fact</span> مالی قابل ثبت باشد.

### زنجیرهٔ اولیه

| مرحله | <span dir="ltr">Candidate</span> | <span dir="ltr">Owner</span> اولیه |
|---|---|---|
| <span dir="ltr">Capability</span> | <span dir="ltr">Execute Credit Disbursement</span> | <span dir="ltr">Lending business</span> |
| <span dir="ltr">Related capability</span> | <span dir="ltr">Credit Customer Funds</span> | <span dir="ltr">Deposits</span> |
| <span dir="ltr">Domains</span> | <span dir="ltr">Lending</span>، <span dir="ltr">Deposits</span>، <span dir="ltr">Accounting</span> | هرکدام مدل خودش را دارد |
| <span dir="ltr">Context</span> | <span dir="ltr">Loan Servicing</span> / <span dir="ltr">Deposit Account</span> / <span dir="ltr">Financial Accounting</span> | معانی <span dir="ltr">Amount/Balance/Completion</span> متفاوت‌اند |
| <span dir="ltr">Use case</span> | <span dir="ltr">DisburseLoan</span> | <span dir="ltr">Lending</span> |
| <span dir="ltr">Outbound command</span> | <span dir="ltr">CreditDeposit</span> | <span dir="ltr">Deposits</span> تصمیم به پذیرش/رد اثر روی حساب را دارد |
| <span dir="ltr">Business result</span> | <span dir="ltr">Deposit credit reference</span> | نتیجهٔ قابل‌همبستگی |
| <span dir="ltr">Events</span> | <span dir="ltr">LoanDisbursementStarted</span>، <span dir="ltr">DepositCredited</span>، <span dir="ltr">LoanDisbursed</span> | هر <span dir="ltr">Fact</span> توسط <span dir="ltr">Owner</span> خودش |
| <span dir="ltr">Accounting input</span> | <span dir="ltr">Business fact/Accounting fact candidate</span> | نحوهٔ دقیق در <span dir="ltr">Week 13</span> تصمیم می‌شود |

این جدول هنوز <span dir="ltr">Saga</span>، <span dir="ltr">Kafka</span> یا تراکنش توزیع‌شده را انتخاب نمی‌کند. <span dir="ltr">Week 01</span> فقط <span dir="ltr">Intent</span>، <span dir="ltr">Fact</span> و <span dir="ltr">Ownership</span> را از هم جدا می‌کند.

## <span dir="ltr">7. Contract Card</span> قبل از <span dir="ltr">OpenAPI/AsyncAPI</span>

قبل از نوشتن <span dir="ltr">YAML</span> این کارت را کامل کن:


</div>

<div dir="ltr" align="left">

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

</div>

<div dir="rtl" align="right">


این کارت جلوی دو خطا را می‌گیرد: <span dir="ltr">Contract</span> بزرگ بر اساس <span dir="ltr">Entity</span> داخلی و <span dir="ltr">Event</span> مبهمی که <span dir="ltr">Consumer</span> را مجبور به <span dir="ltr">Query</span> همگام می‌کند.

## <span dir="ltr">8. Command</span>، <span dir="ltr">Query</span>، <span dir="ltr">Result</span> و <span dir="ltr">Event</span>

| نوع | زمان دستوری | می‌تواند رد شود؟ | <span dir="ltr">Owner</span> نام‌گذاری | نمونه |
|---|---|---:|---|---|
| <span dir="ltr">Command</span> | حال/امر | بله | <span dir="ltr">Context</span> دریافت‌کننده | <span dir="ltr">`PlaceFundsHold`</span> |
| <span dir="ltr">Query</span> | درخواست مشاهده | ممکن است <span dir="ltr">Not Found</span> | <span dir="ltr">Owner</span> داده | <span dir="ltr">`GetAvailableBalance`</span> |
| <span dir="ltr">Result</span> | پاسخ به درخواست | نتیجهٔ اجرا | <span dir="ltr">Context</span> اجراکننده | <span dir="ltr">`HoldAccepted`</span> <span dir="ltr">result</span> |
| <span dir="ltr">Event</span> | گذشته | <span dir="ltr">Fact</span> رخ داده | <span dir="ltr">Context</span> تولیدکننده | <span dir="ltr">`FundsHeld`</span> |

<span dir="ltr">Event</span> با نام <span dir="ltr">`ProcessLoan`</span> یا <span dir="ltr">`DoAccounting`</span> نه <span dir="ltr">Fact</span> روشن دارد، نه معلوم می‌کند چه چیزی کامل شده است.

## 9. نگاشت یک‌به‌یک ممنوع

این برابری‌ها معمولاً غلط‌اند:


</div>

<div dir="ltr" align="left">

```text
1 Capability = 1 Bounded Context
1 Bounded Context = 1 Module
1 Module = 1 Microservice
1 Use Case = 1 REST endpoint
1 Table = 1 Aggregate
1 Event = 1 Topic
```

</div>

<div dir="rtl" align="right">


هر نگاشت باید <span dir="ltr">Forces</span> داشته باشد. یک <span dir="ltr">Capability</span> مانند <span dir="ltr">Execute Payments</span> ممکن است <span dir="ltr">Context</span>های <span dir="ltr">Payment Order</span>، <span dir="ltr">Fraud Control</span> و <span dir="ltr">Settlement</span> را درگیر کند. یک <span dir="ltr">Context</span> ممکن است فعلاً چند <span dir="ltr">Module</span> داشته باشد یا برعکس، یک <span dir="ltr">Module</span> آموزشی نمایندهٔ یک <span dir="ltr">Hypothesis Context</span> باشد.

## 10. تست سازگاری زنجیره

پس از ساخت زنجیره، این هشت کنترل را انجام بده:

1. آیا نام <span dir="ltr">Capability Outcome</span> محور است؟
2. آیا <span dir="ltr">Domain</span> به دانش مسئله اشاره دارد یا نام تیم؟
3. آیا <span dir="ltr">Context</span> مرز زبان و <span dir="ltr">Rule</span> دارد؟
4. آیا <span dir="ltr">Module</span> مسئولیت منسجم دارد؟
5. آیا <span dir="ltr">Use Case</span> فقط یک قصد اصلی دارد؟
6. آیا <span dir="ltr">Command</span> توسط <span dir="ltr">Owner</span> درست دریافت می‌شود؟
7. آیا <span dir="ltr">Event</span> واقعیت گذشته و مالک روشن دارد؟
8. آیا می‌توان <span dir="ltr">Contract</span> را به <span dir="ltr">Outcome</span> اول برگرداند؟

اگر یک ردیف حذف شود و هیچ‌چیز تغییر نکند، احتمالاً تزئینی است. اگر بین دو ردیف چند تصمیم پنهان باشد، زنجیره ناقص است.

## <span dir="ltr">11. Anti-pattern</span>های <span dir="ltr">Traceability</span>

### <span dir="ltr">Database-first chain</span>


</div>

<div dir="ltr" align="left">

```text
LOAN table → LoanService → CRUD API
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Capability</span>، <span dir="ltr">Rule</span>، <span dir="ltr">Owner</span> و <span dir="ltr">Use Case</span> حذف شده‌اند. <span dir="ltr">Table</span> فقط شاهد وضع موجود است.

### <span dir="ltr">Organization-first chain</span>


</div>

<div dir="ltr" align="left">

```text
ادارهٔ چک → Check microservice
```

</div>

<div dir="rtl" align="right">


ساختار سازمان دلیل کافی برای <span dir="ltr">Boundary</span> یا <span dir="ltr">Deployment</span> نیست.

### <span dir="ltr">Vendor-first chain</span>


</div>

<div dir="ltr" align="left">

```text
BIAN Current Account Service Domain → CurrentAccount microservice
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Reference model</span> به <span dir="ltr">Blueprint</span> محلی تبدیل شده است.

### <span dir="ltr">Channel-owned business rule</span>


</div>

<div dir="ltr" align="left">

```text
Mobile app → calculate available balance
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Channel Rule</span> دامینی را تصاحب کرده و <span dir="ltr">Contract</span> به رفتار داخلی نشت کرده است.

## 12. تمرین هدایت‌شده

برای <span dir="ltr">`ReleaseFundsHold`</span> سه سؤال پاسخ بده:

1. آیا <span dir="ltr">Actor</span> مجاز است مستقیماً <span dir="ltr">Deposits</span> را صدا بزند یا <span dir="ltr">Legal Orders</span> باید ابتدا اعتبار <span dir="ltr">Release</span> را تأیید کند؟ این تصمیم هنوز <span dir="ltr">`OPEN`</span> است.
2. <span dir="ltr">Event</span> نهایی <span dir="ltr">`HoldReleaseRequested`</span> است یا <span dir="ltr">`FundsHoldReleased`</span>؟ اولی <span dir="ltr">Fact</span> درخواست، دومی <span dir="ltr">Fact</span> اثر موفق است؛ هر دو ممکن‌اند ولی <span dir="ltr">Owner</span> متفاوت دارند.
3. آیا <span dir="ltr">Release</span> یک <span dir="ltr">API</span> همگام است یا <span dir="ltr">Event</span>؟ هنوز از روی <span dir="ltr">Capability</span> نمی‌توان <span dir="ltr">Transport</span> را تعیین کرد.

تمرین نشان می‌دهد <span dir="ltr">Traceability</span> پاسخ همه‌چیز را از پیش نمی‌دهد؛ محل تصمیم و <span dir="ltr">Unknown</span> را آشکار می‌کند.

## 13. تمرین مستقل و <span dir="ltr">Rubric</span>

[<span dir="ltr">Day 03 Exercise</span>](../exercises/day-03-traceability-chain.md) را انجام بده و از [<span dir="ltr">Template</span>](../artifacts/traceability-chain-template.md) استفاده کن.

| معیار | امتیاز |
|---|---:|
| <span dir="ltr">Trigger/Outcome</span> و <span dir="ltr">Capability</span> درست | ۲ |
| <span dir="ltr">Context/Owner</span> قابل‌دفاع | ۲ |
| <span dir="ltr">Use Case</span> و <span dir="ltr">Contract</span> بدون پرش | ۲ |
| تمایز <span dir="ltr">Command/Query/Event</span> | ۲ |
| <span dir="ltr">Unknown</span> و <span dir="ltr">Reverse trace</span> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. وجود یک <span dir="ltr">Service Candidate</span> بدون <span dir="ltr">Capability</span> یا <span dir="ltr">Owner</span>، <span dir="ltr">Critical Error</span> است.

## 14. آزمون خروج

درس را ببند و [<span dir="ltr">Exit Ticket</span>](../quizzes/day-03-exit-ticket.md) را پاسخ بده. فردا کیفیت <span dir="ltr">Boundary</span>های این زنجیره را با چهار نیروی طراحی نقد می‌کنیم.


</div>
