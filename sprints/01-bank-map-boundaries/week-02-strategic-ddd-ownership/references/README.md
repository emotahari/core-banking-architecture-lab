<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">References</bdi> — <bdi dir="ltr">Week 02</bdi>

این فهرست «کتابخانهٔ لینک» نیست. برای هر منبع، زمان و پرسش مطالعه مشخص شده است. ابتدا درس فارسی همان روز را بخوان و سپس فقط بخش تعیین‌شده را از مرجع اصلی بررسی کن.

## منبع پایهٔ <bdi dir="ltr">Strategic DDD</bdi>

### <bdi dir="ltr">Domain-Driven Design Reference</bdi> — <bdi dir="ltr">Eric Evans</bdi>

- منبع: [<bdi dir="ltr">DDD Reference 2015</bdi>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- روزهای استفاده: ۱ تا ۴
- زمان کل پیشنهادی: ۳۵ دقیقه در طول هفته
- تمرکز:
  - <bdi dir="ltr">Ubiquitous Language</bdi> و <bdi dir="ltr">Bounded Context</bdi>
  - <bdi dir="ltr">Context Map</bdi>
  - <bdi dir="ltr">Customer/Supplier</bdi>
  - <bdi dir="ltr">Conformist</bdi>
  - <bdi dir="ltr">Anticorruption Layer</bdi>
  - <bdi dir="ltr">Open Host Service</bdi> و <bdi dir="ltr">Published Language</bdi>
- پرسش مطالعه: این <bdi dir="ltr">Pattern</bdi> کدام رابطهٔ قدرت، وابستگی مدل یا نیاز ترجمه را آشکار می‌کند؟

این <bdi dir="ltr">Reference</bdi> خلاصهٔ رسمی الگوهای کتاب <bdi dir="ltr">Eric Evans</bdi> است. تعریف‌ها در درس‌ها بازنویسی و برای بانک مثال‌سازی شده‌اند؛ متن مرجع جای <bdi dir="ltr">Discovery</bdi> محلی بانک را نمی‌گیرد.

## منابع رسمی <bdi dir="ltr">Spring Modulith 2.1.0</bdi>

### <bdi dir="ltr">Fundamentals</bdi>

- منبع: [<bdi dir="ltr">Spring Modulith Fundamentals</bdi>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- روز استفاده: ۵
- زمان: ۱۵ دقیقه
- فقط این بخش‌ها:
  - <bdi dir="ltr">Application Modules</bdi>
  - <bdi dir="ltr">Simple</bdi> و <bdi dir="ltr">Advanced Application Modules</bdi>
  - <bdi dir="ltr">Explicit Application Module Dependencies</bdi>
  - <bdi dir="ltr">Named Interfaces</bdi>
- باید بتوانی پاسخ بدهی:
  - <bdi dir="ltr">Provided Interface</bdi>، <bdi dir="ltr">Internal Implementation</bdi> و <bdi dir="ltr">Required Interface</bdi> چیست؟
  - چرا <bdi dir="ltr">Package</bdi> اصلی <bdi dir="ltr">Module API</bdi> و <bdi dir="ltr">Subpackage</bdi>ها <bdi dir="ltr">Internal</bdi> محسوب می‌شوند؟
  - <bdi dir="ltr">`allowedDependencies`</bdi> چه چیزی را کنترل می‌کند؟
  - عبارت <bdi dir="ltr">`module :: named-interface`</bdi> چه معنایی دارد؟

### <bdi dir="ltr">Verification</bdi>

- منبع: [<bdi dir="ltr">Verifying Application Module Structure</bdi>](https://docs.spring.io/spring-modulith/reference/verification.html)
- روز استفاده: ۶
- زمان: ۸ دقیقه
- تمرکز:
  - نبودن <bdi dir="ltr">Cycle</bdi> بین <bdi dir="ltr">Module</bdi>ها
  - ممنوعیت دسترسی به <bdi dir="ltr">Internal Package</bdi>
  - کنترل <bdi dir="ltr">Explicit Dependency</bdi>
  - تفاوت <bdi dir="ltr">`verify()`</bdi> و <bdi dir="ltr">`detectViolations()`</bdi>

### <bdi dir="ltr">Module Testing</bdi>

- منبع: [<bdi dir="ltr">Integration Testing Application Modules</bdi>](https://docs.spring.io/spring-modulith/reference/testing.html)
- روز استفاده: ۶
- زمان: ۱۰ دقیقه
- تمرکز:
  - <bdi dir="ltr">`@ApplicationModuleTest`</bdi>
  - <bdi dir="ltr">`STANDALONE`</bdi>
  - <bdi dir="ltr">`DIRECT_DEPENDENCIES`</bdi>
  - <bdi dir="ltr">`ALL_DEPENDENCIES`</bdi>
- پرسش مطالعه: زیادشدن <bdi dir="ltr">Dependency</bdi> لازم برای <bdi dir="ltr">Bootstrap</bdi> چه نشانه‌ای دربارهٔ <bdi dir="ltr">Coupling</bdi> می‌دهد؟

### نسخه و وضعیت پروژه

- منبع: [<bdi dir="ltr">Spring Modulith Reference 2.1.0</bdi>](https://docs.spring.io/spring-modulith/reference/index.html)
- هدف: کنترل نسخهٔ <bdi dir="ltr">Stable</bdi> و <bdi dir="ltr">BOM</bdi> مورد استفاده در <bdi dir="ltr">`pom.xml`</bdi>

## مرجع بانکی

### <bdi dir="ltr">BIAN Service Landscape 14.0</bdi>

- منبع: [<bdi dir="ltr">BIAN Service Landscape</bdi>](https://bian.org/deliverables/service-landscape/)
- روز استفاده: ۱ و ۷
- زمان: ۱۰ دقیقه
- هدف:
  - <bdi dir="ltr">Gap Check</bdi> نام‌ها و مسئولیت‌ها
  - مقایسهٔ فرضیهٔ <bdi dir="ltr">Domain Map</bdi> با <bdi dir="ltr">Reference Landscape</bdi>
- ممنوع:
  - تبدیل هر <bdi dir="ltr">Service Domain</bdi> به یک <bdi dir="ltr">Bounded Context</bdi> یا <bdi dir="ltr">Microservice</bdi>
  - کپی‌کردن کل <bdi dir="ltr">Landscape</bdi> به‌عنوان معماری بانک

<bdi dir="ltr">BIAN 14.0</bdi> در فوریهٔ ۲۰۲۶ منتشر شده است. در این هفته از آن به‌عنوان <bdi dir="ltr">Reference Structure</bdi> استفاده می‌کنیم، نه <bdi dir="ltr">Deployment Blueprint.</bdi>

## ترتیب مطالعه برحسب روز

| روز | منبع | بخش | سقف زمان |
|---|---|---|---:|
| ۱ | <bdi dir="ltr">DDD Reference</bdi> + <bdi dir="ltr">BIAN</bdi> | <bdi dir="ltr">Domain/Core Domain</bdi> و <bdi dir="ltr">Gap Check</bdi> | ۱۰ دقیقه |
| ۲ | <bdi dir="ltr">DDD Reference</bdi> | <bdi dir="ltr">Ubiquitous Language</bdi> و <bdi dir="ltr">Bounded Context</bdi> | ۸ دقیقه |
| ۳ | <bdi dir="ltr">DDD Reference</bdi> | <bdi dir="ltr">Context Map Patterns</bdi> | ۱۲ دقیقه |
| ۴ | درس فارسی + <bdi dir="ltr">Artifact</bdi>ها | <bdi dir="ltr">Ownership</bdi> و <bdi dir="ltr">Authority</bdi> | بدون مطالعهٔ اضافه |
| ۵ | <bdi dir="ltr">Spring Modulith Fundamentals</bdi> | <bdi dir="ltr">Module/API/Internal/Dependency</bdi> | ۱۵ دقیقه |
| ۶ | <bdi dir="ltr">Verification</bdi> + <bdi dir="ltr">Testing</bdi> | <bdi dir="ltr">`verify()`</bdi> و <bdi dir="ltr">Module Test</bdi> | ۱۸ دقیقه |
| ۷ | <bdi dir="ltr">BIAN</bdi> + <bdi dir="ltr">Artifact</bdi>های خودت | <bdi dir="ltr">Gap Check</bdi> نهایی | ۵ دقیقه |
| ۸ | <bdi dir="ltr">Fowler Refactoring catalog</bdi> + درس فارسی | <bdi dir="ltr">Refactor</bdi>، <bdi dir="ltr">Strategy decision</bdi> و <bdi dir="ltr">Tell-Don</bdi>’<bdi dir="ltr">t-Ask</bdi> | ۱۰ دقیقه داخل بودجهٔ افزوده |
| ۹ | منابع رسمی <bdi dir="ltr">Monzo</bdi> + <bdi dir="ltr">FCA</bdi> داخل <bdi dir="ltr">Case File</bdi> | <bdi dir="ltr">Timeline</bdi>، معماری جاری، شکست و درس انتقالی | لینک‌ها داخل پرونده |

## منابع افزودهٔ <bdi dir="ltr">Code Craft</bdi>

- [<bdi dir="ltr">Catalog of Refactorings</bdi>](https://refactoring.com/catalog/) — مرجع حرکت‌های کوچک و نام‌گذاری <bdi dir="ltr">Refactor</bdi>ها
- [<bdi dir="ltr">Replace Conditional with Polymorphism</bdi>](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html) — گزینهٔ مشروط برای <bdi dir="ltr">Variation</bdi> واقعی
- [<bdi dir="ltr">Tell</bdi>, <bdi dir="ltr">Don</bdi>’<bdi dir="ltr">t Ask</bdi>](https://martinfowler.com/bliki/TellDontAsk.html) — هم اصل و هم هشدار دربارهٔ استفادهٔ افراطی
- *<bdi dir="ltr">Design Patterns</bdi>* از <bdi dir="ltr">Gamma</bdi>, <bdi dir="ltr">Helm</bdi>, <bdi dir="ltr">Johnson</bdi> و <bdi dir="ltr">Vlissides</bdi> — تعریف <bdi dir="ltr">Strategy/Factory</bdi>
- *<bdi dir="ltr">Effective Java</bdi>, <bdi dir="ltr">3rd Edition</bdi>* از <bdi dir="ltr">Joshua Bloch</bdi> — <bdi dir="ltr">Type safety</bdi>، <bdi dir="ltr">Immutability</bdi> و <bdi dir="ltr">API design</bdi>

## منابع افزودهٔ پروندهٔ <bdi dir="ltr">Monzo</bdi>

<bdi dir="ltr">Source register</bdi> کامل و تاریخ کنترل در [پروندهٔ <bdi dir="ltr">Week 02</bdi>](../case-studies/week-02-monzo-fa.md) آمده است. برای ادعای جاری، نوشتهٔ ۲۰۱۶ را به‌تنهایی منبع <bdi dir="ltr">Technology stack</bdi> سال ۲۰۲۶ قرار نده.

## قواعد استناد در <bdi dir="ltr">Artifact</bdi>ها

- <bdi dir="ltr">Fact</bdi> برگرفته از مرجع را با لینک ثبت کن.
- تصمیم بانک را به مرجع نسبت نده؛ آن را <bdi dir="ltr">`Decision`</bdi> و دلیلش را <bdi dir="ltr">Forces</bdi> بنویس.
- برداشت اثبات‌نشده را <bdi dir="ltr">`Hypothesis`</bdi> علامت بزن.
- موضوع نیازمند نظر خبره یا مقررات را <bdi dir="ltr">`Open Question`</bdi> نگه دار.
- هیچ داده، نام مشتری، <bdi dir="ltr">Schema</bdi> یا کد واقعی بانک در مخزن عمومی قرار نده.

</div>
