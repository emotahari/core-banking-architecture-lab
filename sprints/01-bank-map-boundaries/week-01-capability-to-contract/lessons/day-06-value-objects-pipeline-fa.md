# Day 06 — Value Objectهای بانکی و Pipeline قابل اعتماد

- Day budget: 60 minutes — 18 lesson + 35 coding/test + 7 exit ticket
- Output: `Money`، `AccountId`، `CustomerId`، `BranchId` و `mvn verify` سبز
- Code scope: `backend/banking-modulith`

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. Primitive Obsession را در مرزهای بانکی تشخیص بدهی.
2. Value Object را بر اساس معنا، Equality، Invariant و Immutability طراحی کنی.
3. Money را بدون `double`، Rounding پنهان یا Equality اشتباه بسازی.
4. شناسهٔ داخلی را از شمارهٔ حساب، CIF و کد شعبه جدا نگه داری.
5. تست‌های مثبت، منفی و Edge را در Pipeline Maven اجرا کنی.

## 2. چرا Day 06 هنوز معماری است؟

اگر Contract بگوید همه‌چیز `String` و `BigDecimal` خام است، زبان دامین در مرز کد گم می‌شود:

```java
transfer("1001", "1002", new BigDecimal("100000"), "IRR", "001");
```

از Signature معلوم نیست `1001` حساب، مشتری یا شعبه است؛ مبلغ مثبت بودن را چه کسی کنترل می‌کند؛ Currency با چه Policy مقایسه می‌شود؛ و `001` چه معنایی دارد. Typeهای دامینی بخشی از Information Hiding و Error prevention هستند.

## 3. Value Object چیست؟

Value Object شیئی است که هویتش با مقدار و معنا تعیین می‌شود، نه با Identity مستقل و Lifecycle قابل‌پیگیری.

ویژگی‌های مورد انتظار:

- Immutable
- Equality بر اساس اجزای معنادار
- Invariant معتبر از لحظهٔ ساخت
- Operationهای بدون Side effect روی مقدار
- نام و API دامینی

`Money(100, IRR)` با Money دیگری با همان مقدار عددی و Currency برابر است؛ لازم نیست شناسهٔ مستقل داشته باشد.

## 4. Entity در برابر Value Object

| پرسش | Entity | Value Object |
|---|---|---|
| هویت مستقل دارد؟ | بله | خیر |
| تغییر State در زمان مهم است؟ | معمولاً بله | معمولاً با نمونهٔ جدید |
| Equality | Identity | Value/meaning |
| مثال | DepositAccount، LoanAgreement | Money، AccountId، DateRange |

Typed ID خودش Value Object است اما به Entity دیگری اشاره می‌کند. `AccountId` با `AccountNumber` یکی نیست: اولی شناسهٔ داخلی پایدار، دومی Identifier کسب‌وکاری/نمایشی با قواعد و Lifecycle دیگر است.

## 5. طراحی Money

### اجزای حداقلی

- `BigDecimal amount`
- `Currency currency`

### چرا `double` ممنوع است؟

اعداد ممیز شناور دودویی بسیاری از مقادیر ده‌دهی را دقیق نمایش نمی‌دهند. خطای کوچک برای پول، تجمیع و Reconciliation قابل‌قبول نیست. `BigDecimal` نمایش ده‌دهی کنترل‌شده می‌دهد، اما به‌تنهایی همهٔ مسائل را حل نمی‌کند.

### Scale و Equality

در Java:

```java
new BigDecimal("100.0").equals(new BigDecimal("100.00")) // false
new BigDecimal("100.0").compareTo(new BigDecimal("100.00")) // 0
```

اگر Equality Money باید عددی باشد، Implementation باید Scale ظاهری را Normalise یا با `compareTo` و Hash سازگار مدیریت کند. `equals` و `hashCode` باید Contract مشترک داشته باشند؛ فقط Override کردن equals کافی نیست.

### Currency

جمع دو Money با Currency متفاوت باید Fail-fast شود. تبدیل ارز Operation جدا با Rate، Source و Timestamp است؛ `add` نباید Conversion پنهان انجام دهد.

### Signed یا Positive؟

Money عمومی می‌تواند منفی باشد، چون Adjustment، Delta و Accounting amount ممکن است Signed باشند. اما `TransferAmount` یا Use Case انتقال باید مثبت‌بودن را کنترل کند. اگر Money را همیشه مثبت کنی، شاید Reuse را محدود کنی؛ اگر همه‌جا Signed بگذاری، هر Use Case باید Rule خودش را اعمال کند. تصمیم را ثبت کن.

### Rounding

هیچ Factory یا Arithmetic نباید بدون Policy مقدار را Round کند. Operation نیازمند Rounding باید Scale و `RoundingMode` یا یک Policy دامینی صریح دریافت کند.

```java
money.roundedTo(0, RoundingMode.HALF_EVEN)
```

Policy Scale می‌تواند در Product، Payments یا Accounting متفاوت باشد؛ Currency default به‌تنهایی همیشه کافی نیست.

## 6. Typed IDها

اگر همهٔ شناسه‌ها `String` باشند، Compiler نمی‌تواند این خطا را بگیرد:

```java
credit(customerId, accountId); // ترتیب اشتباه ولی compile می‌شود
```

با Typeهای مستقل:

```java
credit(AccountId accountId, CustomerId customerId);
```

خطای جابه‌جایی پیش از اجرا آشکار می‌شود.

### قواعد طراحی

- مقدار تهی و Blank رد شود.
- Format فقط اگر Contract واقعی دارد Validate شود؛ Regex خیالی نساز.
- Parsing و Creation معنای روشن داشته باشند.
- `toString` نباید ناخواسته دادهٔ حساس را در Log افشا کند.
- ID داخلی با شمارهٔ بانکی نمایش‌پذیر یکی نشود.

Java `record` برای Value Object کوچک مناسب است، اما Compact constructor و Equality پیش‌فرض باید با Rule سازگار باشند. برای Money، Equality پیش‌فرض `BigDecimal` ممکن است کافی نباشد.

## 7. Static Factory؛ Pattern یا API design؟

Factoryهایی مانند `Money.of(amount, currency)` یا `AccountId.parse(text)` می‌توانند Intent و Validation را روشن کنند. اما ایجاد Class به نام `MoneyFactory` بدون Decision واقعی فقط Indirection است.

از Static Factory وقتی استفاده کن که:

- نام Creation معنا می‌دهد (`parse`, `zero`, `ofMinorUnits`)
- Canonicalisation یا Validation لازم است
- Constructor خام ممکن است Contract را مبهم کند

از Abstract Factory یا Registry در Week 01 استفاده نکن؛ Variation واقعی وجود ندارد.

## 8. تست‌های لازم

### Happy path

- ساخت Money معتبر
- جمع و تفریق Currency یکسان
- Parse شناسهٔ معتبر

### Equality

- `100.0 IRR == 100.00 IRR`
- مبلغ برابر با Currency متفاوت، برابر نیست
- `hashCode` برای Moneyهای برابر یکسان است

### Negative/edge

- amount/currency null
- Currency mismatch
- ID null/blank
- نیاز به Rounding بدون Policy
- مقدار بسیار بزرگ بدون Overflow عددی

### Compile-time evidence

اینکه `CustomerId` را نمی‌توان جای `AccountId` داد، تست Runtime نیست. در Workbook با Signature یا Compilation evidence توضیح داده می‌شود؛ لازم نیست تستی بسازی که پروژه را عمداً Fail نگه دارد.

## 9. ساختار پیشنهادی Package

در Week 01 Typeها را در Package آموزشی کوچک نگه دار. آن‌ها را سریعاً در `common` یا `shared-kernel` سراسری قرار نده. Money در Accounting ممکن است Policy و معنای متفاوتی از Payments داشته باشد.

```text
com.example.corebankinglab.foundation.money
com.example.corebankinglab.foundation.identity
```

این فقط نقطهٔ شروع است. Week 02 با کشف Contextها تصمیم Shared Kernel را نقد می‌کند.

## 10. Pipeline `mvn verify`

Pipeline این هفته باید حداقل این زنجیره را اجرا کند:

```text
checkout
  → Java 21
  → compile
  → unit tests
  → Spring context/module tests already present
  → package/verify
```

Command محلی:

```bash
cd backend/banking-modulith
mvn -B -ntp verify
```

`verify` فقط سبزبودن فعلی را نشان می‌دهد؛ کیفیت تست و Coverage معنایی را تضمین نمی‌کند. یک تست که فقط Getter را می‌خواند شاهد Rule دامینی نیست.

## 11. ترتیب پیاده‌سازی سبز

1. Baseline `mvn verify` را ثبت کن.
2. ابتدا `AccountId` و Test null/blank را بساز.
3. سه Typed ID را با Duplication کوچک و روشن بساز؛ زود Abstract Base نساز.
4. Money را با Null/Currency guard ایجاد کن.
5. Equality عددی و hashCode سازگار را تست کن.
6. `add/subtract` با Currency check را اضافه کن.
7. Rounding صریح و Edge test را اضافه کن.
8. `mvn verify` نهایی را ثبت و Diff را مرور کن.

Duplication سه ID در این مرحله ارزان‌تر از Hierarchy اشتباه و Coupling سراسری است. بعد از مشاهدهٔ الگو می‌توان تصمیم گرفت.

## 12. خطاهای رایج

- استفاده از `double` یا `float`
- Setter روی Money
- تبدیل ارز داخل `add`
- `setScale` پنهان در Constructor
- Equality ناسازگار با hashCode
- Validation خیالی برای Format ID
- استفاده از Entity/JPA annotation روی Value Object مستقل
- ایجاد `BaseId<T>` پیچیده پیش از نیاز
- قرار دادن همهٔ Typeها در `common` بدون Context owner

## 13. تمرین و Rubric

[Day 06 Exercise](../exercises/day-06-value-objects.md) را اجرا کن.

| معیار | امتیاز |
|---|---:|
| Immutability و invariant ساخت | ۲ |
| Equality/hashCode صحیح Money | ۲ |
| Currency و Rounding صریح | ۲ |
| Typed IDs و مرز معنایی | ۲ |
| تست منفی و `mvn verify` | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. استفاده از `double` یا Rounding پنهان Critical Error است.

## 14. آزمون خروج

کد و درس را ببند و [Exit Ticket](../quizzes/day-06-exit-ticket.md) را پاسخ بده. Day 08 همین Typeها را در یک Refactor واقعی به کار می‌گیرد؛ امروز می‌توانی Implementation خودت را بسازی، اما Starter روز هشتم راه‌حل کامل را تحمیل نمی‌کند.

