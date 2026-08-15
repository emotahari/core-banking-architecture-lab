<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Sprint 01</bdi> — نقشهٔ بانک، زبان و مرزها

- <bdi dir="ltr">Weeks: 01</bdi>–02
- <bdi dir="ltr">Status:</bdi> **<bdi dir="ltr">Doing</bdi>**
- <bdi dir="ltr">Outcome:</bdi> عبور مستدل از <bdi dir="ltr">Capability</bdi> به <bdi dir="ltr">Domain</bdi>، <bdi dir="ltr">Bounded Context</bdi>، <bdi dir="ltr">Module/Service</bdi> و <bdi dir="ltr">Contract</bdi>

![اینفوگرافیک اسپرینت اول](sprint-01-infographic.svg)

## هفته‌ها

1. [<bdi dir="ltr">Week 01</bdi> — <bdi dir="ltr">Capability</bdi> تا <bdi dir="ltr">API/Event</bdi>](week-01-capability-to-contract/README.md)
2. [<bdi dir="ltr">Week 02</bdi> — <bdi dir="ltr">Strategic DDD</bdi> و مالکیت](week-02-strategic-ddd-ownership/README.md)

از <bdi dir="ltr">Week 01</bdi>، ریل اصلی هر هفته بدون کاهش با دو خروجی افزوده تکمیل می‌شود: <bdi dir="ltr">Code Craft Lab</bdi> و پروندهٔ مستند یک <bdi dir="ltr">Core Banking/</bdi>سامانهٔ بانکی واقعی. استاندارد مشترک در [الحاقیهٔ هفتگی](../../docs/course/expanded-weekly-tracks.md) ثبت شده است.

## خروجی اسپرینت

- <bdi dir="ltr">Banking Capability Map v1</bdi>
- <bdi dir="ltr">Domain Map</bdi> و <bdi dir="ltr">Context Map v1</bdi>
- واژه‌نامهٔ حداقل ۴۰ اصطلاح
- <bdi dir="ltr">Data/Decision Ownership Matrix v1</bdi>
- شش پروندهٔ دامینی اولیه
- شش ماژول منطقی <bdi dir="ltr">Spring Modulith</bdi>
- <bdi dir="ltr">Architecture Fitness Test</bdi>
- دو <bdi dir="ltr">Code Craft Lab</bdi> با تست و <bdi dir="ltr">Pattern Decision</bdi>
- دو پروندهٔ مستند سامانهٔ بانکی: <bdi dir="ltr">UPI</bdi> و <bdi dir="ltr">Monzo</bdi>

## <bdi dir="ltr">Gate</bdi>

برای قابلیت «مسدودی قضایی سپرده» باید بدون شروع از جدول یا نام سرویس، این زنجیره دفاع شود:


</div>

<div dir="ltr" align="left">

```text
Capability → Domain/Subdomain → Bounded Context → Module/Service
           → Use Case → Command/Query → API/Event
```

</div>

<div dir="rtl" align="right">


هیچ <bdi dir="ltr">Service Candidate</bdi> بدون <bdi dir="ltr">Capability</bdi>، مالک کسب‌وکار و دلیل <bdi dir="ltr">Boundary</bdi> پذیرفته نمی‌شود.


</div>
