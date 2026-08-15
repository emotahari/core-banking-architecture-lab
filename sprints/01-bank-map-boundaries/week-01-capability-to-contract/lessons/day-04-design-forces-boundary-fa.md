<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 04</bdi> — <bdi dir="ltr">Coupling</bdi>، <bdi dir="ltr">Cohesion</bdi>، <bdi dir="ltr">Encapsulation</bdi> و <bdi dir="ltr">Information Hiding</bdi>

- <bdi dir="ltr">Day budget: 55 minutes</bdi> — <bdi dir="ltr">27 lesson</bdi> + <bdi dir="ltr">23 exercise</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output: Coupling Review</bdi> و <bdi dir="ltr">Boundary redesign</bdi>
- <bdi dir="ltr">Banking case:</bdi> اعطای تسهیلات و واریز به سپرده

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Coupling</bdi> و <bdi dir="ltr">Cohesion</bdi> را با مثال رفتاری، نه فقط تعریف کتابی، تحلیل کنی.
2. <bdi dir="ltr">Encapsulation</bdi> را از <bdi dir="ltr">Information Hiding</bdi> جدا کنی.
3. پنج نوع <bdi dir="ltr">Coupling</bdi> مهم در سامانهٔ بانکی را پیدا کنی.
4. تشخیص بدهی یک <bdi dir="ltr">API</bdi> ظاهراً مستقل چگونه مدل، زمان‌بندی یا دادهٔ داخلی را نشت می‌دهد.
5. یک طراحی کاپل‌شده را بدون پریدن به <bdi dir="ltr">Microservice</bdi> بازطراحی کنی.

## 2. چرا این چهار نیرو مهم‌اند؟

<bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Traceability</bdi> می‌گویند چرا یک مسئولیت وجود دارد. چهار نیروی امروز می‌گویند **مسئولیت‌ها چگونه کنار هم قرار گیرند تا تغییر محلی بماند و دانش داخلی نشت نکند**.

مرز خوب معمولاً این ویژگی‌ها را دارد:

- اجزای درون مرز به یک دلیل کسب‌وکاری نزدیک تغییر می‌کنند: <bdi dir="ltr">Cohesion</bdi> بالا.
- تغییر داخل مرز کمترین اجبار را به بیرون تحمیل می‌کند: <bdi dir="ltr">Coupling</bdi> کنترل‌شده.
- <bdi dir="ltr">Invariant</bdi> و <bdi dir="ltr">State</bdi> فقط از مسیر رفتار مجاز تغییر می‌کنند: <bdi dir="ltr">Encapsulation.</bdi>
- تصمیم‌ها و ساختارهایی که ممکن است عوض شوند پشت <bdi dir="ltr">Contract</bdi> پایدار پنهان‌اند: <bdi dir="ltr">Information Hiding.</bdi>

این‌ها عددهای مطلق یا هدف‌های جداگانه نیستند. گاهی افزودن یک <bdi dir="ltr">Contract</bdi>، <bdi dir="ltr">Coupling</bdi> فنی را بیشتر اما <bdi dir="ltr">Coupling</bdi> تغییر را کمتر می‌کند.

## <bdi dir="ltr">3. Coupling</bdi>؛ وابستگی فقط <bdi dir="ltr">Import</bdi> نیست

دو جزء وقتی <bdi dir="ltr">Coupled</bdi> هستند که تغییر یا رفتار یکی بر دیگری اثر بگذارد. نبود <bdi dir="ltr">Dependency</bdi> کامپایل به معنی نبود <bdi dir="ltr">Coupling</bdi> نیست.

### <bdi dir="ltr">3.1 Structural coupling</bdi>

یک <bdi dir="ltr">Module Class</bdi> یا <bdi dir="ltr">Package</bdi> داخلی <bdi dir="ltr">Module</bdi> دیگر را <bdi dir="ltr">Import</bdi> می‌کند. این نوع در <bdi dir="ltr">Code Review</bdi> دیده می‌شود.


</div>

<div dir="ltr" align="left">

```java
depositRepository.updateBalance(...); // از داخل Lending
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Lending</bdi> اکنون ساختار و <bdi dir="ltr">Lifecycle</bdi> دادهٔ <bdi dir="ltr">Deposits</bdi> را می‌شناسد.

### <bdi dir="ltr">3.2 Data coupling</bdi>

دو جزء <bdi dir="ltr">Schema</bdi>، <bdi dir="ltr">Entity</bdi> یا <bdi dir="ltr">Payload</bdi> بسیار بزرگ مشترک دارند. اگر <bdi dir="ltr">`CustomerEntity`</bdi> مشترک تغییر کند، چند <bdi dir="ltr">Context</bdi> هم‌زمان <bdi dir="ltr">Release</bdi> می‌شوند.

راه‌حل همیشه حذف دادهٔ مشترک نیست؛ <bdi dir="ltr">Contract</bdi> باید فقط <bdi dir="ltr">Fact</bdi> لازم را با معنای روشن حمل کند، نه <bdi dir="ltr">Object</bdi> داخلی را.

### <bdi dir="ltr">3.3 Behavioral coupling</bdi>

مصرف‌کننده به ترتیب یا <bdi dir="ltr">Side effect</bdi> داخلی <bdi dir="ltr">Provider</bdi> وابسته است. مثلاً <bdi dir="ltr">Channel</bdi> می‌داند برای انتقال وجه باید ابتدا <bdi dir="ltr">`validate`</bdi>، سپس <bdi dir="ltr">`reserve`</bdi> و سپس <bdi dir="ltr">`post`</bdi> را با ترتیب خاص صدا بزند. در واقع <bdi dir="ltr">Workflow</bdi> داخلی <bdi dir="ltr">Payments</bdi> به <bdi dir="ltr">Channel</bdi> نشت کرده است.

### <bdi dir="ltr">3.4 Temporal coupling</bdi>

اجزا باید هم‌زمان در دسترس یا با ترتیب زمانی ظریف اجرا شوند. پنج <bdi dir="ltr">Call</bdi> همگام زنجیره‌ای <bdi dir="ltr">Availability</bdi> را ضرب می‌کنند. <bdi dir="ltr">Event</bdi> هم <bdi dir="ltr">Temporal coupling</bdi> را خودکار حذف نمی‌کند؛ <bdi dir="ltr">Consumer</bdi> ممکن است به ترتیب پنهان <bdi dir="ltr">Event</bdi>ها وابسته باشد.

### <bdi dir="ltr">3.5 Change coupling</bdi>

دو جزء معمولاً به دلیل یک <bdi dir="ltr">Rule</bdi> با هم تغییر و <bdi dir="ltr">Release</bdi> می‌شوند. این مهم‌ترین <bdi dir="ltr">Evidence</bdi> برای بازبینی <bdi dir="ltr">Boundary</bdi> است. <bdi dir="ltr">Git history</bdi>، <bdi dir="ltr">Incident</bdi> و <bdi dir="ltr">Change request</bdi> از <bdi dir="ltr">Diagram</bdi> معتبرترند.

### <bdi dir="ltr">3.6 Operational coupling</bdi>

یک <bdi dir="ltr">Deployment</bdi>، دیتابیس، <bdi dir="ltr">Queue</bdi>، <bdi dir="ltr">Scaling profile</bdi> یا <bdi dir="ltr">Runbook</bdi> مشترک باعث می‌شود <bdi dir="ltr">Failure</bdi> یکی روی دیگری اثر بگذارد. این موضوع هنگام استخراج <bdi dir="ltr">Microservice</bdi> تعیین‌کننده است، نه در <bdi dir="ltr">Week 01.</bdi>

## <bdi dir="ltr">4. Cohesion</bdi>؛ چرا این مسئولیت‌ها کنار هم‌اند؟

<bdi dir="ltr">Cohesion</bdi> میزان ارتباط معنایی و تغییر مشترک اجزای داخل یک مرز است.

### <bdi dir="ltr">Cohesion</bdi> بالا

در <bdi dir="ltr">Deposits</bdi>، محاسبهٔ <bdi dir="ltr">available balance</bdi>، <bdi dir="ltr">Hold</bdi> و کنترل اجازهٔ برداشت حول <bdi dir="ltr">Invariant</bdi> «چه مقدار اکنون قابل برداشت است؟» نزدیک‌اند.

### <bdi dir="ltr">Cohesion</bdi> پایین

کلاس <bdi dir="ltr">`BankingService`</bdi> که افتتاح سپرده، تصویب تسهیلات، ثبت سند، ارسال پیامک و گزارش مدیریتی را انجام می‌دهد، فقط به این دلیل کنار هم است که «همه بانکی‌اند».

### آزمون یک جمله‌ای

مسئولیت <bdi dir="ltr">Module</bdi> را در یک جمله بنویس:

> این <bdi dir="ltr">Module</bdi> مسئول ... است و تنها <bdi dir="ltr">Authority</bdi> تغییر ... را دارد.

اگر جمله به چند «و همچنین» طولانی نیاز دارد یا <bdi dir="ltr">Owner</bdi>های متفاوت دارد، <bdi dir="ltr">Cohesion</bdi> مشکوک است.

## <bdi dir="ltr">5. Encapsulation</bdi>؛ کنترل <bdi dir="ltr">State</bdi> و <bdi dir="ltr">Invariant</bdi>

<bdi dir="ltr">Encapsulation</bdi> یعنی داده و رفتار مرتبط طوری کنار هم قرار گیرند که <bdi dir="ltr">State</bdi> فقط از مسیر <bdi dir="ltr">Operation</bdi>های معتبر تغییر کند.

نمونهٔ ضعیف:


</div>

<div dir="ltr" align="left">

```java
account.setAvailableBalance(account.getAvailableBalance().subtract(amount));
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Caller</bdi> باید بداند <bdi dir="ltr">available balance</bdi> چگونه محاسبه می‌شود، <bdi dir="ltr">Hold</bdi> چه اثری دارد و منفی‌شدن مجاز است یا نه.

نمونهٔ بهتر از نظر <bdi dir="ltr">Intent:</bdi>


</div>

<div dir="ltr" align="left">

```java
account.placeHold(holdId, amount, legalOrderReference);
```

</div>

<div dir="rtl" align="right">


این <bdi dir="ltr">Signature</bdi> هنوز طراحی نهایی نیست، اما <bdi dir="ltr">Invariant</bdi> را داخل مدل نگه می‌دارد. <bdi dir="ltr">Encapsulation</bdi> صرفاً <bdi dir="ltr">`private`</bdi> کردن <bdi dir="ltr">Field</bdi> نیست؛ اگر <bdi dir="ltr">Setter</bdi> عمومی همه‌چیز را تغییر دهد، <bdi dir="ltr">State</bdi> پنهان ولی <bdi dir="ltr">Rule</bdi> بی‌دفاع است.

## <bdi dir="ltr">6. Information Hiding</bdi>؛ پنهان‌کردن تصمیم متغیر

<bdi dir="ltr">Information Hiding</bdi> می‌پرسد چه تصمیمی احتمال تغییر دارد و چه کسانی نباید آن را بدانند.

نمونه‌ها:

- <bdi dir="ltr">Channel</bdi> نباید بداند <bdi dir="ltr">Deposits</bdi> مانده را از یک <bdi dir="ltr">Row</bdi>، <bdi dir="ltr">Ledger</bdi> یا <bdi dir="ltr">Projection</bdi> می‌خواند.
- <bdi dir="ltr">Lending</bdi> نباید بداند <bdi dir="ltr">Accounting</bdi> برای چه سرفصل و تفصیلی <bdi dir="ltr">Journal</bdi> می‌سازد.
- <bdi dir="ltr">Consumer</bdi> نباید به نام جدول یا ترتیب <bdi dir="ltr">Internal Step</bdi> وابسته شود.
- <bdi dir="ltr">Contract</bdi> نباید <bdi dir="ltr">Precision</bdi> دیتابیس را بدون دلیل به مدل کسب‌وکار تبدیل کند.

<bdi dir="ltr">Encapsulation</bdi> بیشتر دربارهٔ حفاظت از <bdi dir="ltr">State/Invariant</bdi> است؛ <bdi dir="ltr">Information Hiding</bdi> دربارهٔ حفاظت از تصمیم طراحی و جلوگیری از <bdi dir="ltr">Ripple change.</bdi> هم‌پوشانی دارند اما مساوی نیستند.

## 7. طراحی کاپل‌شدهٔ اعطا

فرض کن یک <bdi dir="ltr">`LoanDisbursementOrchestrator`</bdi> این کارها را انجام می‌دهد:


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


و برای این کار به سه <bdi dir="ltr">Schema</bdi> مشترک دسترسی مستقیم دارد.

### اشکال‌ها

| نشانه | نوع مشکل | پیامد |
|---|---|---|
| <bdi dir="ltr">Update</bdi> جدول <bdi dir="ltr">Deposits</bdi> از <bdi dir="ltr">Lending</bdi> | <bdi dir="ltr">Data/structural coupling</bdi> | <bdi dir="ltr">Rule</bdi> مانده دور زده می‌شود |
| وضعیت <bdi dir="ltr">Loan</bdi> قبل از نتیجهٔ واریز قطعی می‌شود | <bdi dir="ltr">Temporal/semantic coupling</bdi> | وضعیت کاذب |
| <bdi dir="ltr">Orchestrator</bdi> سرفصل‌ها را می‌شناسد | <bdi dir="ltr">Information leak</bdi> | تغییر <bdi dir="ltr">Accounting</bdi> نیازمند تغییر <bdi dir="ltr">Orchestrator</bdi> |
| <bdi dir="ltr">Notification</bdi> در همان <bdi dir="ltr">Method</bdi> | <bdi dir="ltr">Cohesion</bdi> پایین | <bdi dir="ltr">Failure</bdi> پیامک عملیات مالی را آلوده می‌کند |
| یک تراکنش <bdi dir="ltr">DB</bdi> برای سه <bdi dir="ltr">Owner</bdi> | <bdi dir="ltr">Ownership</bdi> مشترک مصنوعی | استقلال مدل از بین می‌رود |

## 8. بازطراحی مرحله‌ای، بدون انتخاب زودهنگام فناوری

### گام 1 — <bdi dir="ltr">Authority</bdi> را جدا کن

- <bdi dir="ltr">Lending</bdi> فقط وضعیت و <bdi dir="ltr">Rule</bdi> اعطا را تغییر دهد.
- <bdi dir="ltr">Deposits</bdi> فقط اثر <bdi dir="ltr">Credit</bdi> روی حساب و ماندهٔ عملیاتی را اعمال کند.
- <bdi dir="ltr">Accounting</bdi> فقط <bdi dir="ltr">Fact</bdi> مالی را به <bdi dir="ltr">Journal</bdi> تبدیل کند.

### گام 2 — <bdi dir="ltr">Contract</bdi> معنایی تعریف کن


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


### گام 3 — <bdi dir="ltr">Internal representation</bdi> را پنهان کن

هیچ <bdi dir="ltr">Contract</bdi>ی <bdi dir="ltr">`TB_LOAN_ROW`</bdi>، <bdi dir="ltr">`DEPOSIT_ENTITY`</bdi> یا لیست <bdi dir="ltr">Debit/Credit</bdi> داخلی را حمل نکند. فقط شناسه، مبلغ، معنا و <bdi dir="ltr">Metadata</bdi> لازم حمل شود.

### گام 4 — <bdi dir="ltr">Failure</bdi> را نام‌گذاری کن

اگر <bdi dir="ltr">Deposit Credit</bdi> رد شود، <bdi dir="ltr">Lending</bdi> نباید <bdi dir="ltr">`DISBURSED`</bdi> شود. اگر پاسخ گم شود، باید <bdi dir="ltr">Correlation/Idempotency</bdi> در هفته‌های بعد طراحی شود. امروز <bdi dir="ltr">Unknown</bdi> و <bdi dir="ltr">Expected outcome</bdi> ثبت می‌شود.

### گام 5 — <bdi dir="ltr">Deployment</bdi> را باز بگذار

سه مسئولیت می‌توانند فعلاً سه <bdi dir="ltr">Module</bdi> در یک <bdi dir="ltr">Modulith</bdi> باشند. جداسازی مدل الزاماً جداسازی شبکه‌ای نیست.

## <bdi dir="ltr">9. API</bdi> چگونه <bdi dir="ltr">Information leak</bdi> می‌دهد؟

وجود <bdi dir="ltr">HTTP</bdi> مرز را ایجاد نمی‌کند. این <bdi dir="ltr">API</bdi> ضعیف است:


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


<bdi dir="ltr">Consumer</bdi> تصمیم داخلی <bdi dir="ltr">Provider</bdi> را کنترل می‌کند. <bdi dir="ltr">Contract</bdi> معنایی‌تر:


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


حتی این <bdi dir="ltr">Contract</bdi> نیز نیازمند <bdi dir="ltr">Policy</bdi> امنیت، <bdi dir="ltr">Idempotency</bdi> و <bdi dir="ltr">Ownership</bdi> است؛ اما به‌جای <bdi dir="ltr">Update</bdi> عمومی، <bdi dir="ltr">Intent</bdi> را بیان می‌کند.

## <bdi dir="ltr">10. Event</bdi> چگونه <bdi dir="ltr">Coupling</bdi> می‌سازد؟

<bdi dir="ltr">Event-driven</bdi> بودن مترادف <bdi dir="ltr">Loose coupling</bdi> نیست. این موارد <bdi dir="ltr">Coupling</bdi> ایجاد می‌کنند:

- <bdi dir="ltr">Event</bdi> بزرگ با <bdi dir="ltr">Snapshot</bdi> همهٔ <bdi dir="ltr">Entity</bdi>ها
- نام مبهم و نیاز <bdi dir="ltr">Consumer</bdi> به تفسیر داخلی
- وابستگی به ترتیب چند <bdi dir="ltr">Topic</bdi> بدون <bdi dir="ltr">Key</bdi> روشن
- تغییر <bdi dir="ltr">Breaking</bdi> بدون <bdi dir="ltr">Versioning</bdi>
- <bdi dir="ltr">Consumer</bdi>ی که برای تکمیل <bdi dir="ltr">Event</bdi> باید پنج <bdi dir="ltr">Query</bdi> همگام بزند
- <bdi dir="ltr">Event</bdi>ی که در واقع <bdi dir="ltr">Command</bdi> پنهان است و <bdi dir="ltr">Consumer</bdi> خاص را هدف گرفته است

پس <bdi dir="ltr">Coupling</bdi> را از روی <bdi dir="ltr">Protocol</bdi> قضاوت نکن؛ از روی <bdi dir="ltr">Knowledge</bdi> و <bdi dir="ltr">Change impact</bdi> قضاوت کن.

## <bdi dir="ltr">11. Heuristic</bdi>های بازبینی <bdi dir="ltr">Boundary</bdi>

برای هر <bdi dir="ltr">Dependency</bdi> این پرسش‌ها را ثبت کن:

1. چه دانش داخلی‌ای عبور می‌کند؟
2. اگر <bdi dir="ltr">Rule Provider</bdi> تغییر کند، <bdi dir="ltr">Consumer</bdi> هم باید تغییر کند؟
3. چه کسی تصمیم نهایی را می‌گیرد؟
4. آیا ترتیب <bdi dir="ltr">Call</bdi>ها بخشی از <bdi dir="ltr">Contract</bdi> است یا <bdi dir="ltr">Leak</bdi>؟
5. <bdi dir="ltr">Failure</bdi> یک جزء چه <bdi dir="ltr">State</bdi> نامعلومی در جزء دیگر می‌سازد؟
6. آیا دادهٔ ارسالی حداقلِ لازم است یا <bdi dir="ltr">Entity dump</bdi>؟
7. آیا دو جزء به یک دلیل کسب‌وکاری تغییر می‌کنند؟
8. آیا مرز جدید فقط تعداد <bdi dir="ltr">Network call</bdi> را زیاد کرده است؟

## <bdi dir="ltr">12. Trade-off</bdi>؛ کمترین <bdi dir="ltr">Coupling</bdi> ممکن هدف نیست

یک سامانهٔ بدون <bdi dir="ltr">Coupling</bdi> وجود ندارد. <bdi dir="ltr">Contract</bdi> مشترک خود نوعی <bdi dir="ltr">Coupling</bdi> است. هدف:

- <bdi dir="ltr">Coupling</bdi> آگاهانه و قابل‌مشاهده
- وابستگی به معنا و <bdi dir="ltr">Contract</bdi> پایدار، نه <bdi dir="ltr">Representation</bdi> داخلی
- <bdi dir="ltr">Cohesion</bdi> مناسب در محل <bdi dir="ltr">Rule</bdi>
- <bdi dir="ltr">Failure</bdi> و <bdi dir="ltr">Change impact</bdi> قابل‌پیش‌بینی

کپی‌کردن همهٔ داده‌ها برای حذف <bdi dir="ltr">Call</bdi> می‌تواند <bdi dir="ltr">Consistency coupling</bdi> و <bdi dir="ltr">Reconciliation cost</bdi> را بیشتر کند. تصمیم همیشه <bdi dir="ltr">Contextual</bdi> است.

## 13. تمرین مستقل و <bdi dir="ltr">Rubric</bdi>

[<bdi dir="ltr">Day 04 Exercise</bdi>](../exercises/day-04-coupling-review.md) را با [<bdi dir="ltr">Template</bdi>](../artifacts/coupling-review-template.md) انجام بده.

| معیار | امتیاز |
|---|---:|
| تشخیص حداقل پنج <bdi dir="ltr">Coupling</bdi> با شاهد | ۳ |
| ارزیابی <bdi dir="ltr">Cohesion</bdi> و <bdi dir="ltr">Owner</bdi> | ۲ |
| تفکیک <bdi dir="ltr">Encapsulation/Information Hiding</bdi> | ۲ |
| <bdi dir="ltr">Redesign</bdi> معنایی بدون <bdi dir="ltr">Technology leap</bdi> | ۲ |
| <bdi dir="ltr">Trade-off</bdi> و <bdi dir="ltr">Debt</bdi> باقی‌مانده | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 14. آزمون خروج

درس را ببند و [<bdi dir="ltr">Exit Ticket</bdi>](../quizzes/day-04-exit-ticket.md) را پاسخ بده. فردا این معیارها را روی <bdi dir="ltr">Capability Map</bdi> و <bdi dir="ltr">BIAN</bdi> به کار می‌بریم.


</div>
