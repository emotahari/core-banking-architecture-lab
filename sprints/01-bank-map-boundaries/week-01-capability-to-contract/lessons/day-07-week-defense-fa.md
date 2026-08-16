<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 07</span> — تثبیت، گزارش و دفاع <span dir="ltr">Week 01</span>

- <span dir="ltr">Day budget: 20 minutes self-preparation</span>
- <span dir="ltr">Output: Week Report</span>، <span dir="ltr">Evidence index</span> و دفاع ده‌دقیقه‌ای
- <span dir="ltr">Gate:</span> حداقل 8 از 10 و بدون <span dir="ltr">Critical Error</span>

## 1. هدف روز

<span dir="ltr">Day 07</span> درس تازه‌ای اضافه نمی‌کند. هدف تبدیل شش روز مطالعه به یک **استدلال معماری قابل دفاع** است. اگر نتوانی از <span dir="ltr">Map</span>، <span dir="ltr">Chain</span> و کد خودت دفاع کنی، خواندن متن‌ها <span dir="ltr">Week</span> را تمام نمی‌کند.

## <span dir="ltr">2. Evidence</span>هایی که باید باز شوند

پیش از دفاع، این موارد باید لینک یا مسیر معتبر داشته باشند:

1. پاسخ خام <span dir="ltr">Day 01</span> و <span dir="ltr">Revision</span> جداگانه
2. <span dir="ltr">Distinction Matrix</span>
3. دو <span dir="ltr">Traceability Chain</span>
4. <span dir="ltr">Coupling Review</span> قبل/بعد
5. <span dir="ltr">Capability Map v1</span>
6. <span dir="ltr">BIAN Gap Check</span>
7. <span dir="ltr">Glossary</span> حداقل ۴۰ واژه
8. کد و تست <span dir="ltr">Money/Typed IDs</span>
9. خروجی <span dir="ltr">`mvn verify`</span>
10. <span dir="ltr">Week 01 Report</span>

اگر <span dir="ltr">Artifact</span> خالی است، در <span dir="ltr">Report</span> آن را <span dir="ltr">`Missing`</span> ثبت کن؛ با جملهٔ کلی «انجام شد» پنهان نکن.

## 3. ساختار دفاع ده‌دقیقه‌ای

### دقیقه 0 تا 1 — مسئله و <span dir="ltr">Scope</span>

- <span dir="ltr">Scope Week</span> چیست؟
- چه چیزهایی عمداً هنوز تصمیم نگرفته‌ایم؟

### دقیقه 1 تا 3 — <span dir="ltr">Capability Map</span>

- چهار <span dir="ltr">Capability</span> اصلی را نشان بده.
- یک موردی را که ابتدا <span dir="ltr">System/Process</span> فرض کرده بودی و اصلاح شد توضیح بده.
- یک <span dir="ltr">Gap</span> یا <span dir="ltr">False Friend</span> حاصل از <span dir="ltr">BIAN</span> را بیان کن.

### دقیقه 3 تا 6 — <span dir="ltr">Traceability</span>

- زنجیرهٔ مسدودی قضایی را از <span dir="ltr">Outcome</span> تا <span dir="ltr">Contract</span> طی کن.
- <span dir="ltr">Owner</span> حکم، <span dir="ltr">Hold</span>، <span dir="ltr">available balance</span> و <span dir="ltr">Journal</span> را جدا کن.
- <span dir="ltr">Command</span> و <span dir="ltr">Event</span> را با نام و زمان دستوری مقایسه کن.

### دقیقه 6 تا 8 — <span dir="ltr">Design quality</span>

- یک <span dir="ltr">Coupling</span> خطرناک را با اثر تغییر یا شکست نشان بده.
- توضیح بده <span dir="ltr">Encapsulation</span> و <span dir="ltr">Information Hiding</span> در <span dir="ltr">Redesign</span> چه فرقی داشتند.

### دقیقه 8 تا 9 — <span dir="ltr">Code evidence</span>

- یک <span dir="ltr">Invariant Money</span> و یک خطای <span dir="ltr">Typed ID</span> را نشان بده.
- نتیجهٔ <span dir="ltr">`mvn verify`</span> را ارائه کن.

### دقیقه 9 تا 10 — <span dir="ltr">Unknown</span> و تصمیم بعدی

- مهم‌ترین <span dir="ltr">Unknown</span> را صریح بگو.
- مشخص کن <span dir="ltr">Week 02</span> کدام <span dir="ltr">Boundary/Ownership hypothesis</span> را خواهد آزمود.

## 4. پرسش‌های دفاعی محتمل

1. چرا «سامانه تسهیلات» <span dir="ltr">Capability</span> نیست ولی «مدیریت تعهدات اعتباری» می‌تواند باشد؟
2. چرا یک <span dir="ltr">Capability</span> می‌تواند چند <span dir="ltr">Bounded Context</span> داشته باشد؟
3. چه <span dir="ltr">Evidence</span> دیگری غیر از <span dir="ltr">BIAN</span> برای <span dir="ltr">Service boundary</span> لازم است؟
4. اگر <span dir="ltr">Legal Orders</span> و <span dir="ltr">Deposits</span> یک <span dir="ltr">Deployable</span> باشند، آیا هنوز دو <span dir="ltr">Context/Module</span> می‌توانند باشند؟
5. چه کسی مالک <span dir="ltr">available balance</span> و چه کسی مالک <span dir="ltr">Journal</span> است؟
6. <span dir="ltr">`PlaceFundsHold`</span> چرا <span dir="ltr">Command</span> و <span dir="ltr">`FundsHeld`</span> چرا <span dir="ltr">Event</span> است؟
7. <span dir="ltr">HTTP</span> چگونه می‌تواند شدیداً <span dir="ltr">Coupled</span> باشد؟
8. چرا <span dir="ltr">Money</span> منفی را مجاز یا ممنوع کردی؟
9. چرا <span dir="ltr">`100.0`</span> و <span dir="ltr">`100.00`</span> باید یا نباید برابر باشند؟
10. مهم‌ترین فرض اثبات‌نشدهٔ <span dir="ltr">Map</span> تو چیست؟

## <span dir="ltr">5. Rubric Gate</span>

| حوزه | امتیاز | شاهد |
|---|---:|---|
| زبان و تمایز مفاهیم | ۲ | <span dir="ltr">Distinction Matrix</span> + پاسخ شفاهی |
| <span dir="ltr">Capability Map</span> و <span dir="ltr">BIAN</span> | ۲ | <span dir="ltr">Map v1</span> + <span dir="ltr">Gap Check</span> |
| <span dir="ltr">Traceability</span> و <span dir="ltr">Ownership</span> | ۲ | دو <span dir="ltr">Chain</span> |
| <span dir="ltr">Coupling/Encapsulation</span> | ۱.۵ | <span dir="ltr">Coupling Review</span> |
| <span dir="ltr">Value Object</span> و تست | ۱.۵ | کد + <span dir="ltr">`mvn verify`</span> |
| صداقت دربارهٔ <span dir="ltr">Unknown/Trade-off</span> | ۱ | <span dir="ltr">Report</span> و دفاع |
| **جمع** | **۱۰** |  |

حد عبور ۸ است. امتیاز ۸ با <span dir="ltr">Critical Error</span> پذیرفته نمی‌شود.

## <span dir="ltr">6. Critical Error</span>ها

- <span dir="ltr">Application/API/Table</span> به‌عنوان <span dir="ltr">Capability</span>
- <span dir="ltr">BIAN Service Domain</span> برابر <span dir="ltr">Microservice</span>
- <span dir="ltr">Owner</span> مشترک و مبهم برای یک <span dir="ltr">Fact</span> واحد
- <span dir="ltr">Event</span> امری یا بدون <span dir="ltr">Fact</span> روشن
- دسترسی مستقیم به <span dir="ltr">State</span> داخلی <span dir="ltr">Context</span> دیگر به‌عنوان <span dir="ltr">Contract</span>
- <span dir="ltr">`double`</span> یا <span dir="ltr">Rounding</span> پنهان برای <span dir="ltr">Money</span>
- ادعای <span dir="ltr">`Done`</span> بدون <span dir="ltr">Evidence</span> قابل بازشدن

## 7. روش اصلاح

<span dir="ltr">Gate</span> ناموفق به معنی تکرار کل هفته نیست. <span dir="ltr">Critical Error</span> به کوچک‌ترین تمرین مربوط برمی‌گردد:

| ضعف | <span dir="ltr">Remediation</span> |
|---|---|
| تمایز <span dir="ltr">Capability</span> | طبقه‌بندی ۵ مثال تازه |
| <span dir="ltr">Traceability</span> | بازسازی یک <span dir="ltr">Chain</span> کوتاه |
| <span dir="ltr">Ownership</span> | جدول <span dir="ltr">Fact/Authority</span> سه‌ردیفی |
| <span dir="ltr">BIAN</span> | تحلیل یک <span dir="ltr">False Friend</span> |
| <span dir="ltr">Money</span> | افزودن یک تست شکست و <span dir="ltr">Refactor</span> |

پس از اصلاح، پاسخ قبلی پاک نمی‌شود؛ <span dir="ltr">`REVISION`</span> و <span dir="ltr">Evidence</span> تازه افزوده می‌شود.

## 8. کار بعد

[<span dir="ltr">Day 07 Exercise</span>](../exercises/day-07-week-defense.md) و [<span dir="ltr">Week Report</span>](../artifacts/week-01-report-template.md) را تکمیل کن. بعد از عبور هسته، برای وضعیت <span dir="ltr">`Done — Expanded`</span> باید <span dir="ltr">Day 08 Code Craft</span> و <span dir="ltr">Day 09 UPI</span> نیز تمام شوند.


</div>
