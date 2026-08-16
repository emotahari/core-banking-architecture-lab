<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 04</span> — <span dir="ltr">Coupling</span>، <span dir="ltr">Cohesion</span>، <span dir="ltr">Encapsulation</span> و <span dir="ltr">Information Hiding</span>

- <span dir="ltr">Day budget: 55 minutes</span> — <span dir="ltr">27 lesson</span> + <span dir="ltr">23 exercise</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output: Coupling Review</span> و <span dir="ltr">Boundary redesign</span>
- <span dir="ltr">Banking case:</span> اعطای تسهیلات و واریز به سپرده

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Coupling</span> و <span dir="ltr">Cohesion</span> را با مثال رفتاری، نه فقط تعریف کتابی، تحلیل کنی.
2. <span dir="ltr">Encapsulation</span> را از <span dir="ltr">Information Hiding</span> جدا کنی.
3. پنج نوع <span dir="ltr">Coupling</span> مهم در سامانهٔ بانکی را پیدا کنی.
4. تشخیص بدهی یک <span dir="ltr">API</span> ظاهراً مستقل چگونه مدل، زمان‌بندی یا دادهٔ داخلی را نشت می‌دهد.
5. یک طراحی کاپل‌شده را بدون پریدن به <span dir="ltr">Microservice</span> بازطراحی کنی.

## 2. چرا این چهار نیرو مهم‌اند؟

<span dir="ltr">Capability</span> و <span dir="ltr">Traceability</span> می‌گویند چرا یک مسئولیت وجود دارد. چهار نیروی امروز می‌گویند **مسئولیت‌ها چگونه کنار هم قرار گیرند تا تغییر محلی بماند و دانش داخلی نشت نکند**.

مرز خوب معمولاً این ویژگی‌ها را دارد:

- اجزای درون مرز به یک دلیل کسب‌وکاری نزدیک تغییر می‌کنند: <span dir="ltr">Cohesion</span> بالا.
- تغییر داخل مرز کمترین اجبار را به بیرون تحمیل می‌کند: <span dir="ltr">Coupling</span> کنترل‌شده.
- <span dir="ltr">Invariant</span> و <span dir="ltr">State</span> فقط از مسیر رفتار مجاز تغییر می‌کنند: <span dir="ltr">Encapsulation.</span>
- تصمیم‌ها و ساختارهایی که ممکن است عوض شوند پشت <span dir="ltr">Contract</span> پایدار پنهان‌اند: <span dir="ltr">Information Hiding.</span>

این‌ها عددهای مطلق یا هدف‌های جداگانه نیستند. گاهی افزودن یک <span dir="ltr">Contract</span>، <span dir="ltr">Coupling</span> فنی را بیشتر اما <span dir="ltr">Coupling</span> تغییر را کمتر می‌کند.

## <span dir="ltr">3. Coupling</span>؛ وابستگی فقط <span dir="ltr">Import</span> نیست

دو جزء وقتی <span dir="ltr">Coupled</span> هستند که تغییر یا رفتار یکی بر دیگری اثر بگذارد. نبود <span dir="ltr">Dependency</span> کامپایل به معنی نبود <span dir="ltr">Coupling</span> نیست.

### <span dir="ltr">3.1 Structural coupling</span>

یک <span dir="ltr">Module Class</span> یا <span dir="ltr">Package</span> داخلی <span dir="ltr">Module</span> دیگر را <span dir="ltr">Import</span> می‌کند. این نوع در <span dir="ltr">Code Review</span> دیده می‌شود.


</div>

<div dir="ltr" align="left">

```java
depositRepository.updateBalance(...); // از داخل Lending
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Lending</span> اکنون ساختار و <span dir="ltr">Lifecycle</span> دادهٔ <span dir="ltr">Deposits</span> را می‌شناسد.

### <span dir="ltr">3.2 Data coupling</span>

دو جزء <span dir="ltr">Schema</span>، <span dir="ltr">Entity</span> یا <span dir="ltr">Payload</span> بسیار بزرگ مشترک دارند. اگر <span dir="ltr">`CustomerEntity`</span> مشترک تغییر کند، چند <span dir="ltr">Context</span> هم‌زمان <span dir="ltr">Release</span> می‌شوند.

راه‌حل همیشه حذف دادهٔ مشترک نیست؛ <span dir="ltr">Contract</span> باید فقط <span dir="ltr">Fact</span> لازم را با معنای روشن حمل کند، نه <span dir="ltr">Object</span> داخلی را.

### <span dir="ltr">3.3 Behavioral coupling</span>

مصرف‌کننده به ترتیب یا <span dir="ltr">Side effect</span> داخلی <span dir="ltr">Provider</span> وابسته است. مثلاً <span dir="ltr">Channel</span> می‌داند برای انتقال وجه باید ابتدا <span dir="ltr">`validate`</span>، سپس <span dir="ltr">`reserve`</span> و سپس <span dir="ltr">`post`</span> را با ترتیب خاص صدا بزند. در واقع <span dir="ltr">Workflow</span> داخلی <span dir="ltr">Payments</span> به <span dir="ltr">Channel</span> نشت کرده است.

### <span dir="ltr">3.4 Temporal coupling</span>

اجزا باید هم‌زمان در دسترس یا با ترتیب زمانی ظریف اجرا شوند. پنج <span dir="ltr">Call</span> همگام زنجیره‌ای <span dir="ltr">Availability</span> را ضرب می‌کنند. <span dir="ltr">Event</span> هم <span dir="ltr">Temporal coupling</span> را خودکار حذف نمی‌کند؛ <span dir="ltr">Consumer</span> ممکن است به ترتیب پنهان <span dir="ltr">Event</span>ها وابسته باشد.

### <span dir="ltr">3.5 Change coupling</span>

دو جزء معمولاً به دلیل یک <span dir="ltr">Rule</span> با هم تغییر و <span dir="ltr">Release</span> می‌شوند. این مهم‌ترین <span dir="ltr">Evidence</span> برای بازبینی <span dir="ltr">Boundary</span> است. <span dir="ltr">Git history</span>، <span dir="ltr">Incident</span> و <span dir="ltr">Change request</span> از <span dir="ltr">Diagram</span> معتبرترند.

### <span dir="ltr">3.6 Operational coupling</span>

یک <span dir="ltr">Deployment</span>، دیتابیس، <span dir="ltr">Queue</span>، <span dir="ltr">Scaling profile</span> یا <span dir="ltr">Runbook</span> مشترک باعث می‌شود <span dir="ltr">Failure</span> یکی روی دیگری اثر بگذارد. این موضوع هنگام استخراج <span dir="ltr">Microservice</span> تعیین‌کننده است، نه در <span dir="ltr">Week 01.</span>

## <span dir="ltr">4. Cohesion</span>؛ چرا این مسئولیت‌ها کنار هم‌اند؟

<span dir="ltr">Cohesion</span> میزان ارتباط معنایی و تغییر مشترک اجزای داخل یک مرز است.

### <span dir="ltr">Cohesion</span> بالا

در <span dir="ltr">Deposits</span>، محاسبهٔ <span dir="ltr">available balance</span>، <span dir="ltr">Hold</span> و کنترل اجازهٔ برداشت حول <span dir="ltr">Invariant</span> «چه مقدار اکنون قابل برداشت است؟» نزدیک‌اند.

### <span dir="ltr">Cohesion</span> پایین

کلاس <span dir="ltr">`BankingService`</span> که افتتاح سپرده، تصویب تسهیلات، ثبت سند، ارسال پیامک و گزارش مدیریتی را انجام می‌دهد، فقط به این دلیل کنار هم است که «همه بانکی‌اند».

### آزمون یک جمله‌ای

مسئولیت <span dir="ltr">Module</span> را در یک جمله بنویس:

> این <span dir="ltr">Module</span> مسئول ... است و تنها <span dir="ltr">Authority</span> تغییر ... را دارد.

اگر جمله به چند «و همچنین» طولانی نیاز دارد یا <span dir="ltr">Owner</span>های متفاوت دارد، <span dir="ltr">Cohesion</span> مشکوک است.

## <span dir="ltr">5. Encapsulation</span>؛ کنترل <span dir="ltr">State</span> و <span dir="ltr">Invariant</span>

<span dir="ltr">Encapsulation</span> یعنی داده و رفتار مرتبط طوری کنار هم قرار گیرند که <span dir="ltr">State</span> فقط از مسیر <span dir="ltr">Operation</span>های معتبر تغییر کند.

نمونهٔ ضعیف:


</div>

<div dir="ltr" align="left">

```java
account.setAvailableBalance(account.getAvailableBalance().subtract(amount));
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Caller</span> باید بداند <span dir="ltr">available balance</span> چگونه محاسبه می‌شود، <span dir="ltr">Hold</span> چه اثری دارد و منفی‌شدن مجاز است یا نه.

نمونهٔ بهتر از نظر <span dir="ltr">Intent:</span>


</div>

<div dir="ltr" align="left">

```java
account.placeHold(holdId, amount, legalOrderReference);
```

</div>

<div dir="rtl" align="right">


این <span dir="ltr">Signature</span> هنوز طراحی نهایی نیست، اما <span dir="ltr">Invariant</span> را داخل مدل نگه می‌دارد. <span dir="ltr">Encapsulation</span> صرفاً <span dir="ltr">`private`</span> کردن <span dir="ltr">Field</span> نیست؛ اگر <span dir="ltr">Setter</span> عمومی همه‌چیز را تغییر دهد، <span dir="ltr">State</span> پنهان ولی <span dir="ltr">Rule</span> بی‌دفاع است.

## <span dir="ltr">6. Information Hiding</span>؛ پنهان‌کردن تصمیم متغیر

<span dir="ltr">Information Hiding</span> می‌پرسد چه تصمیمی احتمال تغییر دارد و چه کسانی نباید آن را بدانند.

نمونه‌ها:

- <span dir="ltr">Channel</span> نباید بداند <span dir="ltr">Deposits</span> مانده را از یک <span dir="ltr">Row</span>، <span dir="ltr">Ledger</span> یا <span dir="ltr">Projection</span> می‌خواند.
- <span dir="ltr">Lending</span> نباید بداند <span dir="ltr">Accounting</span> برای چه سرفصل و تفصیلی <span dir="ltr">Journal</span> می‌سازد.
- <span dir="ltr">Consumer</span> نباید به نام جدول یا ترتیب <span dir="ltr">Internal Step</span> وابسته شود.
- <span dir="ltr">Contract</span> نباید <span dir="ltr">Precision</span> دیتابیس را بدون دلیل به مدل کسب‌وکار تبدیل کند.

<span dir="ltr">Encapsulation</span> بیشتر دربارهٔ حفاظت از <span dir="ltr">State/Invariant</span> است؛ <span dir="ltr">Information Hiding</span> دربارهٔ حفاظت از تصمیم طراحی و جلوگیری از <span dir="ltr">Ripple change.</span> هم‌پوشانی دارند اما مساوی نیستند.

## 7. طراحی کاپل‌شدهٔ اعطا

فرض کن یک <span dir="ltr">`LoanDisbursementOrchestrator`</span> این کارها را انجام می‌دهد:


</div>

<div dir="ltr" align="left">

```text
1. SELECT loan row
2. UPDATE loan.status = DISBURSED
3. UPDATE deposit.balance = balance + amount
4. INSERT accounting.document_line twice
5. SEND notification
```

</div>

<div dir="rtl" align="right">


و برای این کار به سه <span dir="ltr">Schema</span> مشترک دسترسی مستقیم دارد.

### اشکال‌ها

| نشانه | نوع مشکل | پیامد |
|---|---|---|
| <span dir="ltr">Update</span> جدول <span dir="ltr">Deposits</span> از <span dir="ltr">Lending</span> | <span dir="ltr">Data/structural coupling</span> | <span dir="ltr">Rule</span> مانده دور زده می‌شود |
| وضعیت <span dir="ltr">Loan</span> قبل از نتیجهٔ واریز قطعی می‌شود | <span dir="ltr">Temporal/semantic coupling</span> | وضعیت کاذب |
| <span dir="ltr">Orchestrator</span> سرفصل‌ها را می‌شناسد | <span dir="ltr">Information leak</span> | تغییر <span dir="ltr">Accounting</span> نیازمند تغییر <span dir="ltr">Orchestrator</span> |
| <span dir="ltr">Notification</span> در همان <span dir="ltr">Method</span> | <span dir="ltr">Cohesion</span> پایین | <span dir="ltr">Failure</span> پیامک عملیات مالی را آلوده می‌کند |
| یک تراکنش <span dir="ltr">DB</span> برای سه <span dir="ltr">Owner</span> | <span dir="ltr">Ownership</span> مشترک مصنوعی | استقلال مدل از بین می‌رود |

## 8. بازطراحی مرحله‌ای، بدون انتخاب زودهنگام فناوری

### گام 1 — <span dir="ltr">Authority</span> را جدا کن

- <span dir="ltr">Lending</span> فقط وضعیت و <span dir="ltr">Rule</span> اعطا را تغییر دهد.
- <span dir="ltr">Deposits</span> فقط اثر <span dir="ltr">Credit</span> روی حساب و ماندهٔ عملیاتی را اعمال کند.
- <span dir="ltr">Accounting</span> فقط <span dir="ltr">Fact</span> مالی را به <span dir="ltr">Journal</span> تبدیل کند.

### گام 2 — <span dir="ltr">Contract</span> معنایی تعریف کن


</div>

<div dir="ltr" align="left">

```text
Lending intent: DisburseLoan
Deposits intent: CreditDeposit for a business transaction
Deposits fact: DepositCredited
Lending fact: LoanDisbursed
Accounting input: accepted business/accounting fact
```

</div>

<div dir="rtl" align="right">


### گام 3 — <span dir="ltr">Internal representation</span> را پنهان کن

هیچ <span dir="ltr">Contract</span>ی <span dir="ltr">`TB_LOAN_ROW`</span>، <span dir="ltr">`DEPOSIT_ENTITY`</span> یا لیست <span dir="ltr">Debit/Credit</span> داخلی را حمل نکند. فقط شناسه، مبلغ، معنا و <span dir="ltr">Metadata</span> لازم حمل شود.

### گام 4 — <span dir="ltr">Failure</span> را نام‌گذاری کن

اگر <span dir="ltr">Deposit Credit</span> رد شود، <span dir="ltr">Lending</span> نباید <span dir="ltr">`DISBURSED`</span> شود. اگر پاسخ گم شود، باید <span dir="ltr">Correlation/Idempotency</span> در هفته‌های بعد طراحی شود. امروز <span dir="ltr">Unknown</span> و <span dir="ltr">Expected outcome</span> ثبت می‌شود.

### گام 5 — <span dir="ltr">Deployment</span> را باز بگذار

سه مسئولیت می‌توانند فعلاً سه <span dir="ltr">Module</span> در یک <span dir="ltr">Modulith</span> باشند. جداسازی مدل الزاماً جداسازی شبکه‌ای نیست.

## <span dir="ltr">9. API</span> چگونه <span dir="ltr">Information leak</span> می‌دهد؟

وجود <span dir="ltr">HTTP</span> مرز را ایجاد نمی‌کند. این <span dir="ltr">API</span> ضعیف است:


</div>

<div dir="ltr" align="left">

```json
{
  "table": "TB_DEPOSIT",
  "operation": "UPDATE",
  "column": "AVAILABLE_BALANCE",
  "delta": 100000000
}
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Consumer</span> تصمیم داخلی <span dir="ltr">Provider</span> را کنترل می‌کند. <span dir="ltr">Contract</span> معنایی‌تر:


</div>

<div dir="ltr" align="left">

```json
{
  "businessTransactionId": "...",
  "accountId": "...",
  "money": { "amount": "100000000", "currency": "IRR" },
  "reason": "LOAN_DISBURSEMENT",
  "loanDisbursementId": "..."
}
```

</div>

<div dir="rtl" align="right">


حتی این <span dir="ltr">Contract</span> نیز نیازمند <span dir="ltr">Policy</span> امنیت، <span dir="ltr">Idempotency</span> و <span dir="ltr">Ownership</span> است؛ اما به‌جای <span dir="ltr">Update</span> عمومی، <span dir="ltr">Intent</span> را بیان می‌کند.

## <span dir="ltr">10. Event</span> چگونه <span dir="ltr">Coupling</span> می‌سازد؟

<span dir="ltr">Event-driven</span> بودن مترادف <span dir="ltr">Loose coupling</span> نیست. این موارد <span dir="ltr">Coupling</span> ایجاد می‌کنند:

- <span dir="ltr">Event</span> بزرگ با <span dir="ltr">Snapshot</span> همهٔ <span dir="ltr">Entity</span>ها
- نام مبهم و نیاز <span dir="ltr">Consumer</span> به تفسیر داخلی
- وابستگی به ترتیب چند <span dir="ltr">Topic</span> بدون <span dir="ltr">Key</span> روشن
- تغییر <span dir="ltr">Breaking</span> بدون <span dir="ltr">Versioning</span>
- <span dir="ltr">Consumer</span>ی که برای تکمیل <span dir="ltr">Event</span> باید پنج <span dir="ltr">Query</span> همگام بزند
- <span dir="ltr">Event</span>ی که در واقع <span dir="ltr">Command</span> پنهان است و <span dir="ltr">Consumer</span> خاص را هدف گرفته است

پس <span dir="ltr">Coupling</span> را از روی <span dir="ltr">Protocol</span> قضاوت نکن؛ از روی <span dir="ltr">Knowledge</span> و <span dir="ltr">Change impact</span> قضاوت کن.

## <span dir="ltr">11. Heuristic</span>های بازبینی <span dir="ltr">Boundary</span>

برای هر <span dir="ltr">Dependency</span> این پرسش‌ها را ثبت کن:

1. چه دانش داخلی‌ای عبور می‌کند؟
2. اگر <span dir="ltr">Rule Provider</span> تغییر کند، <span dir="ltr">Consumer</span> هم باید تغییر کند؟
3. چه کسی تصمیم نهایی را می‌گیرد؟
4. آیا ترتیب <span dir="ltr">Call</span>ها بخشی از <span dir="ltr">Contract</span> است یا <span dir="ltr">Leak</span>؟
5. <span dir="ltr">Failure</span> یک جزء چه <span dir="ltr">State</span> نامعلومی در جزء دیگر می‌سازد؟
6. آیا دادهٔ ارسالی حداقلِ لازم است یا <span dir="ltr">Entity dump</span>؟
7. آیا دو جزء به یک دلیل کسب‌وکاری تغییر می‌کنند؟
8. آیا مرز جدید فقط تعداد <span dir="ltr">Network call</span> را زیاد کرده است؟

## <span dir="ltr">12. Trade-off</span>؛ کمترین <span dir="ltr">Coupling</span> ممکن هدف نیست

یک سامانهٔ بدون <span dir="ltr">Coupling</span> وجود ندارد. <span dir="ltr">Contract</span> مشترک خود نوعی <span dir="ltr">Coupling</span> است. هدف:

- <span dir="ltr">Coupling</span> آگاهانه و قابل‌مشاهده
- وابستگی به معنا و <span dir="ltr">Contract</span> پایدار، نه <span dir="ltr">Representation</span> داخلی
- <span dir="ltr">Cohesion</span> مناسب در محل <span dir="ltr">Rule</span>
- <span dir="ltr">Failure</span> و <span dir="ltr">Change impact</span> قابل‌پیش‌بینی

کپی‌کردن همهٔ داده‌ها برای حذف <span dir="ltr">Call</span> می‌تواند <span dir="ltr">Consistency coupling</span> و <span dir="ltr">Reconciliation cost</span> را بیشتر کند. تصمیم همیشه <span dir="ltr">Contextual</span> است.

## 13. تمرین مستقل و <span dir="ltr">Rubric</span>

[<span dir="ltr">Day 04 Exercise</span>](../exercises/day-04-coupling-review.md) را با [<span dir="ltr">Template</span>](../artifacts/coupling-review-template.md) انجام بده.

| معیار | امتیاز |
|---|---:|
| تشخیص حداقل پنج <span dir="ltr">Coupling</span> با شاهد | ۳ |
| ارزیابی <span dir="ltr">Cohesion</span> و <span dir="ltr">Owner</span> | ۲ |
| تفکیک <span dir="ltr">Encapsulation/Information Hiding</span> | ۲ |
| <span dir="ltr">Redesign</span> معنایی بدون <span dir="ltr">Technology leap</span> | ۲ |
| <span dir="ltr">Trade-off</span> و <span dir="ltr">Debt</span> باقی‌مانده | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 14. آزمون خروج

درس را ببند و [<span dir="ltr">Exit Ticket</span>](../quizzes/day-04-exit-ticket.md) را پاسخ بده. فردا این معیارها را روی <span dir="ltr">Capability Map</span> و <span dir="ltr">BIAN</span> به کار می‌بریم.


</div>
