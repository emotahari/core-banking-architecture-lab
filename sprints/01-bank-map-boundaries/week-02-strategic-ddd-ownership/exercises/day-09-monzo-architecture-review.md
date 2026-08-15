# Day 09 Exercise — Monzo Architecture Review

- Timebox: 15 minutes after reading the case file
- Output: one-page review in Week 02 Workbook
- Rule: فقط از شواهد پرونده استفاده کن؛ حدس را با `INFERENCE` یا `UNKNOWN` برچسب بزن.

## Part 1 — Five-point timeline

پنج نقطه‌ای را انتخاب کن که تغییر Capability و Architecture را هم‌زمان نشان می‌دهند:

| Date/phase | Business/domain change | Architecture/technology response | New risk |
|---|---|---|---|
|  |  |  |  |

## Part 2 — Fact / Inference / Unknown

شش ادعا بنویس؛ حداقل دو مورد از هر نوع:

| Claim | FACT / INFERENCE / UNKNOWN | Evidence or reason |
|---|---|---|
|  |  |  |

حداقل یکی از ادعاها باید دربارهٔ Domain/Bounded Context و یکی دربارهٔ Technology stack فعلی باشد.

## Part 3 — Ownership analysis

برای Failure کنترل‌های Financial Crime پاسخ بده:

1. کدام Business decisionها Owner لازم داشتند؟
2. کدام داده‌ها برای Onboarding/Risk/Monitoring Authority لازم داشتند؟
3. چرا یک Microservice جدید به‌تنهایی راه‌حل نبود؟
4. چه Fitness Function یا Control evidence می‌توانست هشدار زودتری بدهد؟

## Part 4 — ADR-lite

### Decision question

آیا `banking-modulith` ما باید با استناد به Monzo از همین حالا Microservice-first شود؟

### Required format

- Context:
- Forces:
- Option A — retain Modular Monolith:
- Option B — Microservice-first:
- Decision:
- Consequences:
- Verification:
- Revisit trigger:

## Acceptance criteria

- Timeline فقط Feature list نیست و Risk را نشان می‌دهد.
- Fact و Inference مخلوط نشده‌اند.
- Architecture جاری از Architecture تاریخی تفکیک شده است.
- FCA finding به «یک Bug» تقلیل داده نشده است.
- ADR-lite از Monzo درس می‌گیرد، اما Stack و Scale آن را Copy نمی‌کند.
