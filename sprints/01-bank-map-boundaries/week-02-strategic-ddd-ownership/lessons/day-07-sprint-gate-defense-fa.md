<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 07</span> — <span dir="ltr">Gate</span> اسپرینت اول: دفاع معماری مسدودی قضایی

- <span dir="ltr">Preparation timebox: 20 minutes</span>
- <span dir="ltr">Oral/written review with instructor: maximum 10 minutes</span>, <span dir="ltr">outside the 360-minute self-study budget</span>
- <span dir="ltr">Passing score: 8/10 with no Critical Error</span>
- <span dir="ltr">Rule: lesson and prior artifacts may be used for preparation</span>; <span dir="ltr">model answer does not exist in the repository before submission.</span>

## 1. هدف قابل سنجش <span dir="ltr">Gate</span>

این <span dir="ltr">Gate</span> بررسی نمی‌کند که تعریف‌ها را حفظ کرده‌ای. باید نشان بدهی می‌توانی روی یک سناریوی بانکی:

- از <span dir="ltr">Capability</span> شروع کنی؛
- <span dir="ltr">Domain/Subdomain</span> و <span dir="ltr">Bounded Context</span> را جدا کنی؛
- <span dir="ltr">Ubiquitous Language</span> را دقیق کنی؛
- <span dir="ltr">Data/Decision Authority</span> را تعیین کنی؛
- رابطهٔ <span dir="ltr">Context</span>ها را با <span dir="ltr">Pattern</span> و <span dir="ltr">Contract</span> نشان بدهی؛
- فرضیه را به <span dir="ltr">Module Boundary</span> قابل <span dir="ltr">Verification</span> وصل کنی؛
- <span dir="ltr">Failure</span>های اولیه را بدون پریدن به <span dir="ltr">Technology</span> تشخیص بدهی.

## 2. سناریوی <span dir="ltr">Gate</span>

بانک یک دستور قضایی معتبر دریافت می‌کند که بر اساس آن باید مبلغ مشخصی از سپردهٔ مشتری مسدود شود. ممکن است:

- دستور تکراری دریافت شود؛
- دستور بعداً اصلاح یا لغو شود؛
- حساب هدف بسته، محدود یا فاقد شرایط لازم باشد؛
- درخواست اعمال <span dir="ltr">Hold</span> موفق شود اما پاسخ به درخواست‌کننده نرسد؛
- چند سپرده یا چند مشتری با مشخصات نزدیک وجود داشته باشند؛
- واحدهای حقوقی، عملیات سپرده و حسابداری برداشت متفاوتی از واژهٔ «مسدودی» داشته باشند.

در این مرحله دربارهٔ <span dir="ltr">REST</span>، <span dir="ltr">Kafka</span>، <span dir="ltr">Saga</span>، <span dir="ltr">Database</span> و ساختار <span dir="ltr">Deployment</span> تصمیم نگرفته‌ایم.

## 3. خروجی مورد انتظار

[<span dir="ltr">Sprint 01 Gate Evidence</span>](../artifacts/sprint-01-gate-evidence-template.md) را کامل کن. خروجی باید این بخش‌ها را داشته باشد:

1. <span dir="ltr">Problem statement</span> به زبان خودت
2. <span dir="ltr">Traceability chain</span> کامل
3. <span dir="ltr">Context-specific language</span>
4. <span dir="ltr">Data and decision ownership</span>
5. <span dir="ltr">Context Map relation</span> و <span dir="ltr">Pattern</span>
6. <span dir="ltr">Command/Query/Event candidates</span>
7. <span dir="ltr">Module boundary and verification evidence</span>
8. <span dir="ltr">Failure expectations</span>
9. <span dir="ltr">Assumptions/Open Questions</span>
10. خلاصهٔ دفاع حداکثر ۲۰۰ کلمه

## 4. ترتیب ۲۰ دقیقه‌ای

### دقیقهٔ 0 تا 3 — مسئله و <span dir="ltr">Capability</span>

- مسئله را بدون نام سامانه بازنویسی کن.
- <span dir="ltr">Capability</span>ها و <span dir="ltr">Outcome</span> را مشخص کن.
- <span dir="ltr">Scope</span> و <span dir="ltr">Out-of-scope</span> را بنویس.

### دقیقهٔ 3 تا 7 — <span dir="ltr">Domain</span>، <span dir="ltr">Context</span> و <span dir="ltr">Language</span>

- <span dir="ltr">Problem Space</span>ها و <span dir="ltr">Context candidates</span> را مشخص کن.
- حداقل سه اصطلاح با معنای <span dir="ltr">Contextual</span> بنویس.
- مرز را با <span dir="ltr">Rule/Lifecycle/Authority</span> دفاع کن.

### دقیقهٔ 7 تا 11 — <span dir="ltr">Ownership</span>

- <span dir="ltr">Trigger</span>، <span dir="ltr">Decision</span> و <span dir="ltr">State owner</span> را جدا کن.
- <span dir="ltr">Fact</span>ها را ریز و <span dir="ltr">Semantic-specific</span> بنویس.
- <span dir="ltr">Reference/Snapshot/Consumer/Not Allowed</span> را مشخص کن.

### دقیقهٔ 11 تا 14 — <span dir="ltr">Context Map</span>

- <span dir="ltr">Upstream</span> و <span dir="ltr">Downstream</span> را تعیین کن.
- <span dir="ltr">Pattern</span> اصلی و یک <span dir="ltr">Alternative</span> را بنویس.
- <span dir="ltr">Contract</span> و محل <span dir="ltr">Translation</span> را ثبت کن.

### دقیقهٔ 14 تا 17 — <span dir="ltr">Contract</span> و <span dir="ltr">Failure</span>

- <span dir="ltr">Command/Query/Result/Event candidate</span>ها را نام‌گذاری کن.
- رفتار <span dir="ltr">Duplicate</span>، <span dir="ltr">Lost Response</span>، <span dir="ltr">Revoke</span> و <span dir="ltr">Rejection</span> را در سطح انتظار کسب‌وکار بیان کن.
- <span dir="ltr">Transport</span> انتخاب نکن.

### دقیقهٔ 17 تا 20 — <span dir="ltr">Module</span> و دفاع

- <span dir="ltr">Mapping</span> اولیه به <span dir="ltr">Module</span> را بنویس.
- یک <span dir="ltr">Rule</span> قابل <span dir="ltr">Verification</span> پیشنهاد بده.
- خلاصهٔ ۲۰۰ کلمه‌ای را تکمیل و <span dir="ltr">Critical Error</span>ها را کنترل کن.

## 5. پرسش‌هایی که در دفاع از تو می‌پرسم

برای این پرسش‌ها آماده باش:

1. چرا عنوان <span dir="ltr">Capability</span> تو نام <span dir="ltr">Process</span> یا <span dir="ltr">Application</span> نیست؟
2. چه شواهدی باعث شد دو <span dir="ltr">Context</span> بسازی؟
3. کدام واژه در دو <span dir="ltr">Context</span> معنای متفاوت دارد؟
4. <span dir="ltr">Trigger</span> درخواست با <span dir="ltr">Decision Authority</span> چه تفاوتی دارد؟
5. دقیقاً چه کسی مجاز است <span dir="ltr">Operational Hold</span> را تغییر دهد و چرا؟
6. <span dir="ltr">Context</span> حقوقی چه چیزی را مالک است و چه چیزی را نباید مالک شود؟
7. <span dir="ltr">Upstream/Downstream</span> را بر چه مبنایی تعیین کردی؟
8. چرا <span dir="ltr">Pattern</span> انتخابی بهتر از <span dir="ltr">Conformist</span> یا <span dir="ltr">ACL</span> جایگزین است؟
9. اگر پاسخ گم شود، کدام <span dir="ltr">Fact</span> را از کدام <span dir="ltr">Authority</span> بررسی می‌کنی؟
10. <span dir="ltr">Accounting</span> کدام <span dir="ltr">Fact</span> را مصرف/ثبت می‌کند و کدام <span dir="ltr">State</span> عملیاتی را نباید تصاحب کند؟
11. چرا <span dir="ltr">Module</span> پیشنهادی هنوز <span dir="ltr">Microservice decision</span> نیست؟
12. کدام بخش پاسخ تو <span dir="ltr">Hypothesis</span> است و چگونه اعتبارسنجی می‌شود؟

## 6. معیار ارزیابی و <span dir="ltr">Rubric</span>

| حوزه | امتیاز | شاهد قبولی |
|---|---:|---|
| <span dir="ltr">Capability</span> و <span dir="ltr">Traceability</span> | ۱.۵ | زنجیره بدون شروع از <span dir="ltr">System/Table</span> |
| <span dir="ltr">Domain/Context/Language</span> | ۱.۵ | مرز و معنای واژه‌ها با شواهد |
| <span dir="ltr">Data and Decision Ownership</span> | ۲ | یک <span dir="ltr">Authority</span> برای هر <span dir="ltr">Fact/Decision</span> |
| <span dir="ltr">Context Map Pattern</span> | ۱ | جهت، <span dir="ltr">Pattern</span>، <span dir="ltr">Contract</span>، <span dir="ltr">Translation</span> |
| <span dir="ltr">Command/Query/Event semantics</span> | ۱ | <span dir="ltr">Intent</span> و <span dir="ltr">Fact</span> از هم جدا |
| <span dir="ltr">Module boundary and verification</span> | ۱ | <span dir="ltr">API/Internal</span> و <span dir="ltr">Rule</span> قابل تست |
| <span dir="ltr">Failure behavior</span> | ۱ | <span dir="ltr">Duplicate</span>، <span dir="ltr">lost response</span>، <span dir="ltr">revoke/reject</span> |
| <span dir="ltr">Assumptions and defense quality</span> | ۱ | <span dir="ltr">Hypothesis/Open Question</span> صریح و قابل دفاع |
| **جمع** | **۱۰** |  |

## <span dir="ltr">7. Critical Error</span>ها

وجود هر مورد <span dir="ltr">Gate</span> را متوقف می‌کند، حتی اگر جمع امتیاز ۸ یا بیشتر باشد:

1. شروع <span dir="ltr">Boundary</span> از نام جدول، <span dir="ltr">Controller</span>، سامانه یا <span dir="ltr">BIAN Service Domain</span>
2. اعلام مالکیت مشترک برای یک <span dir="ltr">Fact</span> با <span dir="ltr">Semantic</span> یکسان
3. مجازکردن <span dir="ltr">Context</span> خارجی به <span dir="ltr">Update</span> مستقیم <span dir="ltr">State/Database</span> داخلی <span dir="ltr">Context</span> دیگر
4. قراردادن <span dir="ltr">Hold</span> یا <span dir="ltr">Available Balance</span> عملیاتی تحت <span dir="ltr">Authority</span> حسابداری
5. یکی‌گرفتن <span dir="ltr">Command</span> با <span dir="ltr">Event</span>
6. <span dir="ltr">Context Map</span> بدون جهت/<span dir="ltr">Pattern/Contract</span>
7. اعلام «هر <span dir="ltr">Context</span> یک <span dir="ltr">Microservice</span>» بدون <span dir="ltr">Forces</span> فیزیکی
8. دسترسی <span dir="ltr">Module</span> به <span dir="ltr">`internal`</span> <span dir="ltr">Module</span> دیگر به‌عنوان <span dir="ltr">Integration</span>

## 8. قواعد پاسخ

- <span dir="ltr">Diagram</span> زیبا بدون جدول <span dir="ltr">Ownership</span> پذیرفته نیست.
- برچسب <span dir="ltr">Pattern</span> بدون دلیل نصف امتیاز هم نمی‌گیرد.
- می‌توانی بخشی را <span dir="ltr">`Open Question`</span> بگذاری، اگر <span dir="ltr">Risk</span> و <span dir="ltr">Validation owner</span> را مشخص کنی.
- لازم نیست <span dir="ltr">Transport</span> یا <span dir="ltr">Schema</span> نهایی طراحی کنی.
- لازم نیست سند حسابداری دقیق بسازی؛ باید نیاز یا عدم‌نیاز آن را با <span dir="ltr">Fact</span> و <span dir="ltr">Owner</span> تحلیل کنی.
- داده و نام واقعی بانک در پاسخ عمومی نگذار.

## 9. تمرین مستقل و آزمون خروج

[<span dir="ltr">Day 07 Exercise</span> — <span dir="ltr">Sprint Gate</span>](../exercises/day-07-sprint-gate.md) همان تمرین مستقل و آزمون خروج این روز است. پاسخ خام را در [<span dir="ltr">Sprint 01 Gate Response</span>](../submissions/sprint-01-gate-response.md) ثبت کن.

## 10. پس از <span dir="ltr">Submission</span>

پاسخ را برای <span dir="ltr">Review</span> بفرست. <span dir="ltr">Review</span> در پنج دسته انجام می‌شود:

1. <span dir="ltr">Concept</span>
2. <span dir="ltr">Boundary</span>
3. <span dir="ltr">Ownership</span>
4. <span dir="ltr">Contract/Failure</span>
5. <span dir="ltr">Code/Verification</span>

اگر <span dir="ltr">Gate</span> پاس نشود، کل هفته تکرار نمی‌شود. فقط ضعیف‌ترین <span dir="ltr">Boundary</span> با سناریوی کوچک‌تر بازطراحی و دوباره دفاع می‌شود.

## 11. منابع اصلی و مجاز برای <span dir="ltr">Preparation</span>

- <span dir="ltr">Artifact</span>های خودت در <span dir="ltr">Week 01</span> و <span dir="ltr">Week 02</span>
- [<span dir="ltr">DDD Reference</span>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- [<span dir="ltr">Spring Modulith Verification</span>](https://docs.spring.io/spring-modulith/reference/verification.html)
- [<span dir="ltr">BIAN Service Landscape 14.0</span>](https://bian.org/deliverables/service-landscape/) فقط برای <span dir="ltr">Gap Check</span>

در زمان دفاع، پاسخ باید از مدل خودت بیاید؛ نقل نام <span dir="ltr">Pattern</span> بدون توضیح <span dir="ltr">Forces</span> کافی نیست.

</div>
