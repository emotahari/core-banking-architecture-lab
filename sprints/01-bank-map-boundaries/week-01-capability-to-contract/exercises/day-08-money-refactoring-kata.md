# Day 08 Exercise — Primitive-to-Value-Object Refactoring Kata

- Timebox: 65 minutes coding + 10 minutes self-review
- Working directory: `backend/banking-modulith`
- Starter package: `com.example.corebankinglab.craftsmanship.week01`
- Output: Refactored code + tests + [Code Review Checklist](../artifacts/day-08-code-review-checklist.md)

## قانون تمرین

رفتار ثبت‌شدهٔ Baseline را در Refactor ناخواسته تغییر نده. هر تغییر Rule را `OPEN/RULE CHANGE` ثبت و از Commit Refactor جدا کن.

## Step 0 — Baseline

```bash
mvn -Dtest=PrimitiveTransferRequestCharacterizationTest test
```

ثبت کن:

- تعداد تست‌ها و نتیجه
- زمان اجرا
- Branch/commit یا Worktree state
- خروجی `mvn verify` پیش از تغییر

## Step 1 — Smell Map

حداقل شش Smell با این قالب:

| Symbol | Smell | Concrete risk | Smallest move |
|---|---|---|---|
|  |  |  |  |

عبارت «SOLID رعایت نشده» بدون Location و Risk امتیاز ندارد.

## Step 2 — یک Edge Test

یکی را انتخاب کن:

- lowercase currency
- whitespace around ID
- amount با Scale زیاد
- delimiter داخل ID و اثر روی audit key
- source/target با تفاوت ظاهری whitespace

اگر Expected behavior معلوم نیست، `OPEN` ثبت کن و مورد دیگری را تست کن.

## Step 3 — چهار Checkpoint سبز

1. `AccountId` برای source/target
2. `CustomerId` و `BranchId`
3. `Money` برای amount/currency
4. Creation API و Request نام‌دار

پس از هر Checkpoint تست هدفمند اجرا و نتیجه ثبت شود.

## Step 4 — Money Decision

صریح تصمیم بگیر:

- Money عمومی Signed است یا این Type فقط TransferAmount مثبت است؟
- Equality عددی Scale را نادیده می‌گیرد یا نه؟
- Rounding کجا و با چه API صریح می‌شود؟
- Currency با `java.util.Currency` یا Type محدود دیگری نمایش داده می‌شود؟

Rule خیالی برای Decimalهای IRR نساز.

## Step 5 — Factory Decision

سه گزینه را با Forces مقایسه کن:

```text
public constructor | static factory | factory class
```

Factory class فقط وقتی معتبر است که Creation decision یا Dependency واقعی داشته باشد.

## Step 6 — Compatibility

اگر Constructor یا `auditKey` قبلی را تغییر می‌دهی، رفتار Characterization را با Adapter یا Test روشن حفظ کن. حذف API قبلی باید تصمیم جدا باشد.

## Step 7 — Final verification

```bash
mvn -B -ntp verify
```

تمام تست‌های Week 01 و Week 02 و Spring context باید سبز بمانند.

## Step 8 — Self-review

1. کدام خطا اکنون Compile-time یا creation-time متوقف می‌شود؟
2. کدام Coupling کمتر شد؟
3. چند Type تازه ساختی و هزینه‌شان چیست؟
4. کدام Rule را عمداً تغییر ندادی؟
5. چه Debt/Unknownی باقی ماند؟

## Acceptance criteria

- Baseline و Refactor هر دو Evidence سبز دارند.
- حداقل یک Edge Test تازه وجود دارد.
- amount/currency به Concept منسجم تبدیل شده‌اند.
- Typed IDs قابل‌جابه‌جایی نیستند.
- `double`، Setter، Rounding پنهان و Base hierarchy غیرضروری وجود ندارد.
- Factory یا رد آن با Alternative، Cost و Revisit trigger دفاع شده است.
- `mvn verify` سبز است.

