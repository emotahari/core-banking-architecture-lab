<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 06 Exercise</span> — <span dir="ltr">Money and Typed IDs</span>

- <span dir="ltr">Timebox: 60 minutes</span>
- مسیر کد: <span dir="ltr">backend/banking-modulith</span>
- هدف: ساخت <span dir="ltr">Value Object</span>هایی که خطا را در مرز مدل متوقف می‌کنند.

## <span dir="ltr">Type</span>های لازم

- <span dir="ltr">Money</span>
- <span dir="ltr">AccountId</span>
- <span dir="ltr">CustomerId</span>
- <span dir="ltr">BranchId</span>

## <span dir="ltr">Contract</span> طراحی <span dir="ltr">Money</span>

1. <span dir="ltr">Immutable</span> باشد.
2. <span dir="ltr">amount</span> و <span dir="ltr">currency</span> تهی نباشند.
3. <span dir="ltr">Equality</span> عددی از تفاوت <span dir="ltr">Scale</span> ظاهری <span dir="ltr">BigDecimal</span> آسیب نبیند؛ 100.0 و 100.00 در یک <span dir="ltr">Currency</span> برابر باشند.
4. جمع و تفریق فقط برای <span dir="ltr">Currency</span> یکسان مجاز باشد.
5. هیچ <span dir="ltr">Rounding</span> پنهانی در <span dir="ltr">Factory</span> یا <span dir="ltr">Arithmetic</span> رخ ندهد.
6. هر عملیات نیازمند <span dir="ltr">Rounding</span>، <span dir="ltr">Scale</span> و <span dir="ltr">RoundingMode</span> را صریح دریافت کند.
7. <span dir="ltr">Money</span> عمومی می‌تواند <span dir="ltr">Signed</span> باشد؛ مثبت‌بودن مبلغ قاعدهٔ <span dir="ltr">Use Case</span> است، نه ذات <span dir="ltr">Money.</span>
8. <span dir="ltr">toString</span> برای نمایش <span dir="ltr">UI</span> یا سند رسمی مبنا نیست؛ <span dir="ltr">Formatting</span> مسئولیت جدا دارد.

## <span dir="ltr">Contract</span> طراحی <span dir="ltr">Typed ID</span>

1. هر <span dir="ltr">ID Type</span> مستقل باشد تا <span dir="ltr">CustomerId</span> تصادفی جای <span dir="ltr">AccountId</span> استفاده نشود.
2. مقدار تهی و <span dir="ltr">String</span> نامعتبر رد شود.
3. <span dir="ltr">Parsing</span> در <span dir="ltr">Factory</span> روشن باشد.
4. <span dir="ltr">ID</span> داخلی با شمارهٔ حساب، <span dir="ltr">CIF</span> یا کد شعبه اشتباه نشود.

## تست‌های اجباری

- <span dir="ltr">sameNumericAmountWithDifferentScaleIsEqual</span>
- <span dir="ltr">differentCurrenciesAreNotEqual</span>
- <span dir="ltr">addingDifferentCurrenciesFails</span>
- <span dir="ltr">nullAmountFails</span>
- <span dir="ltr">nullCurrencyFails</span>
- <span dir="ltr">roundingMustBeExplicit</span>
- <span dir="ltr">validIdsCanBeParsed</span>
- <span dir="ltr">invalidIdsFailFast</span>
- <span dir="ltr">typedIdsWithSameRawValueAreNotInterchangeable</span> در سطح طراحی/کامپایل توضیح داده شود.

## تصمیمی که باید ثبت شود

در یک یادداشت کوتاه توضیح بده:

- چرا <span dir="ltr">Money</span> منفی را در <span dir="ltr">Value Object</span> عمومی ممنوع یا مجاز کردی؟
- <span dir="ltr">Currency Scale Policy</span> متعلق به <span dir="ltr">Money</span> است یا <span dir="ltr">Product/Accounting Context</span>؟
- چرا استفادهٔ مستقیم از <span dir="ltr">double</span> برای مبلغ بانکی رد می‌شود؟

## قبولی


</div>

<div dir="ltr" align="left">

~~~bash
mvn verify
~~~

</div>

<div dir="rtl" align="right">


باید سبز باشد و هیچ <span dir="ltr">Setter</span> یا <span dir="ltr">Dependency</span> به <span dir="ltr">Spring/JPA</span> در <span dir="ltr">Value Object</span>ها وجود نداشته باشد.

</div>
