<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 01 Exit Ticket</span>

- <span dir="ltr">Timebox: 8 minutes</span>
- بدون مراجعه به درس
- پاسخ‌ها در انتهای <span dir="ltr">Submission</span> روز اول افزوده شوند.

## پرسش‌ها

1. در یک جمله بگو <span dir="ltr">Business Capability</span> چیست و چه چیزی نیست.
2. چرا «سامانه تسهیلات» نام مناسبی برای <span dir="ltr">Capability</span> نیست؟
3. آیا یک <span dir="ltr">BIAN Service Domain</span> الزاماً یک <span dir="ltr">Microservice</span> قابل استقرار است؟ دلیل را بگو.
4. تفاوت <span dir="ltr">Domain</span> و <span dir="ltr">Bounded Context</span> را با یک مثال بانکی توضیح بده.
5. تفاوت <span dir="ltr">Module</span> و <span dir="ltr">Deployable Service</span> چیست؟
6. زنجیرهٔ زیر چه اشکالی دارد؟

   «جدول <span dir="ltr">LOAN</span> وجود دارد، پس <span dir="ltr">LoanService</span> می‌سازیم، سپس برایش <span dir="ltr">API</span> تعریف می‌کنیم.»

7. در قابلیت مسدودی قضایی سپرده، مالک متن/اعتبار حکم و مالک <span dir="ltr">Hold</span> عملیاتی سپرده لزوماً یکی‌اند؟ چرا؟
8. سه سؤال بنویس که قبل از معرفی هر <span dir="ltr">Service Candidate</span> باید پاسخ داده شوند.

## <span dir="ltr">Rubric</span>

| حوزه | امتیاز |
|---|---:|
| تمایز <span dir="ltr">Capability</span> از <span dir="ltr">Process/System</span> | ۲ |
| تمایز <span dir="ltr">Domain/Context/Module/Service</span> | ۳ |
| فهم نقش <span dir="ltr">BIAN</span> | ۱ |
| تشخیص <span dir="ltr">Ownership</span> و <span dir="ltr">Traceability</span> | ۲ |
| **جمع** | **۸** |

حد عبور روز اول ۶ از ۸ است. امتیاز کمتر به معنی شکست نیست؛ بخش مربوط با یک مثال کوچک‌تر دوباره تمرین می‌شود.


1. در یک جمله بگو <span dir="ltr">Business Capability</span> چیست و چه چیزی نیست.توانمدی انجام یک نیاز است
2. چرا «سامانه تسهیلات» نام مناسبی برای <span dir="ltr">Capability</span> نیست؟ این نام مربوط به یک سامانه است، توتنمندی میتواند امکان مدیریت تسهیلات اعطایی باشد.
3. آیا یک <span dir="ltr">BIAN Service Domain</span> الزاماً یک <span dir="ltr">Microservice</span> قابل استقرار است؟ دلیل را بگو. خیر یک پارتیشن منطقی و استاندارد حوزه بانکی هست در صورتی ماکرو سرویس به سوالات دیگری مثل تراکنش و استقرار و غره نیز پاسخگو ست
4. تفاوت <span dir="ltr">Domain</span> و <span dir="ltr">Bounded Context</span> را با یک مثال بانکی توضیح بده. سپرده و حسابداری هر کدام یک دامین هستند اما معنای قرارداد در هر کدام میتواند یک <span dir="ltr">bounded context</span> مشخص باشد
5. تفاوت <span dir="ltr">Module</span> و <span dir="ltr">Deployable Service</span> چیست؟ <span dir="ltr">Deployable Service</span> یک واحد <span dir="ltr">runtime</span> قابل اجراست در صورتی که یک <span dir="ltr">Bounded Context</span> می‌تواند ابتدا یک <span dir="ltr">Module</span> باشد و بعداً یک یا چند <span dir="ltr">Deployable Service</span> شود.
6. زنجیرهٔ زیر چه اشکالی دارد؟

</div>
