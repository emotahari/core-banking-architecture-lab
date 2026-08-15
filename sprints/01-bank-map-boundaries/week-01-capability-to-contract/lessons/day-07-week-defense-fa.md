<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 07</bdi> — تثبیت، گزارش و دفاع <bdi dir="ltr">Week 01</bdi>

- <bdi dir="ltr">Day budget: 20 minutes self-preparation</bdi>
- <bdi dir="ltr">Output: Week Report</bdi>، <bdi dir="ltr">Evidence index</bdi> و دفاع ده‌دقیقه‌ای
- <bdi dir="ltr">Gate:</bdi> حداقل 8 از 10 و بدون <bdi dir="ltr">Critical Error</bdi>

## 1. هدف روز

<bdi dir="ltr">Day 07</bdi> درس تازه‌ای اضافه نمی‌کند. هدف تبدیل شش روز مطالعه به یک **استدلال معماری قابل دفاع** است. اگر نتوانی از <bdi dir="ltr">Map</bdi>، <bdi dir="ltr">Chain</bdi> و کد خودت دفاع کنی، خواندن متن‌ها <bdi dir="ltr">Week</bdi> را تمام نمی‌کند.

## <bdi dir="ltr">2. Evidence</bdi>هایی که باید باز شوند

پیش از دفاع، این موارد باید لینک یا مسیر معتبر داشته باشند:

1. پاسخ خام <bdi dir="ltr">Day 01</bdi> و <bdi dir="ltr">Revision</bdi> جداگانه
2. <bdi dir="ltr">Distinction Matrix</bdi>
3. دو <bdi dir="ltr">Traceability Chain</bdi>
4. <bdi dir="ltr">Coupling Review</bdi> قبل/بعد
5. <bdi dir="ltr">Capability Map v1</bdi>
6. <bdi dir="ltr">BIAN Gap Check</bdi>
7. <bdi dir="ltr">Glossary</bdi> حداقل ۴۰ واژه
8. کد و تست <bdi dir="ltr">Money/Typed IDs</bdi>
9. خروجی <bdi dir="ltr">`mvn verify`</bdi>
10. <bdi dir="ltr">Week 01 Report</bdi>

اگر <bdi dir="ltr">Artifact</bdi> خالی است، در <bdi dir="ltr">Report</bdi> آن را <bdi dir="ltr">`Missing`</bdi> ثبت کن؛ با جملهٔ کلی «انجام شد» پنهان نکن.

## 3. ساختار دفاع ده‌دقیقه‌ای

### دقیقه 0 تا 1 — مسئله و <bdi dir="ltr">Scope</bdi>

- <bdi dir="ltr">Scope Week</bdi> چیست؟
- چه چیزهایی عمداً هنوز تصمیم نگرفته‌ایم؟

### دقیقه 1 تا 3 — <bdi dir="ltr">Capability Map</bdi>

- چهار <bdi dir="ltr">Capability</bdi> اصلی را نشان بده.
- یک موردی را که ابتدا <bdi dir="ltr">System/Process</bdi> فرض کرده بودی و اصلاح شد توضیح بده.
- یک <bdi dir="ltr">Gap</bdi> یا <bdi dir="ltr">False Friend</bdi> حاصل از <bdi dir="ltr">BIAN</bdi> را بیان کن.

### دقیقه 3 تا 6 — <bdi dir="ltr">Traceability</bdi>

- زنجیرهٔ مسدودی قضایی را از <bdi dir="ltr">Outcome</bdi> تا <bdi dir="ltr">Contract</bdi> طی کن.
- <bdi dir="ltr">Owner</bdi> حکم، <bdi dir="ltr">Hold</bdi>، <bdi dir="ltr">available balance</bdi> و <bdi dir="ltr">Journal</bdi> را جدا کن.
- <bdi dir="ltr">Command</bdi> و <bdi dir="ltr">Event</bdi> را با نام و زمان دستوری مقایسه کن.

### دقیقه 6 تا 8 — <bdi dir="ltr">Design quality</bdi>

- یک <bdi dir="ltr">Coupling</bdi> خطرناک را با اثر تغییر یا شکست نشان بده.
- توضیح بده <bdi dir="ltr">Encapsulation</bdi> و <bdi dir="ltr">Information Hiding</bdi> در <bdi dir="ltr">Redesign</bdi> چه فرقی داشتند.

### دقیقه 8 تا 9 — <bdi dir="ltr">Code evidence</bdi>

- یک <bdi dir="ltr">Invariant Money</bdi> و یک خطای <bdi dir="ltr">Typed ID</bdi> را نشان بده.
- نتیجهٔ <bdi dir="ltr">`mvn verify`</bdi> را ارائه کن.

### دقیقه 9 تا 10 — <bdi dir="ltr">Unknown</bdi> و تصمیم بعدی

- مهم‌ترین <bdi dir="ltr">Unknown</bdi> را صریح بگو.
- مشخص کن <bdi dir="ltr">Week 02</bdi> کدام <bdi dir="ltr">Boundary/Ownership hypothesis</bdi> را خواهد آزمود.

## 4. پرسش‌های دفاعی محتمل

1. چرا «سامانه تسهیلات» <bdi dir="ltr">Capability</bdi> نیست ولی «مدیریت تعهدات اعتباری» می‌تواند باشد؟
2. چرا یک <bdi dir="ltr">Capability</bdi> می‌تواند چند <bdi dir="ltr">Bounded Context</bdi> داشته باشد؟
3. چه <bdi dir="ltr">Evidence</bdi> دیگری غیر از <bdi dir="ltr">BIAN</bdi> برای <bdi dir="ltr">Service boundary</bdi> لازم است؟
4. اگر <bdi dir="ltr">Legal Orders</bdi> و <bdi dir="ltr">Deposits</bdi> یک <bdi dir="ltr">Deployable</bdi> باشند، آیا هنوز دو <bdi dir="ltr">Context/Module</bdi> می‌توانند باشند؟
5. چه کسی مالک <bdi dir="ltr">available balance</bdi> و چه کسی مالک <bdi dir="ltr">Journal</bdi> است؟
6. <bdi dir="ltr">`PlaceFundsHold`</bdi> چرا <bdi dir="ltr">Command</bdi> و <bdi dir="ltr">`FundsHeld`</bdi> چرا <bdi dir="ltr">Event</bdi> است؟
7. <bdi dir="ltr">HTTP</bdi> چگونه می‌تواند شدیداً <bdi dir="ltr">Coupled</bdi> باشد؟
8. چرا <bdi dir="ltr">Money</bdi> منفی را مجاز یا ممنوع کردی؟
9. چرا <bdi dir="ltr">`100.0`</bdi> و <bdi dir="ltr">`100.00`</bdi> باید یا نباید برابر باشند؟
10. مهم‌ترین فرض اثبات‌نشدهٔ <bdi dir="ltr">Map</bdi> تو چیست؟

## <bdi dir="ltr">5. Rubric Gate</bdi>

| حوزه | امتیاز | شاهد |
|---|---:|---|
| زبان و تمایز مفاهیم | ۲ | <bdi dir="ltr">Distinction Matrix</bdi> + پاسخ شفاهی |
| <bdi dir="ltr">Capability Map</bdi> و <bdi dir="ltr">BIAN</bdi> | ۲ | <bdi dir="ltr">Map v1</bdi> + <bdi dir="ltr">Gap Check</bdi> |
| <bdi dir="ltr">Traceability</bdi> و <bdi dir="ltr">Ownership</bdi> | ۲ | دو <bdi dir="ltr">Chain</bdi> |
| <bdi dir="ltr">Coupling/Encapsulation</bdi> | ۱.۵ | <bdi dir="ltr">Coupling Review</bdi> |
| <bdi dir="ltr">Value Object</bdi> و تست | ۱.۵ | کد + <bdi dir="ltr">`mvn verify`</bdi> |
| صداقت دربارهٔ <bdi dir="ltr">Unknown/Trade-off</bdi> | ۱ | <bdi dir="ltr">Report</bdi> و دفاع |
| **جمع** | **۱۰** |  |

حد عبور ۸ است. امتیاز ۸ با <bdi dir="ltr">Critical Error</bdi> پذیرفته نمی‌شود.

## <bdi dir="ltr">6. Critical Error</bdi>ها

- <bdi dir="ltr">Application/API/Table</bdi> به‌عنوان <bdi dir="ltr">Capability</bdi>
- <bdi dir="ltr">BIAN Service Domain</bdi> برابر <bdi dir="ltr">Microservice</bdi>
- <bdi dir="ltr">Owner</bdi> مشترک و مبهم برای یک <bdi dir="ltr">Fact</bdi> واحد
- <bdi dir="ltr">Event</bdi> امری یا بدون <bdi dir="ltr">Fact</bdi> روشن
- دسترسی مستقیم به <bdi dir="ltr">State</bdi> داخلی <bdi dir="ltr">Context</bdi> دیگر به‌عنوان <bdi dir="ltr">Contract</bdi>
- <bdi dir="ltr">`double`</bdi> یا <bdi dir="ltr">Rounding</bdi> پنهان برای <bdi dir="ltr">Money</bdi>
- ادعای <bdi dir="ltr">`Done`</bdi> بدون <bdi dir="ltr">Evidence</bdi> قابل بازشدن

## 7. روش اصلاح

<bdi dir="ltr">Gate</bdi> ناموفق به معنی تکرار کل هفته نیست. <bdi dir="ltr">Critical Error</bdi> به کوچک‌ترین تمرین مربوط برمی‌گردد:

| ضعف | <bdi dir="ltr">Remediation</bdi> |
|---|---|
| تمایز <bdi dir="ltr">Capability</bdi> | طبقه‌بندی ۵ مثال تازه |
| <bdi dir="ltr">Traceability</bdi> | بازسازی یک <bdi dir="ltr">Chain</bdi> کوتاه |
| <bdi dir="ltr">Ownership</bdi> | جدول <bdi dir="ltr">Fact/Authority</bdi> سه‌ردیفی |
| <bdi dir="ltr">BIAN</bdi> | تحلیل یک <bdi dir="ltr">False Friend</bdi> |
| <bdi dir="ltr">Money</bdi> | افزودن یک تست شکست و <bdi dir="ltr">Refactor</bdi> |

پس از اصلاح، پاسخ قبلی پاک نمی‌شود؛ <bdi dir="ltr">`REVISION`</bdi> و <bdi dir="ltr">Evidence</bdi> تازه افزوده می‌شود.

## 8. کار بعد

[<bdi dir="ltr">Day 07 Exercise</bdi>](../exercises/day-07-week-defense.md) و [<bdi dir="ltr">Week Report</bdi>](../artifacts/week-01-report-template.md) را تکمیل کن. بعد از عبور هسته، برای وضعیت <bdi dir="ltr">`Done — Expanded`</bdi> باید <bdi dir="ltr">Day 08 Code Craft</bdi> و <bdi dir="ltr">Day 09 UPI</bdi> نیز تمام شوند.


</div>
