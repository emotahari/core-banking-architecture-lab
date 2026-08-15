<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Core Banking Architecture Lab</bdi>

یک آزمایشگاه ۲۴ هفته‌ای و مستندمحور برای یادگیری عمیق معماری نرم‌افزار و معماری <bdi dir="ltr">Core Banking</bdi>؛ با <bdi dir="ltr">Java</bdi>، <bdi dir="ltr">Spring</bdi>، مدل‌سازی دامینی، داده، حسابداری، معماری رویدادمحور و دفاع معماری.

> وضعیت فعلی: **<bdi dir="ltr">Sprint 01</bdi> · <bdi dir="ltr">Week 01</bdi> — محتوای کامل آماده؛ پاسخ <bdi dir="ltr">Day 01</bdi> در انتظار تکمیل/<bdi dir="ltr">Review</bdi>**

این مخزن کتابی برای ورق‌زدن نیست. هر مفهوم باید به یک <bdi dir="ltr">Artifact</bdi>، تصمیم، کد، تست یا دفاع کوتاه تبدیل شود.

## از کجا شروع کنم؟

1. ابتدا [قرارداد آموزشی](TEACHING-CONTRACT.md) را بخوان.
2. برنامهٔ کل دوره را در [نقشهٔ راه ۲۴ هفته‌ای](core-banking-architecture-roadmap-fa.md) ببین.
3. وارد [<bdi dir="ltr">Sprint 01</bdi>](sprints/01-bank-map-boundaries/README.md) شو.
4. برنامه، درس‌ها، تمرین‌ها و ترتیب اجرای کامل را در [<bdi dir="ltr">Week 01</bdi>](sprints/01-bank-map-boundaries/week-01-capability-to-contract/README.md) ببین.
5. پاسخ خام <bdi dir="ltr">Day 01</bdi> را پاک نکن؛ پرسش‌های باقی‌مانده را کامل و سپس از <bdi dir="ltr">Day 02</bdi> ادامه بده.

## پروژهٔ ثابت دوره

یک <bdi dir="ltr">Core Banking</bdi> آموزشی با شش دامین اصلی:

- <bdi dir="ltr">Party</bdi> & <bdi dir="ltr">Customer</bdi>
- <bdi dir="ltr">Product</bdi> & <bdi dir="ltr">Agreement</bdi>
- <bdi dir="ltr">Deposits</bdi>
- <bdi dir="ltr">Lending</bdi>
- <bdi dir="ltr">Payments</bdi>
- <bdi dir="ltr">Accounting</bdi>

سه برش عمودی تا انتهای دوره واقعاً پیاده‌سازی و آزمون می‌شوند:

1. اعطای تسهیلات و واریز مبلغ به سپرده
2. انتقال وجه بین‌شعبه‌ای
3. شکست سپردهٔ بلندمدت و اصلاح سود

## نقشهٔ اسپرینت‌ها

| اسپرینت | هفته‌ها | محور | وضعیت |
|---|---:|---|---|
| [01](sprints/01-bank-map-boundaries/README.md) | ۱–۲ | نقشهٔ بانک، زبان و مرزها | **<bdi dir="ltr">Doing</bdi>** |
| [02](sprints/02-domain-model-code-architecture/README.md) | ۳–۴ | <bdi dir="ltr">Domain Model</bdi> و معماری داخلی کد | <bdi dir="ltr">Backlog</bdi> |
| [03](sprints/03-contracts-services-security/README.md) | ۵–۶ | قرارداد، مرز سرویس و امنیت | <bdi dir="ltr">Backlog</bdi> |
| [04](sprints/04-transactions-balances-cqrs/README.md) | ۷–۸ | تراکنش، مانده و <bdi dir="ltr">CQRS</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [05](sprints/05-events-kafka-outbox/README.md) | ۹–۱۰ | <bdi dir="ltr">Event</bdi>، <bdi dir="ltr">Kafka</bdi> و <bdi dir="ltr">Outbox/Inbox</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [06](sprints/06-saga-failure-observability/README.md) | ۱۱–۱۲ | <bdi dir="ltr">Saga</bdi>، شکست و <bdi dir="ltr">Observability</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [07](sprints/07-accounting-facts-ledger/README.md) | ۱۳–۱۴ | <bdi dir="ltr">Accounting Facts</bdi>، <bdi dir="ltr">Ledger</bdi> و <bdi dir="ltr">GL</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [08](sprints/08-data-performance-eod/README.md) | ۱۵–۱۶ | طراحی فیزیکی داده، <bdi dir="ltr">Performance</bdi> و <bdi dir="ltr">EOD</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [09](sprints/09-customer-product-deposits/README.md) | ۱۷–۱۸ | <bdi dir="ltr">Customer</bdi>، <bdi dir="ltr">Product</bdi>، <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">Teller</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [10](sprints/10-lending-payments-near-core/README.md) | ۱۹–۲۰ | <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Collections</bdi> و <bdi dir="ltr">Payments</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [11](sprints/11-microfrontend-production/README.md) | ۲۱–۲۲ | <bdi dir="ltr">Micro-frontend</bdi> و <bdi dir="ltr">Production Architecture</bdi> | <bdi dir="ltr">Backlog</bdi> |
| [12](sprints/12-integration-migration-defense/README.md) | ۲۳–۲۴ | یکپارچه‌سازی، مهاجرت و دفاع نهایی | <bdi dir="ltr">Backlog</bdi> |

## ساختار مخزن


</div>

<div dir="ltr" align="left">

```text
.
├── backend/                    کد Java/Spring
├── contracts/                  OpenAPI، AsyncAPI و Schemaها
├── docs/                       قرارداد دوره، ADR، مدل‌ها و تصمیم‌ها
├── frontend/                   از Sprint 11
├── platform/                   Compose، Observability و Kubernetes
├── sprints/                    محتوای آموزشی و خروجی هر اسپرینت
├── tests/                      E2E، Failure و Performance
└── core-banking-architecture-roadmap-fa.md
```

</div>

<div dir="rtl" align="right">


## ریتم هفتگی

ریل اصلی هر هفته ۳۶۰ دقیقه و هفت نقطهٔ کنترل دارد. خواندن به‌تنهایی <bdi dir="ltr">Done</bdi> نیست:

1. یادگیری هدایت‌شده
2. تحلیل مسئلهٔ بانکی
3. مدل‌سازی و تصمیم
4. پیاده‌سازی
5. تست منفی یا <bdi dir="ltr">Failure</bdi>
6. <bdi dir="ltr">Refactor</bdi> و ثبت تصمیم
7. دفاع کوتاه و گزارش

### مسیر توسعه‌یافته از <bdi dir="ltr">Week 01</bdi>

هفت نقطهٔ کنترل و ۳۶۰ دقیقهٔ بالا بدون کاهش حفظ می‌شوند. برای تقویت هم‌زمان مهارت کدنویسی و شناخت صنعت، دو جلسه به انتهای هر هفته افزوده شده است:

8. **<bdi dir="ltr">Code Craft Lab</bdi> — ۱۰۵ دقیقه:** <bdi dir="ltr">Clean Code</bdi>، <bdi dir="ltr">Refactoring</bdi>، <bdi dir="ltr">Design Pattern</bdi>، تست و <bdi dir="ltr">Code Review</bdi> روی همان مسئلهٔ بانکی
9. **<bdi dir="ltr">Core Banking Case File</bdi> — ۴۵ دقیقه:** داستان مستند یک <bdi dir="ltr">Core Banking</bdi> یا سامانهٔ بانکی واقعی از تولد تا معماری، خطاها و دستاوردهای جاری

نسخهٔ کامل برنامه از <bdi dir="ltr">Week 01</bdi> برابر ۵۱۰ دقیقه است. قرارداد، <bdi dir="ltr">Definition of Done</bdi> و نقشهٔ موضوعات در [الحاقیهٔ ثابت هفتگی](docs/course/expanded-weekly-tracks.md) آمده است.

قواعد مشارکت، نام <bdi dir="ltr">Branch</bdi> و <bdi dir="ltr">Commit</bdi> و <bdi dir="ltr">Definition of Done</bdi> در [<bdi dir="ltr">CONTRIBUTING.md</bdi>](CONTRIBUTING.md) ثبت شده‌اند.

## خط پایهٔ فنی

- <bdi dir="ltr">Java 21 LTS</bdi>
- <bdi dir="ltr">Spring Boot 4.1.0</bdi>
- <bdi dir="ltr">Spring Modulith 2.1.0</bdi>
- <bdi dir="ltr">Maven</bdi>
- <bdi dir="ltr">PostgreSQL</bdi> برای اجرای روزانه
- <bdi dir="ltr">Oracle</bdi> برای طراحی فیزیکی و آزمایش‌های بانکی
- <bdi dir="ltr">Kafka</bdi>، <bdi dir="ltr">Testcontainers</bdi>، <bdi dir="ltr">OpenTelemetry</bdi>، <bdi dir="ltr">React/Vite</bdi> و <bdi dir="ltr">Kubernetes</bdi> در اسپرینت‌های مربوط

نسخه‌ها هنگام شروع هر اسپرینت با مستندات رسمی دوباره کنترل می‌شوند.


</div>
