<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">References</span> — <span dir="ltr">Week 01</span>

- <span dir="ltr">Last checked: 15 August 2026</span>
- <span dir="ltr">Rule:</span> منبع برای پاسخ‌دادن به سؤال روز خوانده می‌شود؛ نه برای گشتن بی‌هدف یا <span dir="ltr">Copy</span> کردن <span dir="ltr">Blueprint.</span>

## مسیر روزانه

| روز | منبع | بخش/هدف | بودجه |
|---|---|---|---:|
| 01 | درس <span dir="ltr">Synthesised</span> + <span dir="ltr">BIAN overview</span> | زبان پایه و نقش <span dir="ltr">BIAN</span> | داخل بودجهٔ درس |
| 02 | <span dir="ltr">TOGAF Business Capabilities</span> | <span dir="ltr">Capability</span> در برابر راه‌حل | ۵ دقیقه |
| 03 | <span dir="ltr">Traceability lesson</span> | <span dir="ltr">Intent</span>، <span dir="ltr">Fact</span> و <span dir="ltr">Owner</span> | داخل درس |
| 04 | <span dir="ltr">Parnas/Fowler references</span> | <span dir="ltr">Information Hiding</span> و <span dir="ltr">Coupling</span> | ۵ دقیقه |
| 05 | <span dir="ltr">BIAN 14 Portal/Release Notes</span> | <span dir="ltr">Gap Check</span> پس از <span dir="ltr">Map</span> محلی | ۲۰ دقیقه |
| 06 | <span dir="ltr">Java BigDecimal/Currency docs</span> | <span dir="ltr">Equality</span>، <span dir="ltr">Scale</span> و <span dir="ltr">Rounding</span> | ۵ دقیقه |
| 08 | <span dir="ltr">Fowler Refactoring catalog</span> | <span dir="ltr">Refactor</span> مرحله‌ای | ۵ دقیقه |
| 09 | <span dir="ltr">Source Register</span> پروندهٔ <span dir="ltr">UPI</span> | <span dir="ltr">Fact/Inference/Unknown</span> | داخل ۴۵ دقیقه |

## اجباری — معماری و <span dir="ltr">BIAN</span>

### <span dir="ltr">1. TOGAF Business Capabilities</span>

- مرجع: https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html
- استفاده: <span dir="ltr">Capability</span> به‌عنوان توانایی پایدار کسب‌وکار؛ نه <span dir="ltr">Process/System</span>
- قرار نیست: کل <span dir="ltr">TOGAF</span> خوانده یا <span dir="ltr">Capability Map</span> به <span dir="ltr">Architecture</span> کامل تبدیل شود.

### <span dir="ltr">2. BIAN Service Landscape 14.0</span>

- مرجع: https://bian.org/deliverables/service-landscape/
- استفاده: شناخت نقش <span dir="ltr">Service Landscape</span> و ورود به <span dir="ltr">Repository</span> نسخهٔ 14
- زمان: ۱۰ دقیقه
- قرار نیست: کل <span dir="ltr">Landscape</span> حفظ یا هر <span dir="ltr">Service Domain</span> به <span dir="ltr">Microservice</span> تبدیل شود.

### <span dir="ltr">3. BIAN 14.0 Release Notes</span>

- مرجع: https://bian.org/wp-content/uploads/2026/02/BIAN-v14.0-Release-Notes-v1.0_-Final-Version.pdf
- بخش: صفحات ۶ تا ۹ و جدول <span dir="ltr">Metrics</span>
- استفاده: فهم <span dir="ltr">Artifact</span>ها، شیوهٔ مدل‌سازی و محدودیت نسخه
- زمان: ۱۵ دقیقه
- دادهٔ کنترل‌شدهٔ دوره: ۳۲۲ <span dir="ltr">Service Domain</span>، ۳۸ <span dir="ltr">Business Domain</span>، ۵۸۶ <span dir="ltr">Business Capability</span> و ۲۴۲ <span dir="ltr">Semantic API</span>

### <span dir="ltr">4. BIAN 14 Architecture Portal</span>

- مرجع: https://bian.org/servicelandscape-14-0-0/
- استفاده در <span dir="ltr">Day 05: Gap Check</span> برای <span dir="ltr">Capability Map</span> ساخته‌شده
- زمان: ۲۰ دقیقه
- روش: ابتدا <span dir="ltr">Map</span> خودمان، سپس جست‌وجوی <span dir="ltr">BIAN</span>؛ نه برعکس.

## اجباری — طراحی کد

### <span dir="ltr">Java BigDecimal</span>

- مرجع: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/BigDecimal.html
- استفاده: تفاوت <span dir="ltr">`equals`</span> و <span dir="ltr">`compareTo`</span>، <span dir="ltr">Scale</span> و <span dir="ltr">RoundingMode</span>
- هشدار: انتخاب <span dir="ltr">Scale</span> دامینی از مستند <span dir="ltr">Java</span> استخراج نمی‌شود.

### <span dir="ltr">Java Currency</span>

- مرجع: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Currency.html
- استفاده: نمایش <span dir="ltr">Type-safe</span> کد <span dir="ltr">Currency</span>
- هشدار: <span dir="ltr">Fraction digits</span> پیش‌فرض <span dir="ltr">Currency</span> جای <span dir="ltr">Rule</span> محصول/حسابداری نیست.

### <span dir="ltr">Martin Fowler</span> — <span dir="ltr">Refactoring Catalog</span>

- مرجع: https://refactoring.com/catalog/
- استفاده: گام کوچک و حفظ رفتار
- مورد مرتبط: https://refactoring.com/catalog/replacePrimitiveWithObject.html

## مرجع فنی محیط

### <span dir="ltr">Spring Boot 4.1 System Requirements</span>

- مرجع: https://docs.spring.io/spring-boot/system-requirements.html
- دلیل: کنترل <span dir="ltr">Java</span> و <span dir="ltr">Maven</span> موردنیاز
- تصمیم پروژه: <span dir="ltr">Java 21</span>

### <span dir="ltr">Spring Modulith</span>

- مرجع: https://spring.io/projects/spring-modulith
- دلیل: آماده‌سازی <span dir="ltr">Week 02</span> و فهم <span dir="ltr">Module</span> دارای <span dir="ltr">API</span> آشکار و <span dir="ltr">Internal implementation</span>

## پروندهٔ <span dir="ltr">UPI</span>

<span dir="ltr">Source Register</span> کامل، برچسب <span dir="ltr">Fact/Inference</span> و تاریخ کنترل داخل [<span dir="ltr">UPI Case File</span>](../case-studies/week-01-upi-fa.md) است. منابع اصلی:

- https://www.npci.org.in/product/upi/about-upi
- https://www.npci.org.in/product/upi/product-statistics
- https://www.npci.org.in/circulars/upi
- https://www.rbi.org.in/commonman/Upload/English/Content/PDFs/English12052026.pdf

## تکمیلی

- <span dir="ltr">Parnas</span>, *<span dir="ltr">On the Criteria To Be Used in Decomposing Systems into Modules</span>* — <span dir="ltr">Information Hiding</span>
- <span dir="ltr">Martin Fowler</span>, *<span dir="ltr">Refactoring</span>, <span dir="ltr">2nd Edition</span>*
- <span dir="ltr">Eric Evans</span>, *<span dir="ltr">Domain-Driven Design</span>* — <span dir="ltr">Bounded Context</span> و <span dir="ltr">Value Object</span>
- <span dir="ltr">Joshua Bloch</span>, *<span dir="ltr">Effective Java</span>, <span dir="ltr">3rd Edition</span>* — <span dir="ltr">Immutability</span>، <span dir="ltr">factories</span> و <span dir="ltr">equals/hashCode</span>

## سیاست منبع

- منبع اصلی برای <span dir="ltr">Fact</span>های نسخه‌ای اولویت دارد.
- متن درس <span dir="ltr">Synthesise</span> استاد است و جای کپی متن مرجع را نمی‌گیرد.
- هر <span dir="ltr">Fact</span> متغیر با تاریخ کنترل ثبت می‌شود.
- <span dir="ltr">Domain/Context map</span> بیرونی یک <span dir="ltr">Hypothesis</span> است، نه <span dir="ltr">Fact</span> سازمانی.
- اطلاعات غیرعمومی <span dir="ltr">Tech stack</span> با <span dir="ltr">`UNKNOWN`</span> ثبت می‌شود؛ با حدس پر نمی‌شود.


</div>
