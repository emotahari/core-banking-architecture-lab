# Week 01 — Capability تا API/Event

- Status: **Day 01 — Doing**
- Time budget: 360 minutes
- Banking lens: اعطای تسهیلات، انتقال وجه و شکست سپرده
- Main question: چگونه از «بانک باید چه کاری بتواند انجام دهد؟» به Contract قابل اجرا می‌رسیم؟

![برنامهٔ دقیق هفتهٔ اول](week-01-plan.svg)

## ترتیب دقیق روزها

| روز | زمان | موضوع | فعالیت دقیق | شاهد پایان |
|---|---:|---|---|---|
| ۱ | ۶۰ دقیقه | زبان معماری و خط پایه | ۱۲ دقیقه پاسخ خام، ۲۵ دقیقه درس، ۱۵ دقیقه تحلیل زنجیره، ۸ دقیقه Exit Ticket | پاسخ خط پایه + Quiz |
| ۲ | ۴۵ دقیقه | Capability در برابر Process/Service/System | ساخت جدول تمایز و طبقه‌بندی ۱۵ مثال بانکی | Distinction Matrix |
| ۳ | ۵۰ دقیقه | System تا Contract | ترسیم زنجیره برای «مسدودی قضایی سپرده» و «اعطای تسهیلات» | دو Traceability Chain |
| ۴ | ۵۵ دقیقه | Coupling، Cohesion، Encapsulation و Information Hiding | نقد یک طراحی کاپل‌شده و بازطراحی Boundary | Coupling Review |
| ۵ | ۷۰ دقیقه | Banking Capability Map و BIAN 14 | ساخت L1 Map، طبقه‌بندی چهارلایه و Gap Check با BIAN | Capability Map v1 |
| ۶ | ۶۰ دقیقه | Value Object و Pipeline | Money و سه Typed ID، Unit Test و mvn verify | کد و تست سبز |
| ۷ | ۲۰ دقیقه | تثبیت و دفاع | تکمیل واژه‌نامه، گزارش و دفاع ده‌دقیقه‌ای | Week Report |
| **جمع** | **۳۶۰ دقیقه** |  |  |  |

## امروز؛ Day 01

ترتیب را عوض نکن:

1. **پیش از خواندن درس**، [تمرین خط پایه](exercises/day-01-baseline.md) را باز کن و پاسخ را در [فایل Submission](submissions/day-01-baseline-response.md) بنویس.
2. [درس روز اول](lessons/day-01-architecture-language-fa.md) را بخوان.
3. بخش «زنجیرهٔ Capability تا Contract» را روی پاسخ اولیهٔ خودت اعمال کن؛ پاسخ قبلی را پاک نکن، اصلاح را زیر آن بنویس.
4. [Exit Ticket](quizzes/day-01-exit-ticket.md) را بدون مراجعه به متن پاسخ بده.
5. فایل Submission را برای Review بفرست.

## خروجی‌های پایان Week 01

- [Capability Map working draft](artifacts/capability-map-working-draft.md) که در Day 05 به v1 تبدیل می‌شود
- [Glossary](artifacts/glossary.md) با حداقل ۴۰ واژه
- پاسخ خط پایهٔ سه سناریوی نهایی
- Money، AccountId، CustomerId و BranchId با تست
- Pipeline اولیهٔ mvn verify
- گزارش هفته

## Definition of Done

- تفاوت Capability، Process، Business Service، System و API با مثال بانکی توضیح داده شود.
- زنجیرهٔ Capability تا API/Event برای دو سناریو قابل ردیابی باشد.
- هیچ Service Candidate بدون Capability و مالک تصمیم معرفی نشده باشد.
- نقش BIAN به‌عنوان Reference Model، نه Deployment Blueprint، دفاع شود.
- Value Objectها Equality و ورودی نامعتبر را آزمون کنند و Rounding پنهان نداشته باشند.
- mvn verify سبز باشد.

## منابع

ترتیب و دلیل مطالعه در [References](references/README.md) ثبت شده است. فقط بخش‌های مشخص‌شده خوانده می‌شوند؛ گشتن بی‌هدف در صدها Service Domain جزو تمرین نیست.
