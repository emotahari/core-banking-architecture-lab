<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# الحاقیهٔ ثابت هفتگی — <bdi dir="ltr">Code Craft</bdi> و پروندهٔ <bdi dir="ltr">Core Banking</bdi>

- <bdi dir="ltr">Effective from: Week 01</bdi>
- <bdi dir="ltr">Core curriculum: preserved without reduction</bdi>
- <bdi dir="ltr">Expanded weekly budget: 510 minutes</bdi>
- <bdi dir="ltr">Review rule: Pattern</bdi> بدون <bdi dir="ltr">Forces</bdi> و <bdi dir="ltr">Test</bdi> پذیرفته نیست؛ روایت شرکتی بدون <bdi dir="ltr">Source</bdi> و تفکیک <bdi dir="ltr">Fact/Inference</bdi> نیز پذیرفته نیست.

## 1. قرارداد عدم کاهش

برنامهٔ اصلی معماری و <bdi dir="ltr">Core Banking</bdi> حذف، فشرده یا جایگزین نمی‌شود. از <bdi dir="ltr">Week 01</bdi> به بعد هر هفته سه ریل هم‌زمان دارد:

1. **<bdi dir="ltr">Architecture</bdi> & <bdi dir="ltr">Banking Domain Core</bdi> — <bdi dir="ltr">360 minutes:</bdi>** همان درس‌ها، <bdi dir="ltr">Artifact</bdi>ها، کد، <bdi dir="ltr">Failure</bdi> و <bdi dir="ltr">Gate</bdi> قبلی.
2. **<bdi dir="ltr">Code Craft Lab</bdi> — <bdi dir="ltr">105 minutes:</bdi>** <bdi dir="ltr">Clean Code</bdi>، <bdi dir="ltr">Refactoring</bdi>، <bdi dir="ltr">Design Pattern</bdi>، <bdi dir="ltr">Unit Test</bdi> و <bdi dir="ltr">Code Review</bdi> روی مسئلهٔ بانکی همان هفته.
3. **<bdi dir="ltr">Core Banking Case File</bdi> — <bdi dir="ltr">45 minutes:</bdi>** داستان یک <bdi dir="ltr">Core Banking</bdi>، بانک دیجیتال یا سامانهٔ بانکی واقعی با شواهد عمومی.

اگر در هفته‌ای فقط شش ساعت زمان وجود داشت، ریل اصلی اجرا می‌شود و دو ریل افزوده با وضعیت <bdi dir="ltr">`Extension Pending`</bdi> به اولین زمان آزاد منتقل می‌شوند؛ حذف خاموش یا کوچک‌کردن <bdi dir="ltr">Gate</bdi> اصلی مجاز نیست. وضعیت <bdi dir="ltr">`Week Done — Expanded`</bdi> فقط وقتی ثبت می‌شود که هر سه ریل تمام شده باشند.

## 2. استاندارد <bdi dir="ltr">Code Craft Lab</bdi>

هر <bdi dir="ltr">Lab</bdi> باید این چرخه را طی کند:


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

- کد <bdi dir="ltr">Baseline</bdi> قابل اجرا و نتیجهٔ تست قبل از تغییر
- <bdi dir="ltr">Smell Map</bdi> با محل، نشانه و اثر هر <bdi dir="ltr">Smell</bdi>
- <bdi dir="ltr">Commit</bdi>های کوچک یا دست‌کم <bdi dir="ltr">Diff</bdi> مرحله‌بندی‌شده
- تست رفتار عادی و حداقل یک <bdi dir="ltr">Edge Case</bdi>
- <bdi dir="ltr">Pattern Decision</bdi> شامل <bdi dir="ltr">`Problem / Forces / Options / Decision / Cost`</bdi>
- نسخهٔ <bdi dir="ltr">Refactored</bdi> با نام‌های دامینی و <bdi dir="ltr">Dependency</bdi>های محدودتر
- <bdi dir="ltr">Self-review</bdi> با ذکر یک بهبود و یک <bdi dir="ltr">Debt</bdi> باقی‌مانده

### قواعد آموزشی

- <bdi dir="ltr">Clean Code</bdi> مساوی «<bdi dir="ltr">Method</bdi> کوتاه به هر قیمت» نیست؛ خوانایی، <bdi dir="ltr">Cohesion</bdi>، <bdi dir="ltr">Encapsulation</bdi> و قابلیت تغییر معیارند.
- <bdi dir="ltr">`Strategy`</bdi> جایگزین خودکار هر <bdi dir="ltr">`switch`</bdi> نیست. اگر <bdi dir="ltr">Variation</bdi> واقعی و مستقل وجود ندارد، <bdi dir="ltr">Conditional</bdi> ساده می‌تواند انتخاب تمیزتری باشد.
- <bdi dir="ltr">`Factory`</bdi> نباید فقط <bdi dir="ltr">Constructor</bdi> را پنهان کند؛ باید <bdi dir="ltr">Creation decision</bdi> معناداری را متمرکز کند.
- <bdi dir="ltr">Pattern</bdi> نام‌گذاری برای دفاع از <bdi dir="ltr">Complexity</bdi> نیست. اگر تعداد <bdi dir="ltr">Type</bdi>ها زیاد شد اما <bdi dir="ltr">Change coupling</bdi> کم نشد، <bdi dir="ltr">Refactor</bdi> شکست خورده است.
- <bdi dir="ltr">Refactor</bdi> نباید رفتار را ناخواسته تغییر دهد؛ تغییر <bdi dir="ltr">Rule</bdi> دامینی و <bdi dir="ltr">Refactor</bdi> دو <bdi dir="ltr">Commit/</bdi>تصمیم جدا هستند.
- مثال‌های بانکی این دوره آموزشی‌اند و نرخ‌ها، <bdi dir="ltr">Limits</bdi> و <bdi dir="ltr">Accounting rule</bdi>های آن‌ها تعرفه یا مقررات واقعی بانک محسوب نمی‌شوند.

## 3. استاندارد پروندهٔ هفتگی <bdi dir="ltr">Core Banking</bdi>

هر پرونده باید دست‌کم این بخش‌ها را داشته باشد:

1. هویت سامانه/بانک و <bdi dir="ltr">Scope</bdi> بررسی
2. مسئله‌ای که باعث تولد آن شد
3. <bdi dir="ltr">Timeline</bdi> از تأسیس تا امروز
4. تحول محصول و مدل کسب‌وکار
5. تحول معماری و فناوری
6. معماری و <bdi dir="ltr">Technology stack</bdi> فعلی، فقط در حد اطلاعات عمومی قابل اثبات
7. <bdi dir="ltr">Capability/Domain map</bdi> تحلیلی با برچسب صریح <bdi dir="ltr">`Fact`</bdi> یا <bdi dir="ltr">`Inference`</bdi>
8. اشتباه‌ها، رخدادها، <bdi dir="ltr">Migration</bdi>های دشوار و شرط‌بندی‌های ناموفق
9. دستاوردهای جدید با تاریخ کنترل منبع
10. درس‌های قابل انتقال و غیرقابل انتقال برای <bdi dir="ltr">Core Banking Lab</bdi>
11. پنج سؤال دفاعی و یک <bdi dir="ltr">Artifact</bdi> کوچک
12. <bdi dir="ltr">Source register</bdi> با اولویت گزارش رسمی، رگولاتور، مستند فنی و سخنرانی سازندگان

نباید از صفحهٔ محصول، نام تیم یا نام <bdi dir="ltr">Microservice</bdi> به‌تنهایی <bdi dir="ltr">Bounded Context</bdi> قطعی استنتاج شود. هر <bdi dir="ltr">Domain map</bdi> بیرونی که از اطلاعات عمومی ساخته می‌شود یک **فرضیهٔ تحلیلی** است، نه بازسازی نقشهٔ محرمانهٔ شرکت.

## <bdi dir="ltr">4. Definition of Done</bdi> افزوده

| ریل | شرط قبولی |
|---|---|
| <bdi dir="ltr">Code Craft</bdi> | <bdi dir="ltr">Baseline</bdi> سبز، تست <bdi dir="ltr">Characterization</bdi>، <bdi dir="ltr">Refactor</bdi> کوچک، <bdi dir="ltr">Edge Test</bdi>، <bdi dir="ltr">Pattern Decision</bdi> و <bdi dir="ltr">Self-review</bdi> |
| <bdi dir="ltr">Case File</bdi> | <bdi dir="ltr">Timeline</bdi> مستند، <bdi dir="ltr">Current-state</bdi> تاریخ‌دار، حداقل یک شکست واقعی، تفکیک <bdi dir="ltr">Fact/Inference</bdi> و انتقال درس به پروژه |
| کل هفته | <bdi dir="ltr">Gate</bdi> اصلی قبلی + دو شرط بالا؛ هیچ‌کدام جای دیگری را پر نمی‌کند |

## 5. نقشهٔ افزودهٔ <bdi dir="ltr">Week 01</bdi> تا <bdi dir="ltr">Week 24</bdi>

این جدول موضوع را رزرو می‌کند؛ پروندهٔ هر هفته هنگام شروع همان هفته با منابع جاری دوباره اعتبارسنجی می‌شود.

| هفته | <bdi dir="ltr">Code Craft</bdi> و <bdi dir="ltr">Pattern</bdi> | تمرکز <bdi dir="ltr">Clean Code/Refactor</bdi> | پروندهٔ پیشنهادی سامانهٔ بانکی |
|---:|---|---|---|
| 01 | <bdi dir="ltr">Value Object</bdi> + <bdi dir="ltr">Static Factory</bdi> روی <bdi dir="ltr">Money</bdi> و <bdi dir="ltr">Typed IDs</bdi> | <bdi dir="ltr">Primitive Obsession</bdi>، <bdi dir="ltr">Data Clump</bdi>، <bdi dir="ltr">Long Parameter List</bdi> و <bdi dir="ltr">Validation</bdi> پراکنده | <bdi dir="ltr">UPI</bdi> هند؛ <bdi dir="ltr">Capability</bdi>، نقش‌ها، <bdi dir="ltr">API network</bdi> و <bdi dir="ltr">Failure amplification</bdi> |
| 02 | <bdi dir="ltr">Strategy</bdi> + <bdi dir="ltr">Registry/Factory</bdi> روی <bdi dir="ltr">Fee Policy</bdi> | <bdi dir="ltr">Magic literal</bdi>، <bdi dir="ltr">Primitive Obsession</bdi>، <bdi dir="ltr">Flag Argument</bdi>، نام‌گذاری دامینی | <bdi dir="ltr">Monzo</bdi>؛ مالکیت، <bdi dir="ltr">Microservice scale</bdi> و کنترل‌های بانکی |
| 03 | <bdi dir="ltr">Strategy</bdi>، <bdi dir="ltr">Specification</bdi> و <bdi dir="ltr">State</bdi> روی <bdi dir="ltr">Deposits</bdi> | رفتار کنار داده، <bdi dir="ltr">Tell-Don</bdi>’<bdi dir="ltr">t-Ask</bdi> و <bdi dir="ltr">Invariant</bdi> | <bdi dir="ltr">Thought Machine Vault Core</bdi> |
| 04 | <bdi dir="ltr">Ports</bdi> & <bdi dir="ltr">Adapters</bdi>، <bdi dir="ltr">Repository</bdi> و <bdi dir="ltr">Mapper</bdi> | <bdi dir="ltr">Dependency Inversion</bdi> و جداسازی <bdi dir="ltr">Domain</bdi> از <bdi dir="ltr">Framework</bdi> | <bdi dir="ltr">Temenos Transact/T24</bdi> |
| 05 | <bdi dir="ltr">Command</bdi>، <bdi dir="ltr">Query</bdi>، <bdi dir="ltr">DTO</bdi> و <bdi dir="ltr">Assembler</bdi> | <bdi dir="ltr">Contract surface</bdi> کوچک و خطای <bdi dir="ltr">Leakage</bdi> | <bdi dir="ltr">Oracle FLEXCUBE</bdi> |
| 06 | <bdi dir="ltr">Decorator</bdi> و <bdi dir="ltr">Chain of Responsibility</bdi> برای <bdi dir="ltr">Policy</bdi> | <bdi dir="ltr">Composition</bdi>، خطای <bdi dir="ltr">Boolean explosion</bdi> و تست <bdi dir="ltr">Security rule</bdi> | <bdi dir="ltr">Infosys Finacle</bdi> |
| 07 | <bdi dir="ltr">Transaction Script</bdi> در برابر <bdi dir="ltr">Domain Model</bdi>؛ <bdi dir="ltr">Unit of Work</bdi> | مرز <bdi dir="ltr">Transaction</bdi> و <bdi dir="ltr">Side effect</bdi> آشکار | <bdi dir="ltr">Mambu</bdi> |
| 08 | <bdi dir="ltr">CQRS</bdi>، <bdi dir="ltr">Projection</bdi> و <bdi dir="ltr">Builder</bdi>های تست | <bdi dir="ltr">Readability</bdi> تست، <bdi dir="ltr">Immutability</bdi> و <bdi dir="ltr">Lag-aware naming</bdi> | <bdi dir="ltr">10x Banking</bdi> |
| 09 | <bdi dir="ltr">Domain Event</bdi>، <bdi dir="ltr">Observer</bdi> و <bdi dir="ltr">Transactional Outbox</bdi> | <bdi dir="ltr">Event naming</bdi>، <bdi dir="ltr">Temporal coupling</bdi> و <bdi dir="ltr">Duplicate logic</bdi> | <bdi dir="ltr">Nubank</bdi> |
| 10 | <bdi dir="ltr">Idempotent Consumer</bdi>، <bdi dir="ltr">Inbox</bdi> و <bdi dir="ltr">Retry Policy</bdi> | <bdi dir="ltr">Error handling</bdi> و رفتار صریح در <bdi dir="ltr">Duplicate</bdi> | <bdi dir="ltr">Starling Bank</bdi> و <bdi dir="ltr">Engine by Starling</bdi> |
| 11 | <bdi dir="ltr">Process Manager/Saga</bdi> و <bdi dir="ltr">State Machine</bdi> | <bdi dir="ltr">Long method</bdi>، <bdi dir="ltr">Temporal coupling</bdi> و <bdi dir="ltr">Compensation clarity</bdi> | مهاجرت <bdi dir="ltr">TSB/Proteo</bdi> به‌عنوان پروندهٔ شکست |
| 12 | <bdi dir="ltr">Circuit Breaker</bdi>، <bdi dir="ltr">Bulkhead</bdi>، <bdi dir="ltr">Timeout</bdi> و <bdi dir="ltr">Fallback</bdi> | <bdi dir="ltr">Failure semantics</bdi> و حذف <bdi dir="ltr">Catch-all</bdi> | <bdi dir="ltr">DBS transformation</bdi> |
| 13 | <bdi dir="ltr">Accounting Entry</bdi>، <bdi dir="ltr">Composite</bdi> و <bdi dir="ltr">immutable journal</bdi> | نام‌گذاری <bdi dir="ltr">Debit/Credit</bdi> و جلوگیری از <bdi dir="ltr">setter-driven model</bdi> | <bdi dir="ltr">Avaloq Core Platform</bdi> |
| 14 | <bdi dir="ltr">Posting Rule Strategy</bdi> و <bdi dir="ltr">Reconciliation pipeline</bdi> | <bdi dir="ltr">Separating policy from orchestration</bdi> | <bdi dir="ltr">FIS Modern Banking Platform</bdi> |
| 15 | <bdi dir="ltr">Data Mapper</bdi>، <bdi dir="ltr">Repository</bdi> و <bdi dir="ltr">Optimistic Lock</bdi> | <bdi dir="ltr">Persistence ignorance</bdi> و <bdi dir="ltr">Exception translation</bdi> | <bdi dir="ltr">Santander Gravity</bdi> |
| 16 | <bdi dir="ltr">Pipeline</bdi>، <bdi dir="ltr">Chunk</bdi> و <bdi dir="ltr">Template Method</bdi> در <bdi dir="ltr">EOD</bdi> | <bdi dir="ltr">Batch observability</bdi> و <bdi dir="ltr">restartable step</bdi> | <bdi dir="ltr">Commonwealth Bank core modernization</bdi> |
| 17 | <bdi dir="ltr">Effective-dated Policy</bdi> و <bdi dir="ltr">Specification</bdi> | <bdi dir="ltr">Null handling</bdi>، <bdi dir="ltr">temporal names</bdi> و <bdi dir="ltr">valid-time tests</bdi> | <bdi dir="ltr">Fiserv DNA</bdi> |
| 18 | <bdi dir="ltr">State</bdi> + <bdi dir="ltr">Policy</bdi> روی <bdi dir="ltr">Deposit lifecycle</bdi> | حذف <bdi dir="ltr">Anemic Model</bdi> و کنترل <bdi dir="ltr">transition</bdi> | <bdi dir="ltr">TCS BaNCS</bdi> |
| 19 | <bdi dir="ltr">Factory</bdi> + <bdi dir="ltr">Strategy</bdi> + <bdi dir="ltr">Specification</bdi> روی <bdi dir="ltr">Lending</bdi> | <bdi dir="ltr">Rule composition</bdi> و پرهیز از <bdi dir="ltr">God Service</bdi> | <bdi dir="ltr">LendingClub banking platform</bdi> |
| 20 | <bdi dir="ltr">Adapter</bdi>، <bdi dir="ltr">Command</bdi> و <bdi dir="ltr">Idempotency</bdi> روی <bdi dir="ltr">Payments</bdi> | <bdi dir="ltr">Boundary translation</bdi> و <bdi dir="ltr">audit-friendly code</bdi> | <bdi dir="ltr">Wise payments platform</bdi> |
| 21 | <bdi dir="ltr">Plugin/Registry</bdi>، <bdi dir="ltr">Facade</bdi> و <bdi dir="ltr">Mediator</bdi> در <bdi dir="ltr">Micro-frontend</bdi> | <bdi dir="ltr">Stable interface</bdi> و جلوگیری از <bdi dir="ltr">shared mutable state</bdi> | <bdi dir="ltr">ING digital banking platform</bdi> |
| 22 | <bdi dir="ltr">Sidecar/Gateway patterns</bdi> و <bdi dir="ltr">deployment policy</bdi> | <bdi dir="ltr">Configuration as code</bdi> و <bdi dir="ltr">operational ownership</bdi> | <bdi dir="ltr">Capital One cloud transformation</bdi> |
| 23 | <bdi dir="ltr">Strangler Fig</bdi>، <bdi dir="ltr">ACL</bdi> و <bdi dir="ltr">Branch by Abstraction</bdi> | <bdi dir="ltr">Safe migration</bdi> و حذف <bdi dir="ltr">Big-bang rewrite</bdi> | <bdi dir="ltr">Lloyds Banking Group modernization</bdi> |
| 24 | <bdi dir="ltr">Pattern synthesis</bdi> و <bdi dir="ltr">architecture-guided refactor</bdi> | حذف <bdi dir="ltr">Pattern</bdi>های بی‌دلیل و دفاع از کد نهایی | جمع‌بندی تطبیقی <bdi dir="ltr">Temenos</bdi>، <bdi dir="ltr">Vault</bdi>، <bdi dir="ltr">Mambu</bdi> و <bdi dir="ltr">Core</bdi> داخلی |

## 6. روش ارزیابی <bdi dir="ltr">Pattern</bdi>

برای هر <bdi dir="ltr">Pattern</bdi> پنج سؤال پاسخ داده می‌شود:

1. چه <bdi dir="ltr">Variation</bdi> یا <bdi dir="ltr">Pressure</bdi> واقعی وجود دارد؟
2. ساده‌ترین گزینهٔ بدون <bdi dir="ltr">Pattern</bdi> چیست؟
3. <bdi dir="ltr">Pattern</bdi> کدام <bdi dir="ltr">Coupling</bdi> را کم و کدام <bdi dir="ltr">Complexity</bdi> را اضافه می‌کند؟
4. با چه <bdi dir="ltr">Test</bdi> یا تغییر فرضی، ارزش آن را ثابت می‌کنیم؟
5. چه <bdi dir="ltr">Revisit Trigger</bdi>ی باعث حذف یا جایگزینی آن می‌شود؟

پاسخ «چون <bdi dir="ltr">Best Practice</bdi> است» امتیاز صفر دارد.

## 7. روش ارزیابی <bdi dir="ltr">Case File</bdi>

برای هر ادعا یکی از برچسب‌های زیر استفاده می‌شود:

- <bdi dir="ltr">`FACT — primary`</bdi>: گزارش رسمی، رگولاتور یا نوشتهٔ سازندگان
- <bdi dir="ltr">`FACT — secondary`</bdi>: منبع معتبر مستقل، فقط وقتی منبع اصلی در دسترس نیست
- <bdi dir="ltr">`INFERENCE`</bdi>: نتیجه‌گیری تحلیلی از چند <bdi dir="ltr">Fact</bdi>
- <bdi dir="ltr">`UNKNOWN`</bdi>: اطلاعات عمومی کافی وجود ندارد

کیفیت پرونده با تعداد فناوری‌ها سنجیده نمی‌شود؛ با توانایی اتصال **تصمیم، زمینه، پیامد و شواهد** سنجیده می‌شود.


</div>
