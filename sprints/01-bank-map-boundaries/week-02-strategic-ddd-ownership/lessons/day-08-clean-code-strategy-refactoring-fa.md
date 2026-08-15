<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 08</bdi> — <bdi dir="ltr">Clean Code</bdi> و <bdi dir="ltr">Refactoring</bdi> با <bdi dir="ltr">Strategy/Factory</bdi>

- <bdi dir="ltr">Expansion budget: 105 minutes</bdi> — <bdi dir="ltr">25 lesson</bdi> + <bdi dir="ltr">65 coding</bdi> + <bdi dir="ltr">10 self-review</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output: refactored Transfer Fee kata</bdi> + <bdi dir="ltr">tests</bdi> + <bdi dir="ltr">Pattern Decision</bdi> + <bdi dir="ltr">Code Review</bdi>
- <bdi dir="ltr">Code scope: test-only educational fixture</bdi>
- <bdi dir="ltr">Banking note:</bdi> همهٔ نرخ‌ها و <bdi dir="ltr">Limits</bdi> این <bdi dir="ltr">Kata</bdi> ساختگی‌اند و تعرفهٔ واقعی بانکی نیستند.

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. تفاوت <bdi dir="ltr">Clean Code</bdi>، <bdi dir="ltr">Code Smell</bdi>، <bdi dir="ltr">Refactoring</bdi> و <bdi dir="ltr">Design Pattern</bdi> را بدون شعار توضیح بدهی.
2. رفتار کد <bdi dir="ltr">Legacy</bdi> را پیش از تغییر با <bdi dir="ltr">Characterization Test</bdi> تثبیت کنی.
3. <bdi dir="ltr">`Magic Literal`</bdi>، <bdi dir="ltr">`Primitive Obsession`</bdi>، <bdi dir="ltr">`Flag Argument`</bdi> و مسئولیت‌های مخلوط را در یک مثال بانکی پیدا کنی.
4. تصمیم بگیری آیا <bdi dir="ltr">Variation</bdi> نرخ کارمزد واقعاً <bdi dir="ltr">Strategy</bdi> را توجیه می‌کند یا یک <bdi dir="ltr">`switch`</bdi> خوانا کافی است.
5. در صورت انتخاب <bdi dir="ltr">Strategy</bdi>، <bdi dir="ltr">Selection</bdi> را با یک <bdi dir="ltr">Registry/Factory</bdi> کوچک از <bdi dir="ltr">Calculation</bdi> جدا کنی.
6. <bdi dir="ltr">Refactor</bdi> را بدون تغییر ناخواستهٔ <bdi dir="ltr">Rule</bdi> دامینی و در گام‌های سبز انجام بدهی.
7. هزینهٔ <bdi dir="ltr">Pattern</bdi> اضافه‌شده را در <bdi dir="ltr">Code Review</bdi> صریح ثبت کنی.

## 2. پیش‌نیاز

- <bdi dir="ltr">Baseline</bdi> پروژه با <bdi dir="ltr">`mvn verify`</bdi> سبز باشد.
- تفاوت <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Bounded Context</bdi> و <bdi dir="ltr">Module</bdi> را بدانی.
- با <bdi dir="ltr">Java record</bdi>، <bdi dir="ltr">enum</bdi>، <bdi dir="ltr">interface</bdi>، <bdi dir="ltr">JUnit</bdi> و <bdi dir="ltr">Exception</bdi> آشنا باشی.
- <bdi dir="ltr">Day 05</bdi> و <bdi dir="ltr">Day 06</bdi> را انجام داده باشی تا <bdi dir="ltr">Package boundary</bdi> را با <bdi dir="ltr">Class design</bdi> اشتباه نگیری.

## 3. چرا این درس به <bdi dir="ltr">Week 02</bdi> اضافه شده است؟

<bdi dir="ltr">Boundary</bdi> روی <bdi dir="ltr">Diagram</bdi> اگر در کد به <bdi dir="ltr">Interface</bdi>های نامفهوم، <bdi dir="ltr">String</bdi>های جادویی و <bdi dir="ltr">`Service`</bdi>های چندمسئولیتی تبدیل شود، عمر زیادی ندارد. از طرف دیگر، استفادهٔ نمایشی از <bdi dir="ltr">Pattern</bdi> نیز <bdi dir="ltr">Boundary</bdi> را بهتر نمی‌کند؛ فقط تعداد <bdi dir="ltr">Type</bdi>ها را بالا می‌برد.

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


این هفته مسئله عمداً کوچک است: محاسبهٔ کارمزد <bdi dir="ltr">Transfer</bdi> روی سه <bdi dir="ltr">Rail</bdi> فرضی. قرار نیست <bdi dir="ltr">Fees</bdi> را به هفتمین <bdi dir="ltr">Microservice</bdi> تبدیل کنیم. فقط می‌خواهیم ببینیم چگونه یک <bdi dir="ltr">Rule</bdi> متغیر را تمیز، تست‌پذیر و قابل‌دفاع می‌کنیم.

## 4. تعریف‌های دقیق

### <bdi dir="ltr">Clean Code</bdi>

کدی که <bdi dir="ltr">Intent</bdi> و <bdi dir="ltr">Rule</bdi> را برای <bdi dir="ltr">Maintainer</bdi> بعدی آشکار می‌کند، تغییر محلی را ممکن می‌سازد و اثر جانبی و <bdi dir="ltr">Dependency</bdi> را پنهان نمی‌کند. <bdi dir="ltr">Clean Code</bdi> الزاماً کم‌خط‌ترین، پرکلاس‌ترین یا بدون <bdi dir="ltr">Getter</bdi>ترین کد نیست.

### <bdi dir="ltr">Code Smell</bdi>

نشانه‌ای که احتمال یک مشکل طراحی را بالا می‌برد؛ نه حکم قطعی. <bdi dir="ltr">`switch`</bdi> می‌تواند <bdi dir="ltr">Smell</bdi> باشد، اما وقتی مجموعهٔ حالت‌ها کوچک، بسته و پایدار است ممکن است از <bdi dir="ltr">Hierarchy</bdi> چندکلاسه خواناتر باشد.

### <bdi dir="ltr">Refactoring</bdi>

تغییر ساختار داخلی کد بدون تغییر رفتار قابل مشاهده. اگر نرخ <bdi dir="ltr">ACH</bdi> را هم‌زمان عوض کنی، آن <bdi dir="ltr">Commit</bdi> فقط <bdi dir="ltr">Refactor</bdi> نیست؛ تغییر <bdi dir="ltr">Rule</bdi> دامینی نیز هست.

### <bdi dir="ltr">Characterization Test</bdi>

تستی که رفتار موجود را ثبت می‌کند، حتی اگر ساختار موجود را دوست نداشته باشیم. این تست «صحیح‌بودن تعرفه» را اثبات نمی‌کند؛ فقط مانع تغییر ناخواسته در جریان <bdi dir="ltr">Refactor</bdi> می‌شود.

### <bdi dir="ltr">Strategy</bdi>

یک خانواده از <bdi dir="ltr">Algorithm/Policy</bdi>های قابل جایگزینی پشت یک <bdi dir="ltr">Contract</bdi> مشترک. <bdi dir="ltr">Strategy</bdi> زمانی مفید است که <bdi dir="ltr">Rule</bdi>ها مستقل تغییر کنند، تست جدا بخواهند یا <bdi dir="ltr">Consumer</bdi> نباید <bdi dir="ltr">Selection logic</bdi> را بداند.

### <bdi dir="ltr">Factory/Registry</bdi>

نقطه‌ای که تصمیم می‌گیرد برای یک ورودی کدام <bdi dir="ltr">Strategy</bdi> استفاده شود. <bdi dir="ltr">Registry</bdi> سادهٔ <bdi dir="ltr">`Map<PaymentRail, FeePolicy>`</bdi> برای این <bdi dir="ltr">Kata</bdi> معمولاً از <bdi dir="ltr">Abstract Factory</bdi> یا <bdi dir="ltr">Reflection</bdi> مناسب‌تر است.

## <bdi dir="ltr">5. Baseline</bdi> عمداً بد

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

- <bdi dir="ltr">`INTERNAL`</bdi>: بدون کارمزد
- <bdi dir="ltr">`ACH`</bdi>: دو ده‌هزارم مبلغ، حداقل ۵۰٬۰۰۰ و حداکثر ۲۵۰٬۰۰۰ ریال
- <bdi dir="ltr">`RTGS`</bdi>: مبلغ ثابت ۲۰۰٬۰۰۰ ریال
- مشتری <bdi dir="ltr">Preferred:</bdi> نصف کارمزد محاسبه‌شده

این اعداد صرفاً <bdi dir="ltr">Fixture</bdi> آموزشی‌اند.

### <bdi dir="ltr">Smell map</bdi> اولیه

| محل | <bdi dir="ltr">Smell</bdi> | چرا مهم است؟ | آیا اصلاح قطعی است؟ |
|---|---|---|---|
| <bdi dir="ltr">`String paymentRail`</bdi> | <bdi dir="ltr">Primitive Obsession</bdi> / <bdi dir="ltr">Type Code</bdi> | غلط املایی فقط در <bdi dir="ltr">Runtime</bdi> دیده می‌شود و <bdi dir="ltr">Vocabulary</bdi> پخش می‌شود | معمولاً بله؛ <bdi dir="ltr">Boundary parser</bdi> جدا لازم است |
| اعداد داخل <bdi dir="ltr">Method</bdi> | <bdi dir="ltr">Magic Literal</bdi> | <bdi dir="ltr">Rule</bdi> قابل نام‌گذاری، <bdi dir="ltr">Audit</bdi> و تغییر مستقل نیست | بله؛ نام و محل مالک لازم است |
| <bdi dir="ltr">`boolean preferredCustomer`</bdi> | <bdi dir="ltr">Flag Argument</bdi> | <bdi dir="ltr">Caller</bdi> باید اثر <bdi dir="ltr">Boolean</bdi> را حدس بزند و دو رفتار در یک <bdi dir="ltr">Signature</bdi> پنهان می‌شود | اغلب؛ ابتدا <bdi dir="ltr">Meaning</bdi> را مدل کن |
| <bdi dir="ltr">`if/else`</bdi> <bdi dir="ltr">Rail</bdi>ها | <bdi dir="ltr">Conditional complexity</bdi> | <bdi dir="ltr">Selection</bdi> و <bdi dir="ltr">Calculation</bdi> در یک محل تغییر می‌کنند | مشروط؛ شاید <bdi dir="ltr">Strategy</bdi>، شاید <bdi dir="ltr">`switch`</bdi> تمیز |
| <bdi dir="ltr">`long amountRials`</bdi> | <bdi dir="ltr">Primitive Obsession</bdi> | <bdi dir="ltr">Currency/Scale/overflow contract</bdi> پنهان است | در <bdi dir="ltr">Domain code</bdi> بله؛ در <bdi dir="ltr">Boundary</bdi> خام ممکن است موقت باشد |
| <bdi dir="ltr">Validation</bdi> + <bdi dir="ltr">Selection</bdi> + <bdi dir="ltr">Pricing</bdi> | <bdi dir="ltr">Mixed responsibilities</bdi> | چند دلیل مستقل برای تغییر یک <bdi dir="ltr">Method</bdi> | بله، اما نه الزاماً یک <bdi dir="ltr">Class</bdi> برای هر خط |
| پیام <bdi dir="ltr">Exception</bdi> عمومی | <bdi dir="ltr">Weak error model</bdi> | <bdi dir="ltr">Caller</bdi> نوع <bdi dir="ltr">Failure</bdi> را <bdi dir="ltr">Machine-readable</bdi> نمی‌داند | در <bdi dir="ltr">Product code</bdi> بله؛ در <bdi dir="ltr">Kata</bdi> می‌تواند مرحله‌ای باشد |

<bdi dir="ltr">Smell map</bdi> پاسخ نهایی نیست. باید مشخص کنی کدام مورد در ۶۵ دقیقه واقعاً ارزش اصلاح دارد.

## 6. مدل تغییر مورد انتظار

فرض کن این سه <bdi dir="ltr">Pressure</bdi> واقعی وجود دارد:

1. تیم <bdi dir="ltr">Payments Rail</bdi> جدید اضافه می‌کند.
2. تیم <bdi dir="ltr">Fees</bdi> نرخ هر <bdi dir="ltr">Rail</bdi> را مستقل و با تاریخ مؤثر تغییر می‌دهد.
3. <bdi dir="ltr">Product</bdi> برای <bdi dir="ltr">Customer segment</bdi>ها <bdi dir="ltr">Discount policy</bdi> جدا دارد.

در این وضعیت سه محور تغییر داریم:


</div>

<div dir="ltr" align="left">

```text
rail selection ── fee calculation ── customer discount
```

</div>

<div dir="rtl" align="right">


اگر همه در یک <bdi dir="ltr">Method</bdi> بمانند، هر تغییر ممکن است بقیه را لمس کند. اگر هر محور را بی‌دلیل به ده <bdi dir="ltr">Interface</bdi> تبدیل کنیم، <bdi dir="ltr">Navigation</bdi> و <bdi dir="ltr">Cognitive load</bdi> زیاد می‌شود. هدف پیدا کردن **کوچک‌ترین جداسازی مفید** است.

## 7. مسیر هدایت‌شدهٔ <bdi dir="ltr">Refactor</bdi>

### گام 1 — <bdi dir="ltr">Baseline</bdi> را اجرا کن


</div>

<div dir="ltr" align="left">

```bash
cd backend/banking-modulith
mvn -Dtest=LegacyTransferFeeCalculatorCharacterizationTest test
```

</div>

<div dir="rtl" align="right">


تعداد <bdi dir="ltr">Test</bdi> و نتیجه را ثبت کن. روی <bdi dir="ltr">Baseline</bdi> قرمز <bdi dir="ltr">Refactor</bdi> نکن.

### گام 2 — شکاف رفتار را پیش از تغییر پیدا کن

حداقل دو رفتار ثبت‌نشده را شناسایی کن. نمونهٔ سؤال، نه پاسخ آماده:

- ورودی <bdi dir="ltr">Blank</bdi> چه می‌شود؟
- <bdi dir="ltr">Preferred</bdi> روی کارمزد صفر چه اثری دارد؟
- <bdi dir="ltr">Case sensitivity</bdi> بخشی از <bdi dir="ltr">Contract</bdi> است؟
- ضرب <bdi dir="ltr">`amountRials * 2`</bdi> در چه محدوده‌ای <bdi dir="ltr">overflow</bdi> می‌کند؟
- <bdi dir="ltr">Discount</bdi> قبل از <bdi dir="ltr">Min/Max</bdi> اعمال می‌شود یا بعد از آن؟

برای یک مورد <bdi dir="ltr">Test</bdi> اضافه کن. اگر <bdi dir="ltr">Rule</bdi> نامشخص است، <bdi dir="ltr">Test</bdi> را حدس نزن؛ آن را <bdi dir="ltr">`OPEN`</bdi> ثبت کن.

### گام 3 — <bdi dir="ltr">Type Code</bdi> را در <bdi dir="ltr">Boundary</bdi> محصور کن

یک <bdi dir="ltr">Type</bdi> معنادار برای <bdi dir="ltr">Rail</bdi> بساز. <bdi dir="ltr">Parse</bdi> کردن <bdi dir="ltr">String</bdi> باید در <bdi dir="ltr">Boundary</bdi> انجام شود؛ <bdi dir="ltr">Core calculation</bdi> نباید دائماً <bdi dir="ltr">String</bdi> را تفسیر کند.

<bdi dir="ltr">Skeleton</bdi> مجاز:


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


این هنوز <bdi dir="ltr">Strategy</bdi> نیست. پس از این گام تست‌ها باید سبز باشند.

### گام 4 — <bdi dir="ltr">Magic Literal</bdi>ها را نام‌گذاری کن

نام باید <bdi dir="ltr">Business meaning</bdi> را آشکار کند، نه فقط <bdi dir="ltr">Unit</bdi> را:

- ضعیف: <bdi dir="ltr">`NUMBER_50000`</bdi>
- بهتر: <bdi dir="ltr">`ACH_MINIMUM_FEE_RIALS`</bdi>

اگر <bdi dir="ltr">Rule</bdi> به یک <bdi dir="ltr">Strategy</bdi> منتقل شد، <bdi dir="ltr">Constant</bdi> نیز کنار همان <bdi dir="ltr">Policy</bdi> بماند؛ یک <bdi dir="ltr">`Constants`</bdi> عمومی نساز.

### گام 5 — ابتدا ساده‌ترین گزینه را امتحان کن

یک <bdi dir="ltr">`switch`</bdi> <bdi dir="ltr">expression</bdi> کوچک روی <bdi dir="ltr">enum</bdi> بساز و <bdi dir="ltr">Validation</bdi> را از <bdi dir="ltr">Selection</bdi> جدا کن. سپس <bdi dir="ltr">Diff</bdi> را ببین. اگر کد اکنون روشن و <bdi dir="ltr">Change pressure</bdi> فرضی ضعیف است، همین می‌تواند پاسخ نهایی باشد.


</div>

<div dir="ltr" align="left">

```java
return switch (rail) {
    // policies remain explicit here
};
```

</div>

<div dir="rtl" align="right">


امتیاز این تمرین به استفادهٔ اجباری از <bdi dir="ltr">Strategy</bdi> وابسته نیست؛ به کیفیت تصمیم وابسته است.

### گام 6 — در صورت توجیه، <bdi dir="ltr">Strategy</bdi> را معرفی کن

<bdi dir="ltr">Contract</bdi> باید با زبان <bdi dir="ltr">Domain</bdi> حرف بزند و کوچک باشد:


</div>

<div dir="ltr" align="left">

```java
interface TransferFeePolicy {
    long calculateFor(long amountRials);
}
```

</div>

<div dir="rtl" align="right">


این <bdi dir="ltr">Skeleton</bdi> پاسخ کامل نیست. باید تصمیم بگیری:

- آیا <bdi dir="ltr">`long`</bdi> فعلاً می‌ماند یا <bdi dir="ltr">`Money`</bdi> <bdi dir="ltr">Week 01</bdi> استفاده می‌شود؟
- آیا <bdi dir="ltr">Rail</bdi> بخشی از <bdi dir="ltr">Strategy</bdi> است یا فقط <bdi dir="ltr">Key</bdi> رجیستری؟
- <bdi dir="ltr">Discount</bdi> داخل <bdi dir="ltr">Strategy</bdi> است یا یک <bdi dir="ltr">Policy</bdi> مستقل بعد از <bdi dir="ltr">Base fee</bdi>؟
- <bdi dir="ltr">Unsupported rail</bdi> در <bdi dir="ltr">Parser</bdi> رد می‌شود یا <bdi dir="ltr">Registry</bdi>؟

برای هر <bdi dir="ltr">Rail</bdi> فقط وقتی <bdi dir="ltr">Class</bdi> جدا بساز که <bdi dir="ltr">Rule</bdi> مستقل، نام‌پذیر و قابل‌تست باشد.

### گام 7 — <bdi dir="ltr">Selection</bdi> را متمرکز کن

به‌جای <bdi dir="ltr">`if/else`</bdi> تکرارشونده در <bdi dir="ltr">Caller</bdi>ها، یک <bdi dir="ltr">Registry/Factory</bdi> کوچک داشته باش. شرایط قبولی:

- همهٔ <bdi dir="ltr">Strategy</bdi>ها هنگام ساخت <bdi dir="ltr">Registry</bdi> ثبت شوند.
- <bdi dir="ltr">Duplicate key</bdi> یا <bdi dir="ltr">Missing policy Fail-fast</bdi> باشد.
- <bdi dir="ltr">Registry</bdi> منطق محاسبهٔ کارمزد را مالک نشود.
- <bdi dir="ltr">Reflection</bdi>، <bdi dir="ltr">Classpath scanning</bdi> یا <bdi dir="ltr">DI</bdi> پیچیده برای سه <bdi dir="ltr">Policy</bdi> وارد نکن.

### گام 8 — <bdi dir="ltr">Flag</bdi> را به مفهوم تبدیل کن

<bdi dir="ltr">`preferredCustomer=true`</bdi> نام یک <bdi dir="ltr">Pricing decision</bdi> نیست. گزینه‌ها را مقایسه کن:

1. <bdi dir="ltr">`CustomerPricingProfile`</bdi> به‌عنوان <bdi dir="ltr">enum/Value Object</bdi>
2. <bdi dir="ltr">`DiscountPolicy`</bdi> مستقل و قابل <bdi dir="ltr">Composition</bdi>
3. دو <bdi dir="ltr">Method</bdi> صریح، اگر فقط دو رفتار ثابت داریم

نباید هم‌زمان تمام گزینه‌ها را پیاده‌سازی کنی. یکی را با دلیل انتخاب کن.

### گام 9 — <bdi dir="ltr">Test</bdi>ها را بر اساس رفتار سازمان بده

<bdi dir="ltr">Test name</bdi> باید <bdi dir="ltr">Rule</bdi> را بیان کند، نه <bdi dir="ltr">Method</bdi> را:

- ضعیف: <bdi dir="ltr">`testCalculate2`</bdi>
- بهتر: <bdi dir="ltr">`achFeeIsCappedAtTheMaximum`</bdi>

حداقل این دسته‌ها را نگه دار:

- یک <bdi dir="ltr">Test</bdi> مستقل برای هر <bdi dir="ltr">Rail</bdi>
- <bdi dir="ltr">Min/inside/max</bdi> برای <bdi dir="ltr">ACH</bdi>
- <bdi dir="ltr">Discount behavior</bdi>
- <bdi dir="ltr">Unsupported rail</bdi>
- <bdi dir="ltr">non-positive amount</bdi>
- <bdi dir="ltr">Edge Case</bdi> انتخابی تو

### گام 10 — <bdi dir="ltr">Diff</bdi> را بخوان

پیش از اعلام پایان، پاسخ بده:

- تعداد <bdi dir="ltr">Branch</bdi>ها کمتر شد یا فقط جابه‌جا شد؟
- <bdi dir="ltr">Rule</bdi>ها نزدیک‌تر به نام دامینی خود هستند؟
- اضافه‌کردن <bdi dir="ltr">Rail</bdi> جدید چند فایل را تغییر می‌دهد؟
- آیا یک <bdi dir="ltr">Class</bdi> فقط برای عبور دادن یک <bdi dir="ltr">Method</bdi> ساخته‌ای؟
- تست‌ها <bdi dir="ltr">Implementation</bdi> را قفل کرده‌اند یا <bdi dir="ltr">Behavior</bdi> را؟

## <bdi dir="ltr">8. Strategy</bdi> یا <bdi dir="ltr">`switch`</bdi>؟

| <bdi dir="ltr">Force</bdi> | <bdi dir="ltr">`switch`</bdi> تمیز | <bdi dir="ltr">Strategy</bdi> + <bdi dir="ltr">Registry</bdi> |
|---|---|---|
| حالت‌ها کم و بسته‌اند | مناسب | ممکن است <bdi dir="ltr">Over-design</bdi> باشد |
| <bdi dir="ltr">Rule</bdi>ها مستقل و پرجزئیات‌اند | زود شلوغ می‌شود | مناسب‌تر |
| تیم‌های جدا <bdi dir="ltr">Rule</bdi>ها را تغییر می‌دهند | <bdi dir="ltr">Merge hotspot</bdi> | <bdi dir="ltr">Ownership</bdi> بهتر |
| انتخاب <bdi dir="ltr">Runtime/Configuration</bdi> است | پیچیده‌تر | <bdi dir="ltr">Registry</bdi> مناسب |
| نیاز به <bdi dir="ltr">Test</bdi> جدا برای هر <bdi dir="ltr">Rule</bdi> | ممکن ولی متمرکز | طبیعی‌تر |
| <bdi dir="ltr">Navigation cost</bdi> مهم است | کمتر | بیشتر |

<bdi dir="ltr">Pattern Decision</bdi> باید به <bdi dir="ltr">Forces</bdi> همین مسئله پاسخ دهد؛ نه تعریف کتابی <bdi dir="ltr">Strategy.</bdi>

## 9. مرز <bdi dir="ltr">Clean Code</bdi> و معماری

<bdi dir="ltr">Refactor</bdi> این <bdi dir="ltr">Kata</bdi> حق ندارد نتیجه‌گیری کند که <bdi dir="ltr">Fees</bdi> باید <bdi dir="ltr">Microservice</bdi> مستقل باشد. این‌ها سطوح متفاوت‌اند:

| تصمیم | سطح |
|---|---|
| نام <bdi dir="ltr">Type</bdi> و <bdi dir="ltr">Method</bdi> | <bdi dir="ltr">Code design</bdi> |
| <bdi dir="ltr">Strategy</bdi> برای <bdi dir="ltr">Rule</bdi> متغیر | <bdi dir="ltr">Object/module design</bdi> |
| <bdi dir="ltr">Module API</bdi> برای محاسبهٔ <bdi dir="ltr">Fee</bdi> | <bdi dir="ltr">Application architecture</bdi> |
| <bdi dir="ltr">Bounded Context</bdi> مستقل <bdi dir="ltr">Fees</bdi> | <bdi dir="ltr">Strategic DDD</bdi> |
| <bdi dir="ltr">Deployable Fee Service</bdi> | <bdi dir="ltr">Deployment/operational architecture</bdi> |

تمیزی کد <bdi dir="ltr">Evidence</bdi> مفید برای <bdi dir="ltr">Boundary</bdi> است، اما به‌تنهایی <bdi dir="ltr">Boundary</bdi> کسب‌وکاری یا <bdi dir="ltr">Deployment</bdi> را اثبات نمی‌کند.

## 10. تمرین مستقل

[<bdi dir="ltr">Day 08 Exercise</bdi>](../exercises/day-08-transfer-fee-refactoring.md) را انجام بده. این درس <bdi dir="ltr">Skeleton</bdi> و مسیر را داده است؛ پیاده‌سازی نهایی، نام <bdi dir="ltr">Type</bdi>ها و <bdi dir="ltr">Pattern Decision</bdi> باید متعلق به تو باشد.

## 11. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| <bdi dir="ltr">Baseline</bdi> و <bdi dir="ltr">Characterization evidence</bdi> | ۲ |
| <bdi dir="ltr">Smell Map</bdi> دقیق و غیرشعاری | ۲ |
| <bdi dir="ltr">Refactor</bdi> مرحله‌ای با تست سبز | ۲ |
| <bdi dir="ltr">Strategy/Factory decision</bdi> با <bdi dir="ltr">Alternative</bdi> و <bdi dir="ltr">Cost</bdi> | ۲ |
| <bdi dir="ltr">Edge Test</bdi> و <bdi dir="ltr">Self-review</bdi> صادقانه | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. استفاده از سه <bdi dir="ltr">Pattern</bdi> بدون توضیح <bdi dir="ltr">Forces</bdi> حداکثر ۵ می‌گیرد؛ راه‌حل سادهٔ مستدل می‌تواند امتیاز کامل بگیرد.

## 12. آزمون خروج

درس و کد را ببند و [<bdi dir="ltr">Day 08 Exit Ticket</bdi>](../quizzes/day-08-exit-ticket.md) را بدون مراجعه پاسخ بده.

## 13. منابع اصلی

- <bdi dir="ltr">Martin Fowler</bdi>, *<bdi dir="ltr">Refactoring</bdi>, <bdi dir="ltr">2nd Edition</bdi>* و [<bdi dir="ltr">Catalog of Refactorings</bdi>](https://refactoring.com/catalog/) — برای گام‌های کوچک و حفظ رفتار
- [<bdi dir="ltr">Replace Conditional with Polymorphism</bdi>](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html) — گزینه‌ای برای <bdi dir="ltr">Conditional</bdi>های دارای <bdi dir="ltr">Variation</bdi> واقعی، نه نسخهٔ عمومی همهٔ <bdi dir="ltr">`switch`</bdi>ها
- [<bdi dir="ltr">Tell</bdi>, <bdi dir="ltr">Don</bdi>’<bdi dir="ltr">t Ask</bdi>](https://martinfowler.com/bliki/TellDontAsk.html) — برای نزدیک‌کردن رفتار و داده، همراه با هشدار خود <bdi dir="ltr">Fowler</bdi> دربارهٔ استفادهٔ افراطی
- <bdi dir="ltr">Erich Gamma et al.</bdi>, *<bdi dir="ltr">Design Patterns</bdi>* — تعریف <bdi dir="ltr">Strategy</bdi> و <bdi dir="ltr">Factory</bdi>؛ نام <bdi dir="ltr">Pattern</bdi> جای تحلیل <bdi dir="ltr">Forces</bdi> را نمی‌گیرد
- <bdi dir="ltr">Joshua Bloch</bdi>, *<bdi dir="ltr">Effective Java</bdi>, <bdi dir="ltr">3rd Edition</bdi>* — <bdi dir="ltr">Type safety</bdi>، <bdi dir="ltr">Immutability</bdi> و <bdi dir="ltr">API design</bdi> در <bdi dir="ltr">Java</bdi>

</div>
