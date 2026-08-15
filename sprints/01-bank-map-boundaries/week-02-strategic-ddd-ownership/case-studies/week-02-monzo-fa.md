<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# پروندهٔ <bdi dir="ltr">Week 02</bdi> — <bdi dir="ltr">Monzo</bdi>؛ از <bdi dir="ltr">Mondo</bdi> تا بانک ۳۰۰۰+ <bdi dir="ltr">Microservice</bdi>

- <bdi dir="ltr">Case type:</bdi> بانک دیجیتال با <bdi dir="ltr">Core Banking</bdi> داخلی؛ نه محصول <bdi dir="ltr">Core Banking</bdi> قابل خرید
- <bdi dir="ltr">Relevance: Strategic DDD</bdi>، <bdi dir="ltr">Ownership</bdi>، <bdi dir="ltr">Team autonomy</bdi>، <bdi dir="ltr">Platform engineering</bdi> و هزینهٔ مرزهای بسیار ریز
- <bdi dir="ltr">Evidence checked: 15 August 2026</bdi>
- <bdi dir="ltr">Reading/analysis budget: 45 minutes</bdi>
- <bdi dir="ltr">Evidence rule: Fact</bdi>های جاری از منابع رسمی <bdi dir="ltr">Monzo</bdi> یا <bdi dir="ltr">FCA</bdi>؛ <bdi dir="ltr">Domain map</bdi> این پرونده یک <bdi dir="ltr">Inference</bdi> تحلیلی است.

## 1. چرا <bdi dir="ltr">Monzo</bdi> برای <bdi dir="ltr">Week 02</bdi>؟

<bdi dir="ltr">Monzo</bdi> نمونهٔ سادهٔ «<bdi dir="ltr">Cloud</bdi> خوب، <bdi dir="ltr">Mainframe</bdi> بد» نیست. داستان آن تضادهای مهم‌تری دارد:

- با سه <bdi dir="ltr">Backend developer</bdi>، از روز اول <bdi dir="ltr">Microservice-first</bdi> شد.
- برای استقلال تیم‌ها و استقرار مستقل طراحی کرد، اما بعدها باید بیش از ۳۰۰۰ <bdi dir="ltr">Service</bdi> را استاندارد، مهاجرت و کنترل می‌کرد.
- معماری بسیار مدرن مانع عقب‌ماندن کنترل‌های <bdi dir="ltr">Financial Crime</bdi> از رشد نشد.
- برای تحمل خرابی کامل <bdi dir="ltr">Cloud</bdi>، یک <bdi dir="ltr">Stand-in</bdi> مستقل و کوچک در <bdi dir="ltr">Cloud</bdi> دوم ساخت.
- در بریتانیا به رشد و سودآوری بزرگ رسید، ولی تجربهٔ آمریکا را در ۲۰۲۶ بست.

این پرونده دقیقاً پرسش <bdi dir="ltr">Week 02</bdi> را زنده می‌کند: **چه کسی مالک تصمیم است، مرزها چگونه اجرا می‌شوند و چه چیزی با زیادکردن <bdi dir="ltr">Service</bdi> حل نمی‌شود؟**

## 2. یک سوءبرداشت مهم

<bdi dir="ltr">Monzo</bdi> را نباید با <bdi dir="ltr">Temenos Transact</bdi>، <bdi dir="ltr">FLEXCUBE</bdi>، <bdi dir="ltr">Finacle</bdi> یا <bdi dir="ltr">Mambu</bdi> یکی گرفت. آن شرکت‌ها <bdi dir="ltr">Platform/Core Banking</bdi> را به مؤسسات مختلف عرضه می‌کنند؛ <bdi dir="ltr">Monzo</bdi> یک بانک است که بخش بزرگی از <bdi dir="ltr">Banking platform</bdi> خود را برای عملیات خودش ساخته است.

بنابراین:

- تعداد <bdi dir="ltr">Microservice</bdi>های <bdi dir="ltr">Monzo</bdi> الگوی مستقیم برای بانک دیگر نیست.
- نام <bdi dir="ltr">Service</bdi>های <bdi dir="ltr">Monzo</bdi> معادل <bdi dir="ltr">Bounded Context</bdi>های ما نیست.
- موفقیت محصول، درستی تک‌تک <bdi dir="ltr">Boundary</bdi>ها را ثابت نمی‌کند.
- شکست <bdi dir="ltr">Compliance</bdi> نیز ثابت نمی‌کند <bdi dir="ltr">Microservices</bdi> علت آن بوده‌اند.

## 3. تولد: مسئله قبل از فناوری

<bdi dir="ltr">Monzo</bdi> در فوریهٔ ۲۰۱۵ با نام **<bdi dir="ltr">Mondo</bdi>** شروع شد. ایده فقط ساخت یک <bdi dir="ltr">Mobile app</bdi> روی <bdi dir="ltr">Core</bdi> قدیمی نبود؛ بنیان‌گذاران می‌خواستند بانک جدیدی بسازند که تجربهٔ مالی آن <bdi dir="ltr">Real-time</bdi>، شفاف و قابل کنترل از موبایل باشد. در مرحلهٔ <bdi dir="ltr">Alpha/Beta</bdi> از <bdi dir="ltr">Prepaid card</bdi> استفاده شد تا پیش از آماده‌شدن <bdi dir="ltr">Full current account</bdi>، محصول با مشتری واقعی آزموده شود.

تا اوت ۲۰۱۶ حدود ۳۰ هزار <bdi dir="ltr">Prepaid card</bdi> در گردش بود و بیش از ۲۰۰ هزار نفر برای مشارکت در مسیر محصول ثبت‌نام کرده بودند. همان ماه بانک مجوز محدود گرفت و وارد <bdi dir="ltr">Mobilisation</bdi> شد؛ مجوز محدود به آن اجازه می‌داد اتصال به <bdi dir="ltr">Payment network</bdi> و کنترل‌های عملیاتی را پیش از <bdi dir="ltr">Launch</bdi> عمومی آزمایش کند. [اعلام رسمی مجوز محدود و آغاز از فوریهٔ ۲۰۱۵](https://monzo.com/blog/2016/08/11/we-are-now-a-bank)، [توضیح <bdi dir="ltr">Mobilisation</bdi> و اتصال به <bdi dir="ltr">Mastercard</bdi>، <bdi dir="ltr">Bacs</bdi> و <bdi dir="ltr">Faster Payments</bdi>](https://monzo.com/blog/2016/08/15/launching-the-bank)

### اولین خطای پرهزینه اما قابل بازیابی: نام

<bdi dir="ltr">Trademark</bdi> نام <bdi dir="ltr">Mondo</bdi> با چالش حقوقی یک شرکت دیگر روبه‌رو شد. تیم به‌جای دعوای طولانی، <bdi dir="ltr">Rebrand</bdi> را انتخاب کرد و پس از دریافت بیش از ۱۲٬۵۰۰ پیشنهاد از جامعه، نام <bdi dir="ltr">Monzo</bdi> را برگزید. این خطا معماری نرم‌افزار نبود، اما یک درس معماری سازمانی دارد: **دارایی حیاتی فقط <bdi dir="ltr">Code</bdi> و <bdi dir="ltr">Data</bdi> نیست؛ <bdi dir="ltr">Name</bdi>، <bdi dir="ltr">License</bdi>، <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Regulatory permission</bdi> نیز <bdi dir="ltr">Dependency</bdi> واقعی‌اند.** [شرح رسمی دلیل تغییر نام](https://monzo.com/blog/2016/08/26/how-we-picked-monzo)، [اعلام نام <bdi dir="ltr">Monzo</bdi>](https://monzo.com/blog/2016/08/25/monzo)

## <bdi dir="ltr">4. Timeline</bdi> تحول

| دوره | رخداد مستند | تغییر مسئله و <bdi dir="ltr">Capability</bdi> |
|---|---|---|
| 2015 | شروع <bdi dir="ltr">Mondo</bdi> و ساخت <bdi dir="ltr">Prepaid beta</bdi> | آزمون <bdi dir="ltr">Product/UX</bdi> و <bdi dir="ltr">Card processing</bdi> پیش از بانک کامل |
| 2016 | مجوز بانکی محدود، <bdi dir="ltr">Mobilisation</bdi> و تغییر نام به <bdi dir="ltr">Monzo</bdi> | ورود جدی <bdi dir="ltr">Risk</bdi>، <bdi dir="ltr">Compliance</bdi>، <bdi dir="ltr">Bacs</bdi>، <bdi dir="ltr">Faster Payments</bdi> و <bdi dir="ltr">Mastercard</bdi> |
| <bdi dir="ltr">Apr 2017</bdi> | رفع محدودیت‌های مجوز و تبدیل به بانک کاملاً مجاز | مسئولیت کامل <bdi dir="ltr">Current Account</bdi> و <bdi dir="ltr">Deposit-taking</bdi>؛ [اعلام رسمی](https://monzo.com/blog/2017/04/05/banking-licence) |
| <bdi dir="ltr">Jul</bdi>–<bdi dir="ltr">Dec 2017</bdi> | <bdi dir="ltr">Rollout</bdi> تدریجی <bdi dir="ltr">Current Account</bdi> و <bdi dir="ltr">Migration</bdi> از <bdi dir="ltr">Prepaid</bdi> | <bdi dir="ltr">Account lifecycle</bdi>، <bdi dir="ltr">Direct Debit</bdi>، <bdi dir="ltr">Standing Order</bdi>، <bdi dir="ltr">Overdraft</bdi> و <bdi dir="ltr">Migration</bdi>؛ [برنامهٔ <bdi dir="ltr">Rollout</bdi>](https://monzo.com/blog/2017/07/17/current-account-preview) |
| 2018–2019 | عبور از یک میلیون مشتری، <bdi dir="ltr">Joint account</bdi>، <bdi dir="ltr">Apple Pay</bdi>، <bdi dir="ltr">Savings partnership</bdi> و <bdi dir="ltr">Lending</bdi>؛ شروع <bdi dir="ltr">Business Banking</bdi> | عبور از «کارت خوب» به بانک چندمحصولی؛ [مرور رسمی 2019](https://monzo.com/blog/2019/01/04/monzo-in-2019) |
| 2019 | <bdi dir="ltr">Launch</bdi> در آمریکا با <bdi dir="ltr">Partner bank</bdi> | آزمون <bdi dir="ltr">Market/Regulatory model</bdi> متفاوت؛ [گزارش رسمی 2019](https://monzo.com/blog/2019/06/27/monzo-2019-annual-report) |
| 2020–2022 | رشد بسیار سریع <bdi dir="ltr">Customer</bdi> و <bdi dir="ltr">Product</bdi>؛ ضعف جدی <bdi dir="ltr">Financial Crime controls</bdi> | کنترل‌های <bdi dir="ltr">Onboarding</bdi>، <bdi dir="ltr">Risk assessment</bdi> و <bdi dir="ltr">Transaction monitoring</bdi> از رشد عقب ماندند |
| 2022–2024 | <bdi dir="ltr">Direct participation</bdi> در <bdi dir="ltr">Bacs</bdi>، <bdi dir="ltr">International Payments</bdi>، <bdi dir="ltr">Investments</bdi> و رشد <bdi dir="ltr">Business Banking</bdi> | افزایش عمق <bdi dir="ltr">Payment</bdi>، <bdi dir="ltr">Wealth</bdi> و <bdi dir="ltr">Business capabilities</bdi> |
| 2024 | حدود ۲۸۰۰ تا ۳۰۰۰ <bdi dir="ltr">Microservice</bdi>؛ <bdi dir="ltr">Migration</bdi>های سراسری و <bdi dir="ltr">Rate limiting</bdi> توزیع‌شده | <bdi dir="ltr">Platform consistency</bdi> و <bdi dir="ltr">Mass change</bdi> به مسئلهٔ معماری درجه‌اول تبدیل شد |
| 2025 | معرفی <bdi dir="ltr">Monzo Stand-in</bdi> و جریمهٔ <bdi dir="ltr">FCA</bdi> | <bdi dir="ltr">Cloud-level resilience</bdi> رشد کرد؛ در مقابل <bdi dir="ltr">Debt</bdi> کنترل مالی رسمی شد |
| 2026 | <bdi dir="ltr">Migration</bdi> بیش از ۳۰۰۰ <bdi dir="ltr">Service</bdi> به <bdi dir="ltr">EKS</bdi>، <bdi dir="ltr">Launch</bdi> در <bdi dir="ltr">Ireland</bdi> و بستن حساب‌های آمریکا | <bdi dir="ltr">Platform productization</bdi>، تمرکز جغرافیایی جدید و خروج از آزمایش آمریکا |

<bdi dir="ltr">Timeline</bdi> بالا گزیده است؛ هدف اتصال تحول <bdi dir="ltr">Capability</bdi> به تحول معماری است، نه فهرست همهٔ <bdi dir="ltr">Feature</bdi>ها.

## 5. معماری نسل اول: <bdi dir="ltr">Microservice</bdi> از روز اول

<bdi dir="ltr">Monzo</bdi> در ۲۰۱۶ نوشت <bdi dir="ltr">Backend</bdi> از ابتدا مجموعه‌ای از <bdi dir="ltr">Microservice</bdi>های توزیع‌شده بوده است؛ انتخابی غیرعادی برای <bdi dir="ltr">Startup.</bdi> استدلال اصلی، 24×7 بودن، <bdi dir="ltr">Fault isolation</bdi>، استقرار سریع و استقلال تیم‌های آینده بود. در شروع فقط سه <bdi dir="ltr">Backend developer</bdi> داشتند، اما هنگام <bdi dir="ltr">Beta</bdi> تعداد <bdi dir="ltr">Service</bdi>ها نزدیک ۱۰۰ و سپس حدود ۱۵۰ شده بود. [شرح معماری اولیه توسط <bdi dir="ltr">Head of Engineering</bdi>](https://monzo.com/blog/2016/09/19/building-a-modern-bank-backend)

<bdi dir="ltr">Technology/architecture</bdi> اعلام‌شده در آن زمان:

- <bdi dir="ltr">Go</bdi> به‌عنوان زبان غالب <bdi dir="ltr">Service</bdi>ها
- <bdi dir="ltr">Containerization</bdi> با <bdi dir="ltr">Docker</bdi>
- مهاجرت از <bdi dir="ltr">Mesos/Marathon</bdi> به <bdi dir="ltr">Kubernetes</bdi> روی <bdi dir="ltr">AWS</bdi>
- <bdi dir="ltr">RPC</bdi> برای ارتباط همگام و <bdi dir="ltr">Linkerd/Finagle</bdi> در نسل اولیه
- <bdi dir="ltr">Kafka</bdi> به‌عنوان <bdi dir="ltr">Commit log/Message backbone</bdi> با <bdi dir="ltr">At-least-once delivery</bdi> و <bdi dir="ltr">Replay</bdi>
- سرویس‌های کوچک برای <bdi dir="ltr">Shared platform capabilities</bdi>

### تصمیم درست یا <bdi dir="ltr">Premature decomposition</bdi>؟

از دادهٔ عمومی نمی‌توان حکم قطعی داد. این انتخاب دو اثر واقعی داشت:

**سودها**

- تیم‌ها می‌توانستند <bdi dir="ltr">Build/Deploy/Scale</bdi> مستقل‌تری داشته باشند.
- <bdi dir="ltr">Failure isolation</bdi> و <bdi dir="ltr">Continuous delivery</bdi> از ابتدا <bdi dir="ltr">Design concern</bdi> شد.
- <bdi dir="ltr">Event</bdi> و <bdi dir="ltr">Replay</bdi> برای عملیات بانکی بخشی از <bdi dir="ltr">Platform</bdi> بود، نه افزونهٔ دیرهنگام.

**هزینه‌ها**

- با تیم کوچک، تعداد <bdi dir="ltr">Service</bdi>ها بسیار سریع بالا رفت.
- <bdi dir="ltr">RPC</bdi>، <bdi dir="ltr">Queue</bdi>، <bdi dir="ltr">Service discovery</bdi>، <bdi dir="ltr">Deployment</bdi>، <bdi dir="ltr">Observability</bdi> و <bdi dir="ltr">Migration</bdi> سراسری باید خیلی زود حل می‌شد.
- مرز کوچک <bdi dir="ltr">Deployment</bdi> الزاماً مرز دامینی خوب نیست و می‌تواند <bdi dir="ltr">Cognitive load</bdi> را زیاد کند.

نتیجه برای <bdi dir="ltr">Lab</bdi> ما «از روز اول <bdi dir="ltr">Microservice</bdi> بساز» نیست. نتیجه این است که اگر استقلال <bdi dir="ltr">Deploy</bdi> را زود انتخاب می‌کنی، باید هزینهٔ <bdi dir="ltr">Platform</bdi> و عملیات آن را نیز از روز اول بپردازی.

## 6. معماری در مقیاس: استانداردسازی برای مهار توزیع

تا ۲۰۲۴ <bdi dir="ltr">Monzo</bdi> از ۲۸۰۰ تا بیش از ۳۰۰۰ <bdi dir="ltr">Microservice</bdi> حرف می‌زد. نکتهٔ مهم این نیست که عدد بزرگ تحسین شود؛ مهم این است که چنین عددی چه <bdi dir="ltr">Governance</bdi>ای طلب می‌کند.

در پروندهٔ <bdi dir="ltr">Migration</bdi> از <bdi dir="ltr">OpenTracing</bdi> به <bdi dir="ltr">OpenTelemetry</bdi>، <bdi dir="ltr">Monzo</bdi> چند قابلیت کلیدی را اعلام کرد:

- همهٔ <bdi dir="ltr">Service</bdi>های مورد بحث با <bdi dir="ltr">Go</bdi> و <bdi dir="ltr">Technology version</bdi> سازگار ساخته شده‌اند.
- کد <bdi dir="ltr">Service</bdi>ها در یک <bdi dir="ltr">Monorepo</bdi> است.
- <bdi dir="ltr">CI</bdi> با ابزارهایی مانند <bdi dir="ltr">Semgrep Convention</bdi>ها را سراسری <bdi dir="ltr">enforce</bdi> می‌کند.
- <bdi dir="ltr">Mass deployment</bdi> و <bdi dir="ltr">Automated rollback</bdi> وجود دارد.
- <bdi dir="ltr">Config service</bdi> امکان <bdi dir="ltr">Roll-forward</bdi> تدریجی و <bdi dir="ltr">Rollback</bdi> سریع را می‌دهد.
- <bdi dir="ltr">Migration</bdi> بزرگ به‌صورت مرکزی هدایت می‌شود، زیرا واگذاری کامل به <bdi dir="ltr">Owner</bdi>های پراکنده قبلاً <bdi dir="ltr">Migration</bdi>های نیمه‌تمام و <bdi dir="ltr">Coordination cost</bdi> ایجاد کرده بود. [شرح <bdi dir="ltr">Migration</bdi> در ۲۸۰۰ <bdi dir="ltr">Microservice</bdi>](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)

این یک <bdi dir="ltr">Trade-off</bdi> جالب <bdi dir="ltr">Ownership</bdi> است:


</div>

<div dir="ltr" align="left">

```text
product behavior ownership       → decentralized squads
cross-cutting platform migration → centrally driven platform team
```

</div>

<div dir="rtl" align="right">


<bdi dir="ltr">Ownership</bdi> همیشه به معنی «هر تیم هر کاری خواست» نیست. استاندارد مشترک و تغییر سراسری نیز <bdi dir="ltr">Owner</bdi> لازم دارد.

## 7. معماری جاریِ قابل اثبات در ۲۰۲۶

جدول زیر فقط مواردی را قطعی می‌داند که در منابع رسمی ۲۰۲۴ تا ۲۰۲۶ آمده‌اند:

| حوزه | آنچه عمومی و قابل اثبات است | سطح اطمینان |
|---|---|---|
| <bdi dir="ltr">Service architecture</bdi> | بیش از ۳۰۰۰ <bdi dir="ltr">Microservice</bdi>؛ <bdi dir="ltr">Backend</bdi>ها در <bdi dir="ltr">Monorepo</bdi> و <bdi dir="ltr">Common patterns</bdi> | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Application language</bdi> | نوشتهٔ <bdi dir="ltr">Migration</bdi> ۲۰۲۴ می‌گوید <bdi dir="ltr">Service</bdi>های آن‌ها با <bdi dir="ltr">Go</bdi> نوشته شده‌اند | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi>، <bdi dir="ltr">scope</bdi> همان <bdi dir="ltr">Backend fleet</bdi> |
| <bdi dir="ltr">Container platform</bdi> | <bdi dir="ltr">Kubernetes</bdi>؛ <bdi dir="ltr">Workload</bdi>ها از <bdi dir="ltr">Self-hosted Kubernetes</bdi> به <bdi dir="ltr">Amazon EKS</bdi> مهاجرت کرده‌اند | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Primary cloud</bdi> | <bdi dir="ltr">Primary Platform</bdi> روی <bdi dir="ltr">AWS</bdi> | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Stand-in cloud</bdi> | <bdi dir="ltr">Stand-in</bdi> مستقل روی <bdi dir="ltr">GCP</bdi> با حدود ۱۸ <bdi dir="ltr">Service</bdi> | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Async/event</bdi> | <bdi dir="ltr">Kafka</bdi> در <bdi dir="ltr">Platform</bdi> اصلی؛ <bdi dir="ltr">GCP Pub/Sub</bdi> برای <bdi dir="ltr">Advice</bdi>های <bdi dir="ltr">Stand-in</bdi> | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Platform interface</bdi> | <bdi dir="ltr">Platform operation</bdi>ها پشت <bdi dir="ltr">Service/API</bdi>های <bdi dir="ltr">opinionated</bdi>، با <bdi dir="ltr">Multi-party authorization</bdi> برای عملیات حساس | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Observability/migration</bdi> | <bdi dir="ltr">Central metrics/logging</bdi>، <bdi dir="ltr">OpenTelemetry migration</bdi>، <bdi dir="ltr">automated health checks</bdi> و <bdi dir="ltr">rollback</bdi> | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Analytics</bdi> | <bdi dir="ltr">BigQuery</bdi> + <bdi dir="ltr">dbt</bdi>؛ بیش از سه میلیارد <bdi dir="ltr">Analytics event</bdi> در روز در گزارش ۲۰۲۴ | <bdi dir="ltr">FACT</bdi> — <bdi dir="ltr">primary</bdi> |
| <bdi dir="ltr">Primary operational datastore</bdi> | نام فعلی در منابع بررسی‌شده اعلام نشده؛ مقالهٔ ۲۰۲۴ فقط از <bdi dir="ltr">Migration</bdi> پایگاه <bdi dir="ltr">Core</bdi> حرف می‌زند | <bdi dir="ltr">UNKNOWN</bdi> |
| <bdi dir="ltr">Historic datastore</bdi> | <bdi dir="ltr">Cassandra</bdi> در منابع قدیمی <bdi dir="ltr">Monzo</bdi> و آگهی‌های فنی آمده است، اما این پرونده آن را <bdi dir="ltr">Database</bdi> قطعی ۲۰۲۶ اعلام نمی‌کند | <bdi dir="ltr">HISTORIC FACT</bdi> / <bdi dir="ltr">CURRENT UNKNOWN</bdi> |
| <bdi dir="ltr">Exact Bounded Context map</bdi> | عمومی نشده است | <bdi dir="ltr">UNKNOWN</bdi> |

منابع: [<bdi dir="ltr">Platform engineering</bdi> و <bdi dir="ltr">Migration</bdi> بیش از ۳۰۰۰ <bdi dir="ltr">Service</bdi> به <bdi dir="ltr">EKS</bdi> در ۲۰۲۶](https://monzo.com/blog/the-engineering-behind-the-platform)، [<bdi dir="ltr">Scale</bdi> و <bdi dir="ltr">Migration</bdi> در ۲۰۲۴](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)، [<bdi dir="ltr">Data platform</bdi> و سه میلیارد <bdi dir="ltr">Event</bdi> روزانه](https://monzo.com/blog/how-we-use-incremental-modelling-to-handle-billions-of-events-every-day)

## <bdi dir="ltr">8. Monzo Stand-in:</bdi> تاب‌آوری با استقلال، نه <bdi dir="ltr">Clone</bdi> کامل

یکی از مهم‌ترین دستاوردهای معماری <bdi dir="ltr">Monzo</bdi>، **<bdi dir="ltr">Stand-in</bdi>** است. <bdi dir="ltr">Primary Platform</bdi> روی <bdi dir="ltr">AWS</bdi> حدود ۳۰۰۰ <bdi dir="ltr">Microservice</bdi> دارد؛ <bdi dir="ltr">Stand-in</bdi> روی <bdi dir="ltr">GCP</bdi> فقط ۱۸ <bdi dir="ltr">Service</bdi> مستقل دارد و برای خرابی بزرگ، <bdi dir="ltr">Capability</bdi>های حیاتی زیر را نگه می‌دارد:

- <bdi dir="ltr">Card spend</bdi> و <bdi dir="ltr">Cash withdrawal</bdi>
- <bdi dir="ltr">Bank transfer</bdi>های اصلی
- مشاهدهٔ <bdi dir="ltr">Balance</bdi> و <bdi dir="ltr">Transaction</bdi>
- <bdi dir="ltr">Freeze/Unfreeze card</bdi>

<bdi dir="ltr">Stand-in</bdi> کپی کامل <bdi dir="ltr">Primary</bdi> نیست. <bdi dir="ltr">Software</bdi>، <bdi dir="ltr">Service</bdi>ها و <bdi dir="ltr">Cloud</bdi> جدا هستند تا یک <bdi dir="ltr">Bug</bdi> یا <bdi dir="ltr">Process failure</bdi> مشترک هر دو را هم‌زمان از کار نیندازد. داده از <bdi dir="ltr">Primary</bdi> به <bdi dir="ltr">Stand-in</bdi> به‌صورت <bdi dir="ltr">Non-blocking</bdi> و <bdi dir="ltr">Eventually consistent</bdi> می‌رود. <bdi dir="ltr">Stand-in</bdi> هنگام فعال‌بودن <bdi dir="ltr">Decision</bdi>های خودش را می‌گیرد و نتیجه را به شکل <bdi dir="ltr">Advice durable</bdi> برای <bdi dir="ltr">Primary</bdi> ثبت می‌کند؛ <bdi dir="ltr">Primary</bdi> پس از بازیابی، این <bdi dir="ltr">Effects</bdi> را اعمال و با <bdi dir="ltr">Correlation ID</bdi> تطبیق می‌دهد. <bdi dir="ltr">Primary</bdi> همچنان <bdi dir="ltr">System of Record</bdi> باقی می‌ماند. [شرح کامل <bdi dir="ltr">Stand-in</bdi> توسط <bdi dir="ltr">Monzo</bdi>](https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in)

### <bdi dir="ltr">Trade-off</bdi> آگاهانه

<bdi dir="ltr">Monzo</bdi> صریحاً می‌پذیرد که <bdi dir="ltr">Stand-in</bdi> ممکن است با <bdi dir="ltr">View</bdi> کمی قدیمی، پرداختی را تأیید کند که <bdi dir="ltr">Primary</bdi> آن را <bdi dir="ltr">Insufficient funds</bdi> می‌داند؛ نتیجه می‌تواند <bdi dir="ltr">Unapproved overdraft</bdi> باشد. این ریسک با <bdi dir="ltr">Control</bdi> و <bdi dir="ltr">Reconciliation</bdi> مدیریت می‌شود، نه با ادعای <bdi dir="ltr">Consistency</bdi> کامل.

درس معماری:

> <bdi dir="ltr">Availability</bdi> بالا همیشه حاصل <bdi dir="ltr">Replication</bdi> کامل نیست؛ گاهی حاصل کاهش <bdi dir="ltr">Scope</bdi>، استقلال <bdi dir="ltr">Failure mode</bdi> و پذیرش آگاهانهٔ <bdi dir="ltr">Consistency</bdi> محدود است.

## <bdi dir="ltr">9. Domain/Capability map</bdi> تحلیلی

<bdi dir="ltr">Monzo</bdi> نقشهٔ رسمی <bdi dir="ltr">Bounded Context</bdi>های خود را عمومی نکرده است. جدول زیر از <bdi dir="ltr">Product</bdi>ها، گزارش مالی و نوشته‌های فنی **استنتاج** شده و نباید به‌عنوان ساختار داخلی قطعی بازنشر شود.

| <bdi dir="ltr">Capability cluster</bdi> | شواهد عمومی | فرضیهٔ <bdi dir="ltr">Ownership</bdi> |
|---|---|---|
| <bdi dir="ltr">Party</bdi>, <bdi dir="ltr">Customer</bdi> & <bdi dir="ltr">Onboarding</bdi> | <bdi dir="ltr">Account signup</bdi>، <bdi dir="ltr">KYC</bdi> و <bdi dir="ltr">FCA findings</bdi> | هویت، <bdi dir="ltr">Eligibility</bdi> و <bdi dir="ltr">Customer risk</bdi> باید <bdi dir="ltr">Authority</bdi> روشن داشته باشد |
| <bdi dir="ltr">Accounts</bdi> & <bdi dir="ltr">Deposits</bdi> | <bdi dir="ltr">Current account</bdi>، <bdi dir="ltr">Joint</bdi>، <bdi dir="ltr">Under-16</bdi>، <bdi dir="ltr">Pots</bdi> و £<bdi dir="ltr">25.7bn deposits</bdi> در <bdi dir="ltr">FY2026</bdi> | <bdi dir="ltr">Operational account state</bdi> و <bdi dir="ltr">available balance</bdi> در <bdi dir="ltr">Banking platform</bdi> |
| <bdi dir="ltr">Cards</bdi> & <bdi dir="ltr">Cash</bdi> | <bdi dir="ltr">Mastercard</bdi>، <bdi dir="ltr">ATM</bdi>، <bdi dir="ltr">freeze/unfreeze</bdi> و <bdi dir="ltr">Stand-in card processor</bdi> | <bdi dir="ltr">Card lifecycle</bdi> و <bdi dir="ltr">Authorization</bdi> جدا از <bdi dir="ltr">Channel UI</bdi> |
| <bdi dir="ltr">Payments</bdi> | <bdi dir="ltr">Faster Payments</bdi>، <bdi dir="ltr">Bacs</bdi>، <bdi dir="ltr">Direct Debit</bdi>، <bdi dir="ltr">SWIFT/International payments</bdi> | <bdi dir="ltr">Payment instruction</bdi>، <bdi dir="ltr">processing state</bdi>، <bdi dir="ltr">scheme adapter</bdi> و <bdi dir="ltr">reconciliation</bdi> |
| <bdi dir="ltr">Ledger</bdi> & <bdi dir="ltr">Balance</bdi> | <bdi dir="ltr">Stand-in</bdi> مقاله صریحاً از <bdi dir="ltr">Ledger</bdi> و <bdi dir="ltr">System of Record</bdi> حرف می‌زند | <bdi dir="ltr">Primary Ledger Authority</bdi>؛ <bdi dir="ltr">Stand-in decision/effect</bdi> موقت و <bdi dir="ltr">reconciled</bdi> |
| <bdi dir="ltr">Borrowing</bdi> | <bdi dir="ltr">Loan</bdi>، <bdi dir="ltr">Overdraft</bdi> و <bdi dir="ltr">Flex</bdi> | <bdi dir="ltr">Credit decision</bdi>، <bdi dir="ltr">agreement</bdi> و <bdi dir="ltr">servicing</bdi> با <bdi dir="ltr">Lifecycle</bdi> مستقل |
| <bdi dir="ltr">Savings</bdi> & <bdi dir="ltr">Wealth</bdi> | <bdi dir="ltr">Savings</bdi>، <bdi dir="ltr">ISA</bdi>، <bdi dir="ltr">Investments</bdi> و <bdi dir="ltr">Pensions</bdi> | <bdi dir="ltr">Product/partner orchestration</bdi> و <bdi dir="ltr">customer holdings</bdi> |
| <bdi dir="ltr">Business Banking</bdi> | <bdi dir="ltr">Business current account</bdi>، <bdi dir="ltr">invoicing</bdi> و <bdi dir="ltr">expense cards</bdi> | <bdi dir="ltr">Party/business relationship</bdi> و <bdi dir="ltr">entitlements</bdi> چندکاربره |
| <bdi dir="ltr">Financial Crime</bdi> & <bdi dir="ltr">Fraud</bdi> | <bdi dir="ltr">Customer risk assessment</bdi>، <bdi dir="ltr">transaction monitoring</bdi>، <bdi dir="ltr">fraud controls</bdi> | <bdi dir="ltr">Policy/decision ownership</bdi> باید همگام با <bdi dir="ltr">Product growth</bdi> مقیاس بگیرد |
| <bdi dir="ltr">Customer Operations</bdi> | <bdi dir="ltr">Support</bdi> و <bdi dir="ltr">Ops Agent</bdi> | <bdi dir="ltr">Case/operation workflows</bdi> بدون تصاحب <bdi dir="ltr">Source of Truth</bdi> دامین‌ها |
| <bdi dir="ltr">Platform</bdi> & <bdi dir="ltr">Reliability</bdi> | <bdi dir="ltr">Kubernetes</bdi>، <bdi dir="ltr">EKS</bdi>، <bdi dir="ltr">deployment</bdi>، <bdi dir="ltr">MPA</bdi>، <bdi dir="ltr">Stand-in</bdi> | <bdi dir="ltr">Internal platform product</bdi> با <bdi dir="ltr">API</bdi> و <bdi dir="ltr">Owner</bdi> مستقل |
| <bdi dir="ltr">Data</bdi> & <bdi dir="ltr">Analytics</bdi> | <bdi dir="ltr">BigQuery</bdi>، <bdi dir="ltr">dbt</bdi> و <bdi dir="ltr">event ingestion</bdi> | <bdi dir="ltr">Analytical projection</bdi>؛ نه مالک <bdi dir="ltr">Operational facts</bdi> |

نکتهٔ <bdi dir="ltr">Week 02:</bdi> وجود ۳۰۰۰ <bdi dir="ltr">Service</bdi> به معنی ۳۰۰۰ <bdi dir="ltr">Domain</bdi> نیست. بسیاری <bdi dir="ltr">Platform service</bdi>، <bdi dir="ltr">Adapter</bdi>، <bdi dir="ltr">Workflow step</bdi> یا <bdi dir="ltr">Technical capability</bdi> هستند.

## 10. اشتباه‌ها و شرط‌بندی‌های ناموفق

### <bdi dir="ltr">10.1 Financial Crime controls</bdi> از رشد عقب ماند

<bdi dir="ltr">FCA</bdi> در ژوئیهٔ ۲۰۲۵ <bdi dir="ltr">Monzo</bdi> را ۲۱٬۰۹۱٬۳۰۰ پوند جریمه کرد. تخلف‌های اعلام‌شده شامل ناکافی‌بودن سیستم‌ها و کنترل‌های <bdi dir="ltr">Financial Crime</bdi> بین اکتبر ۲۰۱۸ تا اوت ۲۰۲۰ و نقض مکرر محدودیت <bdi dir="ltr">Onboarding</bdi> مشتریان <bdi dir="ltr">High-risk</bdi> بین اوت ۲۰۲۰ تا ژوئن ۲۰۲۲ بود. <bdi dir="ltr">FCA</bdi> گفت <bdi dir="ltr">Customer base</bdi> از حدود ۶۰۰ هزار در ۲۰۱۸ به بیش از ۵.۸ میلیون در ۲۰۲۲ رسید، اما کنترل‌ها هم‌پای رشد نکردند؛ بیش از ۳۴ هزار <bdi dir="ltr">High-risk customer</bdi> برخلاف <bdi dir="ltr">Requirement</bdi> ثبت شدند. <bdi dir="ltr">Monzo</bdi> پس از <bdi dir="ltr">Review</bdi> مستقل، <bdi dir="ltr">Change programme</bdi> مربوط را تکمیل کرد. [اعلام و جزئیات رسمی <bdi dir="ltr">FCA</bdi>](https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls)

این <bdi dir="ltr">Failure</bdi> را نباید به «<bdi dir="ltr">Bug</bdi> یک <bdi dir="ltr">Microservice</bdi>» تقلیل داد. حداقل چهار مالکیت باید هم‌راستا می‌بود:

- <bdi dir="ltr">Product growth</bdi> و <bdi dir="ltr">Onboarding flow</bdi>
- <bdi dir="ltr">Customer risk policy</bdi>
- <bdi dir="ltr">Transaction monitoring capability</bdi>
- <bdi dir="ltr">Regulatory control</bdi>، <bdi dir="ltr">evidence</bdi> و <bdi dir="ltr">change governance</bdi>

درس: **<bdi dir="ltr">Compliance</bdi> یک <bdi dir="ltr">Non-functional afterthought</bdi> نیست؛ مجموعه‌ای از <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Decision owner</bdi>، <bdi dir="ltr">Data quality</bdi>، <bdi dir="ltr">Control loop</bdi> و <bdi dir="ltr">Evidence</bdi> است.**

### <bdi dir="ltr">10.2 Microservice scale</bdi> خودش مسئله ساخت

<bdi dir="ltr">Monzo</bdi> در ۲۰۲۴ صریحاً نوشت معماری ۲۸۰۰ <bdi dir="ltr">Service</bdi> ارزش زیادی داده، اما <bdi dir="ltr">Migration</bdi> سراسری را دشوار کرده است. تجربهٔ <bdi dir="ltr">Decentralized migration</bdi> نیز به کار نیمه‌تمام و <bdi dir="ltr">Coordination</bdi> زیاد منجر شده بود؛ برای همین <bdi dir="ltr">Standardization</bdi>، <bdi dir="ltr">Monorepo</bdi>، <bdi dir="ltr">central tooling</bdi> و <bdi dir="ltr">centrally driven migration</bdi> تقویت شد. [منبع رسمی <bdi dir="ltr">Migration</bdi>](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)

این «اثبات شکست <bdi dir="ltr">Microservices</bdi>» نیست؛ اثبات این است که استقلال زیاد بدون <bdi dir="ltr">Platform governance</bdi> پایدار نمی‌ماند.

### 10.3 آزمایش آمریکا پایان یافت

<bdi dir="ltr">Monzo</bdi> در ۲۰۱۹ با <bdi dir="ltr">Partner bank</bdi> وارد آمریکا شد، اما از ۸ ژوئن ۲۰۲۶ همهٔ حساب‌های آمریکا بسته شدند و شرکت تمرکز خود را بر <bdi dir="ltr">UK</bdi> و <bdi dir="ltr">Europe</bdi> گذاشت. <bdi dir="ltr">Monzo</bdi> در صفحهٔ رسمی <bdi dir="ltr">Closure</bdi> دلیل فنی یا شکست معماری واحدی اعلام نمی‌کند؛ بنابراین پرونده نیز علت‌سازی نمی‌کند. <bdi dir="ltr">Fact</bdi> قطعی، پایان <bdi dir="ltr">Product/market experiment</bdi> است. [اطلاعیهٔ رسمی بستن حساب‌های آمریکا](https://monzo.com/help/us-account-closure-support/us-account-closure-support)

درس: <bdi dir="ltr">Technology reuse</bdi> به‌تنهایی <bdi dir="ltr">Product-market fit</bdi>، <bdi dir="ltr">Regulation</bdi>، <bdi dir="ltr">Payment rails</bdi> و <bdi dir="ltr">Unit economics</bdi> بازار جدید را حل نمی‌کند.

### <bdi dir="ltr">10.4 Self-hosted Kubernetes</bdi> تا <bdi dir="ltr">EKS</bdi>

در ۲۰۱۶ اجرای <bdi dir="ltr">Highly available Kubernetes</bdi> روی <bdi dir="ltr">AWS</bdi> را دشوار اما ارزشمند توصیف کردند. در ۲۰۲۶ اعلام شد بیش از ۳۰۰۰ <bdi dir="ltr">Service</bdi> از <bdi dir="ltr">Self-hosted Kubernetes</bdi> به <bdi dir="ltr">EKS</bdi> مهاجرت کرده‌اند. این را نباید بدون شواهد «اشتباه اولیه» نامید؛ در ۲۰۱۶ <bdi dir="ltr">Managed option</bdi> امروز وجود نداشت. این یک نمونهٔ <bdi dir="ltr">Revisit architecture decision</bdi> با تغییر <bdi dir="ltr">Technology landscape</bdi> است.

## 11. دستاوردهای تازه تا <bdi dir="ltr">FY2026</bdi>

### <bdi dir="ltr">Business/Product</bdi>

گزارش سال مالی ۲۰۲۶ <bdi dir="ltr">Monzo</bdi> ارقام زیر را منتشر کرده است:

- درآمد ۱.۷ میلیارد پوند
- <bdi dir="ltr">Adjusted profit before tax</bdi> برابر ۱۷۲.۶ میلیون پوند
- سپردهٔ مشتریان ۲۵.۷ میلیارد پوند
- ۱۵.۲ میلیون مشتری و ۱۰.۴ میلیون <bdi dir="ltr">Monthly active user</bdi>
- ۷۳ میلیارد پوند <bdi dir="ltr">Card spend</bdi>
- رشد ۴۵ درصدی <bdi dir="ltr">Business banking customers</bdi>
- <bdi dir="ltr">Launch</bdi> در <bdi dir="ltr">Ireland</bdi>

[<bdi dir="ltr">Monzo FY2026 Annual Report summary</bdi>](https://monzo.com/annual-report)

### <bdi dir="ltr">Technology/Architecture</bdi>

- <bdi dir="ltr">Stand-in</bdi> مستقل روی <bdi dir="ltr">GCP</bdi> برای <bdi dir="ltr">Critical banking capabilities</bdi>
- <bdi dir="ltr">Migration</bdi> خودکار بیش از ۳۰۰۰ <bdi dir="ltr">Microservice</bdi> به <bdi dir="ltr">EKS</bdi>، همراه با <bdi dir="ltr">Health check</bdi> و <bdi dir="ltr">Rollback</bdi>؛ حتی <bdi dir="ltr">Migrator service</bdi> خودش را مهاجرت کرد
- <bdi dir="ltr">Platform operation</bdi>ها به‌صورت <bdi dir="ltr">API/Service</bdi> با <bdi dir="ltr">Multi-party authorization</bdi>، به‌جای <bdi dir="ltr">Runbook</bdi> و <bdi dir="ltr">Script</bdi> دستی
- <bdi dir="ltr">Standardized Go/Monorepo estate</bdi> برای <bdi dir="ltr">Migration</bdi>های سراسری و کنترل <bdi dir="ltr">Convention</bdi>

این دستاوردها نشان می‌دهند <bdi dir="ltr">Platform engineering</bdi> در بانک فقط «زیرساخت» نیست؛ یک <bdi dir="ltr">Product</bdi> داخلی با <bdi dir="ltr">API</bdi>، <bdi dir="ltr">User</bdi>، <bdi dir="ltr">Ownership</bdi>، <bdi dir="ltr">Test</bdi> و <bdi dir="ltr">Control</bdi> است.

## 12. ارزیابی معماری

### نقاط قوت

1. **<bdi dir="ltr">Boundary</bdi> اجرایی واقعی:** <bdi dir="ltr">Service</bdi>ها <bdi dir="ltr">Build/Deploy/Scale</bdi> مستقل دارند.
2. **<bdi dir="ltr">Platform as product:</bdi>** عملیات حساس پشت <bdi dir="ltr">API</bdi> و <bdi dir="ltr">Approval</bdi> قرار گرفته است.
3. **<bdi dir="ltr">Change at scale:</bdi>** <bdi dir="ltr">Monorepo</bdi> و <bdi dir="ltr">Standard stack</bdi> امکان <bdi dir="ltr">Refactor</bdi> سراسری می‌دهند.
4. **<bdi dir="ltr">Event-driven durability:</bdi>** <bdi dir="ltr">Replay</bdi>، <bdi dir="ltr">At-least-once</bdi> و <bdi dir="ltr">Advice log</bdi> از ابتدا/در تاب‌آوری مهم‌اند.
5. **<bdi dir="ltr">Failure diversity:</bdi>** <bdi dir="ltr">Stand-in</bdi> همان <bdi dir="ltr">Software</bdi> را در <bdi dir="ltr">Cloud</bdi> دوم کپی نمی‌کند.
6. **<bdi dir="ltr">Transparency:</bdi>** بسیاری از <bdi dir="ltr">Trade-off</bdi>ها و محدودیت‌ها عمومی نوشته شده‌اند.

### هزینه‌ها و ریسک‌ها

1. ۳۰۰۰ <bdi dir="ltr">Service</bdi> نیازمند <bdi dir="ltr">Platform team</bdi> و <bdi dir="ltr">Automation</bdi> در سطح بسیار بالا هستند.
2. <bdi dir="ltr">Deployment boundary</bdi>های ریز می‌توانند <bdi dir="ltr">Runtime coupling</bdi> و <bdi dir="ltr">Cognitive load</bdi> بسازند.
3. <bdi dir="ltr">Consistency</bdi> و <bdi dir="ltr">Authority</bdi> در <bdi dir="ltr">Stand-in</bdi> نیازمند <bdi dir="ltr">Advice</bdi>، <bdi dir="ltr">Correlation</bdi> و <bdi dir="ltr">Reconciliation</bdi> دقیق است.
4. <bdi dir="ltr">Technology excellence</bdi> جای <bdi dir="ltr">Financial Crime control</bdi> و <bdi dir="ltr">Regulatory ownership</bdi> را نمی‌گیرد.
5. <bdi dir="ltr">Standardization</bdi> برای <bdi dir="ltr">Migration</bdi> سراسری، بخشی از آزادی تکنولوژیک تیم‌ها را محدود می‌کند.

## 13. چه چیزی را برای <bdi dir="ltr">Core Banking Lab</bdi> خودمان می‌گیریم؟

### می‌گیریم

- هر <bdi dir="ltr">Module/Context API</bdi> آشکار و <bdi dir="ltr">Internal implementation</bdi> محافظت‌شده داشته باشد.
- <bdi dir="ltr">Product team autonomy</bdi> همراه <bdi dir="ltr">Platform standards</bdi> و <bdi dir="ltr">Architecture fitness test</bdi> باشد.
- <bdi dir="ltr">Event delivery</bdi> با <bdi dir="ltr">Duplicate</bdi> و <bdi dir="ltr">Replay</bdi> طراحی شود، نه <bdi dir="ltr">Happy path.</bdi>
- <bdi dir="ltr">Analytical data</bdi> را با <bdi dir="ltr">Operational Source of Truth</bdi> اشتباه نگیریم.
- <bdi dir="ltr">Compliance/Fraud</bdi> را <bdi dir="ltr">Capability</bdi> و <bdi dir="ltr">Owner</bdi> واقعی بدانیم.
- برای <bdi dir="ltr">Critical flow</bdi>، <bdi dir="ltr">Minimal viable continuity</bdi> را از <bdi dir="ltr">Full duplicate</bdi> جدا کنیم.
- تصمیم‌های <bdi dir="ltr">Technology</bdi> با <bdi dir="ltr">Revisit trigger</bdi> تاریخ‌دار باشند.

### فعلاً نمی‌گیریم

- <bdi dir="ltr">Microservice</bdi> از روز اول
- <bdi dir="ltr">Database/Queue</bdi> برای هر <bdi dir="ltr">Package</bdi>
- سه‌هزار <bdi dir="ltr">Deployable component</bdi>
- <bdi dir="ltr">Multi-cloud</bdi> قبل از داشتن <bdi dir="ltr">SLO</bdi> و <bdi dir="ltr">Failure model</bdi>
- <bdi dir="ltr">Eventual consistency</bdi> برای <bdi dir="ltr">Ledger</bdi> اصلی
- تقلید <bdi dir="ltr">Stack</bdi> بدون <bdi dir="ltr">Team/Scale/Regulatory context</bdi>

تصمیم <bdi dir="ltr">Lab</bdi> همچنان درست است: ابتدا <bdi dir="ltr">Modular Monolith</bdi>، سپس استخراج فقط با <bdi dir="ltr">Evidence.</bdi>

## 14. پنج سؤال دفاعی

1. چرا ۳۰۰۰ <bdi dir="ltr">Microservice</bdi> را نمی‌توان معادل ۳۰۰۰ <bdi dir="ltr">Bounded Context</bdi> دانست؟
2. <bdi dir="ltr">Monorepo</bdi> و <bdi dir="ltr">Migration</bdi> مرکزی چگونه با <bdi dir="ltr">Team autonomy</bdi> جمع می‌شوند؟
3. در <bdi dir="ltr">Stand-in</bdi>، <bdi dir="ltr">Owner</bdi> نهایی <bdi dir="ltr">Balance</bdi> و <bdi dir="ltr">Ledger</bdi> کیست و <bdi dir="ltr">Stand-in</bdi> چه چیزی را موقتاً <bdi dir="ltr">Authority</bdi> می‌گیرد؟
4. شکست <bdi dir="ltr">Financial Crime</bdi> بیشتر شکست <bdi dir="ltr">Technology</bdi> بود، <bdi dir="ltr">Ownership</bdi> بود یا <bdi dir="ltr">Governance</bdi>؟ با شواهد دفاع کن.
5. اگر <bdi dir="ltr">Monzo</bdi> را برای بانک بزرگ خودت الگو بگیری، کدام تصمیم را <bdi dir="ltr">Copy</bdi> نمی‌کنی و چرا؟

## <bdi dir="ltr">15. Artifact</bdi> چهل‌وپنج‌دقیقه‌ای

[<bdi dir="ltr">Day 09 Architecture Review</bdi>](../exercises/day-09-monzo-architecture-review.md) را کامل کن. خروجی باید یک صفحه باشد و شامل این سه بخش:

1. یک <bdi dir="ltr">Timeline</bdi> پنج‌نقطه‌ای
2. یک جدول <bdi dir="ltr">`Fact / Inference / Unknown`</bdi>
3. یک <bdi dir="ltr">ADR-lite:</bdi> «آیا <bdi dir="ltr">Core Banking Lab</bdi> باید <bdi dir="ltr">Microservice-first</bdi> شود؟»

## <bdi dir="ltr">16. Source register</bdi>

### تاریخ و محصول

- [<bdi dir="ltr">We Are Now a Bank</bdi> — 2016](https://monzo.com/blog/2016/08/11/we-are-now-a-bank)
- [<bdi dir="ltr">Launching the Bank</bdi> — <bdi dir="ltr">Mobilisation</bdi>](https://monzo.com/blog/2016/08/15/launching-the-bank)
- [<bdi dir="ltr">Welcome to Monzo Bank</bdi> — <bdi dir="ltr">unrestricted licence</bdi>, 2017](https://monzo.com/blog/2017/04/05/banking-licence)
- [<bdi dir="ltr">Monzo in 2019</bdi>](https://monzo.com/blog/2019/01/04/monzo-in-2019)
- [<bdi dir="ltr">FY2026 Annual Report</bdi>](https://monzo.com/annual-report)
- [<bdi dir="ltr">US account closure</bdi> — 2026](https://monzo.com/help/us-account-closure-support/us-account-closure-support)

### فناوری و معماری

- [<bdi dir="ltr">Building a Modern Bank Backend</bdi> — 2016](https://monzo.com/blog/2016/09/19/building-a-modern-bank-backend)
- [<bdi dir="ltr">How we run migrations across 2</bdi>,<bdi dir="ltr">800 microservices</bdi> — 2024](https://monzo.com/blog/how-we-run-migrations-across-2800-microservices)
- [<bdi dir="ltr">Tolerating full cloud outages with Monzo Stand-in</bdi> — 2025](https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in)
- [<bdi dir="ltr">The Engineering Behind the Platform</bdi> — 2026](https://monzo.com/blog/the-engineering-behind-the-platform)
- [<bdi dir="ltr">Incremental modelling and billions of events</bdi> — 2024](https://monzo.com/blog/how-we-use-incremental-modelling-to-handle-billions-of-events-every-day)

### شکست و کنترل

- [<bdi dir="ltr">FCA fine and findings</bdi> — 2025](https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls)

## 17. محدودیت پرونده

- <bdi dir="ltr">Source code</bdi>، <bdi dir="ltr">Service catalog</bdi>، <bdi dir="ltr">Data model</bdi> و <bdi dir="ltr">Context map</bdi> کامل <bdi dir="ltr">Monzo</bdi> عمومی نیست.
- عدد <bdi dir="ltr">Service</bdi>ها در زمان‌های مختلف ۲۸۰۰، نزدیک ۳۰۰۰ و بیش از ۳۰۰۰ گزارش شده؛ این تفاوت <bdi dir="ltr">Timeline</bdi> رشد است، نه تناقضی که باید با یک عدد ثابت پنهان شود.
- <bdi dir="ltr">Product list</bdi> را نباید <bdi dir="ltr">Bounded Context list</bdi> فرض کرد.
- <bdi dir="ltr">Current primary database technology</bdi> در منابع رسمی بررسی‌شده نام‌گذاری نشده است.
- تحلیل‌های «چرا آمریکا موفق نشد» بدون منبع رسمی در این پرونده عمداً حذف شده‌اند.

</div>
