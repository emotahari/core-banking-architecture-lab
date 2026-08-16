<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">References</span> — <span dir="ltr">Week 02</span>

این فهرست «کتابخانهٔ لینک» نیست. برای هر منبع، زمان و پرسش مطالعه مشخص شده است. ابتدا درس فارسی همان روز را بخوان و سپس فقط بخش تعیین‌شده را از مرجع اصلی بررسی کن.

## منبع پایهٔ <span dir="ltr">Strategic DDD</span>

### <span dir="ltr">Domain-Driven Design Reference</span> — <span dir="ltr">Eric Evans</span>

- منبع: [<span dir="ltr">DDD Reference 2015</span>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- روزهای استفاده: ۱ تا ۴
- زمان کل پیشنهادی: ۳۵ دقیقه در طول هفته
- تمرکز:
  - <span dir="ltr">Ubiquitous Language</span> و <span dir="ltr">Bounded Context</span>
  - <span dir="ltr">Context Map</span>
  - <span dir="ltr">Customer/Supplier</span>
  - <span dir="ltr">Conformist</span>
  - <span dir="ltr">Anticorruption Layer</span>
  - <span dir="ltr">Open Host Service</span> و <span dir="ltr">Published Language</span>
- پرسش مطالعه: این <span dir="ltr">Pattern</span> کدام رابطهٔ قدرت، وابستگی مدل یا نیاز ترجمه را آشکار می‌کند؟

این <span dir="ltr">Reference</span> خلاصهٔ رسمی الگوهای کتاب <span dir="ltr">Eric Evans</span> است. تعریف‌ها در درس‌ها بازنویسی و برای بانک مثال‌سازی شده‌اند؛ متن مرجع جای <span dir="ltr">Discovery</span> محلی بانک را نمی‌گیرد.

## منابع رسمی <span dir="ltr">Spring Modulith 2.1.0</span>

### <span dir="ltr">Fundamentals</span>

- منبع: [<span dir="ltr">Spring Modulith Fundamentals</span>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- روز استفاده: ۵
- زمان: ۱۵ دقیقه
- فقط این بخش‌ها:
  - <span dir="ltr">Application Modules</span>
  - <span dir="ltr">Simple</span> و <span dir="ltr">Advanced Application Modules</span>
  - <span dir="ltr">Explicit Application Module Dependencies</span>
  - <span dir="ltr">Named Interfaces</span>
- باید بتوانی پاسخ بدهی:
  - <span dir="ltr">Provided Interface</span>، <span dir="ltr">Internal Implementation</span> و <span dir="ltr">Required Interface</span> چیست؟
  - چرا <span dir="ltr">Package</span> اصلی <span dir="ltr">Module API</span> و <span dir="ltr">Subpackage</span>ها <span dir="ltr">Internal</span> محسوب می‌شوند؟
  - <span dir="ltr">`allowedDependencies`</span> چه چیزی را کنترل می‌کند؟
  - عبارت <span dir="ltr">`module :: named-interface`</span> چه معنایی دارد؟

### <span dir="ltr">Verification</span>

- منبع: [<span dir="ltr">Verifying Application Module Structure</span>](https://docs.spring.io/spring-modulith/reference/verification.html)
- روز استفاده: ۶
- زمان: ۸ دقیقه
- تمرکز:
  - نبودن <span dir="ltr">Cycle</span> بین <span dir="ltr">Module</span>ها
  - ممنوعیت دسترسی به <span dir="ltr">Internal Package</span>
  - کنترل <span dir="ltr">Explicit Dependency</span>
  - تفاوت <span dir="ltr">`verify()`</span> و <span dir="ltr">`detectViolations()`</span>

### <span dir="ltr">Module Testing</span>

- منبع: [<span dir="ltr">Integration Testing Application Modules</span>](https://docs.spring.io/spring-modulith/reference/testing.html)
- روز استفاده: ۶
- زمان: ۱۰ دقیقه
- تمرکز:
  - <span dir="ltr">`@ApplicationModuleTest`</span>
  - <span dir="ltr">`STANDALONE`</span>
  - <span dir="ltr">`DIRECT_DEPENDENCIES`</span>
  - <span dir="ltr">`ALL_DEPENDENCIES`</span>
- پرسش مطالعه: زیادشدن <span dir="ltr">Dependency</span> لازم برای <span dir="ltr">Bootstrap</span> چه نشانه‌ای دربارهٔ <span dir="ltr">Coupling</span> می‌دهد؟

### نسخه و وضعیت پروژه

- منبع: [<span dir="ltr">Spring Modulith Reference 2.1.0</span>](https://docs.spring.io/spring-modulith/reference/index.html)
- هدف: کنترل نسخهٔ <span dir="ltr">Stable</span> و <span dir="ltr">BOM</span> مورد استفاده در <span dir="ltr">`pom.xml`</span>

## مرجع بانکی

### <span dir="ltr">BIAN Service Landscape 14.0</span>

- منبع: [<span dir="ltr">BIAN Service Landscape</span>](https://bian.org/deliverables/service-landscape/)
- روز استفاده: ۱ و ۷
- زمان: ۱۰ دقیقه
- هدف:
  - <span dir="ltr">Gap Check</span> نام‌ها و مسئولیت‌ها
  - مقایسهٔ فرضیهٔ <span dir="ltr">Domain Map</span> با <span dir="ltr">Reference Landscape</span>
- ممنوع:
  - تبدیل هر <span dir="ltr">Service Domain</span> به یک <span dir="ltr">Bounded Context</span> یا <span dir="ltr">Microservice</span>
  - کپی‌کردن کل <span dir="ltr">Landscape</span> به‌عنوان معماری بانک

<span dir="ltr">BIAN 14.0</span> در فوریهٔ ۲۰۲۶ منتشر شده است. در این هفته از آن به‌عنوان <span dir="ltr">Reference Structure</span> استفاده می‌کنیم، نه <span dir="ltr">Deployment Blueprint.</span>

## ترتیب مطالعه برحسب روز

| روز | منبع | بخش | سقف زمان |
|---|---|---|---:|
| ۱ | <span dir="ltr">DDD Reference</span> + <span dir="ltr">BIAN</span> | <span dir="ltr">Domain/Core Domain</span> و <span dir="ltr">Gap Check</span> | ۱۰ دقیقه |
| ۲ | <span dir="ltr">DDD Reference</span> | <span dir="ltr">Ubiquitous Language</span> و <span dir="ltr">Bounded Context</span> | ۸ دقیقه |
| ۳ | <span dir="ltr">DDD Reference</span> | <span dir="ltr">Context Map Patterns</span> | ۱۲ دقیقه |
| ۴ | درس فارسی + <span dir="ltr">Artifact</span>ها | <span dir="ltr">Ownership</span> و <span dir="ltr">Authority</span> | بدون مطالعهٔ اضافه |
| ۵ | <span dir="ltr">Spring Modulith Fundamentals</span> | <span dir="ltr">Module/API/Internal/Dependency</span> | ۱۵ دقیقه |
| ۶ | <span dir="ltr">Verification</span> + <span dir="ltr">Testing</span> | <span dir="ltr">`verify()`</span> و <span dir="ltr">Module Test</span> | ۱۸ دقیقه |
| ۷ | <span dir="ltr">BIAN</span> + <span dir="ltr">Artifact</span>های خودت | <span dir="ltr">Gap Check</span> نهایی | ۵ دقیقه |
| ۸ | <span dir="ltr">Fowler Refactoring catalog</span> + درس فارسی | <span dir="ltr">Refactor</span>، <span dir="ltr">Strategy decision</span> و <span dir="ltr">Tell-Don</span>’<span dir="ltr">t-Ask</span> | ۱۰ دقیقه داخل بودجهٔ افزوده |
| ۹ | منابع رسمی <span dir="ltr">Monzo</span> + <span dir="ltr">FCA</span> داخل <span dir="ltr">Case File</span> | <span dir="ltr">Timeline</span>، معماری جاری، شکست و درس انتقالی | لینک‌ها داخل پرونده |

## منابع افزودهٔ <span dir="ltr">Code Craft</span>

- [<span dir="ltr">Catalog of Refactorings</span>](https://refactoring.com/catalog/) — مرجع حرکت‌های کوچک و نام‌گذاری <span dir="ltr">Refactor</span>ها
- [<span dir="ltr">Replace Conditional with Polymorphism</span>](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html) — گزینهٔ مشروط برای <span dir="ltr">Variation</span> واقعی
- [<span dir="ltr">Tell</span>, <span dir="ltr">Don</span>’<span dir="ltr">t Ask</span>](https://martinfowler.com/bliki/TellDontAsk.html) — هم اصل و هم هشدار دربارهٔ استفادهٔ افراطی
- *<span dir="ltr">Design Patterns</span>* از <span dir="ltr">Gamma</span>, <span dir="ltr">Helm</span>, <span dir="ltr">Johnson</span> و <span dir="ltr">Vlissides</span> — تعریف <span dir="ltr">Strategy/Factory</span>
- *<span dir="ltr">Effective Java</span>, <span dir="ltr">3rd Edition</span>* از <span dir="ltr">Joshua Bloch</span> — <span dir="ltr">Type safety</span>، <span dir="ltr">Immutability</span> و <span dir="ltr">API design</span>

## منابع افزودهٔ پروندهٔ <span dir="ltr">Monzo</span>

<span dir="ltr">Source register</span> کامل و تاریخ کنترل در [پروندهٔ <span dir="ltr">Week 02</span>](../case-studies/week-02-monzo-fa.md) آمده است. برای ادعای جاری، نوشتهٔ ۲۰۱۶ را به‌تنهایی منبع <span dir="ltr">Technology stack</span> سال ۲۰۲۶ قرار نده.

## قواعد استناد در <span dir="ltr">Artifact</span>ها

- <span dir="ltr">Fact</span> برگرفته از مرجع را با لینک ثبت کن.
- تصمیم بانک را به مرجع نسبت نده؛ آن را <span dir="ltr">`Decision`</span> و دلیلش را <span dir="ltr">Forces</span> بنویس.
- برداشت اثبات‌نشده را <span dir="ltr">`Hypothesis`</span> علامت بزن.
- موضوع نیازمند نظر خبره یا مقررات را <span dir="ltr">`Open Question`</span> نگه دار.
- هیچ داده، نام مشتری، <span dir="ltr">Schema</span> یا کد واقعی بانک در مخزن عمومی قرار نده.

</div>
