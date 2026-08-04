# Day 06 Exercise — Money and Typed IDs

- Timebox: 60 minutes
- مسیر کد: backend/banking-modulith
- هدف: ساخت Value Objectهایی که خطا را در مرز مدل متوقف می‌کنند.

## Typeهای لازم

- Money
- AccountId
- CustomerId
- BranchId

## Contract طراحی Money

1. Immutable باشد.
2. amount و currency تهی نباشند.
3. Equality عددی از تفاوت Scale ظاهری BigDecimal آسیب نبیند؛ 100.0 و 100.00 در یک Currency برابر باشند.
4. جمع و تفریق فقط برای Currency یکسان مجاز باشد.
5. هیچ Rounding پنهانی در Factory یا Arithmetic رخ ندهد.
6. هر عملیات نیازمند Rounding، Scale و RoundingMode را صریح دریافت کند.
7. Money عمومی می‌تواند Signed باشد؛ مثبت‌بودن مبلغ قاعدهٔ Use Case است، نه ذات Money.
8. toString برای نمایش UI یا سند رسمی مبنا نیست؛ Formatting مسئولیت جدا دارد.

## Contract طراحی Typed ID

1. هر ID Type مستقل باشد تا CustomerId تصادفی جای AccountId استفاده نشود.
2. مقدار تهی و String نامعتبر رد شود.
3. Parsing در Factory روشن باشد.
4. ID داخلی با شمارهٔ حساب، CIF یا کد شعبه اشتباه نشود.

## تست‌های اجباری

- sameNumericAmountWithDifferentScaleIsEqual
- differentCurrenciesAreNotEqual
- addingDifferentCurrenciesFails
- nullAmountFails
- nullCurrencyFails
- roundingMustBeExplicit
- validIdsCanBeParsed
- invalidIdsFailFast
- typedIdsWithSameRawValueAreNotInterchangeable در سطح طراحی/کامپایل توضیح داده شود.

## تصمیمی که باید ثبت شود

در یک یادداشت کوتاه توضیح بده:

- چرا Money منفی را در Value Object عمومی ممنوع یا مجاز کردی؟
- Currency Scale Policy متعلق به Money است یا Product/Accounting Context؟
- چرا استفادهٔ مستقیم از double برای مبلغ بانکی رد می‌شود؟

## قبولی

~~~bash
mvn verify
~~~

باید سبز باشد و هیچ Setter یا Dependency به Spring/JPA در Value Objectها وجود نداشته باشد.
