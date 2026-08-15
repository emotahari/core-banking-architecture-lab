# Day 05 — تبدیل فرضیهٔ مرزها به Spring Modulith

- Day budget: 100 minutes — 20 lesson/reference + 75 implementation + 5 exit ticket
- Output: six logical Application Modules + dependency policy
- Code root: `backend/banking-modulith`
- Versions: Java 21، Spring Boot 4.1.0، Spring Modulith 2.1.0

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. توضیح بدهی چرا Application Module یک Boundary منطقی است، نه Microservice.
2. شش Module را بر اساس Packageهای Function-first بسازی.
3. Provided Interface، Internal Implementation و Required Interface را تشخیص بدهی.
4. `@ApplicationModule`، `allowedDependencies` و `@NamedInterface` را درست به‌کار ببری.
5. Dependency Policy را از Context Map استخراج کنی؛ نه از ترتیب Controllerها.
6. از ساخت `common` یا Shared Entity بدون دلیل جلوگیری کنی.

## 2. چرا بعد از چهار روز تحلیل وارد کد می‌شویم؟

Package Structure یک تصمیم بی‌اثر نیست. Dependencyهای Compile-time و دسترسی به Typeها به‌تدریج مدل ذهنی تیم را تثبیت می‌کنند. اگر از روز اول Packageها را بر اساس جدول یا Layer بسازیم، حتی یک Domain Map خوب نیز در کد بی‌اثر می‌شود.

ترتیب این هفته عمداً چنین بود:

~~~text
Subdomain strategy
  → language boundaries
  → context relationships
  → data/decision ownership
  → module hypothesis in code
~~~

امروز کد «اثبات» نمی‌کند Boundary دامینی درست است. کد فقط فرضیهٔ فعلی را:

- آشکار می‌کند؛
- Dependencyهای آن را قابل‌مشاهده می‌کند؛
- نقض آن را قابل‌آزمون می‌کند؛
- امکان Refactor آینده را بالا می‌برد.

## 3. Application Module در Spring Modulith

طبق [مستند رسمی Fundamentals](https://docs.spring.io/spring-modulith/reference/fundamentals.html)، یک Application Module واحدی از Functionality است که سه بخش دارد:

### Provided Interface

آنچه Module به دیگر Moduleها عرضه می‌کند:

- Spring Beanهای Public API
- Command/Query facadeهای منطقی
- Application/Domain Eventهای Published
- Typeهای Contract که عمداً Expose شده‌اند

Provided Interface با REST Controller یکی نیست. REST می‌تواند Adapter بیرونی باشد؛ Module API یک Boundary داخل Application است.

### Internal Implementation

جزئیاتی که دیگر Moduleها نباید بدانند:

- Domain model internals
- Repository implementations
- Policy/Strategy implementations
- JPA mappings
- workflow details

ممکن است Type داخلی برای استفاده در Subpackageهای همان Module `public` باشد، اما Spring Modulith دسترسی Module دیگر به Subpackage داخلی را رد می‌کند.

### Required Interface

API یا Eventهایی از Moduleهای دیگر که این Module برای کارکردن نیاز دارد. Required Interface باید در Dependency Policy صریح باشد.

## 4. کشف Module با Package

Application اصلی در Package زیر است:

~~~text
com.example.corebankinglab
└── CoreBankingLabApplication
~~~

در Detection پیش‌فرض Spring Modulith، هر Direct Subpackage زیر Package اصلی یک Application Module Candidate است:

~~~text
com.example.corebankinglab.partycustomer
com.example.corebankinglab.productagreement
com.example.corebankinglab.deposits
com.example.corebankinglab.lending
com.example.corebankinglab.payments
com.example.corebankinglab.accounting
~~~

برای Lab، این شش Module یک فرضیهٔ آموزشی‌اند. Domain Map ممکن است نشان دهد Product Catalog و Agreement دو Bounded Context هستند، اما برای Sprint 01 می‌توانند در یک Module موقت قرار بگیرند؛ این تفاوت باید در Dossier به‌عنوان Constraint/Decision ثبت شود.

## 5. API Package و Internal Package

در Module بستهٔ پیش‌فرض:

- Typeهای Public در Base Package، API قابل‌دسترسی Module هستند.
- Subpackageها Internal محسوب می‌شوند، مگر اینکه صریحاً Named Interface شوند.

نمونه:

~~~text
deposits/
├── package-info.java                 module metadata
├── DepositOperations.java           provided interface
├── DepositAccountId.java             exposed contract type, only if intentional
├── events/
│   ├── package-info.java             named interface: events
│   └── DepositCredited.java          published contract
└── internal/
    ├── DepositOperationsService.java
    ├── model/
    └── persistence/
~~~

در این هفته نیاز نیست منطق Deposits را پیاده کنی. هدف ساخت Boundary و Verification است. کلاس و Interface مصنوعی صرفاً برای پرکردن Folder نساز؛ هر Type باید Purpose داشته باشد.

## 6. `package-info.java` برای Module

نمونهٔ هدایت‌شده برای Deposits در اولین مرحله و بدون Dependency مستقیم:

```java
@org.springframework.modulith.ApplicationModule(
        displayName = "Deposits",
        allowedDependencies = {}
)
package com.example.corebankinglab.deposits;
```

نکات:

- آرایهٔ خالی یعنی Dependency به Module دیگر مجاز نیست.
- حذف `allowedDependencies` یعنی Spring Modulith Dependencyهای Module را از این Attribute محدود نمی‌کند؛ Internal-access و Cycle checks همچنان قواعد خود را دارند.
- Module به‌صورت پیش‌فرض `CLOSED` است.
- `OPEN` برای Migration تدریجی Legacy وجود دارد؛ استفاده از آن در Lab جدید، Encapsulation را تضعیف می‌کند و ممنوع است مگر ADR مستقل.

## 7. Named Interface

Base Package API پیش‌فرض را عرضه می‌کند. اگر یک Subpackage مشخص نیز باید Expose شود، آن را Named Interface کن.

مثال:

```java
@org.springframework.modulith.NamedInterface("events")
package com.example.corebankinglab.deposits.events;
```

اکنون یک Module مصرف‌کننده می‌تواند در `allowedDependencies` دقیقاً به این Interface اشاره کند:

```java
@org.springframework.modulith.ApplicationModule(
        allowedDependencies = "deposits::events"
)
package com.example.corebankinglab.accounting;
```

این کد فقط Syntax را نشان می‌دهد. اینکه Accounting واقعاً باید Compile-time به `deposits::events` وابسته باشد یا Contract در Integration Boundary دیگری قرار گیرد، یک تصمیم معماری بعدی است. امروز هر Dependency را با Context Map و Ownership دفاع کن.

می‌توان بیش از یک Dependency را نوشت:

```java
@org.springframework.modulith.ApplicationModule(
        allowedDependencies = {
                "partycustomer::reference",
                "productagreement::agreement-snapshot"
        }
)
package com.example.corebankinglab.lending;
```

این نمونه نیز پاسخ نهایی Lab نیست. Named Interfaceها باید واقعاً در Provider تعریف شده باشند و نام‌ها از Language همان Boundary بیایند.

## 8. Function-first، نه Layer-first

ساختار ضعیف:

~~~text
controller/
service/
repository/
entity/
dto/
~~~

این ساختار همهٔ Domainها را در Layerهای افقی مخلوط می‌کند و دسترسی متقابل را آسان می‌سازد.

ساختار بهتر:

~~~text
partycustomer/
productagreement/
deposits/
lending/
payments/
accounting/
~~~

هر Module می‌تواند در داخل خودش Layer یا Hexagonal structure داشته باشد؛ آن موضوع Sprint 02 است. ابتدا Boundary کسب‌وکاری، سپس ساختار داخلی.

## 9. Dependency Policy از کجا می‌آید؟

برای هر Dependency Candidate این سؤال‌ها را پاسخ بده:

1. کدام Use Case واقعاً آن را نیاز دارد؟
2. Provider کدام Fact/Capability را مالک است؟
3. Consumer به Reference، Snapshot، Query، Command یا Event نیاز دارد؟
4. آیا Dependency به یک Named Interface کوچک محدود می‌شود؟
5. آیا Event یا Translation می‌تواند Compile-time Coupling را کمتر کند؟
6. اگر Provider تغییر کند، چه چیزی در Consumer Recompile/Release می‌شود؟
7. آیا Dependency معکوس یا Cycle ایجاد می‌کند؟

وجود یک فلش در Sequence Diagram به‌تنهایی مجوز Import Typeهای داخلی نیست.

## 10. Mapping پیشنهادی اولیه، نه پاسخ قطعی

| Problem-space hypothesis | Lab module | نکته |
|---|---|---|
| Party/Customer Identity and Relationship | `partycustomer` | Consumerها Reference/Snapshot می‌گیرند |
| Product Catalog + Agreement | `productagreement` | ممکن است بعداً به دو Context/Module تفکیک شود |
| Deposit Account Servicing | `deposits` | مانده و Hold عملیاتی را محصور می‌کند |
| Loan Lifecycle/Servicing | `lending` | مانده و برنامهٔ عملیاتی Loan |
| Payment Order/Clearing/Settlement | `payments` | Channel مالک Payment State نیست |
| Journal/Subledger/GL | `accounting` | Operational Domain state را مالک نمی‌شود |

`Legal Orders` در Gate یک Context خارجی/near-core است و الزاماً Module هفتم Lab در این Sprint نیست. Contract آن با Deposits باید در Context Map نشان داده شود.

## 11. Typeهای مشترک و دام `common`

Week 01 ممکن است `Money` و Typed IDها را ساخته باشی. اکنون باید محل آن‌ها را آگاهانه بازبینی کنی.

### Typed ID

- `CustomerId` بهتر است Contract type متعلق به Authority یا Published Reference باشد.
- `AccountId` نباید با شمارهٔ حساب بانکی یا Accounting Account ID یکی فرض شود.
- Import کردن Entity کامل برای گرفتن ID ممنوع است.

### Money

مفهوم پایهٔ Amount/Currency می‌تواند بسیار کوچک و مشترک باشد، اما Policyهای Scale، Rounding و Sign ممکن است Contextual باشند. سه گزینهٔ قابل بررسی:

1. Value Object مستقل در هر Context با Semantic خاص
2. Shared Kernel بسیار کوچک با Governance سخت‌گیرانه
3. Boundary Contract type و Translation به مدل داخلی

در این Sprint یک Package عمومی `common` نساز. ابتدا Usage، Owner و Change coupling را ثبت کن. Shared Kernel یک تصمیم صریح است، نه سطل Typeهای راحت.

## 12. برنامهٔ ۷۵ دقیقه‌ای اجرا

### دقیقهٔ 0 تا 5 — Baseline

از مسیر `backend/banking-modulith` اجرا کن:

~~~bash
mvn verify
~~~

نتیجه و Commit پایه را ثبت کن. اگر Baseline قرمز است، Module work را روی شکست قبلی بنا نکن.

### دقیقهٔ 5 تا 15 — Dependency Plan

[Module Dependency Policy](../artifacts/module-dependency-policy.md) را باز کن. برای شش Module، Purpose و Provided/Required Interface فرضی را بنویس. هنوز Import نساز.

### دقیقهٔ 15 تا 35 — Base Packages

شش Direct Subpackage و `package-info.java` بساز. در مرحلهٔ اول `allowedDependencies = {}` قرار بده تا هر Dependency بعدی آگاهانه اضافه شود.

### دقیقهٔ 35 تا 50 — Public/Internal Boundary

برای هر Module:

- یک Public API واقعی یا Placeholder مستندشدهٔ حداقلی در Base Package
- یک `internal` package
- بدون Public Entity مشترک

اگر هنوز Use Case مشخصی نداری، `package-info.java` و Module description کافی است؛ API مصنوعی نساز.

### دقیقهٔ 50 تا 60 — Named Interfaces

فقط Named Interfaceهایی را بساز که Context Map نیاز آن‌ها را نشان داده است. برای هر مورد دلیل و Consumer را در Policy ثبت کن.

### دقیقهٔ 60 تا 68 — Allowed Dependencies

Dependencyهای لازم را یکی‌یکی اضافه کن. اگر برای حل Compile به Dependency متقابل نیاز شد، توقف کن: احتمالاً Contract یا Direction مشکل دارد.

### دقیقهٔ 68 تا 75 — Inspect and verify

با `ApplicationModules` ساختار کشف‌شده را چاپ کن و سپس Verification را اجرا کن. تست رسمی روز ششم اضافه می‌شود، ولی امروز باید شش Module تشخیص داده شوند.

## 13. مشاهدهٔ مدل Moduleها

نمونهٔ کد موقت یا تست:

```java
var modules = org.springframework.modulith.core.ApplicationModules
        .of(CoreBankingLabApplication.class);

modules.forEach(System.out::println);
```

خروجی را برای این موارد بخوان:

- Logical name
- Base package
- Spring beans
- Exposed types
- Direct dependencies

صرف دیدن شش نام کافی نیست؛ Public surface و Dependencyها را نیز بررسی کن.

## 14. خطاهای رایج

### شش Domain مساوی شش Microservice

ما فقط شش Module داخل یک Deployment ساخته‌ایم. استخراج Service نیازمند ADR، NFR، Team autonomy، Data و Operational evidence است.

### `internal` فقط Convention است

اگر Architecture Test نباشد، Developer می‌تواند Type عمومی داخل Subpackage را Import کند. Day 06 آن را enforce می‌کند.

### همه‌چیز Public در Base Package

هر Public Type در Base Package بخشی از Provided Interface است. Surface بزرگ Coupling را زیاد می‌کند.

### Named Interface برای هر Folder

Named Interface باید Consumer و Contract مشخص داشته باشد؛ نه اینکه Encapsulation را بی‌اثر کند.

### Dependency برای استفادهٔ دوباره از Entity

Reuse کد دلیل کافی برای وابستگی Domain نیست. Contract، Reference یا Translation را بررسی کن.

### Cycle را با Event پنهان‌کردن

اگر مدل و فرآیند ذاتاً دوری و مبهم است، عوض‌کردن Method call با Event نامفهوم مسئله را حل نمی‌کند. Ownership و Direction را دوباره تحلیل کن.

## 15. تمرین مستقل

[Day 05 Exercise — Module Skeleton](../exercises/day-05-module-skeleton.md) را اجرا کن. کد را خودت بنویس و Output ماژول‌ها و تصمیم Dependency را در Workbook ثبت کن.

## 16. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| شش Module بر اساس Direct Subpackage | ۲ |
| API/Internal boundary عمدی | ۲ |
| Named Interface محدود و معنادار | ۲ |
| Allowed dependencies مستدل و بدون Cycle | ۲ |
| Policy و Traceability به Context Map | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. استفاده از Open Module یا Import داخلی بدون ADR پذیرفته نیست.

## 17. آزمون خروج

پس از پایان کدنویسی، [Day 05 Exit Ticket](../quizzes/day-05-exit-ticket.md) را بدون مراجعه به درس پاسخ بده.

## 18. منابع اصلی

- [Spring Modulith Fundamentals 2.1.0](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- [ApplicationModule Javadoc 2.1.0](https://docs.spring.io/spring-modulith/docs/2.1.0/api/org/springframework/modulith/ApplicationModule.html)

Syntaxهای `allowedDependencies`، آرایهٔ خالی، Closed Module و Named Interface با مستند رسمی 2.1.0 تطبیق داده شده‌اند.
