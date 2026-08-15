<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Banking Modulith</bdi>

این برنامه نقطهٔ شروع واحد پروژه است. ایجاد چند <bdi dir="ltr">Package</bdi> دامینی در <bdi dir="ltr">Week 02</bdi> به معنی استقرار چند <bdi dir="ltr">Microservice</bdi> نیست.

## نسخه‌ها

- <bdi dir="ltr">Java 21</bdi>
- <bdi dir="ltr">Spring Boot 4.1.0</bdi>
- <bdi dir="ltr">Spring Modulith 2.1.0</bdi>
- <bdi dir="ltr">Maven 3.6.3+</bdi>

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

- <bdi dir="ltr">Application skeleton:</bdi> آماده
- <bdi dir="ltr">Context smoke test:</bdi> آماده
- <bdi dir="ltr">Value Object</bdi>ها: تمرین <bdi dir="ltr">Day 06</bdi>
- شش <bdi dir="ltr">Application Module:</bdi> [تمرین <bdi dir="ltr">Week 02</bdi> / <bdi dir="ltr">Day 05</bdi>](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-05-module-skeleton.md)
- <bdi dir="ltr">Module Verification:</bdi> [تمرین <bdi dir="ltr">Week 02</bdi> / <bdi dir="ltr">Day 06</bdi>](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-06-module-verification.md)
- <bdi dir="ltr">Code Craft starter:</bdi> [<bdi dir="ltr">Transfer Fee Refactoring</bdi> / <bdi dir="ltr">Day 08</bdi>](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-08-transfer-fee-refactoring.md)

## قواعد

- کد دامینی به <bdi dir="ltr">Controller</bdi>، <bdi dir="ltr">JPA Entity</bdi> یا <bdi dir="ltr">Message Broker</bdi> وابسته نمی‌شود.
- <bdi dir="ltr">Type</bdi>های دامینی برای راحتی <bdi dir="ltr">Persistence</bdi> تضعیف نمی‌شوند.
- <bdi dir="ltr">Package</bdi> داخلی ماژول از ماژول دیگر قابل استفاده نیست.
- <bdi dir="ltr">Microservice</bdi> فقط پس از <bdi dir="ltr">ADR</bdi> و شواهد استخراج می‌شود.

</div>
