<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Banking Capability Map</bdi> — <bdi dir="ltr">Working Draft</bdi>

- <bdi dir="ltr">Version: 0.1</bdi>
- <bdi dir="ltr">Status: Working Draft</bdi>
- <bdi dir="ltr">Scope:</bdi> بانک جامع؛ سطح <bdi dir="ltr">L1</bdi>
- <bdi dir="ltr">Owner: Business Architecture</bdi>
- <bdi dir="ltr">Review date: Day 05</bdi>

این <bdi dir="ltr">Map</bdi> پاسخ نهایی نیست. در <bdi dir="ltr">Day 05</bdi> باید با مسئله‌های واقعی و سپس <bdi dir="ltr">BIAN 14 Gap Check</bdi> شود.


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


## آزمون کیفیت <bdi dir="ltr">L1</bdi>

برای هر <bdi dir="ltr">Capability</bdi> بررسی شود:

- آیا «چه کاری باید بتوانیم انجام دهیم» را می‌گوید، نه چگونه؟
- آیا نام واحد سازمانی، نرم‌افزار، <bdi dir="ltr">Vendor</bdi> یا فناوری در آن نیامده است؟
- آیا نسبتاً پایدارتر از <bdi dir="ltr">Process</bdi> و <bdi dir="ltr">System</bdi> است؟
- آیا <bdi dir="ltr">Owner</bdi> کسب‌وکاری قابل تعیین دارد؟
- آیا می‌توان <bdi dir="ltr">Outcome</bdi> و <bdi dir="ltr">KPI</bdi> برای آن تعریف کرد؟
- آیا با <bdi dir="ltr">Capability</bdi> دیگر هم‌پوشانی مبهم ندارد؟

## طبقه‌بندی چهارلایهٔ موقت

| لایه | نمونهٔ <bdi dir="ltr">Capability</bdi> | نکته |
|---|---|---|
| هستهٔ بانکداری | مشتری، محصول/قرارداد، سپرده، اعتبار، ثبت مالی پایه | مبنای وضعیت و تعهدات بانکی |
| عملیات و خدمات بانکداری | پرداخت، کارت، کانال، شعبه، <bdi dir="ltr">Teller</bdi>، چک، وصول | اجرای خدمت و اتصال هسته به شبکه‌ها و عملیات |
| سامانه‌های سازمانی | منابع انسانی، تدارکات، املاک، ناوگان، بودجهٔ سازمانی | ادارهٔ بنگاه، نه نگهداری تعهد بانکی مشتری |
| اکوسیستم دیجیتال | <bdi dir="ltr">Open Banking</bdi>، <bdi dir="ltr">Partner/Fintech</bdi>، <bdi dir="ltr">Marketplace</bdi> و <bdi dir="ltr">Embedded Finance</bdi> | گسترش خدمت خارج از مرز سنتی بانک |

این چهار لایه برای <bdi dir="ltr">Portfolio</bdi> و <bdi dir="ltr">Operating Model</bdi> مفیدند، اما <bdi dir="ltr">Bounded Context</bdi> یا <bdi dir="ltr">Deployment Boundary</bdi> نیستند.

</div>
