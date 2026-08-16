<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 06</span> — <span dir="ltr">Value Object</span>های بانکی و <span dir="ltr">Pipeline</span> قابل اعتماد

- <span dir="ltr">Day budget: 60 minutes</span> — <span dir="ltr">18 lesson</span> + <span dir="ltr">35 coding/test</span> + <span dir="ltr">7 exit ticket</span>
- <span dir="ltr">Output:</span> <span dir="ltr">`Money`</span>، <span dir="ltr">`AccountId`</span>، <span dir="ltr">`CustomerId`</span>، <span dir="ltr">`BranchId`</span> و <span dir="ltr">`mvn verify`</span> سبز
- <span dir="ltr">Code scope:</span> <span dir="ltr">`backend/banking-modulith`</span>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Primitive Obsession</span> را در مرزهای بانکی تشخیص بدهی.
2. <span dir="ltr">Value Object</span> را بر اساس معنا، <span dir="ltr">Equality</span>، <span dir="ltr">Invariant</span> و <span dir="ltr">Immutability</span> طراحی کنی.
3. <span dir="ltr">Money</span> را بدون <span dir="ltr">`double`</span>، <span dir="ltr">Rounding</span> پنهان یا <span dir="ltr">Equality</span> اشتباه بسازی.
4. شناسهٔ داخلی را از شمارهٔ حساب، <span dir="ltr">CIF</span> و کد شعبه جدا نگه داری.
5. تست‌های مثبت، منفی و <span dir="ltr">Edge</span> را در <span dir="ltr">Pipeline Maven</span> اجرا کنی.

## 2. چرا <span dir="ltr">Day 06</span> هنوز معماری است؟

اگر <span dir="ltr">Contract</span> بگوید همه‌چیز <span dir="ltr">`String`</span> و <span dir="ltr">`BigDecimal`</span> خام است، زبان دامین در مرز کد گم می‌شود:


</div>

<div dir="ltr" align="left">

```java
transfer("1001", "1002", new BigDecimal("100000"), "IRR", "001");
```

</div>

<div dir="rtl" align="right">


از <span dir="ltr">Signature</span> معلوم نیست <span dir="ltr">`1001`</span> حساب، مشتری یا شعبه است؛ مبلغ مثبت بودن را چه کسی کنترل می‌کند؛ <span dir="ltr">Currency</span> با چه <span dir="ltr">Policy</span> مقایسه می‌شود؛ و <span dir="ltr">`001`</span> چه معنایی دارد. <span dir="ltr">Type</span>های دامینی بخشی از <span dir="ltr">Information Hiding</span> و <span dir="ltr">Error prevention</span> هستند.

## <span dir="ltr">3. Value Object</span> چیست؟

<span dir="ltr">Value Object</span> شیئی است که هویتش با مقدار و معنا تعیین می‌شود، نه با <span dir="ltr">Identity</span> مستقل و <span dir="ltr">Lifecycle</span> قابل‌پیگیری.

ویژگی‌های مورد انتظار:

- <span dir="ltr">Immutable</span>
- <span dir="ltr">Equality</span> بر اساس اجزای معنادار
- <span dir="ltr">Invariant</span> معتبر از لحظهٔ ساخت
- <span dir="ltr">Operation</span>های بدون <span dir="ltr">Side effect</span> روی مقدار
- نام و <span dir="ltr">API</span> دامینی

<span dir="ltr">`Money(100, IRR)`</span> با <span dir="ltr">Money</span> دیگری با همان مقدار عددی و <span dir="ltr">Currency</span> برابر است؛ لازم نیست شناسهٔ مستقل داشته باشد.

## <span dir="ltr">4. Entity</span> در برابر <span dir="ltr">Value Object</span>

| پرسش | <span dir="ltr">Entity</span> | <span dir="ltr">Value Object</span> |
|---|---|---|
| هویت مستقل دارد؟ | بله | خیر |
| تغییر <span dir="ltr">State</span> در زمان مهم است؟ | معمولاً بله | معمولاً با نمونهٔ جدید |
| <span dir="ltr">Equality</span> | <span dir="ltr">Identity</span> | <span dir="ltr">Value/meaning</span> |
| مثال | <span dir="ltr">DepositAccount</span>، <span dir="ltr">LoanAgreement</span> | <span dir="ltr">Money</span>، <span dir="ltr">AccountId</span>، <span dir="ltr">DateRange</span> |

<span dir="ltr">Typed ID</span> خودش <span dir="ltr">Value Object</span> است اما به <span dir="ltr">Entity</span> دیگری اشاره می‌کند. <span dir="ltr">`AccountId`</span> با <span dir="ltr">`AccountNumber`</span> یکی نیست: اولی شناسهٔ داخلی پایدار، دومی <span dir="ltr">Identifier</span> کسب‌وکاری/نمایشی با قواعد و <span dir="ltr">Lifecycle</span> دیگر است.

## 5. طراحی <span dir="ltr">Money</span>

### اجزای حداقلی

- <span dir="ltr">`BigDecimal amount`</span>
- <span dir="ltr">`Currency currency`</span>

### چرا <span dir="ltr">`double`</span> ممنوع است؟

اعداد ممیز شناور دودویی بسیاری از مقادیر ده‌دهی را دقیق نمایش نمی‌دهند. خطای کوچک برای پول، تجمیع و <span dir="ltr">Reconciliation</span> قابل‌قبول نیست. <span dir="ltr">`BigDecimal`</span> نمایش ده‌دهی کنترل‌شده می‌دهد، اما به‌تنهایی همهٔ مسائل را حل نمی‌کند.

### <span dir="ltr">Scale</span> و <span dir="ltr">Equality</span>

در <span dir="ltr">Java:</span>


</div>

<div dir="ltr" align="left">

```java
new BigDecimal("100.0").equals(new BigDecimal("100.00")) // false
new BigDecimal("100.0").compareTo(new BigDecimal("100.00")) // 0
```

</div>

<div dir="rtl" align="right">


اگر <span dir="ltr">Equality Money</span> باید عددی باشد، <span dir="ltr">Implementation</span> باید <span dir="ltr">Scale</span> ظاهری را <span dir="ltr">Normalise</span> یا با <span dir="ltr">`compareTo`</span> و <span dir="ltr">Hash</span> سازگار مدیریت کند. <span dir="ltr">`equals`</span> و <span dir="ltr">`hashCode`</span> باید <span dir="ltr">Contract</span> مشترک داشته باشند؛ فقط <span dir="ltr">Override</span> کردن <span dir="ltr">equals</span> کافی نیست.

### <span dir="ltr">Currency</span>

جمع دو <span dir="ltr">Money</span> با <span dir="ltr">Currency</span> متفاوت باید <span dir="ltr">Fail-fast</span> شود. تبدیل ارز <span dir="ltr">Operation</span> جدا با <span dir="ltr">Rate</span>، <span dir="ltr">Source</span> و <span dir="ltr">Timestamp</span> است؛ <span dir="ltr">`add`</span> نباید <span dir="ltr">Conversion</span> پنهان انجام دهد.

### <span dir="ltr">Signed</span> یا <span dir="ltr">Positive</span>؟

<span dir="ltr">Money</span> عمومی می‌تواند منفی باشد، چون <span dir="ltr">Adjustment</span>، <span dir="ltr">Delta</span> و <span dir="ltr">Accounting amount</span> ممکن است <span dir="ltr">Signed</span> باشند. اما <span dir="ltr">`TransferAmount`</span> یا <span dir="ltr">Use Case</span> انتقال باید مثبت‌بودن را کنترل کند. اگر <span dir="ltr">Money</span> را همیشه مثبت کنی، شاید <span dir="ltr">Reuse</span> را محدود کنی؛ اگر همه‌جا <span dir="ltr">Signed</span> بگذاری، هر <span dir="ltr">Use Case</span> باید <span dir="ltr">Rule</span> خودش را اعمال کند. تصمیم را ثبت کن.

### <span dir="ltr">Rounding</span>

هیچ <span dir="ltr">Factory</span> یا <span dir="ltr">Arithmetic</span> نباید بدون <span dir="ltr">Policy</span> مقدار را <span dir="ltr">Round</span> کند. <span dir="ltr">Operation</span> نیازمند <span dir="ltr">Rounding</span> باید <span dir="ltr">Scale</span> و <span dir="ltr">`RoundingMode`</span> یا یک <span dir="ltr">Policy</span> دامینی صریح دریافت کند.


</div>

<div dir="ltr" align="left">

```java
money.roundedTo(0, RoundingMode.HALF_EVEN)
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Policy Scale</span> می‌تواند در <span dir="ltr">Product</span>، <span dir="ltr">Payments</span> یا <span dir="ltr">Accounting</span> متفاوت باشد؛ <span dir="ltr">Currency default</span> به‌تنهایی همیشه کافی نیست.

## <span dir="ltr">6. Typed ID</span>ها

اگر همهٔ شناسه‌ها <span dir="ltr">`String`</span> باشند، <span dir="ltr">Compiler</span> نمی‌تواند این خطا را بگیرد:


</div>

<div dir="ltr" align="left">

```java
credit(customerId, accountId); // ترتیب اشتباه ولی compile می‌شود
```

</div>

<div dir="rtl" align="right">


با <span dir="ltr">Type</span>های مستقل:


</div>

<div dir="ltr" align="left">

```java
credit(AccountId accountId, CustomerId customerId);
```

</div>

<div dir="rtl" align="right">


خطای جابه‌جایی پیش از اجرا آشکار می‌شود.

### قواعد طراحی

- مقدار تهی و <span dir="ltr">Blank</span> رد شود.
- <span dir="ltr">Format</span> فقط اگر <span dir="ltr">Contract</span> واقعی دارد <span dir="ltr">Validate</span> شود؛ <span dir="ltr">Regex</span> خیالی نساز.
- <span dir="ltr">Parsing</span> و <span dir="ltr">Creation</span> معنای روشن داشته باشند.
- <span dir="ltr">`toString`</span> نباید ناخواسته دادهٔ حساس را در <span dir="ltr">Log</span> افشا کند.
- <span dir="ltr">ID</span> داخلی با شمارهٔ بانکی نمایش‌پذیر یکی نشود.

<span dir="ltr">Java</span> <span dir="ltr">`record`</span> برای <span dir="ltr">Value Object</span> کوچک مناسب است، اما <span dir="ltr">Compact constructor</span> و <span dir="ltr">Equality</span> پیش‌فرض باید با <span dir="ltr">Rule</span> سازگار باشند. برای <span dir="ltr">Money</span>، <span dir="ltr">Equality</span> پیش‌فرض <span dir="ltr">`BigDecimal`</span> ممکن است کافی نباشد.

## <span dir="ltr">7. Static Factory</span>؛ <span dir="ltr">Pattern</span> یا <span dir="ltr">API design</span>؟

<span dir="ltr">Factory</span>هایی مانند <span dir="ltr">`Money.of(amount, currency)`</span> یا <span dir="ltr">`AccountId.parse(text)`</span> می‌توانند <span dir="ltr">Intent</span> و <span dir="ltr">Validation</span> را روشن کنند. اما ایجاد <span dir="ltr">Class</span> به نام <span dir="ltr">`MoneyFactory`</span> بدون <span dir="ltr">Decision</span> واقعی فقط <span dir="ltr">Indirection</span> است.

از <span dir="ltr">Static Factory</span> وقتی استفاده کن که:

- نام <span dir="ltr">Creation</span> معنا می‌دهد (<span dir="ltr">`parse`</span>, <span dir="ltr">`zero`</span>, <span dir="ltr">`ofMinorUnits`</span>)
- <span dir="ltr">Canonicalisation</span> یا <span dir="ltr">Validation</span> لازم است
- <span dir="ltr">Constructor</span> خام ممکن است <span dir="ltr">Contract</span> را مبهم کند

از <span dir="ltr">Abstract Factory</span> یا <span dir="ltr">Registry</span> در <span dir="ltr">Week 01</span> استفاده نکن؛ <span dir="ltr">Variation</span> واقعی وجود ندارد.

## 8. تست‌های لازم

### <span dir="ltr">Happy path</span>

- ساخت <span dir="ltr">Money</span> معتبر
- جمع و تفریق <span dir="ltr">Currency</span> یکسان
- <span dir="ltr">Parse</span> شناسهٔ معتبر

### <span dir="ltr">Equality</span>

- <span dir="ltr">`100.0 IRR == 100.00 IRR`</span>
- مبلغ برابر با <span dir="ltr">Currency</span> متفاوت، برابر نیست
- <span dir="ltr">`hashCode`</span> برای <span dir="ltr">Money</span>های برابر یکسان است

### <span dir="ltr">Negative/edge</span>

- <span dir="ltr">amount/currency null</span>
- <span dir="ltr">Currency mismatch</span>
- <span dir="ltr">ID null/blank</span>
- نیاز به <span dir="ltr">Rounding</span> بدون <span dir="ltr">Policy</span>
- مقدار بسیار بزرگ بدون <span dir="ltr">Overflow</span> عددی

### <span dir="ltr">Compile-time evidence</span>

اینکه <span dir="ltr">`CustomerId`</span> را نمی‌توان جای <span dir="ltr">`AccountId`</span> داد، تست <span dir="ltr">Runtime</span> نیست. در <span dir="ltr">Workbook</span> با <span dir="ltr">Signature</span> یا <span dir="ltr">Compilation evidence</span> توضیح داده می‌شود؛ لازم نیست تستی بسازی که پروژه را عمداً <span dir="ltr">Fail</span> نگه دارد.

## 9. ساختار پیشنهادی <span dir="ltr">Package</span>

در <span dir="ltr">Week 01 Type</span>ها را در <span dir="ltr">Package</span> آموزشی کوچک نگه دار. آن‌ها را سریعاً در <span dir="ltr">`common`</span> یا <span dir="ltr">`shared-kernel`</span> سراسری قرار نده. <span dir="ltr">Money</span> در <span dir="ltr">Accounting</span> ممکن است <span dir="ltr">Policy</span> و معنای متفاوتی از <span dir="ltr">Payments</span> داشته باشد.


</div>

<div dir="ltr" align="left">

```text
com.example.corebankinglab.foundation.money
com.example.corebankinglab.foundation.identity
```

</div>

<div dir="rtl" align="right">


این فقط نقطهٔ شروع است. <span dir="ltr">Week 02</span> با کشف <span dir="ltr">Context</span>ها تصمیم <span dir="ltr">Shared Kernel</span> را نقد می‌کند.

## <span dir="ltr">10. Pipeline</span> <span dir="ltr">`mvn verify`</span>

<span dir="ltr">Pipeline</span> این هفته باید حداقل این زنجیره را اجرا کند:


</div>

<div dir="ltr" align="left">

```text
checkout
  → Java 21
  → compile
  → unit tests
  → Spring context/module tests already present
  → package/verify
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Command</span> محلی:


</div>

<div dir="ltr" align="left">

```bash
cd backend/banking-modulith
mvn -B -ntp verify
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">`verify`</span> فقط سبزبودن فعلی را نشان می‌دهد؛ کیفیت تست و <span dir="ltr">Coverage</span> معنایی را تضمین نمی‌کند. یک تست که فقط <span dir="ltr">Getter</span> را می‌خواند شاهد <span dir="ltr">Rule</span> دامینی نیست.

## 11. ترتیب پیاده‌سازی سبز

1. <span dir="ltr">Baseline</span> <span dir="ltr">`mvn verify`</span> را ثبت کن.
2. ابتدا <span dir="ltr">`AccountId`</span> و <span dir="ltr">Test null/blank</span> را بساز.
3. سه <span dir="ltr">Typed ID</span> را با <span dir="ltr">Duplication</span> کوچک و روشن بساز؛ زود <span dir="ltr">Abstract Base</span> نساز.
4. <span dir="ltr">Money</span> را با <span dir="ltr">Null/Currency guard</span> ایجاد کن.
5. <span dir="ltr">Equality</span> عددی و <span dir="ltr">hashCode</span> سازگار را تست کن.
6. <span dir="ltr">`add/subtract`</span> با <span dir="ltr">Currency check</span> را اضافه کن.
7. <span dir="ltr">Rounding</span> صریح و <span dir="ltr">Edge test</span> را اضافه کن.
8. <span dir="ltr">`mvn verify`</span> نهایی را ثبت و <span dir="ltr">Diff</span> را مرور کن.

<span dir="ltr">Duplication</span> سه <span dir="ltr">ID</span> در این مرحله ارزان‌تر از <span dir="ltr">Hierarchy</span> اشتباه و <span dir="ltr">Coupling</span> سراسری است. بعد از مشاهدهٔ الگو می‌توان تصمیم گرفت.

## 12. خطاهای رایج

- استفاده از <span dir="ltr">`double`</span> یا <span dir="ltr">`float`</span>
- <span dir="ltr">Setter</span> روی <span dir="ltr">Money</span>
- تبدیل ارز داخل <span dir="ltr">`add`</span>
- <span dir="ltr">`setScale`</span> پنهان در <span dir="ltr">Constructor</span>
- <span dir="ltr">Equality</span> ناسازگار با <span dir="ltr">hashCode</span>
- <span dir="ltr">Validation</span> خیالی برای <span dir="ltr">Format ID</span>
- استفاده از <span dir="ltr">Entity/JPA annotation</span> روی <span dir="ltr">Value Object</span> مستقل
- ایجاد <span dir="ltr">`BaseId<T>`</span> پیچیده پیش از نیاز
- قرار دادن همهٔ <span dir="ltr">Type</span>ها در <span dir="ltr">`common`</span> بدون <span dir="ltr">Context owner</span>

## 13. تمرین و <span dir="ltr">Rubric</span>

[<span dir="ltr">Day 06 Exercise</span>](../exercises/day-06-value-objects.md) را اجرا کن.

| معیار | امتیاز |
|---|---:|
| <span dir="ltr">Immutability</span> و <span dir="ltr">invariant</span> ساخت | ۲ |
| <span dir="ltr">Equality/hashCode</span> صحیح <span dir="ltr">Money</span> | ۲ |
| <span dir="ltr">Currency</span> و <span dir="ltr">Rounding</span> صریح | ۲ |
| <span dir="ltr">Typed IDs</span> و مرز معنایی | ۲ |
| تست منفی و <span dir="ltr">`mvn verify`</span> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. استفاده از <span dir="ltr">`double`</span> یا <span dir="ltr">Rounding</span> پنهان <span dir="ltr">Critical Error</span> است.

## 14. آزمون خروج

کد و درس را ببند و [<span dir="ltr">Exit Ticket</span>](../quizzes/day-06-exit-ticket.md) را پاسخ بده. <span dir="ltr">Day 08</span> همین <span dir="ltr">Type</span>ها را در یک <span dir="ltr">Refactor</span> واقعی به کار می‌گیرد؛ امروز می‌توانی <span dir="ltr">Implementation</span> خودت را بسازی، اما <span dir="ltr">Starter</span> روز هشتم راه‌حل کامل را تحمیل نمی‌کند.


</div>
