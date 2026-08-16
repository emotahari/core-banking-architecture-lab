<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Sprint 01</span> — نقشهٔ بانک، زبان و مرزها

- <span dir="ltr">Weeks: 01</span>–02
- <span dir="ltr">Status:</span> **<span dir="ltr">Doing</span>**
- <span dir="ltr">Outcome:</span> عبور مستدل از <span dir="ltr">Capability</span> به <span dir="ltr">Domain</span>، <span dir="ltr">Bounded Context</span>، <span dir="ltr">Module/Service</span> و <span dir="ltr">Contract</span>

![اینفوگرافیک اسپرینت اول](sprint-01-infographic.svg)

## هفته‌ها

1. [<span dir="ltr">Week 01</span> — <span dir="ltr">Capability</span> تا <span dir="ltr">API/Event</span>](week-01-capability-to-contract/README.md)
2. [<span dir="ltr">Week 02</span> — <span dir="ltr">Strategic DDD</span> و مالکیت](week-02-strategic-ddd-ownership/README.md)

از <span dir="ltr">Week 01</span>، ریل اصلی هر هفته بدون کاهش با دو خروجی افزوده تکمیل می‌شود: <span dir="ltr">Code Craft Lab</span> و پروندهٔ مستند یک <span dir="ltr">Core Banking/</span>سامانهٔ بانکی واقعی. استاندارد مشترک در [الحاقیهٔ هفتگی](../../docs/course/expanded-weekly-tracks.md) ثبت شده است.

## خروجی اسپرینت

- <span dir="ltr">Banking Capability Map v1</span>
- <span dir="ltr">Domain Map</span> و <span dir="ltr">Context Map v1</span>
- واژه‌نامهٔ حداقل ۴۰ اصطلاح
- <span dir="ltr">Data/Decision Ownership Matrix v1</span>
- شش پروندهٔ دامینی اولیه
- شش ماژول منطقی <span dir="ltr">Spring Modulith</span>
- <span dir="ltr">Architecture Fitness Test</span>
- دو <span dir="ltr">Code Craft Lab</span> با تست و <span dir="ltr">Pattern Decision</span>
- دو پروندهٔ مستند سامانهٔ بانکی: <span dir="ltr">UPI</span> و <span dir="ltr">Monzo</span>

## <span dir="ltr">Gate</span>

برای قابلیت «مسدودی قضایی سپرده» باید بدون شروع از جدول یا نام سرویس، این زنجیره دفاع شود:


</div>

<div dir="ltr" align="left">

```text
Capability → Domain/Subdomain → Bounded Context → Module/Service
           → Use Case → Command/Query → API/Event
```

</div>

<div dir="rtl" align="right">


هیچ <span dir="ltr">Service Candidate</span> بدون <span dir="ltr">Capability</span>، مالک کسب‌وکار و دلیل <span dir="ltr">Boundary</span> پذیرفته نمی‌شود.


</div>
