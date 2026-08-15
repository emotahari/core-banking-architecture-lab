<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 06 Exercise</bdi> — <bdi dir="ltr">Money and Typed IDs</bdi>

- <bdi dir="ltr">Timebox: 60 minutes</bdi>
- مسیر کد: <bdi dir="ltr">backend/banking-modulith</bdi>
- هدف: ساخت <bdi dir="ltr">Value Object</bdi>هایی که خطا را در مرز مدل متوقف می‌کنند.

## <bdi dir="ltr">Type</bdi>های لازم

- <bdi dir="ltr">Money</bdi>
- <bdi dir="ltr">AccountId</bdi>
- <bdi dir="ltr">CustomerId</bdi>
- <bdi dir="ltr">BranchId</bdi>

## <bdi dir="ltr">Contract</bdi> طراحی <bdi dir="ltr">Money</bdi>

1. <bdi dir="ltr">Immutable</bdi> باشد.
2. <bdi dir="ltr">amount</bdi> و <bdi dir="ltr">currency</bdi> تهی نباشند.
3. <bdi dir="ltr">Equality</bdi> عددی از تفاوت <bdi dir="ltr">Scale</bdi> ظاهری <bdi dir="ltr">BigDecimal</bdi> آسیب نبیند؛ 100.0 و 100.00 در یک <bdi dir="ltr">Currency</bdi> برابر باشند.
4. جمع و تفریق فقط برای <bdi dir="ltr">Currency</bdi> یکسان مجاز باشد.
5. هیچ <bdi dir="ltr">Rounding</bdi> پنهانی در <bdi dir="ltr">Factory</bdi> یا <bdi dir="ltr">Arithmetic</bdi> رخ ندهد.
6. هر عملیات نیازمند <bdi dir="ltr">Rounding</bdi>، <bdi dir="ltr">Scale</bdi> و <bdi dir="ltr">RoundingMode</bdi> را صریح دریافت کند.
7. <bdi dir="ltr">Money</bdi> عمومی می‌تواند <bdi dir="ltr">Signed</bdi> باشد؛ مثبت‌بودن مبلغ قاعدهٔ <bdi dir="ltr">Use Case</bdi> است، نه ذات <bdi dir="ltr">Money.</bdi>
8. <bdi dir="ltr">toString</bdi> برای نمایش <bdi dir="ltr">UI</bdi> یا سند رسمی مبنا نیست؛ <bdi dir="ltr">Formatting</bdi> مسئولیت جدا دارد.

## <bdi dir="ltr">Contract</bdi> طراحی <bdi dir="ltr">Typed ID</bdi>

1. هر <bdi dir="ltr">ID Type</bdi> مستقل باشد تا <bdi dir="ltr">CustomerId</bdi> تصادفی جای <bdi dir="ltr">AccountId</bdi> استفاده نشود.
2. مقدار تهی و <bdi dir="ltr">String</bdi> نامعتبر رد شود.
3. <bdi dir="ltr">Parsing</bdi> در <bdi dir="ltr">Factory</bdi> روشن باشد.
4. <bdi dir="ltr">ID</bdi> داخلی با شمارهٔ حساب، <bdi dir="ltr">CIF</bdi> یا کد شعبه اشتباه نشود.

## تست‌های اجباری

- <bdi dir="ltr">sameNumericAmountWithDifferentScaleIsEqual</bdi>
- <bdi dir="ltr">differentCurrenciesAreNotEqual</bdi>
- <bdi dir="ltr">addingDifferentCurrenciesFails</bdi>
- <bdi dir="ltr">nullAmountFails</bdi>
- <bdi dir="ltr">nullCurrencyFails</bdi>
- <bdi dir="ltr">roundingMustBeExplicit</bdi>
- <bdi dir="ltr">validIdsCanBeParsed</bdi>
- <bdi dir="ltr">invalidIdsFailFast</bdi>
- <bdi dir="ltr">typedIdsWithSameRawValueAreNotInterchangeable</bdi> در سطح طراحی/کامپایل توضیح داده شود.

## تصمیمی که باید ثبت شود

در یک یادداشت کوتاه توضیح بده:

- چرا <bdi dir="ltr">Money</bdi> منفی را در <bdi dir="ltr">Value Object</bdi> عمومی ممنوع یا مجاز کردی؟
- <bdi dir="ltr">Currency Scale Policy</bdi> متعلق به <bdi dir="ltr">Money</bdi> است یا <bdi dir="ltr">Product/Accounting Context</bdi>؟
- چرا استفادهٔ مستقیم از <bdi dir="ltr">double</bdi> برای مبلغ بانکی رد می‌شود؟

## قبولی


</div>

<div dir="ltr" align="left">

~~~bash
mvn verify
~~~

</div>

<div dir="rtl" align="right">


باید سبز باشد و هیچ <bdi dir="ltr">Setter</bdi> یا <bdi dir="ltr">Dependency</bdi> به <bdi dir="ltr">Spring/JPA</bdi> در <bdi dir="ltr">Value Object</bdi>ها وجود نداشته باشد.

</div>
