<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 03</bdi> — از <bdi dir="ltr">System</bdi> تا <bdi dir="ltr">Contract</bdi>؛ ساخت <bdi dir="ltr">Traceability Chain</bdi>

- <bdi dir="ltr">Day budget: 50 minutes</bdi> — <bdi dir="ltr">24 lesson</bdi> + <bdi dir="ltr">21 exercise</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output:</bdi> دو زنجیرهٔ قابل‌ردیابی برای مسدودی قضایی و اعطای تسهیلات
- <bdi dir="ltr">Main skill:</bdi> رفت‌وبرگشت از <bdi dir="ltr">Outcome</bdi> کسب‌وکاری تا <bdi dir="ltr">API/Event</bdi> بدون پرش مفهومی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. زنجیرهٔ <bdi dir="ltr">`Capability → Domain → Bounded Context → Module/Service Candidate → Use Case → Contract`</bdi> را مرحله‌به‌مرحله بسازی.
2. برای هر گام سؤال، <bdi dir="ltr">Evidence</bdi> و <bdi dir="ltr">Owner</bdi> مناسب ثبت کنی.
3. تشخیص بدهی کجا از نام جدول یا سامانه به <bdi dir="ltr">Service</bdi> پریده‌ای.
4. <bdi dir="ltr">Command</bdi>، <bdi dir="ltr">Query</bdi>، <bdi dir="ltr">Result</bdi> و <bdi dir="ltr">Event</bdi> را در سطح مفهومی از هم جدا کنی.
5. یک <bdi dir="ltr">Contract Candidate</bdi> را به <bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Outcome</bdi> اولیه بازگردانی و توجیه کنی.

## <bdi dir="ltr">2. Traceability</bdi> چرا معماری است؟

معماری فقط مجموعه‌ای از <bdi dir="ltr">Box</bdi> و <bdi dir="ltr">Arrow</bdi> نیست. هر <bdi dir="ltr">Box</bdi> و <bdi dir="ltr">Contract</bdi> باید بتواند به یک مسئله و تصمیم کسب‌وکاری برگردد. اگر برای یک <bdi dir="ltr">API</bdi> نتوانیم پاسخ دهیم «کدام <bdi dir="ltr">Use Case</bdi>، در کدام مدل، برای کدام <bdi dir="ltr">Capability</bdi> و تحت مالکیت چه کسی؟»، احتمالاً <bdi dir="ltr">Contract</bdi> از روی پیاده‌سازی موجود طراحی شده است.

<bdi dir="ltr">Traceability</bdi> دو جهت دارد:


</div>

<div dir="ltr" align="left">

```text
Top-down:  Business outcome → capability → model → executable contract
Bottom-up: API/event/table → use case → owner → business justification
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Top-down</bdi> از ساخت <bdi dir="ltr">Service</bdi> بی‌مسئله جلوگیری می‌کند. <bdi dir="ltr">Bottom-up</bdi> برای ممیزی <bdi dir="ltr">Legacy</bdi> و حذف <bdi dir="ltr">Contract</bdi>های بی‌مالک لازم است.

## 3. زنجیرهٔ مرجع

### <bdi dir="ltr">3.1 Outcome/Driver</bdi>

قبل از <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Trigger</bdi> و <bdi dir="ltr">Outcome</bdi> را روشن کن.

نمونه: «حکم معتبر قضایی باید بدون تغییر ماندهٔ دفتری، امکان برداشت مبلغ مشخص را متوقف کند و نتیجه قابل‌ممیزی باشد.»

### <bdi dir="ltr">3.2 Capability</bdi>

بانک چه کاری باید بتواند انجام دهد؟

نمونه: <bdi dir="ltr">`اعمال و مدیریت محدودیت روی وجوه مشتری`</bdi>.

### <bdi dir="ltr">3.3 Domain/Subdomain</bdi>

دانش اصلی و قواعد مسئله کجاست؟ ممکن است حکم و <bdi dir="ltr">Hold</bdi> در دو <bdi dir="ltr">Subdomain</bdi> متفاوت باشند:

- <bdi dir="ltr">Legal/Compliance:</bdi> اعتبار، متن، مرجع و دامنهٔ حکم
- <bdi dir="ltr">Deposits:</bdi> اثر عملیاتی <bdi dir="ltr">Hold</bdi> بر <bdi dir="ltr">available balance</bdi> و برداشت

### <bdi dir="ltr">3.4 Bounded Context</bdi>

در کدام مرز مدل، واژه‌ها و قواعد سازگارند؟ نام <bdi dir="ltr">Context</bdi> یک <bdi dir="ltr">Hypothesis</bdi> است و باید <bdi dir="ltr">Owner</bdi>، اصطلاحات و قواعد کلیدی داشته باشد.

### <bdi dir="ltr">3.5 Module/Service Candidate</bdi>

مسئولیت در کد کجا محصور می‌شود؟ در <bdi dir="ltr">Week 01</bdi> پیش‌فرض <bdi dir="ltr">`Module`</bdi> است. <bdi dir="ltr">Service Candidate</bdi> فقط نامزدی برای بررسی بعدی است، نه تصمیم استقرار.

### <bdi dir="ltr">3.6 Use Case</bdi>

یک قصد مشخص کسب‌وکاری که <bdi dir="ltr">Actor</bdi> یا سیستم همکار آغاز می‌کند:

- <bdi dir="ltr">RegisterLegalOrder</bdi>
- <bdi dir="ltr">PlaceFundsHold</bdi>
- <bdi dir="ltr">ReleaseFundsHold</bdi>
- <bdi dir="ltr">GetHoldStatus</bdi>

### <bdi dir="ltr">3.7 Command/Query</bdi>

- <bdi dir="ltr">Command</bdi> قصد تغییر وضعیت دارد و ممکن است رد شود.
- <bdi dir="ltr">Query</bdi> اطلاعات می‌خواهد و نباید اثر کسب‌وکاری پنهان داشته باشد.

<bdi dir="ltr">Command</bdi> برابر <bdi dir="ltr">Event</bdi> نیست. <bdi dir="ltr">`PlaceFundsHold`</bdi> درخواست انجام کار است؛ <bdi dir="ltr">`FundsHeld`</bdi> واقعیتی است که پس از موفقیت رخ داده است.

### <bdi dir="ltr">3.8 API/Event</bdi>

<bdi dir="ltr">Contract</bdi> بیرونی باید <bdi dir="ltr">Intent</bdi> یا <bdi dir="ltr">Fact</bdi> را با زبان مرز منتشر کند. نوع <bdi dir="ltr">Transport</bdi> هنوز تصمیم ثانویه است. می‌توان ابتدا <bdi dir="ltr">Contract Card</bdi> ساخت و بعد در <bdi dir="ltr">Week 05/09</bdi> دربارهٔ <bdi dir="ltr">REST</bdi> یا <bdi dir="ltr">Messaging</bdi> تصمیم گرفت.

## 4. کارت ردیابی هر گام

برای هر ردیف زنجیره این ستون‌ها را ثبت کن:

| فیلد | سؤال |
|---|---|
| <bdi dir="ltr">Element</bdi> | نام دقیق چیست؟ |
| <bdi dir="ltr">Type</bdi> | <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Context</bdi>، <bdi dir="ltr">Use Case</bdi>، <bdi dir="ltr">Command</bdi>، <bdi dir="ltr">Event</bdi> و...؟ |
| <bdi dir="ltr">Owner</bdi> | چه نقش/<bdi dir="ltr">Context</bdi>ی حق تغییر تصمیم را دارد؟ |
| <bdi dir="ltr">Input evidence</bdi> | چه سند، <bdi dir="ltr">Rule</bdi> یا نیاز واقعی این مورد را توجیه می‌کند؟ |
| <bdi dir="ltr">Output/Outcome</bdi> | چه چیزی پس از آن قابل مشاهده است؟ |
| <bdi dir="ltr">Boundary rule</bdi> | این عنصر چه چیزی را عمداً پنهان یا رد می‌کند؟ |
| <bdi dir="ltr">Open question</bdi> | کدام فرض هنوز اثبات نشده است؟ |

## 5. مثال کامل اول: مسدودی قضایی سپرده

### <bdi dir="ltr">Trigger</bdi> و <bdi dir="ltr">Outcome</bdi>

- <bdi dir="ltr">Trigger:</bdi> دریافت حکم قضایی معتبر با شناسه و دامنهٔ مشخص
- <bdi dir="ltr">Outcome:</bdi> مبلغ مشمول <bdi dir="ltr">Hold</bdi> قابل برداشت نباشد؛ اصل مانده و <bdi dir="ltr">Journal</bdi> مستقل باقی بمانند؛ وضعیت قابل‌پیگیری باشد.

### زنجیره

| مرحله | <bdi dir="ltr">Candidate</bdi> | دلیل |
|---|---|---|
| <bdi dir="ltr">Capability</bdi> | <bdi dir="ltr">Manage Legal Restrictions on Funds</bdi> | توانایی پایدار، مستقل از نرم‌افزار |
| <bdi dir="ltr">Domain</bdi> | <bdi dir="ltr">Compliance/Legal</bdi> + <bdi dir="ltr">Deposits</bdi> | اعتبار حکم و اعمال <bdi dir="ltr">Hold</bdi> دو دانش متفاوت‌اند |
| <bdi dir="ltr">Subdomain</bdi> | <bdi dir="ltr">Legal Order Management</bdi> / <bdi dir="ltr">Deposit Availability Control</bdi> | قواعد و <bdi dir="ltr">Lifecycle</bdi> مستقل دارند |
| <bdi dir="ltr">Bounded Context</bdi> | <bdi dir="ltr">Legal Orders</bdi> / <bdi dir="ltr">Deposits</bdi> | واژهٔ <bdi dir="ltr">Order</bdi> در یکی سند معتبر و در دیگری <bdi dir="ltr">Reference</bdi> است |
| <bdi dir="ltr">Module</bdi> | <bdi dir="ltr">`legalorders`</bdi> / <bdi dir="ltr">`deposits`</bdi> | مسئولیت و مدل داخلی جدا |
| <bdi dir="ltr">Use Case</bdi> | <bdi dir="ltr">RegisterLegalOrder</bdi> / <bdi dir="ltr">PlaceFundsHold</bdi> | دو قصد با دو <bdi dir="ltr">Owner</bdi> تصمیم |
| <bdi dir="ltr">Command</bdi> | <bdi dir="ltr">`PlaceFundsHold(orderRef, accountId, amount)`</bdi> | درخواست تغییر <bdi dir="ltr">available funds</bdi> |
| <bdi dir="ltr">Result</bdi> | <bdi dir="ltr">Accepted</bdi> / <bdi dir="ltr">Rejected with reason</bdi> | <bdi dir="ltr">Command</bdi> ممکن است رد شود |
| <bdi dir="ltr">Event</bdi> | <bdi dir="ltr">`FundsHeld`</bdi> | <bdi dir="ltr">Fact</bdi> پس از تغییر موفق |
| <bdi dir="ltr">Query</bdi> | <bdi dir="ltr">`GetHoldStatus(holdId)`</bdi> | مشاهدهٔ وضعیت بدون تغییر |

### مالکیت

- <bdi dir="ltr">Legal Orders</bdi> مالک متن، اعتبار و <bdi dir="ltr">Lifecycle</bdi> حکم است.
- <bdi dir="ltr">Deposits</bdi> مالک امکان اعمال <bdi dir="ltr">Hold</bdi>، مبلغ <bdi dir="ltr">Held</bdi> و <bdi dir="ltr">available balance</bdi> است.
- <bdi dir="ltr">Accounting</bdi> مالک <bdi dir="ltr">Journal</bdi> مالی است، نه تصمیم اجازهٔ برداشت.
- <bdi dir="ltr">Channel</bdi> فقط درخواست/نمایش را انجام می‌دهد.

این تفکیک به معنی الزام دو <bdi dir="ltr">Microservice</bdi> نیست. می‌تواند دو <bdi dir="ltr">Module</bdi> در یک <bdi dir="ltr">Deployable</bdi> باشد.

## 6. مثال کامل دوم: اعطای تسهیلات و واریز به سپرده

### <bdi dir="ltr">Trigger</bdi> و <bdi dir="ltr">Outcome</bdi>

- <bdi dir="ltr">Trigger:</bdi> قرارداد تسهیلات مصوب، امضاشده و آمادهٔ اعطا
- <bdi dir="ltr">Outcome:</bdi> تعهد <bdi dir="ltr">Lending</bdi> قطعی شود، وجه دقیقاً یک‌بار به سپرده واریز گردد و <bdi dir="ltr">Fact</bdi> مالی قابل ثبت باشد.

### زنجیرهٔ اولیه

| مرحله | <bdi dir="ltr">Candidate</bdi> | <bdi dir="ltr">Owner</bdi> اولیه |
|---|---|---|
| <bdi dir="ltr">Capability</bdi> | <bdi dir="ltr">Execute Credit Disbursement</bdi> | <bdi dir="ltr">Lending business</bdi> |
| <bdi dir="ltr">Related capability</bdi> | <bdi dir="ltr">Credit Customer Funds</bdi> | <bdi dir="ltr">Deposits</bdi> |
| <bdi dir="ltr">Domains</bdi> | <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Accounting</bdi> | هرکدام مدل خودش را دارد |
| <bdi dir="ltr">Context</bdi> | <bdi dir="ltr">Loan Servicing</bdi> / <bdi dir="ltr">Deposit Account</bdi> / <bdi dir="ltr">Financial Accounting</bdi> | معانی <bdi dir="ltr">Amount/Balance/Completion</bdi> متفاوت‌اند |
| <bdi dir="ltr">Use case</bdi> | <bdi dir="ltr">DisburseLoan</bdi> | <bdi dir="ltr">Lending</bdi> |
| <bdi dir="ltr">Outbound command</bdi> | <bdi dir="ltr">CreditDeposit</bdi> | <bdi dir="ltr">Deposits</bdi> تصمیم به پذیرش/رد اثر روی حساب را دارد |
| <bdi dir="ltr">Business result</bdi> | <bdi dir="ltr">Deposit credit reference</bdi> | نتیجهٔ قابل‌همبستگی |
| <bdi dir="ltr">Events</bdi> | <bdi dir="ltr">LoanDisbursementStarted</bdi>، <bdi dir="ltr">DepositCredited</bdi>، <bdi dir="ltr">LoanDisbursed</bdi> | هر <bdi dir="ltr">Fact</bdi> توسط <bdi dir="ltr">Owner</bdi> خودش |
| <bdi dir="ltr">Accounting input</bdi> | <bdi dir="ltr">Business fact/Accounting fact candidate</bdi> | نحوهٔ دقیق در <bdi dir="ltr">Week 13</bdi> تصمیم می‌شود |

این جدول هنوز <bdi dir="ltr">Saga</bdi>، <bdi dir="ltr">Kafka</bdi> یا تراکنش توزیع‌شده را انتخاب نمی‌کند. <bdi dir="ltr">Week 01</bdi> فقط <bdi dir="ltr">Intent</bdi>، <bdi dir="ltr">Fact</bdi> و <bdi dir="ltr">Ownership</bdi> را از هم جدا می‌کند.

## <bdi dir="ltr">7. Contract Card</bdi> قبل از <bdi dir="ltr">OpenAPI/AsyncAPI</bdi>

قبل از نوشتن <bdi dir="ltr">YAML</bdi> این کارت را کامل کن:


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


این کارت جلوی دو خطا را می‌گیرد: <bdi dir="ltr">Contract</bdi> بزرگ بر اساس <bdi dir="ltr">Entity</bdi> داخلی و <bdi dir="ltr">Event</bdi> مبهمی که <bdi dir="ltr">Consumer</bdi> را مجبور به <bdi dir="ltr">Query</bdi> همگام می‌کند.

## <bdi dir="ltr">8. Command</bdi>، <bdi dir="ltr">Query</bdi>، <bdi dir="ltr">Result</bdi> و <bdi dir="ltr">Event</bdi>

| نوع | زمان دستوری | می‌تواند رد شود؟ | <bdi dir="ltr">Owner</bdi> نام‌گذاری | نمونه |
|---|---|---:|---|---|
| <bdi dir="ltr">Command</bdi> | حال/امر | بله | <bdi dir="ltr">Context</bdi> دریافت‌کننده | <bdi dir="ltr">`PlaceFundsHold`</bdi> |
| <bdi dir="ltr">Query</bdi> | درخواست مشاهده | ممکن است <bdi dir="ltr">Not Found</bdi> | <bdi dir="ltr">Owner</bdi> داده | <bdi dir="ltr">`GetAvailableBalance`</bdi> |
| <bdi dir="ltr">Result</bdi> | پاسخ به درخواست | نتیجهٔ اجرا | <bdi dir="ltr">Context</bdi> اجراکننده | <bdi dir="ltr">`HoldAccepted`</bdi> <bdi dir="ltr">result</bdi> |
| <bdi dir="ltr">Event</bdi> | گذشته | <bdi dir="ltr">Fact</bdi> رخ داده | <bdi dir="ltr">Context</bdi> تولیدکننده | <bdi dir="ltr">`FundsHeld`</bdi> |

<bdi dir="ltr">Event</bdi> با نام <bdi dir="ltr">`ProcessLoan`</bdi> یا <bdi dir="ltr">`DoAccounting`</bdi> نه <bdi dir="ltr">Fact</bdi> روشن دارد، نه معلوم می‌کند چه چیزی کامل شده است.

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


هر نگاشت باید <bdi dir="ltr">Forces</bdi> داشته باشد. یک <bdi dir="ltr">Capability</bdi> مانند <bdi dir="ltr">Execute Payments</bdi> ممکن است <bdi dir="ltr">Context</bdi>های <bdi dir="ltr">Payment Order</bdi>، <bdi dir="ltr">Fraud Control</bdi> و <bdi dir="ltr">Settlement</bdi> را درگیر کند. یک <bdi dir="ltr">Context</bdi> ممکن است فعلاً چند <bdi dir="ltr">Module</bdi> داشته باشد یا برعکس، یک <bdi dir="ltr">Module</bdi> آموزشی نمایندهٔ یک <bdi dir="ltr">Hypothesis Context</bdi> باشد.

## 10. تست سازگاری زنجیره

پس از ساخت زنجیره، این هشت کنترل را انجام بده:

1. آیا نام <bdi dir="ltr">Capability Outcome</bdi> محور است؟
2. آیا <bdi dir="ltr">Domain</bdi> به دانش مسئله اشاره دارد یا نام تیم؟
3. آیا <bdi dir="ltr">Context</bdi> مرز زبان و <bdi dir="ltr">Rule</bdi> دارد؟
4. آیا <bdi dir="ltr">Module</bdi> مسئولیت منسجم دارد؟
5. آیا <bdi dir="ltr">Use Case</bdi> فقط یک قصد اصلی دارد؟
6. آیا <bdi dir="ltr">Command</bdi> توسط <bdi dir="ltr">Owner</bdi> درست دریافت می‌شود؟
7. آیا <bdi dir="ltr">Event</bdi> واقعیت گذشته و مالک روشن دارد؟
8. آیا می‌توان <bdi dir="ltr">Contract</bdi> را به <bdi dir="ltr">Outcome</bdi> اول برگرداند؟

اگر یک ردیف حذف شود و هیچ‌چیز تغییر نکند، احتمالاً تزئینی است. اگر بین دو ردیف چند تصمیم پنهان باشد، زنجیره ناقص است.

## <bdi dir="ltr">11. Anti-pattern</bdi>های <bdi dir="ltr">Traceability</bdi>

### <bdi dir="ltr">Database-first chain</bdi>


</div>

<div dir="ltr" align="left">

```text
LOAN table → LoanService → CRUD API
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Rule</bdi>، <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">Use Case</bdi> حذف شده‌اند. <bdi dir="ltr">Table</bdi> فقط شاهد وضع موجود است.

### <bdi dir="ltr">Organization-first chain</bdi>


</div>

<div dir="ltr" align="left">

```text
ادارهٔ چک → Check microservice
```

</div>

<div dir="rtl" align="right">


ساختار سازمان دلیل کافی برای <bdi dir="ltr">Boundary</bdi> یا <bdi dir="ltr">Deployment</bdi> نیست.

### <bdi dir="ltr">Vendor-first chain</bdi>


</div>

<div dir="ltr" align="left">

```text
BIAN Current Account Service Domain → CurrentAccount microservice
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Reference model</bdi> به <bdi dir="ltr">Blueprint</bdi> محلی تبدیل شده است.

### <bdi dir="ltr">Channel-owned business rule</bdi>


</div>

<div dir="ltr" align="left">

```text
Mobile app → calculate available balance
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Channel Rule</bdi> دامینی را تصاحب کرده و <bdi dir="ltr">Contract</bdi> به رفتار داخلی نشت کرده است.

## 12. تمرین هدایت‌شده

برای <bdi dir="ltr">`ReleaseFundsHold`</bdi> سه سؤال پاسخ بده:

1. آیا <bdi dir="ltr">Actor</bdi> مجاز است مستقیماً <bdi dir="ltr">Deposits</bdi> را صدا بزند یا <bdi dir="ltr">Legal Orders</bdi> باید ابتدا اعتبار <bdi dir="ltr">Release</bdi> را تأیید کند؟ این تصمیم هنوز <bdi dir="ltr">`OPEN`</bdi> است.
2. <bdi dir="ltr">Event</bdi> نهایی <bdi dir="ltr">`HoldReleaseRequested`</bdi> است یا <bdi dir="ltr">`FundsHoldReleased`</bdi>؟ اولی <bdi dir="ltr">Fact</bdi> درخواست، دومی <bdi dir="ltr">Fact</bdi> اثر موفق است؛ هر دو ممکن‌اند ولی <bdi dir="ltr">Owner</bdi> متفاوت دارند.
3. آیا <bdi dir="ltr">Release</bdi> یک <bdi dir="ltr">API</bdi> همگام است یا <bdi dir="ltr">Event</bdi>؟ هنوز از روی <bdi dir="ltr">Capability</bdi> نمی‌توان <bdi dir="ltr">Transport</bdi> را تعیین کرد.

تمرین نشان می‌دهد <bdi dir="ltr">Traceability</bdi> پاسخ همه‌چیز را از پیش نمی‌دهد؛ محل تصمیم و <bdi dir="ltr">Unknown</bdi> را آشکار می‌کند.

## 13. تمرین مستقل و <bdi dir="ltr">Rubric</bdi>

[<bdi dir="ltr">Day 03 Exercise</bdi>](../exercises/day-03-traceability-chain.md) را انجام بده و از [<bdi dir="ltr">Template</bdi>](../artifacts/traceability-chain-template.md) استفاده کن.

| معیار | امتیاز |
|---|---:|
| <bdi dir="ltr">Trigger/Outcome</bdi> و <bdi dir="ltr">Capability</bdi> درست | ۲ |
| <bdi dir="ltr">Context/Owner</bdi> قابل‌دفاع | ۲ |
| <bdi dir="ltr">Use Case</bdi> و <bdi dir="ltr">Contract</bdi> بدون پرش | ۲ |
| تمایز <bdi dir="ltr">Command/Query/Event</bdi> | ۲ |
| <bdi dir="ltr">Unknown</bdi> و <bdi dir="ltr">Reverse trace</bdi> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. وجود یک <bdi dir="ltr">Service Candidate</bdi> بدون <bdi dir="ltr">Capability</bdi> یا <bdi dir="ltr">Owner</bdi>، <bdi dir="ltr">Critical Error</bdi> است.

## 14. آزمون خروج

درس را ببند و [<bdi dir="ltr">Exit Ticket</bdi>](../quizzes/day-03-exit-ticket.md) را پاسخ بده. فردا کیفیت <bdi dir="ltr">Boundary</bdi>های این زنجیره را با چهار نیروی طراحی نقد می‌کنیم.


</div>
