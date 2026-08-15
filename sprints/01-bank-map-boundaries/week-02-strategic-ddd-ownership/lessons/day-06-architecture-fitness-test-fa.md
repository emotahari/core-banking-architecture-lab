# Day 06 — Architecture Fitness Test و Module Verification

- Day budget: 45 minutes — 10 review + 30 exercise + 5 exit ticket
- Output: automated module verification + one negative experiment
- Tool: Spring Modulith 2.1.0

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. Architecture Principle را به Fitness Function قابل اجرا تبدیل کنی.
2. `ApplicationModules.verify()` را در Build قرار بدهی.
3. سه گروه نقضی را که Spring Modulith بررسی می‌کند توضیح بدهی.
4. یک نقض Internal Access یا Cycle را عمداً ایجاد، مشاهده و اصلاح کنی.
5. محدودیت Verification را بشناسی و آن را با صحت دامینی اشتباه نگیری.
6. Scopeهای `@ApplicationModuleTest` را برای روزهای بعد انتخاب کنی.

## 2. از تصمیم معماری تا شاهد اجرایی

جملهٔ زیر Principle است:

> Moduleها نباید جزئیات داخلی یکدیگر را مصرف کنند.

اگر فقط در Wiki بماند، با اولین Deadline دور زده می‌شود. Fitness Function آن را به شرطی تبدیل می‌کند که Build بتواند نقضش را تشخیص دهد.

مدل ذهنی:

~~~text
architectural intent
      ↓ encode a measurable rule
fitness function
      ↓ run continuously
fast violation feedback
      ↓ repair or explicit ADR change
evolution with guardrails
~~~

Fitness Function باید:

- با Property مهم مرتبط باشد؛
- تا حد ممکن Objective و تکرارپذیر باشد؛
- در CI اجرا شود؛
- پیام شکست قابل‌فهم بدهد؛
- هزینهٔ نگهداری معقول داشته باشد؛
- با تغییر عمدی معماری، همراه ADR تغییر کند.

## 3. چه چیزی را Spring Modulith Verify می‌کند؟

طبق [مستند رسمی Verification](https://docs.spring.io/spring-modulith/reference/verification.html)، فراخوانی زیر ساختار را بررسی می‌کند:

```java
ApplicationModules.of(CoreBankingLabApplication.class).verify();
```

سه کنترل اصلی:

### 3.1 No Module Cycles

گراف Dependency میان Application Moduleها باید Directed Acyclic Graph باشد. اگر Lending به Deposits و Deposits به Lending وابسته شود، امکان Release/Refactor مستقل کاهش می‌یابد و Ownership معمولاً مبهم است.

Cycle همیشه با حذف یک Import تصادفی حل نمی‌شود. باید بپرسی:

- آیا Direction اشتباه است؟
- آیا Contract در Module نامناسب قرار دارد؟
- آیا یک Fact باید Event شود؟
- آیا Shared concept واقعاً Shared Kernel کوچک است؟
- آیا دو Module در واقع Cohesion بالایی دارند و Boundary غلط است؟

### 3.2 No Access to Internal Packages

Module دیگر فقط به API Base Package یا Named Interface صریح دسترسی دارد. Import از Subpackage داخلی نقض Encapsulation است، حتی اگر Type در Java `public` باشد.

### 3.3 Explicit Allowed Dependencies

اگر `allowedDependencies` تعریف شده باشد، Dependency خارج از فهرست رد می‌شود. این کنترل «چه کسی می‌تواند به چه Interface‌ای وابسته باشد» را قابل اجرا می‌کند.

یک Module با `allowedDependencies = {}` هیچ Dependency به Module دیگر را مجاز نمی‌کند. حذف Attribute یعنی این محدودیت صریح اعمال نمی‌شود؛ بنابراین برای Lab از Allowlist آگاهانه استفاده می‌کنیم.

## 4. تست پایه

فایل زیر را بساز:

~~~text
backend/banking-modulith/src/test/java/
└── com/example/corebankinglab/
    └── ModulithArchitectureTests.java
~~~

محتوا:

```java
package com.example.corebankinglab;

import org.junit.jupiter.api.Test;
import org.springframework.modulith.core.ApplicationModules;

class ModulithArchitectureTests {

    @Test
    void verifiesApplicationModuleBoundaries() {
        ApplicationModules
                .of(CoreBankingLabApplication.class)
                .verify();
    }
}
```

سپس:

~~~bash
cd backend/banking-modulith
mvn verify
~~~

این Test باید بخشی از `mvn verify` و CI باشد؛ اجرای دستی گهگاهی Fitness Function مستمر نیست.

## 5. Inspection قبل از Verification

گاهی Verification سبز است چون Moduleها اصلاً آن‌گونه که انتظار داشتی کشف نشده‌اند. مدل را چاپ کن:

```java
var modules = ApplicationModules.of(CoreBankingLabApplication.class);
modules.forEach(System.out::println);
modules.verify();
```

کنترل کن:

- دقیقاً Moduleهای مورد انتظار کشف شده‌اند.
- Base Package درست است.
- API Surface بیش از حد بزرگ نیست.
- Dependencyهای مستقیم با Policy هماهنگ‌اند.

تست سبز روی مدل کشف‌شدهٔ اشتباه، Evidence کافی نیست.

## 6. آزمایش منفی اجباری

Fitness Function را فقط در حالت سبز اعتماد نکن. باید نشان بدهی نقض موردنظر را واقعاً می‌گیرد.

### گزینهٔ A: Internal Package Access

1. یک Type موقت Public در `deposits.internal` بساز.
2. از `lending` آن را Import و Reference کن.
3. `mvn verify` را اجرا کن.
4. متن نقض را در Workbook ثبت کن.
5. Reference موقت و Type آزمایشی را حذف کن.
6. دوباره `mvn verify` را اجرا کن و نتیجهٔ سبز را ثبت کن.

این کد نقض‌کننده نباید Commit نهایی شود. فقط Evidence شکست و اصلاح در Submission می‌ماند.

### گزینهٔ B: Unauthorized Dependency

1. Moduleای با `allowedDependencies = {}` انتخاب کن.
2. به API Public یک Module دیگر Reference موقت بده.
3. شکست Allowlist را ثبت و سپس اصلاح کن.

### گزینهٔ C: Cycle

فقط اگر دو Dependency مجاز فعلی داری، یک Dependency معکوس موقت بساز و Cycle را مشاهده کن. برای دیدن Cycle، قواعد دیگر نباید زودتر همان Dependency را به دلیل متفاوت رد کنند؛ در غیر این صورت آزمایش مبهم می‌شود.

برای این هفته گزینهٔ A پیشنهاد می‌شود، چون علت شکست روشن‌تر است.

## 7. `verify()` در برابر `detectViolations()`

`verify()` در صورت نقض Exception می‌دهد و Test را Fail می‌کند. انتخاب استاندارد CI همین است.

`detectViolations()` مجموعهٔ نقض‌ها را برای پردازش بیشتر می‌دهد:

```java
var violations = ApplicationModules
        .of(CoreBankingLabApplication.class)
        .detectViolations();

violations.getMessages().forEach(System.out::println);
violations.throwIfPresent();
```

این مسیر برای مشاهده و پردازش فهرست نقض‌هاست، اما Build را همچنان Fail می‌کند. اگر در آینده از `filter(Predicate<Violation>)` برای Exception استفاده شد، Predicate باید فقط نقض‌های غیرمستثنا را باقی بگذارد. Filter کردن برای سبزکردن ظاهری Build ممنوع است، مگر اینکه:

- Debt دقیقاً شناسایی شده باشد؛
- Scope کوچک باشد؛
- Owner و Expiry date داشته باشد؛
- ADR و Issue اصلاح وجود داشته باشد.

نادیده‌گرفتن عمومی نقض، Fitness Function را نمایشی می‌کند.

## 8. Module Integration Test

`verify()` Structure را بررسی می‌کند. برای Behavior داخل یک Module، Spring Modulith ابزار `@ApplicationModuleTest` دارد.

طبق [Testing Reference](https://docs.spring.io/spring-modulith/reference/testing.html)، Modeها:

| Mode | Scope | کاربرد |
|---|---|---|
| `STANDALONE` | فقط Module جاری | Default؛ استقلال و Mock کردن Efferent Dependencyها |
| `DIRECT_DEPENDENCIES` | Module + Dependencyهای مستقیم | Integration محدود |
| `ALL_DEPENDENCIES` | Module + تمام Dependency tree | سناریوی گسترده‌تر، با هزینه و Coupling بیشتر |

نمونهٔ Skeleton:

```java
package com.example.corebankinglab.deposits;

import org.springframework.modulith.test.ApplicationModuleTest;

@ApplicationModuleTest
class DepositsModuleTests {
    // Behavioral tests will be added with the domain model.
}
```

اگر برای بالا آمدن یک Module دائماً `ALL_DEPENDENCIES` لازم است، احتمال High Coupling یا Boundary ضعیف را بررسی کن. واکنش اول نباید بزرگ‌کردن Test scope باشد؛ Dependency بیرونی را می‌توان در `STANDALONE` Mock کرد.

در Sprint 01، Architecture Verification اجباری و Module behavior test در حد Skeleton/Design است. Domain behavior از Sprint 02 اضافه می‌شود.

## 9. چه چیزی را این تست ثابت نمی‌کند؟

`ApplicationModules.verify()` نمی‌تواند ثابت کند:

- Bounded Contextها از نظر کسب‌وکار درست کشف شده‌اند.
- Owner داده و Decision درست است.
- Event نام و Semantic درست دارد.
- دو Module یک جدول مشترک را مستقیم Update نمی‌کنند.
- HTTP call runtime باعث Cycle یا Availability coupling نشده است.
- تراکنش، Idempotency، Retry یا Reconciliation صحیح است.
- Journal balanced است.
- NFRهای Latency و Availability برآورده شده‌اند.

به همین دلیل Architecture Evidence لایه‌ای است:

| Concern | Evidence |
|---|---|
| Strategic boundary | Domain/Context Map + expert review |
| Ownership | Ownership Matrix + scenario defense |
| Compile-time module rules | `ApplicationModules.verify()` |
| Module behavior | Unit + `@ApplicationModuleTest` |
| Runtime contracts | Contract/integration tests در Sprintهای بعد |
| Data ownership | Schema access rules + migration checks در Sprintهای بعد |
| Distributed failure | Failure tests + reconciliation evidence در Sprintهای بعد |

یک Test سبز همهٔ معماری را تأیید نمی‌کند؛ فقط Property تعریف‌شده را تأیید می‌کند.

## 10. Fitness Functionهای آینده

این هفته فقط Baseline است. در ادامه می‌توانیم قواعد زیر را اضافه کنیم:

- Domain code نباید به Spring/JPA وابسته باشد.
- Controller نباید Repository را مستقیم فراخوانی کند.
- Eventها باید Immutable و Versioned باشند.
- هیچ Service به Schema دیگری دسترسی نداشته باشد.
- Journal باید balanced باشد.
- Contract compatibility باید در CI کنترل شود.
- Dependency vulnerability و Secret scanning باید پاس شوند.

هر Rule باید به Risk معماری واقعی وصل باشد؛ زیادکردن Test بدون Intent روشن، Noise تولید می‌کند.

## 11. خطاهای رایج

### Test سبز، پس Boundary درست است

ابزار فقط قواعد ساختاری را روی Package layout فعلی اجرا می‌کند. Domain review همچنان لازم است.

### نقض را با Public کردن Package حل کنیم

Public/Named کردن Type باید Contract decision باشد؛ نه راه فرار از Test.

### Module را Open کنیم

Open Module برای Migration Legacy مفید است، ولی در کد جدید Encapsulation را تضعیف می‌کند.

### Cycle را با `common` بشکنیم

انتقال همهٔ Typeها به `common` Cycle ظاهری را حذف و مدل مشترک عظیم می‌سازد. Ownership و Direction را اصلاح کن.

### فقط Happy Path Test

بدون آزمایش منفی نمی‌دانی Fitness Function واقعاً نقض را می‌گیرد یا Module detection ناقص است.

### Filter دائمی نقض‌ها

Exception list بدون Owner و Expiry به معماری واقعی تبدیل می‌شود.

## 12. تمرین مستقل

[Day 06 Exercise — Module Verification](../exercises/day-06-module-verification.md) را انجام بده. خروجی قرمز آزمایش منفی و خروجی سبز پس از اصلاح هر دو لازم‌اند.

## 13. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| Architecture test در `mvn verify` | ۲ |
| شش Module درست کشف شده | ۲ |
| Negative experiment معتبر | ۲ |
| Repair و نتیجهٔ سبز | ۲ |
| بیان محدودیت Test و Evidenceهای مکمل | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. فقط Screenshot سبز بدون Negative evidence حداکثر ۶ می‌گیرد.

## 14. آزمون خروج

درس را ببند و [Day 06 Exit Ticket](../quizzes/day-06-exit-ticket.md) را پاسخ بده.

## 15. منابع اصلی

- [Spring Modulith — Verification](https://docs.spring.io/spring-modulith/reference/verification.html)
- [Spring Modulith — Module Testing](https://docs.spring.io/spring-modulith/reference/testing.html)

APIها و سه Rule اصلی Verification با مستند رسمی نسخهٔ 2.1.0 تطبیق داده شده‌اند.
