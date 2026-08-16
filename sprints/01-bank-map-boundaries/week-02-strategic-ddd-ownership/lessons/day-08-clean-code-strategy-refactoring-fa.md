<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 08</span> — <span dir="ltr">Clean Code</span> و <span dir="ltr">Refactoring</span> با <span dir="ltr">Strategy/Factory</span>

- <span dir="ltr">Expansion budget: 105 minutes</span> — <span dir="ltr">25 lesson</span> + <span dir="ltr">65 coding</span> + <span dir="ltr">10 self-review</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output: refactored Transfer Fee kata</span> + <span dir="ltr">tests</span> + <span dir="ltr">Pattern Decision</span> + <span dir="ltr">Code Review</span>
- <span dir="ltr">Code scope: test-only educational fixture</span>
- <span dir="ltr">Banking note:</span> همهٔ نرخ‌ها و <span dir="ltr">Limits</span> این <span dir="ltr">Kata</span> ساختگی‌اند و تعرفهٔ واقعی بانکی نیستند.

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. تفاوت <span dir="ltr">Clean Code</span>، <span dir="ltr">Code Smell</span>، <span dir="ltr">Refactoring</span> و <span dir="ltr">Design Pattern</span> را بدون شعار توضیح بدهی.
2. رفتار کد <span dir="ltr">Legacy</span> را پیش از تغییر با <span dir="ltr">Characterization Test</span> تثبیت کنی.
3. <span dir="ltr">`Magic Literal`</span>، <span dir="ltr">`Primitive Obsession`</span>، <span dir="ltr">`Flag Argument`</span> و مسئولیت‌های مخلوط را در یک مثال بانکی پیدا کنی.
4. تصمیم بگیری آیا <span dir="ltr">Variation</span> نرخ کارمزد واقعاً <span dir="ltr">Strategy</span> را توجیه می‌کند یا یک <span dir="ltr">`switch`</span> خوانا کافی است.
5. در صورت انتخاب <span dir="ltr">Strategy</span>، <span dir="ltr">Selection</span> را با یک <span dir="ltr">Registry/Factory</span> کوچک از <span dir="ltr">Calculation</span> جدا کنی.
6. <span dir="ltr">Refactor</span> را بدون تغییر ناخواستهٔ <span dir="ltr">Rule</span> دامینی و در گام‌های سبز انجام بدهی.
7. هزینهٔ <span dir="ltr">Pattern</span> اضافه‌شده را در <span dir="ltr">Code Review</span> صریح ثبت کنی.

## 2. پیش‌نیاز

- <span dir="ltr">Baseline</span> پروژه با <span dir="ltr">`mvn verify`</span> سبز باشد.
- تفاوت <span dir="ltr">Capability</span>، <span dir="ltr">Domain</span>، <span dir="ltr">Bounded Context</span> و <span dir="ltr">Module</span> را بدانی.
- با <span dir="ltr">Java record</span>، <span dir="ltr">enum</span>، <span dir="ltr">interface</span>، <span dir="ltr">JUnit</span> و <span dir="ltr">Exception</span> آشنا باشی.
- <span dir="ltr">Day 05</span> و <span dir="ltr">Day 06</span> را انجام داده باشی تا <span dir="ltr">Package boundary</span> را با <span dir="ltr">Class design</span> اشتباه نگیری.

## 3. چرا این درس به <span dir="ltr">Week 02</span> اضافه شده است؟

<span dir="ltr">Boundary</span> روی <span dir="ltr">Diagram</span> اگر در کد به <span dir="ltr">Interface</span>های نامفهوم، <span dir="ltr">String</span>های جادویی و <span dir="ltr">`Service`</span>های چندمسئولیتی تبدیل شود، عمر زیادی ندارد. از طرف دیگر، استفادهٔ نمایشی از <span dir="ltr">Pattern</span> نیز <span dir="ltr">Boundary</span> را بهتر نمی‌کند؛ فقط تعداد <span dir="ltr">Type</span>ها را بالا می‌برد.

پس هدف این ریل دوگانه است:


</div>

<div dir="ltr" align="left">

```text
Strategic boundary
  + code that expresses the boundary
  + tests that preserve its rules
  + patterns justified by change pressure
= evolvable architecture
```

</div>

<div dir="rtl" align="right">


این هفته مسئله عمداً کوچک است: محاسبهٔ کارمزد <span dir="ltr">Transfer</span> روی سه <span dir="ltr">Rail</span> فرضی. قرار نیست <span dir="ltr">Fees</span> را به هفتمین <span dir="ltr">Microservice</span> تبدیل کنیم. فقط می‌خواهیم ببینیم چگونه یک <span dir="ltr">Rule</span> متغیر را تمیز، تست‌پذیر و قابل‌دفاع می‌کنیم.

## 4. تعریف‌های دقیق

### <span dir="ltr">Clean Code</span>

کدی که <span dir="ltr">Intent</span> و <span dir="ltr">Rule</span> را برای <span dir="ltr">Maintainer</span> بعدی آشکار می‌کند، تغییر محلی را ممکن می‌سازد و اثر جانبی و <span dir="ltr">Dependency</span> را پنهان نمی‌کند. <span dir="ltr">Clean Code</span> الزاماً کم‌خط‌ترین، پرکلاس‌ترین یا بدون <span dir="ltr">Getter</span>ترین کد نیست.

### <span dir="ltr">Code Smell</span>

نشانه‌ای که احتمال یک مشکل طراحی را بالا می‌برد؛ نه حکم قطعی. <span dir="ltr">`switch`</span> می‌تواند <span dir="ltr">Smell</span> باشد، اما وقتی مجموعهٔ حالت‌ها کوچک، بسته و پایدار است ممکن است از <span dir="ltr">Hierarchy</span> چندکلاسه خواناتر باشد.

### <span dir="ltr">Refactoring</span>

تغییر ساختار داخلی کد بدون تغییر رفتار قابل مشاهده. اگر نرخ <span dir="ltr">ACH</span> را هم‌زمان عوض کنی، آن <span dir="ltr">Commit</span> فقط <span dir="ltr">Refactor</span> نیست؛ تغییر <span dir="ltr">Rule</span> دامینی نیز هست.

### <span dir="ltr">Characterization Test</span>

تستی که رفتار موجود را ثبت می‌کند، حتی اگر ساختار موجود را دوست نداشته باشیم. این تست «صحیح‌بودن تعرفه» را اثبات نمی‌کند؛ فقط مانع تغییر ناخواسته در جریان <span dir="ltr">Refactor</span> می‌شود.

### <span dir="ltr">Strategy</span>

یک خانواده از <span dir="ltr">Algorithm/Policy</span>های قابل جایگزینی پشت یک <span dir="ltr">Contract</span> مشترک. <span dir="ltr">Strategy</span> زمانی مفید است که <span dir="ltr">Rule</span>ها مستقل تغییر کنند، تست جدا بخواهند یا <span dir="ltr">Consumer</span> نباید <span dir="ltr">Selection logic</span> را بداند.

### <span dir="ltr">Factory/Registry</span>

نقطه‌ای که تصمیم می‌گیرد برای یک ورودی کدام <span dir="ltr">Strategy</span> استفاده شود. <span dir="ltr">Registry</span> سادهٔ <span dir="ltr">`Map<PaymentRail, FeePolicy>`</span> برای این <span dir="ltr">Kata</span> معمولاً از <span dir="ltr">Abstract Factory</span> یا <span dir="ltr">Reflection</span> مناسب‌تر است.

## <span dir="ltr">5. Baseline</span> عمداً بد

فایل زیر را باز کن:


</div>

<div dir="ltr" align="left">

```text
backend/banking-modulith/src/test/java/
com/example/corebankinglab/craftsmanship/week02/
LegacyTransferFeeCalculator.java
```

</div>

<div dir="rtl" align="right">


رفتار فعلی:

- <span dir="ltr">`INTERNAL`</span>: بدون کارمزد
- <span dir="ltr">`ACH`</span>: دو ده‌هزارم مبلغ، حداقل ۵۰٬۰۰۰ و حداکثر ۲۵۰٬۰۰۰ ریال
- <span dir="ltr">`RTGS`</span>: مبلغ ثابت ۲۰۰٬۰۰۰ ریال
- مشتری <span dir="ltr">Preferred:</span> نصف کارمزد محاسبه‌شده

این اعداد صرفاً <span dir="ltr">Fixture</span> آموزشی‌اند.

### <span dir="ltr">Smell map</span> اولیه

| محل | <span dir="ltr">Smell</span> | چرا مهم است؟ | آیا اصلاح قطعی است؟ |
|---|---|---|---|
| <span dir="ltr">`String paymentRail`</span> | <span dir="ltr">Primitive Obsession</span> / <span dir="ltr">Type Code</span> | غلط املایی فقط در <span dir="ltr">Runtime</span> دیده می‌شود و <span dir="ltr">Vocabulary</span> پخش می‌شود | معمولاً بله؛ <span dir="ltr">Boundary parser</span> جدا لازم است |
| اعداد داخل <span dir="ltr">Method</span> | <span dir="ltr">Magic Literal</span> | <span dir="ltr">Rule</span> قابل نام‌گذاری، <span dir="ltr">Audit</span> و تغییر مستقل نیست | بله؛ نام و محل مالک لازم است |
| <span dir="ltr">`boolean preferredCustomer`</span> | <span dir="ltr">Flag Argument</span> | <span dir="ltr">Caller</span> باید اثر <span dir="ltr">Boolean</span> را حدس بزند و دو رفتار در یک <span dir="ltr">Signature</span> پنهان می‌شود | اغلب؛ ابتدا <span dir="ltr">Meaning</span> را مدل کن |
| <span dir="ltr">`if/else`</span> <span dir="ltr">Rail</span>ها | <span dir="ltr">Conditional complexity</span> | <span dir="ltr">Selection</span> و <span dir="ltr">Calculation</span> در یک محل تغییر می‌کنند | مشروط؛ شاید <span dir="ltr">Strategy</span>، شاید <span dir="ltr">`switch`</span> تمیز |
| <span dir="ltr">`long amountRials`</span> | <span dir="ltr">Primitive Obsession</span> | <span dir="ltr">Currency/Scale/overflow contract</span> پنهان است | در <span dir="ltr">Domain code</span> بله؛ در <span dir="ltr">Boundary</span> خام ممکن است موقت باشد |
| <span dir="ltr">Validation</span> + <span dir="ltr">Selection</span> + <span dir="ltr">Pricing</span> | <span dir="ltr">Mixed responsibilities</span> | چند دلیل مستقل برای تغییر یک <span dir="ltr">Method</span> | بله، اما نه الزاماً یک <span dir="ltr">Class</span> برای هر خط |
| پیام <span dir="ltr">Exception</span> عمومی | <span dir="ltr">Weak error model</span> | <span dir="ltr">Caller</span> نوع <span dir="ltr">Failure</span> را <span dir="ltr">Machine-readable</span> نمی‌داند | در <span dir="ltr">Product code</span> بله؛ در <span dir="ltr">Kata</span> می‌تواند مرحله‌ای باشد |

<span dir="ltr">Smell map</span> پاسخ نهایی نیست. باید مشخص کنی کدام مورد در ۶۵ دقیقه واقعاً ارزش اصلاح دارد.

## 6. مدل تغییر مورد انتظار

فرض کن این سه <span dir="ltr">Pressure</span> واقعی وجود دارد:

1. تیم <span dir="ltr">Payments Rail</span> جدید اضافه می‌کند.
2. تیم <span dir="ltr">Fees</span> نرخ هر <span dir="ltr">Rail</span> را مستقل و با تاریخ مؤثر تغییر می‌دهد.
3. <span dir="ltr">Product</span> برای <span dir="ltr">Customer segment</span>ها <span dir="ltr">Discount policy</span> جدا دارد.

در این وضعیت سه محور تغییر داریم:


</div>

<div dir="ltr" align="left">

```text
rail selection ── fee calculation ── customer discount
```

</div>

<div dir="rtl" align="right">


اگر همه در یک <span dir="ltr">Method</span> بمانند، هر تغییر ممکن است بقیه را لمس کند. اگر هر محور را بی‌دلیل به ده <span dir="ltr">Interface</span> تبدیل کنیم، <span dir="ltr">Navigation</span> و <span dir="ltr">Cognitive load</span> زیاد می‌شود. هدف پیدا کردن **کوچک‌ترین جداسازی مفید** است.

## 7. مسیر هدایت‌شدهٔ <span dir="ltr">Refactor</span>

### گام 1 — <span dir="ltr">Baseline</span> را اجرا کن


</div>

<div dir="ltr" align="left">

```bash
cd backend/banking-modulith
mvn -Dtest=LegacyTransferFeeCalculatorCharacterizationTest test
```

</div>

<div dir="rtl" align="right">


تعداد <span dir="ltr">Test</span> و نتیجه را ثبت کن. روی <span dir="ltr">Baseline</span> قرمز <span dir="ltr">Refactor</span> نکن.

### گام 2 — شکاف رفتار را پیش از تغییر پیدا کن

حداقل دو رفتار ثبت‌نشده را شناسایی کن. نمونهٔ سؤال، نه پاسخ آماده:

- ورودی <span dir="ltr">Blank</span> چه می‌شود؟
- <span dir="ltr">Preferred</span> روی کارمزد صفر چه اثری دارد؟
- <span dir="ltr">Case sensitivity</span> بخشی از <span dir="ltr">Contract</span> است؟
- ضرب <span dir="ltr">`amountRials * 2`</span> در چه محدوده‌ای <span dir="ltr">overflow</span> می‌کند؟
- <span dir="ltr">Discount</span> قبل از <span dir="ltr">Min/Max</span> اعمال می‌شود یا بعد از آن؟

برای یک مورد <span dir="ltr">Test</span> اضافه کن. اگر <span dir="ltr">Rule</span> نامشخص است، <span dir="ltr">Test</span> را حدس نزن؛ آن را <span dir="ltr">`OPEN`</span> ثبت کن.

### گام 3 — <span dir="ltr">Type Code</span> را در <span dir="ltr">Boundary</span> محصور کن

یک <span dir="ltr">Type</span> معنادار برای <span dir="ltr">Rail</span> بساز. <span dir="ltr">Parse</span> کردن <span dir="ltr">String</span> باید در <span dir="ltr">Boundary</span> انجام شود؛ <span dir="ltr">Core calculation</span> نباید دائماً <span dir="ltr">String</span> را تفسیر کند.

<span dir="ltr">Skeleton</span> مجاز:


</div>

<div dir="ltr" align="left">

```java
enum PaymentRail {
    INTERNAL,
    ACH,
    RTGS
}
```

</div>

<div dir="rtl" align="right">


این هنوز <span dir="ltr">Strategy</span> نیست. پس از این گام تست‌ها باید سبز باشند.

### گام 4 — <span dir="ltr">Magic Literal</span>ها را نام‌گذاری کن

نام باید <span dir="ltr">Business meaning</span> را آشکار کند، نه فقط <span dir="ltr">Unit</span> را:

- ضعیف: <span dir="ltr">`NUMBER_50000`</span>
- بهتر: <span dir="ltr">`ACH_MINIMUM_FEE_RIALS`</span>

اگر <span dir="ltr">Rule</span> به یک <span dir="ltr">Strategy</span> منتقل شد، <span dir="ltr">Constant</span> نیز کنار همان <span dir="ltr">Policy</span> بماند؛ یک <span dir="ltr">`Constants`</span> عمومی نساز.

### گام 5 — ابتدا ساده‌ترین گزینه را امتحان کن

یک <span dir="ltr">`switch`</span> <span dir="ltr">expression</span> کوچک روی <span dir="ltr">enum</span> بساز و <span dir="ltr">Validation</span> را از <span dir="ltr">Selection</span> جدا کن. سپس <span dir="ltr">Diff</span> را ببین. اگر کد اکنون روشن و <span dir="ltr">Change pressure</span> فرضی ضعیف است، همین می‌تواند پاسخ نهایی باشد.


</div>

<div dir="ltr" align="left">

```java
return switch (rail) {
    // policies remain explicit here
};
```

</div>

<div dir="rtl" align="right">


امتیاز این تمرین به استفادهٔ اجباری از <span dir="ltr">Strategy</span> وابسته نیست؛ به کیفیت تصمیم وابسته است.

### گام 6 — در صورت توجیه، <span dir="ltr">Strategy</span> را معرفی کن

<span dir="ltr">Contract</span> باید با زبان <span dir="ltr">Domain</span> حرف بزند و کوچک باشد:


</div>

<div dir="ltr" align="left">

```java
interface TransferFeePolicy {
    long calculateFor(long amountRials);
}
```

</div>

<div dir="rtl" align="right">


این <span dir="ltr">Skeleton</span> پاسخ کامل نیست. باید تصمیم بگیری:

- آیا <span dir="ltr">`long`</span> فعلاً می‌ماند یا <span dir="ltr">`Money`</span> <span dir="ltr">Week 01</span> استفاده می‌شود؟
- آیا <span dir="ltr">Rail</span> بخشی از <span dir="ltr">Strategy</span> است یا فقط <span dir="ltr">Key</span> رجیستری؟
- <span dir="ltr">Discount</span> داخل <span dir="ltr">Strategy</span> است یا یک <span dir="ltr">Policy</span> مستقل بعد از <span dir="ltr">Base fee</span>؟
- <span dir="ltr">Unsupported rail</span> در <span dir="ltr">Parser</span> رد می‌شود یا <span dir="ltr">Registry</span>؟

برای هر <span dir="ltr">Rail</span> فقط وقتی <span dir="ltr">Class</span> جدا بساز که <span dir="ltr">Rule</span> مستقل، نام‌پذیر و قابل‌تست باشد.

### گام 7 — <span dir="ltr">Selection</span> را متمرکز کن

به‌جای <span dir="ltr">`if/else`</span> تکرارشونده در <span dir="ltr">Caller</span>ها، یک <span dir="ltr">Registry/Factory</span> کوچک داشته باش. شرایط قبولی:

- همهٔ <span dir="ltr">Strategy</span>ها هنگام ساخت <span dir="ltr">Registry</span> ثبت شوند.
- <span dir="ltr">Duplicate key</span> یا <span dir="ltr">Missing policy Fail-fast</span> باشد.
- <span dir="ltr">Registry</span> منطق محاسبهٔ کارمزد را مالک نشود.
- <span dir="ltr">Reflection</span>، <span dir="ltr">Classpath scanning</span> یا <span dir="ltr">DI</span> پیچیده برای سه <span dir="ltr">Policy</span> وارد نکن.

### گام 8 — <span dir="ltr">Flag</span> را به مفهوم تبدیل کن

<span dir="ltr">`preferredCustomer=true`</span> نام یک <span dir="ltr">Pricing decision</span> نیست. گزینه‌ها را مقایسه کن:

1. <span dir="ltr">`CustomerPricingProfile`</span> به‌عنوان <span dir="ltr">enum/Value Object</span>
2. <span dir="ltr">`DiscountPolicy`</span> مستقل و قابل <span dir="ltr">Composition</span>
3. دو <span dir="ltr">Method</span> صریح، اگر فقط دو رفتار ثابت داریم

نباید هم‌زمان تمام گزینه‌ها را پیاده‌سازی کنی. یکی را با دلیل انتخاب کن.

### گام 9 — <span dir="ltr">Test</span>ها را بر اساس رفتار سازمان بده

<span dir="ltr">Test name</span> باید <span dir="ltr">Rule</span> را بیان کند، نه <span dir="ltr">Method</span> را:

- ضعیف: <span dir="ltr">`testCalculate2`</span>
- بهتر: <span dir="ltr">`achFeeIsCappedAtTheMaximum`</span>

حداقل این دسته‌ها را نگه دار:

- یک <span dir="ltr">Test</span> مستقل برای هر <span dir="ltr">Rail</span>
- <span dir="ltr">Min/inside/max</span> برای <span dir="ltr">ACH</span>
- <span dir="ltr">Discount behavior</span>
- <span dir="ltr">Unsupported rail</span>
- <span dir="ltr">non-positive amount</span>
- <span dir="ltr">Edge Case</span> انتخابی تو

### گام 10 — <span dir="ltr">Diff</span> را بخوان

پیش از اعلام پایان، پاسخ بده:

- تعداد <span dir="ltr">Branch</span>ها کمتر شد یا فقط جابه‌جا شد؟
- <span dir="ltr">Rule</span>ها نزدیک‌تر به نام دامینی خود هستند؟
- اضافه‌کردن <span dir="ltr">Rail</span> جدید چند فایل را تغییر می‌دهد؟
- آیا یک <span dir="ltr">Class</span> فقط برای عبور دادن یک <span dir="ltr">Method</span> ساخته‌ای؟
- تست‌ها <span dir="ltr">Implementation</span> را قفل کرده‌اند یا <span dir="ltr">Behavior</span> را؟

## <span dir="ltr">8. Strategy</span> یا <span dir="ltr">`switch`</span>؟

| <span dir="ltr">Force</span> | <span dir="ltr">`switch`</span> تمیز | <span dir="ltr">Strategy</span> + <span dir="ltr">Registry</span> |
|---|---|---|
| حالت‌ها کم و بسته‌اند | مناسب | ممکن است <span dir="ltr">Over-design</span> باشد |
| <span dir="ltr">Rule</span>ها مستقل و پرجزئیات‌اند | زود شلوغ می‌شود | مناسب‌تر |
| تیم‌های جدا <span dir="ltr">Rule</span>ها را تغییر می‌دهند | <span dir="ltr">Merge hotspot</span> | <span dir="ltr">Ownership</span> بهتر |
| انتخاب <span dir="ltr">Runtime/Configuration</span> است | پیچیده‌تر | <span dir="ltr">Registry</span> مناسب |
| نیاز به <span dir="ltr">Test</span> جدا برای هر <span dir="ltr">Rule</span> | ممکن ولی متمرکز | طبیعی‌تر |
| <span dir="ltr">Navigation cost</span> مهم است | کمتر | بیشتر |

<span dir="ltr">Pattern Decision</span> باید به <span dir="ltr">Forces</span> همین مسئله پاسخ دهد؛ نه تعریف کتابی <span dir="ltr">Strategy.</span>

## 9. مرز <span dir="ltr">Clean Code</span> و معماری

<span dir="ltr">Refactor</span> این <span dir="ltr">Kata</span> حق ندارد نتیجه‌گیری کند که <span dir="ltr">Fees</span> باید <span dir="ltr">Microservice</span> مستقل باشد. این‌ها سطوح متفاوت‌اند:

| تصمیم | سطح |
|---|---|
| نام <span dir="ltr">Type</span> و <span dir="ltr">Method</span> | <span dir="ltr">Code design</span> |
| <span dir="ltr">Strategy</span> برای <span dir="ltr">Rule</span> متغیر | <span dir="ltr">Object/module design</span> |
| <span dir="ltr">Module API</span> برای محاسبهٔ <span dir="ltr">Fee</span> | <span dir="ltr">Application architecture</span> |
| <span dir="ltr">Bounded Context</span> مستقل <span dir="ltr">Fees</span> | <span dir="ltr">Strategic DDD</span> |
| <span dir="ltr">Deployable Fee Service</span> | <span dir="ltr">Deployment/operational architecture</span> |

تمیزی کد <span dir="ltr">Evidence</span> مفید برای <span dir="ltr">Boundary</span> است، اما به‌تنهایی <span dir="ltr">Boundary</span> کسب‌وکاری یا <span dir="ltr">Deployment</span> را اثبات نمی‌کند.

## 10. تمرین مستقل

[<span dir="ltr">Day 08 Exercise</span>](../exercises/day-08-transfer-fee-refactoring.md) را انجام بده. این درس <span dir="ltr">Skeleton</span> و مسیر را داده است؛ پیاده‌سازی نهایی، نام <span dir="ltr">Type</span>ها و <span dir="ltr">Pattern Decision</span> باید متعلق به تو باشد.

## 11. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| <span dir="ltr">Baseline</span> و <span dir="ltr">Characterization evidence</span> | ۲ |
| <span dir="ltr">Smell Map</span> دقیق و غیرشعاری | ۲ |
| <span dir="ltr">Refactor</span> مرحله‌ای با تست سبز | ۲ |
| <span dir="ltr">Strategy/Factory decision</span> با <span dir="ltr">Alternative</span> و <span dir="ltr">Cost</span> | ۲ |
| <span dir="ltr">Edge Test</span> و <span dir="ltr">Self-review</span> صادقانه | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. استفاده از سه <span dir="ltr">Pattern</span> بدون توضیح <span dir="ltr">Forces</span> حداکثر ۵ می‌گیرد؛ راه‌حل سادهٔ مستدل می‌تواند امتیاز کامل بگیرد.

## 12. آزمون خروج

درس و کد را ببند و [<span dir="ltr">Day 08 Exit Ticket</span>](../quizzes/day-08-exit-ticket.md) را بدون مراجعه پاسخ بده.

## 13. منابع اصلی

- <span dir="ltr">Martin Fowler</span>, *<span dir="ltr">Refactoring</span>, <span dir="ltr">2nd Edition</span>* و [<span dir="ltr">Catalog of Refactorings</span>](https://refactoring.com/catalog/) — برای گام‌های کوچک و حفظ رفتار
- [<span dir="ltr">Replace Conditional with Polymorphism</span>](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html) — گزینه‌ای برای <span dir="ltr">Conditional</span>های دارای <span dir="ltr">Variation</span> واقعی، نه نسخهٔ عمومی همهٔ <span dir="ltr">`switch`</span>ها
- [<span dir="ltr">Tell</span>, <span dir="ltr">Don</span>’<span dir="ltr">t Ask</span>](https://martinfowler.com/bliki/TellDontAsk.html) — برای نزدیک‌کردن رفتار و داده، همراه با هشدار خود <span dir="ltr">Fowler</span> دربارهٔ استفادهٔ افراطی
- <span dir="ltr">Erich Gamma et al.</span>, *<span dir="ltr">Design Patterns</span>* — تعریف <span dir="ltr">Strategy</span> و <span dir="ltr">Factory</span>؛ نام <span dir="ltr">Pattern</span> جای تحلیل <span dir="ltr">Forces</span> را نمی‌گیرد
- <span dir="ltr">Joshua Bloch</span>, *<span dir="ltr">Effective Java</span>, <span dir="ltr">3rd Edition</span>* — <span dir="ltr">Type safety</span>، <span dir="ltr">Immutability</span> و <span dir="ltr">API design</span> در <span dir="ltr">Java</span>

</div>
