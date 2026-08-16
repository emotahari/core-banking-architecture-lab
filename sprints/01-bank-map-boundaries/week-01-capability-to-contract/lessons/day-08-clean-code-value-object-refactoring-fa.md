<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 08</span> — <span dir="ltr">Clean Code</span> و <span dir="ltr">Refactoring</span> از <span dir="ltr">Primitive</span> به <span dir="ltr">Value Object</span>

- <span dir="ltr">Expansion budget: 105 minutes</span> — <span dir="ltr">25 lesson</span> + <span dir="ltr">65 coding</span> + <span dir="ltr">10 self-review</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output: Refactored Transfer Request kata</span> + <span dir="ltr">tests</span> + <span dir="ltr">Pattern Decision</span> + <span dir="ltr">Code Review</span>
- <span dir="ltr">Code scope: Test-only educational fixture</span>
- <span dir="ltr">Banking note:</span> شناسه‌ها و قواعد این <span dir="ltr">Kata</span> ساختگی‌اند و <span dir="ltr">Contract</span> واقعی بانک محسوب نمی‌شوند.

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">`Primitive Obsession`</span>، <span dir="ltr">`Data Clump`</span>، <span dir="ltr">`Long Parameter List`</span> و <span dir="ltr">Validation</span> پراکنده را با محل و اثر تغییر شناسایی کنی.
2. رفتار کد موجود را پیش از <span dir="ltr">Refactor</span> با <span dir="ltr">Characterization Test</span> تثبیت کنی.
3. <span dir="ltr">`Money`</span> و <span dir="ltr">Typed ID</span>ها را مرحله‌ای و بدون تغییر ناخواستهٔ رفتار معرفی کنی.
4. بین <span dir="ltr">Constructor</span>، <span dir="ltr">Static Factory</span> و <span dir="ltr">Factory class</span> تصمیم مستدل بگیری.
5. تفاوت <span dir="ltr">Refactor</span> با تغییر <span dir="ltr">Rule</span> دامینی را در <span dir="ltr">Commit</span> و <span dir="ltr">Test</span> حفظ کنی.
6. هزینهٔ <span dir="ltr">Type</span> و <span dir="ltr">Abstraction</span> تازه را صریح در <span dir="ltr">Code Review</span> ثبت کنی.

## 2. پیش‌نیاز

- <span dir="ltr">Day 01</span> تا <span dir="ltr">Day 07</span> هستهٔ <span dir="ltr">Week 01</span> انجام شده باشد.
- <span dir="ltr">Baseline</span> کل پروژه با <span dir="ltr">`mvn verify`</span> سبز باشد.
- <span dir="ltr">Contract</span> طراحی <span dir="ltr">Money</span> در <span dir="ltr">Day 06</span> را خوانده باشی.
- با <span dir="ltr">Java record/class</span>، <span dir="ltr">`BigDecimal`</span>، <span dir="ltr">`Currency`</span> و <span dir="ltr">JUnit</span> آشنا باشی.

## 3. چهار اصطلاحی که نباید یکی شوند

### <span dir="ltr">Clean Code</span>

کدی که <span dir="ltr">Intent</span> و <span dir="ltr">Rule</span> را آشکار می‌کند، تغییر مرتبط را محلی نگه می‌دارد، خطای نامعتبر را زود متوقف می‌کند و <span dir="ltr">Dependency/Side effect</span> را پنهان نمی‌سازد. <span dir="ltr">Clean Code</span> الزاماً کوتاه‌ترین یا پرکلاس‌ترین کد نیست.

### <span dir="ltr">Code Smell</span>

نشانه‌ای که احتمال مشکل طراحی را بالا می‌برد؛ نه حکم قطعی. <span dir="ltr">Long Parameter List</span> می‌تواند نشان دهد چند مفهوم در <span dir="ltr">Primitive</span>ها پنهان شده‌اند، اما ایجاد یک <span dir="ltr">Object</span> بزرگ <span dir="ltr">`RequestContext`</span> برای همهٔ پارامترها ممکن است مشکل را بدتر کند.

### <span dir="ltr">Refactoring</span>

تغییر ساختار داخلی بدون تغییر رفتار قابل مشاهده. اگر هم‌زمان مبلغ صفر را از مجاز به نامجاز تبدیل کنی، آن <span dir="ltr">Commit</span> فقط <span dir="ltr">Refactor</span> نیست؛ <span dir="ltr">Rule change</span> نیز هست.

### <span dir="ltr">Design Pattern</span>

راه‌حل نام‌دار برای <span dir="ltr">Forces</span> تکرارشونده. <span dir="ltr">Pattern</span> جایگزین تحلیل نیست. <span dir="ltr">Value Object</span> از الگوهای <span dir="ltr">DDD</span> است؛ <span dir="ltr">Static Factory</span> یک <span dir="ltr">API/creation idiom</span> است. ساخت <span dir="ltr">Factory hierarchy</span> فقط برای اینکه «<span dir="ltr">Design Pattern</span> استفاده شود» مردود است.

## <span dir="ltr">4. Baseline</span> عمداً <span dir="ltr">Primitive</span>

<span dir="ltr">Starter</span> این <span dir="ltr">Week</span> یک <span dir="ltr">Transfer Request</span> کوچک دارد:


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

- <span dir="ltr">Source</span> و <span dir="ltr">target</span> هر دو <span dir="ltr">String</span> و قابل‌جابه‌جایی‌اند.
- <span dir="ltr">Customer</span> و <span dir="ltr">Branch</span> نیز <span dir="ltr">String</span> هستند.
- <span dir="ltr">Amount</span> و <span dir="ltr">Currency</span> یک <span dir="ltr">Data Clump</span> تکرارشونده‌اند.
- <span dir="ltr">Validation</span> در <span dir="ltr">Constructor</span> پراکنده است.
- <span dir="ltr">Equality</span> عددی <span dir="ltr">`BigDecimal`</span> و <span dir="ltr">Currency semantics</span> روشن نیست.
- <span dir="ltr">`auditKey`</span> با <span dir="ltr">Concatenation Representation</span> داخلی می‌سازد.

بااین‌حال <span dir="ltr">Baseline</span> یک رفتار موجود دارد. قبل از تغییر باید بدانیم چه چیزی را حفظ می‌کنیم و چه چیزی <span dir="ltr">`OPEN`</span> است.

## <span dir="ltr">5. Characterization Test</span> چیست؟

<span dir="ltr">Characterization Test</span> رفتار فعلی سیستم را ثبت می‌کند، حتی اگر رفتار ایده‌آل نباشد. هدف ابتدا ایجاد <span dir="ltr">Safety net</span> است.

<span dir="ltr">Starter</span> این رفتارها را ثبت می‌کند:

- <span dir="ltr">Request</span> معتبر ساخته می‌شود.
- <span dir="ltr">Source</span> و <span dir="ltr">target</span> یکسان رد می‌شود.
- مبلغ <span dir="ltr">null</span>، صفر و منفی رد می‌شود.
- <span dir="ltr">Currency blank</span> رد می‌شود.
- مقدار <span dir="ltr">Amount</span> همان <span dir="ltr">Scale</span> ورودی را نگه می‌دارد.
- <span dir="ltr">Audit key</span> از فیلدهای فعلی ساخته می‌شود.

این تست‌ها نمی‌گویند همهٔ <span dir="ltr">Rules</span> درست‌اند. اگر <span dir="ltr">Format</span> شناسه‌ها هیچ <span dir="ltr">Contract</span> رسمی ندارد، <span dir="ltr">Test</span> نباید <span dir="ltr">Regex</span> خیالی را تثبیت کند.

## <span dir="ltr">6. Smell Map</span> باید <span dir="ltr">Concrete</span> باشد

<span dir="ltr">Smell map</span> ضعیف:

> <span dir="ltr">SOLID</span> رعایت نشده و کد تمیز نیست.

<span dir="ltr">Smell map</span> قابل‌استفاده:

| <span dir="ltr">Symbol</span> | <span dir="ltr">Smell</span> | <span dir="ltr">Change risk</span> | <span dir="ltr">Smallest safe move</span> |
|---|---|---|---|
| <span dir="ltr">constructor parameters</span> | <span dir="ltr">Long Parameter List</span> + <span dir="ltr">Primitive Obsession</span> | جابه‌جایی شناسه‌ها <span dir="ltr">Compile</span> می‌شود | معرفی یک <span dir="ltr">Typed ID</span> در هر گام |
| <span dir="ltr">amount</span> + <span dir="ltr">currency</span> | <span dir="ltr">Data Clump</span> | <span dir="ltr">Validation/operation</span> تکراری | استخراج <span dir="ltr">Money</span> پس از <span dir="ltr">Characterization</span> |
| <span dir="ltr">string guards</span> | <span dir="ltr">Scattered validation</span> | <span dir="ltr">Rule</span>ها با هم ناسازگار می‌شوند | <span dir="ltr">Guard</span> داخل <span dir="ltr">Value Object</span> مرتبط |
| <span dir="ltr">auditKey</span> | <span dir="ltr">Representation leak</span> | تغییر <span dir="ltr">Format</span> مصرف‌کننده را می‌شکند | نام‌گذاری <span dir="ltr">Contract</span> یا نگه‌داشتن <span dir="ltr">Adapter</span> |

<span dir="ltr">Smell</span> باید <span dir="ltr">Location</span>، نشانه و اثر واقعی داشته باشد.

## 7. مسیر <span dir="ltr">Refactor</span> مرحله‌ای

### گام 0 — <span dir="ltr">Baseline</span> کل پروژه


</div>

<div dir="ltr" align="left">

```bash
cd backend/banking-modulith
mvn -B -ntp verify
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Commit/SHA</span>، تعداد تست و نتیجه را ثبت کن.

### گام 1 — تست <span dir="ltr">Edge</span> تازه

یکی از <span dir="ltr">Unknown</span>ها را انتخاب کن:

- <span dir="ltr">Currency</span> با حروف کوچک
- <span dir="ltr">Whitespace</span> اطراف <span dir="ltr">ID</span>
- مبلغ با <span dir="ltr">Scale</span> بسیار بزرگ
- <span dir="ltr">Audit key</span> در صورت وجود <span dir="ltr">delimiter</span> داخل <span dir="ltr">ID</span>
- <span dir="ltr">Source/target</span> که فقط در <span dir="ltr">whitespace</span> فرق دارند

اگر <span dir="ltr">Expected behavior</span> از <span dir="ltr">Baseline</span> یا <span dir="ltr">Requirement</span> قابل استنتاج نیست، آن را <span dir="ltr">`OPEN`</span> نگه دار و <span dir="ltr">Edge</span> دیگری را تست کن. <span dir="ltr">Rule</span> بانکی را حدس نزن.

### گام 2 — <span dir="ltr">`AccountId`</span>

فقط <span dir="ltr">Source/target</span> را <span dir="ltr">Type-safe</span> کن. تست‌ها سبز شوند. هنوز <span dir="ltr">Customer/Branch</span> و <span dir="ltr">Money</span> را تغییر نده. این کار <span dir="ltr">Diff</span> را کوچک و علت <span dir="ltr">Failure</span> را روشن نگه می‌دارد.

### گام 3 — <span dir="ltr">`CustomerId`</span> و <span dir="ltr">`BranchId`</span>

سه <span dir="ltr">Type</span> مشابه ممکن است کمی <span dir="ltr">Duplication</span> داشته باشند. فعلاً <span dir="ltr">`AbstractStringId<T>`</span> نساز. هنوز نمی‌دانیم <span dir="ltr">Validation</span> و نمایش آن‌ها واقعاً یکسان است.

### گام 4 — <span dir="ltr">`Money`</span>

<span dir="ltr">Amount</span> و <span dir="ltr">Currency</span> را کنار هم قرار بده. <span dir="ltr">Validation null/blank</span> به <span dir="ltr">Money</span> منتقل شود. <span dir="ltr">Rule</span> مثبت‌بودن را آگاهانه انتخاب کن:

- <span dir="ltr">Option A: Money</span> عمومی <span dir="ltr">Signed</span>؛ <span dir="ltr">`TransferAmount`</span>/<span dir="ltr">Request</span> مثبت‌بودن را کنترل کند.
- <span dir="ltr">Option B:</span> این <span dir="ltr">Kata</span> یک <span dir="ltr">Money</span> محدود به انتقال بسازد؛ نام <span dir="ltr">Type</span> باید محدودیت را نشان دهد.

یک <span dir="ltr">`Money`</span> عمومی با <span dir="ltr">invariant</span> مثبت پنهان، انتخاب مبهمی است.

### گام 5 — <span dir="ltr">Equality</span> و <span dir="ltr">Scale</span>

رفتار <span dir="ltr">Characterization</span> باید حفظ شود، اما <span dir="ltr">Equality Value Object</span> جدید باید مستند باشد. اگر <span dir="ltr">`100.0`</span> و <span dir="ltr">`100.00`</span> برابرند، <span dir="ltr">`hashCode`</span> را نیز سازگار کن. ذخیرهٔ <span dir="ltr">Scale</span> ورودی و <span dir="ltr">Equality</span> عددی می‌توانند هم‌زمان وجود داشته باشند، اما پیچیدگی را ثبت کن.

### گام 6 — <span dir="ltr">Creation API</span>

سه گزینه را مقایسه کن:

1. <span dir="ltr">Constructor</span> عمومی و ساده
2. <span dir="ltr">Static Factory</span> مانند <span dir="ltr">`AccountId.parse`</span> و <span dir="ltr">`Money.of`</span>
3. <span dir="ltr">Factory class</span> مستقل

برای این <span dir="ltr">Kata</span> گزینهٔ سوم معمولاً اضافه است، مگر چند <span dir="ltr">Creation policy</span> واقعی، <span dir="ltr">Dependency</span> یا <span dir="ltr">Source</span> متفاوت داشته باشیم.

### گام 7 — نام و <span dir="ltr">API Request</span>

<span dir="ltr">Signature</span> جدید باید بدون خواندن <span dir="ltr">Implementation</span> قابل فهم باشد:


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


ممکن است <span dir="ltr">`TransferParty`</span> یا <span dir="ltr">`TransferRoute`</span> به ذهن برسد؛ فقط اگر <span dir="ltr">Cohesion</span> و <span dir="ltr">Variation</span> واقعی دارند آن‌ها را بساز.

### گام 8 — <span dir="ltr">Adapter</span> برای رفتار قدیمی

اگر <span dir="ltr">Audit key</span> یا <span dir="ltr">Constructor</span> قبلی <span dir="ltr">Consumer</span> دارد، یک <span dir="ltr">Adapter/Deprecated factory</span> کوچک می‌تواند رفتار را حفظ کند. لازم نیست <span dir="ltr">API</span> قدیمی را فوراً حذف کنی. <span dir="ltr">Branch by Abstraction</span> در <span dir="ltr">Week 23</span> عمیق‌تر می‌شود؛ اینجا فقط <span dir="ltr">Diff</span> امن می‌خواهیم.

### گام 9 — <span dir="ltr">`mvn verify`</span> و <span dir="ltr">Diff review</span>

پس از هر <span dir="ltr">Checkpoint</span> تست هدفمند و در پایان کل <span dir="ltr">Verify</span> را اجرا کن. <span dir="ltr">Diff</span> را از دید <span dir="ltr">Maintainer</span> بخوان:

- آیا <span dir="ltr">Intent</span> روشن‌تر شد؟
- آیا تعداد <span dir="ltr">Type</span>ها بیش از ارزششان شد؟
- آیا <span dir="ltr">Validation</span> به <span dir="ltr">Owner</span> درست رفت؟
- آیا <span dir="ltr">Rule</span> جدیدی ناخواسته وارد شد؟

## <span dir="ltr">8. Pattern Decision</span> نمونه

### <span dir="ltr">Problem</span>

<span dir="ltr">Primitive</span>ها اجازهٔ جابه‌جایی شناسه و جدایی <span dir="ltr">Amount/Currency</span> را می‌دهند.

### <span dir="ltr">Forces</span>

- خطای مالی باید زود <span dir="ltr">Fail</span> شود.
- <span dir="ltr">Type</span>ها باید <span dir="ltr">Framework-independent</span> باشند.
- <span dir="ltr">Format</span> شناسه‌ها هنوز کامل مشخص نیست.
- <span dir="ltr">Week 02</span> ممکن است <span dir="ltr">Context ownership</span> را تغییر دهد.
- <span dir="ltr">Abstraction</span> سراسری زودهنگام هزینه دارد.

### <span dir="ltr">Options</span>

- <span dir="ltr">Primitive</span>ها + <span dir="ltr">validation</span> در <span dir="ltr">Service</span>
- <span dir="ltr">Value Object</span>های کوچک + <span dir="ltr">Constructor</span>
- <span dir="ltr">Value Object</span> + <span dir="ltr">Static Factory</span>
- <span dir="ltr">Factory hierarchy</span> مشترک

### <span dir="ltr">Decision candidate</span>

<span dir="ltr">Value Object</span>های کوچک با <span dir="ltr">Static Factory</span> فقط جایی که نام <span dir="ltr">Creation/Parsing</span> معنا دارد؛ بدون <span dir="ltr">Base class</span> و <span dir="ltr">Factory hierarchy.</span>

### <span dir="ltr">Cost</span>

<span dir="ltr">Type</span> و <span dir="ltr">Mapping</span> بیشتر، <span dir="ltr">Serialization/ORM adapter</span> در آینده، احتمال <span dir="ltr">Duplicate</span> مدل میان <span dir="ltr">Context</span>ها.

### <span dir="ltr">Revisit trigger</span>

وقتی <span dir="ltr">Contract</span> رسمی <span dir="ltr">Format ID</span>، چند <span dir="ltr">Currency policy</span> یا چند <span dir="ltr">Creation source</span> ایجاد شد.

این فقط نمونهٔ ساختار است؛ <span dir="ltr">Decision</span> نهایی باید به کد تو و <span dir="ltr">Diff</span> واقعی اشاره کند.

## <span dir="ltr">9. Clean Code</span> با معماری یکی نیست

| تصمیم | سطح |
|---|---|
| نام <span dir="ltr">Method</span> و <span dir="ltr">Type</span> | <span dir="ltr">Code design</span> |
| <span dir="ltr">Value Object</span> و <span dir="ltr">Factory</span> | <span dir="ltr">Object/module design</span> |
| <span dir="ltr">Package API</span> | <span dir="ltr">Application architecture</span> |
| <span dir="ltr">Shared Kernel</span> یا مدل مستقل | <span dir="ltr">Strategic DDD</span> |
| <span dir="ltr">Microservice</span> مستقل | <span dir="ltr">Deployment/operations</span> |

وجود <span dir="ltr">`Money`</span> تمیز اثبات نمی‌کند <span dir="ltr">Money</span> باید <span dir="ltr">Library</span> مشترک کل بانک یا <span dir="ltr">Microservice</span> باشد. <span dir="ltr">Week 02</span> معنای هر <span dir="ltr">Type</span> در <span dir="ltr">Context</span> را بررسی می‌کند.

## 10. خطاهای رایج <span dir="ltr">Refactor</span>

### تغییر <span dir="ltr">Rule</span> زیر نام <span dir="ltr">Refactor</span>

<span dir="ltr">Normalize</span> کردن <span dir="ltr">Currency</span>، <span dir="ltr">Trim</span> کردن <span dir="ltr">ID</span> یا ممنوع‌کردن مبلغ صفر رفتار است. اگر <span dir="ltr">Requirement</span> ندارد، جدا ثبت کن.

### <span dir="ltr">God Value Object</span>

<span dir="ltr">`TransferContext`</span> که <span dir="ltr">Account</span>، <span dir="ltr">Customer</span>، <span dir="ltr">Branch</span>، <span dir="ltr">Money</span>، <span dir="ltr">Channel</span>، <span dir="ltr">Device</span> و <span dir="ltr">Session</span> را یکجا می‌گیرد فقط <span dir="ltr">Long Parameter List</span> را پنهان می‌کند.

### <span dir="ltr">Generic Base</span> زودهنگام

سه <span dir="ltr">ID</span> مشابه دلیل کافی برای <span dir="ltr">Generic inheritance</span> نیست. <span dir="ltr">Duplication</span> کوچک می‌تواند استقلال تغییر را حفظ کند.

### <span dir="ltr">Factory</span> نمایشی

<span dir="ltr">`TransferRequestAbstractFactoryProvider`</span> هیچ <span dir="ltr">Creation decision</span> واقعی ندارد و خوانایی را کم می‌کند.

### <span dir="ltr">Test</span> بر اساس <span dir="ltr">Implementation</span>

تست تعداد <span dir="ltr">Method</span>ها، نام <span dir="ltr">Field</span> خصوصی یا استفاده از <span dir="ltr">record</span> رفتار کسب‌وکاری را تثبیت نمی‌کند.

## 11. معیار <span dir="ltr">Code Review</span>

<span dir="ltr">Review</span> باید این شش سؤال را جواب دهد:

1. کدام خطای <span dir="ltr">Primitive</span> اکنون <span dir="ltr">Compile-time</span> یا <span dir="ltr">creation-time</span> متوقف می‌شود؟
2. کدام <span dir="ltr">Change coupling</span> کمتر شد؟
3. کدام <span dir="ltr">Complexity</span> اضافه شد؟
4. چه <span dir="ltr">Rule</span>ای عمداً تغییر نکرد؟
5. چه <span dir="ltr">Edge Case</span>ای تست شد؟
6. چه <span dir="ltr">Debt</span> یا <span dir="ltr">Unknown</span>ی باقی ماند؟

## 12. تمرین مستقل و <span dir="ltr">Rubric</span>

[<span dir="ltr">Day 08 Exercise</span>](../exercises/day-08-money-refactoring-kata.md) را انجام بده و [<span dir="ltr">Code Review Checklist</span>](../artifacts/day-08-code-review-checklist.md) را کامل کن.

| معیار | امتیاز |
|---|---:|
| <span dir="ltr">Baseline</span> و <span dir="ltr">Characterization evidence</span> | ۲ |
| <span dir="ltr">Smell Map Concrete</span> | ۲ |
| <span dir="ltr">Refactor</span> کوچک و سبز | ۲ |
| <span dir="ltr">Pattern Decision</span> با <span dir="ltr">Alternative/Cost</span> | ۲ |
| <span dir="ltr">Edge Test</span> و <span dir="ltr">Self-review</span> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. راه‌حل سادهٔ مستدل می‌تواند امتیاز کامل بگیرد؛ <span dir="ltr">Pattern</span> نمایشی امتیاز اضافه ندارد.

## 13. آزمون خروج و منابع

درس و کد را ببند و [<span dir="ltr">Exit Ticket</span>](../quizzes/day-08-exit-ticket.md) را پاسخ بده.

- [<span dir="ltr">Martin Fowler</span> — <span dir="ltr">Refactoring</span>](https://refactoring.com/)
- [<span dir="ltr">Replace Data Value with Object</span>](https://refactoring.com/catalog/replacePrimitiveWithObject.html)
- <span dir="ltr">Eric Evans</span>, *<span dir="ltr">Domain-Driven Design</span>* — <span dir="ltr">Value Objects</span>
- <span dir="ltr">Joshua Bloch</span>, *<span dir="ltr">Effective Java</span>* — <span dir="ltr">Static factories</span>، <span dir="ltr">immutability</span> و <span dir="ltr">`equals/hashCode`</span>


</div>
