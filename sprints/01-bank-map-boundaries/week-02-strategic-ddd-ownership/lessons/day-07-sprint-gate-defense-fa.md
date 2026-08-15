<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 07</bdi> — <bdi dir="ltr">Gate</bdi> اسپرینت اول: دفاع معماری مسدودی قضایی

- <bdi dir="ltr">Preparation timebox: 20 minutes</bdi>
- <bdi dir="ltr">Oral/written review with instructor: maximum 10 minutes</bdi>, <bdi dir="ltr">outside the 360-minute self-study budget</bdi>
- <bdi dir="ltr">Passing score: 8/10 with no Critical Error</bdi>
- <bdi dir="ltr">Rule: lesson and prior artifacts may be used for preparation</bdi>; <bdi dir="ltr">model answer does not exist in the repository before submission.</bdi>

## 1. هدف قابل سنجش <bdi dir="ltr">Gate</bdi>

این <bdi dir="ltr">Gate</bdi> بررسی نمی‌کند که تعریف‌ها را حفظ کرده‌ای. باید نشان بدهی می‌توانی روی یک سناریوی بانکی:

- از <bdi dir="ltr">Capability</bdi> شروع کنی؛
- <bdi dir="ltr">Domain/Subdomain</bdi> و <bdi dir="ltr">Bounded Context</bdi> را جدا کنی؛
- <bdi dir="ltr">Ubiquitous Language</bdi> را دقیق کنی؛
- <bdi dir="ltr">Data/Decision Authority</bdi> را تعیین کنی؛
- رابطهٔ <bdi dir="ltr">Context</bdi>ها را با <bdi dir="ltr">Pattern</bdi> و <bdi dir="ltr">Contract</bdi> نشان بدهی؛
- فرضیه را به <bdi dir="ltr">Module Boundary</bdi> قابل <bdi dir="ltr">Verification</bdi> وصل کنی؛
- <bdi dir="ltr">Failure</bdi>های اولیه را بدون پریدن به <bdi dir="ltr">Technology</bdi> تشخیص بدهی.

## 2. سناریوی <bdi dir="ltr">Gate</bdi>

بانک یک دستور قضایی معتبر دریافت می‌کند که بر اساس آن باید مبلغ مشخصی از سپردهٔ مشتری مسدود شود. ممکن است:

- دستور تکراری دریافت شود؛
- دستور بعداً اصلاح یا لغو شود؛
- حساب هدف بسته، محدود یا فاقد شرایط لازم باشد؛
- درخواست اعمال <bdi dir="ltr">Hold</bdi> موفق شود اما پاسخ به درخواست‌کننده نرسد؛
- چند سپرده یا چند مشتری با مشخصات نزدیک وجود داشته باشند؛
- واحدهای حقوقی، عملیات سپرده و حسابداری برداشت متفاوتی از واژهٔ «مسدودی» داشته باشند.

در این مرحله دربارهٔ <bdi dir="ltr">REST</bdi>، <bdi dir="ltr">Kafka</bdi>، <bdi dir="ltr">Saga</bdi>، <bdi dir="ltr">Database</bdi> و ساختار <bdi dir="ltr">Deployment</bdi> تصمیم نگرفته‌ایم.

## 3. خروجی مورد انتظار

[<bdi dir="ltr">Sprint 01 Gate Evidence</bdi>](../artifacts/sprint-01-gate-evidence-template.md) را کامل کن. خروجی باید این بخش‌ها را داشته باشد:

1. <bdi dir="ltr">Problem statement</bdi> به زبان خودت
2. <bdi dir="ltr">Traceability chain</bdi> کامل
3. <bdi dir="ltr">Context-specific language</bdi>
4. <bdi dir="ltr">Data and decision ownership</bdi>
5. <bdi dir="ltr">Context Map relation</bdi> و <bdi dir="ltr">Pattern</bdi>
6. <bdi dir="ltr">Command/Query/Event candidates</bdi>
7. <bdi dir="ltr">Module boundary and verification evidence</bdi>
8. <bdi dir="ltr">Failure expectations</bdi>
9. <bdi dir="ltr">Assumptions/Open Questions</bdi>
10. خلاصهٔ دفاع حداکثر ۲۰۰ کلمه

## 4. ترتیب ۲۰ دقیقه‌ای

### دقیقهٔ 0 تا 3 — مسئله و <bdi dir="ltr">Capability</bdi>

- مسئله را بدون نام سامانه بازنویسی کن.
- <bdi dir="ltr">Capability</bdi>ها و <bdi dir="ltr">Outcome</bdi> را مشخص کن.
- <bdi dir="ltr">Scope</bdi> و <bdi dir="ltr">Out-of-scope</bdi> را بنویس.

### دقیقهٔ 3 تا 7 — <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Context</bdi> و <bdi dir="ltr">Language</bdi>

- <bdi dir="ltr">Problem Space</bdi>ها و <bdi dir="ltr">Context candidates</bdi> را مشخص کن.
- حداقل سه اصطلاح با معنای <bdi dir="ltr">Contextual</bdi> بنویس.
- مرز را با <bdi dir="ltr">Rule/Lifecycle/Authority</bdi> دفاع کن.

### دقیقهٔ 7 تا 11 — <bdi dir="ltr">Ownership</bdi>

- <bdi dir="ltr">Trigger</bdi>، <bdi dir="ltr">Decision</bdi> و <bdi dir="ltr">State owner</bdi> را جدا کن.
- <bdi dir="ltr">Fact</bdi>ها را ریز و <bdi dir="ltr">Semantic-specific</bdi> بنویس.
- <bdi dir="ltr">Reference/Snapshot/Consumer/Not Allowed</bdi> را مشخص کن.

### دقیقهٔ 11 تا 14 — <bdi dir="ltr">Context Map</bdi>

- <bdi dir="ltr">Upstream</bdi> و <bdi dir="ltr">Downstream</bdi> را تعیین کن.
- <bdi dir="ltr">Pattern</bdi> اصلی و یک <bdi dir="ltr">Alternative</bdi> را بنویس.
- <bdi dir="ltr">Contract</bdi> و محل <bdi dir="ltr">Translation</bdi> را ثبت کن.

### دقیقهٔ 14 تا 17 — <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Failure</bdi>

- <bdi dir="ltr">Command/Query/Result/Event candidate</bdi>ها را نام‌گذاری کن.
- رفتار <bdi dir="ltr">Duplicate</bdi>، <bdi dir="ltr">Lost Response</bdi>، <bdi dir="ltr">Revoke</bdi> و <bdi dir="ltr">Rejection</bdi> را در سطح انتظار کسب‌وکار بیان کن.
- <bdi dir="ltr">Transport</bdi> انتخاب نکن.

### دقیقهٔ 17 تا 20 — <bdi dir="ltr">Module</bdi> و دفاع

- <bdi dir="ltr">Mapping</bdi> اولیه به <bdi dir="ltr">Module</bdi> را بنویس.
- یک <bdi dir="ltr">Rule</bdi> قابل <bdi dir="ltr">Verification</bdi> پیشنهاد بده.
- خلاصهٔ ۲۰۰ کلمه‌ای را تکمیل و <bdi dir="ltr">Critical Error</bdi>ها را کنترل کن.

## 5. پرسش‌هایی که در دفاع از تو می‌پرسم

برای این پرسش‌ها آماده باش:

1. چرا عنوان <bdi dir="ltr">Capability</bdi> تو نام <bdi dir="ltr">Process</bdi> یا <bdi dir="ltr">Application</bdi> نیست؟
2. چه شواهدی باعث شد دو <bdi dir="ltr">Context</bdi> بسازی؟
3. کدام واژه در دو <bdi dir="ltr">Context</bdi> معنای متفاوت دارد؟
4. <bdi dir="ltr">Trigger</bdi> درخواست با <bdi dir="ltr">Decision Authority</bdi> چه تفاوتی دارد؟
5. دقیقاً چه کسی مجاز است <bdi dir="ltr">Operational Hold</bdi> را تغییر دهد و چرا؟
6. <bdi dir="ltr">Context</bdi> حقوقی چه چیزی را مالک است و چه چیزی را نباید مالک شود؟
7. <bdi dir="ltr">Upstream/Downstream</bdi> را بر چه مبنایی تعیین کردی؟
8. چرا <bdi dir="ltr">Pattern</bdi> انتخابی بهتر از <bdi dir="ltr">Conformist</bdi> یا <bdi dir="ltr">ACL</bdi> جایگزین است؟
9. اگر پاسخ گم شود، کدام <bdi dir="ltr">Fact</bdi> را از کدام <bdi dir="ltr">Authority</bdi> بررسی می‌کنی؟
10. <bdi dir="ltr">Accounting</bdi> کدام <bdi dir="ltr">Fact</bdi> را مصرف/ثبت می‌کند و کدام <bdi dir="ltr">State</bdi> عملیاتی را نباید تصاحب کند؟
11. چرا <bdi dir="ltr">Module</bdi> پیشنهادی هنوز <bdi dir="ltr">Microservice decision</bdi> نیست؟
12. کدام بخش پاسخ تو <bdi dir="ltr">Hypothesis</bdi> است و چگونه اعتبارسنجی می‌شود؟

## 6. معیار ارزیابی و <bdi dir="ltr">Rubric</bdi>

| حوزه | امتیاز | شاهد قبولی |
|---|---:|---|
| <bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Traceability</bdi> | ۱.۵ | زنجیره بدون شروع از <bdi dir="ltr">System/Table</bdi> |
| <bdi dir="ltr">Domain/Context/Language</bdi> | ۱.۵ | مرز و معنای واژه‌ها با شواهد |
| <bdi dir="ltr">Data and Decision Ownership</bdi> | ۲ | یک <bdi dir="ltr">Authority</bdi> برای هر <bdi dir="ltr">Fact/Decision</bdi> |
| <bdi dir="ltr">Context Map Pattern</bdi> | ۱ | جهت، <bdi dir="ltr">Pattern</bdi>، <bdi dir="ltr">Contract</bdi>، <bdi dir="ltr">Translation</bdi> |
| <bdi dir="ltr">Command/Query/Event semantics</bdi> | ۱ | <bdi dir="ltr">Intent</bdi> و <bdi dir="ltr">Fact</bdi> از هم جدا |
| <bdi dir="ltr">Module boundary and verification</bdi> | ۱ | <bdi dir="ltr">API/Internal</bdi> و <bdi dir="ltr">Rule</bdi> قابل تست |
| <bdi dir="ltr">Failure behavior</bdi> | ۱ | <bdi dir="ltr">Duplicate</bdi>، <bdi dir="ltr">lost response</bdi>، <bdi dir="ltr">revoke/reject</bdi> |
| <bdi dir="ltr">Assumptions and defense quality</bdi> | ۱ | <bdi dir="ltr">Hypothesis/Open Question</bdi> صریح و قابل دفاع |
| **جمع** | **۱۰** |  |

## <bdi dir="ltr">7. Critical Error</bdi>ها

وجود هر مورد <bdi dir="ltr">Gate</bdi> را متوقف می‌کند، حتی اگر جمع امتیاز ۸ یا بیشتر باشد:

1. شروع <bdi dir="ltr">Boundary</bdi> از نام جدول، <bdi dir="ltr">Controller</bdi>، سامانه یا <bdi dir="ltr">BIAN Service Domain</bdi>
2. اعلام مالکیت مشترک برای یک <bdi dir="ltr">Fact</bdi> با <bdi dir="ltr">Semantic</bdi> یکسان
3. مجازکردن <bdi dir="ltr">Context</bdi> خارجی به <bdi dir="ltr">Update</bdi> مستقیم <bdi dir="ltr">State/Database</bdi> داخلی <bdi dir="ltr">Context</bdi> دیگر
4. قراردادن <bdi dir="ltr">Hold</bdi> یا <bdi dir="ltr">Available Balance</bdi> عملیاتی تحت <bdi dir="ltr">Authority</bdi> حسابداری
5. یکی‌گرفتن <bdi dir="ltr">Command</bdi> با <bdi dir="ltr">Event</bdi>
6. <bdi dir="ltr">Context Map</bdi> بدون جهت/<bdi dir="ltr">Pattern/Contract</bdi>
7. اعلام «هر <bdi dir="ltr">Context</bdi> یک <bdi dir="ltr">Microservice</bdi>» بدون <bdi dir="ltr">Forces</bdi> فیزیکی
8. دسترسی <bdi dir="ltr">Module</bdi> به <bdi dir="ltr">`internal`</bdi> <bdi dir="ltr">Module</bdi> دیگر به‌عنوان <bdi dir="ltr">Integration</bdi>

## 8. قواعد پاسخ

- <bdi dir="ltr">Diagram</bdi> زیبا بدون جدول <bdi dir="ltr">Ownership</bdi> پذیرفته نیست.
- برچسب <bdi dir="ltr">Pattern</bdi> بدون دلیل نصف امتیاز هم نمی‌گیرد.
- می‌توانی بخشی را <bdi dir="ltr">`Open Question`</bdi> بگذاری، اگر <bdi dir="ltr">Risk</bdi> و <bdi dir="ltr">Validation owner</bdi> را مشخص کنی.
- لازم نیست <bdi dir="ltr">Transport</bdi> یا <bdi dir="ltr">Schema</bdi> نهایی طراحی کنی.
- لازم نیست سند حسابداری دقیق بسازی؛ باید نیاز یا عدم‌نیاز آن را با <bdi dir="ltr">Fact</bdi> و <bdi dir="ltr">Owner</bdi> تحلیل کنی.
- داده و نام واقعی بانک در پاسخ عمومی نگذار.

## 9. تمرین مستقل و آزمون خروج

[<bdi dir="ltr">Day 07 Exercise</bdi> — <bdi dir="ltr">Sprint Gate</bdi>](../exercises/day-07-sprint-gate.md) همان تمرین مستقل و آزمون خروج این روز است. پاسخ خام را در [<bdi dir="ltr">Sprint 01 Gate Response</bdi>](../submissions/sprint-01-gate-response.md) ثبت کن.

## 10. پس از <bdi dir="ltr">Submission</bdi>

پاسخ را برای <bdi dir="ltr">Review</bdi> بفرست. <bdi dir="ltr">Review</bdi> در پنج دسته انجام می‌شود:

1. <bdi dir="ltr">Concept</bdi>
2. <bdi dir="ltr">Boundary</bdi>
3. <bdi dir="ltr">Ownership</bdi>
4. <bdi dir="ltr">Contract/Failure</bdi>
5. <bdi dir="ltr">Code/Verification</bdi>

اگر <bdi dir="ltr">Gate</bdi> پاس نشود، کل هفته تکرار نمی‌شود. فقط ضعیف‌ترین <bdi dir="ltr">Boundary</bdi> با سناریوی کوچک‌تر بازطراحی و دوباره دفاع می‌شود.

## 11. منابع اصلی و مجاز برای <bdi dir="ltr">Preparation</bdi>

- <bdi dir="ltr">Artifact</bdi>های خودت در <bdi dir="ltr">Week 01</bdi> و <bdi dir="ltr">Week 02</bdi>
- [<bdi dir="ltr">DDD Reference</bdi>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- [<bdi dir="ltr">Spring Modulith Verification</bdi>](https://docs.spring.io/spring-modulith/reference/verification.html)
- [<bdi dir="ltr">BIAN Service Landscape 14.0</bdi>](https://bian.org/deliverables/service-landscape/) فقط برای <bdi dir="ltr">Gap Check</bdi>

در زمان دفاع، پاسخ باید از مدل خودت بیاید؛ نقل نام <bdi dir="ltr">Pattern</bdi> بدون توضیح <bdi dir="ltr">Forces</bdi> کافی نیست.

</div>
