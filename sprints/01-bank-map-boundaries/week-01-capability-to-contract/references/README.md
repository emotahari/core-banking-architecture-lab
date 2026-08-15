# References — Week 01

- Last checked: 15 August 2026
- Rule: منبع برای پاسخ‌دادن به سؤال روز خوانده می‌شود؛ نه برای گشتن بی‌هدف یا Copy کردن Blueprint.

## مسیر روزانه

| روز | منبع | بخش/هدف | بودجه |
|---|---|---|---:|
| 01 | درس Synthesised + BIAN overview | زبان پایه و نقش BIAN | داخل بودجهٔ درس |
| 02 | TOGAF Business Capabilities | Capability در برابر راه‌حل | ۵ دقیقه |
| 03 | Traceability lesson | Intent، Fact و Owner | داخل درس |
| 04 | Parnas/Fowler references | Information Hiding و Coupling | ۵ دقیقه |
| 05 | BIAN 14 Portal/Release Notes | Gap Check پس از Map محلی | ۲۰ دقیقه |
| 06 | Java BigDecimal/Currency docs | Equality، Scale و Rounding | ۵ دقیقه |
| 08 | Fowler Refactoring catalog | Refactor مرحله‌ای | ۵ دقیقه |
| 09 | Source Register پروندهٔ UPI | Fact/Inference/Unknown | داخل ۴۵ دقیقه |

## اجباری — معماری و BIAN

### 1. TOGAF Business Capabilities

- مرجع: https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html
- استفاده: Capability به‌عنوان توانایی پایدار کسب‌وکار؛ نه Process/System
- قرار نیست: کل TOGAF خوانده یا Capability Map به Architecture کامل تبدیل شود.

### 2. BIAN Service Landscape 14.0

- مرجع: https://bian.org/deliverables/service-landscape/
- استفاده: شناخت نقش Service Landscape و ورود به Repository نسخهٔ 14
- زمان: ۱۰ دقیقه
- قرار نیست: کل Landscape حفظ یا هر Service Domain به Microservice تبدیل شود.

### 3. BIAN 14.0 Release Notes

- مرجع: https://bian.org/wp-content/uploads/2026/02/BIAN-v14.0-Release-Notes-v1.0_-Final-Version.pdf
- بخش: صفحات ۶ تا ۹ و جدول Metrics
- استفاده: فهم Artifactها، شیوهٔ مدل‌سازی و محدودیت نسخه
- زمان: ۱۵ دقیقه
- دادهٔ کنترل‌شدهٔ دوره: ۳۲۲ Service Domain، ۳۸ Business Domain، ۵۸۶ Business Capability و ۲۴۲ Semantic API

### 4. BIAN 14 Architecture Portal

- مرجع: https://bian.org/servicelandscape-14-0-0/
- استفاده در Day 05: Gap Check برای Capability Map ساخته‌شده
- زمان: ۲۰ دقیقه
- روش: ابتدا Map خودمان، سپس جست‌وجوی BIAN؛ نه برعکس.

## اجباری — طراحی کد

### Java BigDecimal

- مرجع: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/BigDecimal.html
- استفاده: تفاوت `equals` و `compareTo`، Scale و RoundingMode
- هشدار: انتخاب Scale دامینی از مستند Java استخراج نمی‌شود.

### Java Currency

- مرجع: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Currency.html
- استفاده: نمایش Type-safe کد Currency
- هشدار: Fraction digits پیش‌فرض Currency جای Rule محصول/حسابداری نیست.

### Martin Fowler — Refactoring Catalog

- مرجع: https://refactoring.com/catalog/
- استفاده: گام کوچک و حفظ رفتار
- مورد مرتبط: https://refactoring.com/catalog/replacePrimitiveWithObject.html

## مرجع فنی محیط

### Spring Boot 4.1 System Requirements

- مرجع: https://docs.spring.io/spring-boot/system-requirements.html
- دلیل: کنترل Java و Maven موردنیاز
- تصمیم پروژه: Java 21

### Spring Modulith

- مرجع: https://spring.io/projects/spring-modulith
- دلیل: آماده‌سازی Week 02 و فهم Module دارای API آشکار و Internal implementation

## پروندهٔ UPI

Source Register کامل، برچسب Fact/Inference و تاریخ کنترل داخل [UPI Case File](../case-studies/week-01-upi-fa.md) است. منابع اصلی:

- https://www.npci.org.in/product/upi/about-upi
- https://www.npci.org.in/product/upi/product-statistics
- https://www.npci.org.in/circulars/upi
- https://www.rbi.org.in/commonman/Upload/English/Content/PDFs/English12052026.pdf

## تکمیلی

- Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* — Information Hiding
- Martin Fowler, *Refactoring, 2nd Edition*
- Eric Evans, *Domain-Driven Design* — Bounded Context و Value Object
- Joshua Bloch, *Effective Java, 3rd Edition* — Immutability، factories و equals/hashCode

## سیاست منبع

- منبع اصلی برای Factهای نسخه‌ای اولویت دارد.
- متن درس Synthesise استاد است و جای کپی متن مرجع را نمی‌گیرد.
- هر Fact متغیر با تاریخ کنترل ثبت می‌شود.
- Domain/Context map بیرونی یک Hypothesis است، نه Fact سازمانی.
- اطلاعات غیرعمومی Tech stack با `UNKNOWN` ثبت می‌شود؛ با حدس پر نمی‌شود.

