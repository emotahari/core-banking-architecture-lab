# References — Week 02

این فهرست «کتابخانهٔ لینک» نیست. برای هر منبع، زمان و پرسش مطالعه مشخص شده است. ابتدا درس فارسی همان روز را بخوان و سپس فقط بخش تعیین‌شده را از مرجع اصلی بررسی کن.

## منبع پایهٔ Strategic DDD

### Domain-Driven Design Reference — Eric Evans

- منبع: [DDD Reference 2015](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- روزهای استفاده: ۱ تا ۴
- زمان کل پیشنهادی: ۳۵ دقیقه در طول هفته
- تمرکز:
  - Ubiquitous Language و Bounded Context
  - Context Map
  - Customer/Supplier
  - Conformist
  - Anticorruption Layer
  - Open Host Service و Published Language
- پرسش مطالعه: این Pattern کدام رابطهٔ قدرت، وابستگی مدل یا نیاز ترجمه را آشکار می‌کند؟

این Reference خلاصهٔ رسمی الگوهای کتاب Eric Evans است. تعریف‌ها در درس‌ها بازنویسی و برای بانک مثال‌سازی شده‌اند؛ متن مرجع جای Discovery محلی بانک را نمی‌گیرد.

## منابع رسمی Spring Modulith 2.1.0

### Fundamentals

- منبع: [Spring Modulith Fundamentals](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- روز استفاده: ۵
- زمان: ۱۵ دقیقه
- فقط این بخش‌ها:
  - Application Modules
  - Simple و Advanced Application Modules
  - Explicit Application Module Dependencies
  - Named Interfaces
- باید بتوانی پاسخ بدهی:
  - Provided Interface، Internal Implementation و Required Interface چیست؟
  - چرا Package اصلی Module API و Subpackageها Internal محسوب می‌شوند؟
  - `allowedDependencies` چه چیزی را کنترل می‌کند؟
  - عبارت `module :: named-interface` چه معنایی دارد؟

### Verification

- منبع: [Verifying Application Module Structure](https://docs.spring.io/spring-modulith/reference/verification.html)
- روز استفاده: ۶
- زمان: ۸ دقیقه
- تمرکز:
  - نبودن Cycle بین Moduleها
  - ممنوعیت دسترسی به Internal Package
  - کنترل Explicit Dependency
  - تفاوت `verify()` و `detectViolations()`

### Module Testing

- منبع: [Integration Testing Application Modules](https://docs.spring.io/spring-modulith/reference/testing.html)
- روز استفاده: ۶
- زمان: ۱۰ دقیقه
- تمرکز:
  - `@ApplicationModuleTest`
  - `STANDALONE`
  - `DIRECT_DEPENDENCIES`
  - `ALL_DEPENDENCIES`
- پرسش مطالعه: زیادشدن Dependency لازم برای Bootstrap چه نشانه‌ای دربارهٔ Coupling می‌دهد؟

### نسخه و وضعیت پروژه

- منبع: [Spring Modulith Reference 2.1.0](https://docs.spring.io/spring-modulith/reference/index.html)
- هدف: کنترل نسخهٔ Stable و BOM مورد استفاده در `pom.xml`

## مرجع بانکی

### BIAN Service Landscape 14.0

- منبع: [BIAN Service Landscape](https://bian.org/deliverables/service-landscape/)
- روز استفاده: ۱ و ۷
- زمان: ۱۰ دقیقه
- هدف:
  - Gap Check نام‌ها و مسئولیت‌ها
  - مقایسهٔ فرضیهٔ Domain Map با Reference Landscape
- ممنوع:
  - تبدیل هر Service Domain به یک Bounded Context یا Microservice
  - کپی‌کردن کل Landscape به‌عنوان معماری بانک

BIAN 14.0 در فوریهٔ ۲۰۲۶ منتشر شده است. در این هفته از آن به‌عنوان Reference Structure استفاده می‌کنیم، نه Deployment Blueprint.

## ترتیب مطالعه برحسب روز

| روز | منبع | بخش | سقف زمان |
|---|---|---|---:|
| ۱ | DDD Reference + BIAN | Domain/Core Domain و Gap Check | ۱۰ دقیقه |
| ۲ | DDD Reference | Ubiquitous Language و Bounded Context | ۸ دقیقه |
| ۳ | DDD Reference | Context Map Patterns | ۱۲ دقیقه |
| ۴ | درس فارسی + Artifactها | Ownership و Authority | بدون مطالعهٔ اضافه |
| ۵ | Spring Modulith Fundamentals | Module/API/Internal/Dependency | ۱۵ دقیقه |
| ۶ | Verification + Testing | `verify()` و Module Test | ۱۸ دقیقه |
| ۷ | BIAN + Artifactهای خودت | Gap Check نهایی | ۵ دقیقه |

## قواعد استناد در Artifactها

- Fact برگرفته از مرجع را با لینک ثبت کن.
- تصمیم بانک را به مرجع نسبت نده؛ آن را `Decision` و دلیلش را Forces بنویس.
- برداشت اثبات‌نشده را `Hypothesis` علامت بزن.
- موضوع نیازمند نظر خبره یا مقررات را `Open Question` نگه دار.
- هیچ داده، نام مشتری، Schema یا کد واقعی بانک در مخزن عمومی قرار نده.
