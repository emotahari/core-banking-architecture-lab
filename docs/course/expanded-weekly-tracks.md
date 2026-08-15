# الحاقیهٔ ثابت هفتگی — Code Craft و پروندهٔ Core Banking

- Effective from: Week 02
- Core curriculum: preserved without reduction
- Expanded weekly budget: 510 minutes
- Review rule: Pattern بدون Forces و Test پذیرفته نیست؛ روایت شرکتی بدون Source و تفکیک Fact/Inference نیز پذیرفته نیست.

## 1. قرارداد عدم کاهش

برنامهٔ اصلی معماری و Core Banking حذف، فشرده یا جایگزین نمی‌شود. از Week 02 به بعد هر هفته سه ریل هم‌زمان دارد:

1. **Architecture & Banking Domain Core — 360 minutes:** همان درس‌ها، Artifactها، کد، Failure و Gate قبلی.
2. **Code Craft Lab — 105 minutes:** Clean Code، Refactoring، Design Pattern، Unit Test و Code Review روی مسئلهٔ بانکی همان هفته.
3. **Core Banking Case File — 45 minutes:** داستان یک Core Banking، بانک دیجیتال یا سامانهٔ بانکی واقعی با شواهد عمومی.

اگر در هفته‌ای فقط شش ساعت زمان وجود داشت، ریل اصلی اجرا می‌شود و دو ریل افزوده با وضعیت `Extension Pending` به اولین زمان آزاد منتقل می‌شوند؛ حذف خاموش یا کوچک‌کردن Gate اصلی مجاز نیست. وضعیت `Week Done — Expanded` فقط وقتی ثبت می‌شود که هر سه ریل تمام شده باشند.

## 2. استاندارد Code Craft Lab

هر Lab باید این چرخه را طی کند:

```text
running baseline
  → identify concrete smells
  → add/verify characterization tests
  → refactor in small green steps
  → introduce a pattern only when forces justify it
  → add a negative/edge test
  → inspect diff and write a code-review note
```

### خروجی اجباری

- کد Baseline قابل اجرا و نتیجهٔ تست قبل از تغییر
- Smell Map با محل، نشانه و اثر هر Smell
- Commitهای کوچک یا دست‌کم Diff مرحله‌بندی‌شده
- تست رفتار عادی و حداقل یک Edge Case
- Pattern Decision شامل `Problem / Forces / Options / Decision / Cost`
- نسخهٔ Refactored با نام‌های دامینی و Dependencyهای محدودتر
- Self-review با ذکر یک بهبود و یک Debt باقی‌مانده

### قواعد آموزشی

- Clean Code مساوی «Method کوتاه به هر قیمت» نیست؛ خوانایی، Cohesion، Encapsulation و قابلیت تغییر معیارند.
- `Strategy` جایگزین خودکار هر `switch` نیست. اگر Variation واقعی و مستقل وجود ندارد، Conditional ساده می‌تواند انتخاب تمیزتری باشد.
- `Factory` نباید فقط Constructor را پنهان کند؛ باید Creation decision معناداری را متمرکز کند.
- Pattern نام‌گذاری برای دفاع از Complexity نیست. اگر تعداد Typeها زیاد شد اما Change coupling کم نشد، Refactor شکست خورده است.
- Refactor نباید رفتار را ناخواسته تغییر دهد؛ تغییر Rule دامینی و Refactor دو Commit/تصمیم جدا هستند.
- مثال‌های بانکی این دوره آموزشی‌اند و نرخ‌ها، Limits و Accounting ruleهای آن‌ها تعرفه یا مقررات واقعی بانک محسوب نمی‌شوند.

## 3. استاندارد پروندهٔ هفتگی Core Banking

هر پرونده باید دست‌کم این بخش‌ها را داشته باشد:

1. هویت سامانه/بانک و Scope بررسی
2. مسئله‌ای که باعث تولد آن شد
3. Timeline از تأسیس تا امروز
4. تحول محصول و مدل کسب‌وکار
5. تحول معماری و فناوری
6. معماری و Technology stack فعلی، فقط در حد اطلاعات عمومی قابل اثبات
7. Capability/Domain map تحلیلی با برچسب صریح `Fact` یا `Inference`
8. اشتباه‌ها، رخدادها، Migrationهای دشوار و شرط‌بندی‌های ناموفق
9. دستاوردهای جدید با تاریخ کنترل منبع
10. درس‌های قابل انتقال و غیرقابل انتقال برای Core Banking Lab
11. پنج سؤال دفاعی و یک Artifact کوچک
12. Source register با اولویت گزارش رسمی، رگولاتور، مستند فنی و سخنرانی سازندگان

نباید از صفحهٔ محصول، نام تیم یا نام Microservice به‌تنهایی Bounded Context قطعی استنتاج شود. هر Domain map بیرونی که از اطلاعات عمومی ساخته می‌شود یک **فرضیهٔ تحلیلی** است، نه بازسازی نقشهٔ محرمانهٔ شرکت.

## 4. Definition of Done افزوده

| ریل | شرط قبولی |
|---|---|
| Code Craft | Baseline سبز، تست Characterization، Refactor کوچک، Edge Test، Pattern Decision و Self-review |
| Case File | Timeline مستند، Current-state تاریخ‌دار، حداقل یک شکست واقعی، تفکیک Fact/Inference و انتقال درس به پروژه |
| کل هفته | Gate اصلی قبلی + دو شرط بالا؛ هیچ‌کدام جای دیگری را پر نمی‌کند |

## 5. نقشهٔ افزودهٔ Week 02 تا Week 24

این جدول موضوع را رزرو می‌کند؛ پروندهٔ هر هفته هنگام شروع همان هفته با منابع جاری دوباره اعتبارسنجی می‌شود.

| هفته | Code Craft و Pattern | تمرکز Clean Code/Refactor | پروندهٔ پیشنهادی سامانهٔ بانکی |
|---:|---|---|---|
| 02 | Strategy + Registry/Factory روی Fee Policy | Magic literal، Primitive Obsession، Flag Argument، نام‌گذاری دامینی | Monzo؛ مالکیت، Microservice scale و کنترل‌های بانکی |
| 03 | Strategy، Specification و State روی Deposits | رفتار کنار داده، Tell-Don’t-Ask و Invariant | Thought Machine Vault Core |
| 04 | Ports & Adapters، Repository و Mapper | Dependency Inversion و جداسازی Domain از Framework | Temenos Transact/T24 |
| 05 | Command، Query، DTO و Assembler | Contract surface کوچک و خطای Leakage | Oracle FLEXCUBE |
| 06 | Decorator و Chain of Responsibility برای Policy | Composition، خطای Boolean explosion و تست Security rule | Infosys Finacle |
| 07 | Transaction Script در برابر Domain Model؛ Unit of Work | مرز Transaction و Side effect آشکار | Mambu |
| 08 | CQRS، Projection و Builderهای تست | Readability تست، Immutability و Lag-aware naming | 10x Banking |
| 09 | Domain Event، Observer و Transactional Outbox | Event naming، Temporal coupling و Duplicate logic | Nubank |
| 10 | Idempotent Consumer، Inbox و Retry Policy | Error handling و رفتار صریح در Duplicate | Starling Bank و Engine by Starling |
| 11 | Process Manager/Saga و State Machine | Long method، Temporal coupling و Compensation clarity | مهاجرت TSB/Proteo به‌عنوان پروندهٔ شکست |
| 12 | Circuit Breaker، Bulkhead، Timeout و Fallback | Failure semantics و حذف Catch-all | DBS transformation |
| 13 | Accounting Entry، Composite و immutable journal | نام‌گذاری Debit/Credit و جلوگیری از setter-driven model | Avaloq Core Platform |
| 14 | Posting Rule Strategy و Reconciliation pipeline | Separating policy from orchestration | FIS Modern Banking Platform |
| 15 | Data Mapper، Repository و Optimistic Lock | Persistence ignorance و Exception translation | Santander Gravity |
| 16 | Pipeline، Chunk و Template Method در EOD | Batch observability و restartable step | Commonwealth Bank core modernization |
| 17 | Effective-dated Policy و Specification | Null handling، temporal names و valid-time tests | Fiserv DNA |
| 18 | State + Policy روی Deposit lifecycle | حذف Anemic Model و کنترل transition | TCS BaNCS |
| 19 | Factory + Strategy + Specification روی Lending | Rule composition و پرهیز از God Service | LendingClub banking platform |
| 20 | Adapter، Command و Idempotency روی Payments | Boundary translation و audit-friendly code | Wise payments platform |
| 21 | Plugin/Registry، Facade و Mediator در Micro-frontend | Stable interface و جلوگیری از shared mutable state | ING digital banking platform |
| 22 | Sidecar/Gateway patterns و deployment policy | Configuration as code و operational ownership | Capital One cloud transformation |
| 23 | Strangler Fig، ACL و Branch by Abstraction | Safe migration و حذف Big-bang rewrite | Lloyds Banking Group modernization |
| 24 | Pattern synthesis و architecture-guided refactor | حذف Patternهای بی‌دلیل و دفاع از کد نهایی | جمع‌بندی تطبیقی Temenos، Vault، Mambu و Core داخلی |

## 6. روش ارزیابی Pattern

برای هر Pattern پنج سؤال پاسخ داده می‌شود:

1. چه Variation یا Pressure واقعی وجود دارد؟
2. ساده‌ترین گزینهٔ بدون Pattern چیست؟
3. Pattern کدام Coupling را کم و کدام Complexity را اضافه می‌کند؟
4. با چه Test یا تغییر فرضی، ارزش آن را ثابت می‌کنیم؟
5. چه Revisit Triggerی باعث حذف یا جایگزینی آن می‌شود؟

پاسخ «چون Best Practice است» امتیاز صفر دارد.

## 7. روش ارزیابی Case File

برای هر ادعا یکی از برچسب‌های زیر استفاده می‌شود:

- `FACT — primary`: گزارش رسمی، رگولاتور یا نوشتهٔ سازندگان
- `FACT — secondary`: منبع معتبر مستقل، فقط وقتی منبع اصلی در دسترس نیست
- `INFERENCE`: نتیجه‌گیری تحلیلی از چند Fact
- `UNKNOWN`: اطلاعات عمومی کافی وجود ندارد

کیفیت پرونده با تعداد فناوری‌ها سنجیده نمی‌شود؛ با توانایی اتصال **تصمیم، زمینه، پیامد و شواهد** سنجیده می‌شود.
