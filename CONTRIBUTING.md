<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# روش کار در مخزن

## وضعیت‌ها

<bdi dir="ltr">Board</bdi> دوره فقط این وضعیت‌ها را دارد:


</div>

<div dir="ltr" align="left">

~~~text
Backlog → Ready → Doing → Review → Gate → Done
~~~

</div>

<div dir="rtl" align="right">


در هر زمان فقط یک روز در <bdi dir="ltr">Doing</bdi> است.

## نام‌گذاری <bdi dir="ltr">Branch</bdi> و <bdi dir="ltr">Commit</bdi>

- <bdi dir="ltr">Branch</bdi> روزانه: <bdi dir="ltr">learning/s01-w01-d01</bdi>
- <bdi dir="ltr">Commit</bdi> روزانه: <bdi dir="ltr">S01W01D01: architecture baseline</bdi>
- پایان هفته: <bdi dir="ltr">tag</bdi> با الگوی <bdi dir="ltr">week-01-done</bdi>
- پایان <bdi dir="ltr">Gate: tag</bdi> با الگوی <bdi dir="ltr">gate-01-passed</bdi>

تا زمانی که تمرین روز بازبینی نشده، عبارت <bdi dir="ltr">done</bdi> در <bdi dir="ltr">Commit</bdi> استفاده نمی‌شود.

## مسیر پاسخ‌ها

پاسخ هر تمرین در پوشهٔ <bdi dir="ltr">submissions</bdi> همان هفته نوشته می‌شود. محتوای تولیدشده توسط استاد در <bdi dir="ltr">lessons</bdi> و پاسخ دانشجو در <bdi dir="ltr">submissions</bdi> می‌ماند تا تغییر مدل ذهنی در طول دوره قابل مشاهده باشد.

## <bdi dir="ltr">Definition of Done</bdi> هفتگی

- <bdi dir="ltr">Artifact</bdi> یا کد در <bdi dir="ltr">Git</bdi> ثبت شده باشد.
- <bdi dir="ltr">mvn verify</bdi> موفق باشد.
- قواعد دامینی جدید <bdi dir="ltr">Unit Test</bdi> داشته باشند.
- مرزهای جدید با <bdi dir="ltr">Architecture Test</bdi> یا <bdi dir="ltr">Module Verification</bdi> کنترل شوند.
- تغییر قرارداد در <bdi dir="ltr">OpenAPI</bdi> یا <bdi dir="ltr">AsyncAPI</bdi> ثبت شود.
- دست‌کم یک <bdi dir="ltr">Edge Case</bdi> یا <bdi dir="ltr">Failure</bdi> آزموده شود.
- تصمیم غیر بدیهی در <bdi dir="ltr">ADR</bdi> ثبت شود.
- گزارش هفته تکمیل شود.
- دفاع ده‌دقیقه‌ای قابل ارائه باشد.
- از <bdi dir="ltr">Week 02</bdi>، <bdi dir="ltr">Code Craft Lab</bdi> شامل <bdi dir="ltr">Baseline</bdi>، <bdi dir="ltr">Characterization Test</bdi>، <bdi dir="ltr">Pattern Decision</bdi>، <bdi dir="ltr">Edge Test</bdi> و <bdi dir="ltr">Self-review</bdi> تکمیل شود.
- از <bdi dir="ltr">Week 02</bdi>، <bdi dir="ltr">Core Banking Case File</bdi> با تفکیک <bdi dir="ltr">Fact/Inference/Unknown</bdi> و یک تصمیم قابل انتقال مرور شود.

مورد نامرتبط با عبارت <bdi dir="ltr">Not Applicable</bdi> و دلیل ثبت می‌شود؛ خالی نمی‌ماند.

## قواعد <bdi dir="ltr">Review</bdi>

<bdi dir="ltr">Review</bdi> فقط به «درست/غلط» ختم نمی‌شود. برای هر ایراد باید ثبت شود:

1. محل دقیق ایراد
2. نوع ایراد: <bdi dir="ltr">Concept</bdi>، <bdi dir="ltr">Boundary</bdi>، <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Code</bdi>، <bdi dir="ltr">Data</bdi>، <bdi dir="ltr">Test</bdi> یا <bdi dir="ltr">Documentation</bdi>
3. اثر بالقوه
4. اصلاح حداقلی
5. شاهد قبولی پس از اصلاح

## زبان و قالب

- متن آموزشی فارسی است؛ نام الگوها، قراردادها و اجزای کد به انگلیسی استاندارد می‌ماند.
- فایل‌ها <bdi dir="ltr">UTF-8</bdi> و <bdi dir="ltr">LF</bdi> هستند و <bdi dir="ltr">Markdown</bdi>های دارای متن فارسی باید از [استاندارد <bdi dir="ltr">BiDi</bdi> مخزن](docs/course/markdown-bidi-style-guide.md) پیروی کنند.
- نثر فارسی داخل ظرف <bdi dir="ltr">RTL</bdi>، اصطلاحات و <bdi dir="ltr">inline code</bdi> داخل <bdi dir="ltr">`bdi dir="ltr"`</bdi> و <bdi dir="ltr">fenced code block</bdi>ها داخل ظرف <bdi dir="ltr">LTR</bdi> قرار می‌گیرند.
- نویسه‌های نامرئی کنترل جهت مجاز نیستند؛ پیش از <bdi dir="ltr">Commit</bdi>، <bdi dir="ltr">`python3 scripts/markdown_bidi.py --check`</bdi> باید موفق باشد.
- <bdi dir="ltr">Diagram</bdi>ها باید <bdi dir="ltr">Version</bdi>، <bdi dir="ltr">Scope</bdi> و <bdi dir="ltr">Ownership</bdi> را نشان دهند.
- دادهٔ واقعی بانک و کد تولیدی در مخزن قرار نمی‌گیرد.

</div>
