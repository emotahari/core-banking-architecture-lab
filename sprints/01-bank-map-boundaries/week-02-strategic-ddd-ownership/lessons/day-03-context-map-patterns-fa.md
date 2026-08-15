<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 03</bdi> — <bdi dir="ltr">Context Map</bdi> و الگوهای رابطه

- <bdi dir="ltr">Day budget: 50 minutes including exercise and exit ticket</bdi>
- <bdi dir="ltr">Output: Context Map relationships v0.1</bdi>
- <bdi dir="ltr">Banking case:</bdi> اعطای تسهیلات و واریز به سپرده

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Context Map</bdi> را از <bdi dir="ltr">System Diagram</bdi>، <bdi dir="ltr">Sequence Diagram</bdi> و <bdi dir="ltr">Data Flow</bdi> جدا کنی.
2. <bdi dir="ltr">Upstream</bdi> و <bdi dir="ltr">Downstream</bdi> را بر اساس وابستگی مدل و قدرت تغییر تشخیص بدهی؛ نه جهت فراخوانی <bdi dir="ltr">HTTP.</bdi>
3. <bdi dir="ltr">Customer/Supplier</bdi>، <bdi dir="ltr">Conformist</bdi>، <bdi dir="ltr">Anticorruption Layer</bdi> و <bdi dir="ltr">Open Host Service/Published Language</bdi> را درست انتخاب کنی.
4. برای هر رابطه <bdi dir="ltr">Contract</bdi>، <bdi dir="ltr">Translation</bdi>، <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">Failure Impact</bdi> ثبت کنی.
5. توضیح بدهی چرا نوشتن <bdi dir="ltr">`REST`</bdi> یا <bdi dir="ltr">`Kafka`</bdi> <bdi dir="ltr">Pattern</bdi> رابطهٔ <bdi dir="ltr">Context</bdi>ها نیست.

## 2. چرا <bdi dir="ltr">Context Map</bdi> لازم است؟

مرزبندی <bdi dir="ltr">Context</bdi>ها فقط نیمی از <bdi dir="ltr">Strategic Design</bdi> است. هیچ <bdi dir="ltr">Context</bdi> مهم بانکی در خلأ کار نمی‌کند. <bdi dir="ltr">Customer facts</bdi> وارد <bdi dir="ltr">Lending</bdi> می‌شوند، <bdi dir="ltr">Lending</bdi> از <bdi dir="ltr">Deposits</bdi> واریز می‌خواهد، <bdi dir="ltr">Payments</bdi> وضعیت شبکه را نگه می‌دارد و <bdi dir="ltr">Accounting Fact</bdi>های کسب‌وکار را به <bdi dir="ltr">Journal</bdi> تبدیل می‌کند.

اگر فقط <bdi dir="ltr">Box</bdi>ها را بکشیم و آن‌ها را با خط وصل کنیم، پرسش‌های اصلی پنهان می‌مانند:

- مدل کدام طرف بر دیگری اثر می‌گذارد؟
- چه تیمی برای تغییر <bdi dir="ltr">Contract</bdi> قدرت بیشتری دارد؟
- <bdi dir="ltr">Downstream</bdi> مدل <bdi dir="ltr">Upstream</bdi> را می‌پذیرد یا ترجمه می‌کند؟
- <bdi dir="ltr">Contract</bdi> برای یک <bdi dir="ltr">Consumer</bdi> خاص طراحی شده یا عمومی و <bdi dir="ltr">Published</bdi> است؟
- شکست یا تغییر <bdi dir="ltr">Upstream</bdi> چه اثری روی <bdi dir="ltr">Downstream</bdi> دارد؟

<bdi dir="ltr">Context Map</bdi> نقشهٔ **روابط مدل و همکاری** میان <bdi dir="ltr">Bounded Context</bdi>هاست.

## <bdi dir="ltr">3. Context Map</bdi> چه چیزی نیست؟

| <bdi dir="ltr">Diagram/Artifact</bdi> | سؤال اصلی | چرا جای <bdi dir="ltr">Context Map</bdi> را نمی‌گیرد؟ |
|---|---|---|
| <bdi dir="ltr">System Context Diagram</bdi> | چه سیستم‌ها و <bdi dir="ltr">Actor</bdi>هایی درگیرند؟ | مدل، زبان و رابطهٔ قدرت را الزاماً نشان نمی‌دهد |
| <bdi dir="ltr">Sequence Diagram</bdi> | پیام‌ها با چه ترتیب زمانی ردوبدل می‌شوند؟ | <bdi dir="ltr">Upstream/Downstream</bdi> دامینی را از روی <bdi dir="ltr">Caller</bdi> نمی‌توان فهمید |
| <bdi dir="ltr">Data Flow</bdi> | چه داده‌ای حرکت می‌کند؟ | <bdi dir="ltr">Authority</bdi> و <bdi dir="ltr">Translation Policy</bdi> ممکن است پنهان بماند |
| <bdi dir="ltr">Deployment Diagram</bdi> | <bdi dir="ltr">Process/Node/Pod</bdi> کجاست؟ | <bdi dir="ltr">Boundary</bdi> مدل با <bdi dir="ltr">Deployment</bdi> یکی نیست |
| <bdi dir="ltr">Organization Chart</bdi> | تیم‌ها کجا هستند؟ | رابطهٔ تاریخی سازمان الزاماً رابطهٔ مدل نیست |

این <bdi dir="ltr">Artifact</bdi>ها مکمل یکدیگرند. <bdi dir="ltr">Context Map</bdi> به‌طور خاص می‌گوید <bdi dir="ltr">Context</bdi>ها چگونه با تفاوت مدل و قدرت تغییر کنار می‌آیند.

## <bdi dir="ltr">4. Upstream</bdi> و <bdi dir="ltr">Downstream</bdi>

### تعریف عملیاتی

<bdi dir="ltr">`Upstream`</bdi> طرفی است که مدل یا <bdi dir="ltr">Contract</bdi> ارائه‌شدهٔ آن روی طرف دیگر اثر می‌گذارد و معمولاً اختیار بیشتری بر تکامل آن دارد.

<bdi dir="ltr">`Downstream`</bdi> برای کارکرد خود به آن <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Fact</bdi> یا <bdi dir="ltr">Contract</bdi> وابسته است و باید با تغییرات <bdi dir="ltr">Upstream</bdi> کنار بیاید.

### دام رایج: <bdi dir="ltr">Caller</bdi> برابر <bdi dir="ltr">Upstream</bdi>

فرض کن <bdi dir="ltr">Lending</bdi> فرمان <bdi dir="ltr">`CreditDepositAccount`</bdi> را به <bdi dir="ltr">Deposits</bdi> می‌فرستد. <bdi dir="ltr">Lending Caller</bdi> است، اما دربارهٔ قواعد حساب، پذیرش واریز و مانده اختیار ندارد. <bdi dir="ltr">Deposits</bdi> قابلیت و مدل عملیاتی را ارائه می‌کند و <bdi dir="ltr">Lending</bdi> به آن وابسته است؛ بنابراین در این رابطه، <bdi dir="ltr">Deposits</bdi> می‌تواند <bdi dir="ltr">Upstream</bdi> و <bdi dir="ltr">Lending Downstream</bdi> باشد.

در مقابل، ممکن است <bdi dir="ltr">Deposit</bdi> تیم <bdi dir="ltr">Contract</bdi> خود را با نیازهای <bdi dir="ltr">Lending</bdi> تنظیم کند. این شیوهٔ همکاری <bdi dir="ltr">Customer/Supplier</bdi> است و <bdi dir="ltr">Lending</bdi> به‌عنوان <bdi dir="ltr">Downstream Customer</bdi> روی <bdi dir="ltr">Backlog Upstream</bdi> اثر می‌گذارد.

جهت <bdi dir="ltr">Event</bdi> نیز به‌تنهایی جهت مدل را ثابت نمی‌کند. <bdi dir="ltr">Context</bdi>ی که <bdi dir="ltr">Event</bdi> منتشر می‌کند معمولاً <bdi dir="ltr">Fact</bdi> خودش را منتشر می‌کند، اما <bdi dir="ltr">Governance</bdi> و <bdi dir="ltr">Pattern</bdi> باید جدا تحلیل شوند.

## <bdi dir="ltr">5. Pattern</bdi> اول: <bdi dir="ltr">Customer/Supplier</bdi>

### معنا

دو تیم رابطهٔ <bdi dir="ltr">Upstream/Downstream</bdi> دارند و <bdi dir="ltr">Upstream</bdi> متعهد می‌شود نیازهای واقعی <bdi dir="ltr">Downstream</bdi> را در برنامه‌ریزی و <bdi dir="ltr">Contract</bdi> لحاظ کند. <bdi dir="ltr">Downstream</bdi> مشتری مدل/خدمت است، نه صرفاً مصرف‌کننده‌ای بی‌قدرت.

### چه زمانی مناسب است؟

- تیم‌ها امکان مذاکره و برنامه‌ریزی مشترک دارند.
- نیاز <bdi dir="ltr">Downstream</bdi> برای <bdi dir="ltr">Outcome</bdi> مهم است.
- <bdi dir="ltr">Upstream</bdi> می‌تواند <bdi dir="ltr">Contract</bdi> هدفمند ارائه کند.
- رابطه و <bdi dir="ltr">SLA</bdi> مالک روشن دارد.

### مثال بانکی

<bdi dir="ltr">Party</bdi> & <bdi dir="ltr">Customer</bdi>، اطلاعات هویتی معتبر را ارائه می‌کند و <bdi dir="ltr">Lending</bdi> برای تصمیم اعتباری به یک <bdi dir="ltr">Customer Reference</bdi> نیاز دارد. اگر تیم <bdi dir="ltr">Customer</bdi> نیازهای <bdi dir="ltr">Versioning</bdi>، <bdi dir="ltr">KYC evidence</bdi> و <bdi dir="ltr">Bulk/latency</bdi> موردنیاز <bdi dir="ltr">Lending</bdi> را در <bdi dir="ltr">Product Backlog</bdi> لحاظ کند، رابطه می‌تواند <bdi dir="ltr">Customer/Supplier</bdi> باشد.

### خطا

نوشتن <bdi dir="ltr">C/S</bdi> روی <bdi dir="ltr">Diagram</bdi> بدون مکانیزم <bdi dir="ltr">Governance</bdi>، <bdi dir="ltr">Owner</bdi>، <bdi dir="ltr">Compatibility</bdi> و مسیر <bdi dir="ltr">Escalation</bdi> فقط برچسب است.

## <bdi dir="ltr">6. Pattern</bdi> دوم: <bdi dir="ltr">Conformist</bdi>

### معنا

<bdi dir="ltr">Downstream</bdi> مدل <bdi dir="ltr">Upstream</bdi> را همان‌گونه که هست می‌پذیرد و مدل مستقل یا <bdi dir="ltr">Translation</bdi> قابل‌توجهی نمی‌سازد.

### چه زمانی قابل دفاع است؟

- <bdi dir="ltr">Downstream</bdi> قدرت یا امکان تغییر <bdi dir="ltr">Upstream</bdi> را ندارد.
- مدل <bdi dir="ltr">Upstream</bdi> برای مسئلهٔ <bdi dir="ltr">Downstream</bdi> به‌اندازهٔ کافی مناسب است.
- هزینهٔ <bdi dir="ltr">Translation</bdi> از ارزش مدل مستقل بیشتر است.
- این بخش برای <bdi dir="ltr">Downstream Core</bdi> نیست یا خطر آلودگی مدل پایین است.

### مثال محتمل

یک ابزار گزارش‌گیری ساده ممکن است <bdi dir="ltr">Classification</bdi> و <bdi dir="ltr">Code</bdi>های رسمی <bdi dir="ltr">Accounting</bdi> را بدون مدل مستقل بپذیرد. اگر فقط نمایش می‌دهد و تصمیم دامینی متفاوتی ندارد، <bdi dir="ltr">Conformist</bdi> می‌تواند اقتصادی باشد.

### خطر

اگر <bdi dir="ltr">Lending</bdi> مدل <bdi dir="ltr">Customer Legacy</bdi> را با صدها <bdi dir="ltr">Flag</bdi> تاریخی وارد <bdi dir="ltr">Domain Model</bdi> خود کند، زبان و تصمیم اعتباری به <bdi dir="ltr">Upstream</bdi> آلوده می‌شود. کم‌شدن <bdi dir="ltr">Mapper</bdi> لزوماً کاهش <bdi dir="ltr">Coupling</bdi> نیست.

<bdi dir="ltr">Conformist</bdi> «<bdi dir="ltr">Pattern</bdi> بد» نیست؛ انتخابی آگاهانه با <bdi dir="ltr">Trade-off</bdi> است. برای <bdi dir="ltr">Core Subdomain</bdi> باید با احتیاط بیشتری استفاده شود.

## <bdi dir="ltr">7. Pattern</bdi> سوم: <bdi dir="ltr">Anticorruption Layer</bdi>

### معنا

<bdi dir="ltr">Downstream</bdi> یک لایهٔ ترجمه می‌سازد تا مدل <bdi dir="ltr">Upstream</bdi> وارد مدل داخلی آن نشود. <bdi dir="ltr">ACL</bdi> می‌تواند شامل <bdi dir="ltr">Adapter</bdi>، <bdi dir="ltr">Translator</bdi>، <bdi dir="ltr">Facade</bdi> و <bdi dir="ltr">Contract-specific Model</bdi> باشد.

### هدف

هدف <bdi dir="ltr">ACL</bdi> صرفاً تبدیل <bdi dir="ltr">JSON</bdi> یا <bdi dir="ltr">Rename</bdi> فیلد نیست. باید **معنا** را ترجمه و مدل <bdi dir="ltr">Downstream</bdi> را محافظت کند.

### مثال بانکی: <bdi dir="ltr">Legacy Deposits</bdi>

فرض کن سامانهٔ قدیمی سپرده پاسخ زیر را می‌دهد:


</div>

<div dir="ltr" align="left">

~~~text
statusCode=17, accType=203, usableAmt=..., block1=..., block2=...
~~~

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Lending</bdi> نباید این <bdi dir="ltr">Code</bdi>ها و ساختار <bdi dir="ltr">Legacy</bdi> را در <bdi dir="ltr">Rule</bdi>های اعطا منتشر کند. <bdi dir="ltr">ACL</bdi> می‌تواند آن را به مدل محدود زیر ترجمه کند:


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


<bdi dir="ltr">ACL</bdi> مالک <bdi dir="ltr">Available Balance</bdi> نمی‌شود. فقط معنای موردنیاز <bdi dir="ltr">Downstream</bdi> را از <bdi dir="ltr">Contract Upstream</bdi> ترجمه می‌کند و <bdi dir="ltr">Provenance</bdi> را نگه می‌دارد.

### چه زمانی لازم است؟

- <bdi dir="ltr">Upstream Legacy</bdi> یا مدل نامتناسب دارد.
- <bdi dir="ltr">Downstream Core</bdi> است و باید مدلش محافظت شود.
- دو <bdi dir="ltr">Context</bdi> اصطلاح یا <bdi dir="ltr">Invariant</bdi> متفاوت دارند.
- تغییر <bdi dir="ltr">Upstream</bdi> نباید در مدل <bdi dir="ltr">Downstream</bdi> موج ایجاد کند.

### هزینه

- کد و تست ترجمه
- <bdi dir="ltr">Mapping</bdi> خطا و <bdi dir="ltr">Version</bdi>
- <bdi dir="ltr">Risk</bdi> از دست‌رفتن معنا
- <bdi dir="ltr">Monitoring</bdi> و <bdi dir="ltr">Reconciliation</bdi>

<bdi dir="ltr">ACL</bdi> را برای هر <bdi dir="ltr">DTO</bdi> کوچک نساز. باید خطری واقعی برای مدل وجود داشته باشد.

## <bdi dir="ltr">8. Pattern</bdi> چهارم: <bdi dir="ltr">Open Host Service</bdi> و <bdi dir="ltr">Published Language</bdi>

### <bdi dir="ltr">Open Host Service</bdi>

<bdi dir="ltr">Upstream</bdi> مجموعه‌ای مشخص و پایدار از خدمات/<bdi dir="ltr">Protocol</bdi> را برای چند مصرف‌کننده عرضه می‌کند، به‌جای ساخت <bdi dir="ltr">Integration</bdi> اختصاصی و متفاوت برای هرکدام.

### <bdi dir="ltr">Published Language</bdi>

زبان <bdi dir="ltr">Contract</bdi> مستند، <bdi dir="ltr">Versioned</bdi> و قابل‌مصرفی است که دو یا چند <bdi dir="ltr">Context</bdi> برای تبادل از آن استفاده می‌کنند؛ مانند <bdi dir="ltr">Schema</bdi> یک <bdi dir="ltr">Business Event</bdi> یا <bdi dir="ltr">Semantic API.</bdi>

<bdi dir="ltr">Published Language</bdi> مدل داخلی <bdi dir="ltr">Upstream</bdi> یا یک <bdi dir="ltr">Canonical Model</bdi> برای کل بانک نیست. باید فقط معنای لازم در <bdi dir="ltr">Boundary</bdi> را منتقل کند.

### مثال بانکی

<bdi dir="ltr">Deposits</bdi> می‌تواند <bdi dir="ltr">Contract</bdi> عمومی عملیات سپرده را با <bdi dir="ltr">Command/Result</bdi>های مشخص عرضه کند و <bdi dir="ltr">Event</bdi>های <bdi dir="ltr">Versioned</bdi> مانند <bdi dir="ltr">`DepositCredited`</bdi> منتشر کند. <bdi dir="ltr">Accounting</bdi>، <bdi dir="ltr">Notification</bdi> و <bdi dir="ltr">Reconciliation</bdi> ممکن است از <bdi dir="ltr">Published Language</bdi> رخداد استفاده کنند، ولی هرکدام آن را به مدل خود ترجمه می‌کنند.

### کنترل‌های لازم

- <bdi dir="ltr">Semantic naming</bdi>
- <bdi dir="ltr">Schema/contract version</bdi>
- <bdi dir="ltr">Compatibility policy</bdi>
- <bdi dir="ltr">Error taxonomy</bdi>
- <bdi dir="ltr">Idempotency/correlation semantics</bdi> در صورت نیاز
- <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">deprecation path</bdi>

وجود <bdi dir="ltr">OpenAPI</bdi> یا <bdi dir="ltr">AsyncAPI</bdi> به‌تنهایی <bdi dir="ltr">Published Language</bdi> خوب نمی‌سازد؛ <bdi dir="ltr">Contract</bdi> باید معنای دامینی پایدار داشته باشد.

## <bdi dir="ltr">9. Pattern</bdi>های مکمل

تمرکز آزمون روی چهار <bdi dir="ltr">Pattern</bdi> بالاست، ولی <bdi dir="ltr">Context Map</bdi> واقعی ممکن است این‌ها را هم نیاز داشته باشد.

### <bdi dir="ltr">Partnership</bdi>

دو <bdi dir="ltr">Context/Team</bdi> موفقیت مشترک و وابستگی متقابل قوی دارند و تغییرها را هماهنگ می‌کنند. این <bdi dir="ltr">Pattern Coordination Cost</bdi> بالایی دارد و استقلال <bdi dir="ltr">Release</bdi> را کاهش می‌دهد؛ باید آگاهانه باشد.

### <bdi dir="ltr">Shared Kernel</bdi>

بخش بسیار کوچک و صریحی از مدل/کد بین <bdi dir="ltr">Context</bdi>ها مشترک است و هر تغییر با هماهنگی انجام می‌شود. <bdi dir="ltr">Shared Kernel</bdi> نباید به <bdi dir="ltr">`common`</bdi> عظیم، <bdi dir="ltr">Entity</bdi>های <bdi dir="ltr">JPA</bdi> مشترک یا <bdi dir="ltr">Database</bdi> مشترک تبدیل شود.

### <bdi dir="ltr">Separate Ways</bdi>

ارزش <bdi dir="ltr">Integration</bdi> کمتر از هزینه و <bdi dir="ltr">Coupling</bdi> است؛ <bdi dir="ltr">Context</bdi>ها مستقل می‌مانند، حتی اگر مقداری <bdi dir="ltr">Duplication</bdi> وجود داشته باشد.

## 10. مثال هدایت‌شده: اعطای تسهیلات

سناریو: پس از انعقاد قرارداد مرابحه، <bdi dir="ltr">Lending</bdi> مبلغ را به سپردهٔ مشتری واریز می‌کند و آثار مالی باید ثبت شوند.

### رابطهٔ <bdi dir="ltr">Product Catalog</bdi> → <bdi dir="ltr">Lending</bdi>

- <bdi dir="ltr">Upstream: Product/Agreement reference provider</bdi>
- <bdi dir="ltr">Downstream: Lending</bdi>
- <bdi dir="ltr">Fact: ProductVersion</bdi> و شروط لازم
- نکته: <bdi dir="ltr">Lending</bdi> برای قرارداد منعقدشده به <bdi dir="ltr">Snapshot</bdi> مؤثر نیاز دارد، نه <bdi dir="ltr">Query</bdi> دائمی نسخهٔ جاری.
- <bdi dir="ltr">Pattern candidate: OHS/Published Language</bdi> یا <bdi dir="ltr">Customer/Supplier</bdi>، بسته به <bdi dir="ltr">Governance</bdi>

### رابطهٔ <bdi dir="ltr">Party</bdi> & <bdi dir="ltr">Customer</bdi> → <bdi dir="ltr">Lending</bdi>

- <bdi dir="ltr">Upstream: Party</bdi> & <bdi dir="ltr">Customer</bdi>
- <bdi dir="ltr">Downstream: Lending</bdi>
- <bdi dir="ltr">Fact: Party identity</bdi> و <bdi dir="ltr">KYC evidence</bdi>
- <bdi dir="ltr">Decision distinction: KYC validity</bdi> با <bdi dir="ltr">Credit Eligibility</bdi> یکی نیست.
- <bdi dir="ltr">Pattern candidate: Customer/Supplier</bdi> + <bdi dir="ltr">Published Language</bdi>

### رابطهٔ <bdi dir="ltr">Deposits</bdi> → <bdi dir="ltr">Lending</bdi>

- <bdi dir="ltr">Upstream model authority: Deposits</bdi> برای عملیات واریز/حساب
- <bdi dir="ltr">Downstream: Lending</bdi> که <bdi dir="ltr">Outcome</bdi> اعطا به واریز وابسته است
- <bdi dir="ltr">Command direction: Lending</bdi> → <bdi dir="ltr">Deposits</bdi>
- <bdi dir="ltr">Result/Event direction: Deposits</bdi> → <bdi dir="ltr">Lending/consumers</bdi>
- <bdi dir="ltr">Pattern candidate: Customer/Supplier</bdi> اگر <bdi dir="ltr">Contract</bdi> با نیاز اعطا طراحی شود؛ <bdi dir="ltr">ACL</bdi> اگر مدل <bdi dir="ltr">Legacy Deposits</bdi> نامتناسب باشد.

### رابطهٔ <bdi dir="ltr">Lending</bdi> → <bdi dir="ltr">Accounting</bdi>

- <bdi dir="ltr">Upstream fact producer: Lending</bdi> برای <bdi dir="ltr">Fact</bdi>های خودش
- <bdi dir="ltr">Downstream: Accounting</bdi> برای ترجمهٔ <bdi dir="ltr">Fact</bdi> به <bdi dir="ltr">Journal</bdi>
- <bdi dir="ltr">Accounting</bdi> نباید <bdi dir="ltr">State</bdi> داخلی <bdi dir="ltr">Loan</bdi> را مالک شود.
- <bdi dir="ltr">Pattern candidate: OHS/Published Language</bdi> در <bdi dir="ltr">Boundary</bdi> رخداد + <bdi dir="ltr">ACL/Translator</bdi> داخل <bdi dir="ltr">Accounting</bdi>

نکته: ممکن است برای یک <bdi dir="ltr">Pair</bdi> چند <bdi dir="ltr">Contract</bdi> با <bdi dir="ltr">Pattern</bdi>های متفاوت وجود داشته باشد. آن‌ها را در یک خط مبهم ادغام نکن.

## 11. انتخاب <bdi dir="ltr">Pattern</bdi> با پنج سؤال

برای هر رابطه بپرس:

1. چه کسی <bdi dir="ltr">Authority</bdi> مدل/<bdi dir="ltr">Fact</bdi> است؟
2. کدام طرف از تغییر دیگری آسیب می‌بیند؟
3. <bdi dir="ltr">Downstream</bdi> چقدر قدرت اثرگذاری بر <bdi dir="ltr">Roadmap Upstream</bdi> دارد؟
4. مدل <bdi dir="ltr">Upstream</bdi> برای مسئلهٔ <bdi dir="ltr">Downstream</bdi> مناسب است یا باید ترجمه شود؟
5. <bdi dir="ltr">Contract</bdi> یک <bdi dir="ltr">Consumer</bdi> خاص دارد یا باید برای چند مصرف‌کننده <bdi dir="ltr">Published</bdi> باشد؟

سپس <bdi dir="ltr">Pattern</bdi>، <bdi dir="ltr">Owner</bdi> قرارداد، <bdi dir="ltr">Translation location</bdi> و <bdi dir="ltr">Failure impact</bdi> را ثبت کن.

## 12. خطاهای رایج

### <bdi dir="ltr">`REST`</bdi> یا <bdi dir="ltr">`Kafka`</bdi> به‌عنوان <bdi dir="ltr">Pattern</bdi>

این‌ها <bdi dir="ltr">Transport/Technology</bdi> هستند. <bdi dir="ltr">C/S</bdi>، <bdi dir="ltr">ACL</bdi> و <bdi dir="ltr">Conformist</bdi> دربارهٔ رابطهٔ مدل و تیم‌اند و می‌توانند روی <bdi dir="ltr">HTTP</bdi> یا <bdi dir="ltr">Messaging</bdi> اجرا شوند.

### فلش بدون جهت معنایی

فلش باید بگوید <bdi dir="ltr">Upstream/Downstream</bdi> چیست. <bdi dir="ltr">Call direction</bdi> را جداگانه در <bdi dir="ltr">Sequence Diagram</bdi> نشان بده.

### <bdi dir="ltr">ACL</bdi> در <bdi dir="ltr">Upstream</bdi>

<bdi dir="ltr">ACL</bdi> معمولاً از مدل <bdi dir="ltr">Downstream</bdi> محافظت می‌کند و تحت کنترل <bdi dir="ltr">Downstream</bdi> است. اگر <bdi dir="ltr">Translator</bdi> را <bdi dir="ltr">Upstream</bdi> تحمیل کند، ممکن است باز هم مدل <bdi dir="ltr">Upstream</bdi> غالب بماند.

### <bdi dir="ltr">Published Language</bdi> برابر <bdi dir="ltr">Shared Entity</bdi>

<bdi dir="ltr">Published Contract</bdi> باید <bdi dir="ltr">Boundary DTO/Event</bdi> باشد؛ <bdi dir="ltr">Entity</bdi> داخلی و <bdi dir="ltr">Schema</bdi> دیتابیس نیست.

### <bdi dir="ltr">Conformist</bdi> بدون ثبت <bdi dir="ltr">Risk</bdi>

پذیرفتن مدل <bdi dir="ltr">Upstream</bdi> ممکن است اقتصادی باشد، اما <bdi dir="ltr">Coupling</bdi> و محدودیت تکامل باید ثبت شود.

### یک رابطهٔ دوطرفهٔ مبهم

اگر <bdi dir="ltr">Payments</bdi> از <bdi dir="ltr">Deposits Debit</bdi> می‌خواهد و <bdi dir="ltr">Deposits</bdi> رخداد به <bdi dir="ltr">Payments</bdi> می‌دهد، <bdi dir="ltr">Intent</bdi>، <bdi dir="ltr">Fact</bdi> و <bdi dir="ltr">Authority</bdi> را جدا تحلیل کن؛ یک فلش دوسر اطلاعات کافی ندارد.

## 13. تمرین هدایت‌شده

رابطهٔ <bdi dir="ltr">`Legacy Customer → New Lending`</bdi> را در یک ردیف کامل کن:

| <bdi dir="ltr">Upstream</bdi> | <bdi dir="ltr">Downstream</bdi> | <bdi dir="ltr">Pattern</bdi> | <bdi dir="ltr">Contract</bdi> | <bdi dir="ltr">Translation</bdi> | <bdi dir="ltr">Failure impact</bdi> |
|---|---|---|---|---|---|
| <bdi dir="ltr">Legacy Customer</bdi> | <bdi dir="ltr">New Lending</bdi> | ؟ | ؟ | ؟ | ؟ |

سپس یک <bdi dir="ltr">Alternative Pattern</bdi> بنویس و توضیح بده چه <bdi dir="ltr">Force</bdi>ای انتخاب را تغییر می‌دهد.

## 14. تمرین مستقل

[<bdi dir="ltr">Day 03 Exercise</bdi> — <bdi dir="ltr">Context Map</bdi>](../exercises/day-03-context-map.md) را انجام بده. حداقل شش رابطه بنویس و برای هرکدام <bdi dir="ltr">Pattern</bdi> را با <bdi dir="ltr">Forces</bdi> دفاع کن.

## 15. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| تشخیص درست <bdi dir="ltr">Upstream/Downstream</bdi> | ۲ |
| انتخاب <bdi dir="ltr">Pattern</bdi> با استدلال | ۳ |
| <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Translation</bdi> روشن | ۲ |
| <bdi dir="ltr">Authority</bdi> و <bdi dir="ltr">Failure impact</bdi> | ۲ |
| ثبت <bdi dir="ltr">Alternative/Open Question</bdi> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. خط بدون <bdi dir="ltr">Pattern</bdi> و <bdi dir="ltr">Contract</bdi> امتیاز ندارد.

## 16. آزمون خروج

درس را ببند و [<bdi dir="ltr">Day 03 Exit Ticket</bdi>](../quizzes/day-03-exit-ticket.md) را پاسخ بده.

## 17. منبع اصلی

- [<bdi dir="ltr">Domain-Driven Design Reference</bdi> — <bdi dir="ltr">Context Mapping Patterns</bdi>](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

<bdi dir="ltr">Pattern</bdi>ها از مرجع <bdi dir="ltr">Eric Evans</bdi> گرفته شده‌اند؛ انتخاب هر <bdi dir="ltr">Pattern</bdi> در مثال بانکی یک <bdi dir="ltr">Design Hypothesis</bdi> وابسته به رابطهٔ واقعی تیم‌ها و <bdi dir="ltr">Contract</bdi>هاست.

</div>
