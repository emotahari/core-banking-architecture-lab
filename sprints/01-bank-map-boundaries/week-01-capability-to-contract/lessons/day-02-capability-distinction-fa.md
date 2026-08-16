<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 02</span> — <span dir="ltr">Capability</span> در برابر <span dir="ltr">Process</span>، <span dir="ltr">Business Service</span> و <span dir="ltr">System</span>

- <span dir="ltr">Day budget: 45 minutes</span> — <span dir="ltr">22 lesson</span> + <span dir="ltr">18 exercise</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output: Distinction Matrix</span> برای ۱۵ مثال بانکی
- <span dir="ltr">Banking case:</span> افتتاح سپرده، اعطای تسهیلات، انتقال وجه و مسدودی قضایی

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Business Capability</span> را بدون استفاده از نام سامانه یا فناوری تعریف کنی.
2. <span dir="ltr">Capability</span> را از <span dir="ltr">Process</span>، <span dir="ltr">Value Stream</span>، <span dir="ltr">Business Service</span>، <span dir="ltr">Product</span>، <span dir="ltr">System</span>، <span dir="ltr">Organization Unit</span> و <span dir="ltr">API</span> جدا کنی.
3. یک عبارت مبهم بانکی را با آزمون‌های مشخص طبقه‌بندی کنی.
4. برای هر <span dir="ltr">Capability</span>، <span dir="ltr">Outcome</span>، <span dir="ltr">Owner</span> و <span dir="ltr">KPI</span> اولیه پیشنهاد بدهی.
5. تشخیص بدهی چه زمانی یک نام ظاهراً دامینی هنوز فقط نام <span dir="ltr">Legacy Application</span> است.

## 2. مسئلهٔ واقعی

در نقشه‌های سازمانی معمولاً فهرستی مانند زیر می‌بینیم:

- سامانهٔ تسهیلات
- ادارهٔ چک
- سرویس افتتاح حساب
- <span dir="ltr">API</span> استعلام مانده
- فرایند انتقال وجه
- محصول سپردهٔ کوتاه‌مدت

اگر همهٔ این موارد را در یک سطح از <span dir="ltr">Diagram</span> بگذاریم، <span dir="ltr">Map</span> از همان ابتدا چند نوع چیز متفاوت را مخلوط کرده است. نتیجه این می‌شود که تیم‌ها از روی نام‌های موجود <span dir="ltr">Service</span> می‌سازند، مالکیت تصمیم مبهم می‌ماند و تغییر یک <span dir="ltr">Capability</span> به چند سامانهٔ بدون مرز پخش می‌شود.

## 3. تعریف عملیاتی <span dir="ltr">Business Capability</span>

<span dir="ltr">Business Capability</span> بیان می‌کند **سازمان چه توانایی نسبتاً پایداری باید داشته باشد تا <span dir="ltr">Outcome</span> کسب‌وکاری تولید کند**؛ مستقل از اینکه امروز این توانایی با کدام فرایند، تیم، نرم‌افزار، <span dir="ltr">Vendor</span> یا فناوری اجرا می‌شود.

نمونه‌های مناسب:

- مدیریت رابطه با مشتری
- نگهداری وجوه مشتری
- مدیریت تعهدات اعتباری
- اجرای پرداخت و انتقال وجه
- اعمال محدودیت و مسدودی روی وجوه
- ثبت و گزارش آثار مالی

نمونه‌های نامناسب:

- <span dir="ltr">`LoanSystem`</span>؛ نام راه‌حل یا <span dir="ltr">Application</span> است.
- «بررسی درخواست در سه مرحله»؛ <span dir="ltr">Process</span> است.
- <span dir="ltr">`POST /loans`</span>؛ <span dir="ltr">Contract</span> فنی است.
- «ادارهٔ اعتبارات»؛ واحد سازمانی است.
- «وام مرابحهٔ فرهنگیان»؛ <span dir="ltr">Product/Offering</span> است.

<span dir="ltr">Capability</span> پاسخ <span dir="ltr">`what`</span> سازمانی است، نه <span dir="ltr">`how`</span> اجرایی.

## 4. هفت مفهوم مجاور

### <span dir="ltr">4.1 Process</span>

<span dir="ltr">Process</span> توالی فعالیت‌ها، تصمیم‌ها و <span dir="ltr">Hand-off</span>ها برای رسیدن به نتیجه است. <span dir="ltr">Process</span> تغییرپذیرتر از <span dir="ltr">Capability</span> است.


</div>

<div dir="ltr" align="left">

```text
Capability: مدیریت سپرده
Process: دریافت درخواست → احراز هویت → کنترل محصول → افتتاح → ابلاغ نتیجه
```

</div>

<div dir="rtl" align="right">


با حذف امضای کاغذی و افزودن <span dir="ltr">Video KYC</span>، <span dir="ltr">Process</span> تغییر می‌کند؛ <span dir="ltr">Capability</span> افتتاح و نگهداری رابطهٔ سپرده باقی می‌ماند.

### <span dir="ltr">4.2 Value Stream</span>

<span dir="ltr">Value Stream</span> جریان ایجاد ارزش برای ذی‌نفع از <span dir="ltr">Trigger</span> تا <span dir="ltr">Outcome</span> است و می‌تواند چند <span dir="ltr">Capability</span> و چند <span dir="ltr">Process</span> را درگیر کند. «از درخواست تسهیلات تا دریافت وجه» یک <span dir="ltr">Value Stream</span> است، نه یک <span dir="ltr">Capability</span> منفرد.

### <span dir="ltr">4.3 Business Service</span>

<span dir="ltr">Business Service</span> نمای قابل‌مصرف یک یا چند <span dir="ltr">Capability</span> برای مشتری یا شریک است. «خدمت انتقال آنی وجه» چیزی است که مصرف‌کننده دریافت می‌کند؛ پشت آن <span dir="ltr">Capability</span>های ثبت دستور پرداخت، کنترل ریسک، جابه‌جایی وجه، تسویه و رسیدگی به مغایرت قرار دارند.

<span dir="ltr">Business Service</span> با <span dir="ltr">`REST service`</span> یا <span dir="ltr">Microservice</span> یکی نیست.

### <span dir="ltr">4.4 Product/Offering</span>

<span dir="ltr">Product</span> بسته‌ای از ویژگی، قیمت، شرایط و تعهد قابل‌عرضه به بازار است. «سپردهٔ بلندمدت یک‌ساله» محصول است. <span dir="ltr">Capability</span> «طراحی و مدیریت محصول» یا «نگهداری سپرده» است.

### <span dir="ltr">4.5 Organization Unit/Team</span>

واحد سازمانی پاسخ می‌دهد چه کسانی مسئول کارند. <span dir="ltr">Capability</span> پاسخ می‌دهد سازمان چه توانایی‌ای لازم دارد. یک تیم ممکن است چند <span dir="ltr">Capability</span> را پوشش دهد و یک <span dir="ltr">Capability</span> ممکن است میان چند واحد پراکنده باشد؛ این پراکندگی خود یک <span dir="ltr">Risk</span> برای <span dir="ltr">Ownership</span> است.

### <span dir="ltr">4.6 Application/System</span>

<span dir="ltr">System</span> پیاده‌سازی فعلی بخشی از توانمندی‌هاست. «سامانه سپرده» ممکن است افتتاح، مانده، سود، <span dir="ltr">Hold</span> و گزارش را یکجا انجام دهد. این واقعیت <span dir="ltr">Legacy</span> نه اثبات می‌کند همهٔ آن‌ها یک <span dir="ltr">Capability</span> هستند و نه اثبات می‌کند باید یک <span dir="ltr">Bounded Context</span> بمانند.

### <span dir="ltr">4.7 API/Event</span>

<span dir="ltr">API</span> و <span dir="ltr">Event</span> قرارداد تعامل‌اند. <span dir="ltr">`GET /accounts/{id}/balance`</span> یک <span dir="ltr">Query Contract</span> است؛ <span dir="ltr">`FundsHeld`</span> یک <span dir="ltr">Fact</span> منتشرشده است. هیچ‌کدام به‌تنهایی <span dir="ltr">Capability</span> نیستند.

## 5. جدول تشخیص سریع

| نوع | پرسش تشخیصی | نسبت پایداری | مثال بانکی |
|---|---|---|---|
| <span dir="ltr">Capability</span> | بانک باید چه کاری بتواند انجام دهد؟ | زیاد | مدیریت تعهدات اعتباری |
| <span dir="ltr">Value Stream</span> | ارزش از چه <span dir="ltr">Trigger</span> تا چه <span dir="ltr">Outcome</span> ایجاد می‌شود؟ | متوسط | از درخواست وام تا دریافت وجه |
| <span dir="ltr">Process</span> | کار با چه توالی انجام می‌شود؟ | متوسط/کم | فرایند افتتاح سپرده |
| <span dir="ltr">Business Service</span> | چه خدمتی به مصرف‌کننده عرضه می‌شود؟ | متوسط | انتقال آنی وجه |
| <span dir="ltr">Product</span> | چه بستهٔ شرایطی عرضه می‌شود؟ | متوسط | سپردهٔ یک‌ساله |
| <span dir="ltr">Org Unit</span> | چه گروهی پاسخ‌گوست؟ | کم/متوسط | ادارهٔ اعتبارات |
| <span dir="ltr">System</span> | اکنون با چه راه‌حلی اجرا می‌شود؟ | کم | سامانهٔ تسهیلات |
| <span dir="ltr">API/Event</span> | تعامل با چه <span dir="ltr">Contract</span>ی انجام می‌شود؟ | کم | <span dir="ltr">`LoanDisbursed`</span> |

## 6. آزمون شش‌گانهٔ <span dir="ltr">Capability</span>

برای هر نام پیشنهادی شش سؤال بپرس:

1. آیا <span dir="ltr">Outcome</span> کسب‌وکاری قابل تعریف دارد؟
2. آیا بدون اشاره به فناوری یا نرم‌افزار قابل بیان است؟
3. آیا با تغییر <span dir="ltr">Process</span> هنوز باقی می‌ماند؟
4. آیا <span dir="ltr">Business Owner</span> قابل تعیین دارد؟
5. آیا <span dir="ltr">KPI</span> یا سطح بلوغ برای آن قابل سنجش است؟
6. آیا نام آن «توانایی» را می‌رساند، نه یک شیء، کانال یا واحد؟

اگر پاسخ چند سؤال منفی است، مورد احتمالاً <span dir="ltr">Capability</span> نیست یا نام‌گذاری آن ضعیف است.

## 7. پانزده مثال طبقه‌بندی‌شده

| عبارت | نوع غالب | دلیل کوتاه |
|---|---|---|
| مدیریت هویت و رابطهٔ مشتری | <span dir="ltr">Capability</span> | توانایی پایدار و <span dir="ltr">Outcome</span> محور |
| افتتاح حساب غیرحضوری | <span dir="ltr">Business Service/Process</span> | خدمت قابل‌عرضه با جریان اجرایی مشخص |
| سپردهٔ قرض‌الحسنه جاری | <span dir="ltr">Product</span> | بستهٔ شرایط و تعهد |
| سامانهٔ سپرده | <span dir="ltr">System</span> | راه‌حل نرم‌افزاری موجود |
| محاسبهٔ سود روزشمار | <span dir="ltr">Domain Rule/Process step</span> | قاعده یا فعالیت در <span dir="ltr">Capability</span> بزرگ‌تر |
| نگهداری وجوه مشتری | <span dir="ltr">Capability</span> | توانایی بنیادی بانک |
| ادارهٔ شعب | <span dir="ltr">Organization Unit</span> | ساختار پاسخ‌گویی |
| خدمت مسدودی قضایی | <span dir="ltr">Business Service</span> | نمای خدمت برای مرجع/عملیات |
| اعمال <span dir="ltr">Hold</span> روی ماندهٔ قابل برداشت | <span dir="ltr">Use Case</span> | قصد مشخص در یک <span dir="ltr">Context</span> |
| <span dir="ltr">`POST /holds`</span> | <span dir="ltr">API Operation</span> | <span dir="ltr">Contract</span> فنی |
| <span dir="ltr">`FundsHeld`</span> | <span dir="ltr">Event</span> | <span dir="ltr">Fact</span> رخ‌داده |
| از درخواست وام تا واریز | <span dir="ltr">Value Stream</span> | جریان <span dir="ltr">End-to-end</span> ارزش |
| ارزیابی اهلیت اعتباری | <span dir="ltr">Capability</span> | توانایی تصمیم‌گیری اعتباری |
| کمیتهٔ اعتباری | <span dir="ltr">Organization/Decision mechanism</span> | سازوکار تصمیم فعلی |
| <span dir="ltr">Core Banking</span> | <span dir="ltr">Portfolio/System landscape label</span> | برچسب سبد؛ نه <span dir="ltr">Capability</span> منفرد |

طبقه‌بندی همیشه فقط یک برچسب ندارد. «افتتاح حساب غیرحضوری» از دید مشتری <span dir="ltr">Business Service</span> و از دید عملیات یک <span dir="ltr">Process</span> است. نکته این است که سطح مورد استفاده در <span dir="ltr">Diagram</span> صریح باشد.

## 8. نام‌گذاری <span dir="ltr">Capability</span>

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

- پسوند <span dir="ltr">`System`</span>، <span dir="ltr">`Platform`</span>، <span dir="ltr">`Portal`</span> یا نام <span dir="ltr">Vendor</span>
- نام جدول یا <span dir="ltr">Entity</span> فنی
- نام کانال مانند <span dir="ltr">Mobile/Branch</span> در <span dir="ltr">L1</span>
- عبارت بسیار ریز و عملیاتی مانند «چاپ رسید»
- عبارت بسیار کلان مانند «بانکداری»
- ترکیب چند توانایی با «و» بدون <span dir="ltr">Outcome</span> مشترک

## <span dir="ltr">9. Capability</span> با <span dir="ltr">Bounded Context</span> یکی نیست

<span dir="ltr">Capability</span> از منظر <span dir="ltr">Business Architecture</span> توانایی سازمان را بیان می‌کند. <span dir="ltr">Bounded Context</span> از منظر مدل‌سازی، مرز اعتبار یک مدل و زبان را تعیین می‌کند. نگاشت آن‌ها ممکن است:

- یک <span dir="ltr">Capability</span> در چند <span dir="ltr">Context</span> پیاده شود.
- چند <span dir="ltr">Capability</span> در یک <span dir="ltr">Context</span> منسجم پیاده شوند.
- یک <span dir="ltr">Context</span> بخشی از یک <span dir="ltr">Capability</span> را برای چند کانال ارائه کند.

پس از <span dir="ltr">Capability Map</span> نمی‌توان مستقیم تعداد <span dir="ltr">Microservice</span>ها را شمرد.

## 10. مثال هدایت‌شده: «سامانهٔ تسهیلات»

عبارت <span dir="ltr">Legacy</span> را باز کن:


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


این فهرست هنوز مرز نهایی نیست، اما نشان می‌دهد یک <span dir="ltr">Application</span> می‌تواند چند <span dir="ltr">Capability</span> و چند <span dir="ltr">Subdomain</span> را در خود فشرده کرده باشد. اسم <span dir="ltr">Application</span> نباید جای تحلیل را بگیرد.

برای <span dir="ltr">`اعطای تسهیلات`</span>:

- <span dir="ltr">Capability:</span> مدیریت تعهدات و پرداخت اعتباری
- <span dir="ltr">Outcome:</span> قرارداد مصوب به تعهد اجرایی و پرداخت قابل‌رهگیری تبدیل شود.
- <span dir="ltr">Owner</span> اولیه: کسب‌وکار اعتبارات/<span dir="ltr">Lending</span>
- <span dir="ltr">KPI</span> نمونه: زمان اعطا، نرخ خطای پرداخت، درصد اعطای تکراری صفر
- <span dir="ltr">Process</span> فعلی: ممکن است دستی، <span dir="ltr">Workflow</span> یا <span dir="ltr">Event-driven</span> باشد.
- <span dir="ltr">Systems</span> فعلی: ممکن است چند <span dir="ltr">Legacy</span> و <span dir="ltr">Core</span> را درگیر کند.

## 11. خطاهای رایج

### «هر چیزی که <span dir="ltr">Business</span> نام دارد <span dir="ltr">Capability</span> است»

خیر. <span dir="ltr">Product</span>، <span dir="ltr">Process</span>، <span dir="ltr">Rule</span> و <span dir="ltr">Business Service</span> هم <span dir="ltr">Business</span> هستند ولی نوعشان متفاوت است.

### «<span dir="ltr">Capability</span> را تیم مالک است، پس <span dir="ltr">Team</span> همان <span dir="ltr">Capability</span> است»

<span dir="ltr">Owner</span> و موضوع مالکیت یکی نیستند. ساختار تیم می‌تواند تغییر کند.

### «یک <span dir="ltr">Capability</span> یک <span dir="ltr">API</span> دارد»

یک <span dir="ltr">Capability</span> معمولاً با چند <span dir="ltr">Use Case</span> و <span dir="ltr">Contract</span> محقق می‌شود و یک <span dir="ltr">API</span> ممکن است بخشی از چند <span dir="ltr">Capability</span> را در یک <span dir="ltr">Facade</span> پنهان کند.

### «<span dir="ltr">Capability Map</span> همان <span dir="ltr">Application Portfolio</span> است»

<span dir="ltr">Application Portfolio</span> می‌گوید چه سیستم‌هایی داریم؛ <span dir="ltr">Capability Map</span> می‌گوید چه توانایی‌هایی لازم داریم. <span dir="ltr">Overlay</span> این دو برای کشف <span dir="ltr">Duplicate</span> و <span dir="ltr">Gap</span> مفید است، اما یکی نیستند.

## 12. تمرین هدایت‌شده

عبارت «کارمزد» را بررسی کن:

1. «محاسبهٔ کارمزد انتقال» احتمالاً <span dir="ltr">Rule/Use Case</span> است.
2. «سامانهٔ کارمزد» <span dir="ltr">Application</span> است.
3. «مدیریت قیمت‌گذاری و کارمزد» می‌تواند <span dir="ltr">Capability</span> باشد، اگر <span dir="ltr">Outcome</span> و <span dir="ltr">Owner</span> روشن داشته باشد.
4. <span dir="ltr">`FeeCalculated`</span> <span dir="ltr">Event</span> است.
5. «کارمزد پل» <span dir="ltr">Product pricing term</span> است.

همین واژه در پنج سطح ظاهر می‌شود. نام مشترک دلیل هم‌نوع‌بودن نیست.

## 13. تمرین مستقل و قبولی

[<span dir="ltr">Day 02 Exercise</span>](../exercises/day-02-capability-distinction.md) را انجام بده. برای ۱۵ مثال فقط برچسب نزن؛ <span dir="ltr">`Reason`</span> و در موارد مبهم <span dir="ltr">`Alternative interpretation`</span> را نیز ثبت کن.

| معیار | امتیاز |
|---|---:|
| تعریف <span dir="ltr">Capability</span> و استقلال از راه‌حل | ۲ |
| تمایز هشت نوع مفهوم | ۳ |
| تحلیل ابهام و <span dir="ltr">Context</span> دیدگاه | ۲ |
| <span dir="ltr">Outcome/Owner/KPI</span> برای سه <span dir="ltr">Capability</span> | ۲ |
| پرهیز از تبدیل مستقیم به <span dir="ltr">Service</span> | ۱ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰.

## 14. آزمون خروج و منابع

درس را ببند و [<span dir="ltr">Exit Ticket</span>](../quizzes/day-02-exit-ticket.md) را پاسخ بده.

منابع هدفمند:

- [<span dir="ltr">TOGAF</span> — <span dir="ltr">Business Capabilities</span>](https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html)
- [<span dir="ltr">BIAN Service Landscape</span>](https://bian.org/deliverables/service-landscape/)

تعریف‌ها از منابع معماری استخراج شده‌اند؛ مثال‌ها و طبقه‌بندی‌های بانکی این درس مدل آموزشی و قابل‌نقد هستند.


</div>
