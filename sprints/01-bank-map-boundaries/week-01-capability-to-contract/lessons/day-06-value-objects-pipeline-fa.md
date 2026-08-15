<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 06</bdi> — <bdi dir="ltr">Value Object</bdi>های بانکی و <bdi dir="ltr">Pipeline</bdi> قابل اعتماد

- <bdi dir="ltr">Day budget: 60 minutes</bdi> — <bdi dir="ltr">18 lesson</bdi> + <bdi dir="ltr">35 coding/test</bdi> + <bdi dir="ltr">7 exit ticket</bdi>
- <bdi dir="ltr">Output:</bdi> <bdi dir="ltr">`Money`</bdi>، <bdi dir="ltr">`AccountId`</bdi>، <bdi dir="ltr">`CustomerId`</bdi>، <bdi dir="ltr">`BranchId`</bdi> و <bdi dir="ltr">`mvn verify`</bdi> سبز
- <bdi dir="ltr">Code scope:</bdi> <bdi dir="ltr">`backend/banking-modulith`</bdi>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Primitive Obsession</bdi> را در مرزهای بانکی تشخیص بدهی.
2. <bdi dir="ltr">Value Object</bdi> را بر اساس معنا، <bdi dir="ltr">Equality</bdi>، <bdi dir="ltr">Invariant</bdi> و <bdi dir="ltr">Immutability</bdi> طراحی کنی.
3. <bdi dir="ltr">Money</bdi> را بدون <bdi dir="ltr">`double`</bdi>، <bdi dir="ltr">Rounding</bdi> پنهان یا <bdi dir="ltr">Equality</bdi> اشتباه بسازی.
4. شناسهٔ داخلی را از شمارهٔ حساب، <bdi dir="ltr">CIF</bdi> و کد شعبه جدا نگه داری.
5. تست‌های مثبت، منفی و <bdi dir="ltr">Edge</bdi> را در <bdi dir="ltr">Pipeline Maven</bdi> اجرا کنی.

## 2. چرا <bdi dir="ltr">Day 06</bdi> هنوز معماری است؟

اگر <bdi dir="ltr">Contract</bdi> بگوید همه‌چیز <bdi dir="ltr">`String`</bdi> و <bdi dir="ltr">`BigDecimal`</bdi> خام است، زبان دامین در مرز کد گم می‌شود:


</div>

<div dir="ltr" align="left">

```java
transfer("1001", "1002", new BigDecimal("100000"), "IRR", "001");
```

</div>

<div dir="rtl" align="right">


از <bdi dir="ltr">Signature</bdi> معلوم نیست <bdi dir="ltr">`1001`</bdi> حساب، مشتری یا شعبه است؛ مبلغ مثبت بودن را چه کسی کنترل می‌کند؛ <bdi dir="ltr">Currency</bdi> با چه <bdi dir="ltr">Policy</bdi> مقایسه می‌شود؛ و <bdi dir="ltr">`001`</bdi> چه معنایی دارد. <bdi dir="ltr">Type</bdi>های دامینی بخشی از <bdi dir="ltr">Information Hiding</bdi> و <bdi dir="ltr">Error prevention</bdi> هستند.

## <bdi dir="ltr">3. Value Object</bdi> چیست؟

<bdi dir="ltr">Value Object</bdi> شیئی است که هویتش با مقدار و معنا تعیین می‌شود، نه با <bdi dir="ltr">Identity</bdi> مستقل و <bdi dir="ltr">Lifecycle</bdi> قابل‌پیگیری.

ویژگی‌های مورد انتظار:

- <bdi dir="ltr">Immutable</bdi>
- <bdi dir="ltr">Equality</bdi> بر اساس اجزای معنادار
- <bdi dir="ltr">Invariant</bdi> معتبر از لحظهٔ ساخت
- <bdi dir="ltr">Operation</bdi>های بدون <bdi dir="ltr">Side effect</bdi> روی مقدار
- نام و <bdi dir="ltr">API</bdi> دامینی

<bdi dir="ltr">`Money(100, IRR)`</bdi> با <bdi dir="ltr">Money</bdi> دیگری با همان مقدار عددی و <bdi dir="ltr">Currency</bdi> برابر است؛ لازم نیست شناسهٔ مستقل داشته باشد.

## <bdi dir="ltr">4. Entity</bdi> در برابر <bdi dir="ltr">Value Object</bdi>

| پرسش | <bdi dir="ltr">Entity</bdi> | <bdi dir="ltr">Value Object</bdi> |
|---|---|---|
| هویت مستقل دارد؟ | بله | خیر |
| تغییر <bdi dir="ltr">State</bdi> در زمان مهم است؟ | معمولاً بله | معمولاً با نمونهٔ جدید |
| <bdi dir="ltr">Equality</bdi> | <bdi dir="ltr">Identity</bdi> | <bdi dir="ltr">Value/meaning</bdi> |
| مثال | <bdi dir="ltr">DepositAccount</bdi>، <bdi dir="ltr">LoanAgreement</bdi> | <bdi dir="ltr">Money</bdi>، <bdi dir="ltr">AccountId</bdi>، <bdi dir="ltr">DateRange</bdi> |

<bdi dir="ltr">Typed ID</bdi> خودش <bdi dir="ltr">Value Object</bdi> است اما به <bdi dir="ltr">Entity</bdi> دیگری اشاره می‌کند. <bdi dir="ltr">`AccountId`</bdi> با <bdi dir="ltr">`AccountNumber`</bdi> یکی نیست: اولی شناسهٔ داخلی پایدار، دومی <bdi dir="ltr">Identifier</bdi> کسب‌وکاری/نمایشی با قواعد و <bdi dir="ltr">Lifecycle</bdi> دیگر است.

## 5. طراحی <bdi dir="ltr">Money</bdi>

### اجزای حداقلی

- <bdi dir="ltr">`BigDecimal amount`</bdi>
- <bdi dir="ltr">`Currency currency`</bdi>

### چرا <bdi dir="ltr">`double`</bdi> ممنوع است؟

اعداد ممیز شناور دودویی بسیاری از مقادیر ده‌دهی را دقیق نمایش نمی‌دهند. خطای کوچک برای پول، تجمیع و <bdi dir="ltr">Reconciliation</bdi> قابل‌قبول نیست. <bdi dir="ltr">`BigDecimal`</bdi> نمایش ده‌دهی کنترل‌شده می‌دهد، اما به‌تنهایی همهٔ مسائل را حل نمی‌کند.

### <bdi dir="ltr">Scale</bdi> و <bdi dir="ltr">Equality</bdi>

در <bdi dir="ltr">Java:</bdi>


</div>

<div dir="ltr" align="left">

```java
new BigDecimal("100.0").equals(new BigDecimal("100.00")) // false
new BigDecimal("100.0").compareTo(new BigDecimal("100.00")) // 0
```

</div>

<div dir="rtl" align="right">


اگر <bdi dir="ltr">Equality Money</bdi> باید عددی باشد، <bdi dir="ltr">Implementation</bdi> باید <bdi dir="ltr">Scale</bdi> ظاهری را <bdi dir="ltr">Normalise</bdi> یا با <bdi dir="ltr">`compareTo`</bdi> و <bdi dir="ltr">Hash</bdi> سازگار مدیریت کند. <bdi dir="ltr">`equals`</bdi> و <bdi dir="ltr">`hashCode`</bdi> باید <bdi dir="ltr">Contract</bdi> مشترک داشته باشند؛ فقط <bdi dir="ltr">Override</bdi> کردن <bdi dir="ltr">equals</bdi> کافی نیست.

### <bdi dir="ltr">Currency</bdi>

جمع دو <bdi dir="ltr">Money</bdi> با <bdi dir="ltr">Currency</bdi> متفاوت باید <bdi dir="ltr">Fail-fast</bdi> شود. تبدیل ارز <bdi dir="ltr">Operation</bdi> جدا با <bdi dir="ltr">Rate</bdi>، <bdi dir="ltr">Source</bdi> و <bdi dir="ltr">Timestamp</bdi> است؛ <bdi dir="ltr">`add`</bdi> نباید <bdi dir="ltr">Conversion</bdi> پنهان انجام دهد.

### <bdi dir="ltr">Signed</bdi> یا <bdi dir="ltr">Positive</bdi>؟

<bdi dir="ltr">Money</bdi> عمومی می‌تواند منفی باشد، چون <bdi dir="ltr">Adjustment</bdi>، <bdi dir="ltr">Delta</bdi> و <bdi dir="ltr">Accounting amount</bdi> ممکن است <bdi dir="ltr">Signed</bdi> باشند. اما <bdi dir="ltr">`TransferAmount`</bdi> یا <bdi dir="ltr">Use Case</bdi> انتقال باید مثبت‌بودن را کنترل کند. اگر <bdi dir="ltr">Money</bdi> را همیشه مثبت کنی، شاید <bdi dir="ltr">Reuse</bdi> را محدود کنی؛ اگر همه‌جا <bdi dir="ltr">Signed</bdi> بگذاری، هر <bdi dir="ltr">Use Case</bdi> باید <bdi dir="ltr">Rule</bdi> خودش را اعمال کند. تصمیم را ثبت کن.

### <bdi dir="ltr">Rounding</bdi>

هیچ <bdi dir="ltr">Factory</bdi> یا <bdi dir="ltr">Arithmetic</bdi> نباید بدون <bdi dir="ltr">Policy</bdi> مقدار را <bdi dir="ltr">Round</bdi> کند. <bdi dir="ltr">Operation</bdi> نیازمند <bdi dir="ltr">Rounding</bdi> باید <bdi dir="ltr">Scale</bdi> و <bdi dir="ltr">`RoundingMode`</bdi> یا یک <bdi dir="ltr">Policy</bdi> دامینی صریح دریافت کند.


</div>

<div dir="ltr" align="left">

```java
money.roundedTo(0, RoundingMode.HALF_EVEN)
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Policy Scale</bdi> می‌تواند در <bdi dir="ltr">Product</bdi>، <bdi dir="ltr">Payments</bdi> یا <bdi dir="ltr">Accounting</bdi> متفاوت باشد؛ <bdi dir="ltr">Currency default</bdi> به‌تنهایی همیشه کافی نیست.

## <bdi dir="ltr">6. Typed ID</bdi>ها

اگر همهٔ شناسه‌ها <bdi dir="ltr">`String`</bdi> باشند، <bdi dir="ltr">Compiler</bdi> نمی‌تواند این خطا را بگیرد:


</div>

<div dir="ltr" align="left">

```java
credit(customerId, accountId); // ترتیب اشتباه ولی compile می‌شود
```

</div>

<div dir="rtl" align="right">


با <bdi dir="ltr">Type</bdi>های مستقل:


</div>

<div dir="ltr" align="left">

```java
credit(AccountId accountId, CustomerId customerId);
```

</div>

<div dir="rtl" align="right">


خطای جابه‌جایی پیش از اجرا آشکار می‌شود.

### قواعد طراحی

- مقدار تهی و <bdi dir="ltr">Blank</bdi> رد شود.
- <bdi dir="ltr">Format</bdi> فقط اگر <bdi dir="ltr">Contract</bdi> واقعی دارد <bdi dir="ltr">Validate</bdi> شود؛ <bdi dir="ltr">Regex</bdi> خیالی نساز.
- <bdi dir="ltr">Parsing</bdi> و <bdi dir="ltr">Creation</bdi> معنای روشن داشته باشند.
- <bdi dir="ltr">`toString`</bdi> نباید ناخواسته دادهٔ حساس را در <bdi dir="ltr">Log</bdi> افشا کند.
- <bdi dir="ltr">ID</bdi> داخلی با شمارهٔ بانکی نمایش‌پذیر یکی نشود.

<bdi dir="ltr">Java</bdi> <bdi dir="ltr">`record`</bdi> برای <bdi dir="ltr">Value Object</bdi> کوچک مناسب است، اما <bdi dir="ltr">Compact constructor</bdi> و <bdi dir="ltr">Equality</bdi> پیش‌فرض باید با <bdi dir="ltr">Rule</bdi> سازگار باشند. برای <bdi dir="ltr">Money</bdi>، <bdi dir="ltr">Equality</bdi> پیش‌فرض <bdi dir="ltr">`BigDecimal`</bdi> ممکن است کافی نباشد.

## <bdi dir="ltr">7. Static Factory</bdi>؛ <bdi dir="ltr">Pattern</bdi> یا <bdi dir="ltr">API design</bdi>؟

<bdi dir="ltr">Factory</bdi>هایی مانند <bdi dir="ltr">`Money.of(amount, currency)`</bdi> یا <bdi dir="ltr">`AccountId.parse(text)`</bdi> می‌توانند <bdi dir="ltr">Intent</bdi> و <bdi dir="ltr">Validation</bdi> را روشن کنند. اما ایجاد <bdi dir="ltr">Class</bdi> به نام <bdi dir="ltr">`MoneyFactory`</bdi> بدون <bdi dir="ltr">Decision</bdi> واقعی فقط <bdi dir="ltr">Indirection</bdi> است.

از <bdi dir="ltr">Static Factory</bdi> وقتی استفاده کن که:

- نام <bdi dir="ltr">Creation</bdi> معنا می‌دهد (<bdi dir="ltr">`parse`</bdi>, <bdi dir="ltr">`zero`</bdi>, <bdi dir="ltr">`ofMinorUnits`</bdi>)
- <bdi dir="ltr">Canonicalisation</bdi> یا <bdi dir="ltr">Validation</bdi> لازم است
- <bdi dir="ltr">Constructor</bdi> خام ممکن است <bdi dir="ltr">Contract</bdi> را مبهم کند

از <bdi dir="ltr">Abstract Factory</bdi> یا <bdi dir="ltr">Registry</bdi> در <bdi dir="ltr">Week 01</bdi> استفاده نکن؛ <bdi dir="ltr">Variation</bdi> واقعی وجود ندارد.

## 8. تست‌های لازم

### <bdi dir="ltr">Happy path</bdi>

- ساخت <bdi dir="ltr">Money</bdi> معتبر
- جمع و تفریق <bdi dir="ltr">Currency</bdi> یکسان
- <bdi dir="ltr">Parse</bdi> شناسهٔ معتبر

### <bdi dir="ltr">Equality</bdi>

- <bdi dir="ltr">`100.0 IRR == 100.00 IRR`</bdi>
- مبلغ برابر با <bdi dir="ltr">Currency</bdi> متفاوت، برابر نیست
- <bdi dir="ltr">`hashCode`</bdi> برای <bdi dir="ltr">Money</bdi>های برابر یکسان است

### <bdi dir="ltr">Negative/edge</bdi>

- <bdi dir="ltr">amount/currency null</bdi>
- <bdi dir="ltr">Currency mismatch</bdi>
- <bdi dir="ltr">ID null/blank</bdi>
- نیاز به <bdi dir="ltr">Rounding</bdi> بدون <bdi dir="ltr">Policy</bdi>
- مقدار بسیار بزرگ بدون <bdi dir="ltr">Overflow</bdi> عددی

### <bdi dir="ltr">Compile-time evidence</bdi>

اینکه <bdi dir="ltr">`CustomerId`</bdi> را نمی‌توان جای <bdi dir="ltr">`AccountId`</bdi> داد، تست <bdi dir="ltr">Runtime</bdi> نیست. در <bdi dir="ltr">Workbook</bdi> با <bdi dir="ltr">Signature</bdi> یا <bdi dir="ltr">Compilation evidence</bdi> توضیح داده می‌شود؛ لازم نیست تستی بسازی که پروژه را عمداً <bdi dir="ltr">Fail</bdi> نگه دارد.

## 9. ساختار پیشنهادی <bdi dir="ltr">Package</bdi>

در <bdi dir="ltr">Week 01 Type</bdi>ها را در <bdi dir="ltr">Package</bdi> آموزشی کوچک نگه دار. آن‌ها را سریعاً در <bdi dir="ltr">`common`</bdi> یا <bdi dir="ltr">`shared-kernel`</bdi> سراسری قرار نده. <bdi dir="ltr">Money</bdi> در <bdi dir="ltr">Accounting</bdi> ممکن است <bdi dir="ltr">Policy</bdi> و معنای متفاوتی از <bdi dir="ltr">Payments</bdi> داشته باشد.


</div>

<div dir="ltr" align="left">

```text
com.example.corebankinglab.foundation.money
com.example.corebankinglab.foundation.identity
```

</div>

<div dir="rtl" align="right">


این فقط نقطهٔ شروع است. <bdi dir="ltr">Week 02</bdi> با کشف <bdi dir="ltr">Context</bdi>ها تصمیم <bdi dir="ltr">Shared Kernel</bdi> را نقد می‌کند.

## <bdi dir="ltr">10. Pipeline</bdi> <bdi dir="ltr">`mvn verify`</bdi>

<bdi dir="ltr">Pipeline</bdi> این هفته باید حداقل این زنجیره را اجرا کند:


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


<bdi dir="ltr">Command</bdi> محلی:


</div>

<div dir="ltr" align="left">

```bash
cd backend/banking-modulith
mvn -B -ntp verify
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">`verify`</bdi> فقط سبزبودن فعلی را نشان می‌دهد؛ کیفیت تست و <bdi dir="ltr">Coverage</bdi> معنایی را تضمین نمی‌کند. یک تست که فقط <bdi dir="ltr">Getter</bdi> را می‌خواند شاهد <bdi dir="ltr">Rule</bdi> دامینی نیست.

## 11. ترتیب پیاده‌سازی سبز

1. <bdi dir="ltr">Baseline</bdi> <bdi dir="ltr">`mvn verify`</bdi> را ثبت کن.
2. ابتدا <bdi dir="ltr">`AccountId`</bdi> و <bdi dir="ltr">Test null/blank</bdi> را بساز.
3. سه <bdi dir="ltr">Typed ID</bdi> را با <bdi dir="ltr">Duplication</bdi> کوچک و روشن بساز؛ زود <bdi dir="ltr">Abstract Base</bdi> نساز.
4. <bdi dir="ltr">Money</bdi> را با <bdi dir="ltr">Null/Currency guard</bdi> ایجاد کن.
5. <bdi dir="ltr">Equality</bdi> عددی و <bdi dir="ltr">hashCode</bdi> سازگار را تست کن.
6. <bdi dir="ltr">`add/subtract`</bdi> با <bdi dir="ltr">Currency check</bdi> را اضافه کن.
7. <bdi dir="ltr">Rounding</bdi> صریح و <bdi dir="ltr">Edge test</bdi> را اضافه کن.
8. <bdi dir="ltr">`mvn verify`</bdi> نهایی را ثبت و <bdi dir="ltr">Diff</bdi> را مرور کن.

<bdi dir="ltr">Duplication</bdi> سه <bdi dir="ltr">ID</bdi> در این مرحله ارزان‌تر از <bdi dir="ltr">Hierarchy</bdi> اشتباه و <bdi dir="ltr">Coupling</bdi> سراسری است. بعد از مشاهدهٔ الگو می‌توان تصمیم گرفت.

## 12. خطاهای رایج

- استفاده از <bdi dir="ltr">`double`</bdi> یا <bdi dir="ltr">`float`</bdi>
- <bdi dir="ltr">Setter</bdi> روی <bdi dir="ltr">Money</bdi>
- تبدیل ارز داخل <bdi dir="ltr">`add`</bdi>
- <bdi dir="ltr">`setScale`</bdi> پنهان در <bdi dir="ltr">Constructor</bdi>
- <bdi dir="ltr">Equality</bdi> ناسازگار با <bdi dir="ltr">hashCode</bdi>
- <bdi dir="ltr">Validation</bdi> خیالی برای <bdi dir="ltr">Format ID</bdi>
- استفاده از <bdi dir="ltr">Entity/JPA annotation</bdi> روی <bdi dir="ltr">Value Object</bdi> مستقل
- ایجاد <bdi dir="ltr">`BaseId<T>`</bdi> پیچیده پیش از نیاز
- قرار دادن همهٔ <bdi dir="ltr">Type</bdi>ها در <bdi dir="ltr">`common`</bdi> بدون <bdi dir="ltr">Context owner</bdi>

## 13. تمرین و <bdi dir="ltr">Rubric</bdi>

[<bdi dir="ltr">Day 06 Exercise</bdi>](../exercises/day-06-value-objects.md) را اجرا کن.

| معیار | امتیاز |
|---|---:|
| <bdi dir="ltr">Immutability</bdi> و <bdi dir="ltr">invariant</bdi> ساخت | ۲ |
| <bdi dir="ltr">Equality/hashCode</bdi> صحیح <bdi dir="ltr">Money</bdi> | ۲ |
| <bdi dir="ltr">Currency</bdi> و <bdi dir="ltr">Rounding</bdi> صریح | ۲ |
| <bdi dir="ltr">Typed IDs</bdi> و مرز معنایی | ۲ |
| تست منفی و <bdi dir="ltr">`mvn verify`</bdi> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. استفاده از <bdi dir="ltr">`double`</bdi> یا <bdi dir="ltr">Rounding</bdi> پنهان <bdi dir="ltr">Critical Error</bdi> است.

## 14. آزمون خروج

کد و درس را ببند و [<bdi dir="ltr">Exit Ticket</bdi>](../quizzes/day-06-exit-ticket.md) را پاسخ بده. <bdi dir="ltr">Day 08</bdi> همین <bdi dir="ltr">Type</bdi>ها را در یک <bdi dir="ltr">Refactor</bdi> واقعی به کار می‌گیرد؛ امروز می‌توانی <bdi dir="ltr">Implementation</bdi> خودت را بسازی، اما <bdi dir="ltr">Starter</bdi> روز هشتم راه‌حل کامل را تحمیل نمی‌کند.


</div>
