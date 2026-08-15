# Day 04 — Coupling، Cohesion، Encapsulation و Information Hiding

- Day budget: 55 minutes — 27 lesson + 23 exercise + 5 exit ticket
- Output: Coupling Review و Boundary redesign
- Banking case: اعطای تسهیلات و واریز به سپرده

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. Coupling و Cohesion را با مثال رفتاری، نه فقط تعریف کتابی، تحلیل کنی.
2. Encapsulation را از Information Hiding جدا کنی.
3. پنج نوع Coupling مهم در سامانهٔ بانکی را پیدا کنی.
4. تشخیص بدهی یک API ظاهراً مستقل چگونه مدل، زمان‌بندی یا دادهٔ داخلی را نشت می‌دهد.
5. یک طراحی کاپل‌شده را بدون پریدن به Microservice بازطراحی کنی.

## 2. چرا این چهار نیرو مهم‌اند؟

Capability و Traceability می‌گویند چرا یک مسئولیت وجود دارد. چهار نیروی امروز می‌گویند **مسئولیت‌ها چگونه کنار هم قرار گیرند تا تغییر محلی بماند و دانش داخلی نشت نکند**.

مرز خوب معمولاً این ویژگی‌ها را دارد:

- اجزای درون مرز به یک دلیل کسب‌وکاری نزدیک تغییر می‌کنند: Cohesion بالا.
- تغییر داخل مرز کمترین اجبار را به بیرون تحمیل می‌کند: Coupling کنترل‌شده.
- Invariant و State فقط از مسیر رفتار مجاز تغییر می‌کنند: Encapsulation.
- تصمیم‌ها و ساختارهایی که ممکن است عوض شوند پشت Contract پایدار پنهان‌اند: Information Hiding.

این‌ها عددهای مطلق یا هدف‌های جداگانه نیستند. گاهی افزودن یک Contract، Coupling فنی را بیشتر اما Coupling تغییر را کمتر می‌کند.

## 3. Coupling؛ وابستگی فقط Import نیست

دو جزء وقتی Coupled هستند که تغییر یا رفتار یکی بر دیگری اثر بگذارد. نبود Dependency کامپایل به معنی نبود Coupling نیست.

### 3.1 Structural coupling

یک Module Class یا Package داخلی Module دیگر را Import می‌کند. این نوع در Code Review دیده می‌شود.

```java
depositRepository.updateBalance(...); // از داخل Lending
```

Lending اکنون ساختار و Lifecycle دادهٔ Deposits را می‌شناسد.

### 3.2 Data coupling

دو جزء Schema، Entity یا Payload بسیار بزرگ مشترک دارند. اگر `CustomerEntity` مشترک تغییر کند، چند Context هم‌زمان Release می‌شوند.

راه‌حل همیشه حذف دادهٔ مشترک نیست؛ Contract باید فقط Fact لازم را با معنای روشن حمل کند، نه Object داخلی را.

### 3.3 Behavioral coupling

مصرف‌کننده به ترتیب یا Side effect داخلی Provider وابسته است. مثلاً Channel می‌داند برای انتقال وجه باید ابتدا `validate`، سپس `reserve` و سپس `post` را با ترتیب خاص صدا بزند. در واقع Workflow داخلی Payments به Channel نشت کرده است.

### 3.4 Temporal coupling

اجزا باید هم‌زمان در دسترس یا با ترتیب زمانی ظریف اجرا شوند. پنج Call همگام زنجیره‌ای Availability را ضرب می‌کنند. Event هم Temporal coupling را خودکار حذف نمی‌کند؛ Consumer ممکن است به ترتیب پنهان Eventها وابسته باشد.

### 3.5 Change coupling

دو جزء معمولاً به دلیل یک Rule با هم تغییر و Release می‌شوند. این مهم‌ترین Evidence برای بازبینی Boundary است. Git history، Incident و Change request از Diagram معتبرترند.

### 3.6 Operational coupling

یک Deployment، دیتابیس، Queue، Scaling profile یا Runbook مشترک باعث می‌شود Failure یکی روی دیگری اثر بگذارد. این موضوع هنگام استخراج Microservice تعیین‌کننده است، نه در Week 01.

## 4. Cohesion؛ چرا این مسئولیت‌ها کنار هم‌اند؟

Cohesion میزان ارتباط معنایی و تغییر مشترک اجزای داخل یک مرز است.

### Cohesion بالا

در Deposits، محاسبهٔ available balance، Hold و کنترل اجازهٔ برداشت حول Invariant «چه مقدار اکنون قابل برداشت است؟» نزدیک‌اند.

### Cohesion پایین

کلاس `BankingService` که افتتاح سپرده، تصویب تسهیلات، ثبت سند، ارسال پیامک و گزارش مدیریتی را انجام می‌دهد، فقط به این دلیل کنار هم است که «همه بانکی‌اند».

### آزمون یک جمله‌ای

مسئولیت Module را در یک جمله بنویس:

> این Module مسئول ... است و تنها Authority تغییر ... را دارد.

اگر جمله به چند «و همچنین» طولانی نیاز دارد یا Ownerهای متفاوت دارد، Cohesion مشکوک است.

## 5. Encapsulation؛ کنترل State و Invariant

Encapsulation یعنی داده و رفتار مرتبط طوری کنار هم قرار گیرند که State فقط از مسیر Operationهای معتبر تغییر کند.

نمونهٔ ضعیف:

```java
account.setAvailableBalance(account.getAvailableBalance().subtract(amount));
```

Caller باید بداند available balance چگونه محاسبه می‌شود، Hold چه اثری دارد و منفی‌شدن مجاز است یا نه.

نمونهٔ بهتر از نظر Intent:

```java
account.placeHold(holdId, amount, legalOrderReference);
```

این Signature هنوز طراحی نهایی نیست، اما Invariant را داخل مدل نگه می‌دارد. Encapsulation صرفاً `private` کردن Field نیست؛ اگر Setter عمومی همه‌چیز را تغییر دهد، State پنهان ولی Rule بی‌دفاع است.

## 6. Information Hiding؛ پنهان‌کردن تصمیم متغیر

Information Hiding می‌پرسد چه تصمیمی احتمال تغییر دارد و چه کسانی نباید آن را بدانند.

نمونه‌ها:

- Channel نباید بداند Deposits مانده را از یک Row، Ledger یا Projection می‌خواند.
- Lending نباید بداند Accounting برای چه سرفصل و تفصیلی Journal می‌سازد.
- Consumer نباید به نام جدول یا ترتیب Internal Step وابسته شود.
- Contract نباید Precision دیتابیس را بدون دلیل به مدل کسب‌وکار تبدیل کند.

Encapsulation بیشتر دربارهٔ حفاظت از State/Invariant است؛ Information Hiding دربارهٔ حفاظت از تصمیم طراحی و جلوگیری از Ripple change. هم‌پوشانی دارند اما مساوی نیستند.

## 7. طراحی کاپل‌شدهٔ اعطا

فرض کن یک `LoanDisbursementOrchestrator` این کارها را انجام می‌دهد:

```text
1. SELECT loan row
2. UPDATE loan.status = DISBURSED
3. UPDATE deposit.balance = balance + amount
4. INSERT accounting.document_line twice
5. SEND notification
```

و برای این کار به سه Schema مشترک دسترسی مستقیم دارد.

### اشکال‌ها

| نشانه | نوع مشکل | پیامد |
|---|---|---|
| Update جدول Deposits از Lending | Data/structural coupling | Rule مانده دور زده می‌شود |
| وضعیت Loan قبل از نتیجهٔ واریز قطعی می‌شود | Temporal/semantic coupling | وضعیت کاذب |
| Orchestrator سرفصل‌ها را می‌شناسد | Information leak | تغییر Accounting نیازمند تغییر Orchestrator |
| Notification در همان Method | Cohesion پایین | Failure پیامک عملیات مالی را آلوده می‌کند |
| یک تراکنش DB برای سه Owner | Ownership مشترک مصنوعی | استقلال مدل از بین می‌رود |

## 8. بازطراحی مرحله‌ای، بدون انتخاب زودهنگام فناوری

### گام 1 — Authority را جدا کن

- Lending فقط وضعیت و Rule اعطا را تغییر دهد.
- Deposits فقط اثر Credit روی حساب و ماندهٔ عملیاتی را اعمال کند.
- Accounting فقط Fact مالی را به Journal تبدیل کند.

### گام 2 — Contract معنایی تعریف کن

```text
Lending intent: DisburseLoan
Deposits intent: CreditDeposit for a business transaction
Deposits fact: DepositCredited
Lending fact: LoanDisbursed
Accounting input: accepted business/accounting fact
```

### گام 3 — Internal representation را پنهان کن

هیچ Contractی `TB_LOAN_ROW`، `DEPOSIT_ENTITY` یا لیست Debit/Credit داخلی را حمل نکند. فقط شناسه، مبلغ، معنا و Metadata لازم حمل شود.

### گام 4 — Failure را نام‌گذاری کن

اگر Deposit Credit رد شود، Lending نباید `DISBURSED` شود. اگر پاسخ گم شود، باید Correlation/Idempotency در هفته‌های بعد طراحی شود. امروز Unknown و Expected outcome ثبت می‌شود.

### گام 5 — Deployment را باز بگذار

سه مسئولیت می‌توانند فعلاً سه Module در یک Modulith باشند. جداسازی مدل الزاماً جداسازی شبکه‌ای نیست.

## 9. API چگونه Information leak می‌دهد؟

وجود HTTP مرز را ایجاد نمی‌کند. این API ضعیف است:

```json
{
  "table": "TB_DEPOSIT",
  "operation": "UPDATE",
  "column": "AVAILABLE_BALANCE",
  "delta": 100000000
}
```

Consumer تصمیم داخلی Provider را کنترل می‌کند. Contract معنایی‌تر:

```json
{
  "businessTransactionId": "...",
  "accountId": "...",
  "money": { "amount": "100000000", "currency": "IRR" },
  "reason": "LOAN_DISBURSEMENT",
  "loanDisbursementId": "..."
}
```

حتی این Contract نیز نیازمند Policy امنیت، Idempotency و Ownership است؛ اما به‌جای Update عمومی، Intent را بیان می‌کند.

## 10. Event چگونه Coupling می‌سازد؟

Event-driven بودن مترادف Loose coupling نیست. این موارد Coupling ایجاد می‌کنند:

- Event بزرگ با Snapshot همهٔ Entityها
- نام مبهم و نیاز Consumer به تفسیر داخلی
- وابستگی به ترتیب چند Topic بدون Key روشن
- تغییر Breaking بدون Versioning
- Consumerی که برای تکمیل Event باید پنج Query همگام بزند
- Eventی که در واقع Command پنهان است و Consumer خاص را هدف گرفته است

پس Coupling را از روی Protocol قضاوت نکن؛ از روی Knowledge و Change impact قضاوت کن.

## 11. Heuristicهای بازبینی Boundary

برای هر Dependency این پرسش‌ها را ثبت کن:

1. چه دانش داخلی‌ای عبور می‌کند؟
2. اگر Rule Provider تغییر کند، Consumer هم باید تغییر کند؟
3. چه کسی تصمیم نهایی را می‌گیرد؟
4. آیا ترتیب Callها بخشی از Contract است یا Leak؟
5. Failure یک جزء چه State نامعلومی در جزء دیگر می‌سازد؟
6. آیا دادهٔ ارسالی حداقلِ لازم است یا Entity dump؟
7. آیا دو جزء به یک دلیل کسب‌وکاری تغییر می‌کنند؟
8. آیا مرز جدید فقط تعداد Network call را زیاد کرده است؟

## 12. Trade-off؛ کمترین Coupling ممکن هدف نیست

یک سامانهٔ بدون Coupling وجود ندارد. Contract مشترک خود نوعی Coupling است. هدف:

- Coupling آگاهانه و قابل‌مشاهده
- وابستگی به معنا و Contract پایدار، نه Representation داخلی
- Cohesion مناسب در محل Rule
- Failure و Change impact قابل‌پیش‌بینی

کپی‌کردن همهٔ داده‌ها برای حذف Call می‌تواند Consistency coupling و Reconciliation cost را بیشتر کند. تصمیم همیشه Contextual است.

## 13. تمرین مستقل و Rubric

[Day 04 Exercise](../exercises/day-04-coupling-review.md) را با [Template](../artifacts/coupling-review-template.md) انجام بده.

| معیار | امتیاز |
|---|---:|
| تشخیص حداقل پنج Coupling با شاهد | ۳ |
| ارزیابی Cohesion و Owner | ۲ |
| تفکیک Encapsulation/Information Hiding | ۲ |
| Redesign معنایی بدون Technology leap | ۲ |
| Trade-off و Debt باقی‌مانده | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 14. آزمون خروج

درس را ببند و [Exit Ticket](../quizzes/day-04-exit-ticket.md) را پاسخ بده. فردا این معیارها را روی Capability Map و BIAN به کار می‌بریم.

