<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Banking Modulith</span>

این برنامه نقطهٔ شروع واحد پروژه است. ایجاد چند <span dir="ltr">Package</span> دامینی در <span dir="ltr">Week 02</span> به معنی استقرار چند <span dir="ltr">Microservice</span> نیست.

## نسخه‌ها

- <span dir="ltr">Java 21</span>
- <span dir="ltr">Spring Boot 4.1.0</span>
- <span dir="ltr">Spring Modulith 2.1.0</span>
- <span dir="ltr">Maven 3.6.3+</span>

## اجرا


</div>

<div dir="ltr" align="left">

~~~bash
mvn verify
mvn spring-boot:run
~~~

</div>

<div dir="rtl" align="right">


## وضعیت

- <span dir="ltr">Application skeleton:</span> آماده
- <span dir="ltr">Context smoke test:</span> آماده
- <span dir="ltr">Value Object</span>ها: تمرین <span dir="ltr">Day 06</span>
- شش <span dir="ltr">Application Module:</span> [تمرین <span dir="ltr">Week 02</span> / <span dir="ltr">Day 05</span>](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-05-module-skeleton.md)
- <span dir="ltr">Module Verification:</span> [تمرین <span dir="ltr">Week 02</span> / <span dir="ltr">Day 06</span>](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-06-module-verification.md)
- <span dir="ltr">Code Craft starter:</span> [<span dir="ltr">Transfer Fee Refactoring</span> / <span dir="ltr">Day 08</span>](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-08-transfer-fee-refactoring.md)

## قواعد

- کد دامینی به <span dir="ltr">Controller</span>، <span dir="ltr">JPA Entity</span> یا <span dir="ltr">Message Broker</span> وابسته نمی‌شود.
- <span dir="ltr">Type</span>های دامینی برای راحتی <span dir="ltr">Persistence</span> تضعیف نمی‌شوند.
- <span dir="ltr">Package</span> داخلی ماژول از ماژول دیگر قابل استفاده نیست.
- <span dir="ltr">Microservice</span> فقط پس از <span dir="ltr">ADR</span> و شواهد استخراج می‌شود.

</div>
