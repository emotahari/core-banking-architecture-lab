<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 03</span> — <span dir="ltr">Context Map</span> و الگوهای رابطه

- <span dir="ltr">Day budget: 50 minutes including exercise and exit ticket</span>
- <span dir="ltr">Output: Context Map relationships v0.1</span>
- <span dir="ltr">Banking case:</span> اعطای تسهیلات و واریز به سپرده

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Context Map</span> را از <span dir="ltr">System Diagram</span>، <span dir="ltr">Sequence Diagram</span> و <span dir="ltr">Data Flow</span> جدا کنی.
2. <span dir="ltr">Upstream</span> و <span dir="ltr">Downstream</span> را بر اساس وابستگی مدل و قدرت تغییر تشخیص بدهی؛ نه جهت فراخوانی <span dir="ltr">HTTP.</span>
3. <span dir="ltr">Customer/Supplier</span>، <span dir="ltr">Conformist</span>، <span dir="ltr">Anticorruption Layer</span> و <span dir="ltr">Open Host Service/Published Language</span> را درست انتخاب کنی.
4. برای هر رابطه <span dir="ltr">Contract</span>، <span dir="ltr">Translation</span>، <span dir="ltr">Owner</span> و <span dir="ltr">Failure Impact</span> ثبت کنی.
5. توضیح بدهی چرا نوشتن <span dir="ltr">`REST`</span> یا <span dir="ltr">`Kafka`</span> <span dir="ltr">Pattern</span> رابطهٔ <span dir="ltr">Context</span>ها نیست.

## 2. چرا <span dir="ltr">Context Map</span> لازم است؟

مرزبندی <span dir="ltr">Context</span>ها فقط نیمی از <span dir="ltr">Strategic Design</span> است. هیچ <span dir="ltr">Context</span> مهم بانکی در خلأ کار نمی‌کند. <span dir="ltr">Customer facts</span> وارد <span dir="ltr">Lending</span> می‌شوند، <span dir="ltr">Lending</span> از <span dir="ltr">Deposits</span> واریز می‌خواهد، <span dir="ltr">Payments</span> وضعیت شبکه را نگه می‌دارد و <span dir="ltr">Accounting Fact</span>های کسب‌وکار را به <span dir="ltr">Journal</span> تبدیل می‌کند.

اگر فقط <span dir="ltr">Box</span>ها را بکشیم و آن‌ها را با خط وصل کنیم، پرسش‌های اصلی پنهان می‌مانند:

- مدل کدام طرف بر دیگری اثر می‌گذارد؟
- چه تیمی برای تغییر <span dir="ltr">Contract</span> قدرت بیشتری دارد؟
- <span dir="ltr">Downstream</span> مدل <span dir="ltr">Upstream</span> را می‌پذیرد یا ترجمه می‌کند؟
- <span dir="ltr">Contract</span> برای یک <span dir="ltr">Consumer</span> خاص طراحی شده یا عمومی و <span dir="ltr">Published</span> است؟
- شکست یا تغییر <span dir="ltr">Upstream</span> چه اثری روی <span dir="ltr">Downstream</span> دارد؟

<span dir="ltr">Context Map</span> نقشهٔ **روابط مدل و همکاری** میان <span dir="ltr">Bounded Context</span>هاست.

## <span dir="ltr">3. Context Map</span> چه چیزی نیست؟

| <span dir="ltr">Diagram/Artifact</span> | سؤال اصلی | چرا جای <span dir="ltr">Context Map</span> را نمی‌گیرد؟ |
|---|---|---|
| <span dir="ltr">System Context Diagram</span> | چه سیستم‌ها و <span dir="ltr">Actor</span>هایی درگیرند؟ | مدل، زبان و رابطهٔ قدرت را الزاماً نشان نمی‌دهد |
| <span dir="ltr">Sequence Diagram</span> | پیام‌ها با چه ترتیب زمانی ردوبدل می‌شوند؟ | <span dir="ltr">Upstream/Downstream</span> دامینی را از روی <span dir="ltr">Caller</span> نمی‌توان فهمید |
| <span dir="ltr">Data Flow</span> | چه داده‌ای حرکت می‌کند؟ | <span dir="ltr">Authority</span> و <span dir="ltr">Translation Policy</span> ممکن است پنهان بماند |
| <span dir="ltr">Deployment Diagram</span> | <span dir="ltr">Process/Node/Pod</span> کجاست؟ | <span dir="ltr">Boundary</span> مدل با <span dir="ltr">Deployment</span> یکی نیست |
| <span dir="ltr">Organization Chart</span> | تیم‌ها کجا هستند؟ | رابطهٔ تاریخی سازمان الزاماً رابطهٔ مدل نیست |

این <span dir="ltr">Artifact</span>ها مکمل یکدیگرند. <span dir="ltr">Context Map</span> به‌طور خاص می‌گوید <span dir="ltr">Context</span>ها چگونه با تفاوت مدل و قدرت تغییر کنار می‌آیند.

## <span dir="ltr">4. Upstream</span> و <span dir="ltr">Downstream</span>

### تعریف عملیاتی

<span dir="ltr">`Upstream`</span> طرفی است که مدل یا <span dir="ltr">Contract</span> ارائه‌شدهٔ آن روی طرف دیگر اثر می‌گذارد و معمولاً اختیار بیشتری بر تکامل آن دارد.

<span dir="ltr">`Downstream`</span> برای کارکرد خود به آن <span dir="ltr">Capability</span>، <span dir="ltr">Fact</span> یا <span dir="ltr">Contract</span> وابسته است و باید با تغییرات <span dir="ltr">Upstream</span> کنار بیاید.

### دام رایج: <span dir="ltr">Caller</span> برابر <span dir="ltr">Upstream</span>

فرض کن <span dir="ltr">Lending</span> فرمان <span dir="ltr">`CreditDepositAccount`</span> را به <span dir="ltr">Deposits</span> می‌فرستد. <span dir="ltr">Lending Caller</span> است، اما دربارهٔ قواعد حساب، پذیرش واریز و مانده اختیار ندارد. <span dir="ltr">Deposits</span> قابلیت و مدل عملیاتی را ارائه می‌کند و <span dir="ltr">Lending</span> به آن وابسته است؛ بنابراین در این رابطه، <span dir="ltr">Deposits</span> می‌تواند <span dir="ltr">Upstream</span> و <span dir="ltr">Lending Downstream</span> باشد.

در مقابل، ممکن است <span dir="ltr">Deposit</span> تیم <span dir="ltr">Contract</span> خود را با نیازهای <span dir="ltr">Lending</span> تنظیم کند. این شیوهٔ همکاری <span dir="ltr">Customer/Supplier</span> است و <span dir="ltr">Lending</span> به‌عنوان <span dir="ltr">Downstream Customer</span> روی <span dir="ltr">Backlog Upstream</span> اثر می‌گذارد.

جهت <span dir="ltr">Event</span> نیز به‌تنهایی جهت مدل را ثابت نمی‌کند. <span dir="ltr">Context</span>ی که <span dir="ltr">Event</span> منتشر می‌کند معمولاً <span dir="ltr">Fact</span> خودش را منتشر می‌کند، اما <span dir="ltr">Governance</span> و <span dir="ltr">Pattern</span> باید جدا تحلیل شوند.

## <span dir="ltr">5. Pattern</span> اول: <span dir="ltr">Customer/Supplier</span>

### معنا

دو تیم رابطهٔ <span dir="ltr">Upstream/Downstream</span> دارند و <span dir="ltr">Upstream</span> متعهد می‌شود نیازهای واقعی <span dir="ltr">Downstream</span> را در برنامه‌ریزی و <span dir="ltr">Contract</span> لحاظ کند. <span dir="ltr">Downstream</span> مشتری مدل/خدمت است، نه صرفاً مصرف‌کننده‌ای بی‌قدرت.

### چه زمانی مناسب است؟

- تیم‌ها امکان مذاکره و برنامه‌ریزی مشترک دارند.
- نیاز <span dir="ltr">Downstream</span> برای <span dir="ltr">Outcome</span> مهم است.
- <span dir="ltr">Upstream</span> می‌تواند <span dir="ltr">Contract</span> هدفمند ارائه کند.
- رابطه و <span dir="ltr">SLA</span> مالک روشن دارد.

### مثال بانکی

<span dir="ltr">Party</span> & <span dir="ltr">Customer</span>، اطلاعات هویتی معتبر را ارائه می‌کند و <span dir="ltr">Lending</span> برای تصمیم اعتباری به یک <span dir="ltr">Customer Reference</span> نیاز دارد. اگر تیم <span dir="ltr">Customer</span> نیازهای <span dir="ltr">Versioning</span>، <span dir="ltr">KYC evidence</span> و <span dir="ltr">Bulk/latency</span> موردنیاز <span dir="ltr">Lending</span> را در <span dir="ltr">Product Backlog</span> لحاظ کند، رابطه می‌تواند <span dir="ltr">Customer/Supplier</span> باشد.

### خطا

نوشتن <span dir="ltr">C/S</span> روی <span dir="ltr">Diagram</span> بدون مکانیزم <span dir="ltr">Governance</span>، <span dir="ltr">Owner</span>، <span dir="ltr">Compatibility</span> و مسیر <span dir="ltr">Escalation</span> فقط برچسب است.

## <span dir="ltr">6. Pattern</span> دوم: <span dir="ltr">Conformist</span>

### معنا

<span dir="ltr">Downstream</span> مدل <span dir="ltr">Upstream</span> را همان‌گونه که هست می‌پذیرد و مدل مستقل یا <span dir="ltr">Translation</span> قابل‌توجهی نمی‌سازد.

### چه زمانی قابل دفاع است؟

- <span dir="ltr">Downstream</span> قدرت یا امکان تغییر <span dir="ltr">Upstream</span> را ندارد.
- مدل <span dir="ltr">Upstream</span> برای مسئلهٔ <span dir="ltr">Downstream</span> به‌اندازهٔ کافی مناسب است.
- هزینهٔ <span dir="ltr">Translation</span> از ارزش مدل مستقل بیشتر است.
- این بخش برای <span dir="ltr">Downstream Core</span> نیست یا خطر آلودگی مدل پایین است.

### مثال محتمل

یک ابزار گزارش‌گیری ساده ممکن است <span dir="ltr">Classification</span> و <span dir="ltr">Code</span>های رسمی <span dir="ltr">Accounting</span> را بدون مدل مستقل بپذیرد. اگر فقط نمایش می‌دهد و تصمیم دامینی متفاوتی ندارد، <span dir="ltr">Conformist</span> می‌تواند اقتصادی باشد.

### خطر

اگر <span dir="ltr">Lending</span> مدل <span dir="ltr">Customer Legacy</span> را با صدها <span dir="ltr">Flag</span> تاریخی وارد <span dir="ltr">Domain Model</span> خود کند، زبان و تصمیم اعتباری به <span dir="ltr">Upstream</span> آلوده می‌شود. کم‌شدن <span dir="ltr">Mapper</span> لزوماً کاهش <span dir="ltr">Coupling</span> نیست.

<span dir="ltr">Conformist</span> «<span dir="ltr">Pattern</span> بد» نیست؛ انتخابی آگاهانه با <span dir="ltr">Trade-off</span> است. برای <span dir="ltr">Core Subdomain</span> باید با احتیاط بیشتری استفاده شود.

## <span dir="ltr">7. Pattern</span> سوم: <span dir="ltr">Anticorruption Layer</span>

### معنا

<span dir="ltr">Downstream</span> یک لایهٔ ترجمه می‌سازد تا مدل <span dir="ltr">Upstream</span> وارد مدل داخلی آن نشود. <span dir="ltr">ACL</span> می‌تواند شامل <span dir="ltr">Adapter</span>، <span dir="ltr">Translator</span>، <span dir="ltr">Facade</span> و <span dir="ltr">Contract-specific Model</span> باشد.

### هدف

هدف <span dir="ltr">ACL</span> صرفاً تبدیل <span dir="ltr">JSON</span> یا <span dir="ltr">Rename</span> فیلد نیست. باید **معنا** را ترجمه و مدل <span dir="ltr">Downstream</span> را محافظت کند.

### مثال بانکی: <span dir="ltr">Legacy Deposits</span>

فرض کن سامانهٔ قدیمی سپرده پاسخ زیر را می‌دهد:


</div>

<div dir="ltr" align="left">

~~~text
statusCode=17, accType=203, usableAmt=..., block1=..., block2=...
~~~

</div>

<div dir="rtl" align="right">


<span dir="ltr">Lending</span> نباید این <span dir="ltr">Code</span>ها و ساختار <span dir="ltr">Legacy</span> را در <span dir="ltr">Rule</span>های اعطا منتشر کند. <span dir="ltr">ACL</span> می‌تواند آن را به مدل محدود زیر ترجمه کند:


</div>

<div dir="ltr" align="left">

~~~text
DisbursementAccountAssessment
- accountId
- acceptsLoanDisbursement
- rejectionReason
- assessedAt
- sourceVersion
~~~

</div>

<div dir="rtl" align="right">


<span dir="ltr">ACL</span> مالک <span dir="ltr">Available Balance</span> نمی‌شود. فقط معنای موردنیاز <span dir="ltr">Downstream</span> را از <span dir="ltr">Contract Upstream</span> ترجمه می‌کند و <span dir="ltr">Provenance</span> را نگه می‌دارد.

### چه زمانی لازم است؟

- <span dir="ltr">Upstream Legacy</span> یا مدل نامتناسب دارد.
- <span dir="ltr">Downstream Core</span> است و باید مدلش محافظت شود.
- دو <span dir="ltr">Context</span> اصطلاح یا <span dir="ltr">Invariant</span> متفاوت دارند.
- تغییر <span dir="ltr">Upstream</span> نباید در مدل <span dir="ltr">Downstream</span> موج ایجاد کند.

### هزینه

- کد و تست ترجمه
- <span dir="ltr">Mapping</span> خطا و <span dir="ltr">Version</span>
- <span dir="ltr">Risk</span> از دست‌رفتن معنا
- <span dir="ltr">Monitoring</span> و <span dir="ltr">Reconciliation</span>

<span dir="ltr">ACL</span> را برای هر <span dir="ltr">DTO</span> کوچک نساز. باید خطری واقعی برای مدل وجود داشته باشد.

## <span dir="ltr">8. Pattern</span> چهارم: <span dir="ltr">Open Host Service</span> و <span dir="ltr">Published Language</span>

### <span dir="ltr">Open Host Service</span>

<span dir="ltr">Upstream</span> مجموعه‌ای مشخص و پایدار از خدمات/<span dir="ltr">Protocol</span> را برای چند مصرف‌کننده عرضه می‌کند، به‌جای ساخت <span dir="ltr">Integration</span> اختصاصی و متفاوت برای هرکدام.

### <span dir="ltr">Published Language</span>

زبان <span dir="ltr">Contract</span> مستند، <span dir="ltr">Versioned</span> و قابل‌مصرفی است که دو یا چند <span dir="ltr">Context</span> برای تبادل از آن استفاده می‌کنند؛ مانند <span dir="ltr">Schema</span> یک <span dir="ltr">Business Event</span> یا <span dir="ltr">Semantic API.</span>

<span dir="ltr">Published Language</span> مدل داخلی <span dir="ltr">Upstream</span> یا یک <span dir="ltr">Canonical Model</span> برای کل بانک نیست. باید فقط معنای لازم در <span dir="ltr">Boundary</span> را منتقل کند.

### مثال بانکی

<span dir="ltr">Deposits</span> می‌تواند <span dir="ltr">Contract</span> عمومی عملیات سپرده را با <span dir="ltr">Command/Result</span>های مشخص عرضه کند و <span dir="ltr">Event</span>های <span dir="ltr">Versioned</span> مانند <span dir="ltr">`DepositCredited`</span> منتشر کند. <span dir="ltr">Accounting</span>، <span dir="ltr">Notification</span> و <span dir="ltr">Reconciliation</span> ممکن است از <span dir="ltr">Published Language</span> رخداد استفاده کنند، ولی هرکدام آن را به مدل خود ترجمه می‌کنند.

### کنترل‌های لازم

- <span dir="ltr">Semantic naming</span>
- <span dir="ltr">Schema/contract version</span>
- <span dir="ltr">Compatibility policy</span>
- <span dir="ltr">Error taxonomy</span>
- <span dir="ltr">Idempotency/correlation semantics</span> در صورت نیاز
- <span dir="ltr">Owner</span> و <span dir="ltr">deprecation path</span>

وجود <span dir="ltr">OpenAPI</span> یا <span dir="ltr">AsyncAPI</span> به‌تنهایی <span dir="ltr">Published Language</span> خوب نمی‌سازد؛ <span dir="ltr">Contract</span> باید معنای دامینی پایدار داشته باشد.

## <span dir="ltr">9. Pattern</span>های مکمل

تمرکز آزمون روی چهار <span dir="ltr">Pattern</span> بالاست، ولی <span dir="ltr">Context Map</span> واقعی ممکن است این‌ها را هم نیاز داشته باشد.

### <span dir="ltr">Partnership</span>

دو <span dir="ltr">Context/Team</span> موفقیت مشترک و وابستگی متقابل قوی دارند و تغییرها را هماهنگ می‌کنند. این <span dir="ltr">Pattern Coordination Cost</span> بالایی دارد و استقلال <span dir="ltr">Release</span> را کاهش می‌دهد؛ باید آگاهانه باشد.

### <span dir="ltr">Shared Kernel</span>

بخش بسیار کوچک و صریحی از مدل/کد بین <span dir="ltr">Context</span>ها مشترک است و هر تغییر با هماهنگی انجام می‌شود. <span dir="ltr">Shared Kernel</span> نباید به <span dir="ltr">`common`</span> عظیم، <span dir="ltr">Entity</span>های <span dir="ltr">JPA</span> مشترک یا <span dir="ltr">Database</span> مشترک تبدیل شود.

### <span dir="ltr">Separate Ways</span>

ارزش <span dir="ltr">Integration</span> کمتر از هزینه و <span dir="ltr">Coupling</span> است؛ <span dir="ltr">Context</span>ها مستقل می‌مانند، حتی اگر مقداری <span dir="ltr">Duplication</span> وجود داشته باشد.

## 10. مثال هدایت‌شده: اعطای تسهیلات

سناریو: پس از انعقاد قرارداد مرابحه، <span dir="ltr">Lending</span> مبلغ را به سپردهٔ مشتری واریز می‌کند و آثار مالی باید ثبت شوند.

### رابطهٔ <span dir="ltr">Product Catalog</span> → <span dir="ltr">Lending</span>

- <span dir="ltr">Upstream: Product/Agreement reference provider</span>
- <span dir="ltr">Downstream: Lending</span>
- <span dir="ltr">Fact: ProductVersion</span> و شروط لازم
- نکته: <span dir="ltr">Lending</span> برای قرارداد منعقدشده به <span dir="ltr">Snapshot</span> مؤثر نیاز دارد، نه <span dir="ltr">Query</span> دائمی نسخهٔ جاری.
- <span dir="ltr">Pattern candidate: OHS/Published Language</span> یا <span dir="ltr">Customer/Supplier</span>، بسته به <span dir="ltr">Governance</span>

### رابطهٔ <span dir="ltr">Party</span> & <span dir="ltr">Customer</span> → <span dir="ltr">Lending</span>

- <span dir="ltr">Upstream: Party</span> & <span dir="ltr">Customer</span>
- <span dir="ltr">Downstream: Lending</span>
- <span dir="ltr">Fact: Party identity</span> و <span dir="ltr">KYC evidence</span>
- <span dir="ltr">Decision distinction: KYC validity</span> با <span dir="ltr">Credit Eligibility</span> یکی نیست.
- <span dir="ltr">Pattern candidate: Customer/Supplier</span> + <span dir="ltr">Published Language</span>

### رابطهٔ <span dir="ltr">Deposits</span> → <span dir="ltr">Lending</span>

- <span dir="ltr">Upstream model authority: Deposits</span> برای عملیات واریز/حساب
- <span dir="ltr">Downstream: Lending</span> که <span dir="ltr">Outcome</span> اعطا به واریز وابسته است
- <span dir="ltr">Command direction: Lending</span> → <span dir="ltr">Deposits</span>
- <span dir="ltr">Result/Event direction: Deposits</span> → <span dir="ltr">Lending/consumers</span>
- <span dir="ltr">Pattern candidate: Customer/Supplier</span> اگر <span dir="ltr">Contract</span> با نیاز اعطا طراحی شود؛ <span dir="ltr">ACL</span> اگر مدل <span dir="ltr">Legacy Deposits</span> نامتناسب باشد.

### رابطهٔ <span dir="ltr">Lending</span> → <span dir="ltr">Accounting</span>

- <span dir="ltr">Upstream fact producer: Lending</span> برای <span dir="ltr">Fact</span>های خودش
- <span dir="ltr">Downstream: Accounting</span> برای ترجمهٔ <span dir="ltr">Fact</span> به <span dir="ltr">Journal</span>
- <span dir="ltr">Accounting</span> نباید <span dir="ltr">State</span> داخلی <span dir="ltr">Loan</span> را مالک شود.
- <span dir="ltr">Pattern candidate: OHS/Published Language</span> در <span dir="ltr">Boundary</span> رخداد + <span dir="ltr">ACL/Translator</span> داخل <span dir="ltr">Accounting</span>

نکته: ممکن است برای یک <span dir="ltr">Pair</span> چند <span dir="ltr">Contract</span> با <span dir="ltr">Pattern</span>های متفاوت وجود داشته باشد. آن‌ها را در یک خط مبهم ادغام نکن.

## 11. انتخاب <span dir="ltr">Pattern</span> با پنج سؤال

برای هر رابطه بپرس:

1. چه کسی <span dir="ltr">Authority</span> مدل/<span dir="ltr">Fact</span> است؟
2. کدام طرف از تغییر دیگری آسیب می‌بیند؟
3. <span dir="ltr">Downstream</span> چقدر قدرت اثرگذاری بر <span dir="ltr">Roadmap Upstream</span> دارد؟
4. مدل <span dir="ltr">Upstream</span> برای مسئلهٔ <span dir="ltr">Downstream</span> مناسب است یا باید ترجمه شود؟
5. <span dir="ltr">Contract</span> یک <span dir="ltr">Consumer</span> خاص دارد یا باید برای چند مصرف‌کننده <span dir="ltr">Published</span> باشد؟

سپس <span dir="ltr">Pattern</span>، <span dir="ltr">Owner</span> قرارداد، <span dir="ltr">Translation location</span> و <span dir="ltr">Failure impact</span> را ثبت کن.

## 12. خطاهای رایج

### <span dir="ltr">`REST`</span> یا <span dir="ltr">`Kafka`</span> به‌عنوان <span dir="ltr">Pattern</span>

این‌ها <span dir="ltr">Transport/Technology</span> هستند. <span dir="ltr">C/S</span>، <span dir="ltr">ACL</span> و <span dir="ltr">Conformist</span> دربارهٔ رابطهٔ مدل و تیم‌اند و می‌توانند روی <span dir="ltr">HTTP</span> یا <span dir="ltr">Messaging</span> اجرا شوند.

### فلش بدون جهت معنایی

فلش باید بگوید <span dir="ltr">Upstream/Downstream</span> چیست. <span dir="ltr">Call direction</span> را جداگانه در <span dir="ltr">Sequence Diagram</span> نشان بده.

### <span dir="ltr">ACL</span> در <span dir="ltr">Upstream</span>

<span dir="ltr">ACL</span> معمولاً از مدل <span dir="ltr">Downstream</span> محافظت می‌کند و تحت کنترل <span dir="ltr">Downstream</span> است. اگر <span dir="ltr">Translator</span> را <span dir="ltr">Upstream</span> تحمیل کند، ممکن است باز هم مدل <span dir="ltr">Upstream</span> غالب بماند.

### <span dir="ltr">Published Language</span> برابر <span dir="ltr">Shared Entity</span>

<span dir="ltr">Published Contract</span> باید <span dir="ltr">Boundary DTO/Event</span> باشد؛ <span dir="ltr">Entity</span> داخلی و <span dir="ltr">Schema</span> دیتابیس نیست.

### <span dir="ltr">Conformist</span> بدون ثبت <span dir="ltr">Risk</span>

پذیرفتن مدل <span dir="ltr">Upstream</span> ممکن است اقتصادی باشد، اما <span dir="ltr">Coupling</span> و محدودیت تکامل باید ثبت شود.

### یک رابطهٔ دوطرفهٔ مبهم

اگر <span dir="ltr">Payments</span> از <span dir="ltr">Deposits Debit</span> می‌خواهد و <span dir="ltr">Deposits</span> رخداد به <span dir="ltr">Payments</span> می‌دهد، <span dir="ltr">Intent</span>، <span dir="ltr">Fact</span> و <span dir="ltr">Authority</span> را جدا تحلیل کن؛ یک فلش دوسر اطلاعات کافی ندارد.

## 13. تمرین هدایت‌شده

رابطهٔ <span dir="ltr">`Legacy Customer → New Lending`</span> را در یک ردیف کامل کن:

| <span dir="ltr">Upstream</span> | <span dir="ltr">Downstream</span> | <span dir="ltr">Pattern</span> | <span dir="ltr">Contract</span> | <span dir="ltr">Translation</span> | <span dir="ltr">Failure impact</span> |
|---|---|---|---|---|---|
| <span dir="ltr">Legacy Customer</span> | <span dir="ltr">New Lending</span> | ؟ | ؟ | ؟ | ؟ |

سپس یک <span dir="ltr">Alternative Pattern</span> بنویس و توضیح بده چه <span dir="ltr">Force</span>ای انتخاب را تغییر می‌دهد.

## 14. تمرین مستقل

[<span dir="ltr">Day 03 Exercise</span> — <span dir="ltr">Context Map</span>](../exercises/day-03-context-map.md) را انجام بده. حداقل شش رابطه بنویس و برای هرکدام <span dir="ltr">Pattern</span> را با <span dir="ltr">Forces</span> دفاع کن.

## 15. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تشخیص درست <span dir="ltr">Upstream/Downstream</span> | ۲ |
| انتخاب <span dir="ltr">Pattern</span> با استدلال | ۳ |
| <span dir="ltr">Contract</span> و <span dir="ltr">Translation</span> روشن | ۲ |
| <span dir="ltr">Authority</span> و <span dir="ltr">Failure impact</span> | ۲ |
| ثبت <span dir="ltr">Alternative/Open Question</span> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. خط بدون <span dir="ltr">Pattern</span> و <span dir="ltr">Contract</span> امتیاز ندارد.

## 16. آزمون خروج

درس را ببند و [<span dir="ltr">Day 03 Exit Ticket</span>](../quizzes/day-03-exit-ticket.md) را پاسخ بده.

## 17. منبع اصلی

- [<span dir="ltr">Domain-Driven Design Reference</span> — <span dir="ltr">Context Mapping Patterns</span>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

<span dir="ltr">Pattern</span>ها از مرجع <span dir="ltr">Eric Evans</span> گرفته شده‌اند؛ انتخاب هر <span dir="ltr">Pattern</span> در مثال بانکی یک <span dir="ltr">Design Hypothesis</span> وابسته به رابطهٔ واقعی تیم‌ها و <span dir="ltr">Contract</span>هاست.

</div>
