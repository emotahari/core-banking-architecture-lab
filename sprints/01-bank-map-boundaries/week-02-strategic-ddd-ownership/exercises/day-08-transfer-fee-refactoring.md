<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 08 Exercise</span> — <span dir="ltr">Transfer Fee Refactoring Kata</span>

- <span dir="ltr">Timebox: 65 minutes coding</span> + <span dir="ltr">10 minutes self-review</span>
- <span dir="ltr">Working directory:</span> <span dir="ltr">`backend/banking-modulith`</span>
- <span dir="ltr">Starter package:</span> <span dir="ltr">`com.example.corebankinglab.craftsmanship.week02`</span>
- <span dir="ltr">Output: refactored code</span> + <span dir="ltr">tests</span> + [<span dir="ltr">Code Review Checklist</span>](../artifacts/day-08-code-review-checklist.md)

## <span dir="ltr">Rule of the exercise</span>

قواعد عددی <span dir="ltr">Baseline</span> را در <span dir="ltr">Refactor</span> تغییر نده. نرخ‌ها ساختگی‌اند، اما <span dir="ltr">Characterization behavior</span> باید ثابت بماند. هر <span dir="ltr">Rule change</span> پیشنهادی را فقط در بخش <span dir="ltr">`OPEN`</span> ثبت کن.

## <span dir="ltr">Step 0</span> — <span dir="ltr">Record the baseline</span>


</div>

<div dir="ltr" align="left">

```bash
mvn -Dtest=LegacyTransferFeeCalculatorCharacterizationTest test
```

</div>

<div dir="rtl" align="right">


ثبت کن:

- تعداد <span dir="ltr">Test</span>ها
- نتیجه
- مدت اجرا
- <span dir="ltr">Commit/SHA</span> یا وضعیت <span dir="ltr">Worktree</span>

## <span dir="ltr">Step 1</span> — <span dir="ltr">Create your smell map</span>

حداقل پنج <span dir="ltr">Smell</span> را با این قالب بنویس:

| <span dir="ltr">File:line or symbol</span> | <span dir="ltr">Smell</span> | <span dir="ltr">Concrete change risk</span> | <span dir="ltr">Proposed smallest move</span> |
|---|---|---|---|
|  |  |  |  |

عبارت‌هایی مانند «کد کثیف است» یا «<span dir="ltr">SOLID</span> رعایت نشده» بدون محل و اثر امتیاز ندارد.

## <span dir="ltr">Step 2</span> — <span dir="ltr">Add one characterization/edge test</span>

یکی از <span dir="ltr">Unknown</span>های زیر را انتخاب کن یا مورد بهتری پیدا کن:

- <span dir="ltr">Blank rail</span>
- <span dir="ltr">Case sensitivity</span>
- <span dir="ltr">discount on zero-fee rail</span>
- <span dir="ltr">overflow boundary</span>
- <span dir="ltr">ordering of cap and discount</span>

اگر <span dir="ltr">Expected behavior</span> از <span dir="ltr">Fixture</span> قابل استنتاج نیست، آن را به‌عنوان <span dir="ltr">`OPEN`</span> نگه دار و یک <span dir="ltr">Edge Case</span> دیگر را <span dir="ltr">Test</span> کن. <span dir="ltr">Rule</span> بانکی را حدس نزن.

## <span dir="ltr">Step 3</span> — <span dir="ltr">Refactor in green steps</span>

حداقل چهار <span dir="ltr">Checkpoint</span> داشته باش:

1. <span dir="ltr">type-safe Rail</span>
2. <span dir="ltr">named pricing constants/rules</span>
3. <span dir="ltr">separated selection and calculation</span>
4. <span dir="ltr">explicit customer pricing meaning</span>

پس از هر <span dir="ltr">Checkpoint</span> تست را اجرا کن. اگر <span dir="ltr">Git</span> در دسترس است، <span dir="ltr">Commit</span> کوچک بساز؛ در غیر این صورت <span dir="ltr">Diff/</span>زمان <span dir="ltr">Checkpoint</span> را ثبت کن.

## <span dir="ltr">Step 4</span> — <span dir="ltr">Make the pattern decision</span>

یکی از این دو خروجی هر دو معتبر است:

### <span dir="ltr">Option A</span> — <span dir="ltr">Keep an explicit switch</span>

اگر سه حالت بسته و ساده‌اند، یک <span dir="ltr">`switch`</span> خوانا با <span dir="ltr">Method</span>های کوچک نگه دار. توضیح بده چه <span dir="ltr">Revisit Trigger</span>ی <span dir="ltr">Strategy</span> را لازم می‌کند.

### <span dir="ltr">Option B</span> — <span dir="ltr">Introduce Strategy</span> + <span dir="ltr">Registry/Factory</span>

اگر <span dir="ltr">Variation</span> مستقل را کافی می‌دانی:

- <span dir="ltr">Contract</span> کوچک و دامینی بساز.
- هر <span dir="ltr">Policy</span> را مستقل تست کن.
- <span dir="ltr">Selection</span> را در <span dir="ltr">Registry/Factory</span> متمرکز کن.
- <span dir="ltr">Missing/Duplicate policy</span> را <span dir="ltr">Fail-fast</span> کن.
- <span dir="ltr">Discount</span> را آگاهانه قبل یا بعد از <span dir="ltr">Base fee</span> اعمال کن؛ رفتار موجود را حفظ کن.

در هیچ گزینه‌ای <span dir="ltr">Reflection</span>، <span dir="ltr">Annotation scanning</span>، <span dir="ltr">Spring Context</span> یا <span dir="ltr">Database</span> لازم نیست.

## <span dir="ltr">Step 5</span> — <span dir="ltr">Remove the flag meaningfully</span>

<span dir="ltr">`boolean preferredCustomer`</span> را با یک مفهوم صریح جایگزین کن. فقط تغییر نام پارامتر <span dir="ltr">Boolean</span> کافی نیست. <span dir="ltr">Signature</span> جدید باید بدون خواندن <span dir="ltr">Implementation</span> قابل فهم باشد.

## <span dir="ltr">Step 6</span> — <span dir="ltr">Final verification</span>


</div>

<div dir="ltr" align="left">

```bash
mvn verify
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Baseline</span> اصلی <span dir="ltr">Week 02</span> نیز باید سبز بماند. <span dir="ltr">Refactor</span> محلی نباید <span dir="ltr">Module Verification</span> یا <span dir="ltr">Spring context</span> را بشکند.

## <span dir="ltr">Step 7</span> — <span dir="ltr">Self-review</span>

[<span dir="ltr">Code Review Checklist</span>](../artifacts/day-08-code-review-checklist.md) را کامل کن و به این سه سؤال پاسخ بده:

1. کدام <span dir="ltr">Change coupling</span> واقعاً کمتر شد؟
2. <span dir="ltr">Pattern</span> انتخابی چه <span dir="ltr">Complexity</span> تازه‌ای ایجاد کرد؟
3. اگر فقط یک <span dir="ltr">Rail</span> داشتیم، کدام <span dir="ltr">Type</span>ها را حذف می‌کردی؟

## <span dir="ltr">Acceptance criteria</span>

- همهٔ <span dir="ltr">Characterization test</span>های قبلی سبزند.
- حداقل یک <span dir="ltr">Edge Test</span> جدید وجود دارد.
- <span dir="ltr">String rail</span> از <span dir="ltr">Core calculation</span> حذف شده است.
- <span dir="ltr">Magic literal</span>ها نام و <span dir="ltr">Scope</span> معنادار دارند.
- <span dir="ltr">Flag argument</span> با <span dir="ltr">Concept</span> صریح جایگزین شده است.
- <span dir="ltr">Strategy</span> یا رد آن با <span dir="ltr">Forces</span> دفاع شده است.
- هیچ <span dir="ltr">`common`</span>, <span dir="ltr">`utils`</span>, <span dir="ltr">`BaseStrategy`</span>, <span dir="ltr">`AbstractFactoryFactory`</span> یا <span dir="ltr">Spring Bean</span> غیرضروری ایجاد نشده است.
- <span dir="ltr">`mvn verify`</span> سبز است.

## <span dir="ltr">Required evidence in Workbook</span>

1. <span dir="ltr">Baseline output</span>
2. <span dir="ltr">Smell Map</span>
3. <span dir="ltr">Pattern Decision</span>
4. فهرست <span dir="ltr">Checkpoint</span>ها
5. <span dir="ltr">Test</span> جدید
6. <span dir="ltr">Final test output</span>
7. <span dir="ltr">Self-review</span> و <span dir="ltr">Debt</span> باقی‌مانده

راه‌حل کامل در مخزن قرار نگرفته است. هدف این تمرین مشاهدهٔ تصمیم و <span dir="ltr">Refactor</span> توست، نه مقایسهٔ ظاهری با یک <span dir="ltr">Class diagram</span> آماده.

</div>
