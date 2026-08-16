<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# الحاقیهٔ ثابت هفتگی — <span dir="ltr">Code Craft</span> و پروندهٔ <span dir="ltr">Core Banking</span>

- <span dir="ltr">Effective from: Week 01</span>
- <span dir="ltr">Core curriculum: preserved without reduction</span>
- <span dir="ltr">Expanded weekly budget: 510 minutes</span>
- <span dir="ltr">Review rule: Pattern</span> بدون <span dir="ltr">Forces</span> و <span dir="ltr">Test</span> پذیرفته نیست؛ روایت شرکتی بدون <span dir="ltr">Source</span> و تفکیک <span dir="ltr">Fact/Inference</span> نیز پذیرفته نیست.

## 1. قرارداد عدم کاهش

برنامهٔ اصلی معماری و <span dir="ltr">Core Banking</span> حذف، فشرده یا جایگزین نمی‌شود. از <span dir="ltr">Week 01</span> به بعد هر هفته سه ریل هم‌زمان دارد:

1. **<span dir="ltr">Architecture</span> & <span dir="ltr">Banking Domain Core</span> — <span dir="ltr">360 minutes:</span>** همان درس‌ها، <span dir="ltr">Artifact</span>ها، کد، <span dir="ltr">Failure</span> و <span dir="ltr">Gate</span> قبلی.
2. **<span dir="ltr">Code Craft Lab</span> — <span dir="ltr">105 minutes:</span>** <span dir="ltr">Clean Code</span>، <span dir="ltr">Refactoring</span>، <span dir="ltr">Design Pattern</span>، <span dir="ltr">Unit Test</span> و <span dir="ltr">Code Review</span> روی مسئلهٔ بانکی همان هفته.
3. **<span dir="ltr">Core Banking Case File</span> — <span dir="ltr">45 minutes:</span>** داستان یک <span dir="ltr">Core Banking</span>، بانک دیجیتال یا سامانهٔ بانکی واقعی با شواهد عمومی.

اگر در هفته‌ای فقط شش ساعت زمان وجود داشت، ریل اصلی اجرا می‌شود و دو ریل افزوده با وضعیت <span dir="ltr">`Extension Pending`</span> به اولین زمان آزاد منتقل می‌شوند؛ حذف خاموش یا کوچک‌کردن <span dir="ltr">Gate</span> اصلی مجاز نیست. وضعیت <span dir="ltr">`Week Done — Expanded`</span> فقط وقتی ثبت می‌شود که هر سه ریل تمام شده باشند.

## 2. استاندارد <span dir="ltr">Code Craft Lab</span>

هر <span dir="ltr">Lab</span> باید این چرخه را طی کند:


</div>

<div dir="ltr" align="left">

```text
running baseline
  → identify concrete smells
  → add/verify characterization tests
  → refactor in small green steps
  → introduce a pattern only when forces justify it
  → add a negative/edge test
  → inspect diff and write a code-review note
```

</div>

<div dir="rtl" align="right">


### خروجی اجباری

- کد <span dir="ltr">Baseline</span> قابل اجرا و نتیجهٔ تست قبل از تغییر
- <span dir="ltr">Smell Map</span> با محل، نشانه و اثر هر <span dir="ltr">Smell</span>
- <span dir="ltr">Commit</span>های کوچک یا دست‌کم <span dir="ltr">Diff</span> مرحله‌بندی‌شده
- تست رفتار عادی و حداقل یک <span dir="ltr">Edge Case</span>
- <span dir="ltr">Pattern Decision</span> شامل <span dir="ltr">`Problem / Forces / Options / Decision / Cost`</span>
- نسخهٔ <span dir="ltr">Refactored</span> با نام‌های دامینی و <span dir="ltr">Dependency</span>های محدودتر
- <span dir="ltr">Self-review</span> با ذکر یک بهبود و یک <span dir="ltr">Debt</span> باقی‌مانده

### قواعد آموزشی

- <span dir="ltr">Clean Code</span> مساوی «<span dir="ltr">Method</span> کوتاه به هر قیمت» نیست؛ خوانایی، <span dir="ltr">Cohesion</span>، <span dir="ltr">Encapsulation</span> و قابلیت تغییر معیارند.
- <span dir="ltr">`Strategy`</span> جایگزین خودکار هر <span dir="ltr">`switch`</span> نیست. اگر <span dir="ltr">Variation</span> واقعی و مستقل وجود ندارد، <span dir="ltr">Conditional</span> ساده می‌تواند انتخاب تمیزتری باشد.
- <span dir="ltr">`Factory`</span> نباید فقط <span dir="ltr">Constructor</span> را پنهان کند؛ باید <span dir="ltr">Creation decision</span> معناداری را متمرکز کند.
- <span dir="ltr">Pattern</span> نام‌گذاری برای دفاع از <span dir="ltr">Complexity</span> نیست. اگر تعداد <span dir="ltr">Type</span>ها زیاد شد اما <span dir="ltr">Change coupling</span> کم نشد، <span dir="ltr">Refactor</span> شکست خورده است.
- <span dir="ltr">Refactor</span> نباید رفتار را ناخواسته تغییر دهد؛ تغییر <span dir="ltr">Rule</span> دامینی و <span dir="ltr">Refactor</span> دو <span dir="ltr">Commit/</span>تصمیم جدا هستند.
- مثال‌های بانکی این دوره آموزشی‌اند و نرخ‌ها، <span dir="ltr">Limits</span> و <span dir="ltr">Accounting rule</span>های آن‌ها تعرفه یا مقررات واقعی بانک محسوب نمی‌شوند.

## 3. استاندارد پروندهٔ هفتگی <span dir="ltr">Core Banking</span>

هر پرونده باید دست‌کم این بخش‌ها را داشته باشد:

1. هویت سامانه/بانک و <span dir="ltr">Scope</span> بررسی
2. مسئله‌ای که باعث تولد آن شد
3. <span dir="ltr">Timeline</span> از تأسیس تا امروز
4. تحول محصول و مدل کسب‌وکار
5. تحول معماری و فناوری
6. معماری و <span dir="ltr">Technology stack</span> فعلی، فقط در حد اطلاعات عمومی قابل اثبات
7. <span dir="ltr">Capability/Domain map</span> تحلیلی با برچسب صریح <span dir="ltr">`Fact`</span> یا <span dir="ltr">`Inference`</span>
8. اشتباه‌ها، رخدادها، <span dir="ltr">Migration</span>های دشوار و شرط‌بندی‌های ناموفق
9. دستاوردهای جدید با تاریخ کنترل منبع
10. درس‌های قابل انتقال و غیرقابل انتقال برای <span dir="ltr">Core Banking Lab</span>
11. پنج سؤال دفاعی و یک <span dir="ltr">Artifact</span> کوچک
12. <span dir="ltr">Source register</span> با اولویت گزارش رسمی، رگولاتور، مستند فنی و سخنرانی سازندگان

نباید از صفحهٔ محصول، نام تیم یا نام <span dir="ltr">Microservice</span> به‌تنهایی <span dir="ltr">Bounded Context</span> قطعی استنتاج شود. هر <span dir="ltr">Domain map</span> بیرونی که از اطلاعات عمومی ساخته می‌شود یک **فرضیهٔ تحلیلی** است، نه بازسازی نقشهٔ محرمانهٔ شرکت.

## <span dir="ltr">4. Definition of Done</span> افزوده

| ریل | شرط قبولی |
|---|---|
| <span dir="ltr">Code Craft</span> | <span dir="ltr">Baseline</span> سبز، تست <span dir="ltr">Characterization</span>، <span dir="ltr">Refactor</span> کوچک، <span dir="ltr">Edge Test</span>، <span dir="ltr">Pattern Decision</span> و <span dir="ltr">Self-review</span> |
| <span dir="ltr">Case File</span> | <span dir="ltr">Timeline</span> مستند، <span dir="ltr">Current-state</span> تاریخ‌دار، حداقل یک شکست واقعی، تفکیک <span dir="ltr">Fact/Inference</span> و انتقال درس به پروژه |
| کل هفته | <span dir="ltr">Gate</span> اصلی قبلی + دو شرط بالا؛ هیچ‌کدام جای دیگری را پر نمی‌کند |

## 5. نقشهٔ افزودهٔ <span dir="ltr">Week 01</span> تا <span dir="ltr">Week 24</span>

این جدول موضوع را رزرو می‌کند؛ پروندهٔ هر هفته هنگام شروع همان هفته با منابع جاری دوباره اعتبارسنجی می‌شود.

| هفته | <span dir="ltr">Code Craft</span> و <span dir="ltr">Pattern</span> | تمرکز <span dir="ltr">Clean Code/Refactor</span> | پروندهٔ پیشنهادی سامانهٔ بانکی |
|---:|---|---|---|
| 01 | <span dir="ltr">Value Object</span> + <span dir="ltr">Static Factory</span> روی <span dir="ltr">Money</span> و <span dir="ltr">Typed IDs</span> | <span dir="ltr">Primitive Obsession</span>، <span dir="ltr">Data Clump</span>، <span dir="ltr">Long Parameter List</span> و <span dir="ltr">Validation</span> پراکنده | <span dir="ltr">UPI</span> هند؛ <span dir="ltr">Capability</span>، نقش‌ها، <span dir="ltr">API network</span> و <span dir="ltr">Failure amplification</span> |
| 02 | <span dir="ltr">Strategy</span> + <span dir="ltr">Registry/Factory</span> روی <span dir="ltr">Fee Policy</span> | <span dir="ltr">Magic literal</span>، <span dir="ltr">Primitive Obsession</span>، <span dir="ltr">Flag Argument</span>، نام‌گذاری دامینی | <span dir="ltr">Monzo</span>؛ مالکیت، <span dir="ltr">Microservice scale</span> و کنترل‌های بانکی |
| 03 | <span dir="ltr">Strategy</span>، <span dir="ltr">Specification</span> و <span dir="ltr">State</span> روی <span dir="ltr">Deposits</span> | رفتار کنار داده، <span dir="ltr">Tell-Don</span>’<span dir="ltr">t-Ask</span> و <span dir="ltr">Invariant</span> | <span dir="ltr">Thought Machine Vault Core</span> |
| 04 | <span dir="ltr">Ports</span> & <span dir="ltr">Adapters</span>، <span dir="ltr">Repository</span> و <span dir="ltr">Mapper</span> | <span dir="ltr">Dependency Inversion</span> و جداسازی <span dir="ltr">Domain</span> از <span dir="ltr">Framework</span> | <span dir="ltr">Temenos Transact/T24</span> |
| 05 | <span dir="ltr">Command</span>، <span dir="ltr">Query</span>، <span dir="ltr">DTO</span> و <span dir="ltr">Assembler</span> | <span dir="ltr">Contract surface</span> کوچک و خطای <span dir="ltr">Leakage</span> | <span dir="ltr">Oracle FLEXCUBE</span> |
| 06 | <span dir="ltr">Decorator</span> و <span dir="ltr">Chain of Responsibility</span> برای <span dir="ltr">Policy</span> | <span dir="ltr">Composition</span>، خطای <span dir="ltr">Boolean explosion</span> و تست <span dir="ltr">Security rule</span> | <span dir="ltr">Infosys Finacle</span> |
| 07 | <span dir="ltr">Transaction Script</span> در برابر <span dir="ltr">Domain Model</span>؛ <span dir="ltr">Unit of Work</span> | مرز <span dir="ltr">Transaction</span> و <span dir="ltr">Side effect</span> آشکار | <span dir="ltr">Mambu</span> |
| 08 | <span dir="ltr">CQRS</span>، <span dir="ltr">Projection</span> و <span dir="ltr">Builder</span>های تست | <span dir="ltr">Readability</span> تست، <span dir="ltr">Immutability</span> و <span dir="ltr">Lag-aware naming</span> | <span dir="ltr">10x Banking</span> |
| 09 | <span dir="ltr">Domain Event</span>، <span dir="ltr">Observer</span> و <span dir="ltr">Transactional Outbox</span> | <span dir="ltr">Event naming</span>، <span dir="ltr">Temporal coupling</span> و <span dir="ltr">Duplicate logic</span> | <span dir="ltr">Nubank</span> |
| 10 | <span dir="ltr">Idempotent Consumer</span>، <span dir="ltr">Inbox</span> و <span dir="ltr">Retry Policy</span> | <span dir="ltr">Error handling</span> و رفتار صریح در <span dir="ltr">Duplicate</span> | <span dir="ltr">Starling Bank</span> و <span dir="ltr">Engine by Starling</span> |
| 11 | <span dir="ltr">Process Manager/Saga</span> و <span dir="ltr">State Machine</span> | <span dir="ltr">Long method</span>، <span dir="ltr">Temporal coupling</span> و <span dir="ltr">Compensation clarity</span> | مهاجرت <span dir="ltr">TSB/Proteo</span> به‌عنوان پروندهٔ شکست |
| 12 | <span dir="ltr">Circuit Breaker</span>، <span dir="ltr">Bulkhead</span>، <span dir="ltr">Timeout</span> و <span dir="ltr">Fallback</span> | <span dir="ltr">Failure semantics</span> و حذف <span dir="ltr">Catch-all</span> | <span dir="ltr">DBS transformation</span> |
| 13 | <span dir="ltr">Accounting Entry</span>، <span dir="ltr">Composite</span> و <span dir="ltr">immutable journal</span> | نام‌گذاری <span dir="ltr">Debit/Credit</span> و جلوگیری از <span dir="ltr">setter-driven model</span> | <span dir="ltr">Avaloq Core Platform</span> |
| 14 | <span dir="ltr">Posting Rule Strategy</span> و <span dir="ltr">Reconciliation pipeline</span> | <span dir="ltr">Separating policy from orchestration</span> | <span dir="ltr">FIS Modern Banking Platform</span> |
| 15 | <span dir="ltr">Data Mapper</span>، <span dir="ltr">Repository</span> و <span dir="ltr">Optimistic Lock</span> | <span dir="ltr">Persistence ignorance</span> و <span dir="ltr">Exception translation</span> | <span dir="ltr">Santander Gravity</span> |
| 16 | <span dir="ltr">Pipeline</span>، <span dir="ltr">Chunk</span> و <span dir="ltr">Template Method</span> در <span dir="ltr">EOD</span> | <span dir="ltr">Batch observability</span> و <span dir="ltr">restartable step</span> | <span dir="ltr">Commonwealth Bank core modernization</span> |
| 17 | <span dir="ltr">Effective-dated Policy</span> و <span dir="ltr">Specification</span> | <span dir="ltr">Null handling</span>، <span dir="ltr">temporal names</span> و <span dir="ltr">valid-time tests</span> | <span dir="ltr">Fiserv DNA</span> |
| 18 | <span dir="ltr">State</span> + <span dir="ltr">Policy</span> روی <span dir="ltr">Deposit lifecycle</span> | حذف <span dir="ltr">Anemic Model</span> و کنترل <span dir="ltr">transition</span> | <span dir="ltr">TCS BaNCS</span> |
| 19 | <span dir="ltr">Factory</span> + <span dir="ltr">Strategy</span> + <span dir="ltr">Specification</span> روی <span dir="ltr">Lending</span> | <span dir="ltr">Rule composition</span> و پرهیز از <span dir="ltr">God Service</span> | <span dir="ltr">LendingClub banking platform</span> |
| 20 | <span dir="ltr">Adapter</span>، <span dir="ltr">Command</span> و <span dir="ltr">Idempotency</span> روی <span dir="ltr">Payments</span> | <span dir="ltr">Boundary translation</span> و <span dir="ltr">audit-friendly code</span> | <span dir="ltr">Wise payments platform</span> |
| 21 | <span dir="ltr">Plugin/Registry</span>، <span dir="ltr">Facade</span> و <span dir="ltr">Mediator</span> در <span dir="ltr">Micro-frontend</span> | <span dir="ltr">Stable interface</span> و جلوگیری از <span dir="ltr">shared mutable state</span> | <span dir="ltr">ING digital banking platform</span> |
| 22 | <span dir="ltr">Sidecar/Gateway patterns</span> و <span dir="ltr">deployment policy</span> | <span dir="ltr">Configuration as code</span> و <span dir="ltr">operational ownership</span> | <span dir="ltr">Capital One cloud transformation</span> |
| 23 | <span dir="ltr">Strangler Fig</span>، <span dir="ltr">ACL</span> و <span dir="ltr">Branch by Abstraction</span> | <span dir="ltr">Safe migration</span> و حذف <span dir="ltr">Big-bang rewrite</span> | <span dir="ltr">Lloyds Banking Group modernization</span> |
| 24 | <span dir="ltr">Pattern synthesis</span> و <span dir="ltr">architecture-guided refactor</span> | حذف <span dir="ltr">Pattern</span>های بی‌دلیل و دفاع از کد نهایی | جمع‌بندی تطبیقی <span dir="ltr">Temenos</span>، <span dir="ltr">Vault</span>، <span dir="ltr">Mambu</span> و <span dir="ltr">Core</span> داخلی |

## 6. روش ارزیابی <span dir="ltr">Pattern</span>

برای هر <span dir="ltr">Pattern</span> پنج سؤال پاسخ داده می‌شود:

1. چه <span dir="ltr">Variation</span> یا <span dir="ltr">Pressure</span> واقعی وجود دارد؟
2. ساده‌ترین گزینهٔ بدون <span dir="ltr">Pattern</span> چیست؟
3. <span dir="ltr">Pattern</span> کدام <span dir="ltr">Coupling</span> را کم و کدام <span dir="ltr">Complexity</span> را اضافه می‌کند؟
4. با چه <span dir="ltr">Test</span> یا تغییر فرضی، ارزش آن را ثابت می‌کنیم؟
5. چه <span dir="ltr">Revisit Trigger</span>ی باعث حذف یا جایگزینی آن می‌شود؟

پاسخ «چون <span dir="ltr">Best Practice</span> است» امتیاز صفر دارد.

## 7. روش ارزیابی <span dir="ltr">Case File</span>

برای هر ادعا یکی از برچسب‌های زیر استفاده می‌شود:

- <span dir="ltr">`FACT — primary`</span>: گزارش رسمی، رگولاتور یا نوشتهٔ سازندگان
- <span dir="ltr">`FACT — secondary`</span>: منبع معتبر مستقل، فقط وقتی منبع اصلی در دسترس نیست
- <span dir="ltr">`INFERENCE`</span>: نتیجه‌گیری تحلیلی از چند <span dir="ltr">Fact</span>
- <span dir="ltr">`UNKNOWN`</span>: اطلاعات عمومی کافی وجود ندارد

کیفیت پرونده با تعداد فناوری‌ها سنجیده نمی‌شود؛ با توانایی اتصال **تصمیم، زمینه، پیامد و شواهد** سنجیده می‌شود.


</div>
