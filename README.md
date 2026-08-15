# Core Banking Architecture Lab

یک آزمایشگاه ۲۴ هفته‌ای و مستندمحور برای یادگیری عمیق معماری نرم‌افزار و معماری Core Banking؛ با Java، Spring، مدل‌سازی دامینی، داده، حسابداری، معماری رویدادمحور و دفاع معماری.

> وضعیت فعلی: **Sprint 01 · Week 01 · Day 01 — Doing**

این مخزن کتابی برای ورق‌زدن نیست. هر مفهوم باید به یک Artifact، تصمیم، کد، تست یا دفاع کوتاه تبدیل شود.

## از کجا شروع کنم؟

1. ابتدا [قرارداد آموزشی](TEACHING-CONTRACT.md) را بخوان.
2. برنامهٔ کل دوره را در [نقشهٔ راه ۲۴ هفته‌ای](core-banking-architecture-roadmap-fa.md) ببین.
3. وارد [Sprint 01](sprints/01-bank-map-boundaries/README.md) شو.
4. برای شروع واقعی، دستور روز اول را در [Week 01 / Day 01](sprints/01-bank-map-boundaries/week-01-capability-to-contract/README.md) اجرا کن.
5. قبل از خواندن درس، پاسخ خط پایه را در [قالب پاسخ روز اول](sprints/01-bank-map-boundaries/week-01-capability-to-contract/submissions/day-01-baseline-response.md) بنویس.

## پروژهٔ ثابت دوره

یک Core Banking آموزشی با شش دامین اصلی:

- Party & Customer
- Product & Agreement
- Deposits
- Lending
- Payments
- Accounting

سه برش عمودی تا انتهای دوره واقعاً پیاده‌سازی و آزمون می‌شوند:

1. اعطای تسهیلات و واریز مبلغ به سپرده
2. انتقال وجه بین‌شعبه‌ای
3. شکست سپردهٔ بلندمدت و اصلاح سود

## نقشهٔ اسپرینت‌ها

| اسپرینت | هفته‌ها | محور | وضعیت |
|---|---:|---|---|
| [01](sprints/01-bank-map-boundaries/README.md) | ۱–۲ | نقشهٔ بانک، زبان و مرزها | **Doing** |
| [02](sprints/02-domain-model-code-architecture/README.md) | ۳–۴ | Domain Model و معماری داخلی کد | Backlog |
| [03](sprints/03-contracts-services-security/README.md) | ۵–۶ | قرارداد، مرز سرویس و امنیت | Backlog |
| [04](sprints/04-transactions-balances-cqrs/README.md) | ۷–۸ | تراکنش، مانده و CQRS | Backlog |
| [05](sprints/05-events-kafka-outbox/README.md) | ۹–۱۰ | Event، Kafka و Outbox/Inbox | Backlog |
| [06](sprints/06-saga-failure-observability/README.md) | ۱۱–۱۲ | Saga، شکست و Observability | Backlog |
| [07](sprints/07-accounting-facts-ledger/README.md) | ۱۳–۱۴ | Accounting Facts، Ledger و GL | Backlog |
| [08](sprints/08-data-performance-eod/README.md) | ۱۵–۱۶ | طراحی فیزیکی داده، Performance و EOD | Backlog |
| [09](sprints/09-customer-product-deposits/README.md) | ۱۷–۱۸ | Customer، Product، Deposits و Teller | Backlog |
| [10](sprints/10-lending-payments-near-core/README.md) | ۱۹–۲۰ | Lending، Collections و Payments | Backlog |
| [11](sprints/11-microfrontend-production/README.md) | ۲۱–۲۲ | Micro-frontend و Production Architecture | Backlog |
| [12](sprints/12-integration-migration-defense/README.md) | ۲۳–۲۴ | یکپارچه‌سازی، مهاجرت و دفاع نهایی | Backlog |

## ساختار مخزن

~~~text
.
├── backend/                    کد Java/Spring
├── contracts/                  OpenAPI، AsyncAPI و Schemaها
├── docs/                       قرارداد دوره، ADR، مدل‌ها و تصمیم‌ها
├── frontend/                   از Sprint 11
├── platform/                   Compose، Observability و Kubernetes
├── sprints/                    محتوای آموزشی و خروجی هر اسپرینت
├── tests/                      E2E، Failure و Performance
└── core-banking-architecture-roadmap-fa.md
~~~

## ریتم هفتگی

هر هفته حداکثر شش ساعت و دقیقاً هفت نقطهٔ کنترل دارد. خواندن به‌تنهایی Done نیست:

1. یادگیری هدایت‌شده
2. تحلیل مسئلهٔ بانکی
3. مدل‌سازی و تصمیم
4. پیاده‌سازی
5. تست منفی یا Failure
6. Refactor و ثبت تصمیم
7. دفاع کوتاه و گزارش

### مسیر توسعه‌یافته از Week 02

هفت نقطهٔ کنترل و ۳۶۰ دقیقهٔ بالا بدون کاهش حفظ می‌شوند. برای تقویت هم‌زمان مهارت کدنویسی و شناخت صنعت، دو جلسه به انتهای هر هفته افزوده شده است:

8. **Code Craft Lab — ۱۰۵ دقیقه:** Clean Code، Refactoring، Design Pattern، تست و Code Review روی همان مسئلهٔ بانکی
9. **Core Banking Case File — ۴۵ دقیقه:** داستان مستند یک Core Banking یا سامانهٔ بانکی واقعی از تولد تا معماری، خطاها و دستاوردهای جاری

نسخهٔ کامل برنامه از Week 02 برابر ۵۱۰ دقیقه است. قرارداد، Definition of Done و نقشهٔ موضوعات در [الحاقیهٔ ثابت هفتگی](docs/course/expanded-weekly-tracks.md) آمده است.

قواعد مشارکت، نام Branch و Commit و Definition of Done در [CONTRIBUTING.md](CONTRIBUTING.md) ثبت شده‌اند.

## خط پایهٔ فنی

- Java 21 LTS
- Spring Boot 4.1.0
- Spring Modulith 2.1.0
- Maven
- PostgreSQL برای اجرای روزانه
- Oracle برای طراحی فیزیکی و آزمایش‌های بانکی
- Kafka، Testcontainers، OpenTelemetry، React/Vite و Kubernetes در اسپرینت‌های مربوط

نسخه‌ها هنگام شروع هر اسپرینت با مستندات رسمی دوباره کنترل می‌شوند.
