<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 05</bdi> — <bdi dir="ltr">Banking Capability Map</bdi> و استفادهٔ درست از <bdi dir="ltr">BIAN 14</bdi>

- <bdi dir="ltr">Day budget: 70 minutes</bdi> — <bdi dir="ltr">25 lesson</bdi> + <bdi dir="ltr">20 map</bdi> + <bdi dir="ltr">20 BIAN gap check</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output: Capability Map v1</bdi> سطح <bdi dir="ltr">L1</bdi> و <bdi dir="ltr">BIAN Gap Check</bdi>
- <bdi dir="ltr">Source date: 15 August 2026</bdi>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Capability Map</bdi> سطح <bdi dir="ltr">L1</bdi> بانک را مستقل از چارت و <bdi dir="ltr">Application Portfolio</bdi> بسازی.
2. چهار لایهٔ «هسته»، «عملیات و خدمات»، «سازمانی» و «اکوسیستم دیجیتال» را به‌عنوان <bdi dir="ltr">Portfolio lens</bdi> استفاده کنی، نه <bdi dir="ltr">Boundary</bdi> قطعی.
3. <bdi dir="ltr">L1</bdi> را فقط در نقاط لازم به <bdi dir="ltr">L2</bdi> بشکنی و <bdi dir="ltr">Level</bdi>ها را مخلوط نکنی.
4. <bdi dir="ltr">BIAN 14</bdi> را برای <bdi dir="ltr">Vocabulary</bdi>، <bdi dir="ltr">Coverage</bdi> و <bdi dir="ltr">Gap Check</bdi> استفاده کنی.
5. <bdi dir="ltr">Service Domain</bdi>، <bdi dir="ltr">Business Capability</bdi>، <bdi dir="ltr">Control Record</bdi>، <bdi dir="ltr">API</bdi> و <bdi dir="ltr">Microservice</bdi> را یکی نگیری.

## <bdi dir="ltr">2. Capability Map</bdi> چیست؟

<bdi dir="ltr">Capability Map</bdi> نمای سلسله‌مراتبی و نسبتاً پایدار از توانایی‌های سازمان است. <bdi dir="ltr">Map</bdi> خوب به سه پرسش کمک می‌کند:

- برای تحقق <bdi dir="ltr">Strategy</bdi> چه توانایی‌هایی لازم داریم؟
- کدام <bdi dir="ltr">Capability</bdi> ضعیف، تکراری، پرریسک یا بی‌مالک است؟
- <bdi dir="ltr">Application</bdi>ها، داده‌ها، تیم‌ها و <bdi dir="ltr">Investment</bdi>ها روی کدام <bdi dir="ltr">Capability</bdi>ها قرار می‌گیرند؟

<bdi dir="ltr">Capability Map</bdi> پاسخ مستقیم این پرسش‌ها نیست:

- چند <bdi dir="ltr">Microservice</bdi> بسازیم؟
- مرز تراکنش کجاست؟
- کدام جدول به کدام <bdi dir="ltr">Schema</bdi> برود؟
- کدام تیم دقیقاً چند نفر داشته باشد؟

این تصمیم‌ها <bdi dir="ltr">Evidence</bdi>های دیگری می‌خواهند.

## 3. قواعد <bdi dir="ltr">Leveling</bdi>

### <bdi dir="ltr">L1</bdi>

توانایی کلان و پایدار بانک؛ برای <bdi dir="ltr">Portfolio</bdi> و <bdi dir="ltr">Heatmap.</bdi> تعداد معمولاً محدود است و همهٔ بانک را پوشش می‌دهد.

نمونه: <bdi dir="ltr">`مدیریت رابطه با مشتری`</bdi>، <bdi dir="ltr">`مدیریت منابع و سپرده‌ها`</bdi>، <bdi dir="ltr">`مدیریت اعتبار`</bdi>، <bdi dir="ltr">`اجرای پرداخت`</bdi>.

### <bdi dir="ltr">L2</bdi>

تفکیک معنادار درون <bdi dir="ltr">L1</bdi> بر اساس <bdi dir="ltr">Outcome/Rule/Owner.</bdi>


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


### <bdi dir="ltr">L3</bdi>

توانایی دقیق‌تر برای تحلیل <bdi dir="ltr">Investment</bdi> و <bdi dir="ltr">Process</bdi>، بدون سقوط به <bdi dir="ltr">Activity</bdi> یا <bdi dir="ltr">API.</bdi>

مثلاً زیر «کنترل دسترسی به وجوه»: مدیریت <bdi dir="ltr">Hold</bdi>، کنترل حدود برداشت، مدیریت وضعیت حساب.

### خطای <bdi dir="ltr">Level mixing</bdi>

اگر کنار «مدیریت اعتبار» مورد «چاپ دفترچه» قرار گیرد، <bdi dir="ltr">Map L1</bdi> و <bdi dir="ltr">Activity</bdi> را مخلوط کرده است. هر ردیف خواهر باید تقریباً در یک سطح از <bdi dir="ltr">Granularity</bdi> باشد.

## 4. روش ساخت <bdi dir="ltr">Map</bdi> از صفر

### گام 1 — <bdi dir="ltr">Scope</bdi> و <bdi dir="ltr">Stakeholder</bdi>

<bdi dir="ltr">Scope</bdi> این هفته «بانک جامع» و مخاطب <bdi dir="ltr">Business/Architecture Portfolio</bdi> است. نسخه 1.0 هنوز تصمیم اجرایی نیست.

### گام 2 — <bdi dir="ltr">Outcome</bdi>های اصلی

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

نام سامانه، <bdi dir="ltr">Vendor</bdi>، شعبه، <bdi dir="ltr">Mobile</bdi>، <bdi dir="ltr">Mainframe</bdi>، <bdi dir="ltr">Oracle</bdi> و <bdi dir="ltr">Kafka</bdi> حذف شود. اگر با حذف فناوری مفهوم از بین رفت، احتمالاً <bdi dir="ltr">Capability</bdi> نیست.

### گام 4 — <bdi dir="ltr">Level</bdi> و هم‌پوشانی

برای هر <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Definition</bdi> و <bdi dir="ltr">`Includes/Excludes`</bdi> بنویس. دو نام مشابه بدون <bdi dir="ltr">Definition</bdi> به سرعت هم‌پوشان می‌شوند.

### گام 5 — <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">KPI</bdi> اولیه

<bdi dir="ltr">Owner</bdi> فعلی ممکن است مبهم باشد؛ <bdi dir="ltr">`Proposed owner`</bdi> و <bdi dir="ltr">`Ownership gap`</bdi> را جدا ثبت کن. <bdi dir="ltr">KPI</bdi> باید <bdi dir="ltr">Outcome</bdi> را بسنجد، نه فقط تعداد تراکنش.

### گام 6 — <bdi dir="ltr">Heatmap</bdi> اختیاری

پس از تثبیت <bdi dir="ltr">Map</bdi> می‌توان <bdi dir="ltr">Strategy importance</bdi>، <bdi dir="ltr">maturity</bdi>، <bdi dir="ltr">risk</bdi> و <bdi dir="ltr">change demand</bdi> را <bdi dir="ltr">Overlay</bdi> کرد. رنگ زیبا جای <bdi dir="ltr">Definition</bdi> و <bdi dir="ltr">Evidence</bdi> را نمی‌گیرد.

## 5. چهار لایهٔ <bdi dir="ltr">Portfolio</bdi> این دوره

| لایه | پرسش | نمونه‌ها |
|---|---|---|
| هستهٔ بانکداری | چه چیزی رابطه، قرارداد، مانده و تعهد اصلی بانک/مشتری را نگه می‌دارد؟ | <bdi dir="ltr">Customer</bdi>، <bdi dir="ltr">Product/Agreement</bdi>، <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Accounting core facts</bdi> |
| عملیات و خدمات بانکداری | خدمت و اجرای عملیات چگونه به شبکه، شعبه و بازار متصل می‌شود؟ | <bdi dir="ltr">Payments</bdi>، <bdi dir="ltr">Cards</bdi>، <bdi dir="ltr">Checks</bdi>، <bdi dir="ltr">Teller</bdi>، <bdi dir="ltr">Cash</bdi>، <bdi dir="ltr">Collections</bdi>، <bdi dir="ltr">Treasury</bdi> |
| توانمندی‌های سازمانی | خود بنگاه چگونه اداره می‌شود؟ | <bdi dir="ltr">HR</bdi>، <bdi dir="ltr">Procurement</bdi>، <bdi dir="ltr">Budget</bdi>، <bdi dir="ltr">Asset/Fleet</bdi>، <bdi dir="ltr">Portfolio governance</bdi> |
| اکوسیستم دیجیتال | بانک چگونه با <bdi dir="ltr">Partner</bdi> و کانال بیرونی ترکیب می‌شود؟ | <bdi dir="ltr">Open Banking</bdi>، <bdi dir="ltr">API partnership</bdi>، <bdi dir="ltr">Marketplace</bdi>، <bdi dir="ltr">Embedded Finance</bdi> |

این تقسیم‌بندی برای اولویت و <bdi dir="ltr">Portfolio</bdi> مفید است؛ هیچ ردیف آن <bdi dir="ltr">Bounded Context</bdi> یا <bdi dir="ltr">Deployable boundary</bdi> را ثابت نمی‌کند. <bdi dir="ltr">Payments</bdi> ممکن است برای یک بانک <bdi dir="ltr">Near Core</bdi> و برای بانک پرداخت‌محور بخشی از <bdi dir="ltr">Differentiating Core</bdi> باشد.

## <bdi dir="ltr">6. Draft</bdi> سطح <bdi dir="ltr">L1</bdi>

<bdi dir="ltr">Working Draft</bdi> موجود چهار شاخه دارد. امروز باید آن را نقد، <bdi dir="ltr">Definition</bdi>ها را تکمیل و به نسخهٔ 1.0 تبدیل کنی:


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


این <bdi dir="ltr">Map</bdi> پاسخ نهایی صنعت نیست؛ فرضیهٔ دوره است و با <bdi dir="ltr">Domain Dossier</bdi>های هفته‌های بعد اصلاح می‌شود.

## <bdi dir="ltr">7. BIAN</bdi> چیست و چه چیزی نیست؟

<bdi dir="ltr">BIAN</bdi> یک انجمن و <bdi dir="ltr">Reference Architecture</bdi> برای صنعت بانکداری است که <bdi dir="ltr">Service Landscape</bdi>، <bdi dir="ltr">Business Capability</bdi>ها، <bdi dir="ltr">Service Domain</bdi>ها، الگوهای رفتاری و <bdi dir="ltr">Semantic API</bdi>ها را ارائه می‌کند. ارزش اصلی برای این هفته:

- واژگان استاندارد برای گفت‌وگو
- <bdi dir="ltr">Coverage check</bdi> و یافتن <bdi dir="ltr">Capability</bdi>های جاافتاده
- مقایسهٔ <bdi dir="ltr">Scope</bdi> و مسئولیت
- سرنخ برای <bdi dir="ltr">Contract</bdi> و <bdi dir="ltr">Semantic alignment</bdi>

<bdi dir="ltr">BIAN</bdi> این‌ها نیست:

- نقشهٔ محرمانهٔ بانک تو
- چارت سازمانی
- فهرست <bdi dir="ltr">Microservice</bdi>های آمادهٔ استقرار
- جایگزین <bdi dir="ltr">Event Storming</bdi> و تحلیل <bdi dir="ltr">Rule/Ownership</bdi>
- نسخهٔ قطعی <bdi dir="ltr">Data ownership</bdi> یا <bdi dir="ltr">Transaction boundary</bdi> محلی

## 8. اعداد نسخهٔ 14 و معنای درست آن‌ها

طبق <bdi dir="ltr">Release Notes</bdi> نسخهٔ 14، <bdi dir="ltr">BIAN</bdi> مجموعه‌ای بزرگ از <bdi dir="ltr">Service Domain</bdi>، <bdi dir="ltr">Business Domain</bdi>، <bdi dir="ltr">Business Capability</bdi> و <bdi dir="ltr">Semantic API</bdi> دارد. اعداد مرجع ثبت‌شده برای این دوره عبارت‌اند از ۳۲۲ <bdi dir="ltr">Service Domain</bdi>، ۳۸ <bdi dir="ltr">Business Domain</bdi>، ۵۸۶ <bdi dir="ltr">Business Capability</bdi> و ۲۴۲ <bdi dir="ltr">Semantic API.</bdi>

این اعداد دلیل ساخت صدها سرویس نیستند. اندازهٔ <bdi dir="ltr">Landscape</bdi> نشان‌دهندهٔ <bdi dir="ltr">Coverage</bdi> مرجع است، نه <bdi dir="ltr">Topology Runtime</bdi> بانک. هر <bdi dir="ltr">Fact</bdi> نسخه‌ای باید با [<bdi dir="ltr">Release Notes</bdi>](../references/README.md) کنترل شود.

## <bdi dir="ltr">9. Service Domain</bdi> چرا <bdi dir="ltr">Microservice</bdi> نیست؟

<bdi dir="ltr">Service Domain</bdi> یک <bdi dir="ltr">Partion</bdi> منطقی استاندارد از <bdi dir="ltr">Function/Behavior</bdi> بانکی در مدل <bdi dir="ltr">BIAN</bdi> است. برای تبدیل آن به <bdi dir="ltr">Deployable Service</bdi> هنوز باید پاسخ دهیم:

- آیا مدل و زبان محلی واقعاً یک <bdi dir="ltr">Boundary</bdi> مستقل می‌سازند؟
- <bdi dir="ltr">Aggregate</bdi> و <bdi dir="ltr">Transaction boundary</bdi> چیست؟
- <bdi dir="ltr">Change cadence</bdi> و <bdi dir="ltr">Team ownership</bdi> مستقل است؟
- <bdi dir="ltr">Scaling</bdi> و <bdi dir="ltr">Availability profile</bdi> متفاوت است؟
- هزینهٔ <bdi dir="ltr">Network</bdi>، <bdi dir="ltr">Consistency</bdi> و <bdi dir="ltr">Operations</bdi> توجیه دارد؟
- <bdi dir="ltr">Contract</bdi>های لازم و <bdi dir="ltr">Failure semantics</bdi> روشن‌اند؟

تا وقتی این <bdi dir="ltr">Forces</bdi> بررسی نشده‌اند، <bdi dir="ltr">Service Domain</bdi> فقط <bdi dir="ltr">Reference candidate</bdi> است.

## 10. روش درست <bdi dir="ltr">Gap Check</bdi>

### مرحله A — <bdi dir="ltr">Map</bdi> خودمان اول

بر اساس <bdi dir="ltr">Strategy</bdi>، محصولات، مقررات و مسئله‌های واقعی <bdi dir="ltr">Map</bdi> را بساز. از <bdi dir="ltr">Landscape</bdi> شروع نکن؛ وگرنه <bdi dir="ltr">Map</bdi> به ترجمهٔ فهرست <bdi dir="ltr">Vendor</bdi> تبدیل می‌شود.

### مرحله B — <bdi dir="ltr">Search</bdi> و <bdi dir="ltr">Mapping</bdi>

برای هر <bdi dir="ltr">Capability</bdi> محلی در <bdi dir="ltr">BIAN</bdi> جست‌وجو کن و یکی از این وضعیت‌ها را بده:

- <bdi dir="ltr">`MATCH`</bdi>: <bdi dir="ltr">Scope</bdi> نزدیک و واژگان مفید
- <bdi dir="ltr">`PARTIAL`</bdi>: بخشی از <bdi dir="ltr">Scope</bdi> مشترک است
- <bdi dir="ltr">`GAP-LOCAL`</bdi>: نیاز محلی در <bdi dir="ltr">BIAN</bdi> مستقیم پیدا نشد
- <bdi dir="ltr">`GAP-OUR-MAP`</bdi>: <bdi dir="ltr">BIAN</bdi> موردی نشان داد که در <bdi dir="ltr">Map</bdi> ما جا افتاده بود
- <bdi dir="ltr">`FALSE-FRIEND`</bdi>: نام شبیه ولی معنا/<bdi dir="ltr">Scope</bdi> متفاوت
- <bdi dir="ltr">`NOT-APPLICABLE`</bdi>: در <bdi dir="ltr">Scope</bdi> بانک/نسخهٔ ما لازم نیست

### مرحله C — <bdi dir="ltr">Evidence</bdi>، نه <bdi dir="ltr">Copy</bdi>

نام <bdi dir="ltr">BIAN</bdi>، <bdi dir="ltr">Definition</bdi> کوتاه، تفاوت <bdi dir="ltr">Scope</bdi> و تصمیم محلی را ثبت کن. <bdi dir="ltr">Match</bdi> به معنی پذیرش خودکار نیست.

### مرحله D — <bdi dir="ltr">Change log</bdi>

هر تغییر <bdi dir="ltr">Map</bdi> باید <bdi dir="ltr">Reason</bdi> داشته باشد: «افزودن <bdi dir="ltr">Fraud Management</bdi> پس از <bdi dir="ltr">Gap Check</bdi>» معتبرتر از «مطابق <bdi dir="ltr">BIAN</bdi> شد» است.

## 11. سه نمونهٔ <bdi dir="ltr">Gap Check</bdi>

### <bdi dir="ltr">Current Account</bdi>

ممکن است نام با محصول جاری محلی شبیه باشد، اما باید <bdi dir="ltr">Scope Service Domain</bdi>، <bdi dir="ltr">Control Record</bdi> و <bdi dir="ltr">Behavior Qualifier</bdi>ها بررسی شوند. نتیجه می‌تواند <bdi dir="ltr">`PARTIAL`</bdi> باشد، نه <bdi dir="ltr">Copy</bdi> مستقیم.

### <bdi dir="ltr">Customer Relationship Management</bdi>

<bdi dir="ltr">CRM Application</bdi> موجود ممکن است <bdi dir="ltr">Sales/Lead</bdi> را انجام دهد، در حالی که <bdi dir="ltr">Capability</bdi> رابطه و وضعیت <bdi dir="ltr">Customer</bdi> گسترده‌تر یا متفاوت است. نام مشترک <bdi dir="ltr">False Friend</bdi> محتمل است.

### <bdi dir="ltr">Financial Accounting</bdi>

وجود <bdi dir="ltr">Service Domain</bdi> حسابداری به معنی مالکیت ماندهٔ قابل برداشت سپرده نیست. <bdi dir="ltr">BIAN mapping</bdi>، نوع <bdi dir="ltr">Balance</bdi> و <bdi dir="ltr">Authority</bdi> محلی را تعیین نمی‌کند.

## 12. آزمون کیفیت <bdi dir="ltr">Capability Map v1</bdi>

برای هر <bdi dir="ltr">Node</bdi> بررسی کن:

1. <bdi dir="ltr">Outcome</bdi> و <bdi dir="ltr">Definition</bdi> دارد؟
2. نام <bdi dir="ltr">Technology/Org/Application</bdi> ندارد؟
3. در <bdi dir="ltr">Level</bdi> مناسب کنار خواهرهایش است؟
4. <bdi dir="ltr">Includes/Excludes</bdi> هم‌پوشانی را کنترل می‌کند؟
5. <bdi dir="ltr">Owner</bdi> پیشنهادی و <bdi dir="ltr">Gap</bdi> مالکیت ثبت شده؟
6. <bdi dir="ltr">BIAN status</bdi> و <bdi dir="ltr">Evidence</bdi> دارد؟
7. از <bdi dir="ltr">Node</bdi> به <bdi dir="ltr">Context</bdi> یا <bdi dir="ltr">Microservice</bdi> پرش نشده؟

## 13. تمرین مستقل و <bdi dir="ltr">Rubric</bdi>

[<bdi dir="ltr">Day 05 Exercise</bdi>](../exercises/day-05-capability-map-bian-gap-check.md) را انجام بده و [<bdi dir="ltr">Gap Check Template</bdi>](../artifacts/bian-gap-check-template.md) را کامل کن.

| معیار | امتیاز |
|---|---:|
| <bdi dir="ltr">L1</bdi> کامل و هم‌سطح | ۲ |
| <bdi dir="ltr">Definition</bdi> و <bdi dir="ltr">Includes/Excludes</bdi> | ۲ |
| چهارلایه با توضیح غیرقطعی | ۱ |
| حداقل ۱۰ <bdi dir="ltr">Mapping</bdi> مستند <bdi dir="ltr">BIAN</bdi> | ۲ |
| تشخیص <bdi dir="ltr">Gap/Partial/False Friend</bdi> | ۲ |
| عدم تبدیل <bdi dir="ltr">Service Domain</bdi> به <bdi dir="ltr">Microservice</bdi> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰.

## 14. آزمون خروج و منابع

درس را ببند و [<bdi dir="ltr">Exit Ticket</bdi>](../quizzes/day-05-exit-ticket.md) را پاسخ بده.

- [<bdi dir="ltr">BIAN Service Landscape</bdi>](https://bian.org/deliverables/service-landscape/)
- [<bdi dir="ltr">BIAN 14 Architecture Portal</bdi>](https://bian.org/servicelandscape-14-0-0/)
- [<bdi dir="ltr">References Week 01</bdi>](../references/README.md)

اعداد و نام‌های نسخه‌ای با تاریخ کنترل می‌شوند؛ <bdi dir="ltr">Domain Map</bdi> و چهارلایهٔ این درس <bdi dir="ltr">`INFERENCE/LOCAL DECISION`</bdi> هستند.


</div>
