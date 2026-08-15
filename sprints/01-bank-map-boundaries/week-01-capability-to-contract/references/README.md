<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">References</bdi> — <bdi dir="ltr">Week 01</bdi>

- <bdi dir="ltr">Last checked: 15 August 2026</bdi>
- <bdi dir="ltr">Rule:</bdi> منبع برای پاسخ‌دادن به سؤال روز خوانده می‌شود؛ نه برای گشتن بی‌هدف یا <bdi dir="ltr">Copy</bdi> کردن <bdi dir="ltr">Blueprint.</bdi>

## مسیر روزانه

| روز | منبع | بخش/هدف | بودجه |
|---|---|---|---:|
| 01 | درس <bdi dir="ltr">Synthesised</bdi> + <bdi dir="ltr">BIAN overview</bdi> | زبان پایه و نقش <bdi dir="ltr">BIAN</bdi> | داخل بودجهٔ درس |
| 02 | <bdi dir="ltr">TOGAF Business Capabilities</bdi> | <bdi dir="ltr">Capability</bdi> در برابر راه‌حل | ۵ دقیقه |
| 03 | <bdi dir="ltr">Traceability lesson</bdi> | <bdi dir="ltr">Intent</bdi>، <bdi dir="ltr">Fact</bdi> و <bdi dir="ltr">Owner</bdi> | داخل درس |
| 04 | <bdi dir="ltr">Parnas/Fowler references</bdi> | <bdi dir="ltr">Information Hiding</bdi> و <bdi dir="ltr">Coupling</bdi> | ۵ دقیقه |
| 05 | <bdi dir="ltr">BIAN 14 Portal/Release Notes</bdi> | <bdi dir="ltr">Gap Check</bdi> پس از <bdi dir="ltr">Map</bdi> محلی | ۲۰ دقیقه |
| 06 | <bdi dir="ltr">Java BigDecimal/Currency docs</bdi> | <bdi dir="ltr">Equality</bdi>، <bdi dir="ltr">Scale</bdi> و <bdi dir="ltr">Rounding</bdi> | ۵ دقیقه |
| 08 | <bdi dir="ltr">Fowler Refactoring catalog</bdi> | <bdi dir="ltr">Refactor</bdi> مرحله‌ای | ۵ دقیقه |
| 09 | <bdi dir="ltr">Source Register</bdi> پروندهٔ <bdi dir="ltr">UPI</bdi> | <bdi dir="ltr">Fact/Inference/Unknown</bdi> | داخل ۴۵ دقیقه |

## اجباری — معماری و <bdi dir="ltr">BIAN</bdi>

### <bdi dir="ltr">1. TOGAF Business Capabilities</bdi>

- مرجع: https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html
- استفاده: <bdi dir="ltr">Capability</bdi> به‌عنوان توانایی پایدار کسب‌وکار؛ نه <bdi dir="ltr">Process/System</bdi>
- قرار نیست: کل <bdi dir="ltr">TOGAF</bdi> خوانده یا <bdi dir="ltr">Capability Map</bdi> به <bdi dir="ltr">Architecture</bdi> کامل تبدیل شود.

### <bdi dir="ltr">2. BIAN Service Landscape 14.0</bdi>

- مرجع: https://bian.org/deliverables/service-landscape/
- استفاده: شناخت نقش <bdi dir="ltr">Service Landscape</bdi> و ورود به <bdi dir="ltr">Repository</bdi> نسخهٔ 14
- زمان: ۱۰ دقیقه
- قرار نیست: کل <bdi dir="ltr">Landscape</bdi> حفظ یا هر <bdi dir="ltr">Service Domain</bdi> به <bdi dir="ltr">Microservice</bdi> تبدیل شود.

### <bdi dir="ltr">3. BIAN 14.0 Release Notes</bdi>

- مرجع: https://bian.org/wp-content/uploads/2026/02/BIAN-v14.0-Release-Notes-v1.0_-Final-Version.pdf
- بخش: صفحات ۶ تا ۹ و جدول <bdi dir="ltr">Metrics</bdi>
- استفاده: فهم <bdi dir="ltr">Artifact</bdi>ها، شیوهٔ مدل‌سازی و محدودیت نسخه
- زمان: ۱۵ دقیقه
- دادهٔ کنترل‌شدهٔ دوره: ۳۲۲ <bdi dir="ltr">Service Domain</bdi>، ۳۸ <bdi dir="ltr">Business Domain</bdi>، ۵۸۶ <bdi dir="ltr">Business Capability</bdi> و ۲۴۲ <bdi dir="ltr">Semantic API</bdi>

### <bdi dir="ltr">4. BIAN 14 Architecture Portal</bdi>

- مرجع: https://bian.org/servicelandscape-14-0-0/
- استفاده در <bdi dir="ltr">Day 05: Gap Check</bdi> برای <bdi dir="ltr">Capability Map</bdi> ساخته‌شده
- زمان: ۲۰ دقیقه
- روش: ابتدا <bdi dir="ltr">Map</bdi> خودمان، سپس جست‌وجوی <bdi dir="ltr">BIAN</bdi>؛ نه برعکس.

## اجباری — طراحی کد

### <bdi dir="ltr">Java BigDecimal</bdi>

- مرجع: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/BigDecimal.html
- استفاده: تفاوت <bdi dir="ltr">`equals`</bdi> و <bdi dir="ltr">`compareTo`</bdi>، <bdi dir="ltr">Scale</bdi> و <bdi dir="ltr">RoundingMode</bdi>
- هشدار: انتخاب <bdi dir="ltr">Scale</bdi> دامینی از مستند <bdi dir="ltr">Java</bdi> استخراج نمی‌شود.

### <bdi dir="ltr">Java Currency</bdi>

- مرجع: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Currency.html
- استفاده: نمایش <bdi dir="ltr">Type-safe</bdi> کد <bdi dir="ltr">Currency</bdi>
- هشدار: <bdi dir="ltr">Fraction digits</bdi> پیش‌فرض <bdi dir="ltr">Currency</bdi> جای <bdi dir="ltr">Rule</bdi> محصول/حسابداری نیست.

### <bdi dir="ltr">Martin Fowler</bdi> — <bdi dir="ltr">Refactoring Catalog</bdi>

- مرجع: https://refactoring.com/catalog/
- استفاده: گام کوچک و حفظ رفتار
- مورد مرتبط: https://refactoring.com/catalog/replacePrimitiveWithObject.html

## مرجع فنی محیط

### <bdi dir="ltr">Spring Boot 4.1 System Requirements</bdi>

- مرجع: https://docs.spring.io/spring-boot/system-requirements.html
- دلیل: کنترل <bdi dir="ltr">Java</bdi> و <bdi dir="ltr">Maven</bdi> موردنیاز
- تصمیم پروژه: <bdi dir="ltr">Java 21</bdi>

### <bdi dir="ltr">Spring Modulith</bdi>

- مرجع: https://spring.io/projects/spring-modulith
- دلیل: آماده‌سازی <bdi dir="ltr">Week 02</bdi> و فهم <bdi dir="ltr">Module</bdi> دارای <bdi dir="ltr">API</bdi> آشکار و <bdi dir="ltr">Internal implementation</bdi>

## پروندهٔ <bdi dir="ltr">UPI</bdi>

<bdi dir="ltr">Source Register</bdi> کامل، برچسب <bdi dir="ltr">Fact/Inference</bdi> و تاریخ کنترل داخل [<bdi dir="ltr">UPI Case File</bdi>](../case-studies/week-01-upi-fa.md) است. منابع اصلی:

- https://www.npci.org.in/product/upi/about-upi
- https://www.npci.org.in/product/upi/product-statistics
- https://www.npci.org.in/circulars/upi
- https://www.rbi.org.in/commonman/Upload/English/Content/PDFs/English12052026.pdf

## تکمیلی

- <bdi dir="ltr">Parnas</bdi>, *<bdi dir="ltr">On the Criteria To Be Used in Decomposing Systems into Modules</bdi>* — <bdi dir="ltr">Information Hiding</bdi>
- <bdi dir="ltr">Martin Fowler</bdi>, *<bdi dir="ltr">Refactoring</bdi>, <bdi dir="ltr">2nd Edition</bdi>*
- <bdi dir="ltr">Eric Evans</bdi>, *<bdi dir="ltr">Domain-Driven Design</bdi>* — <bdi dir="ltr">Bounded Context</bdi> و <bdi dir="ltr">Value Object</bdi>
- <bdi dir="ltr">Joshua Bloch</bdi>, *<bdi dir="ltr">Effective Java</bdi>, <bdi dir="ltr">3rd Edition</bdi>* — <bdi dir="ltr">Immutability</bdi>، <bdi dir="ltr">factories</bdi> و <bdi dir="ltr">equals/hashCode</bdi>

## سیاست منبع

- منبع اصلی برای <bdi dir="ltr">Fact</bdi>های نسخه‌ای اولویت دارد.
- متن درس <bdi dir="ltr">Synthesise</bdi> استاد است و جای کپی متن مرجع را نمی‌گیرد.
- هر <bdi dir="ltr">Fact</bdi> متغیر با تاریخ کنترل ثبت می‌شود.
- <bdi dir="ltr">Domain/Context map</bdi> بیرونی یک <bdi dir="ltr">Hypothesis</bdi> است، نه <bdi dir="ltr">Fact</bdi> سازمانی.
- اطلاعات غیرعمومی <bdi dir="ltr">Tech stack</bdi> با <bdi dir="ltr">`UNKNOWN`</bdi> ثبت می‌شود؛ با حدس پر نمی‌شود.


</div>
