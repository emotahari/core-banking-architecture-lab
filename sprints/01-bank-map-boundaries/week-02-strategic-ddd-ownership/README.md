# Week 02 — Strategic DDD و مالکیت

- Status: Ready
- Time budget: 360 minutes
- Main question: هر مدل، داده و تصمیم در کدام Bounded Context معنا و مالک دارد؟

![برنامهٔ دقیق هفتهٔ دوم](week-02-plan.svg)

## ترتیب دقیق روزها

| روز | زمان | موضوع | فعالیت دقیق | شاهد پایان |
|---|---:|---|---|---|
| ۱ | ۵۰ دقیقه | Domain/Subdomain | طبقه‌بندی Core، Supporting و Generic با مثال‌های بانکی | Subdomain Matrix |
| ۲ | ۴۵ دقیقه | Bounded Context و Ubiquitous Language | کشف تفاوت معنای Account، Customer و Product در Contextها | Language Conflicts |
| ۳ | ۵۰ دقیقه | Context Map Patterns | Customer/Supplier، Conformist، ACL و Published Language | Context Relations |
| ۴ | ۵۰ دقیقه | Data/Decision Ownership | تکمیل ماتریس شش دامین و تعیین Source of Truth | Ownership Matrix v1 |
| ۵ | ۱۰۰ دقیقه | Spring Modulith | ایجاد شش ماژول، API/Internal Package و Dependency مجاز | Module Skeleton |
| ۶ | ۴۵ دقیقه | Fitness Test | کشف Cycle و دسترسی غیرمجاز با Module Verification | Architecture Test |
| ۷ | ۲۰ دقیقه | Gate Sprint 01 | دفاع قابلیت مسدودی قضایی از Capability تا Event | Gate Evidence |
| **جمع** | **۳۶۰ دقیقه** |  |  |  |

## خروجی‌ها

- Domain Map v1
- Context Map v1
- Data/Decision Ownership Matrix v1
- شش Domain Dossier اولیه
- شش ماژول منطقی Spring Modulith
- Architecture Fitness Test

## Gate

روی قابلیت «مسدودی قضایی سپرده» باید روشن شود:

1. Capability متعلق به چه دامنه‌ای است؟
2. کدام Context دستور را می‌پذیرد؟
3. چه Contextی مجاز به تغییر Hold است؟
4. مرجع حکم قضایی کجاست و آیا Deposits مالک آن است؟
5. API/Command ورودی چیست؟
6. چه Domain/Integration Eventی پس از موفقیت منتشر می‌شود؟
7. Accounting چه چیزی را ثبت می‌کند و چه چیزی را نباید مالک شود؟

پاسخ مبتنی بر نام جدول، Controller یا ساختار سازمانی Gate را پاس نمی‌کند.
