<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 08 Exercise</span> — <span dir="ltr">Primitive-to-Value-Object Refactoring Kata</span>

- <span dir="ltr">Timebox: 65 minutes coding</span> + <span dir="ltr">10 minutes self-review</span>
- <span dir="ltr">Working directory:</span> <span dir="ltr">`backend/banking-modulith`</span>
- <span dir="ltr">Starter package:</span> <span dir="ltr">`com.example.corebankinglab.craftsmanship.week01`</span>
- <span dir="ltr">Output: Refactored code</span> + <span dir="ltr">tests</span> + [<span dir="ltr">Code Review Checklist</span>](../artifacts/day-08-code-review-checklist.md)

## قانون تمرین

رفتار ثبت‌شدهٔ <span dir="ltr">Baseline</span> را در <span dir="ltr">Refactor</span> ناخواسته تغییر نده. هر تغییر <span dir="ltr">Rule</span> را <span dir="ltr">`OPEN/RULE CHANGE`</span> ثبت و از <span dir="ltr">Commit Refactor</span> جدا کن.

## <span dir="ltr">Step 0</span> — <span dir="ltr">Baseline</span>


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
- <span dir="ltr">Branch/commit</span> یا <span dir="ltr">Worktree state</span>
- خروجی <span dir="ltr">`mvn verify`</span> پیش از تغییر

## <span dir="ltr">Step 1</span> — <span dir="ltr">Smell Map</span>

حداقل شش <span dir="ltr">Smell</span> با این قالب:

| <span dir="ltr">Symbol</span> | <span dir="ltr">Smell</span> | <span dir="ltr">Concrete risk</span> | <span dir="ltr">Smallest move</span> |
|---|---|---|---|
|  |  |  |  |

عبارت «<span dir="ltr">SOLID</span> رعایت نشده» بدون <span dir="ltr">Location</span> و <span dir="ltr">Risk</span> امتیاز ندارد.

## <span dir="ltr">Step 2</span> — یک <span dir="ltr">Edge Test</span>

یکی را انتخاب کن:

- <span dir="ltr">lowercase currency</span>
- <span dir="ltr">whitespace around ID</span>
- <span dir="ltr">amount</span> با <span dir="ltr">Scale</span> زیاد
- <span dir="ltr">delimiter</span> داخل <span dir="ltr">ID</span> و اثر روی <span dir="ltr">audit key</span>
- <span dir="ltr">source/target</span> با تفاوت ظاهری <span dir="ltr">whitespace</span>

اگر <span dir="ltr">Expected behavior</span> معلوم نیست، <span dir="ltr">`OPEN`</span> ثبت کن و مورد دیگری را تست کن.

## <span dir="ltr">Step 3</span> — چهار <span dir="ltr">Checkpoint</span> سبز

1. <span dir="ltr">`AccountId`</span> برای <span dir="ltr">source/target</span>
2. <span dir="ltr">`CustomerId`</span> و <span dir="ltr">`BranchId`</span>
3. <span dir="ltr">`Money`</span> برای <span dir="ltr">amount/currency</span>
4. <span dir="ltr">Creation API</span> و <span dir="ltr">Request</span> نام‌دار

پس از هر <span dir="ltr">Checkpoint</span> تست هدفمند اجرا و نتیجه ثبت شود.

## <span dir="ltr">Step 4</span> — <span dir="ltr">Money Decision</span>

صریح تصمیم بگیر:

- <span dir="ltr">Money</span> عمومی <span dir="ltr">Signed</span> است یا این <span dir="ltr">Type</span> فقط <span dir="ltr">TransferAmount</span> مثبت است؟
- <span dir="ltr">Equality</span> عددی <span dir="ltr">Scale</span> را نادیده می‌گیرد یا نه؟
- <span dir="ltr">Rounding</span> کجا و با چه <span dir="ltr">API</span> صریح می‌شود؟
- <span dir="ltr">Currency</span> با <span dir="ltr">`java.util.Currency`</span> یا <span dir="ltr">Type</span> محدود دیگری نمایش داده می‌شود؟

<span dir="ltr">Rule</span> خیالی برای <span dir="ltr">Decimal</span>های <span dir="ltr">IRR</span> نساز.

## <span dir="ltr">Step 5</span> — <span dir="ltr">Factory Decision</span>

سه گزینه را با <span dir="ltr">Forces</span> مقایسه کن:


</div>

<div dir="ltr" align="left">

```text
public constructor | static factory | factory class
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Factory class</span> فقط وقتی معتبر است که <span dir="ltr">Creation decision</span> یا <span dir="ltr">Dependency</span> واقعی داشته باشد.

## <span dir="ltr">Step 6</span> — <span dir="ltr">Compatibility</span>

اگر <span dir="ltr">Constructor</span> یا <span dir="ltr">`auditKey`</span> قبلی را تغییر می‌دهی، رفتار <span dir="ltr">Characterization</span> را با <span dir="ltr">Adapter</span> یا <span dir="ltr">Test</span> روشن حفظ کن. حذف <span dir="ltr">API</span> قبلی باید تصمیم جدا باشد.

## <span dir="ltr">Step 7</span> — <span dir="ltr">Final verification</span>


</div>

<div dir="ltr" align="left">

```bash
mvn -B -ntp verify
```

</div>

<div dir="rtl" align="right">


تمام تست‌های <span dir="ltr">Week 01</span> و <span dir="ltr">Week 02</span> و <span dir="ltr">Spring context</span> باید سبز بمانند.

## <span dir="ltr">Step 8</span> — <span dir="ltr">Self-review</span>

1. کدام خطا اکنون <span dir="ltr">Compile-time</span> یا <span dir="ltr">creation-time</span> متوقف می‌شود؟
2. کدام <span dir="ltr">Coupling</span> کمتر شد؟
3. چند <span dir="ltr">Type</span> تازه ساختی و هزینه‌شان چیست؟
4. کدام <span dir="ltr">Rule</span> را عمداً تغییر ندادی؟
5. چه <span dir="ltr">Debt/Unknown</span>ی باقی ماند؟

## <span dir="ltr">Acceptance criteria</span>

- <span dir="ltr">Baseline</span> و <span dir="ltr">Refactor</span> هر دو <span dir="ltr">Evidence</span> سبز دارند.
- حداقل یک <span dir="ltr">Edge Test</span> تازه وجود دارد.
- <span dir="ltr">amount/currency</span> به <span dir="ltr">Concept</span> منسجم تبدیل شده‌اند.
- <span dir="ltr">Typed IDs</span> قابل‌جابه‌جایی نیستند.
- <span dir="ltr">`double`</span>، <span dir="ltr">Setter</span>، <span dir="ltr">Rounding</span> پنهان و <span dir="ltr">Base hierarchy</span> غیرضروری وجود ندارد.
- <span dir="ltr">Factory</span> یا رد آن با <span dir="ltr">Alternative</span>، <span dir="ltr">Cost</span> و <span dir="ltr">Revisit trigger</span> دفاع شده است.
- <span dir="ltr">`mvn verify`</span> سبز است.


</div>
