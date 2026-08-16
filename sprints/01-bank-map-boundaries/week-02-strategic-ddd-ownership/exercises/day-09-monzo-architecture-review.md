<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 09 Exercise</span> — <span dir="ltr">Monzo Architecture Review</span>

- <span dir="ltr">Timebox: 15 minutes after reading the case file</span>
- <span dir="ltr">Output: one-page review in Week 02 Workbook</span>
- <span dir="ltr">Rule:</span> فقط از شواهد پرونده استفاده کن؛ حدس را با <span dir="ltr">`INFERENCE`</span> یا <span dir="ltr">`UNKNOWN`</span> برچسب بزن.

## <span dir="ltr">Part 1</span> — <span dir="ltr">Five-point timeline</span>

پنج نقطه‌ای را انتخاب کن که تغییر <span dir="ltr">Capability</span> و <span dir="ltr">Architecture</span> را هم‌زمان نشان می‌دهند:

| <span dir="ltr">Date/phase</span> | <span dir="ltr">Business/domain change</span> | <span dir="ltr">Architecture/technology response</span> | <span dir="ltr">New risk</span> |
|---|---|---|---|
|  |  |  |  |

## <span dir="ltr">Part 2</span> — <span dir="ltr">Fact</span> / <span dir="ltr">Inference</span> / <span dir="ltr">Unknown</span>

شش ادعا بنویس؛ حداقل دو مورد از هر نوع:

| <span dir="ltr">Claim</span> | <span dir="ltr">FACT</span> / <span dir="ltr">INFERENCE</span> / <span dir="ltr">UNKNOWN</span> | <span dir="ltr">Evidence or reason</span> |
|---|---|---|
|  |  |  |

حداقل یکی از ادعاها باید دربارهٔ <span dir="ltr">Domain/Bounded Context</span> و یکی دربارهٔ <span dir="ltr">Technology stack</span> فعلی باشد.

## <span dir="ltr">Part 3</span> — <span dir="ltr">Ownership analysis</span>

برای <span dir="ltr">Failure</span> کنترل‌های <span dir="ltr">Financial Crime</span> پاسخ بده:

1. کدام <span dir="ltr">Business decision</span>ها <span dir="ltr">Owner</span> لازم داشتند؟
2. کدام داده‌ها برای <span dir="ltr">Onboarding/Risk/Monitoring Authority</span> لازم داشتند؟
3. چرا یک <span dir="ltr">Microservice</span> جدید به‌تنهایی راه‌حل نبود؟
4. چه <span dir="ltr">Fitness Function</span> یا <span dir="ltr">Control evidence</span> می‌توانست هشدار زودتری بدهد؟

## <span dir="ltr">Part 4</span> — <span dir="ltr">ADR-lite</span>

### <span dir="ltr">Decision question</span>

آیا <span dir="ltr">`banking-modulith`</span> ما باید با استناد به <span dir="ltr">Monzo</span> از همین حالا <span dir="ltr">Microservice-first</span> شود؟

### <span dir="ltr">Required format</span>

- <span dir="ltr">Context:</span>
- <span dir="ltr">Forces:</span>
- <span dir="ltr">Option A</span> — <span dir="ltr">retain Modular Monolith:</span>
- <span dir="ltr">Option B</span> — <span dir="ltr">Microservice-first:</span>
- <span dir="ltr">Decision:</span>
- <span dir="ltr">Consequences:</span>
- <span dir="ltr">Verification:</span>
- <span dir="ltr">Revisit trigger:</span>

## <span dir="ltr">Acceptance criteria</span>

- <span dir="ltr">Timeline</span> فقط <span dir="ltr">Feature list</span> نیست و <span dir="ltr">Risk</span> را نشان می‌دهد.
- <span dir="ltr">Fact</span> و <span dir="ltr">Inference</span> مخلوط نشده‌اند.
- <span dir="ltr">Architecture</span> جاری از <span dir="ltr">Architecture</span> تاریخی تفکیک شده است.
- <span dir="ltr">FCA finding</span> به «یک <span dir="ltr">Bug</span>» تقلیل داده نشده است.
- <span dir="ltr">ADR-lite</span> از <span dir="ltr">Monzo</span> درس می‌گیرد، اما <span dir="ltr">Stack</span> و <span dir="ltr">Scale</span> آن را <span dir="ltr">Copy</span> نمی‌کند.

</div>
