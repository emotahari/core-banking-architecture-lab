<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# پروندهٔ <span dir="ltr">Week 02</span> — <span dir="ltr">Monzo</span>؛ از <span dir="ltr">Mondo</span> تا بانک ۳۰۰۰+ <span dir="ltr">Microservice</span>

- <span dir="ltr">Case type:</span> بانک دیجیتال با <span dir="ltr">Core Banking</span> داخلی؛ نه محصول <span dir="ltr">Core Banking</span> قابل خرید
- <span dir="ltr">Relevance: Strategic DDD</span>، <span dir="ltr">Ownership</span>، <span dir="ltr">Team autonomy</span>، <span dir="ltr">Platform engineering</span> و هزینهٔ مرزهای بسیار ریز
- <span dir="ltr">Evidence checked: 15 August 2026</span>
- <span dir="ltr">Reading/analysis budget: 45 minutes</span>
- <span dir="ltr">Evidence rule: Fact</span>های جاری از منابع رسمی <span dir="ltr">Monzo</span> یا <span dir="ltr">FCA</span>؛ <span dir="ltr">Domain map</span> این پرونده یک <span dir="ltr">Inference</span> تحلیلی است.

## 1. چرا <span dir="ltr">Monzo</span> برای <span dir="ltr">Week 02</span>؟

<span dir="ltr">Monzo</span> نمونهٔ سادهٔ «<span dir="ltr">Cloud</span> خوب، <span dir="ltr">Mainframe</span> بد» نیست. داستان آن تضادهای مهم‌تری دارد:

- با سه <span dir="ltr">Backend developer</span>، از روز اول <span dir="ltr">Microservice-first</span> شد.
- برای استقلال تیم‌ها و استقرار مستقل طراحی کرد، اما بعدها باید بیش از ۳۰۰۰ <span dir="ltr">Service</span> را استاندارد، مهاجرت و کنترل می‌کرد.
- معماری بسیار مدرن مانع عقب‌ماندن کنترل‌های <span dir="ltr">Financial Crime</span> از رشد نشد.
- برای تحمل خرابی کامل <span dir="ltr">Cloud</span>، یک <span dir="ltr">Stand-in</span> مستقل و کوچک در <span dir="ltr">Cloud</span> دوم ساخت.
- در بریتانیا به رشد و سودآوری بزرگ رسید، ولی تجربهٔ آمریکا را در ۲۰۲۶ بست.

این پرونده دقیقاً پرسش <span dir="ltr">Week 02</span> را زنده می‌کند: **چه کسی مالک تصمیم است، مرزها چگونه اجرا می‌شوند و چه چیزی با زیادکردن <span dir="ltr">Service</span> حل نمی‌شود؟**

## 2. یک سوءبرداشت مهم

<span dir="ltr">Monzo</span> را نباید با <span dir="ltr">Temenos Transact</span>، <span dir="ltr">FLEXCUBE</span>، <span dir="ltr">Finacle</span> یا <span dir="ltr">Mambu</span> یکی گرفت. آن شرکت‌ها <span dir="ltr">Platform/Core Banking</span> را به مؤسسات مختلف عرضه می‌کنند؛ <span dir="ltr">Monzo</span> یک بانک است که بخش بزرگی از <span dir="ltr">Banking platform</span> خود را برای عملیات خودش ساخته است.

بنابراین:

- تعداد <span dir="ltr">Microservice</span>های <span dir="ltr">Monzo</span> الگوی مستقیم برای بانک دیگر نیست.
- نام <span dir="ltr">Service</span>های <span dir="ltr">Monzo</span> معادل <span dir="ltr">Bounded Context</span>های ما نیست.
- موفقیت محصول، درستی تک‌تک <span dir="ltr">Boundary</span>ها را ثابت نمی‌کند.
- شکست <span dir="ltr">Compliance</span> نیز ثابت نمی‌کند <span dir="ltr">Microservices</span> علت آن بوده‌اند.

## 3. تولد: مسئله قبل از فناوری

<span dir="ltr">Monzo</span> در فوریهٔ ۲۰۱۵ با نام **<span dir="ltr">Mondo</span>** شروع شد. ایده فقط ساخت یک <span dir="ltr">Mobile app</span> روی <span dir="ltr">Core</span> قدیمی نبود؛ بنیان‌گذاران می‌خواستند بانک جدیدی بسازند که تجربهٔ مالی آن <span dir="ltr">Real-time</span>، شفاف و قابل کنترل از موبایل باشد. در مرحلهٔ <span dir="ltr">Alpha/Beta</span> از <span dir="ltr">Prepaid card</span> استفاده شد تا پیش از آماده‌شدن <span dir="ltr">Full current account</span>، محصول با مشتری واقعی آزموده شود.

تا اوت ۲۰۱۶ حدود ۳۰ هزار <span dir="ltr">Prepaid card</span> در گردش بود و بیش از ۲۰۰ هزار نفر برای مشارکت در مسیر محصول ثبت‌نام کرده بودند. همان ماه بانک مجوز محدود گرفت و وارد <span dir="ltr">Mobilisation</span> شد؛ مجوز محدود به آن اجازه می‌داد اتصال به <span dir="ltr">Payment network</span> و کنترل‌های عملیاتی را پیش از <span dir="ltr">Launch</span> عمومی آزمایش کند. [اعلام رسمی مجوز محدود و آغاز از فوریهٔ ۲۰۱۵](https://monzo.com/blog/2016/08/11/we-are-now-a-bank)، [توضیح <span dir="ltr">Mobilisation</span> و اتصال به <span dir="ltr">Mastercard</span>، <span dir="ltr">Bacs</span> و <span dir="ltr">Faster Payments</span>](https://monzo.com/blog/2016/08/15/launching-the-bank)

### اولین خطای پرهزینه اما قابل بازیابی: نام

<span dir="ltr">Trademark</span> نام <span dir="ltr">Mondo</span> با چالش حقوقی یک شرکت دیگر روبه‌رو شد. تیم به‌جای دعوای طولانی، <span dir="ltr">Rebrand</span> را انتخاب کرد و پس از دریافت بیش از ۱۲٬۵۰۰ پیشنهاد از جامعه، نام <span dir="ltr">Monzo</span> را برگزید. این خطا معماری نرم‌افزار نبود، اما یک درس معماری سازمانی دارد: **دارایی حیاتی فقط <span dir="ltr">Code</span> و <span dir="ltr">Data</span> نیست؛ <span dir="ltr">Name</span>، <span dir="ltr">License</span>، <span dir="ltr">Contract</span> و <span dir="ltr">Regulatory permission</span> نیز <span dir="ltr">Dependency</span> واقعی‌اند.** [شرح رسمی دلیل تغییر نام](https://monzo.com/blog/2016/08/26/how-we-picked-monzo)، [اعلام نام <span dir="ltr">Monzo</span>](https://monzo.com/blog/2016/08/25/monzo)

## <span dir="ltr">4. Timeline</span> تحول

| دوره | رخداد مستند | تغییر مسئله و <span dir="ltr">Capability</span> |
|---|---|---|
| 2015 | شروع <span dir="ltr">Mondo</span> و ساخت <span dir="ltr">Prepaid beta</span> | آزمون <span dir="ltr">Product/UX</span> و <span dir="ltr">Card processing</span> پیش از بانک کامل |
| 2016 | مجوز بانکی محدود، <span dir="ltr">Mobilisation</span> و تغییر نام به <span dir="ltr">Monzo</span> | ورود جدی <span dir="ltr">Risk</span>، <span dir="ltr">Compliance</span>، <span dir="ltr">Bacs</span>، <span dir="ltr">Faster Payments</span> و <span dir="ltr">Mastercard</span> |
| <span dir="ltr">Apr 2017</span> | رفع محدودیت‌های مجوز و تبدیل به بانک کاملاً مجاز | مسئولیت کامل <span dir="ltr">Current Account</span> و <span dir="ltr">Deposit-taking</span>؛ [اعلام رسمی](https://monzo.com/blog/2017/04/05/banking-licence) |
| <span dir="ltr">Jul</span>–<span dir="ltr">Dec 2017</span> | <span dir="ltr">Rollout</span> تدریجی <span dir="ltr">Current Account</span> و <span dir="ltr">Migration</span> از <span dir="ltr">Prepaid</span> | <span dir="ltr">Account lifecycle</span>، <span dir="ltr">Direct Debit</span>، <span dir="ltr">Standing Order</span>، <span dir="ltr">Overdraft</span> و <span dir="ltr">Migration</span>؛ [برنامهٔ <span dir="ltr">Rollout</span>](https://monzo.com/blog/2017/07/17/current-account-preview) |
| 2018–2019 | عبور از یک میلیون مشتری، <span dir="ltr">Joint account</span>، <span dir="ltr">Apple Pay</span>، <span dir="ltr">Savings partnership</span> و <span dir="ltr">Lending</span>؛ شروع <span dir="ltr">Business Banking</span> | عبور از «کارت خوب» به بانک چندمحصولی؛ [مرور رسمی 2019](https://monzo.com/blog/2019/01/04/monzo-in-2019) |
| 2019 | <span dir="ltr">Launch</span> در آمریکا با <span dir="ltr">Partner bank</span> | آزمون <span dir="ltr">Market/Regulatory model</span> متفاوت؛ [گزارش رسمی 2019](https://monzo.com/blog/2019/06/27/monzo-2019-annual-report) |
| 2020–2022 | رشد بسیار سریع <span dir="ltr">Customer</span> و <span dir="ltr">Product</span>؛ ضعف جدی <span dir="ltr">Financial Crime controls</span> | کنترل‌های <span dir="ltr">Onboarding</span>، <span dir="ltr">Risk assessment</span> و <span dir="ltr">Transaction monitoring</span> از رشد عقب ماندند |
| 2022–2024 | <span dir="ltr">Direct participation</span> در <span dir="ltr">Bacs</span>، <span dir="ltr">International Payments</span>، <span dir="ltr">Investments</span> و رشد <span dir="ltr">Business Banking</span> | افزایش عمق <span dir="ltr">Payment</span>، <span dir="ltr">Wealth</span> و <span dir="ltr">Business capabilities</span> |
| 2024 | حدود ۲۸۰۰ تا ۳۰۰۰ <span dir="ltr">Microservice</span>؛ <span dir="ltr">Migration</span>های سراسری و <span dir="ltr">Rate limiting</span> توزیع‌شده | <span dir="ltr">Platform consistency</span> و <span dir="ltr">Mass change</span> به مسئلهٔ معماری درجه‌اول تبدیل شد |
| 2025 | معرفی <span dir="ltr">Monzo Stand-in</span> و جریمهٔ <span dir="ltr">FCA</span> | <span dir="ltr">Cloud-level resilience</span> رشد کرد؛ در مقابل <span dir="ltr">Debt</span> کنترل مالی رسمی شد |
| 2026 | <span dir="ltr">Migration</span> بیش از ۳۰۰۰ <span dir="ltr">Service</span> به <span dir="ltr">EKS</span>، <span dir="ltr">Launch</span> در <span dir="ltr">Ireland</span> و بستن حساب‌های آمریکا | <span dir="ltr">Platform productization</span>، تمرکز جغرافیایی جدید و خروج از آزمایش آمریکا |

<span dir="ltr">Timeline</span> بالا گزیده است؛ هدف اتصال تحول <span dir="ltr">Capability</span> به تحول معماری است، نه فهرست همهٔ <span dir="ltr">Feature</span>ها.

## 5. معماری نسل اول: <span dir="ltr">Microservice</span> از روز اول

<span dir="ltr">Monzo</span> در ۲۰۱۶ نوشت <span dir="ltr">Backend</span> از ابتدا مجموعه‌ای از <span dir="ltr">Microservice</span>های توزیع‌شده بوده است؛ انتخابی غیرعادی برای <span dir="ltr">Startup.</span> استدلال اصلی، 24×7 بودن، <span dir="ltr">Fault isolation</span>، استقرار سریع و استقلال تیم‌های آینده بود. در شروع فقط سه <span dir="ltr">Backend developer</span> داشتند، اما هنگام <span dir="ltr">Beta</span> تعداد <span dir="ltr">Service</span>ها نزدیک ۱۰۰ و سپس حدود ۱۵۰ شده بود. [شرح معماری اولیه توسط <span dir="ltr">Head of Engineering</span>](https://monzo.com/blog/2016/09/19/building-a-modern-bank-backend)

<span dir="ltr">Technology/architecture</span> اعلام‌شده در آن زمان:

- <span dir="ltr">Go</span> به‌عنوان زبان غالب <span dir="ltr">Service</span>ها
- <span dir="ltr">Containerization</span> با <span dir="ltr">Docker</span>
- مهاجرت از <span dir="ltr">Mesos/Marathon</span> به <span dir="ltr">Kubernetes</span> روی <span dir="ltr">AWS</span>
- <span dir="ltr">RPC</span> برای ارتباط همگام و <span dir="ltr">Linkerd/Finagle</span> در نسل اولیه
- <span dir="ltr">Kafka</span> به‌عنوان <span dir="ltr">Commit log/Message backbone</span> با <span dir="ltr">At-least-once delivery</span> و <span dir="ltr">Replay</span>
- سرویس‌های کوچک برای <span dir="ltr">Shared platform capabilities</span>

### تصمیم درست یا <span dir="ltr">Premature decomposition</span>؟

از دادهٔ عمومی نمی‌توان حکم قطعی داد. این انتخاب دو اثر واقعی داشت:

**سودها**

- تیم‌ها می‌توانستند <span dir="ltr">Build/Deploy/Scale</span> مستقل‌تری داشته باشند.
- <span dir="ltr">Failure isolation</span> و <span dir="ltr">Continuous delivery</span> از ابتدا <span dir="ltr">Design concern</span> شد.
- <span dir="ltr">Event</span> و <span dir="ltr">Replay</span> برای عملیات بانکی بخشی از <span dir="ltr">Platform</span> بود، نه افزونهٔ دیرهنگام.

**هزینه‌ها**

- با تیم کوچک، تعداد <span dir="ltr">Service</span>ها بسیار سریع بالا رفت.
- <span dir="ltr">RPC</span>، <span dir="ltr">Queue</span>، <span dir="ltr">Service discovery</span>، <span dir="ltr">Deployment</span>، <span dir="ltr">Observability</span> و <span dir="ltr">Migration</span> سراسری باید خیلی زود حل می‌شد.
- مرز کوچک <span dir="ltr">Deployment</span> الزاماً مرز دامینی خوب نیست و می‌تواند <span dir="ltr">Cognitive load</span> را زیاد کند.

نتیجه برای <span dir="ltr">Lab</span> ما «از روز اول <span dir="ltr">Microservice</span> بساز» نیست. نتیجه این است که اگر استقلال <span dir="ltr">Deploy</span> را زود انتخاب می‌کنی، باید هزینهٔ <span dir="ltr">Platform</span> و عملیات آن را نیز از روز اول بپردازی.

## 6. معماری در مقیاس: استانداردسازی برای مهار توزیع

تا ۲۰۲۴ <span dir="ltr">Monzo</span> از ۲۸۰۰ تا بیش از ۳۰۰۰ <span dir="ltr">Microservice</span> حرف می‌زد. نکتهٔ مهم این نیست که عدد بزرگ تحسین شود؛ مهم این است که چنین عددی چه <span dir="ltr">Governance</span>ای طلب می‌کند.

در پروندهٔ <span dir="ltr">Migration</span> از <span dir="ltr">OpenTracing</span> به <span dir="ltr">OpenTelemetry</span>، <span dir="ltr">Monzo</span> چند قابلیت کلیدی را اعلام کرد:

- همهٔ <span dir="ltr">Service</span>های مورد بحث با <span dir="ltr">Go</span> و <span dir="ltr">Technology version</span> سازگار ساخته شده‌اند.
- کد <span dir="ltr">Service</span>ها در یک <span dir="ltr">Monorepo</span> است.
- <span dir="ltr">CI</span> با ابزارهایی مانند <span dir="ltr">Semgrep Convention</span>ها را سراسری <span dir="ltr">enforce</span> می‌کند.
- <span dir="ltr">Mass deployment</span> و <span dir="ltr">Automated rollback</span> وجود دارد.
- <span dir="ltr">Config service</span> امکان <span dir="ltr">Roll-forward</span> تدریجی و <span dir="ltr">Rollback</span> سریع را می‌دهد.
- <span dir="ltr">Migration</span> بزرگ به‌صورت مرکزی هدایت می‌شود، زیرا واگذاری کامل به <span dir="ltr">Owner</span>های پراکنده قبلاً <span dir="ltr">Migration</span>های نیمه‌تمام و <span dir="ltr">Coordination cost</span> ایجاد کرده بود. [شرح <span dir="ltr">Migration</span> در ۲۸۰۰ <span dir="ltr">Microservice</span>](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)

این یک <span dir="ltr">Trade-off</span> جالب <span dir="ltr">Ownership</span> است:


</div>

<div dir="ltr" align="left">

```text
product behavior ownership       → decentralized squads
cross-cutting platform migration → centrally driven platform team
```

</div>

<div dir="rtl" align="right">


<span dir="ltr">Ownership</span> همیشه به معنی «هر تیم هر کاری خواست» نیست. استاندارد مشترک و تغییر سراسری نیز <span dir="ltr">Owner</span> لازم دارد.

## 7. معماری جاریِ قابل اثبات در ۲۰۲۶

جدول زیر فقط مواردی را قطعی می‌داند که در منابع رسمی ۲۰۲۴ تا ۲۰۲۶ آمده‌اند:

| حوزه | آنچه عمومی و قابل اثبات است | سطح اطمینان |
|---|---|---|
| <span dir="ltr">Service architecture</span> | بیش از ۳۰۰۰ <span dir="ltr">Microservice</span>؛ <span dir="ltr">Backend</span>ها در <span dir="ltr">Monorepo</span> و <span dir="ltr">Common patterns</span> | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Application language</span> | نوشتهٔ <span dir="ltr">Migration</span> ۲۰۲۴ می‌گوید <span dir="ltr">Service</span>های آن‌ها با <span dir="ltr">Go</span> نوشته شده‌اند | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span>، <span dir="ltr">scope</span> همان <span dir="ltr">Backend fleet</span> |
| <span dir="ltr">Container platform</span> | <span dir="ltr">Kubernetes</span>؛ <span dir="ltr">Workload</span>ها از <span dir="ltr">Self-hosted Kubernetes</span> به <span dir="ltr">Amazon EKS</span> مهاجرت کرده‌اند | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Primary cloud</span> | <span dir="ltr">Primary Platform</span> روی <span dir="ltr">AWS</span> | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Stand-in cloud</span> | <span dir="ltr">Stand-in</span> مستقل روی <span dir="ltr">GCP</span> با حدود ۱۸ <span dir="ltr">Service</span> | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Async/event</span> | <span dir="ltr">Kafka</span> در <span dir="ltr">Platform</span> اصلی؛ <span dir="ltr">GCP Pub/Sub</span> برای <span dir="ltr">Advice</span>های <span dir="ltr">Stand-in</span> | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Platform interface</span> | <span dir="ltr">Platform operation</span>ها پشت <span dir="ltr">Service/API</span>های <span dir="ltr">opinionated</span>، با <span dir="ltr">Multi-party authorization</span> برای عملیات حساس | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Observability/migration</span> | <span dir="ltr">Central metrics/logging</span>، <span dir="ltr">OpenTelemetry migration</span>، <span dir="ltr">automated health checks</span> و <span dir="ltr">rollback</span> | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Analytics</span> | <span dir="ltr">BigQuery</span> + <span dir="ltr">dbt</span>؛ بیش از سه میلیارد <span dir="ltr">Analytics event</span> در روز در گزارش ۲۰۲۴ | <span dir="ltr">FACT</span> — <span dir="ltr">primary</span> |
| <span dir="ltr">Primary operational datastore</span> | نام فعلی در منابع بررسی‌شده اعلام نشده؛ مقالهٔ ۲۰۲۴ فقط از <span dir="ltr">Migration</span> پایگاه <span dir="ltr">Core</span> حرف می‌زند | <span dir="ltr">UNKNOWN</span> |
| <span dir="ltr">Historic datastore</span> | <span dir="ltr">Cassandra</span> در منابع قدیمی <span dir="ltr">Monzo</span> و آگهی‌های فنی آمده است، اما این پرونده آن را <span dir="ltr">Database</span> قطعی ۲۰۲۶ اعلام نمی‌کند | <span dir="ltr">HISTORIC FACT</span> / <span dir="ltr">CURRENT UNKNOWN</span> |
| <span dir="ltr">Exact Bounded Context map</span> | عمومی نشده است | <span dir="ltr">UNKNOWN</span> |

منابع: [<span dir="ltr">Platform engineering</span> و <span dir="ltr">Migration</span> بیش از ۳۰۰۰ <span dir="ltr">Service</span> به <span dir="ltr">EKS</span> در ۲۰۲۶](https://monzo.com/blog/the-engineering-behind-the-platform)، [<span dir="ltr">Scale</span> و <span dir="ltr">Migration</span> در ۲۰۲۴](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)، [<span dir="ltr">Data platform</span> و سه میلیارد <span dir="ltr">Event</span> روزانه](https://monzo.com/blog/how-we-use-incremental-modelling-to-handle-billions-of-events-every-day)

## <span dir="ltr">8. Monzo Stand-in:</span> تاب‌آوری با استقلال، نه <span dir="ltr">Clone</span> کامل

یکی از مهم‌ترین دستاوردهای معماری <span dir="ltr">Monzo</span>، **<span dir="ltr">Stand-in</span>** است. <span dir="ltr">Primary Platform</span> روی <span dir="ltr">AWS</span> حدود ۳۰۰۰ <span dir="ltr">Microservice</span> دارد؛ <span dir="ltr">Stand-in</span> روی <span dir="ltr">GCP</span> فقط ۱۸ <span dir="ltr">Service</span> مستقل دارد و برای خرابی بزرگ، <span dir="ltr">Capability</span>های حیاتی زیر را نگه می‌دارد:

- <span dir="ltr">Card spend</span> و <span dir="ltr">Cash withdrawal</span>
- <span dir="ltr">Bank transfer</span>های اصلی
- مشاهدهٔ <span dir="ltr">Balance</span> و <span dir="ltr">Transaction</span>
- <span dir="ltr">Freeze/Unfreeze card</span>

<span dir="ltr">Stand-in</span> کپی کامل <span dir="ltr">Primary</span> نیست. <span dir="ltr">Software</span>، <span dir="ltr">Service</span>ها و <span dir="ltr">Cloud</span> جدا هستند تا یک <span dir="ltr">Bug</span> یا <span dir="ltr">Process failure</span> مشترک هر دو را هم‌زمان از کار نیندازد. داده از <span dir="ltr">Primary</span> به <span dir="ltr">Stand-in</span> به‌صورت <span dir="ltr">Non-blocking</span> و <span dir="ltr">Eventually consistent</span> می‌رود. <span dir="ltr">Stand-in</span> هنگام فعال‌بودن <span dir="ltr">Decision</span>های خودش را می‌گیرد و نتیجه را به شکل <span dir="ltr">Advice durable</span> برای <span dir="ltr">Primary</span> ثبت می‌کند؛ <span dir="ltr">Primary</span> پس از بازیابی، این <span dir="ltr">Effects</span> را اعمال و با <span dir="ltr">Correlation ID</span> تطبیق می‌دهد. <span dir="ltr">Primary</span> همچنان <span dir="ltr">System of Record</span> باقی می‌ماند. [شرح کامل <span dir="ltr">Stand-in</span> توسط <span dir="ltr">Monzo</span>](https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in)

### <span dir="ltr">Trade-off</span> آگاهانه

<span dir="ltr">Monzo</span> صریحاً می‌پذیرد که <span dir="ltr">Stand-in</span> ممکن است با <span dir="ltr">View</span> کمی قدیمی، پرداختی را تأیید کند که <span dir="ltr">Primary</span> آن را <span dir="ltr">Insufficient funds</span> می‌داند؛ نتیجه می‌تواند <span dir="ltr">Unapproved overdraft</span> باشد. این ریسک با <span dir="ltr">Control</span> و <span dir="ltr">Reconciliation</span> مدیریت می‌شود، نه با ادعای <span dir="ltr">Consistency</span> کامل.

درس معماری:

> <span dir="ltr">Availability</span> بالا همیشه حاصل <span dir="ltr">Replication</span> کامل نیست؛ گاهی حاصل کاهش <span dir="ltr">Scope</span>، استقلال <span dir="ltr">Failure mode</span> و پذیرش آگاهانهٔ <span dir="ltr">Consistency</span> محدود است.

## <span dir="ltr">9. Domain/Capability map</span> تحلیلی

<span dir="ltr">Monzo</span> نقشهٔ رسمی <span dir="ltr">Bounded Context</span>های خود را عمومی نکرده است. جدول زیر از <span dir="ltr">Product</span>ها، گزارش مالی و نوشته‌های فنی **استنتاج** شده و نباید به‌عنوان ساختار داخلی قطعی بازنشر شود.

| <span dir="ltr">Capability cluster</span> | شواهد عمومی | فرضیهٔ <span dir="ltr">Ownership</span> |
|---|---|---|
| <span dir="ltr">Party</span>, <span dir="ltr">Customer</span> & <span dir="ltr">Onboarding</span> | <span dir="ltr">Account signup</span>، <span dir="ltr">KYC</span> و <span dir="ltr">FCA findings</span> | هویت، <span dir="ltr">Eligibility</span> و <span dir="ltr">Customer risk</span> باید <span dir="ltr">Authority</span> روشن داشته باشد |
| <span dir="ltr">Accounts</span> & <span dir="ltr">Deposits</span> | <span dir="ltr">Current account</span>، <span dir="ltr">Joint</span>، <span dir="ltr">Under-16</span>، <span dir="ltr">Pots</span> و £<span dir="ltr">25.7bn deposits</span> در <span dir="ltr">FY2026</span> | <span dir="ltr">Operational account state</span> و <span dir="ltr">available balance</span> در <span dir="ltr">Banking platform</span> |
| <span dir="ltr">Cards</span> & <span dir="ltr">Cash</span> | <span dir="ltr">Mastercard</span>، <span dir="ltr">ATM</span>، <span dir="ltr">freeze/unfreeze</span> و <span dir="ltr">Stand-in card processor</span> | <span dir="ltr">Card lifecycle</span> و <span dir="ltr">Authorization</span> جدا از <span dir="ltr">Channel UI</span> |
| <span dir="ltr">Payments</span> | <span dir="ltr">Faster Payments</span>، <span dir="ltr">Bacs</span>، <span dir="ltr">Direct Debit</span>، <span dir="ltr">SWIFT/International payments</span> | <span dir="ltr">Payment instruction</span>، <span dir="ltr">processing state</span>، <span dir="ltr">scheme adapter</span> و <span dir="ltr">reconciliation</span> |
| <span dir="ltr">Ledger</span> & <span dir="ltr">Balance</span> | <span dir="ltr">Stand-in</span> مقاله صریحاً از <span dir="ltr">Ledger</span> و <span dir="ltr">System of Record</span> حرف می‌زند | <span dir="ltr">Primary Ledger Authority</span>؛ <span dir="ltr">Stand-in decision/effect</span> موقت و <span dir="ltr">reconciled</span> |
| <span dir="ltr">Borrowing</span> | <span dir="ltr">Loan</span>، <span dir="ltr">Overdraft</span> و <span dir="ltr">Flex</span> | <span dir="ltr">Credit decision</span>، <span dir="ltr">agreement</span> و <span dir="ltr">servicing</span> با <span dir="ltr">Lifecycle</span> مستقل |
| <span dir="ltr">Savings</span> & <span dir="ltr">Wealth</span> | <span dir="ltr">Savings</span>، <span dir="ltr">ISA</span>، <span dir="ltr">Investments</span> و <span dir="ltr">Pensions</span> | <span dir="ltr">Product/partner orchestration</span> و <span dir="ltr">customer holdings</span> |
| <span dir="ltr">Business Banking</span> | <span dir="ltr">Business current account</span>، <span dir="ltr">invoicing</span> و <span dir="ltr">expense cards</span> | <span dir="ltr">Party/business relationship</span> و <span dir="ltr">entitlements</span> چندکاربره |
| <span dir="ltr">Financial Crime</span> & <span dir="ltr">Fraud</span> | <span dir="ltr">Customer risk assessment</span>، <span dir="ltr">transaction monitoring</span>، <span dir="ltr">fraud controls</span> | <span dir="ltr">Policy/decision ownership</span> باید همگام با <span dir="ltr">Product growth</span> مقیاس بگیرد |
| <span dir="ltr">Customer Operations</span> | <span dir="ltr">Support</span> و <span dir="ltr">Ops Agent</span> | <span dir="ltr">Case/operation workflows</span> بدون تصاحب <span dir="ltr">Source of Truth</span> دامین‌ها |
| <span dir="ltr">Platform</span> & <span dir="ltr">Reliability</span> | <span dir="ltr">Kubernetes</span>، <span dir="ltr">EKS</span>، <span dir="ltr">deployment</span>، <span dir="ltr">MPA</span>، <span dir="ltr">Stand-in</span> | <span dir="ltr">Internal platform product</span> با <span dir="ltr">API</span> و <span dir="ltr">Owner</span> مستقل |
| <span dir="ltr">Data</span> & <span dir="ltr">Analytics</span> | <span dir="ltr">BigQuery</span>، <span dir="ltr">dbt</span> و <span dir="ltr">event ingestion</span> | <span dir="ltr">Analytical projection</span>؛ نه مالک <span dir="ltr">Operational facts</span> |

نکتهٔ <span dir="ltr">Week 02:</span> وجود ۳۰۰۰ <span dir="ltr">Service</span> به معنی ۳۰۰۰ <span dir="ltr">Domain</span> نیست. بسیاری <span dir="ltr">Platform service</span>، <span dir="ltr">Adapter</span>، <span dir="ltr">Workflow step</span> یا <span dir="ltr">Technical capability</span> هستند.

## 10. اشتباه‌ها و شرط‌بندی‌های ناموفق

### <span dir="ltr">10.1 Financial Crime controls</span> از رشد عقب ماند

<span dir="ltr">FCA</span> در ژوئیهٔ ۲۰۲۵ <span dir="ltr">Monzo</span> را ۲۱٬۰۹۱٬۳۰۰ پوند جریمه کرد. تخلف‌های اعلام‌شده شامل ناکافی‌بودن سیستم‌ها و کنترل‌های <span dir="ltr">Financial Crime</span> بین اکتبر ۲۰۱۸ تا اوت ۲۰۲۰ و نقض مکرر محدودیت <span dir="ltr">Onboarding</span> مشتریان <span dir="ltr">High-risk</span> بین اوت ۲۰۲۰ تا ژوئن ۲۰۲۲ بود. <span dir="ltr">FCA</span> گفت <span dir="ltr">Customer base</span> از حدود ۶۰۰ هزار در ۲۰۱۸ به بیش از ۵.۸ میلیون در ۲۰۲۲ رسید، اما کنترل‌ها هم‌پای رشد نکردند؛ بیش از ۳۴ هزار <span dir="ltr">High-risk customer</span> برخلاف <span dir="ltr">Requirement</span> ثبت شدند. <span dir="ltr">Monzo</span> پس از <span dir="ltr">Review</span> مستقل، <span dir="ltr">Change programme</span> مربوط را تکمیل کرد. [اعلام و جزئیات رسمی <span dir="ltr">FCA</span>](https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls)

این <span dir="ltr">Failure</span> را نباید به «<span dir="ltr">Bug</span> یک <span dir="ltr">Microservice</span>» تقلیل داد. حداقل چهار مالکیت باید هم‌راستا می‌بود:

- <span dir="ltr">Product growth</span> و <span dir="ltr">Onboarding flow</span>
- <span dir="ltr">Customer risk policy</span>
- <span dir="ltr">Transaction monitoring capability</span>
- <span dir="ltr">Regulatory control</span>، <span dir="ltr">evidence</span> و <span dir="ltr">change governance</span>

درس: **<span dir="ltr">Compliance</span> یک <span dir="ltr">Non-functional afterthought</span> نیست؛ مجموعه‌ای از <span dir="ltr">Capability</span>، <span dir="ltr">Decision owner</span>، <span dir="ltr">Data quality</span>، <span dir="ltr">Control loop</span> و <span dir="ltr">Evidence</span> است.**

### <span dir="ltr">10.2 Microservice scale</span> خودش مسئله ساخت

<span dir="ltr">Monzo</span> در ۲۰۲۴ صریحاً نوشت معماری ۲۸۰۰ <span dir="ltr">Service</span> ارزش زیادی داده، اما <span dir="ltr">Migration</span> سراسری را دشوار کرده است. تجربهٔ <span dir="ltr">Decentralized migration</span> نیز به کار نیمه‌تمام و <span dir="ltr">Coordination</span> زیاد منجر شده بود؛ برای همین <span dir="ltr">Standardization</span>، <span dir="ltr">Monorepo</span>، <span dir="ltr">central tooling</span> و <span dir="ltr">centrally driven migration</span> تقویت شد. [منبع رسمی <span dir="ltr">Migration</span>](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)

این «اثبات شکست <span dir="ltr">Microservices</span>» نیست؛ اثبات این است که استقلال زیاد بدون <span dir="ltr">Platform governance</span> پایدار نمی‌ماند.

### 10.3 آزمایش آمریکا پایان یافت

<span dir="ltr">Monzo</span> در ۲۰۱۹ با <span dir="ltr">Partner bank</span> وارد آمریکا شد، اما از ۸ ژوئن ۲۰۲۶ همهٔ حساب‌های آمریکا بسته شدند و شرکت تمرکز خود را بر <span dir="ltr">UK</span> و <span dir="ltr">Europe</span> گذاشت. <span dir="ltr">Monzo</span> در صفحهٔ رسمی <span dir="ltr">Closure</span> دلیل فنی یا شکست معماری واحدی اعلام نمی‌کند؛ بنابراین پرونده نیز علت‌سازی نمی‌کند. <span dir="ltr">Fact</span> قطعی، پایان <span dir="ltr">Product/market experiment</span> است. [اطلاعیهٔ رسمی بستن حساب‌های آمریکا](https://monzo.com/help/us-account-closure-support/us-account-closure-support)

درس: <span dir="ltr">Technology reuse</span> به‌تنهایی <span dir="ltr">Product-market fit</span>، <span dir="ltr">Regulation</span>، <span dir="ltr">Payment rails</span> و <span dir="ltr">Unit economics</span> بازار جدید را حل نمی‌کند.

### <span dir="ltr">10.4 Self-hosted Kubernetes</span> تا <span dir="ltr">EKS</span>

در ۲۰۱۶ اجرای <span dir="ltr">Highly available Kubernetes</span> روی <span dir="ltr">AWS</span> را دشوار اما ارزشمند توصیف کردند. در ۲۰۲۶ اعلام شد بیش از ۳۰۰۰ <span dir="ltr">Service</span> از <span dir="ltr">Self-hosted Kubernetes</span> به <span dir="ltr">EKS</span> مهاجرت کرده‌اند. این را نباید بدون شواهد «اشتباه اولیه» نامید؛ در ۲۰۱۶ <span dir="ltr">Managed option</span> امروز وجود نداشت. این یک نمونهٔ <span dir="ltr">Revisit architecture decision</span> با تغییر <span dir="ltr">Technology landscape</span> است.

## 11. دستاوردهای تازه تا <span dir="ltr">FY2026</span>

### <span dir="ltr">Business/Product</span>

گزارش سال مالی ۲۰۲۶ <span dir="ltr">Monzo</span> ارقام زیر را منتشر کرده است:

- درآمد ۱.۷ میلیارد پوند
- <span dir="ltr">Adjusted profit before tax</span> برابر ۱۷۲.۶ میلیون پوند
- سپردهٔ مشتریان ۲۵.۷ میلیارد پوند
- ۱۵.۲ میلیون مشتری و ۱۰.۴ میلیون <span dir="ltr">Monthly active user</span>
- ۷۳ میلیارد پوند <span dir="ltr">Card spend</span>
- رشد ۴۵ درصدی <span dir="ltr">Business banking customers</span>
- <span dir="ltr">Launch</span> در <span dir="ltr">Ireland</span>

[<span dir="ltr">Monzo FY2026 Annual Report summary</span>](https://monzo.com/annual-report)

### <span dir="ltr">Technology/Architecture</span>

- <span dir="ltr">Stand-in</span> مستقل روی <span dir="ltr">GCP</span> برای <span dir="ltr">Critical banking capabilities</span>
- <span dir="ltr">Migration</span> خودکار بیش از ۳۰۰۰ <span dir="ltr">Microservice</span> به <span dir="ltr">EKS</span>، همراه با <span dir="ltr">Health check</span> و <span dir="ltr">Rollback</span>؛ حتی <span dir="ltr">Migrator service</span> خودش را مهاجرت کرد
- <span dir="ltr">Platform operation</span>ها به‌صورت <span dir="ltr">API/Service</span> با <span dir="ltr">Multi-party authorization</span>، به‌جای <span dir="ltr">Runbook</span> و <span dir="ltr">Script</span> دستی
- <span dir="ltr">Standardized Go/Monorepo estate</span> برای <span dir="ltr">Migration</span>های سراسری و کنترل <span dir="ltr">Convention</span>

این دستاوردها نشان می‌دهند <span dir="ltr">Platform engineering</span> در بانک فقط «زیرساخت» نیست؛ یک <span dir="ltr">Product</span> داخلی با <span dir="ltr">API</span>، <span dir="ltr">User</span>، <span dir="ltr">Ownership</span>، <span dir="ltr">Test</span> و <span dir="ltr">Control</span> است.

## 12. ارزیابی معماری

### نقاط قوت

1. **<span dir="ltr">Boundary</span> اجرایی واقعی:** <span dir="ltr">Service</span>ها <span dir="ltr">Build/Deploy/Scale</span> مستقل دارند.
2. **<span dir="ltr">Platform as product:</span>** عملیات حساس پشت <span dir="ltr">API</span> و <span dir="ltr">Approval</span> قرار گرفته است.
3. **<span dir="ltr">Change at scale:</span>** <span dir="ltr">Monorepo</span> و <span dir="ltr">Standard stack</span> امکان <span dir="ltr">Refactor</span> سراسری می‌دهند.
4. **<span dir="ltr">Event-driven durability:</span>** <span dir="ltr">Replay</span>، <span dir="ltr">At-least-once</span> و <span dir="ltr">Advice log</span> از ابتدا/در تاب‌آوری مهم‌اند.
5. **<span dir="ltr">Failure diversity:</span>** <span dir="ltr">Stand-in</span> همان <span dir="ltr">Software</span> را در <span dir="ltr">Cloud</span> دوم کپی نمی‌کند.
6. **<span dir="ltr">Transparency:</span>** بسیاری از <span dir="ltr">Trade-off</span>ها و محدودیت‌ها عمومی نوشته شده‌اند.

### هزینه‌ها و ریسک‌ها

1. ۳۰۰۰ <span dir="ltr">Service</span> نیازمند <span dir="ltr">Platform team</span> و <span dir="ltr">Automation</span> در سطح بسیار بالا هستند.
2. <span dir="ltr">Deployment boundary</span>های ریز می‌توانند <span dir="ltr">Runtime coupling</span> و <span dir="ltr">Cognitive load</span> بسازند.
3. <span dir="ltr">Consistency</span> و <span dir="ltr">Authority</span> در <span dir="ltr">Stand-in</span> نیازمند <span dir="ltr">Advice</span>، <span dir="ltr">Correlation</span> و <span dir="ltr">Reconciliation</span> دقیق است.
4. <span dir="ltr">Technology excellence</span> جای <span dir="ltr">Financial Crime control</span> و <span dir="ltr">Regulatory ownership</span> را نمی‌گیرد.
5. <span dir="ltr">Standardization</span> برای <span dir="ltr">Migration</span> سراسری، بخشی از آزادی تکنولوژیک تیم‌ها را محدود می‌کند.

## 13. چه چیزی را برای <span dir="ltr">Core Banking Lab</span> خودمان می‌گیریم؟

### می‌گیریم

- هر <span dir="ltr">Module/Context API</span> آشکار و <span dir="ltr">Internal implementation</span> محافظت‌شده داشته باشد.
- <span dir="ltr">Product team autonomy</span> همراه <span dir="ltr">Platform standards</span> و <span dir="ltr">Architecture fitness test</span> باشد.
- <span dir="ltr">Event delivery</span> با <span dir="ltr">Duplicate</span> و <span dir="ltr">Replay</span> طراحی شود، نه <span dir="ltr">Happy path.</span>
- <span dir="ltr">Analytical data</span> را با <span dir="ltr">Operational Source of Truth</span> اشتباه نگیریم.
- <span dir="ltr">Compliance/Fraud</span> را <span dir="ltr">Capability</span> و <span dir="ltr">Owner</span> واقعی بدانیم.
- برای <span dir="ltr">Critical flow</span>، <span dir="ltr">Minimal viable continuity</span> را از <span dir="ltr">Full duplicate</span> جدا کنیم.
- تصمیم‌های <span dir="ltr">Technology</span> با <span dir="ltr">Revisit trigger</span> تاریخ‌دار باشند.

### فعلاً نمی‌گیریم

- <span dir="ltr">Microservice</span> از روز اول
- <span dir="ltr">Database/Queue</span> برای هر <span dir="ltr">Package</span>
- سه‌هزار <span dir="ltr">Deployable component</span>
- <span dir="ltr">Multi-cloud</span> قبل از داشتن <span dir="ltr">SLO</span> و <span dir="ltr">Failure model</span>
- <span dir="ltr">Eventual consistency</span> برای <span dir="ltr">Ledger</span> اصلی
- تقلید <span dir="ltr">Stack</span> بدون <span dir="ltr">Team/Scale/Regulatory context</span>

تصمیم <span dir="ltr">Lab</span> همچنان درست است: ابتدا <span dir="ltr">Modular Monolith</span>، سپس استخراج فقط با <span dir="ltr">Evidence.</span>

## 14. پنج سؤال دفاعی

1. چرا ۳۰۰۰ <span dir="ltr">Microservice</span> را نمی‌توان معادل ۳۰۰۰ <span dir="ltr">Bounded Context</span> دانست؟
2. <span dir="ltr">Monorepo</span> و <span dir="ltr">Migration</span> مرکزی چگونه با <span dir="ltr">Team autonomy</span> جمع می‌شوند؟
3. در <span dir="ltr">Stand-in</span>، <span dir="ltr">Owner</span> نهایی <span dir="ltr">Balance</span> و <span dir="ltr">Ledger</span> کیست و <span dir="ltr">Stand-in</span> چه چیزی را موقتاً <span dir="ltr">Authority</span> می‌گیرد؟
4. شکست <span dir="ltr">Financial Crime</span> بیشتر شکست <span dir="ltr">Technology</span> بود، <span dir="ltr">Ownership</span> بود یا <span dir="ltr">Governance</span>؟ با شواهد دفاع کن.
5. اگر <span dir="ltr">Monzo</span> را برای بانک بزرگ خودت الگو بگیری، کدام تصمیم را <span dir="ltr">Copy</span> نمی‌کنی و چرا؟

## <span dir="ltr">15. Artifact</span> چهل‌وپنج‌دقیقه‌ای

[<span dir="ltr">Day 09 Architecture Review</span>](../exercises/day-09-monzo-architecture-review.md) را کامل کن. خروجی باید یک صفحه باشد و شامل این سه بخش:

1. یک <span dir="ltr">Timeline</span> پنج‌نقطه‌ای
2. یک جدول <span dir="ltr">`Fact / Inference / Unknown`</span>
3. یک <span dir="ltr">ADR-lite:</span> «آیا <span dir="ltr">Core Banking Lab</span> باید <span dir="ltr">Microservice-first</span> شود؟»

## <span dir="ltr">16. Source register</span>

### تاریخ و محصول

- [<span dir="ltr">We Are Now a Bank</span> — 2016](https://monzo.com/blog/2016/08/11/we-are-now-a-bank)
- [<span dir="ltr">Launching the Bank</span> — <span dir="ltr">Mobilisation</span>](https://monzo.com/blog/2016/08/15/launching-the-bank)
- [<span dir="ltr">Welcome to Monzo Bank</span> — <span dir="ltr">unrestricted licence</span>, 2017](https://monzo.com/blog/2017/04/05/banking-licence)
- [<span dir="ltr">Monzo in 2019</span>](https://monzo.com/blog/2019/01/04/monzo-in-2019)
- [<span dir="ltr">FY2026 Annual Report</span>](https://monzo.com/annual-report)
- [<span dir="ltr">US account closure</span> — 2026](https://monzo.com/help/us-account-closure-support/us-account-closure-support)

### فناوری و معماری

- [<span dir="ltr">Building a Modern Bank Backend</span> — 2016](https://monzo.com/blog/2016/09/19/building-a-modern-bank-backend)
- [<span dir="ltr">How we run migrations across 2</span>,<span dir="ltr">800 microservices</span> — 2024](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)
- [<span dir="ltr">Tolerating full cloud outages with Monzo Stand-in</span> — 2025](https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in)
- [<span dir="ltr">The Engineering Behind the Platform</span> — 2026](https://monzo.com/blog/the-engineering-behind-the-platform)
- [<span dir="ltr">Incremental modelling and billions of events</span> — 2024](https://monzo.com/blog/how-we-use-incremental-modelling-to-handle-billions-of-events-every-day)

### شکست و کنترل

- [<span dir="ltr">FCA fine and findings</span> — 2025](https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls)

## 17. محدودیت پرونده

- <span dir="ltr">Source code</span>، <span dir="ltr">Service catalog</span>، <span dir="ltr">Data model</span> و <span dir="ltr">Context map</span> کامل <span dir="ltr">Monzo</span> عمومی نیست.
- عدد <span dir="ltr">Service</span>ها در زمان‌های مختلف ۲۸۰۰، نزدیک ۳۰۰۰ و بیش از ۳۰۰۰ گزارش شده؛ این تفاوت <span dir="ltr">Timeline</span> رشد است، نه تناقضی که باید با یک عدد ثابت پنهان شود.
- <span dir="ltr">Product list</span> را نباید <span dir="ltr">Bounded Context list</span> فرض کرد.
- <span dir="ltr">Current primary database technology</span> در منابع رسمی بررسی‌شده نام‌گذاری نشده است.
- تحلیل‌های «چرا آمریکا موفق نشد» بدون منبع رسمی در این پرونده عمداً حذف شده‌اند.

</div>
