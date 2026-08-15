<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 02</bdi> — <bdi dir="ltr">Capability</bdi> در برابر <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Business Service</bdi> و <bdi dir="ltr">System</bdi>

- <bdi dir="ltr">Day budget: 45 minutes</bdi> — <bdi dir="ltr">22 lesson</bdi> + <bdi dir="ltr">18 exercise</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output: Distinction Matrix</bdi> برای ۱۵ مثال بانکی
- <bdi dir="ltr">Banking case:</bdi> افتتاح سپرده، اعطای تسهیلات، انتقال وجه و مسدودی قضایی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Business Capability</bdi> را بدون استفاده از نام سامانه یا فناوری تعریف کنی.
2. <bdi dir="ltr">Capability</bdi> را از <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Value Stream</bdi>، <bdi dir="ltr">Business Service</bdi>، <bdi dir="ltr">Product</bdi>، <bdi dir="ltr">System</bdi>، <bdi dir="ltr">Organization Unit</bdi> و <bdi dir="ltr">API</bdi> جدا کنی.
3. یک عبارت مبهم بانکی را با آزمون‌های مشخص طبقه‌بندی کنی.
4. برای هر <bdi dir="ltr">Capability</bdi>، <bdi dir="ltr">Outcome</bdi>، <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">KPI</bdi> اولیه پیشنهاد بدهی.
5. تشخیص بدهی چه زمانی یک نام ظاهراً دامینی هنوز فقط نام <bdi dir="ltr">Legacy Application</bdi> است.

## 2. مسئلهٔ واقعی

در نقشه‌های سازمانی معمولاً فهرستی مانند زیر می‌بینیم:

- سامانهٔ تسهیلات
- ادارهٔ چک
- سرویس افتتاح حساب
- <bdi dir="ltr">API</bdi> استعلام مانده
- فرایند انتقال وجه
- محصول سپردهٔ کوتاه‌مدت

اگر همهٔ این موارد را در یک سطح از <bdi dir="ltr">Diagram</bdi> بگذاریم، <bdi dir="ltr">Map</bdi> از همان ابتدا چند نوع چیز متفاوت را مخلوط کرده است. نتیجه این می‌شود که تیم‌ها از روی نام‌های موجود <bdi dir="ltr">Service</bdi> می‌سازند، مالکیت تصمیم مبهم می‌ماند و تغییر یک <bdi dir="ltr">Capability</bdi> به چند سامانهٔ بدون مرز پخش می‌شود.

## 3. تعریف عملیاتی <bdi dir="ltr">Business Capability</bdi>

<bdi dir="ltr">Business Capability</bdi> بیان می‌کند **سازمان چه توانایی نسبتاً پایداری باید داشته باشد تا <bdi dir="ltr">Outcome</bdi> کسب‌وکاری تولید کند**؛ مستقل از اینکه امروز این توانایی با کدام فرایند، تیم، نرم‌افزار، <bdi dir="ltr">Vendor</bdi> یا فناوری اجرا می‌شود.

نمونه‌های مناسب:

- مدیریت رابطه با مشتری
- نگهداری وجوه مشتری
- مدیریت تعهدات اعتباری
- اجرای پرداخت و انتقال وجه
- اعمال محدودیت و مسدودی روی وجوه
- ثبت و گزارش آثار مالی

نمونه‌های نامناسب:

- <bdi dir="ltr">`LoanSystem`</bdi>؛ نام راه‌حل یا <bdi dir="ltr">Application</bdi> است.
- «بررسی درخواست در سه مرحله»؛ <bdi dir="ltr">Process</bdi> است.
- <bdi dir="ltr">`POST /loans`</bdi>؛ <bdi dir="ltr">Contract</bdi> فنی است.
- «ادارهٔ اعتبارات»؛ واحد سازمانی است.
- «وام مرابحهٔ فرهنگیان»؛ <bdi dir="ltr">Product/Offering</bdi> است.

<bdi dir="ltr">Capability</bdi> پاسخ <bdi dir="ltr">`what`</bdi> سازمانی است، نه <bdi dir="ltr">`how`</bdi> اجرایی.

## 4. هفت مفهوم مجاور

### <bdi dir="ltr">4.1 Process</bdi>

<bdi dir="ltr">Process</bdi> توالی فعالیت‌ها، تصمیم‌ها و <bdi dir="ltr">Hand-off</bdi>ها برای رسیدن به نتیجه است. <bdi dir="ltr">Process</bdi> تغییرپذیرتر از <bdi dir="ltr">Capability</bdi> است.


</div>

<div dir="ltr" align="left">

```text
Capability: مدیریت سپرده
Process: دریافت درخواست → احراز هویت → کنترل محصول → افتتاح → ابلاغ نتیجه
```

</div>

<div dir="rtl" align="right">


با حذف امضای کاغذی و افزودن <bdi dir="ltr">Video KYC</bdi>، <bdi dir="ltr">Process</bdi> تغییر می‌کند؛ <bdi dir="ltr">Capability</bdi> افتتاح و نگهداری رابطهٔ سپرده باقی می‌ماند.

### <bdi dir="ltr">4.2 Value Stream</bdi>

<bdi dir="ltr">Value Stream</bdi> جریان ایجاد ارزش برای ذی‌نفع از <bdi dir="ltr">Trigger</bdi> تا <bdi dir="ltr">Outcome</bdi> است و می‌تواند چند <bdi dir="ltr">Capability</bdi> و چند <bdi dir="ltr">Process</bdi> را درگیر کند. «از درخواست تسهیلات تا دریافت وجه» یک <bdi dir="ltr">Value Stream</bdi> است، نه یک <bdi dir="ltr">Capability</bdi> منفرد.

### <bdi dir="ltr">4.3 Business Service</bdi>

<bdi dir="ltr">Business Service</bdi> نمای قابل‌مصرف یک یا چند <bdi dir="ltr">Capability</bdi> برای مشتری یا شریک است. «خدمت انتقال آنی وجه» چیزی است که مصرف‌کننده دریافت می‌کند؛ پشت آن <bdi dir="ltr">Capability</bdi>های ثبت دستور پرداخت، کنترل ریسک، جابه‌جایی وجه، تسویه و رسیدگی به مغایرت قرار دارند.

<bdi dir="ltr">Business Service</bdi> با <bdi dir="ltr">`REST service`</bdi> یا <bdi dir="ltr">Microservice</bdi> یکی نیست.

### <bdi dir="ltr">4.4 Product/Offering</bdi>

<bdi dir="ltr">Product</bdi> بسته‌ای از ویژگی، قیمت، شرایط و تعهد قابل‌عرضه به بازار است. «سپردهٔ بلندمدت یک‌ساله» محصول است. <bdi dir="ltr">Capability</bdi> «طراحی و مدیریت محصول» یا «نگهداری سپرده» است.

### <bdi dir="ltr">4.5 Organization Unit/Team</bdi>

واحد سازمانی پاسخ می‌دهد چه کسانی مسئول کارند. <bdi dir="ltr">Capability</bdi> پاسخ می‌دهد سازمان چه توانایی‌ای لازم دارد. یک تیم ممکن است چند <bdi dir="ltr">Capability</bdi> را پوشش دهد و یک <bdi dir="ltr">Capability</bdi> ممکن است میان چند واحد پراکنده باشد؛ این پراکندگی خود یک <bdi dir="ltr">Risk</bdi> برای <bdi dir="ltr">Ownership</bdi> است.

### <bdi dir="ltr">4.6 Application/System</bdi>

<bdi dir="ltr">System</bdi> پیاده‌سازی فعلی بخشی از توانمندی‌هاست. «سامانه سپرده» ممکن است افتتاح، مانده، سود، <bdi dir="ltr">Hold</bdi> و گزارش را یکجا انجام دهد. این واقعیت <bdi dir="ltr">Legacy</bdi> نه اثبات می‌کند همهٔ آن‌ها یک <bdi dir="ltr">Capability</bdi> هستند و نه اثبات می‌کند باید یک <bdi dir="ltr">Bounded Context</bdi> بمانند.

### <bdi dir="ltr">4.7 API/Event</bdi>

<bdi dir="ltr">API</bdi> و <bdi dir="ltr">Event</bdi> قرارداد تعامل‌اند. <bdi dir="ltr">`GET /accounts/{id}/balance`</bdi> یک <bdi dir="ltr">Query Contract</bdi> است؛ <bdi dir="ltr">`FundsHeld`</bdi> یک <bdi dir="ltr">Fact</bdi> منتشرشده است. هیچ‌کدام به‌تنهایی <bdi dir="ltr">Capability</bdi> نیستند.

## 5. جدول تشخیص سریع

| نوع | پرسش تشخیصی | نسبت پایداری | مثال بانکی |
|---|---|---|---|
| <bdi dir="ltr">Capability</bdi> | بانک باید چه کاری بتواند انجام دهد؟ | زیاد | مدیریت تعهدات اعتباری |
| <bdi dir="ltr">Value Stream</bdi> | ارزش از چه <bdi dir="ltr">Trigger</bdi> تا چه <bdi dir="ltr">Outcome</bdi> ایجاد می‌شود؟ | متوسط | از درخواست وام تا دریافت وجه |
| <bdi dir="ltr">Process</bdi> | کار با چه توالی انجام می‌شود؟ | متوسط/کم | فرایند افتتاح سپرده |
| <bdi dir="ltr">Business Service</bdi> | چه خدمتی به مصرف‌کننده عرضه می‌شود؟ | متوسط | انتقال آنی وجه |
| <bdi dir="ltr">Product</bdi> | چه بستهٔ شرایطی عرضه می‌شود؟ | متوسط | سپردهٔ یک‌ساله |
| <bdi dir="ltr">Org Unit</bdi> | چه گروهی پاسخ‌گوست؟ | کم/متوسط | ادارهٔ اعتبارات |
| <bdi dir="ltr">System</bdi> | اکنون با چه راه‌حلی اجرا می‌شود؟ | کم | سامانهٔ تسهیلات |
| <bdi dir="ltr">API/Event</bdi> | تعامل با چه <bdi dir="ltr">Contract</bdi>ی انجام می‌شود؟ | کم | <bdi dir="ltr">`LoanDisbursed`</bdi> |

## 6. آزمون شش‌گانهٔ <bdi dir="ltr">Capability</bdi>

برای هر نام پیشنهادی شش سؤال بپرس:

1. آیا <bdi dir="ltr">Outcome</bdi> کسب‌وکاری قابل تعریف دارد؟
2. آیا بدون اشاره به فناوری یا نرم‌افزار قابل بیان است؟
3. آیا با تغییر <bdi dir="ltr">Process</bdi> هنوز باقی می‌ماند؟
4. آیا <bdi dir="ltr">Business Owner</bdi> قابل تعیین دارد؟
5. آیا <bdi dir="ltr">KPI</bdi> یا سطح بلوغ برای آن قابل سنجش است؟
6. آیا نام آن «توانایی» را می‌رساند، نه یک شیء، کانال یا واحد؟

اگر پاسخ چند سؤال منفی است، مورد احتمالاً <bdi dir="ltr">Capability</bdi> نیست یا نام‌گذاری آن ضعیف است.

## 7. پانزده مثال طبقه‌بندی‌شده

| عبارت | نوع غالب | دلیل کوتاه |
|---|---|---|
| مدیریت هویت و رابطهٔ مشتری | <bdi dir="ltr">Capability</bdi> | توانایی پایدار و <bdi dir="ltr">Outcome</bdi> محور |
| افتتاح حساب غیرحضوری | <bdi dir="ltr">Business Service/Process</bdi> | خدمت قابل‌عرضه با جریان اجرایی مشخص |
| سپردهٔ قرض‌الحسنه جاری | <bdi dir="ltr">Product</bdi> | بستهٔ شرایط و تعهد |
| سامانهٔ سپرده | <bdi dir="ltr">System</bdi> | راه‌حل نرم‌افزاری موجود |
| محاسبهٔ سود روزشمار | <bdi dir="ltr">Domain Rule/Process step</bdi> | قاعده یا فعالیت در <bdi dir="ltr">Capability</bdi> بزرگ‌تر |
| نگهداری وجوه مشتری | <bdi dir="ltr">Capability</bdi> | توانایی بنیادی بانک |
| ادارهٔ شعب | <bdi dir="ltr">Organization Unit</bdi> | ساختار پاسخ‌گویی |
| خدمت مسدودی قضایی | <bdi dir="ltr">Business Service</bdi> | نمای خدمت برای مرجع/عملیات |
| اعمال <bdi dir="ltr">Hold</bdi> روی ماندهٔ قابل برداشت | <bdi dir="ltr">Use Case</bdi> | قصد مشخص در یک <bdi dir="ltr">Context</bdi> |
| <bdi dir="ltr">`POST /holds`</bdi> | <bdi dir="ltr">API Operation</bdi> | <bdi dir="ltr">Contract</bdi> فنی |
| <bdi dir="ltr">`FundsHeld`</bdi> | <bdi dir="ltr">Event</bdi> | <bdi dir="ltr">Fact</bdi> رخ‌داده |
| از درخواست وام تا واریز | <bdi dir="ltr">Value Stream</bdi> | جریان <bdi dir="ltr">End-to-end</bdi> ارزش |
| ارزیابی اهلیت اعتباری | <bdi dir="ltr">Capability</bdi> | توانایی تصمیم‌گیری اعتباری |
| کمیتهٔ اعتباری | <bdi dir="ltr">Organization/Decision mechanism</bdi> | سازوکار تصمیم فعلی |
| <bdi dir="ltr">Core Banking</bdi> | <bdi dir="ltr">Portfolio/System landscape label</bdi> | برچسب سبد؛ نه <bdi dir="ltr">Capability</bdi> منفرد |

طبقه‌بندی همیشه فقط یک برچسب ندارد. «افتتاح حساب غیرحضوری» از دید مشتری <bdi dir="ltr">Business Service</bdi> و از دید عملیات یک <bdi dir="ltr">Process</bdi> است. نکته این است که سطح مورد استفاده در <bdi dir="ltr">Diagram</bdi> صریح باشد.

## 8. نام‌گذاری <bdi dir="ltr">Capability</bdi>

نام خوب معمولاً از یک فعل/توانایی پایدار و یک موضوع کسب‌وکاری تشکیل می‌شود:


</div>

<div dir="ltr" align="left">

```text
Manage Customer Relationship
Manage Deposit Obligations
Assess Creditworthiness
Execute Payments
Control Financial Position
```

</div>

<div dir="rtl" align="right">


اما «مدیریت» را کورکورانه به همه‌چیز اضافه نکن. نام باید مرز معنا را روشن کند. «مدیریت امور بانکی» هیچ مرزی نمی‌دهد.

### نشانه‌های نام بد

- پسوند <bdi dir="ltr">`System`</bdi>، <bdi dir="ltr">`Platform`</bdi>، <bdi dir="ltr">`Portal`</bdi> یا نام <bdi dir="ltr">Vendor</bdi>
- نام جدول یا <bdi dir="ltr">Entity</bdi> فنی
- نام کانال مانند <bdi dir="ltr">Mobile/Branch</bdi> در <bdi dir="ltr">L1</bdi>
- عبارت بسیار ریز و عملیاتی مانند «چاپ رسید»
- عبارت بسیار کلان مانند «بانکداری»
- ترکیب چند توانایی با «و» بدون <bdi dir="ltr">Outcome</bdi> مشترک

## <bdi dir="ltr">9. Capability</bdi> با <bdi dir="ltr">Bounded Context</bdi> یکی نیست

<bdi dir="ltr">Capability</bdi> از منظر <bdi dir="ltr">Business Architecture</bdi> توانایی سازمان را بیان می‌کند. <bdi dir="ltr">Bounded Context</bdi> از منظر مدل‌سازی، مرز اعتبار یک مدل و زبان را تعیین می‌کند. نگاشت آن‌ها ممکن است:

- یک <bdi dir="ltr">Capability</bdi> در چند <bdi dir="ltr">Context</bdi> پیاده شود.
- چند <bdi dir="ltr">Capability</bdi> در یک <bdi dir="ltr">Context</bdi> منسجم پیاده شوند.
- یک <bdi dir="ltr">Context</bdi> بخشی از یک <bdi dir="ltr">Capability</bdi> را برای چند کانال ارائه کند.

پس از <bdi dir="ltr">Capability Map</bdi> نمی‌توان مستقیم تعداد <bdi dir="ltr">Microservice</bdi>ها را شمرد.

## 10. مثال هدایت‌شده: «سامانهٔ تسهیلات»

عبارت <bdi dir="ltr">Legacy</bdi> را باز کن:


</div>

<div dir="ltr" align="left">

```text
سامانهٔ تسهیلات
├── طراحی محصول اعتباری
├── پذیرش و ارزیابی درخواست
├── تصویب و انعقاد قرارداد
├── اعطا و برنامهٔ بازپرداخت
├── محاسبهٔ مطالبات
├── وصول و پیگیری بدهی
└── تولید Fact مالی
```

</div>

<div dir="rtl" align="right">


این فهرست هنوز مرز نهایی نیست، اما نشان می‌دهد یک <bdi dir="ltr">Application</bdi> می‌تواند چند <bdi dir="ltr">Capability</bdi> و چند <bdi dir="ltr">Subdomain</bdi> را در خود فشرده کرده باشد. اسم <bdi dir="ltr">Application</bdi> نباید جای تحلیل را بگیرد.

برای <bdi dir="ltr">`اعطای تسهیلات`</bdi>:

- <bdi dir="ltr">Capability:</bdi> مدیریت تعهدات و پرداخت اعتباری
- <bdi dir="ltr">Outcome:</bdi> قرارداد مصوب به تعهد اجرایی و پرداخت قابل‌رهگیری تبدیل شود.
- <bdi dir="ltr">Owner</bdi> اولیه: کسب‌وکار اعتبارات/<bdi dir="ltr">Lending</bdi>
- <bdi dir="ltr">KPI</bdi> نمونه: زمان اعطا، نرخ خطای پرداخت، درصد اعطای تکراری صفر
- <bdi dir="ltr">Process</bdi> فعلی: ممکن است دستی، <bdi dir="ltr">Workflow</bdi> یا <bdi dir="ltr">Event-driven</bdi> باشد.
- <bdi dir="ltr">Systems</bdi> فعلی: ممکن است چند <bdi dir="ltr">Legacy</bdi> و <bdi dir="ltr">Core</bdi> را درگیر کند.

## 11. خطاهای رایج

### «هر چیزی که <bdi dir="ltr">Business</bdi> نام دارد <bdi dir="ltr">Capability</bdi> است»

خیر. <bdi dir="ltr">Product</bdi>، <bdi dir="ltr">Process</bdi>، <bdi dir="ltr">Rule</bdi> و <bdi dir="ltr">Business Service</bdi> هم <bdi dir="ltr">Business</bdi> هستند ولی نوعشان متفاوت است.

### «<bdi dir="ltr">Capability</bdi> را تیم مالک است، پس <bdi dir="ltr">Team</bdi> همان <bdi dir="ltr">Capability</bdi> است»

<bdi dir="ltr">Owner</bdi> و موضوع مالکیت یکی نیستند. ساختار تیم می‌تواند تغییر کند.

### «یک <bdi dir="ltr">Capability</bdi> یک <bdi dir="ltr">API</bdi> دارد»

یک <bdi dir="ltr">Capability</bdi> معمولاً با چند <bdi dir="ltr">Use Case</bdi> و <bdi dir="ltr">Contract</bdi> محقق می‌شود و یک <bdi dir="ltr">API</bdi> ممکن است بخشی از چند <bdi dir="ltr">Capability</bdi> را در یک <bdi dir="ltr">Facade</bdi> پنهان کند.

### «<bdi dir="ltr">Capability Map</bdi> همان <bdi dir="ltr">Application Portfolio</bdi> است»

<bdi dir="ltr">Application Portfolio</bdi> می‌گوید چه سیستم‌هایی داریم؛ <bdi dir="ltr">Capability Map</bdi> می‌گوید چه توانایی‌هایی لازم داریم. <bdi dir="ltr">Overlay</bdi> این دو برای کشف <bdi dir="ltr">Duplicate</bdi> و <bdi dir="ltr">Gap</bdi> مفید است، اما یکی نیستند.

## 12. تمرین هدایت‌شده

عبارت «کارمزد» را بررسی کن:

1. «محاسبهٔ کارمزد انتقال» احتمالاً <bdi dir="ltr">Rule/Use Case</bdi> است.
2. «سامانهٔ کارمزد» <bdi dir="ltr">Application</bdi> است.
3. «مدیریت قیمت‌گذاری و کارمزد» می‌تواند <bdi dir="ltr">Capability</bdi> باشد، اگر <bdi dir="ltr">Outcome</bdi> و <bdi dir="ltr">Owner</bdi> روشن داشته باشد.
4. <bdi dir="ltr">`FeeCalculated`</bdi> <bdi dir="ltr">Event</bdi> است.
5. «کارمزد پل» <bdi dir="ltr">Product pricing term</bdi> است.

همین واژه در پنج سطح ظاهر می‌شود. نام مشترک دلیل هم‌نوع‌بودن نیست.

## 13. تمرین مستقل و قبولی

[<bdi dir="ltr">Day 02 Exercise</bdi>](../exercises/day-02-capability-distinction.md) را انجام بده. برای ۱۵ مثال فقط برچسب نزن؛ <bdi dir="ltr">`Reason`</bdi> و در موارد مبهم <bdi dir="ltr">`Alternative interpretation`</bdi> را نیز ثبت کن.

| معیار | امتیاز |
|---|---:|
| تعریف <bdi dir="ltr">Capability</bdi> و استقلال از راه‌حل | ۲ |
| تمایز هشت نوع مفهوم | ۳ |
| تحلیل ابهام و <bdi dir="ltr">Context</bdi> دیدگاه | ۲ |
| <bdi dir="ltr">Outcome/Owner/KPI</bdi> برای سه <bdi dir="ltr">Capability</bdi> | ۲ |
| پرهیز از تبدیل مستقیم به <bdi dir="ltr">Service</bdi> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 14. آزمون خروج و منابع

درس را ببند و [<bdi dir="ltr">Exit Ticket</bdi>](../quizzes/day-02-exit-ticket.md) را پاسخ بده.

منابع هدفمند:

- [<bdi dir="ltr">TOGAF</bdi> — <bdi dir="ltr">Business Capabilities</bdi>](https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html)
- [<bdi dir="ltr">BIAN Service Landscape</bdi>](https://bian.org/deliverables/service-landscape/)

تعریف‌ها از منابع معماری استخراج شده‌اند؛ مثال‌ها و طبقه‌بندی‌های بانکی این درس مدل آموزشی و قابل‌نقد هستند.


</div>
