<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 09 Exercise</bdi> — <bdi dir="ltr">Monzo Architecture Review</bdi>

- <bdi dir="ltr">Timebox: 15 minutes after reading the case file</bdi>
- <bdi dir="ltr">Output: one-page review in Week 02 Workbook</bdi>
- <bdi dir="ltr">Rule:</bdi> فقط از شواهد پرونده استفاده کن؛ حدس را با <bdi dir="ltr">`INFERENCE`</bdi> یا <bdi dir="ltr">`UNKNOWN`</bdi> برچسب بزن.

## <bdi dir="ltr">Part 1</bdi> — <bdi dir="ltr">Five-point timeline</bdi>

پنج نقطه‌ای را انتخاب کن که تغییر <bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Architecture</bdi> را هم‌زمان نشان می‌دهند:

| <bdi dir="ltr">Date/phase</bdi> | <bdi dir="ltr">Business/domain change</bdi> | <bdi dir="ltr">Architecture/technology response</bdi> | <bdi dir="ltr">New risk</bdi> |
|---|---|---|---|
|  |  |  |  |

## <bdi dir="ltr">Part 2</bdi> — <bdi dir="ltr">Fact</bdi> / <bdi dir="ltr">Inference</bdi> / <bdi dir="ltr">Unknown</bdi>

شش ادعا بنویس؛ حداقل دو مورد از هر نوع:

| <bdi dir="ltr">Claim</bdi> | <bdi dir="ltr">FACT</bdi> / <bdi dir="ltr">INFERENCE</bdi> / <bdi dir="ltr">UNKNOWN</bdi> | <bdi dir="ltr">Evidence or reason</bdi> |
|---|---|---|
|  |  |  |

حداقل یکی از ادعاها باید دربارهٔ <bdi dir="ltr">Domain/Bounded Context</bdi> و یکی دربارهٔ <bdi dir="ltr">Technology stack</bdi> فعلی باشد.

## <bdi dir="ltr">Part 3</bdi> — <bdi dir="ltr">Ownership analysis</bdi>

برای <bdi dir="ltr">Failure</bdi> کنترل‌های <bdi dir="ltr">Financial Crime</bdi> پاسخ بده:

1. کدام <bdi dir="ltr">Business decision</bdi>ها <bdi dir="ltr">Owner</bdi> لازم داشتند؟
2. کدام داده‌ها برای <bdi dir="ltr">Onboarding/Risk/Monitoring Authority</bdi> لازم داشتند؟
3. چرا یک <bdi dir="ltr">Microservice</bdi> جدید به‌تنهایی راه‌حل نبود؟
4. چه <bdi dir="ltr">Fitness Function</bdi> یا <bdi dir="ltr">Control evidence</bdi> می‌توانست هشدار زودتری بدهد؟

## <bdi dir="ltr">Part 4</bdi> — <bdi dir="ltr">ADR-lite</bdi>

### <bdi dir="ltr">Decision question</bdi>

آیا <bdi dir="ltr">`banking-modulith`</bdi> ما باید با استناد به <bdi dir="ltr">Monzo</bdi> از همین حالا <bdi dir="ltr">Microservice-first</bdi> شود؟

### <bdi dir="ltr">Required format</bdi>

- <bdi dir="ltr">Context:</bdi>
- <bdi dir="ltr">Forces:</bdi>
- <bdi dir="ltr">Option A</bdi> — <bdi dir="ltr">retain Modular Monolith:</bdi>
- <bdi dir="ltr">Option B</bdi> — <bdi dir="ltr">Microservice-first:</bdi>
- <bdi dir="ltr">Decision:</bdi>
- <bdi dir="ltr">Consequences:</bdi>
- <bdi dir="ltr">Verification:</bdi>
- <bdi dir="ltr">Revisit trigger:</bdi>

## <bdi dir="ltr">Acceptance criteria</bdi>

- <bdi dir="ltr">Timeline</bdi> فقط <bdi dir="ltr">Feature list</bdi> نیست و <bdi dir="ltr">Risk</bdi> را نشان می‌دهد.
- <bdi dir="ltr">Fact</bdi> و <bdi dir="ltr">Inference</bdi> مخلوط نشده‌اند.
- <bdi dir="ltr">Architecture</bdi> جاری از <bdi dir="ltr">Architecture</bdi> تاریخی تفکیک شده است.
- <bdi dir="ltr">FCA finding</bdi> به «یک <bdi dir="ltr">Bug</bdi>» تقلیل داده نشده است.
- <bdi dir="ltr">ADR-lite</bdi> از <bdi dir="ltr">Monzo</bdi> درس می‌گیرد، اما <bdi dir="ltr">Stack</bdi> و <bdi dir="ltr">Scale</bdi> آن را <bdi dir="ltr">Copy</bdi> نمی‌کند.

</div>
