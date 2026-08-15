<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 08</bdi> — <bdi dir="ltr">Clean Code</bdi> و <bdi dir="ltr">Refactoring</bdi> از <bdi dir="ltr">Primitive</bdi> به <bdi dir="ltr">Value Object</bdi>

- <bdi dir="ltr">Expansion budget: 105 minutes</bdi> — <bdi dir="ltr">25 lesson</bdi> + <bdi dir="ltr">65 coding</bdi> + <bdi dir="ltr">10 self-review</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output: Refactored Transfer Request kata</bdi> + <bdi dir="ltr">tests</bdi> + <bdi dir="ltr">Pattern Decision</bdi> + <bdi dir="ltr">Code Review</bdi>
- <bdi dir="ltr">Code scope: Test-only educational fixture</bdi>
- <bdi dir="ltr">Banking note:</bdi> شناسه‌ها و قواعد این <bdi dir="ltr">Kata</bdi> ساختگی‌اند و <bdi dir="ltr">Contract</bdi> واقعی بانک محسوب نمی‌شوند.

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">`Primitive Obsession`</bdi>، <bdi dir="ltr">`Data Clump`</bdi>، <bdi dir="ltr">`Long Parameter List`</bdi> و <bdi dir="ltr">Validation</bdi> پراکنده را با محل و اثر تغییر شناسایی کنی.
2. رفتار کد موجود را پیش از <bdi dir="ltr">Refactor</bdi> با <bdi dir="ltr">Characterization Test</bdi> تثبیت کنی.
3. <bdi dir="ltr">`Money`</bdi> و <bdi dir="ltr">Typed ID</bdi>ها را مرحله‌ای و بدون تغییر ناخواستهٔ رفتار معرفی کنی.
4. بین <bdi dir="ltr">Constructor</bdi>، <bdi dir="ltr">Static Factory</bdi> و <bdi dir="ltr">Factory class</bdi> تصمیم مستدل بگیری.
5. تفاوت <bdi dir="ltr">Refactor</bdi> با تغییر <bdi dir="ltr">Rule</bdi> دامینی را در <bdi dir="ltr">Commit</bdi> و <bdi dir="ltr">Test</bdi> حفظ کنی.
6. هزینهٔ <bdi dir="ltr">Type</bdi> و <bdi dir="ltr">Abstraction</bdi> تازه را صریح در <bdi dir="ltr">Code Review</bdi> ثبت کنی.

## 2. پیش‌نیاز

- <bdi dir="ltr">Day 01</bdi> تا <bdi dir="ltr">Day 07</bdi> هستهٔ <bdi dir="ltr">Week 01</bdi> انجام شده باشد.
- <bdi dir="ltr">Baseline</bdi> کل پروژه با <bdi dir="ltr">`mvn verify`</bdi> سبز باشد.
- <bdi dir="ltr">Contract</bdi> طراحی <bdi dir="ltr">Money</bdi> در <bdi dir="ltr">Day 06</bdi> را خوانده باشی.
- با <bdi dir="ltr">Java record/class</bdi>، <bdi dir="ltr">`BigDecimal`</bdi>، <bdi dir="ltr">`Currency`</bdi> و <bdi dir="ltr">JUnit</bdi> آشنا باشی.

## 3. چهار اصطلاحی که نباید یکی شوند

### <bdi dir="ltr">Clean Code</bdi>

کدی که <bdi dir="ltr">Intent</bdi> و <bdi dir="ltr">Rule</bdi> را آشکار می‌کند، تغییر مرتبط را محلی نگه می‌دارد، خطای نامعتبر را زود متوقف می‌کند و <bdi dir="ltr">Dependency/Side effect</bdi> را پنهان نمی‌سازد. <bdi dir="ltr">Clean Code</bdi> الزاماً کوتاه‌ترین یا پرکلاس‌ترین کد نیست.

### <bdi dir="ltr">Code Smell</bdi>

نشانه‌ای که احتمال مشکل طراحی را بالا می‌برد؛ نه حکم قطعی. <bdi dir="ltr">Long Parameter List</bdi> می‌تواند نشان دهد چند مفهوم در <bdi dir="ltr">Primitive</bdi>ها پنهان شده‌اند، اما ایجاد یک <bdi dir="ltr">Object</bdi> بزرگ <bdi dir="ltr">`RequestContext`</bdi> برای همهٔ پارامترها ممکن است مشکل را بدتر کند.

### <bdi dir="ltr">Refactoring</bdi>

تغییر ساختار داخلی بدون تغییر رفتار قابل مشاهده. اگر هم‌زمان مبلغ صفر را از مجاز به نامجاز تبدیل کنی، آن <bdi dir="ltr">Commit</bdi> فقط <bdi dir="ltr">Refactor</bdi> نیست؛ <bdi dir="ltr">Rule change</bdi> نیز هست.

### <bdi dir="ltr">Design Pattern</bdi>

راه‌حل نام‌دار برای <bdi dir="ltr">Forces</bdi> تکرارشونده. <bdi dir="ltr">Pattern</bdi> جایگزین تحلیل نیست. <bdi dir="ltr">Value Object</bdi> از الگوهای <bdi dir="ltr">DDD</bdi> است؛ <bdi dir="ltr">Static Factory</bdi> یک <bdi dir="ltr">API/creation idiom</bdi> است. ساخت <bdi dir="ltr">Factory hierarchy</bdi> فقط برای اینکه «<bdi dir="ltr">Design Pattern</bdi> استفاده شود» مردود است.

## <bdi dir="ltr">4. Baseline</bdi> عمداً <bdi dir="ltr">Primitive</bdi>

<bdi dir="ltr">Starter</bdi> این <bdi dir="ltr">Week</bdi> یک <bdi dir="ltr">Transfer Request</bdi> کوچک دارد:


</div>

<div dir="ltr" align="left">

```java
new PrimitiveTransferRequest(
    "ACC-1001",
    "ACC-2002",
    "CUS-77",
    "BR-001",
    new BigDecimal("125000.00"),
    "IRR"
);
```

</div>

<div dir="rtl" align="right">


مشکل فقط تعداد پارامترها نیست. کد برای فهمیدن معنا به نام متغیر و ترتیب وابسته است:

- <bdi dir="ltr">Source</bdi> و <bdi dir="ltr">target</bdi> هر دو <bdi dir="ltr">String</bdi> و قابل‌جابه‌جایی‌اند.
- <bdi dir="ltr">Customer</bdi> و <bdi dir="ltr">Branch</bdi> نیز <bdi dir="ltr">String</bdi> هستند.
- <bdi dir="ltr">Amount</bdi> و <bdi dir="ltr">Currency</bdi> یک <bdi dir="ltr">Data Clump</bdi> تکرارشونده‌اند.
- <bdi dir="ltr">Validation</bdi> در <bdi dir="ltr">Constructor</bdi> پراکنده است.
- <bdi dir="ltr">Equality</bdi> عددی <bdi dir="ltr">`BigDecimal`</bdi> و <bdi dir="ltr">Currency semantics</bdi> روشن نیست.
- <bdi dir="ltr">`auditKey`</bdi> با <bdi dir="ltr">Concatenation Representation</bdi> داخلی می‌سازد.

بااین‌حال <bdi dir="ltr">Baseline</bdi> یک رفتار موجود دارد. قبل از تغییر باید بدانیم چه چیزی را حفظ می‌کنیم و چه چیزی <bdi dir="ltr">`OPEN`</bdi> است.

## <bdi dir="ltr">5. Characterization Test</bdi> چیست؟

<bdi dir="ltr">Characterization Test</bdi> رفتار فعلی سیستم را ثبت می‌کند، حتی اگر رفتار ایده‌آل نباشد. هدف ابتدا ایجاد <bdi dir="ltr">Safety net</bdi> است.

<bdi dir="ltr">Starter</bdi> این رفتارها را ثبت می‌کند:

- <bdi dir="ltr">Request</bdi> معتبر ساخته می‌شود.
- <bdi dir="ltr">Source</bdi> و <bdi dir="ltr">target</bdi> یکسان رد می‌شود.
- مبلغ <bdi dir="ltr">null</bdi>، صفر و منفی رد می‌شود.
- <bdi dir="ltr">Currency blank</bdi> رد می‌شود.
- مقدار <bdi dir="ltr">Amount</bdi> همان <bdi dir="ltr">Scale</bdi> ورودی را نگه می‌دارد.
- <bdi dir="ltr">Audit key</bdi> از فیلدهای فعلی ساخته می‌شود.

این تست‌ها نمی‌گویند همهٔ <bdi dir="ltr">Rules</bdi> درست‌اند. اگر <bdi dir="ltr">Format</bdi> شناسه‌ها هیچ <bdi dir="ltr">Contract</bdi> رسمی ندارد، <bdi dir="ltr">Test</bdi> نباید <bdi dir="ltr">Regex</bdi> خیالی را تثبیت کند.

## <bdi dir="ltr">6. Smell Map</bdi> باید <bdi dir="ltr">Concrete</bdi> باشد

<bdi dir="ltr">Smell map</bdi> ضعیف:

> <bdi dir="ltr">SOLID</bdi> رعایت نشده و کد تمیز نیست.

<bdi dir="ltr">Smell map</bdi> قابل‌استفاده:

| <bdi dir="ltr">Symbol</bdi> | <bdi dir="ltr">Smell</bdi> | <bdi dir="ltr">Change risk</bdi> | <bdi dir="ltr">Smallest safe move</bdi> |
|---|---|---|---|
| <bdi dir="ltr">constructor parameters</bdi> | <bdi dir="ltr">Long Parameter List</bdi> + <bdi dir="ltr">Primitive Obsession</bdi> | جابه‌جایی شناسه‌ها <bdi dir="ltr">Compile</bdi> می‌شود | معرفی یک <bdi dir="ltr">Typed ID</bdi> در هر گام |
| <bdi dir="ltr">amount</bdi> + <bdi dir="ltr">currency</bdi> | <bdi dir="ltr">Data Clump</bdi> | <bdi dir="ltr">Validation/operation</bdi> تکراری | استخراج <bdi dir="ltr">Money</bdi> پس از <bdi dir="ltr">Characterization</bdi> |
| <bdi dir="ltr">string guards</bdi> | <bdi dir="ltr">Scattered validation</bdi> | <bdi dir="ltr">Rule</bdi>ها با هم ناسازگار می‌شوند | <bdi dir="ltr">Guard</bdi> داخل <bdi dir="ltr">Value Object</bdi> مرتبط |
| <bdi dir="ltr">auditKey</bdi> | <bdi dir="ltr">Representation leak</bdi> | تغییر <bdi dir="ltr">Format</bdi> مصرف‌کننده را می‌شکند | نام‌گذاری <bdi dir="ltr">Contract</bdi> یا نگه‌داشتن <bdi dir="ltr">Adapter</bdi> |

<bdi dir="ltr">Smell</bdi> باید <bdi dir="ltr">Location</bdi>، نشانه و اثر واقعی داشته باشد.

## 7. مسیر <bdi dir="ltr">Refactor</bdi> مرحله‌ای

### گام 0 — <bdi dir="ltr">Baseline</bdi> کل پروژه


</div>

<div dir="ltr" align="left">

```bash
cd backend/banking-modulith
mvn -B -ntp verify
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Commit/SHA</bdi>، تعداد تست و نتیجه را ثبت کن.

### گام 1 — تست <bdi dir="ltr">Edge</bdi> تازه

یکی از <bdi dir="ltr">Unknown</bdi>ها را انتخاب کن:

- <bdi dir="ltr">Currency</bdi> با حروف کوچک
- <bdi dir="ltr">Whitespace</bdi> اطراف <bdi dir="ltr">ID</bdi>
- مبلغ با <bdi dir="ltr">Scale</bdi> بسیار بزرگ
- <bdi dir="ltr">Audit key</bdi> در صورت وجود <bdi dir="ltr">delimiter</bdi> داخل <bdi dir="ltr">ID</bdi>
- <bdi dir="ltr">Source/target</bdi> که فقط در <bdi dir="ltr">whitespace</bdi> فرق دارند

اگر <bdi dir="ltr">Expected behavior</bdi> از <bdi dir="ltr">Baseline</bdi> یا <bdi dir="ltr">Requirement</bdi> قابل استنتاج نیست، آن را <bdi dir="ltr">`OPEN`</bdi> نگه دار و <bdi dir="ltr">Edge</bdi> دیگری را تست کن. <bdi dir="ltr">Rule</bdi> بانکی را حدس نزن.

### گام 2 — <bdi dir="ltr">`AccountId`</bdi>

فقط <bdi dir="ltr">Source/target</bdi> را <bdi dir="ltr">Type-safe</bdi> کن. تست‌ها سبز شوند. هنوز <bdi dir="ltr">Customer/Branch</bdi> و <bdi dir="ltr">Money</bdi> را تغییر نده. این کار <bdi dir="ltr">Diff</bdi> را کوچک و علت <bdi dir="ltr">Failure</bdi> را روشن نگه می‌دارد.

### گام 3 — <bdi dir="ltr">`CustomerId`</bdi> و <bdi dir="ltr">`BranchId`</bdi>

سه <bdi dir="ltr">Type</bdi> مشابه ممکن است کمی <bdi dir="ltr">Duplication</bdi> داشته باشند. فعلاً <bdi dir="ltr">`AbstractStringId<T>`</bdi> نساز. هنوز نمی‌دانیم <bdi dir="ltr">Validation</bdi> و نمایش آن‌ها واقعاً یکسان است.

### گام 4 — <bdi dir="ltr">`Money`</bdi>

<bdi dir="ltr">Amount</bdi> و <bdi dir="ltr">Currency</bdi> را کنار هم قرار بده. <bdi dir="ltr">Validation null/blank</bdi> به <bdi dir="ltr">Money</bdi> منتقل شود. <bdi dir="ltr">Rule</bdi> مثبت‌بودن را آگاهانه انتخاب کن:

- <bdi dir="ltr">Option A: Money</bdi> عمومی <bdi dir="ltr">Signed</bdi>؛ <bdi dir="ltr">`TransferAmount`</bdi>/<bdi dir="ltr">Request</bdi> مثبت‌بودن را کنترل کند.
- <bdi dir="ltr">Option B:</bdi> این <bdi dir="ltr">Kata</bdi> یک <bdi dir="ltr">Money</bdi> محدود به انتقال بسازد؛ نام <bdi dir="ltr">Type</bdi> باید محدودیت را نشان دهد.

یک <bdi dir="ltr">`Money`</bdi> عمومی با <bdi dir="ltr">invariant</bdi> مثبت پنهان، انتخاب مبهمی است.

### گام 5 — <bdi dir="ltr">Equality</bdi> و <bdi dir="ltr">Scale</bdi>

رفتار <bdi dir="ltr">Characterization</bdi> باید حفظ شود، اما <bdi dir="ltr">Equality Value Object</bdi> جدید باید مستند باشد. اگر <bdi dir="ltr">`100.0`</bdi> و <bdi dir="ltr">`100.00`</bdi> برابرند، <bdi dir="ltr">`hashCode`</bdi> را نیز سازگار کن. ذخیرهٔ <bdi dir="ltr">Scale</bdi> ورودی و <bdi dir="ltr">Equality</bdi> عددی می‌توانند هم‌زمان وجود داشته باشند، اما پیچیدگی را ثبت کن.

### گام 6 — <bdi dir="ltr">Creation API</bdi>

سه گزینه را مقایسه کن:

1. <bdi dir="ltr">Constructor</bdi> عمومی و ساده
2. <bdi dir="ltr">Static Factory</bdi> مانند <bdi dir="ltr">`AccountId.parse`</bdi> و <bdi dir="ltr">`Money.of`</bdi>
3. <bdi dir="ltr">Factory class</bdi> مستقل

برای این <bdi dir="ltr">Kata</bdi> گزینهٔ سوم معمولاً اضافه است، مگر چند <bdi dir="ltr">Creation policy</bdi> واقعی، <bdi dir="ltr">Dependency</bdi> یا <bdi dir="ltr">Source</bdi> متفاوت داشته باشیم.

### گام 7 — نام و <bdi dir="ltr">API Request</bdi>

<bdi dir="ltr">Signature</bdi> جدید باید بدون خواندن <bdi dir="ltr">Implementation</bdi> قابل فهم باشد:


</div>

<div dir="ltr" align="left">

```java
TransferRequest.create(
    AccountId source,
    AccountId target,
    CustomerId customer,
    BranchId originatingBranch,
    Money amount
)
```

</div>

<div dir="rtl" align="right">


ممکن است <bdi dir="ltr">`TransferParty`</bdi> یا <bdi dir="ltr">`TransferRoute`</bdi> به ذهن برسد؛ فقط اگر <bdi dir="ltr">Cohesion</bdi> و <bdi dir="ltr">Variation</bdi> واقعی دارند آن‌ها را بساز.

### گام 8 — <bdi dir="ltr">Adapter</bdi> برای رفتار قدیمی

اگر <bdi dir="ltr">Audit key</bdi> یا <bdi dir="ltr">Constructor</bdi> قبلی <bdi dir="ltr">Consumer</bdi> دارد، یک <bdi dir="ltr">Adapter/Deprecated factory</bdi> کوچک می‌تواند رفتار را حفظ کند. لازم نیست <bdi dir="ltr">API</bdi> قدیمی را فوراً حذف کنی. <bdi dir="ltr">Branch by Abstraction</bdi> در <bdi dir="ltr">Week 23</bdi> عمیق‌تر می‌شود؛ اینجا فقط <bdi dir="ltr">Diff</bdi> امن می‌خواهیم.

### گام 9 — <bdi dir="ltr">`mvn verify`</bdi> و <bdi dir="ltr">Diff review</bdi>

پس از هر <bdi dir="ltr">Checkpoint</bdi> تست هدفمند و در پایان کل <bdi dir="ltr">Verify</bdi> را اجرا کن. <bdi dir="ltr">Diff</bdi> را از دید <bdi dir="ltr">Maintainer</bdi> بخوان:

- آیا <bdi dir="ltr">Intent</bdi> روشن‌تر شد؟
- آیا تعداد <bdi dir="ltr">Type</bdi>ها بیش از ارزششان شد؟
- آیا <bdi dir="ltr">Validation</bdi> به <bdi dir="ltr">Owner</bdi> درست رفت؟
- آیا <bdi dir="ltr">Rule</bdi> جدیدی ناخواسته وارد شد؟

## <bdi dir="ltr">8. Pattern Decision</bdi> نمونه

### <bdi dir="ltr">Problem</bdi>

<bdi dir="ltr">Primitive</bdi>ها اجازهٔ جابه‌جایی شناسه و جدایی <bdi dir="ltr">Amount/Currency</bdi> را می‌دهند.

### <bdi dir="ltr">Forces</bdi>

- خطای مالی باید زود <bdi dir="ltr">Fail</bdi> شود.
- <bdi dir="ltr">Type</bdi>ها باید <bdi dir="ltr">Framework-independent</bdi> باشند.
- <bdi dir="ltr">Format</bdi> شناسه‌ها هنوز کامل مشخص نیست.
- <bdi dir="ltr">Week 02</bdi> ممکن است <bdi dir="ltr">Context ownership</bdi> را تغییر دهد.
- <bdi dir="ltr">Abstraction</bdi> سراسری زودهنگام هزینه دارد.

### <bdi dir="ltr">Options</bdi>

- <bdi dir="ltr">Primitive</bdi>ها + <bdi dir="ltr">validation</bdi> در <bdi dir="ltr">Service</bdi>
- <bdi dir="ltr">Value Object</bdi>های کوچک + <bdi dir="ltr">Constructor</bdi>
- <bdi dir="ltr">Value Object</bdi> + <bdi dir="ltr">Static Factory</bdi>
- <bdi dir="ltr">Factory hierarchy</bdi> مشترک

### <bdi dir="ltr">Decision candidate</bdi>

<bdi dir="ltr">Value Object</bdi>های کوچک با <bdi dir="ltr">Static Factory</bdi> فقط جایی که نام <bdi dir="ltr">Creation/Parsing</bdi> معنا دارد؛ بدون <bdi dir="ltr">Base class</bdi> و <bdi dir="ltr">Factory hierarchy.</bdi>

### <bdi dir="ltr">Cost</bdi>

<bdi dir="ltr">Type</bdi> و <bdi dir="ltr">Mapping</bdi> بیشتر، <bdi dir="ltr">Serialization/ORM adapter</bdi> در آینده، احتمال <bdi dir="ltr">Duplicate</bdi> مدل میان <bdi dir="ltr">Context</bdi>ها.

### <bdi dir="ltr">Revisit trigger</bdi>

وقتی <bdi dir="ltr">Contract</bdi> رسمی <bdi dir="ltr">Format ID</bdi>، چند <bdi dir="ltr">Currency policy</bdi> یا چند <bdi dir="ltr">Creation source</bdi> ایجاد شد.

این فقط نمونهٔ ساختار است؛ <bdi dir="ltr">Decision</bdi> نهایی باید به کد تو و <bdi dir="ltr">Diff</bdi> واقعی اشاره کند.

## <bdi dir="ltr">9. Clean Code</bdi> با معماری یکی نیست

| تصمیم | سطح |
|---|---|
| نام <bdi dir="ltr">Method</bdi> و <bdi dir="ltr">Type</bdi> | <bdi dir="ltr">Code design</bdi> |
| <bdi dir="ltr">Value Object</bdi> و <bdi dir="ltr">Factory</bdi> | <bdi dir="ltr">Object/module design</bdi> |
| <bdi dir="ltr">Package API</bdi> | <bdi dir="ltr">Application architecture</bdi> |
| <bdi dir="ltr">Shared Kernel</bdi> یا مدل مستقل | <bdi dir="ltr">Strategic DDD</bdi> |
| <bdi dir="ltr">Microservice</bdi> مستقل | <bdi dir="ltr">Deployment/operations</bdi> |

وجود <bdi dir="ltr">`Money`</bdi> تمیز اثبات نمی‌کند <bdi dir="ltr">Money</bdi> باید <bdi dir="ltr">Library</bdi> مشترک کل بانک یا <bdi dir="ltr">Microservice</bdi> باشد. <bdi dir="ltr">Week 02</bdi> معنای هر <bdi dir="ltr">Type</bdi> در <bdi dir="ltr">Context</bdi> را بررسی می‌کند.

## 10. خطاهای رایج <bdi dir="ltr">Refactor</bdi>

### تغییر <bdi dir="ltr">Rule</bdi> زیر نام <bdi dir="ltr">Refactor</bdi>

<bdi dir="ltr">Normalize</bdi> کردن <bdi dir="ltr">Currency</bdi>، <bdi dir="ltr">Trim</bdi> کردن <bdi dir="ltr">ID</bdi> یا ممنوع‌کردن مبلغ صفر رفتار است. اگر <bdi dir="ltr">Requirement</bdi> ندارد، جدا ثبت کن.

### <bdi dir="ltr">God Value Object</bdi>

<bdi dir="ltr">`TransferContext`</bdi> که <bdi dir="ltr">Account</bdi>، <bdi dir="ltr">Customer</bdi>، <bdi dir="ltr">Branch</bdi>، <bdi dir="ltr">Money</bdi>، <bdi dir="ltr">Channel</bdi>، <bdi dir="ltr">Device</bdi> و <bdi dir="ltr">Session</bdi> را یکجا می‌گیرد فقط <bdi dir="ltr">Long Parameter List</bdi> را پنهان می‌کند.

### <bdi dir="ltr">Generic Base</bdi> زودهنگام

سه <bdi dir="ltr">ID</bdi> مشابه دلیل کافی برای <bdi dir="ltr">Generic inheritance</bdi> نیست. <bdi dir="ltr">Duplication</bdi> کوچک می‌تواند استقلال تغییر را حفظ کند.

### <bdi dir="ltr">Factory</bdi> نمایشی

<bdi dir="ltr">`TransferRequestAbstractFactoryProvider`</bdi> هیچ <bdi dir="ltr">Creation decision</bdi> واقعی ندارد و خوانایی را کم می‌کند.

### <bdi dir="ltr">Test</bdi> بر اساس <bdi dir="ltr">Implementation</bdi>

تست تعداد <bdi dir="ltr">Method</bdi>ها، نام <bdi dir="ltr">Field</bdi> خصوصی یا استفاده از <bdi dir="ltr">record</bdi> رفتار کسب‌وکاری را تثبیت نمی‌کند.

## 11. معیار <bdi dir="ltr">Code Review</bdi>

<bdi dir="ltr">Review</bdi> باید این شش سؤال را جواب دهد:

1. کدام خطای <bdi dir="ltr">Primitive</bdi> اکنون <bdi dir="ltr">Compile-time</bdi> یا <bdi dir="ltr">creation-time</bdi> متوقف می‌شود؟
2. کدام <bdi dir="ltr">Change coupling</bdi> کمتر شد؟
3. کدام <bdi dir="ltr">Complexity</bdi> اضافه شد؟
4. چه <bdi dir="ltr">Rule</bdi>ای عمداً تغییر نکرد؟
5. چه <bdi dir="ltr">Edge Case</bdi>ای تست شد؟
6. چه <bdi dir="ltr">Debt</bdi> یا <bdi dir="ltr">Unknown</bdi>ی باقی ماند؟

## 12. تمرین مستقل و <bdi dir="ltr">Rubric</bdi>

[<bdi dir="ltr">Day 08 Exercise</bdi>](../exercises/day-08-money-refactoring-kata.md) را انجام بده و [<bdi dir="ltr">Code Review Checklist</bdi>](../artifacts/day-08-code-review-checklist.md) را کامل کن.

| معیار | امتیاز |
|---|---:|
| <bdi dir="ltr">Baseline</bdi> و <bdi dir="ltr">Characterization evidence</bdi> | ۲ |
| <bdi dir="ltr">Smell Map Concrete</bdi> | ۲ |
| <bdi dir="ltr">Refactor</bdi> کوچک و سبز | ۲ |
| <bdi dir="ltr">Pattern Decision</bdi> با <bdi dir="ltr">Alternative/Cost</bdi> | ۲ |
| <bdi dir="ltr">Edge Test</bdi> و <bdi dir="ltr">Self-review</bdi> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. راه‌حل سادهٔ مستدل می‌تواند امتیاز کامل بگیرد؛ <bdi dir="ltr">Pattern</bdi> نمایشی امتیاز اضافه ندارد.

## 13. آزمون خروج و منابع

درس و کد را ببند و [<bdi dir="ltr">Exit Ticket</bdi>](../quizzes/day-08-exit-ticket.md) را پاسخ بده.

- [<bdi dir="ltr">Martin Fowler</bdi> — <bdi dir="ltr">Refactoring</bdi>](https://refactoring.com/)
- [<bdi dir="ltr">Replace Data Value with Object</bdi>](https://refactoring.com/catalog/replacePrimitiveWithObject.html)
- <bdi dir="ltr">Eric Evans</bdi>, *<bdi dir="ltr">Domain-Driven Design</bdi>* — <bdi dir="ltr">Value Objects</bdi>
- <bdi dir="ltr">Joshua Bloch</bdi>, *<bdi dir="ltr">Effective Java</bdi>* — <bdi dir="ltr">Static factories</bdi>، <bdi dir="ltr">immutability</bdi> و <bdi dir="ltr">`equals/hashCode`</bdi>


</div>
