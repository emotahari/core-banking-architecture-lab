# روش کار در مخزن

## وضعیت‌ها

Board دوره فقط این وضعیت‌ها را دارد:

~~~text
Backlog → Ready → Doing → Review → Gate → Done
~~~

در هر زمان فقط یک روز در Doing است.

## نام‌گذاری Branch و Commit

- Branch روزانه: learning/s01-w01-d01
- Commit روزانه: S01W01D01: architecture baseline
- پایان هفته: tag با الگوی week-01-done
- پایان Gate: tag با الگوی gate-01-passed

تا زمانی که تمرین روز بازبینی نشده، عبارت done در Commit استفاده نمی‌شود.

## مسیر پاسخ‌ها

پاسخ هر تمرین در پوشهٔ submissions همان هفته نوشته می‌شود. محتوای تولیدشده توسط استاد در lessons و پاسخ دانشجو در submissions می‌ماند تا تغییر مدل ذهنی در طول دوره قابل مشاهده باشد.

## Definition of Done هفتگی

- Artifact یا کد در Git ثبت شده باشد.
- mvn verify موفق باشد.
- قواعد دامینی جدید Unit Test داشته باشند.
- مرزهای جدید با Architecture Test یا Module Verification کنترل شوند.
- تغییر قرارداد در OpenAPI یا AsyncAPI ثبت شود.
- دست‌کم یک Edge Case یا Failure آزموده شود.
- تصمیم غیر بدیهی در ADR ثبت شود.
- گزارش هفته تکمیل شود.
- دفاع ده‌دقیقه‌ای قابل ارائه باشد.
- از Week 02، Code Craft Lab شامل Baseline، Characterization Test، Pattern Decision، Edge Test و Self-review تکمیل شود.
- از Week 02، Core Banking Case File با تفکیک Fact/Inference/Unknown و یک تصمیم قابل انتقال مرور شود.

مورد نامرتبط با عبارت Not Applicable و دلیل ثبت می‌شود؛ خالی نمی‌ماند.

## قواعد Review

Review فقط به «درست/غلط» ختم نمی‌شود. برای هر ایراد باید ثبت شود:

1. محل دقیق ایراد
2. نوع ایراد: Concept، Boundary، Domain، Code، Data، Test یا Documentation
3. اثر بالقوه
4. اصلاح حداقلی
5. شاهد قبولی پس از اصلاح

## زبان و قالب

- متن آموزشی فارسی است؛ نام الگوها، قراردادها و اجزای کد به انگلیسی استاندارد می‌ماند.
- فایل‌ها UTF-8 و جهت متن Markdown طبیعی است.
- Diagramها باید Version، Scope و Ownership را نشان دهند.
- دادهٔ واقعی بانک و کد تولیدی در مخزن قرار نمی‌گیرد.
