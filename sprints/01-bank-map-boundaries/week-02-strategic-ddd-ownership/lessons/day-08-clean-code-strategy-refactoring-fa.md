# Day 08 — Clean Code و Refactoring با Strategy/Factory

- Expansion budget: 105 minutes — 25 lesson + 65 coding + 10 self-review + 5 exit ticket
- Output: refactored Transfer Fee kata + tests + Pattern Decision + Code Review
- Code scope: test-only educational fixture
- Banking note: همهٔ نرخ‌ها و Limits این Kata ساختگی‌اند و تعرفهٔ واقعی بانکی نیستند.

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. تفاوت Clean Code، Code Smell، Refactoring و Design Pattern را بدون شعار توضیح بدهی.
2. رفتار کد Legacy را پیش از تغییر با Characterization Test تثبیت کنی.
3. `Magic Literal`، `Primitive Obsession`، `Flag Argument` و مسئولیت‌های مخلوط را در یک مثال بانکی پیدا کنی.
4. تصمیم بگیری آیا Variation نرخ کارمزد واقعاً Strategy را توجیه می‌کند یا یک `switch` خوانا کافی است.
5. در صورت انتخاب Strategy، Selection را با یک Registry/Factory کوچک از Calculation جدا کنی.
6. Refactor را بدون تغییر ناخواستهٔ Rule دامینی و در گام‌های سبز انجام بدهی.
7. هزینهٔ Pattern اضافه‌شده را در Code Review صریح ثبت کنی.

## 2. پیش‌نیاز

- Baseline پروژه با `mvn verify` سبز باشد.
- تفاوت Capability، Domain، Bounded Context و Module را بدانی.
- با Java record، enum، interface، JUnit و Exception آشنا باشی.
- Day 05 و Day 06 را انجام داده باشی تا Package boundary را با Class design اشتباه نگیری.

## 3. چرا این درس به Week 02 اضافه شده است؟

Boundary روی Diagram اگر در کد به Interfaceهای نامفهوم، Stringهای جادویی و `Service`های چندمسئولیتی تبدیل شود، عمر زیادی ندارد. از طرف دیگر، استفادهٔ نمایشی از Pattern نیز Boundary را بهتر نمی‌کند؛ فقط تعداد Typeها را بالا می‌برد.

پس هدف این ریل دوگانه است:

```text
Strategic boundary
  + code that expresses the boundary
  + tests that preserve its rules
  + patterns justified by change pressure
= evolvable architecture
```

این هفته مسئله عمداً کوچک است: محاسبهٔ کارمزد Transfer روی سه Rail فرضی. قرار نیست Fees را به هفتمین Microservice تبدیل کنیم. فقط می‌خواهیم ببینیم چگونه یک Rule متغیر را تمیز، تست‌پذیر و قابل‌دفاع می‌کنیم.

## 4. تعریف‌های دقیق

### Clean Code

کدی که Intent و Rule را برای Maintainer بعدی آشکار می‌کند، تغییر محلی را ممکن می‌سازد و اثر جانبی و Dependency را پنهان نمی‌کند. Clean Code الزاماً کم‌خط‌ترین، پرکلاس‌ترین یا بدون Getterترین کد نیست.

### Code Smell

نشانه‌ای که احتمال یک مشکل طراحی را بالا می‌برد؛ نه حکم قطعی. `switch` می‌تواند Smell باشد، اما وقتی مجموعهٔ حالت‌ها کوچک، بسته و پایدار است ممکن است از Hierarchy چندکلاسه خواناتر باشد.

### Refactoring

تغییر ساختار داخلی کد بدون تغییر رفتار قابل مشاهده. اگر نرخ ACH را هم‌زمان عوض کنی، آن Commit فقط Refactor نیست؛ تغییر Rule دامینی نیز هست.

### Characterization Test

تستی که رفتار موجود را ثبت می‌کند، حتی اگر ساختار موجود را دوست نداشته باشیم. این تست «صحیح‌بودن تعرفه» را اثبات نمی‌کند؛ فقط مانع تغییر ناخواسته در جریان Refactor می‌شود.

### Strategy

یک خانواده از Algorithm/Policyهای قابل جایگزینی پشت یک Contract مشترک. Strategy زمانی مفید است که Ruleها مستقل تغییر کنند، تست جدا بخواهند یا Consumer نباید Selection logic را بداند.

### Factory/Registry

نقطه‌ای که تصمیم می‌گیرد برای یک ورودی کدام Strategy استفاده شود. Registry سادهٔ `Map<PaymentRail, FeePolicy>` برای این Kata معمولاً از Abstract Factory یا Reflection مناسب‌تر است.

## 5. Baseline عمداً بد

فایل زیر را باز کن:

```text
backend/banking-modulith/src/test/java/
com/example/corebankinglab/craftsmanship/week02/
LegacyTransferFeeCalculator.java
```

رفتار فعلی:

- `INTERNAL`: بدون کارمزد
- `ACH`: دو ده‌هزارم مبلغ، حداقل ۵۰٬۰۰۰ و حداکثر ۲۵۰٬۰۰۰ ریال
- `RTGS`: مبلغ ثابت ۲۰۰٬۰۰۰ ریال
- مشتری Preferred: نصف کارمزد محاسبه‌شده

این اعداد صرفاً Fixture آموزشی‌اند.

### Smell map اولیه

| محل | Smell | چرا مهم است؟ | آیا اصلاح قطعی است؟ |
|---|---|---|---|
| `String paymentRail` | Primitive Obsession / Type Code | غلط املایی فقط در Runtime دیده می‌شود و Vocabulary پخش می‌شود | معمولاً بله؛ Boundary parser جدا لازم است |
| اعداد داخل Method | Magic Literal | Rule قابل نام‌گذاری، Audit و تغییر مستقل نیست | بله؛ نام و محل مالک لازم است |
| `boolean preferredCustomer` | Flag Argument | Caller باید اثر Boolean را حدس بزند و دو رفتار در یک Signature پنهان می‌شود | اغلب؛ ابتدا Meaning را مدل کن |
| `if/else` Railها | Conditional complexity | Selection و Calculation در یک محل تغییر می‌کنند | مشروط؛ شاید Strategy، شاید `switch` تمیز |
| `long amountRials` | Primitive Obsession | Currency/Scale/overflow contract پنهان است | در Domain code بله؛ در Boundary خام ممکن است موقت باشد |
| Validation + Selection + Pricing | Mixed responsibilities | چند دلیل مستقل برای تغییر یک Method | بله، اما نه الزاماً یک Class برای هر خط |
| پیام Exception عمومی | Weak error model | Caller نوع Failure را Machine-readable نمی‌داند | در Product code بله؛ در Kata می‌تواند مرحله‌ای باشد |

Smell map پاسخ نهایی نیست. باید مشخص کنی کدام مورد در ۶۵ دقیقه واقعاً ارزش اصلاح دارد.

## 6. مدل تغییر مورد انتظار

فرض کن این سه Pressure واقعی وجود دارد:

1. تیم Payments Rail جدید اضافه می‌کند.
2. تیم Fees نرخ هر Rail را مستقل و با تاریخ مؤثر تغییر می‌دهد.
3. Product برای Customer segmentها Discount policy جدا دارد.

در این وضعیت سه محور تغییر داریم:

```text
rail selection ── fee calculation ── customer discount
```

اگر همه در یک Method بمانند، هر تغییر ممکن است بقیه را لمس کند. اگر هر محور را بی‌دلیل به ده Interface تبدیل کنیم، Navigation و Cognitive load زیاد می‌شود. هدف پیدا کردن **کوچک‌ترین جداسازی مفید** است.

## 7. مسیر هدایت‌شدهٔ Refactor

### گام 1 — Baseline را اجرا کن

```bash
cd backend/banking-modulith
mvn -Dtest=LegacyTransferFeeCalculatorCharacterizationTest test
```

تعداد Test و نتیجه را ثبت کن. روی Baseline قرمز Refactor نکن.

### گام 2 — شکاف رفتار را پیش از تغییر پیدا کن

حداقل دو رفتار ثبت‌نشده را شناسایی کن. نمونهٔ سؤال، نه پاسخ آماده:

- ورودی Blank چه می‌شود؟
- Preferred روی کارمزد صفر چه اثری دارد؟
- Case sensitivity بخشی از Contract است؟
- ضرب `amountRials * 2` در چه محدوده‌ای overflow می‌کند؟
- Discount قبل از Min/Max اعمال می‌شود یا بعد از آن؟

برای یک مورد Test اضافه کن. اگر Rule نامشخص است، Test را حدس نزن؛ آن را `OPEN` ثبت کن.

### گام 3 — Type Code را در Boundary محصور کن

یک Type معنادار برای Rail بساز. Parse کردن String باید در Boundary انجام شود؛ Core calculation نباید دائماً String را تفسیر کند.

Skeleton مجاز:

```java
enum PaymentRail {
    INTERNAL,
    ACH,
    RTGS
}
```

این هنوز Strategy نیست. پس از این گام تست‌ها باید سبز باشند.

### گام 4 — Magic Literalها را نام‌گذاری کن

نام باید Business meaning را آشکار کند، نه فقط Unit را:

- ضعیف: `NUMBER_50000`
- بهتر: `ACH_MINIMUM_FEE_RIALS`

اگر Rule به یک Strategy منتقل شد، Constant نیز کنار همان Policy بماند؛ یک `Constants` عمومی نساز.

### گام 5 — ابتدا ساده‌ترین گزینه را امتحان کن

یک `switch` expression کوچک روی enum بساز و Validation را از Selection جدا کن. سپس Diff را ببین. اگر کد اکنون روشن و Change pressure فرضی ضعیف است، همین می‌تواند پاسخ نهایی باشد.

```java
return switch (rail) {
    // policies remain explicit here
};
```

امتیاز این تمرین به استفادهٔ اجباری از Strategy وابسته نیست؛ به کیفیت تصمیم وابسته است.

### گام 6 — در صورت توجیه، Strategy را معرفی کن

Contract باید با زبان Domain حرف بزند و کوچک باشد:

```java
interface TransferFeePolicy {
    long calculateFor(long amountRials);
}
```

این Skeleton پاسخ کامل نیست. باید تصمیم بگیری:

- آیا `long` فعلاً می‌ماند یا `Money` Week 01 استفاده می‌شود؟
- آیا Rail بخشی از Strategy است یا فقط Key رجیستری؟
- Discount داخل Strategy است یا یک Policy مستقل بعد از Base fee؟
- Unsupported rail در Parser رد می‌شود یا Registry؟

برای هر Rail فقط وقتی Class جدا بساز که Rule مستقل، نام‌پذیر و قابل‌تست باشد.

### گام 7 — Selection را متمرکز کن

به‌جای `if/else` تکرارشونده در Callerها، یک Registry/Factory کوچک داشته باش. شرایط قبولی:

- همهٔ Strategyها هنگام ساخت Registry ثبت شوند.
- Duplicate key یا Missing policy Fail-fast باشد.
- Registry منطق محاسبهٔ کارمزد را مالک نشود.
- Reflection، Classpath scanning یا DI پیچیده برای سه Policy وارد نکن.

### گام 8 — Flag را به مفهوم تبدیل کن

`preferredCustomer=true` نام یک Pricing decision نیست. گزینه‌ها را مقایسه کن:

1. `CustomerPricingProfile` به‌عنوان enum/Value Object
2. `DiscountPolicy` مستقل و قابل Composition
3. دو Method صریح، اگر فقط دو رفتار ثابت داریم

نباید هم‌زمان تمام گزینه‌ها را پیاده‌سازی کنی. یکی را با دلیل انتخاب کن.

### گام 9 — Testها را بر اساس رفتار سازمان بده

Test name باید Rule را بیان کند، نه Method را:

- ضعیف: `testCalculate2`
- بهتر: `achFeeIsCappedAtTheMaximum`

حداقل این دسته‌ها را نگه دار:

- یک Test مستقل برای هر Rail
- Min/inside/max برای ACH
- Discount behavior
- Unsupported rail
- non-positive amount
- Edge Case انتخابی تو

### گام 10 — Diff را بخوان

پیش از اعلام پایان، پاسخ بده:

- تعداد Branchها کمتر شد یا فقط جابه‌جا شد؟
- Ruleها نزدیک‌تر به نام دامینی خود هستند؟
- اضافه‌کردن Rail جدید چند فایل را تغییر می‌دهد؟
- آیا یک Class فقط برای عبور دادن یک Method ساخته‌ای؟
- تست‌ها Implementation را قفل کرده‌اند یا Behavior را؟

## 8. Strategy یا `switch`؟

| Force | `switch` تمیز | Strategy + Registry |
|---|---|---|
| حالت‌ها کم و بسته‌اند | مناسب | ممکن است Over-design باشد |
| Ruleها مستقل و پرجزئیات‌اند | زود شلوغ می‌شود | مناسب‌تر |
| تیم‌های جدا Ruleها را تغییر می‌دهند | Merge hotspot | Ownership بهتر |
| انتخاب Runtime/Configuration است | پیچیده‌تر | Registry مناسب |
| نیاز به Test جدا برای هر Rule | ممکن ولی متمرکز | طبیعی‌تر |
| Navigation cost مهم است | کمتر | بیشتر |

Pattern Decision باید به Forces همین مسئله پاسخ دهد؛ نه تعریف کتابی Strategy.

## 9. مرز Clean Code و معماری

Refactor این Kata حق ندارد نتیجه‌گیری کند که Fees باید Microservice مستقل باشد. این‌ها سطوح متفاوت‌اند:

| تصمیم | سطح |
|---|---|
| نام Type و Method | Code design |
| Strategy برای Rule متغیر | Object/module design |
| Module API برای محاسبهٔ Fee | Application architecture |
| Bounded Context مستقل Fees | Strategic DDD |
| Deployable Fee Service | Deployment/operational architecture |

تمیزی کد Evidence مفید برای Boundary است، اما به‌تنهایی Boundary کسب‌وکاری یا Deployment را اثبات نمی‌کند.

## 10. تمرین مستقل

[Day 08 Exercise](../exercises/day-08-transfer-fee-refactoring.md) را انجام بده. این درس Skeleton و مسیر را داده است؛ پیاده‌سازی نهایی، نام Typeها و Pattern Decision باید متعلق به تو باشد.

## 11. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| Baseline و Characterization evidence | ۲ |
| Smell Map دقیق و غیرشعاری | ۲ |
| Refactor مرحله‌ای با تست سبز | ۲ |
| Strategy/Factory decision با Alternative و Cost | ۲ |
| Edge Test و Self-review صادقانه | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. استفاده از سه Pattern بدون توضیح Forces حداکثر ۵ می‌گیرد؛ راه‌حل سادهٔ مستدل می‌تواند امتیاز کامل بگیرد.

## 12. آزمون خروج

درس و کد را ببند و [Day 08 Exit Ticket](../quizzes/day-08-exit-ticket.md) را بدون مراجعه پاسخ بده.

## 13. منابع اصلی

- Martin Fowler, *Refactoring, 2nd Edition* و [Catalog of Refactorings](https://refactoring.com/catalog/) — برای گام‌های کوچک و حفظ رفتار
- [Replace Conditional with Polymorphism](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html) — گزینه‌ای برای Conditionalهای دارای Variation واقعی، نه نسخهٔ عمومی همهٔ `switch`ها
- [Tell, Don’t Ask](https://martinfowler.com/bliki/TellDontAsk.html) — برای نزدیک‌کردن رفتار و داده، همراه با هشدار خود Fowler دربارهٔ استفادهٔ افراطی
- Erich Gamma et al., *Design Patterns* — تعریف Strategy و Factory؛ نام Pattern جای تحلیل Forces را نمی‌گیرد
- Joshua Bloch, *Effective Java, 3rd Edition* — Type safety، Immutability و API design در Java
