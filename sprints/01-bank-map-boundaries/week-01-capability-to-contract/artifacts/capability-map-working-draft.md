<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Banking Capability Map</span> — <span dir="ltr">Working Draft</span>

- <span dir="ltr">Version: 0.1</span>
- <span dir="ltr">Status: Working Draft</span>
- <span dir="ltr">Scope:</span> بانک جامع؛ سطح <span dir="ltr">L1</span>
- <span dir="ltr">Owner: Business Architecture</span>
- <span dir="ltr">Review date: Day 05</span>

این <span dir="ltr">Map</span> پاسخ نهایی نیست. در <span dir="ltr">Day 05</span> باید با مسئله‌های واقعی و سپس <span dir="ltr">BIAN 14 Gap Check</span> شود.


</div>

<div dir="ltr" align="left">

~~~mermaid
flowchart TB
    BANK["توانمندی‌های بانک"]
    BANK --> CORE["هستهٔ بانکداری"]
    BANK --> NEAR["عملیات و خدمات بانکداری"]
    BANK --> ENTERPRISE["توانمندی‌های سازمانی"]
    BANK --> ECO["اکوسیستم دیجیتال"]

    CORE --> CUST["مشتری، طرف تجاری و رابطه"]
    CORE --> PROD["محصول، قیمت‌گذاری و قرارداد"]
    CORE --> FUNDS["جذب و نگهداری منابع"]
    CORE --> CREDIT["اعتبار و تأمین مالی"]
    CORE --> FIN["کنترل مالی و حسابداری"]

    NEAR --> MOVE["انتقال، پرداخت و تسویه"]
    NEAR --> MARKET["خزانه‌داری، بازار و اوراق"]
    NEAR --> SERVE["خدمت‌رسانی، شعبه و وجه نقد"]
    NEAR --> COLLECT["وصول و بازیافت مطالبات"]
    NEAR --> CONTROL["ریسک، انطباق و نظارت"]

    ENTERPRISE --> GOV["راهبری و مدیریت بانک"]
    ENTERPRISE --> DATA["داده، گزارش‌گری و تصمیم‌یار"]
    ENTERPRISE --> SUPPORT["منابع و پشتیبانی سازمانی"]
    ENTERPRISE --> SECURITY["امنیت و مدیریت دسترسی"]

    ECO --> OPEN["بانکداری باز و API Partnership"]
    ECO --> PARTNER["مدیریت شریک و Fintech"]
    ECO --> EMBED["Marketplace و Embedded Finance"]
~~~

</div>

<div dir="rtl" align="right">


## آزمون کیفیت <span dir="ltr">L1</span>

برای هر <span dir="ltr">Capability</span> بررسی شود:

- آیا «چه کاری باید بتوانیم انجام دهیم» را می‌گوید، نه چگونه؟
- آیا نام واحد سازمانی، نرم‌افزار، <span dir="ltr">Vendor</span> یا فناوری در آن نیامده است؟
- آیا نسبتاً پایدارتر از <span dir="ltr">Process</span> و <span dir="ltr">System</span> است؟
- آیا <span dir="ltr">Owner</span> کسب‌وکاری قابل تعیین دارد؟
- آیا می‌توان <span dir="ltr">Outcome</span> و <span dir="ltr">KPI</span> برای آن تعریف کرد؟
- آیا با <span dir="ltr">Capability</span> دیگر هم‌پوشانی مبهم ندارد؟

## طبقه‌بندی چهارلایهٔ موقت

| لایه | نمونهٔ <span dir="ltr">Capability</span> | نکته |
|---|---|---|
| هستهٔ بانکداری | مشتری، محصول/قرارداد، سپرده، اعتبار، ثبت مالی پایه | مبنای وضعیت و تعهدات بانکی |
| عملیات و خدمات بانکداری | پرداخت، کارت، کانال، شعبه، <span dir="ltr">Teller</span>، چک، وصول | اجرای خدمت و اتصال هسته به شبکه‌ها و عملیات |
| سامانه‌های سازمانی | منابع انسانی، تدارکات، املاک، ناوگان، بودجهٔ سازمانی | ادارهٔ بنگاه، نه نگهداری تعهد بانکی مشتری |
| اکوسیستم دیجیتال | <span dir="ltr">Open Banking</span>، <span dir="ltr">Partner/Fintech</span>، <span dir="ltr">Marketplace</span> و <span dir="ltr">Embedded Finance</span> | گسترش خدمت خارج از مرز سنتی بانک |

این چهار لایه برای <span dir="ltr">Portfolio</span> و <span dir="ltr">Operating Model</span> مفیدند، اما <span dir="ltr">Bounded Context</span> یا <span dir="ltr">Deployment Boundary</span> نیستند.

</div>
