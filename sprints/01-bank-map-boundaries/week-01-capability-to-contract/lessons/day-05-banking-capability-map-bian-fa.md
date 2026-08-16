<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 05</span> — <span dir="ltr">Banking Capability Map</span> و استفادهٔ درست از <span dir="ltr">BIAN 14</span>

- <span dir="ltr">Day budget: 70 minutes</span> — <span dir="ltr">25 lesson</span> + <span dir="ltr">20 map</span> + <span dir="ltr">20 BIAN gap check</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output: Capability Map v1</span> سطح <span dir="ltr">L1</span> و <span dir="ltr">BIAN Gap Check</span>
- <span dir="ltr">Source date: 15 August 2026</span>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Capability Map</span> سطح <span dir="ltr">L1</span> بانک را مستقل از چارت و <span dir="ltr">Application Portfolio</span> بسازی.
2. چهار لایهٔ «هسته»، «عملیات و خدمات»، «سازمانی» و «اکوسیستم دیجیتال» را به‌عنوان <span dir="ltr">Portfolio lens</span> استفاده کنی، نه <span dir="ltr">Boundary</span> قطعی.
3. <span dir="ltr">L1</span> را فقط در نقاط لازم به <span dir="ltr">L2</span> بشکنی و <span dir="ltr">Level</span>ها را مخلوط نکنی.
4. <span dir="ltr">BIAN 14</span> را برای <span dir="ltr">Vocabulary</span>، <span dir="ltr">Coverage</span> و <span dir="ltr">Gap Check</span> استفاده کنی.
5. <span dir="ltr">Service Domain</span>، <span dir="ltr">Business Capability</span>، <span dir="ltr">Control Record</span>، <span dir="ltr">API</span> و <span dir="ltr">Microservice</span> را یکی نگیری.

## <span dir="ltr">2. Capability Map</span> چیست؟

<span dir="ltr">Capability Map</span> نمای سلسله‌مراتبی و نسبتاً پایدار از توانایی‌های سازمان است. <span dir="ltr">Map</span> خوب به سه پرسش کمک می‌کند:

- برای تحقق <span dir="ltr">Strategy</span> چه توانایی‌هایی لازم داریم؟
- کدام <span dir="ltr">Capability</span> ضعیف، تکراری، پرریسک یا بی‌مالک است؟
- <span dir="ltr">Application</span>ها، داده‌ها، تیم‌ها و <span dir="ltr">Investment</span>ها روی کدام <span dir="ltr">Capability</span>ها قرار می‌گیرند؟

<span dir="ltr">Capability Map</span> پاسخ مستقیم این پرسش‌ها نیست:

- چند <span dir="ltr">Microservice</span> بسازیم؟
- مرز تراکنش کجاست؟
- کدام جدول به کدام <span dir="ltr">Schema</span> برود؟
- کدام تیم دقیقاً چند نفر داشته باشد؟

این تصمیم‌ها <span dir="ltr">Evidence</span>های دیگری می‌خواهند.

## 3. قواعد <span dir="ltr">Leveling</span>

### <span dir="ltr">L1</span>

توانایی کلان و پایدار بانک؛ برای <span dir="ltr">Portfolio</span> و <span dir="ltr">Heatmap.</span> تعداد معمولاً محدود است و همهٔ بانک را پوشش می‌دهد.

نمونه: <span dir="ltr">`مدیریت رابطه با مشتری`</span>، <span dir="ltr">`مدیریت منابع و سپرده‌ها`</span>، <span dir="ltr">`مدیریت اعتبار`</span>، <span dir="ltr">`اجرای پرداخت`</span>.

### <span dir="ltr">L2</span>

تفکیک معنادار درون <span dir="ltr">L1</span> بر اساس <span dir="ltr">Outcome/Rule/Owner.</span>


</div>

<div dir="ltr" align="left">

```text
مدیریت منابع و سپرده‌ها
├── طراحی و عرضهٔ محصول سپرده
├── ایجاد و نگهداری قرارداد سپرده
├── کنترل مانده و دسترسی به وجوه
├── محاسبه و اعمال سود
└── خاتمه و شکست قرارداد
```

</div>

<div dir="rtl" align="right">


### <span dir="ltr">L3</span>

توانایی دقیق‌تر برای تحلیل <span dir="ltr">Investment</span> و <span dir="ltr">Process</span>، بدون سقوط به <span dir="ltr">Activity</span> یا <span dir="ltr">API.</span>

مثلاً زیر «کنترل دسترسی به وجوه»: مدیریت <span dir="ltr">Hold</span>، کنترل حدود برداشت، مدیریت وضعیت حساب.

### خطای <span dir="ltr">Level mixing</span>

اگر کنار «مدیریت اعتبار» مورد «چاپ دفترچه» قرار گیرد، <span dir="ltr">Map L1</span> و <span dir="ltr">Activity</span> را مخلوط کرده است. هر ردیف خواهر باید تقریباً در یک سطح از <span dir="ltr">Granularity</span> باشد.

## 4. روش ساخت <span dir="ltr">Map</span> از صفر

### گام 1 — <span dir="ltr">Scope</span> و <span dir="ltr">Stakeholder</span>

<span dir="ltr">Scope</span> این هفته «بانک جامع» و مخاطب <span dir="ltr">Business/Architecture Portfolio</span> است. نسخه 1.0 هنوز تصمیم اجرایی نیست.

### گام 2 — <span dir="ltr">Outcome</span>های اصلی

تعهدهای بانک را از دید مشتری، رگولاتور، سهام‌دار و عملیات فهرست کن:

- شناخت طرف و رابطه
- طراحی و اجرای قرارداد مالی
- نگهداری وجوه و تعهدات
- اعطای اعتبار و وصول
- انتقال و تسویه
- ثبت و کنترل مالی
- مدیریت ریسک و انطباق
- ادارهٔ سازمان و اکوسیستم

### گام 3 — نام‌گذاری مستقل از وضع موجود

نام سامانه، <span dir="ltr">Vendor</span>، شعبه، <span dir="ltr">Mobile</span>، <span dir="ltr">Mainframe</span>، <span dir="ltr">Oracle</span> و <span dir="ltr">Kafka</span> حذف شود. اگر با حذف فناوری مفهوم از بین رفت، احتمالاً <span dir="ltr">Capability</span> نیست.

### گام 4 — <span dir="ltr">Level</span> و هم‌پوشانی

برای هر <span dir="ltr">Capability</span>، <span dir="ltr">Definition</span> و <span dir="ltr">`Includes/Excludes`</span> بنویس. دو نام مشابه بدون <span dir="ltr">Definition</span> به سرعت هم‌پوشان می‌شوند.

### گام 5 — <span dir="ltr">Owner</span> و <span dir="ltr">KPI</span> اولیه

<span dir="ltr">Owner</span> فعلی ممکن است مبهم باشد؛ <span dir="ltr">`Proposed owner`</span> و <span dir="ltr">`Ownership gap`</span> را جدا ثبت کن. <span dir="ltr">KPI</span> باید <span dir="ltr">Outcome</span> را بسنجد، نه فقط تعداد تراکنش.

### گام 6 — <span dir="ltr">Heatmap</span> اختیاری

پس از تثبیت <span dir="ltr">Map</span> می‌توان <span dir="ltr">Strategy importance</span>، <span dir="ltr">maturity</span>، <span dir="ltr">risk</span> و <span dir="ltr">change demand</span> را <span dir="ltr">Overlay</span> کرد. رنگ زیبا جای <span dir="ltr">Definition</span> و <span dir="ltr">Evidence</span> را نمی‌گیرد.

## 5. چهار لایهٔ <span dir="ltr">Portfolio</span> این دوره

| لایه | پرسش | نمونه‌ها |
|---|---|---|
| هستهٔ بانکداری | چه چیزی رابطه، قرارداد، مانده و تعهد اصلی بانک/مشتری را نگه می‌دارد؟ | <span dir="ltr">Customer</span>، <span dir="ltr">Product/Agreement</span>، <span dir="ltr">Deposits</span>، <span dir="ltr">Lending</span>، <span dir="ltr">Accounting core facts</span> |
| عملیات و خدمات بانکداری | خدمت و اجرای عملیات چگونه به شبکه، شعبه و بازار متصل می‌شود؟ | <span dir="ltr">Payments</span>، <span dir="ltr">Cards</span>، <span dir="ltr">Checks</span>، <span dir="ltr">Teller</span>، <span dir="ltr">Cash</span>، <span dir="ltr">Collections</span>، <span dir="ltr">Treasury</span> |
| توانمندی‌های سازمانی | خود بنگاه چگونه اداره می‌شود؟ | <span dir="ltr">HR</span>، <span dir="ltr">Procurement</span>، <span dir="ltr">Budget</span>، <span dir="ltr">Asset/Fleet</span>، <span dir="ltr">Portfolio governance</span> |
| اکوسیستم دیجیتال | بانک چگونه با <span dir="ltr">Partner</span> و کانال بیرونی ترکیب می‌شود؟ | <span dir="ltr">Open Banking</span>، <span dir="ltr">API partnership</span>، <span dir="ltr">Marketplace</span>، <span dir="ltr">Embedded Finance</span> |

این تقسیم‌بندی برای اولویت و <span dir="ltr">Portfolio</span> مفید است؛ هیچ ردیف آن <span dir="ltr">Bounded Context</span> یا <span dir="ltr">Deployable boundary</span> را ثابت نمی‌کند. <span dir="ltr">Payments</span> ممکن است برای یک بانک <span dir="ltr">Near Core</span> و برای بانک پرداخت‌محور بخشی از <span dir="ltr">Differentiating Core</span> باشد.

## <span dir="ltr">6. Draft</span> سطح <span dir="ltr">L1</span>

<span dir="ltr">Working Draft</span> موجود چهار شاخه دارد. امروز باید آن را نقد، <span dir="ltr">Definition</span>ها را تکمیل و به نسخهٔ 1.0 تبدیل کنی:


</div>

<div dir="ltr" align="left">

```text
Bank Capabilities
├── Core Banking
│   ├── Party & Customer Relationship
│   ├── Product, Pricing & Agreement
│   ├── Funds & Deposit Obligations
│   ├── Credit & Financing Obligations
│   └── Financial Control & Accounting
├── Banking Operations & Services
│   ├── Payments, Clearing & Settlement
│   ├── Treasury, Markets & Securities
│   ├── Branch, Teller & Cash
│   ├── Collections & Recovery
│   └── Risk, Compliance & Supervision
├── Enterprise Capabilities
│   ├── Governance & Portfolio
│   ├── Data, Reporting & Decision Support
│   ├── People, Procurement & Assets
│   └── Security & Access Management
└── Digital Ecosystem
    ├── Open Banking & API Partnership
    ├── Partner/Fintech Management
    └── Marketplace & Embedded Finance
```

</div>

<div dir="rtl" align="right">


این <span dir="ltr">Map</span> پاسخ نهایی صنعت نیست؛ فرضیهٔ دوره است و با <span dir="ltr">Domain Dossier</span>های هفته‌های بعد اصلاح می‌شود.

## <span dir="ltr">7. BIAN</span> چیست و چه چیزی نیست؟

<span dir="ltr">BIAN</span> یک انجمن و <span dir="ltr">Reference Architecture</span> برای صنعت بانکداری است که <span dir="ltr">Service Landscape</span>، <span dir="ltr">Business Capability</span>ها، <span dir="ltr">Service Domain</span>ها، الگوهای رفتاری و <span dir="ltr">Semantic API</span>ها را ارائه می‌کند. ارزش اصلی برای این هفته:

- واژگان استاندارد برای گفت‌وگو
- <span dir="ltr">Coverage check</span> و یافتن <span dir="ltr">Capability</span>های جاافتاده
- مقایسهٔ <span dir="ltr">Scope</span> و مسئولیت
- سرنخ برای <span dir="ltr">Contract</span> و <span dir="ltr">Semantic alignment</span>

<span dir="ltr">BIAN</span> این‌ها نیست:

- نقشهٔ محرمانهٔ بانک تو
- چارت سازمانی
- فهرست <span dir="ltr">Microservice</span>های آمادهٔ استقرار
- جایگزین <span dir="ltr">Event Storming</span> و تحلیل <span dir="ltr">Rule/Ownership</span>
- نسخهٔ قطعی <span dir="ltr">Data ownership</span> یا <span dir="ltr">Transaction boundary</span> محلی

## 8. اعداد نسخهٔ 14 و معنای درست آن‌ها

طبق <span dir="ltr">Release Notes</span> نسخهٔ 14، <span dir="ltr">BIAN</span> مجموعه‌ای بزرگ از <span dir="ltr">Service Domain</span>، <span dir="ltr">Business Domain</span>، <span dir="ltr">Business Capability</span> و <span dir="ltr">Semantic API</span> دارد. اعداد مرجع ثبت‌شده برای این دوره عبارت‌اند از ۳۲۲ <span dir="ltr">Service Domain</span>، ۳۸ <span dir="ltr">Business Domain</span>، ۵۸۶ <span dir="ltr">Business Capability</span> و ۲۴۲ <span dir="ltr">Semantic API.</span>

این اعداد دلیل ساخت صدها سرویس نیستند. اندازهٔ <span dir="ltr">Landscape</span> نشان‌دهندهٔ <span dir="ltr">Coverage</span> مرجع است، نه <span dir="ltr">Topology Runtime</span> بانک. هر <span dir="ltr">Fact</span> نسخه‌ای باید با [<span dir="ltr">Release Notes</span>](../references/README.md) کنترل شود.

## <span dir="ltr">9. Service Domain</span> چرا <span dir="ltr">Microservice</span> نیست؟

<span dir="ltr">Service Domain</span> یک <span dir="ltr">Partion</span> منطقی استاندارد از <span dir="ltr">Function/Behavior</span> بانکی در مدل <span dir="ltr">BIAN</span> است. برای تبدیل آن به <span dir="ltr">Deployable Service</span> هنوز باید پاسخ دهیم:

- آیا مدل و زبان محلی واقعاً یک <span dir="ltr">Boundary</span> مستقل می‌سازند؟
- <span dir="ltr">Aggregate</span> و <span dir="ltr">Transaction boundary</span> چیست؟
- <span dir="ltr">Change cadence</span> و <span dir="ltr">Team ownership</span> مستقل است؟
- <span dir="ltr">Scaling</span> و <span dir="ltr">Availability profile</span> متفاوت است؟
- هزینهٔ <span dir="ltr">Network</span>، <span dir="ltr">Consistency</span> و <span dir="ltr">Operations</span> توجیه دارد؟
- <span dir="ltr">Contract</span>های لازم و <span dir="ltr">Failure semantics</span> روشن‌اند؟

تا وقتی این <span dir="ltr">Forces</span> بررسی نشده‌اند، <span dir="ltr">Service Domain</span> فقط <span dir="ltr">Reference candidate</span> است.

## 10. روش درست <span dir="ltr">Gap Check</span>

### مرحله A — <span dir="ltr">Map</span> خودمان اول

بر اساس <span dir="ltr">Strategy</span>، محصولات، مقررات و مسئله‌های واقعی <span dir="ltr">Map</span> را بساز. از <span dir="ltr">Landscape</span> شروع نکن؛ وگرنه <span dir="ltr">Map</span> به ترجمهٔ فهرست <span dir="ltr">Vendor</span> تبدیل می‌شود.

### مرحله B — <span dir="ltr">Search</span> و <span dir="ltr">Mapping</span>

برای هر <span dir="ltr">Capability</span> محلی در <span dir="ltr">BIAN</span> جست‌وجو کن و یکی از این وضعیت‌ها را بده:

- <span dir="ltr">`MATCH`</span>: <span dir="ltr">Scope</span> نزدیک و واژگان مفید
- <span dir="ltr">`PARTIAL`</span>: بخشی از <span dir="ltr">Scope</span> مشترک است
- <span dir="ltr">`GAP-LOCAL`</span>: نیاز محلی در <span dir="ltr">BIAN</span> مستقیم پیدا نشد
- <span dir="ltr">`GAP-OUR-MAP`</span>: <span dir="ltr">BIAN</span> موردی نشان داد که در <span dir="ltr">Map</span> ما جا افتاده بود
- <span dir="ltr">`FALSE-FRIEND`</span>: نام شبیه ولی معنا/<span dir="ltr">Scope</span> متفاوت
- <span dir="ltr">`NOT-APPLICABLE`</span>: در <span dir="ltr">Scope</span> بانک/نسخهٔ ما لازم نیست

### مرحله C — <span dir="ltr">Evidence</span>، نه <span dir="ltr">Copy</span>

نام <span dir="ltr">BIAN</span>، <span dir="ltr">Definition</span> کوتاه، تفاوت <span dir="ltr">Scope</span> و تصمیم محلی را ثبت کن. <span dir="ltr">Match</span> به معنی پذیرش خودکار نیست.

### مرحله D — <span dir="ltr">Change log</span>

هر تغییر <span dir="ltr">Map</span> باید <span dir="ltr">Reason</span> داشته باشد: «افزودن <span dir="ltr">Fraud Management</span> پس از <span dir="ltr">Gap Check</span>» معتبرتر از «مطابق <span dir="ltr">BIAN</span> شد» است.

## 11. سه نمونهٔ <span dir="ltr">Gap Check</span>

### <span dir="ltr">Current Account</span>

ممکن است نام با محصول جاری محلی شبیه باشد، اما باید <span dir="ltr">Scope Service Domain</span>، <span dir="ltr">Control Record</span> و <span dir="ltr">Behavior Qualifier</span>ها بررسی شوند. نتیجه می‌تواند <span dir="ltr">`PARTIAL`</span> باشد، نه <span dir="ltr">Copy</span> مستقیم.

### <span dir="ltr">Customer Relationship Management</span>

<span dir="ltr">CRM Application</span> موجود ممکن است <span dir="ltr">Sales/Lead</span> را انجام دهد، در حالی که <span dir="ltr">Capability</span> رابطه و وضعیت <span dir="ltr">Customer</span> گسترده‌تر یا متفاوت است. نام مشترک <span dir="ltr">False Friend</span> محتمل است.

### <span dir="ltr">Financial Accounting</span>

وجود <span dir="ltr">Service Domain</span> حسابداری به معنی مالکیت ماندهٔ قابل برداشت سپرده نیست. <span dir="ltr">BIAN mapping</span>، نوع <span dir="ltr">Balance</span> و <span dir="ltr">Authority</span> محلی را تعیین نمی‌کند.

## 12. آزمون کیفیت <span dir="ltr">Capability Map v1</span>

برای هر <span dir="ltr">Node</span> بررسی کن:

1. <span dir="ltr">Outcome</span> و <span dir="ltr">Definition</span> دارد؟
2. نام <span dir="ltr">Technology/Org/Application</span> ندارد؟
3. در <span dir="ltr">Level</span> مناسب کنار خواهرهایش است؟
4. <span dir="ltr">Includes/Excludes</span> هم‌پوشانی را کنترل می‌کند؟
5. <span dir="ltr">Owner</span> پیشنهادی و <span dir="ltr">Gap</span> مالکیت ثبت شده؟
6. <span dir="ltr">BIAN status</span> و <span dir="ltr">Evidence</span> دارد؟
7. از <span dir="ltr">Node</span> به <span dir="ltr">Context</span> یا <span dir="ltr">Microservice</span> پرش نشده؟

## 13. تمرین مستقل و <span dir="ltr">Rubric</span>

[<span dir="ltr">Day 05 Exercise</span>](../exercises/day-05-capability-map-bian-gap-check.md) را انجام بده و [<span dir="ltr">Gap Check Template</span>](../artifacts/bian-gap-check-template.md) را کامل کن.

| معیار | امتیاز |
|---|---:|
| <span dir="ltr">L1</span> کامل و هم‌سطح | ۲ |
| <span dir="ltr">Definition</span> و <span dir="ltr">Includes/Excludes</span> | ۲ |
| چهارلایه با توضیح غیرقطعی | ۱ |
| حداقل ۱۰ <span dir="ltr">Mapping</span> مستند <span dir="ltr">BIAN</span> | ۲ |
| تشخیص <span dir="ltr">Gap/Partial/False Friend</span> | ۲ |
| عدم تبدیل <span dir="ltr">Service Domain</span> به <span dir="ltr">Microservice</span> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰.

## 14. آزمون خروج و منابع

درس را ببند و [<span dir="ltr">Exit Ticket</span>](../quizzes/day-05-exit-ticket.md) را پاسخ بده.

- [<span dir="ltr">BIAN Service Landscape</span>](https://bian.org/deliverables/service-landscape/)
- [<span dir="ltr">BIAN 14 Architecture Portal</span>](https://bian.org/servicelandscape-14-0-0/)
- [<span dir="ltr">References Week 01</span>](../references/README.md)

اعداد و نام‌های نسخه‌ای با تاریخ کنترل می‌شوند؛ <span dir="ltr">Domain Map</span> و چهارلایهٔ این درس <span dir="ltr">`INFERENCE/LOCAL DECISION`</span> هستند.


</div>
