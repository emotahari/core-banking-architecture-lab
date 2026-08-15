<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 08 Exercise</bdi> — <bdi dir="ltr">Transfer Fee Refactoring Kata</bdi>

- <bdi dir="ltr">Timebox: 65 minutes coding</bdi> + <bdi dir="ltr">10 minutes self-review</bdi>
- <bdi dir="ltr">Working directory:</bdi> <bdi dir="ltr">`backend/banking-modulith`</bdi>
- <bdi dir="ltr">Starter package:</bdi> <bdi dir="ltr">`com.example.corebankinglab.craftsmanship.week02`</bdi>
- <bdi dir="ltr">Output: refactored code</bdi> + <bdi dir="ltr">tests</bdi> + [<bdi dir="ltr">Code Review Checklist</bdi>](../artifacts/day-08-code-review-checklist.md)

## <bdi dir="ltr">Rule of the exercise</bdi>

قواعد عددی <bdi dir="ltr">Baseline</bdi> را در <bdi dir="ltr">Refactor</bdi> تغییر نده. نرخ‌ها ساختگی‌اند، اما <bdi dir="ltr">Characterization behavior</bdi> باید ثابت بماند. هر <bdi dir="ltr">Rule change</bdi> پیشنهادی را فقط در بخش <bdi dir="ltr">`OPEN`</bdi> ثبت کن.

## <bdi dir="ltr">Step 0</bdi> — <bdi dir="ltr">Record the baseline</bdi>


</div>

<div dir="ltr" align="left">

```bash
mvn -Dtest=LegacyTransferFeeCalculatorCharacterizationTest test
```

</div>

<div dir="rtl" align="right">


ثبت کن:

- تعداد <bdi dir="ltr">Test</bdi>ها
- نتیجه
- مدت اجرا
- <bdi dir="ltr">Commit/SHA</bdi> یا وضعیت <bdi dir="ltr">Worktree</bdi>

## <bdi dir="ltr">Step 1</bdi> — <bdi dir="ltr">Create your smell map</bdi>

حداقل پنج <bdi dir="ltr">Smell</bdi> را با این قالب بنویس:

| <bdi dir="ltr">File:line or symbol</bdi> | <bdi dir="ltr">Smell</bdi> | <bdi dir="ltr">Concrete change risk</bdi> | <bdi dir="ltr">Proposed smallest move</bdi> |
|---|---|---|---|
|  |  |  |  |

عبارت‌هایی مانند «کد کثیف است» یا «<bdi dir="ltr">SOLID</bdi> رعایت نشده» بدون محل و اثر امتیاز ندارد.

## <bdi dir="ltr">Step 2</bdi> — <bdi dir="ltr">Add one characterization/edge test</bdi>

یکی از <bdi dir="ltr">Unknown</bdi>های زیر را انتخاب کن یا مورد بهتری پیدا کن:

- <bdi dir="ltr">Blank rail</bdi>
- <bdi dir="ltr">Case sensitivity</bdi>
- <bdi dir="ltr">discount on zero-fee rail</bdi>
- <bdi dir="ltr">overflow boundary</bdi>
- <bdi dir="ltr">ordering of cap and discount</bdi>

اگر <bdi dir="ltr">Expected behavior</bdi> از <bdi dir="ltr">Fixture</bdi> قابل استنتاج نیست، آن را به‌عنوان <bdi dir="ltr">`OPEN`</bdi> نگه دار و یک <bdi dir="ltr">Edge Case</bdi> دیگر را <bdi dir="ltr">Test</bdi> کن. <bdi dir="ltr">Rule</bdi> بانکی را حدس نزن.

## <bdi dir="ltr">Step 3</bdi> — <bdi dir="ltr">Refactor in green steps</bdi>

حداقل چهار <bdi dir="ltr">Checkpoint</bdi> داشته باش:

1. <bdi dir="ltr">type-safe Rail</bdi>
2. <bdi dir="ltr">named pricing constants/rules</bdi>
3. <bdi dir="ltr">separated selection and calculation</bdi>
4. <bdi dir="ltr">explicit customer pricing meaning</bdi>

پس از هر <bdi dir="ltr">Checkpoint</bdi> تست را اجرا کن. اگر <bdi dir="ltr">Git</bdi> در دسترس است، <bdi dir="ltr">Commit</bdi> کوچک بساز؛ در غیر این صورت <bdi dir="ltr">Diff/</bdi>زمان <bdi dir="ltr">Checkpoint</bdi> را ثبت کن.

## <bdi dir="ltr">Step 4</bdi> — <bdi dir="ltr">Make the pattern decision</bdi>

یکی از این دو خروجی هر دو معتبر است:

### <bdi dir="ltr">Option A</bdi> — <bdi dir="ltr">Keep an explicit switch</bdi>

اگر سه حالت بسته و ساده‌اند، یک <bdi dir="ltr">`switch`</bdi> خوانا با <bdi dir="ltr">Method</bdi>های کوچک نگه دار. توضیح بده چه <bdi dir="ltr">Revisit Trigger</bdi>ی <bdi dir="ltr">Strategy</bdi> را لازم می‌کند.

### <bdi dir="ltr">Option B</bdi> — <bdi dir="ltr">Introduce Strategy</bdi> + <bdi dir="ltr">Registry/Factory</bdi>

اگر <bdi dir="ltr">Variation</bdi> مستقل را کافی می‌دانی:

- <bdi dir="ltr">Contract</bdi> کوچک و دامینی بساز.
- هر <bdi dir="ltr">Policy</bdi> را مستقل تست کن.
- <bdi dir="ltr">Selection</bdi> را در <bdi dir="ltr">Registry/Factory</bdi> متمرکز کن.
- <bdi dir="ltr">Missing/Duplicate policy</bdi> را <bdi dir="ltr">Fail-fast</bdi> کن.
- <bdi dir="ltr">Discount</bdi> را آگاهانه قبل یا بعد از <bdi dir="ltr">Base fee</bdi> اعمال کن؛ رفتار موجود را حفظ کن.

در هیچ گزینه‌ای <bdi dir="ltr">Reflection</bdi>، <bdi dir="ltr">Annotation scanning</bdi>، <bdi dir="ltr">Spring Context</bdi> یا <bdi dir="ltr">Database</bdi> لازم نیست.

## <bdi dir="ltr">Step 5</bdi> — <bdi dir="ltr">Remove the flag meaningfully</bdi>

<bdi dir="ltr">`boolean preferredCustomer`</bdi> را با یک مفهوم صریح جایگزین کن. فقط تغییر نام پارامتر <bdi dir="ltr">Boolean</bdi> کافی نیست. <bdi dir="ltr">Signature</bdi> جدید باید بدون خواندن <bdi dir="ltr">Implementation</bdi> قابل فهم باشد.

## <bdi dir="ltr">Step 6</bdi> — <bdi dir="ltr">Final verification</bdi>


</div>

<div dir="ltr" align="left">

```bash
mvn verify
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Baseline</bdi> اصلی <bdi dir="ltr">Week 02</bdi> نیز باید سبز بماند. <bdi dir="ltr">Refactor</bdi> محلی نباید <bdi dir="ltr">Module Verification</bdi> یا <bdi dir="ltr">Spring context</bdi> را بشکند.

## <bdi dir="ltr">Step 7</bdi> — <bdi dir="ltr">Self-review</bdi>

[<bdi dir="ltr">Code Review Checklist</bdi>](../artifacts/day-08-code-review-checklist.md) را کامل کن و به این سه سؤال پاسخ بده:

1. کدام <bdi dir="ltr">Change coupling</bdi> واقعاً کمتر شد؟
2. <bdi dir="ltr">Pattern</bdi> انتخابی چه <bdi dir="ltr">Complexity</bdi> تازه‌ای ایجاد کرد؟
3. اگر فقط یک <bdi dir="ltr">Rail</bdi> داشتیم، کدام <bdi dir="ltr">Type</bdi>ها را حذف می‌کردی؟

## <bdi dir="ltr">Acceptance criteria</bdi>

- همهٔ <bdi dir="ltr">Characterization test</bdi>های قبلی سبزند.
- حداقل یک <bdi dir="ltr">Edge Test</bdi> جدید وجود دارد.
- <bdi dir="ltr">String rail</bdi> از <bdi dir="ltr">Core calculation</bdi> حذف شده است.
- <bdi dir="ltr">Magic literal</bdi>ها نام و <bdi dir="ltr">Scope</bdi> معنادار دارند.
- <bdi dir="ltr">Flag argument</bdi> با <bdi dir="ltr">Concept</bdi> صریح جایگزین شده است.
- <bdi dir="ltr">Strategy</bdi> یا رد آن با <bdi dir="ltr">Forces</bdi> دفاع شده است.
- هیچ <bdi dir="ltr">`common`</bdi>, <bdi dir="ltr">`utils`</bdi>, <bdi dir="ltr">`BaseStrategy`</bdi>, <bdi dir="ltr">`AbstractFactoryFactory`</bdi> یا <bdi dir="ltr">Spring Bean</bdi> غیرضروری ایجاد نشده است.
- <bdi dir="ltr">`mvn verify`</bdi> سبز است.

## <bdi dir="ltr">Required evidence in Workbook</bdi>

1. <bdi dir="ltr">Baseline output</bdi>
2. <bdi dir="ltr">Smell Map</bdi>
3. <bdi dir="ltr">Pattern Decision</bdi>
4. فهرست <bdi dir="ltr">Checkpoint</bdi>ها
5. <bdi dir="ltr">Test</bdi> جدید
6. <bdi dir="ltr">Final test output</bdi>
7. <bdi dir="ltr">Self-review</bdi> و <bdi dir="ltr">Debt</bdi> باقی‌مانده

راه‌حل کامل در مخزن قرار نگرفته است. هدف این تمرین مشاهدهٔ تصمیم و <bdi dir="ltr">Refactor</bdi> توست، نه مقایسهٔ ظاهری با یک <bdi dir="ltr">Class diagram</bdi> آماده.

</div>
