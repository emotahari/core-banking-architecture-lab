<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 08 Exercise</bdi> — <bdi dir="ltr">Primitive-to-Value-Object Refactoring Kata</bdi>

- <bdi dir="ltr">Timebox: 65 minutes coding</bdi> + <bdi dir="ltr">10 minutes self-review</bdi>
- <bdi dir="ltr">Working directory:</bdi> <bdi dir="ltr">`backend/banking-modulith`</bdi>
- <bdi dir="ltr">Starter package:</bdi> <bdi dir="ltr">`com.example.corebankinglab.craftsmanship.week01`</bdi>
- <bdi dir="ltr">Output: Refactored code</bdi> + <bdi dir="ltr">tests</bdi> + [<bdi dir="ltr">Code Review Checklist</bdi>](../artifacts/day-08-code-review-checklist.md)

## قانون تمرین

رفتار ثبت‌شدهٔ <bdi dir="ltr">Baseline</bdi> را در <bdi dir="ltr">Refactor</bdi> ناخواسته تغییر نده. هر تغییر <bdi dir="ltr">Rule</bdi> را <bdi dir="ltr">`OPEN/RULE CHANGE`</bdi> ثبت و از <bdi dir="ltr">Commit Refactor</bdi> جدا کن.

## <bdi dir="ltr">Step 0</bdi> — <bdi dir="ltr">Baseline</bdi>


</div>

<div dir="ltr" align="left">

```bash
mvn -Dtest=PrimitiveTransferRequestCharacterizationTest test
```

</div>

<div dir="rtl" align="right">


ثبت کن:

- تعداد تست‌ها و نتیجه
- زمان اجرا
- <bdi dir="ltr">Branch/commit</bdi> یا <bdi dir="ltr">Worktree state</bdi>
- خروجی <bdi dir="ltr">`mvn verify`</bdi> پیش از تغییر

## <bdi dir="ltr">Step 1</bdi> — <bdi dir="ltr">Smell Map</bdi>

حداقل شش <bdi dir="ltr">Smell</bdi> با این قالب:

| <bdi dir="ltr">Symbol</bdi> | <bdi dir="ltr">Smell</bdi> | <bdi dir="ltr">Concrete risk</bdi> | <bdi dir="ltr">Smallest move</bdi> |
|---|---|---|---|
|  |  |  |  |

عبارت «<bdi dir="ltr">SOLID</bdi> رعایت نشده» بدون <bdi dir="ltr">Location</bdi> و <bdi dir="ltr">Risk</bdi> امتیاز ندارد.

## <bdi dir="ltr">Step 2</bdi> — یک <bdi dir="ltr">Edge Test</bdi>

یکی را انتخاب کن:

- <bdi dir="ltr">lowercase currency</bdi>
- <bdi dir="ltr">whitespace around ID</bdi>
- <bdi dir="ltr">amount</bdi> با <bdi dir="ltr">Scale</bdi> زیاد
- <bdi dir="ltr">delimiter</bdi> داخل <bdi dir="ltr">ID</bdi> و اثر روی <bdi dir="ltr">audit key</bdi>
- <bdi dir="ltr">source/target</bdi> با تفاوت ظاهری <bdi dir="ltr">whitespace</bdi>

اگر <bdi dir="ltr">Expected behavior</bdi> معلوم نیست، <bdi dir="ltr">`OPEN`</bdi> ثبت کن و مورد دیگری را تست کن.

## <bdi dir="ltr">Step 3</bdi> — چهار <bdi dir="ltr">Checkpoint</bdi> سبز

1. <bdi dir="ltr">`AccountId`</bdi> برای <bdi dir="ltr">source/target</bdi>
2. <bdi dir="ltr">`CustomerId`</bdi> و <bdi dir="ltr">`BranchId`</bdi>
3. <bdi dir="ltr">`Money`</bdi> برای <bdi dir="ltr">amount/currency</bdi>
4. <bdi dir="ltr">Creation API</bdi> و <bdi dir="ltr">Request</bdi> نام‌دار

پس از هر <bdi dir="ltr">Checkpoint</bdi> تست هدفمند اجرا و نتیجه ثبت شود.

## <bdi dir="ltr">Step 4</bdi> — <bdi dir="ltr">Money Decision</bdi>

صریح تصمیم بگیر:

- <bdi dir="ltr">Money</bdi> عمومی <bdi dir="ltr">Signed</bdi> است یا این <bdi dir="ltr">Type</bdi> فقط <bdi dir="ltr">TransferAmount</bdi> مثبت است؟
- <bdi dir="ltr">Equality</bdi> عددی <bdi dir="ltr">Scale</bdi> را نادیده می‌گیرد یا نه؟
- <bdi dir="ltr">Rounding</bdi> کجا و با چه <bdi dir="ltr">API</bdi> صریح می‌شود؟
- <bdi dir="ltr">Currency</bdi> با <bdi dir="ltr">`java.util.Currency`</bdi> یا <bdi dir="ltr">Type</bdi> محدود دیگری نمایش داده می‌شود؟

<bdi dir="ltr">Rule</bdi> خیالی برای <bdi dir="ltr">Decimal</bdi>های <bdi dir="ltr">IRR</bdi> نساز.

## <bdi dir="ltr">Step 5</bdi> — <bdi dir="ltr">Factory Decision</bdi>

سه گزینه را با <bdi dir="ltr">Forces</bdi> مقایسه کن:


</div>

<div dir="ltr" align="left">

```text
public constructor | static factory | factory class
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Factory class</bdi> فقط وقتی معتبر است که <bdi dir="ltr">Creation decision</bdi> یا <bdi dir="ltr">Dependency</bdi> واقعی داشته باشد.

## <bdi dir="ltr">Step 6</bdi> — <bdi dir="ltr">Compatibility</bdi>

اگر <bdi dir="ltr">Constructor</bdi> یا <bdi dir="ltr">`auditKey`</bdi> قبلی را تغییر می‌دهی، رفتار <bdi dir="ltr">Characterization</bdi> را با <bdi dir="ltr">Adapter</bdi> یا <bdi dir="ltr">Test</bdi> روشن حفظ کن. حذف <bdi dir="ltr">API</bdi> قبلی باید تصمیم جدا باشد.

## <bdi dir="ltr">Step 7</bdi> — <bdi dir="ltr">Final verification</bdi>


</div>

<div dir="ltr" align="left">

```bash
mvn -B -ntp verify
```

</div>

<div dir="rtl" align="right">


تمام تست‌های <bdi dir="ltr">Week 01</bdi> و <bdi dir="ltr">Week 02</bdi> و <bdi dir="ltr">Spring context</bdi> باید سبز بمانند.

## <bdi dir="ltr">Step 8</bdi> — <bdi dir="ltr">Self-review</bdi>

1. کدام خطا اکنون <bdi dir="ltr">Compile-time</bdi> یا <bdi dir="ltr">creation-time</bdi> متوقف می‌شود؟
2. کدام <bdi dir="ltr">Coupling</bdi> کمتر شد؟
3. چند <bdi dir="ltr">Type</bdi> تازه ساختی و هزینه‌شان چیست؟
4. کدام <bdi dir="ltr">Rule</bdi> را عمداً تغییر ندادی؟
5. چه <bdi dir="ltr">Debt/Unknown</bdi>ی باقی ماند؟

## <bdi dir="ltr">Acceptance criteria</bdi>

- <bdi dir="ltr">Baseline</bdi> و <bdi dir="ltr">Refactor</bdi> هر دو <bdi dir="ltr">Evidence</bdi> سبز دارند.
- حداقل یک <bdi dir="ltr">Edge Test</bdi> تازه وجود دارد.
- <bdi dir="ltr">amount/currency</bdi> به <bdi dir="ltr">Concept</bdi> منسجم تبدیل شده‌اند.
- <bdi dir="ltr">Typed IDs</bdi> قابل‌جابه‌جایی نیستند.
- <bdi dir="ltr">`double`</bdi>، <bdi dir="ltr">Setter</bdi>، <bdi dir="ltr">Rounding</bdi> پنهان و <bdi dir="ltr">Base hierarchy</bdi> غیرضروری وجود ندارد.
- <bdi dir="ltr">Factory</bdi> یا رد آن با <bdi dir="ltr">Alternative</bdi>، <bdi dir="ltr">Cost</bdi> و <bdi dir="ltr">Revisit trigger</bdi> دفاع شده است.
- <bdi dir="ltr">`mvn verify`</bdi> سبز است.


</div>
