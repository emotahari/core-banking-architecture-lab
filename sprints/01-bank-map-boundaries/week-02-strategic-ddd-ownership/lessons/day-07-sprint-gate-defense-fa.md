# Day 07 — Gate اسپرینت اول: دفاع معماری مسدودی قضایی

- Preparation timebox: 20 minutes
- Oral/written review with instructor: maximum 10 minutes, outside the 360-minute self-study budget
- Passing score: 8/10 with no Critical Error
- Rule: lesson and prior artifacts may be used for preparation; model answer does not exist in the repository before submission.

## 1. هدف قابل سنجش Gate

این Gate بررسی نمی‌کند که تعریف‌ها را حفظ کرده‌ای. باید نشان بدهی می‌توانی روی یک سناریوی بانکی:

- از Capability شروع کنی؛
- Domain/Subdomain و Bounded Context را جدا کنی؛
- Ubiquitous Language را دقیق کنی؛
- Data/Decision Authority را تعیین کنی؛
- رابطهٔ Contextها را با Pattern و Contract نشان بدهی؛
- فرضیه را به Module Boundary قابل Verification وصل کنی؛
- Failureهای اولیه را بدون پریدن به Technology تشخیص بدهی.

## 2. سناریوی Gate

بانک یک دستور قضایی معتبر دریافت می‌کند که بر اساس آن باید مبلغ مشخصی از سپردهٔ مشتری مسدود شود. ممکن است:

- دستور تکراری دریافت شود؛
- دستور بعداً اصلاح یا لغو شود؛
- حساب هدف بسته، محدود یا فاقد شرایط لازم باشد؛
- درخواست اعمال Hold موفق شود اما پاسخ به درخواست‌کننده نرسد؛
- چند سپرده یا چند مشتری با مشخصات نزدیک وجود داشته باشند؛
- واحدهای حقوقی، عملیات سپرده و حسابداری برداشت متفاوتی از واژهٔ «مسدودی» داشته باشند.

در این مرحله دربارهٔ REST، Kafka، Saga، Database و ساختار Deployment تصمیم نگرفته‌ایم.

## 3. خروجی مورد انتظار

[Sprint 01 Gate Evidence](../artifacts/sprint-01-gate-evidence-template.md) را کامل کن. خروجی باید این بخش‌ها را داشته باشد:

1. Problem statement به زبان خودت
2. Traceability chain کامل
3. Context-specific language
4. Data and decision ownership
5. Context Map relation و Pattern
6. Command/Query/Event candidates
7. Module boundary and verification evidence
8. Failure expectations
9. Assumptions/Open Questions
10. خلاصهٔ دفاع حداکثر ۲۰۰ کلمه

## 4. ترتیب ۲۰ دقیقه‌ای

### دقیقهٔ 0 تا 3 — مسئله و Capability

- مسئله را بدون نام سامانه بازنویسی کن.
- Capabilityها و Outcome را مشخص کن.
- Scope و Out-of-scope را بنویس.

### دقیقهٔ 3 تا 7 — Domain، Context و Language

- Problem Spaceها و Context candidates را مشخص کن.
- حداقل سه اصطلاح با معنای Contextual بنویس.
- مرز را با Rule/Lifecycle/Authority دفاع کن.

### دقیقهٔ 7 تا 11 — Ownership

- Trigger، Decision و State owner را جدا کن.
- Factها را ریز و Semantic-specific بنویس.
- Reference/Snapshot/Consumer/Not Allowed را مشخص کن.

### دقیقهٔ 11 تا 14 — Context Map

- Upstream و Downstream را تعیین کن.
- Pattern اصلی و یک Alternative را بنویس.
- Contract و محل Translation را ثبت کن.

### دقیقهٔ 14 تا 17 — Contract و Failure

- Command/Query/Result/Event candidateها را نام‌گذاری کن.
- رفتار Duplicate، Lost Response، Revoke و Rejection را در سطح انتظار کسب‌وکار بیان کن.
- Transport انتخاب نکن.

### دقیقهٔ 17 تا 20 — Module و دفاع

- Mapping اولیه به Module را بنویس.
- یک Rule قابل Verification پیشنهاد بده.
- خلاصهٔ ۲۰۰ کلمه‌ای را تکمیل و Critical Errorها را کنترل کن.

## 5. پرسش‌هایی که در دفاع از تو می‌پرسم

برای این پرسش‌ها آماده باش:

1. چرا عنوان Capability تو نام Process یا Application نیست؟
2. چه شواهدی باعث شد دو Context بسازی؟
3. کدام واژه در دو Context معنای متفاوت دارد؟
4. Trigger درخواست با Decision Authority چه تفاوتی دارد؟
5. دقیقاً چه کسی مجاز است Operational Hold را تغییر دهد و چرا؟
6. Context حقوقی چه چیزی را مالک است و چه چیزی را نباید مالک شود؟
7. Upstream/Downstream را بر چه مبنایی تعیین کردی؟
8. چرا Pattern انتخابی بهتر از Conformist یا ACL جایگزین است؟
9. اگر پاسخ گم شود، کدام Fact را از کدام Authority بررسی می‌کنی؟
10. Accounting کدام Fact را مصرف/ثبت می‌کند و کدام State عملیاتی را نباید تصاحب کند؟
11. چرا Module پیشنهادی هنوز Microservice decision نیست؟
12. کدام بخش پاسخ تو Hypothesis است و چگونه اعتبارسنجی می‌شود؟

## 6. معیار ارزیابی و Rubric

| حوزه | امتیاز | شاهد قبولی |
|---|---:|---|
| Capability و Traceability | ۱.۵ | زنجیره بدون شروع از System/Table |
| Domain/Context/Language | ۱.۵ | مرز و معنای واژه‌ها با شواهد |
| Data and Decision Ownership | ۲ | یک Authority برای هر Fact/Decision |
| Context Map Pattern | ۱ | جهت، Pattern، Contract، Translation |
| Command/Query/Event semantics | ۱ | Intent و Fact از هم جدا |
| Module boundary and verification | ۱ | API/Internal و Rule قابل تست |
| Failure behavior | ۱ | Duplicate، lost response، revoke/reject |
| Assumptions and defense quality | ۱ | Hypothesis/Open Question صریح و قابل دفاع |
| **جمع** | **۱۰** |  |

## 7. Critical Errorها

وجود هر مورد Gate را متوقف می‌کند، حتی اگر جمع امتیاز ۸ یا بیشتر باشد:

1. شروع Boundary از نام جدول، Controller، سامانه یا BIAN Service Domain
2. اعلام مالکیت مشترک برای یک Fact با Semantic یکسان
3. مجازکردن Context خارجی به Update مستقیم State/Database داخلی Context دیگر
4. قراردادن Hold یا Available Balance عملیاتی تحت Authority حسابداری
5. یکی‌گرفتن Command با Event
6. Context Map بدون جهت/Pattern/Contract
7. اعلام «هر Context یک Microservice» بدون Forces فیزیکی
8. دسترسی Module به `internal` Module دیگر به‌عنوان Integration

## 8. قواعد پاسخ

- Diagram زیبا بدون جدول Ownership پذیرفته نیست.
- برچسب Pattern بدون دلیل نصف امتیاز هم نمی‌گیرد.
- می‌توانی بخشی را `Open Question` بگذاری، اگر Risk و Validation owner را مشخص کنی.
- لازم نیست Transport یا Schema نهایی طراحی کنی.
- لازم نیست سند حسابداری دقیق بسازی؛ باید نیاز یا عدم‌نیاز آن را با Fact و Owner تحلیل کنی.
- داده و نام واقعی بانک در پاسخ عمومی نگذار.

## 9. تمرین مستقل و آزمون خروج

[Day 07 Exercise — Sprint Gate](../exercises/day-07-sprint-gate.md) همان تمرین مستقل و آزمون خروج این روز است. پاسخ خام را در [Sprint 01 Gate Response](../submissions/sprint-01-gate-response.md) ثبت کن.

## 10. پس از Submission

پاسخ را برای Review بفرست. Review در پنج دسته انجام می‌شود:

1. Concept
2. Boundary
3. Ownership
4. Contract/Failure
5. Code/Verification

اگر Gate پاس نشود، کل هفته تکرار نمی‌شود. فقط ضعیف‌ترین Boundary با سناریوی کوچک‌تر بازطراحی و دوباره دفاع می‌شود.

## 11. منابع اصلی و مجاز برای Preparation

- Artifactهای خودت در Week 01 و Week 02
- [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- [Spring Modulith Verification](https://docs.spring.io/spring-modulith/reference/verification.html)
- [BIAN Service Landscape 14.0](https://bian.org/deliverables/service-landscape/) فقط برای Gap Check

در زمان دفاع، پاسخ باید از مدل خودت بیاید؛ نقل نام Pattern بدون توضیح Forces کافی نیست.
