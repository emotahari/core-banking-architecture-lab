# Day 08 Exercise — Transfer Fee Refactoring Kata

- Timebox: 65 minutes coding + 10 minutes self-review
- Working directory: `backend/banking-modulith`
- Starter package: `com.example.corebankinglab.craftsmanship.week02`
- Output: refactored code + tests + [Code Review Checklist](../artifacts/day-08-code-review-checklist.md)

## Rule of the exercise

قواعد عددی Baseline را در Refactor تغییر نده. نرخ‌ها ساختگی‌اند، اما Characterization behavior باید ثابت بماند. هر Rule change پیشنهادی را فقط در بخش `OPEN` ثبت کن.

## Step 0 — Record the baseline

```bash
mvn -Dtest=LegacyTransferFeeCalculatorCharacterizationTest test
```

ثبت کن:

- تعداد Testها
- نتیجه
- مدت اجرا
- Commit/SHA یا وضعیت Worktree

## Step 1 — Create your smell map

حداقل پنج Smell را با این قالب بنویس:

| File:line or symbol | Smell | Concrete change risk | Proposed smallest move |
|---|---|---|---|
|  |  |  |  |

عبارت‌هایی مانند «کد کثیف است» یا «SOLID رعایت نشده» بدون محل و اثر امتیاز ندارد.

## Step 2 — Add one characterization/edge test

یکی از Unknownهای زیر را انتخاب کن یا مورد بهتری پیدا کن:

- Blank rail
- Case sensitivity
- discount on zero-fee rail
- overflow boundary
- ordering of cap and discount

اگر Expected behavior از Fixture قابل استنتاج نیست، آن را به‌عنوان `OPEN` نگه دار و یک Edge Case دیگر را Test کن. Rule بانکی را حدس نزن.

## Step 3 — Refactor in green steps

حداقل چهار Checkpoint داشته باش:

1. type-safe Rail
2. named pricing constants/rules
3. separated selection and calculation
4. explicit customer pricing meaning

پس از هر Checkpoint تست را اجرا کن. اگر Git در دسترس است، Commit کوچک بساز؛ در غیر این صورت Diff/زمان Checkpoint را ثبت کن.

## Step 4 — Make the pattern decision

یکی از این دو خروجی هر دو معتبر است:

### Option A — Keep an explicit switch

اگر سه حالت بسته و ساده‌اند، یک `switch` خوانا با Methodهای کوچک نگه دار. توضیح بده چه Revisit Triggerی Strategy را لازم می‌کند.

### Option B — Introduce Strategy + Registry/Factory

اگر Variation مستقل را کافی می‌دانی:

- Contract کوچک و دامینی بساز.
- هر Policy را مستقل تست کن.
- Selection را در Registry/Factory متمرکز کن.
- Missing/Duplicate policy را Fail-fast کن.
- Discount را آگاهانه قبل یا بعد از Base fee اعمال کن؛ رفتار موجود را حفظ کن.

در هیچ گزینه‌ای Reflection، Annotation scanning، Spring Context یا Database لازم نیست.

## Step 5 — Remove the flag meaningfully

`boolean preferredCustomer` را با یک مفهوم صریح جایگزین کن. فقط تغییر نام پارامتر Boolean کافی نیست. Signature جدید باید بدون خواندن Implementation قابل فهم باشد.

## Step 6 — Final verification

```bash
mvn verify
```

Baseline اصلی Week 02 نیز باید سبز بماند. Refactor محلی نباید Module Verification یا Spring context را بشکند.

## Step 7 — Self-review

[Code Review Checklist](../artifacts/day-08-code-review-checklist.md) را کامل کن و به این سه سؤال پاسخ بده:

1. کدام Change coupling واقعاً کمتر شد؟
2. Pattern انتخابی چه Complexity تازه‌ای ایجاد کرد؟
3. اگر فقط یک Rail داشتیم، کدام Typeها را حذف می‌کردی؟

## Acceptance criteria

- همهٔ Characterization testهای قبلی سبزند.
- حداقل یک Edge Test جدید وجود دارد.
- String rail از Core calculation حذف شده است.
- Magic literalها نام و Scope معنادار دارند.
- Flag argument با Concept صریح جایگزین شده است.
- Strategy یا رد آن با Forces دفاع شده است.
- هیچ `common`, `utils`, `BaseStrategy`, `AbstractFactoryFactory` یا Spring Bean غیرضروری ایجاد نشده است.
- `mvn verify` سبز است.

## Required evidence in Workbook

1. Baseline output
2. Smell Map
3. Pattern Decision
4. فهرست Checkpointها
5. Test جدید
6. Final test output
7. Self-review و Debt باقی‌مانده

راه‌حل کامل در مخزن قرار نگرفته است. هدف این تمرین مشاهدهٔ تصمیم و Refactor توست، نه مقایسهٔ ظاهری با یک Class diagram آماده.
