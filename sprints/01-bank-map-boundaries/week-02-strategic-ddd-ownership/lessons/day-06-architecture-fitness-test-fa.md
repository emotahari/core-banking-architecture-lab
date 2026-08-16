<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 06</span> — <span dir="ltr">Architecture Fitness Test</span> و <span dir="ltr">Module Verification</span>

- <span dir="ltr">Day budget: 45 minutes</span> — <span dir="ltr">10 review</span> + <span dir="ltr">30 exercise</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output: automated module verification</span> + <span dir="ltr">one negative experiment</span>
- <span dir="ltr">Tool: Spring Modulith 2.1.0</span>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <span dir="ltr">Architecture Principle</span> را به <span dir="ltr">Fitness Function</span> قابل اجرا تبدیل کنی.
2. <span dir="ltr">`ApplicationModules.verify()`</span> را در <span dir="ltr">Build</span> قرار بدهی.
3. سه گروه نقضی را که <span dir="ltr">Spring Modulith</span> بررسی می‌کند توضیح بدهی.
4. یک نقض <span dir="ltr">Internal Access</span> یا <span dir="ltr">Cycle</span> را عمداً ایجاد، مشاهده و اصلاح کنی.
5. محدودیت <span dir="ltr">Verification</span> را بشناسی و آن را با صحت دامینی اشتباه نگیری.
6. <span dir="ltr">Scope</span>های <span dir="ltr">`@ApplicationModuleTest`</span> را برای روزهای بعد انتخاب کنی.

## 2. از تصمیم معماری تا شاهد اجرایی

جملهٔ زیر <span dir="ltr">Principle</span> است:

> <span dir="ltr">Module</span>ها نباید جزئیات داخلی یکدیگر را مصرف کنند.

اگر فقط در <span dir="ltr">Wiki</span> بماند، با اولین <span dir="ltr">Deadline</span> دور زده می‌شود. <span dir="ltr">Fitness Function</span> آن را به شرطی تبدیل می‌کند که <span dir="ltr">Build</span> بتواند نقضش را تشخیص دهد.

مدل ذهنی:


</div>

<div dir="ltr" align="left">

~~~text
architectural intent
      ↓ encode a measurable rule
fitness function
      ↓ run continuously
fast violation feedback
      ↓ repair or explicit ADR change
evolution with guardrails
~~~

</div>

<div dir="rtl" align="right">


<span dir="ltr">Fitness Function</span> باید:

- با <span dir="ltr">Property</span> مهم مرتبط باشد؛
- تا حد ممکن <span dir="ltr">Objective</span> و تکرارپذیر باشد؛
- در <span dir="ltr">CI</span> اجرا شود؛
- پیام شکست قابل‌فهم بدهد؛
- هزینهٔ نگهداری معقول داشته باشد؛
- با تغییر عمدی معماری، همراه <span dir="ltr">ADR</span> تغییر کند.

## 3. چه چیزی را <span dir="ltr">Spring Modulith Verify</span> می‌کند؟

طبق [مستند رسمی <span dir="ltr">Verification</span>](https://docs.spring.io/spring-modulith/reference/verification.html)، فراخوانی زیر ساختار را بررسی می‌کند:


</div>

<div dir="ltr" align="left">

```java
ApplicationModules.of(CoreBankingLabApplication.class).verify();
```

</div>

<div dir="rtl" align="right">


سه کنترل اصلی:

### <span dir="ltr">3.1 No Module Cycles</span>

گراف <span dir="ltr">Dependency</span> میان <span dir="ltr">Application Module</span>ها باید <span dir="ltr">Directed Acyclic Graph</span> باشد. اگر <span dir="ltr">Lending</span> به <span dir="ltr">Deposits</span> و <span dir="ltr">Deposits</span> به <span dir="ltr">Lending</span> وابسته شود، امکان <span dir="ltr">Release/Refactor</span> مستقل کاهش می‌یابد و <span dir="ltr">Ownership</span> معمولاً مبهم است.

<span dir="ltr">Cycle</span> همیشه با حذف یک <span dir="ltr">Import</span> تصادفی حل نمی‌شود. باید بپرسی:

- آیا <span dir="ltr">Direction</span> اشتباه است؟
- آیا <span dir="ltr">Contract</span> در <span dir="ltr">Module</span> نامناسب قرار دارد؟
- آیا یک <span dir="ltr">Fact</span> باید <span dir="ltr">Event</span> شود؟
- آیا <span dir="ltr">Shared concept</span> واقعاً <span dir="ltr">Shared Kernel</span> کوچک است؟
- آیا دو <span dir="ltr">Module</span> در واقع <span dir="ltr">Cohesion</span> بالایی دارند و <span dir="ltr">Boundary</span> غلط است؟

### <span dir="ltr">3.2 No Access to Internal Packages</span>

<span dir="ltr">Module</span> دیگر فقط به <span dir="ltr">API Base Package</span> یا <span dir="ltr">Named Interface</span> صریح دسترسی دارد. <span dir="ltr">Import</span> از <span dir="ltr">Subpackage</span> داخلی نقض <span dir="ltr">Encapsulation</span> است، حتی اگر <span dir="ltr">Type</span> در <span dir="ltr">Java</span> <span dir="ltr">`public`</span> باشد.

### <span dir="ltr">3.3 Explicit Allowed Dependencies</span>

اگر <span dir="ltr">`allowedDependencies`</span> تعریف شده باشد، <span dir="ltr">Dependency</span> خارج از فهرست رد می‌شود. این کنترل «چه کسی می‌تواند به چه <span dir="ltr">Interface</span>‌ای وابسته باشد» را قابل اجرا می‌کند.

یک <span dir="ltr">Module</span> با <span dir="ltr">`allowedDependencies = {}`</span> هیچ <span dir="ltr">Dependency</span> به <span dir="ltr">Module</span> دیگر را مجاز نمی‌کند. حذف <span dir="ltr">Attribute</span> یعنی این محدودیت صریح اعمال نمی‌شود؛ بنابراین برای <span dir="ltr">Lab</span> از <span dir="ltr">Allowlist</span> آگاهانه استفاده می‌کنیم.

## 4. تست پایه

فایل زیر را بساز:


</div>

<div dir="ltr" align="left">

~~~text
backend/banking-modulith/src/test/java/
└── com/example/corebankinglab/
    └── ModulithArchitectureTests.java
~~~

</div>

<div dir="rtl" align="right">


محتوا:


</div>

<div dir="ltr" align="left">

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

</div>

<div dir="rtl" align="right">


سپس:


</div>

<div dir="ltr" align="left">

~~~bash
cd backend/banking-modulith
mvn verify
~~~

</div>

<div dir="rtl" align="right">


این <span dir="ltr">Test</span> باید بخشی از <span dir="ltr">`mvn verify`</span> و <span dir="ltr">CI</span> باشد؛ اجرای دستی گهگاهی <span dir="ltr">Fitness Function</span> مستمر نیست.

## <span dir="ltr">5. Inspection</span> قبل از <span dir="ltr">Verification</span>

گاهی <span dir="ltr">Verification</span> سبز است چون <span dir="ltr">Module</span>ها اصلاً آن‌گونه که انتظار داشتی کشف نشده‌اند. مدل را چاپ کن:


</div>

<div dir="ltr" align="left">

```java
var modules = ApplicationModules.of(CoreBankingLabApplication.class);
modules.forEach(System.out::println);
modules.verify();
```

</div>

<div dir="rtl" align="right">


کنترل کن:

- دقیقاً <span dir="ltr">Module</span>های مورد انتظار کشف شده‌اند.
- <span dir="ltr">Base Package</span> درست است.
- <span dir="ltr">API Surface</span> بیش از حد بزرگ نیست.
- <span dir="ltr">Dependency</span>های مستقیم با <span dir="ltr">Policy</span> هماهنگ‌اند.

تست سبز روی مدل کشف‌شدهٔ اشتباه، <span dir="ltr">Evidence</span> کافی نیست.

## 6. آزمایش منفی اجباری

<span dir="ltr">Fitness Function</span> را فقط در حالت سبز اعتماد نکن. باید نشان بدهی نقض موردنظر را واقعاً می‌گیرد.

### گزینهٔ <span dir="ltr">A: Internal Package Access</span>

1. یک <span dir="ltr">Type</span> موقت <span dir="ltr">Public</span> در <span dir="ltr">`deposits.internal`</span> بساز.
2. از <span dir="ltr">`lending`</span> آن را <span dir="ltr">Import</span> و <span dir="ltr">Reference</span> کن.
3. <span dir="ltr">`mvn verify`</span> را اجرا کن.
4. متن نقض را در <span dir="ltr">Workbook</span> ثبت کن.
5. <span dir="ltr">Reference</span> موقت و <span dir="ltr">Type</span> آزمایشی را حذف کن.
6. دوباره <span dir="ltr">`mvn verify`</span> را اجرا کن و نتیجهٔ سبز را ثبت کن.

این کد نقض‌کننده نباید <span dir="ltr">Commit</span> نهایی شود. فقط <span dir="ltr">Evidence</span> شکست و اصلاح در <span dir="ltr">Submission</span> می‌ماند.

### گزینهٔ <span dir="ltr">B: Unauthorized Dependency</span>

1. <span dir="ltr">Module</span>ای با <span dir="ltr">`allowedDependencies = {}`</span> انتخاب کن.
2. به <span dir="ltr">API Public</span> یک <span dir="ltr">Module</span> دیگر <span dir="ltr">Reference</span> موقت بده.
3. شکست <span dir="ltr">Allowlist</span> را ثبت و سپس اصلاح کن.

### گزینهٔ <span dir="ltr">C: Cycle</span>

فقط اگر دو <span dir="ltr">Dependency</span> مجاز فعلی داری، یک <span dir="ltr">Dependency</span> معکوس موقت بساز و <span dir="ltr">Cycle</span> را مشاهده کن. برای دیدن <span dir="ltr">Cycle</span>، قواعد دیگر نباید زودتر همان <span dir="ltr">Dependency</span> را به دلیل متفاوت رد کنند؛ در غیر این صورت آزمایش مبهم می‌شود.

برای این هفته گزینهٔ A پیشنهاد می‌شود، چون علت شکست روشن‌تر است.

## 7. <span dir="ltr">`verify()`</span> در برابر <span dir="ltr">`detectViolations()`</span>

<span dir="ltr">`verify()`</span> در صورت نقض <span dir="ltr">Exception</span> می‌دهد و <span dir="ltr">Test</span> را <span dir="ltr">Fail</span> می‌کند. انتخاب استاندارد <span dir="ltr">CI</span> همین است.

<span dir="ltr">`detectViolations()`</span> مجموعهٔ نقض‌ها را برای پردازش بیشتر می‌دهد:


</div>

<div dir="ltr" align="left">

```java
var violations = ApplicationModules
        .of(CoreBankingLabApplication.class)
        .detectViolations();

violations.getMessages().forEach(System.out::println);
violations.throwIfPresent();
```

</div>

<div dir="rtl" align="right">


این مسیر برای مشاهده و پردازش فهرست نقض‌هاست، اما <span dir="ltr">Build</span> را همچنان <span dir="ltr">Fail</span> می‌کند. اگر در آینده از <span dir="ltr">`filter(Predicate<Violation>)`</span> برای <span dir="ltr">Exception</span> استفاده شد، <span dir="ltr">Predicate</span> باید فقط نقض‌های غیرمستثنا را باقی بگذارد. <span dir="ltr">Filter</span> کردن برای سبزکردن ظاهری <span dir="ltr">Build</span> ممنوع است، مگر اینکه:

- <span dir="ltr">Debt</span> دقیقاً شناسایی شده باشد؛
- <span dir="ltr">Scope</span> کوچک باشد؛
- <span dir="ltr">Owner</span> و <span dir="ltr">Expiry date</span> داشته باشد؛
- <span dir="ltr">ADR</span> و <span dir="ltr">Issue</span> اصلاح وجود داشته باشد.

نادیده‌گرفتن عمومی نقض، <span dir="ltr">Fitness Function</span> را نمایشی می‌کند.

## <span dir="ltr">8. Module Integration Test</span>

<span dir="ltr">`verify()`</span> <span dir="ltr">Structure</span> را بررسی می‌کند. برای <span dir="ltr">Behavior</span> داخل یک <span dir="ltr">Module</span>، <span dir="ltr">Spring Modulith</span> ابزار <span dir="ltr">`@ApplicationModuleTest`</span> دارد.

طبق [<span dir="ltr">Testing Reference</span>](https://docs.spring.io/spring-modulith/reference/testing.html)، <span dir="ltr">Mode</span>ها:

| <span dir="ltr">Mode</span> | <span dir="ltr">Scope</span> | کاربرد |
|---|---|---|
| <span dir="ltr">`STANDALONE`</span> | فقط <span dir="ltr">Module</span> جاری | <span dir="ltr">Default</span>؛ استقلال و <span dir="ltr">Mock</span> کردن <span dir="ltr">Efferent Dependency</span>ها |
| <span dir="ltr">`DIRECT_DEPENDENCIES`</span> | <span dir="ltr">Module</span> + <span dir="ltr">Dependency</span>های مستقیم | <span dir="ltr">Integration</span> محدود |
| <span dir="ltr">`ALL_DEPENDENCIES`</span> | <span dir="ltr">Module</span> + تمام <span dir="ltr">Dependency tree</span> | سناریوی گسترده‌تر، با هزینه و <span dir="ltr">Coupling</span> بیشتر |

نمونهٔ <span dir="ltr">Skeleton:</span>


</div>

<div dir="ltr" align="left">

```java
package com.example.corebankinglab.deposits;

import org.springframework.modulith.test.ApplicationModuleTest;

@ApplicationModuleTest
class DepositsModuleTests {
    // Behavioral tests will be added with the domain model.
}
```

</div>

<div dir="rtl" align="right">


اگر برای بالا آمدن یک <span dir="ltr">Module</span> دائماً <span dir="ltr">`ALL_DEPENDENCIES`</span> لازم است، احتمال <span dir="ltr">High Coupling</span> یا <span dir="ltr">Boundary</span> ضعیف را بررسی کن. واکنش اول نباید بزرگ‌کردن <span dir="ltr">Test scope</span> باشد؛ <span dir="ltr">Dependency</span> بیرونی را می‌توان در <span dir="ltr">`STANDALONE`</span> <span dir="ltr">Mock</span> کرد.

در <span dir="ltr">Sprint 01</span>، <span dir="ltr">Architecture Verification</span> اجباری و <span dir="ltr">Module behavior test</span> در حد <span dir="ltr">Skeleton/Design</span> است. <span dir="ltr">Domain behavior</span> از <span dir="ltr">Sprint 02</span> اضافه می‌شود.

## 9. چه چیزی را این تست ثابت نمی‌کند؟

<span dir="ltr">`ApplicationModules.verify()`</span> نمی‌تواند ثابت کند:

- <span dir="ltr">Bounded Context</span>ها از نظر کسب‌وکار درست کشف شده‌اند.
- <span dir="ltr">Owner</span> داده و <span dir="ltr">Decision</span> درست است.
- <span dir="ltr">Event</span> نام و <span dir="ltr">Semantic</span> درست دارد.
- دو <span dir="ltr">Module</span> یک جدول مشترک را مستقیم <span dir="ltr">Update</span> نمی‌کنند.
- <span dir="ltr">HTTP call runtime</span> باعث <span dir="ltr">Cycle</span> یا <span dir="ltr">Availability coupling</span> نشده است.
- تراکنش، <span dir="ltr">Idempotency</span>، <span dir="ltr">Retry</span> یا <span dir="ltr">Reconciliation</span> صحیح است.
- <span dir="ltr">Journal balanced</span> است.
- <span dir="ltr">NFR</span>های <span dir="ltr">Latency</span> و <span dir="ltr">Availability</span> برآورده شده‌اند.

به همین دلیل <span dir="ltr">Architecture Evidence</span> لایه‌ای است:

| <span dir="ltr">Concern</span> | <span dir="ltr">Evidence</span> |
|---|---|
| <span dir="ltr">Strategic boundary</span> | <span dir="ltr">Domain/Context Map</span> + <span dir="ltr">expert review</span> |
| <span dir="ltr">Ownership</span> | <span dir="ltr">Ownership Matrix</span> + <span dir="ltr">scenario defense</span> |
| <span dir="ltr">Compile-time module rules</span> | <span dir="ltr">`ApplicationModules.verify()`</span> |
| <span dir="ltr">Module behavior</span> | <span dir="ltr">Unit</span> + <span dir="ltr">`@ApplicationModuleTest`</span> |
| <span dir="ltr">Runtime contracts</span> | <span dir="ltr">Contract/integration tests</span> در <span dir="ltr">Sprint</span>های بعد |
| <span dir="ltr">Data ownership</span> | <span dir="ltr">Schema access rules</span> + <span dir="ltr">migration checks</span> در <span dir="ltr">Sprint</span>های بعد |
| <span dir="ltr">Distributed failure</span> | <span dir="ltr">Failure tests</span> + <span dir="ltr">reconciliation evidence</span> در <span dir="ltr">Sprint</span>های بعد |

یک <span dir="ltr">Test</span> سبز همهٔ معماری را تأیید نمی‌کند؛ فقط <span dir="ltr">Property</span> تعریف‌شده را تأیید می‌کند.

## <span dir="ltr">10. Fitness Function</span>های آینده

این هفته فقط <span dir="ltr">Baseline</span> است. در ادامه می‌توانیم قواعد زیر را اضافه کنیم:

- <span dir="ltr">Domain code</span> نباید به <span dir="ltr">Spring/JPA</span> وابسته باشد.
- <span dir="ltr">Controller</span> نباید <span dir="ltr">Repository</span> را مستقیم فراخوانی کند.
- <span dir="ltr">Event</span>ها باید <span dir="ltr">Immutable</span> و <span dir="ltr">Versioned</span> باشند.
- هیچ <span dir="ltr">Service</span> به <span dir="ltr">Schema</span> دیگری دسترسی نداشته باشد.
- <span dir="ltr">Journal</span> باید <span dir="ltr">balanced</span> باشد.
- <span dir="ltr">Contract compatibility</span> باید در <span dir="ltr">CI</span> کنترل شود.
- <span dir="ltr">Dependency vulnerability</span> و <span dir="ltr">Secret scanning</span> باید پاس شوند.

هر <span dir="ltr">Rule</span> باید به <span dir="ltr">Risk</span> معماری واقعی وصل باشد؛ زیادکردن <span dir="ltr">Test</span> بدون <span dir="ltr">Intent</span> روشن، <span dir="ltr">Noise</span> تولید می‌کند.

## 11. خطاهای رایج

### <span dir="ltr">Test</span> سبز، پس <span dir="ltr">Boundary</span> درست است

ابزار فقط قواعد ساختاری را روی <span dir="ltr">Package layout</span> فعلی اجرا می‌کند. <span dir="ltr">Domain review</span> همچنان لازم است.

### نقض را با <span dir="ltr">Public</span> کردن <span dir="ltr">Package</span> حل کنیم

<span dir="ltr">Public/Named</span> کردن <span dir="ltr">Type</span> باید <span dir="ltr">Contract decision</span> باشد؛ نه راه فرار از <span dir="ltr">Test.</span>

### <span dir="ltr">Module</span> را <span dir="ltr">Open</span> کنیم

<span dir="ltr">Open Module</span> برای <span dir="ltr">Migration Legacy</span> مفید است، ولی در کد جدید <span dir="ltr">Encapsulation</span> را تضعیف می‌کند.

### <span dir="ltr">Cycle</span> را با <span dir="ltr">`common`</span> بشکنیم

انتقال همهٔ <span dir="ltr">Type</span>ها به <span dir="ltr">`common`</span> <span dir="ltr">Cycle</span> ظاهری را حذف و مدل مشترک عظیم می‌سازد. <span dir="ltr">Ownership</span> و <span dir="ltr">Direction</span> را اصلاح کن.

### فقط <span dir="ltr">Happy Path Test</span>

بدون آزمایش منفی نمی‌دانی <span dir="ltr">Fitness Function</span> واقعاً نقض را می‌گیرد یا <span dir="ltr">Module detection</span> ناقص است.

### <span dir="ltr">Filter</span> دائمی نقض‌ها

<span dir="ltr">Exception list</span> بدون <span dir="ltr">Owner</span> و <span dir="ltr">Expiry</span> به معماری واقعی تبدیل می‌شود.

## 12. تمرین مستقل

[<span dir="ltr">Day 06 Exercise</span> — <span dir="ltr">Module Verification</span>](../exercises/day-06-module-verification.md) را انجام بده. خروجی قرمز آزمایش منفی و خروجی سبز پس از اصلاح هر دو لازم‌اند.

## 13. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| <span dir="ltr">Architecture test</span> در <span dir="ltr">`mvn verify`</span> | ۲ |
| شش <span dir="ltr">Module</span> درست کشف شده | ۲ |
| <span dir="ltr">Negative experiment</span> معتبر | ۲ |
| <span dir="ltr">Repair</span> و نتیجهٔ سبز | ۲ |
| بیان محدودیت <span dir="ltr">Test</span> و <span dir="ltr">Evidence</span>های مکمل | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. فقط <span dir="ltr">Screenshot</span> سبز بدون <span dir="ltr">Negative evidence</span> حداکثر ۶ می‌گیرد.

## 14. آزمون خروج

درس را ببند و [<span dir="ltr">Day 06 Exit Ticket</span>](../quizzes/day-06-exit-ticket.md) را پاسخ بده.

## 15. منابع اصلی

- [<span dir="ltr">Spring Modulith</span> — <span dir="ltr">Verification</span>](https://docs.spring.io/spring-modulith/reference/verification.html)
- [<span dir="ltr">Spring Modulith</span> — <span dir="ltr">Module Testing</span>](https://docs.spring.io/spring-modulith/reference/testing.html)

<span dir="ltr">API</span>ها و سه <span dir="ltr">Rule</span> اصلی <span dir="ltr">Verification</span> با مستند رسمی نسخهٔ 2.1.0 تطبیق داده شده‌اند.

</div>
