# Day 08 — Clean Code و Refactoring از Primitive به Value Object

- Expansion budget: 105 minutes — 25 lesson + 65 coding + 10 self-review + 5 exit ticket
- Output: Refactored Transfer Request kata + tests + Pattern Decision + Code Review
- Code scope: Test-only educational fixture
- Banking note: شناسه‌ها و قواعد این Kata ساختگی‌اند و Contract واقعی بانک محسوب نمی‌شوند.

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. `Primitive Obsession`، `Data Clump`، `Long Parameter List` و Validation پراکنده را با محل و اثر تغییر شناسایی کنی.
2. رفتار کد موجود را پیش از Refactor با Characterization Test تثبیت کنی.
3. `Money` و Typed IDها را مرحله‌ای و بدون تغییر ناخواستهٔ رفتار معرفی کنی.
4. بین Constructor، Static Factory و Factory class تصمیم مستدل بگیری.
5. تفاوت Refactor با تغییر Rule دامینی را در Commit و Test حفظ کنی.
6. هزینهٔ Type و Abstraction تازه را صریح در Code Review ثبت کنی.

## 2. پیش‌نیاز

- Day 01 تا Day 07 هستهٔ Week 01 انجام شده باشد.
- Baseline کل پروژه با `mvn verify` سبز باشد.
- Contract طراحی Money در Day 06 را خوانده باشی.
- با Java record/class، `BigDecimal`، `Currency` و JUnit آشنا باشی.

## 3. چهار اصطلاحی که نباید یکی شوند

### Clean Code

کدی که Intent و Rule را آشکار می‌کند، تغییر مرتبط را محلی نگه می‌دارد، خطای نامعتبر را زود متوقف می‌کند و Dependency/Side effect را پنهان نمی‌سازد. Clean Code الزاماً کوتاه‌ترین یا پرکلاس‌ترین کد نیست.

### Code Smell

نشانه‌ای که احتمال مشکل طراحی را بالا می‌برد؛ نه حکم قطعی. Long Parameter List می‌تواند نشان دهد چند مفهوم در Primitiveها پنهان شده‌اند، اما ایجاد یک Object بزرگ `RequestContext` برای همهٔ پارامترها ممکن است مشکل را بدتر کند.

### Refactoring

تغییر ساختار داخلی بدون تغییر رفتار قابل مشاهده. اگر هم‌زمان مبلغ صفر را از مجاز به نامجاز تبدیل کنی، آن Commit فقط Refactor نیست؛ Rule change نیز هست.

### Design Pattern

راه‌حل نام‌دار برای Forces تکرارشونده. Pattern جایگزین تحلیل نیست. Value Object از الگوهای DDD است؛ Static Factory یک API/creation idiom است. ساخت Factory hierarchy فقط برای اینکه «Design Pattern استفاده شود» مردود است.

## 4. Baseline عمداً Primitive

Starter این Week یک Transfer Request کوچک دارد:

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

مشکل فقط تعداد پارامترها نیست. کد برای فهمیدن معنا به نام متغیر و ترتیب وابسته است:

- Source و target هر دو String و قابل‌جابه‌جایی‌اند.
- Customer و Branch نیز String هستند.
- Amount و Currency یک Data Clump تکرارشونده‌اند.
- Validation در Constructor پراکنده است.
- Equality عددی `BigDecimal` و Currency semantics روشن نیست.
- `auditKey` با Concatenation Representation داخلی می‌سازد.

بااین‌حال Baseline یک رفتار موجود دارد. قبل از تغییر باید بدانیم چه چیزی را حفظ می‌کنیم و چه چیزی `OPEN` است.

## 5. Characterization Test چیست؟

Characterization Test رفتار فعلی سیستم را ثبت می‌کند، حتی اگر رفتار ایده‌آل نباشد. هدف ابتدا ایجاد Safety net است.

Starter این رفتارها را ثبت می‌کند:

- Request معتبر ساخته می‌شود.
- Source و target یکسان رد می‌شود.
- مبلغ null، صفر و منفی رد می‌شود.
- Currency blank رد می‌شود.
- مقدار Amount همان Scale ورودی را نگه می‌دارد.
- Audit key از فیلدهای فعلی ساخته می‌شود.

این تست‌ها نمی‌گویند همهٔ Rules درست‌اند. اگر Format شناسه‌ها هیچ Contract رسمی ندارد، Test نباید Regex خیالی را تثبیت کند.

## 6. Smell Map باید Concrete باشد

Smell map ضعیف:

> SOLID رعایت نشده و کد تمیز نیست.

Smell map قابل‌استفاده:

| Symbol | Smell | Change risk | Smallest safe move |
|---|---|---|---|
| constructor parameters | Long Parameter List + Primitive Obsession | جابه‌جایی شناسه‌ها Compile می‌شود | معرفی یک Typed ID در هر گام |
| amount + currency | Data Clump | Validation/operation تکراری | استخراج Money پس از Characterization |
| string guards | Scattered validation | Ruleها با هم ناسازگار می‌شوند | Guard داخل Value Object مرتبط |
| auditKey | Representation leak | تغییر Format مصرف‌کننده را می‌شکند | نام‌گذاری Contract یا نگه‌داشتن Adapter |

Smell باید Location، نشانه و اثر واقعی داشته باشد.

## 7. مسیر Refactor مرحله‌ای

### گام 0 — Baseline کل پروژه

```bash
cd backend/banking-modulith
mvn -B -ntp verify
```

Commit/SHA، تعداد تست و نتیجه را ثبت کن.

### گام 1 — تست Edge تازه

یکی از Unknownها را انتخاب کن:

- Currency با حروف کوچک
- Whitespace اطراف ID
- مبلغ با Scale بسیار بزرگ
- Audit key در صورت وجود delimiter داخل ID
- Source/target که فقط در whitespace فرق دارند

اگر Expected behavior از Baseline یا Requirement قابل استنتاج نیست، آن را `OPEN` نگه دار و Edge دیگری را تست کن. Rule بانکی را حدس نزن.

### گام 2 — `AccountId`

فقط Source/target را Type-safe کن. تست‌ها سبز شوند. هنوز Customer/Branch و Money را تغییر نده. این کار Diff را کوچک و علت Failure را روشن نگه می‌دارد.

### گام 3 — `CustomerId` و `BranchId`

سه Type مشابه ممکن است کمی Duplication داشته باشند. فعلاً `AbstractStringId<T>` نساز. هنوز نمی‌دانیم Validation و نمایش آن‌ها واقعاً یکسان است.

### گام 4 — `Money`

Amount و Currency را کنار هم قرار بده. Validation null/blank به Money منتقل شود. Rule مثبت‌بودن را آگاهانه انتخاب کن:

- Option A: Money عمومی Signed؛ `TransferAmount`/Request مثبت‌بودن را کنترل کند.
- Option B: این Kata یک Money محدود به انتقال بسازد؛ نام Type باید محدودیت را نشان دهد.

یک `Money` عمومی با invariant مثبت پنهان، انتخاب مبهمی است.

### گام 5 — Equality و Scale

رفتار Characterization باید حفظ شود، اما Equality Value Object جدید باید مستند باشد. اگر `100.0` و `100.00` برابرند، `hashCode` را نیز سازگار کن. ذخیرهٔ Scale ورودی و Equality عددی می‌توانند هم‌زمان وجود داشته باشند، اما پیچیدگی را ثبت کن.

### گام 6 — Creation API

سه گزینه را مقایسه کن:

1. Constructor عمومی و ساده
2. Static Factory مانند `AccountId.parse` و `Money.of`
3. Factory class مستقل

برای این Kata گزینهٔ سوم معمولاً اضافه است، مگر چند Creation policy واقعی، Dependency یا Source متفاوت داشته باشیم.

### گام 7 — نام و API Request

Signature جدید باید بدون خواندن Implementation قابل فهم باشد:

```java
TransferRequest.create(
    AccountId source,
    AccountId target,
    CustomerId customer,
    BranchId originatingBranch,
    Money amount
)
```

ممکن است `TransferParty` یا `TransferRoute` به ذهن برسد؛ فقط اگر Cohesion و Variation واقعی دارند آن‌ها را بساز.

### گام 8 — Adapter برای رفتار قدیمی

اگر Audit key یا Constructor قبلی Consumer دارد، یک Adapter/Deprecated factory کوچک می‌تواند رفتار را حفظ کند. لازم نیست API قدیمی را فوراً حذف کنی. Branch by Abstraction در Week 23 عمیق‌تر می‌شود؛ اینجا فقط Diff امن می‌خواهیم.

### گام 9 — `mvn verify` و Diff review

پس از هر Checkpoint تست هدفمند و در پایان کل Verify را اجرا کن. Diff را از دید Maintainer بخوان:

- آیا Intent روشن‌تر شد؟
- آیا تعداد Typeها بیش از ارزششان شد؟
- آیا Validation به Owner درست رفت؟
- آیا Rule جدیدی ناخواسته وارد شد؟

## 8. Pattern Decision نمونه

### Problem

Primitiveها اجازهٔ جابه‌جایی شناسه و جدایی Amount/Currency را می‌دهند.

### Forces

- خطای مالی باید زود Fail شود.
- Typeها باید Framework-independent باشند.
- Format شناسه‌ها هنوز کامل مشخص نیست.
- Week 02 ممکن است Context ownership را تغییر دهد.
- Abstraction سراسری زودهنگام هزینه دارد.

### Options

- Primitiveها + validation در Service
- Value Objectهای کوچک + Constructor
- Value Object + Static Factory
- Factory hierarchy مشترک

### Decision candidate

Value Objectهای کوچک با Static Factory فقط جایی که نام Creation/Parsing معنا دارد؛ بدون Base class و Factory hierarchy.

### Cost

Type و Mapping بیشتر، Serialization/ORM adapter در آینده، احتمال Duplicate مدل میان Contextها.

### Revisit trigger

وقتی Contract رسمی Format ID، چند Currency policy یا چند Creation source ایجاد شد.

این فقط نمونهٔ ساختار است؛ Decision نهایی باید به کد تو و Diff واقعی اشاره کند.

## 9. Clean Code با معماری یکی نیست

| تصمیم | سطح |
|---|---|
| نام Method و Type | Code design |
| Value Object و Factory | Object/module design |
| Package API | Application architecture |
| Shared Kernel یا مدل مستقل | Strategic DDD |
| Microservice مستقل | Deployment/operations |

وجود `Money` تمیز اثبات نمی‌کند Money باید Library مشترک کل بانک یا Microservice باشد. Week 02 معنای هر Type در Context را بررسی می‌کند.

## 10. خطاهای رایج Refactor

### تغییر Rule زیر نام Refactor

Normalize کردن Currency، Trim کردن ID یا ممنوع‌کردن مبلغ صفر رفتار است. اگر Requirement ندارد، جدا ثبت کن.

### God Value Object

`TransferContext` که Account، Customer، Branch، Money، Channel، Device و Session را یکجا می‌گیرد فقط Long Parameter List را پنهان می‌کند.

### Generic Base زودهنگام

سه ID مشابه دلیل کافی برای Generic inheritance نیست. Duplication کوچک می‌تواند استقلال تغییر را حفظ کند.

### Factory نمایشی

`TransferRequestAbstractFactoryProvider` هیچ Creation decision واقعی ندارد و خوانایی را کم می‌کند.

### Test بر اساس Implementation

تست تعداد Methodها، نام Field خصوصی یا استفاده از record رفتار کسب‌وکاری را تثبیت نمی‌کند.

## 11. معیار Code Review

Review باید این شش سؤال را جواب دهد:

1. کدام خطای Primitive اکنون Compile-time یا creation-time متوقف می‌شود؟
2. کدام Change coupling کمتر شد؟
3. کدام Complexity اضافه شد؟
4. چه Ruleای عمداً تغییر نکرد؟
5. چه Edge Caseای تست شد؟
6. چه Debt یا Unknownی باقی ماند؟

## 12. تمرین مستقل و Rubric

[Day 08 Exercise](../exercises/day-08-money-refactoring-kata.md) را انجام بده و [Code Review Checklist](../artifacts/day-08-code-review-checklist.md) را کامل کن.

| معیار | امتیاز |
|---|---:|
| Baseline و Characterization evidence | ۲ |
| Smell Map Concrete | ۲ |
| Refactor کوچک و سبز | ۲ |
| Pattern Decision با Alternative/Cost | ۲ |
| Edge Test و Self-review | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. راه‌حل سادهٔ مستدل می‌تواند امتیاز کامل بگیرد؛ Pattern نمایشی امتیاز اضافه ندارد.

## 13. آزمون خروج و منابع

درس و کد را ببند و [Exit Ticket](../quizzes/day-08-exit-ticket.md) را پاسخ بده.

- [Martin Fowler — Refactoring](https://refactoring.com/)
- [Replace Data Value with Object](https://refactoring.com/catalog/replacePrimitiveWithObject.html)
- Eric Evans, *Domain-Driven Design* — Value Objects
- Joshua Bloch, *Effective Java* — Static factories، immutability و `equals/hashCode`

