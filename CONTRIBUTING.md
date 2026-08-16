<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# روش کار در مخزن

## وضعیت‌ها

<span dir="ltr">Board</span> دوره فقط این وضعیت‌ها را دارد:


</div>

<div dir="ltr" align="left">

~~~text
Backlog → Ready → Doing → Review → Gate → Done
~~~

</div>

<div dir="rtl" align="right">


در هر زمان فقط یک روز در <span dir="ltr">Doing</span> است.

## نام‌گذاری <span dir="ltr">Branch</span> و <span dir="ltr">Commit</span>

- <span dir="ltr">Branch</span> روزانه: <span dir="ltr">learning/s01-w01-d01</span>
- <span dir="ltr">Commit</span> روزانه: <span dir="ltr">S01W01D01: architecture baseline</span>
- پایان هفته: <span dir="ltr">tag</span> با الگوی <span dir="ltr">week-01-done</span>
- پایان <span dir="ltr">Gate: tag</span> با الگوی <span dir="ltr">gate-01-passed</span>

تا زمانی که تمرین روز بازبینی نشده، عبارت <span dir="ltr">done</span> در <span dir="ltr">Commit</span> استفاده نمی‌شود.

## مسیر پاسخ‌ها

پاسخ هر تمرین در پوشهٔ <span dir="ltr">submissions</span> همان هفته نوشته می‌شود. محتوای تولیدشده توسط استاد در <span dir="ltr">lessons</span> و پاسخ دانشجو در <span dir="ltr">submissions</span> می‌ماند تا تغییر مدل ذهنی در طول دوره قابل مشاهده باشد.

## <span dir="ltr">Definition of Done</span> هفتگی

- <span dir="ltr">Artifact</span> یا کد در <span dir="ltr">Git</span> ثبت شده باشد.
- <span dir="ltr">mvn verify</span> موفق باشد.
- قواعد دامینی جدید <span dir="ltr">Unit Test</span> داشته باشند.
- مرزهای جدید با <span dir="ltr">Architecture Test</span> یا <span dir="ltr">Module Verification</span> کنترل شوند.
- تغییر قرارداد در <span dir="ltr">OpenAPI</span> یا <span dir="ltr">AsyncAPI</span> ثبت شود.
- دست‌کم یک <span dir="ltr">Edge Case</span> یا <span dir="ltr">Failure</span> آزموده شود.
- تصمیم غیر بدیهی در <span dir="ltr">ADR</span> ثبت شود.
- گزارش هفته تکمیل شود.
- دفاع ده‌دقیقه‌ای قابل ارائه باشد.
- از <span dir="ltr">Week 02</span>، <span dir="ltr">Code Craft Lab</span> شامل <span dir="ltr">Baseline</span>، <span dir="ltr">Characterization Test</span>، <span dir="ltr">Pattern Decision</span>، <span dir="ltr">Edge Test</span> و <span dir="ltr">Self-review</span> تکمیل شود.
- از <span dir="ltr">Week 02</span>، <span dir="ltr">Core Banking Case File</span> با تفکیک <span dir="ltr">Fact/Inference/Unknown</span> و یک تصمیم قابل انتقال مرور شود.

مورد نامرتبط با عبارت <span dir="ltr">Not Applicable</span> و دلیل ثبت می‌شود؛ خالی نمی‌ماند.

## قواعد <span dir="ltr">Review</span>

<span dir="ltr">Review</span> فقط به «درست/غلط» ختم نمی‌شود. برای هر ایراد باید ثبت شود:

1. محل دقیق ایراد
2. نوع ایراد: <span dir="ltr">Concept</span>، <span dir="ltr">Boundary</span>، <span dir="ltr">Domain</span>، <span dir="ltr">Code</span>، <span dir="ltr">Data</span>، <span dir="ltr">Test</span> یا <span dir="ltr">Documentation</span>
3. اثر بالقوه
4. اصلاح حداقلی
5. شاهد قبولی پس از اصلاح

## زبان و قالب

- متن آموزشی فارسی است؛ نام الگوها، قراردادها و اجزای کد به انگلیسی استاندارد می‌ماند.
- فایل‌ها <span dir="ltr">UTF-8</span> و <span dir="ltr">LF</span> هستند و <span dir="ltr">Markdown</span>های دارای متن فارسی باید از [استاندارد <span dir="ltr">BiDi</span> مخزن](docs/course/markdown-bidi-style-guide.md) پیروی کنند.
- نثر فارسی داخل ظرف <span dir="ltr">RTL</span>، اصطلاحات و <span dir="ltr">inline code</span> داخل <span dir="ltr">`span dir="ltr"`</span> و <span dir="ltr">fenced code block</span>ها داخل ظرف <span dir="ltr">LTR</span> قرار می‌گیرند.
- نویسه‌های نامرئی کنترل جهت مجاز نیستند؛ پیش از <span dir="ltr">Commit</span>، <span dir="ltr">`python3 scripts/markdown_bidi.py --check`</span> باید موفق باشد.
- <span dir="ltr">Diagram</span>ها باید <span dir="ltr">Version</span>، <span dir="ltr">Scope</span> و <span dir="ltr">Ownership</span> را نشان دهند.
- دادهٔ واقعی بانک و کد تولیدی در مخزن قرار نمی‌گیرد.

</div>
