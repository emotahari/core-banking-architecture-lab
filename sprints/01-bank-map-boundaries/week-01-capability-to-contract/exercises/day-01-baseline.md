<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 01 Exercise</span> — <span dir="ltr">Architecture Baseline</span>

- <span dir="ltr">Timebox: 12 minutes</span>
- منابع: ممنوع
- هدف: سنجش مدل ذهنی فعلی، نه گرفتن نمره

## سناریو

یک تسهیلات مرابحه پس از تصویب و انعقاد قرارداد، اعطا می‌شود. مبلغ ۱۰۰٬۰۰۰٬۰۰۰ ریال باید به سپردهٔ جاری معرفی‌شده توسط مشتری واریز شود. عملیات باید قابل رهگیری باشد، دوبار واریز نشود و اثر مالی آن در حسابداری ثبت شود.

در این مرحله فرض کن:

- <span dir="ltr">Party/Customer</span>، <span dir="ltr">Product/Agreement</span>، <span dir="ltr">Lending</span>، <span dir="ltr">Deposits</span> و <span dir="ltr">Accounting</span> سامانه‌ها یا حوزه‌های قابل تشخیص سازمان‌اند.
- پاسخ یک سرویس ممکن است گم شود.
- درخواست تکراری ممکن است برسد.
- دربارهٔ <span dir="ltr">Kafka</span>، <span dir="ltr">Saga</span> یا نوع دیتابیس هنوز تصمیم نگرفته‌ایم.

## بدون مطالعه پاسخ بده

1. بانک برای انجام این سناریو به چه <span dir="ltr">Capability</span>هایی نیاز دارد؟ حداکثر ۸ مورد.
2. اجزای منطقی راه‌حل را نام ببر. هنوز لازم نیست <span dir="ltr">Microservice</span> باشند.
3. ترتیب تعامل اجزا را در ۵ تا ۱۰ گام بنویس.
4. مالک هر مورد را مشخص کن:
   - وضعیت اعطای تسهیلات
   - ماندهٔ اصل تسهیلات
   - ماندهٔ قابل برداشت سپرده
   - وضعیت واریز
   - <span dir="ltr">Journal Entry</span>
5. مرز یا مرزهای تراکنش را کجا می‌گذاری و چرا؟
6. کدام تعامل را <span dir="ltr">API/Command</span> و کدام اطلاع‌رسانی را <span dir="ltr">Event</span> می‌دانی؟
7. اگر واریز موفق شود ولی پاسخ گم شود، چه رفتاری انتظار داری؟
8. <span dir="ltr">Accounting</span> را چه کسی و در چه زمانی درگیر می‌کند؟
9. یک <span dir="ltr">Diagram</span> بسیار ساده بکش. <span dir="ltr">Mermaid</span> یا متن مرحله‌ای کافی است.
10. سه فرضی را که در پاسخ خودت پنهان کرده‌ای بنویس.

## قانون مهم

پس از خواندن درس، پاسخ خام را پاک نکن. بخش «بازنگری پس از درس» را در همان <span dir="ltr">Submission</span> اضافه کن تا تفاوت مدل ذهنی قابل مشاهده باشد.

</div>
