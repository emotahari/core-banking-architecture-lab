# Banking Capability Map — Working Draft

- Version: 0.1
- Status: Working Draft
- Scope: بانک جامع؛ سطح L1
- Owner: Business Architecture
- Review date: Day 05

این Map پاسخ نهایی نیست. در Day 05 باید با مسئله‌های واقعی و سپس BIAN 14 Gap Check شود.

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

## آزمون کیفیت L1

برای هر Capability بررسی شود:

- آیا «چه کاری باید بتوانیم انجام دهیم» را می‌گوید، نه چگونه؟
- آیا نام واحد سازمانی، نرم‌افزار، Vendor یا فناوری در آن نیامده است؟
- آیا نسبتاً پایدارتر از Process و System است؟
- آیا Owner کسب‌وکاری قابل تعیین دارد؟
- آیا می‌توان Outcome و KPI برای آن تعریف کرد؟
- آیا با Capability دیگر هم‌پوشانی مبهم ندارد؟

## طبقه‌بندی چهارلایهٔ موقت

| لایه | نمونهٔ Capability | نکته |
|---|---|---|
| هستهٔ بانکداری | مشتری، محصول/قرارداد، سپرده، اعتبار، ثبت مالی پایه | مبنای وضعیت و تعهدات بانکی |
| عملیات و خدمات بانکداری | پرداخت، کارت، کانال، شعبه، Teller، چک، وصول | اجرای خدمت و اتصال هسته به شبکه‌ها و عملیات |
| سامانه‌های سازمانی | منابع انسانی، تدارکات، املاک، ناوگان، بودجهٔ سازمانی | ادارهٔ بنگاه، نه نگهداری تعهد بانکی مشتری |
| اکوسیستم دیجیتال | Open Banking، Partner/Fintech، Marketplace و Embedded Finance | گسترش خدمت خارج از مرز سنتی بانک |

این چهار لایه برای Portfolio و Operating Model مفیدند، اما Bounded Context یا Deployment Boundary نیستند.
