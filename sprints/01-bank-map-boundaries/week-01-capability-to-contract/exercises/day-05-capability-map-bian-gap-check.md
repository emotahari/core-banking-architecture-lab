# Day 05 Exercise — Capability Map v1 and BIAN Gap Check

- Timebox: 40 minutes — 20 map + 20 gap check
- Inputs: [Working Draft](../artifacts/capability-map-working-draft.md) و [BIAN Gap Template](../artifacts/bian-gap-check-template.md)
- Output: Capability Map v1 با Change log

## بخش A — تثبیت L1

1. Scope و Audience را بنویس.
2. برای هر Node سطح L1، Definition یک‌جمله‌ای بساز.
3. برای پنج Node مهم `Includes/Excludes` ثبت کن.
4. موارد ناهم‌سطح، نام سامانه/Vendor/Team و عبارت‌های مبهم را علامت بزن.
5. حداکثر دو L1 را برای نمایش روش به L2 بشکن؛ کل بانک را این هفته به L3 نبر.

## بخش B — چهارلایه

هر L1 را موقتاً در یکی از این Lensها قرار بده:

- هستهٔ بانکداری
- عملیات و خدمات بانکداری
- توانمندی سازمانی
- اکوسیستم دیجیتال

برای دو مورد مرزی توضیح بده چرا طبقه‌بندی وابسته به Strategy بانک است و Boundary قطعی نیست.

## بخش C — BIAN Gap Check

پس از تکمیل Map خودت، حداقل ۱۰ مورد را در BIAN 14 بررسی کن. وضعیت فقط یکی از این‌ها باشد:

```text
MATCH | PARTIAL | GAP-LOCAL | GAP-OUR-MAP | FALSE-FRIEND | NOT-APPLICABLE
```

برای هر مورد Source link، Scope difference و تصمیم محلی بنویس.

حداقل این سه مورد را حتماً بررسی کن:

1. Current Account
2. Customer Relationship Management
3. Financial Accounting

## بخش D — Change log

هر تغییر Working Draft:

| Change | Before | After | Evidence | Consequence |
|---|---|---|---|---|
|  |  |  |  |  |

## Acceptance criteria

- L1ها تقریباً هم‌سطح و Outcome-oriented باشند.
- حداقل یک `FALSE-FRIEND` و یک `GAP-OUR-MAP` یا دلیل نبود آن ثبت شود.
- BIAN Mapping باعث ایجاد خودکار Service/Microservice نشود.
- آمار نسخه و تاریخ بررسی ثبت شود.
- Map Version به `1.0` و Status به `Candidate for Week 02 review` تغییر کند.

