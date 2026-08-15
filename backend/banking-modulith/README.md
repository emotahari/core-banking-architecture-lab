# Banking Modulith

این برنامه نقطهٔ شروع واحد پروژه است. ایجاد چند Package دامینی در Week 02 به معنی استقرار چند Microservice نیست.

## نسخه‌ها

- Java 21
- Spring Boot 4.1.0
- Spring Modulith 2.1.0
- Maven 3.6.3+

## اجرا

~~~bash
mvn verify
mvn spring-boot:run
~~~

## وضعیت

- Application skeleton: آماده
- Context smoke test: آماده
- Value Objectها: تمرین Day 06
- شش Application Module: [تمرین Week 02 / Day 05](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-05-module-skeleton.md)
- Module Verification: [تمرین Week 02 / Day 06](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-06-module-verification.md)
- Code Craft starter: [Transfer Fee Refactoring / Day 08](../../sprints/01-bank-map-boundaries/week-02-strategic-ddd-ownership/exercises/day-08-transfer-fee-refactoring.md)

## قواعد

- کد دامینی به Controller، JPA Entity یا Message Broker وابسته نمی‌شود.
- Typeهای دامینی برای راحتی Persistence تضعیف نمی‌شوند.
- Package داخلی ماژول از ماژول دیگر قابل استفاده نیست.
- Microservice فقط پس از ADR و شواهد استخراج می‌شود.
