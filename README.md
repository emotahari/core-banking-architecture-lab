<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Core Banking Architecture Lab</span>

یک آزمایشگاه ۲۴ هفته‌ای و مستندمحور برای یادگیری عمیق معماری نرم‌افزار و معماری <span dir="ltr">Core Banking</span>؛ با <span dir="ltr">Java</span>، <span dir="ltr">Spring</span>، مدل‌سازی دامینی، داده، حسابداری، معماری رویدادمحور و دفاع معماری.

> وضعیت فعلی: **<span dir="ltr">Sprint 01</span> · <span dir="ltr">Week 01</span> — محتوای کامل آماده؛ پاسخ <span dir="ltr">Day 01</span> در انتظار تکمیل/<span dir="ltr">Review</span>**

این مخزن کتابی برای ورق‌زدن نیست. هر مفهوم باید به یک <span dir="ltr">Artifact</span>، تصمیم، کد، تست یا دفاع کوتاه تبدیل شود.

## از کجا شروع کنم؟

1. ابتدا [قرارداد آموزشی](TEACHING-CONTRACT.md) را بخوان.
2. برنامهٔ کل دوره را در [نقشهٔ راه ۲۴ هفته‌ای](core-banking-architecture-roadmap-fa.md) ببین.
3. وارد [<span dir="ltr">Sprint 01</span>](sprints/01-bank-map-boundaries/README.md) شو.
4. برنامه، درس‌ها، تمرین‌ها و ترتیب اجرای کامل را در [<span dir="ltr">Week 01</span>](sprints/01-bank-map-boundaries/week-01-capability-to-contract/README.md) ببین.
5. پاسخ خام <span dir="ltr">Day 01</span> را پاک نکن؛ پرسش‌های باقی‌مانده را کامل و سپس از <span dir="ltr">Day 02</span> ادامه بده.

## پروژهٔ ثابت دوره

یک <span dir="ltr">Core Banking</span> آموزشی با شش دامین اصلی:

- <span dir="ltr">Party</span> & <span dir="ltr">Customer</span>
- <span dir="ltr">Product</span> & <span dir="ltr">Agreement</span>
- <span dir="ltr">Deposits</span>
- <span dir="ltr">Lending</span>
- <span dir="ltr">Payments</span>
- <span dir="ltr">Accounting</span>

سه برش عمودی تا انتهای دوره واقعاً پیاده‌سازی و آزمون می‌شوند:

1. اعطای تسهیلات و واریز مبلغ به سپرده
2. انتقال وجه بین‌شعبه‌ای
3. شکست سپردهٔ بلندمدت و اصلاح سود

## نقشهٔ اسپرینت‌ها

| اسپرینت | هفته‌ها | محور | وضعیت |
|---|---:|---|---|
| [01](sprints/01-bank-map-boundaries/README.md) | ۱–۲ | نقشهٔ بانک، زبان و مرزها | **<span dir="ltr">Doing</span>** |
| [02](sprints/02-domain-model-code-architecture/README.md) | ۳–۴ | <span dir="ltr">Domain Model</span> و معماری داخلی کد | <span dir="ltr">Backlog</span> |
| [03](sprints/03-contracts-services-security/README.md) | ۵–۶ | قرارداد، مرز سرویس و امنیت | <span dir="ltr">Backlog</span> |
| [04](sprints/04-transactions-balances-cqrs/README.md) | ۷–۸ | تراکنش، مانده و <span dir="ltr">CQRS</span> | <span dir="ltr">Backlog</span> |
| [05](sprints/05-events-kafka-outbox/README.md) | ۹–۱۰ | <span dir="ltr">Event</span>، <span dir="ltr">Kafka</span> و <span dir="ltr">Outbox/Inbox</span> | <span dir="ltr">Backlog</span> |
| [06](sprints/06-saga-failure-observability/README.md) | ۱۱–۱۲ | <span dir="ltr">Saga</span>، شکست و <span dir="ltr">Observability</span> | <span dir="ltr">Backlog</span> |
| [07](sprints/07-accounting-facts-ledger/README.md) | ۱۳–۱۴ | <span dir="ltr">Accounting Facts</span>، <span dir="ltr">Ledger</span> و <span dir="ltr">GL</span> | <span dir="ltr">Backlog</span> |
| [08](sprints/08-data-performance-eod/README.md) | ۱۵–۱۶ | طراحی فیزیکی داده، <span dir="ltr">Performance</span> و <span dir="ltr">EOD</span> | <span dir="ltr">Backlog</span> |
| [09](sprints/09-customer-product-deposits/README.md) | ۱۷–۱۸ | <span dir="ltr">Customer</span>، <span dir="ltr">Product</span>، <span dir="ltr">Deposits</span> و <span dir="ltr">Teller</span> | <span dir="ltr">Backlog</span> |
| [10](sprints/10-lending-payments-near-core/README.md) | ۱۹–۲۰ | <span dir="ltr">Lending</span>، <span dir="ltr">Collections</span> و <span dir="ltr">Payments</span> | <span dir="ltr">Backlog</span> |
| [11](sprints/11-microfrontend-production/README.md) | ۲۱–۲۲ | <span dir="ltr">Micro-frontend</span> و <span dir="ltr">Production Architecture</span> | <span dir="ltr">Backlog</span> |
| [12](sprints/12-integration-migration-defense/README.md) | ۲۳–۲۴ | یکپارچه‌سازی، مهاجرت و دفاع نهایی | <span dir="ltr">Backlog</span> |

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

ریل اصلی هر هفته ۳۶۰ دقیقه و هفت نقطهٔ کنترل دارد. خواندن به‌تنهایی <span dir="ltr">Done</span> نیست:

1. یادگیری هدایت‌شده
2. تحلیل مسئلهٔ بانکی
3. مدل‌سازی و تصمیم
4. پیاده‌سازی
5. تست منفی یا <span dir="ltr">Failure</span>
6. <span dir="ltr">Refactor</span> و ثبت تصمیم
7. دفاع کوتاه و گزارش

### مسیر توسعه‌یافته از <span dir="ltr">Week 01</span>

هفت نقطهٔ کنترل و ۳۶۰ دقیقهٔ بالا بدون کاهش حفظ می‌شوند. برای تقویت هم‌زمان مهارت کدنویسی و شناخت صنعت، دو جلسه به انتهای هر هفته افزوده شده است:

8. **<span dir="ltr">Code Craft Lab</span> — ۱۰۵ دقیقه:** <span dir="ltr">Clean Code</span>، <span dir="ltr">Refactoring</span>، <span dir="ltr">Design Pattern</span>، تست و <span dir="ltr">Code Review</span> روی همان مسئلهٔ بانکی
9. **<span dir="ltr">Core Banking Case File</span> — ۴۵ دقیقه:** داستان مستند یک <span dir="ltr">Core Banking</span> یا سامانهٔ بانکی واقعی از تولد تا معماری، خطاها و دستاوردهای جاری

نسخهٔ کامل برنامه از <span dir="ltr">Week 01</span> برابر ۵۱۰ دقیقه است. قرارداد، <span dir="ltr">Definition of Done</span> و نقشهٔ موضوعات در [الحاقیهٔ ثابت هفتگی](docs/course/expanded-weekly-tracks.md) آمده است.

قواعد مشارکت، نام <span dir="ltr">Branch</span> و <span dir="ltr">Commit</span> و <span dir="ltr">Definition of Done</span> در [<span dir="ltr">CONTRIBUTING.md</span>](CONTRIBUTING.md) ثبت شده‌اند.

## خط پایهٔ فنی

- <span dir="ltr">Java 21 LTS</span>
- <span dir="ltr">Spring Boot 4.1.0</span>
- <span dir="ltr">Spring Modulith 2.1.0</span>
- <span dir="ltr">Maven</span>
- <span dir="ltr">PostgreSQL</span> برای اجرای روزانه
- <span dir="ltr">Oracle</span> برای طراحی فیزیکی و آزمایش‌های بانکی
- <span dir="ltr">Kafka</span>، <span dir="ltr">Testcontainers</span>، <span dir="ltr">OpenTelemetry</span>، <span dir="ltr">React/Vite</span> و <span dir="ltr">Kubernetes</span> در اسپرینت‌های مربوط

نسخه‌ها هنگام شروع هر اسپرینت با مستندات رسمی دوباره کنترل می‌شوند.


</div>
