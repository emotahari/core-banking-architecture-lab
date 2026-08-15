# Day 07 — تثبیت، گزارش و دفاع Week 01

- Day budget: 20 minutes self-preparation
- Output: Week Report، Evidence index و دفاع ده‌دقیقه‌ای
- Gate: حداقل 8 از 10 و بدون Critical Error

## 1. هدف روز

Day 07 درس تازه‌ای اضافه نمی‌کند. هدف تبدیل شش روز مطالعه به یک **استدلال معماری قابل دفاع** است. اگر نتوانی از Map، Chain و کد خودت دفاع کنی، خواندن متن‌ها Week را تمام نمی‌کند.

## 2. Evidenceهایی که باید باز شوند

پیش از دفاع، این موارد باید لینک یا مسیر معتبر داشته باشند:

1. پاسخ خام Day 01 و Revision جداگانه
2. Distinction Matrix
3. دو Traceability Chain
4. Coupling Review قبل/بعد
5. Capability Map v1
6. BIAN Gap Check
7. Glossary حداقل ۴۰ واژه
8. کد و تست Money/Typed IDs
9. خروجی `mvn verify`
10. Week 01 Report

اگر Artifact خالی است، در Report آن را `Missing` ثبت کن؛ با جملهٔ کلی «انجام شد» پنهان نکن.

## 3. ساختار دفاع ده‌دقیقه‌ای

### دقیقه 0 تا 1 — مسئله و Scope

- Scope Week چیست؟
- چه چیزهایی عمداً هنوز تصمیم نگرفته‌ایم؟

### دقیقه 1 تا 3 — Capability Map

- چهار Capability اصلی را نشان بده.
- یک موردی را که ابتدا System/Process فرض کرده بودی و اصلاح شد توضیح بده.
- یک Gap یا False Friend حاصل از BIAN را بیان کن.

### دقیقه 3 تا 6 — Traceability

- زنجیرهٔ مسدودی قضایی را از Outcome تا Contract طی کن.
- Owner حکم، Hold، available balance و Journal را جدا کن.
- Command و Event را با نام و زمان دستوری مقایسه کن.

### دقیقه 6 تا 8 — Design quality

- یک Coupling خطرناک را با اثر تغییر یا شکست نشان بده.
- توضیح بده Encapsulation و Information Hiding در Redesign چه فرقی داشتند.

### دقیقه 8 تا 9 — Code evidence

- یک Invariant Money و یک خطای Typed ID را نشان بده.
- نتیجهٔ `mvn verify` را ارائه کن.

### دقیقه 9 تا 10 — Unknown و تصمیم بعدی

- مهم‌ترین Unknown را صریح بگو.
- مشخص کن Week 02 کدام Boundary/Ownership hypothesis را خواهد آزمود.

## 4. پرسش‌های دفاعی محتمل

1. چرا «سامانه تسهیلات» Capability نیست ولی «مدیریت تعهدات اعتباری» می‌تواند باشد؟
2. چرا یک Capability می‌تواند چند Bounded Context داشته باشد؟
3. چه Evidence دیگری غیر از BIAN برای Service boundary لازم است؟
4. اگر Legal Orders و Deposits یک Deployable باشند، آیا هنوز دو Context/Module می‌توانند باشند؟
5. چه کسی مالک available balance و چه کسی مالک Journal است؟
6. `PlaceFundsHold` چرا Command و `FundsHeld` چرا Event است؟
7. HTTP چگونه می‌تواند شدیداً Coupled باشد؟
8. چرا Money منفی را مجاز یا ممنوع کردی؟
9. چرا `100.0` و `100.00` باید یا نباید برابر باشند؟
10. مهم‌ترین فرض اثبات‌نشدهٔ Map تو چیست؟

## 5. Rubric Gate

| حوزه | امتیاز | شاهد |
|---|---:|---|
| زبان و تمایز مفاهیم | ۲ | Distinction Matrix + پاسخ شفاهی |
| Capability Map و BIAN | ۲ | Map v1 + Gap Check |
| Traceability و Ownership | ۲ | دو Chain |
| Coupling/Encapsulation | ۱.۵ | Coupling Review |
| Value Object و تست | ۱.۵ | کد + `mvn verify` |
| صداقت دربارهٔ Unknown/Trade-off | ۱ | Report و دفاع |
| **جمع** | **۱۰** |  |

حد عبور ۸ است. امتیاز ۸ با Critical Error پذیرفته نمی‌شود.

## 6. Critical Errorها

- Application/API/Table به‌عنوان Capability
- BIAN Service Domain برابر Microservice
- Owner مشترک و مبهم برای یک Fact واحد
- Event امری یا بدون Fact روشن
- دسترسی مستقیم به State داخلی Context دیگر به‌عنوان Contract
- `double` یا Rounding پنهان برای Money
- ادعای `Done` بدون Evidence قابل بازشدن

## 7. روش اصلاح

Gate ناموفق به معنی تکرار کل هفته نیست. Critical Error به کوچک‌ترین تمرین مربوط برمی‌گردد:

| ضعف | Remediation |
|---|---|
| تمایز Capability | طبقه‌بندی ۵ مثال تازه |
| Traceability | بازسازی یک Chain کوتاه |
| Ownership | جدول Fact/Authority سه‌ردیفی |
| BIAN | تحلیل یک False Friend |
| Money | افزودن یک تست شکست و Refactor |

پس از اصلاح، پاسخ قبلی پاک نمی‌شود؛ `REVISION` و Evidence تازه افزوده می‌شود.

## 8. کار بعد

[Day 07 Exercise](../exercises/day-07-week-defense.md) و [Week Report](../artifacts/week-01-report-template.md) را تکمیل کن. بعد از عبور هسته، برای وضعیت `Done — Expanded` باید Day 08 Code Craft و Day 09 UPI نیز تمام شوند.

