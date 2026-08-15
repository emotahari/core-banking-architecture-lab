<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 06</bdi> — <bdi dir="ltr">Architecture Fitness Test</bdi> و <bdi dir="ltr">Module Verification</bdi>

- <bdi dir="ltr">Day budget: 45 minutes</bdi> — <bdi dir="ltr">10 review</bdi> + <bdi dir="ltr">30 exercise</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output: automated module verification</bdi> + <bdi dir="ltr">one negative experiment</bdi>
- <bdi dir="ltr">Tool: Spring Modulith 2.1.0</bdi>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. <bdi dir="ltr">Architecture Principle</bdi> را به <bdi dir="ltr">Fitness Function</bdi> قابل اجرا تبدیل کنی.
2. <bdi dir="ltr">`ApplicationModules.verify()`</bdi> را در <bdi dir="ltr">Build</bdi> قرار بدهی.
3. سه گروه نقضی را که <bdi dir="ltr">Spring Modulith</bdi> بررسی می‌کند توضیح بدهی.
4. یک نقض <bdi dir="ltr">Internal Access</bdi> یا <bdi dir="ltr">Cycle</bdi> را عمداً ایجاد، مشاهده و اصلاح کنی.
5. محدودیت <bdi dir="ltr">Verification</bdi> را بشناسی و آن را با صحت دامینی اشتباه نگیری.
6. <bdi dir="ltr">Scope</bdi>های <bdi dir="ltr">`@ApplicationModuleTest`</bdi> را برای روزهای بعد انتخاب کنی.

## 2. از تصمیم معماری تا شاهد اجرایی

جملهٔ زیر <bdi dir="ltr">Principle</bdi> است:

> <bdi dir="ltr">Module</bdi>ها نباید جزئیات داخلی یکدیگر را مصرف کنند.

اگر فقط در <bdi dir="ltr">Wiki</bdi> بماند، با اولین <bdi dir="ltr">Deadline</bdi> دور زده می‌شود. <bdi dir="ltr">Fitness Function</bdi> آن را به شرطی تبدیل می‌کند که <bdi dir="ltr">Build</bdi> بتواند نقضش را تشخیص دهد.

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


<bdi dir="ltr">Fitness Function</bdi> باید:

- با <bdi dir="ltr">Property</bdi> مهم مرتبط باشد؛
- تا حد ممکن <bdi dir="ltr">Objective</bdi> و تکرارپذیر باشد؛
- در <bdi dir="ltr">CI</bdi> اجرا شود؛
- پیام شکست قابل‌فهم بدهد؛
- هزینهٔ نگهداری معقول داشته باشد؛
- با تغییر عمدی معماری، همراه <bdi dir="ltr">ADR</bdi> تغییر کند.

## 3. چه چیزی را <bdi dir="ltr">Spring Modulith Verify</bdi> می‌کند؟

طبق [مستند رسمی <bdi dir="ltr">Verification</bdi>](https://docs.spring.io/spring-modulith/reference/verification.html)، فراخوانی زیر ساختار را بررسی می‌کند:


</div>

<div dir="ltr" align="left">

```java
ApplicationModules.of(CoreBankingLabApplication.class).verify();
```

</div>

<div dir="rtl" align="right">


سه کنترل اصلی:

### <bdi dir="ltr">3.1 No Module Cycles</bdi>

گراف <bdi dir="ltr">Dependency</bdi> میان <bdi dir="ltr">Application Module</bdi>ها باید <bdi dir="ltr">Directed Acyclic Graph</bdi> باشد. اگر <bdi dir="ltr">Lending</bdi> به <bdi dir="ltr">Deposits</bdi> و <bdi dir="ltr">Deposits</bdi> به <bdi dir="ltr">Lending</bdi> وابسته شود، امکان <bdi dir="ltr">Release/Refactor</bdi> مستقل کاهش می‌یابد و <bdi dir="ltr">Ownership</bdi> معمولاً مبهم است.

<bdi dir="ltr">Cycle</bdi> همیشه با حذف یک <bdi dir="ltr">Import</bdi> تصادفی حل نمی‌شود. باید بپرسی:

- آیا <bdi dir="ltr">Direction</bdi> اشتباه است؟
- آیا <bdi dir="ltr">Contract</bdi> در <bdi dir="ltr">Module</bdi> نامناسب قرار دارد؟
- آیا یک <bdi dir="ltr">Fact</bdi> باید <bdi dir="ltr">Event</bdi> شود؟
- آیا <bdi dir="ltr">Shared concept</bdi> واقعاً <bdi dir="ltr">Shared Kernel</bdi> کوچک است؟
- آیا دو <bdi dir="ltr">Module</bdi> در واقع <bdi dir="ltr">Cohesion</bdi> بالایی دارند و <bdi dir="ltr">Boundary</bdi> غلط است؟

### <bdi dir="ltr">3.2 No Access to Internal Packages</bdi>

<bdi dir="ltr">Module</bdi> دیگر فقط به <bdi dir="ltr">API Base Package</bdi> یا <bdi dir="ltr">Named Interface</bdi> صریح دسترسی دارد. <bdi dir="ltr">Import</bdi> از <bdi dir="ltr">Subpackage</bdi> داخلی نقض <bdi dir="ltr">Encapsulation</bdi> است، حتی اگر <bdi dir="ltr">Type</bdi> در <bdi dir="ltr">Java</bdi> <bdi dir="ltr">`public`</bdi> باشد.

### <bdi dir="ltr">3.3 Explicit Allowed Dependencies</bdi>

اگر <bdi dir="ltr">`allowedDependencies`</bdi> تعریف شده باشد، <bdi dir="ltr">Dependency</bdi> خارج از فهرست رد می‌شود. این کنترل «چه کسی می‌تواند به چه <bdi dir="ltr">Interface</bdi>‌ای وابسته باشد» را قابل اجرا می‌کند.

یک <bdi dir="ltr">Module</bdi> با <bdi dir="ltr">`allowedDependencies = {}`</bdi> هیچ <bdi dir="ltr">Dependency</bdi> به <bdi dir="ltr">Module</bdi> دیگر را مجاز نمی‌کند. حذف <bdi dir="ltr">Attribute</bdi> یعنی این محدودیت صریح اعمال نمی‌شود؛ بنابراین برای <bdi dir="ltr">Lab</bdi> از <bdi dir="ltr">Allowlist</bdi> آگاهانه استفاده می‌کنیم.

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


این <bdi dir="ltr">Test</bdi> باید بخشی از <bdi dir="ltr">`mvn verify`</bdi> و <bdi dir="ltr">CI</bdi> باشد؛ اجرای دستی گهگاهی <bdi dir="ltr">Fitness Function</bdi> مستمر نیست.

## <bdi dir="ltr">5. Inspection</bdi> قبل از <bdi dir="ltr">Verification</bdi>

گاهی <bdi dir="ltr">Verification</bdi> سبز است چون <bdi dir="ltr">Module</bdi>ها اصلاً آن‌گونه که انتظار داشتی کشف نشده‌اند. مدل را چاپ کن:


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

- دقیقاً <bdi dir="ltr">Module</bdi>های مورد انتظار کشف شده‌اند.
- <bdi dir="ltr">Base Package</bdi> درست است.
- <bdi dir="ltr">API Surface</bdi> بیش از حد بزرگ نیست.
- <bdi dir="ltr">Dependency</bdi>های مستقیم با <bdi dir="ltr">Policy</bdi> هماهنگ‌اند.

تست سبز روی مدل کشف‌شدهٔ اشتباه، <bdi dir="ltr">Evidence</bdi> کافی نیست.

## 6. آزمایش منفی اجباری

<bdi dir="ltr">Fitness Function</bdi> را فقط در حالت سبز اعتماد نکن. باید نشان بدهی نقض موردنظر را واقعاً می‌گیرد.

### گزینهٔ <bdi dir="ltr">A: Internal Package Access</bdi>

1. یک <bdi dir="ltr">Type</bdi> موقت <bdi dir="ltr">Public</bdi> در <bdi dir="ltr">`deposits.internal`</bdi> بساز.
2. از <bdi dir="ltr">`lending`</bdi> آن را <bdi dir="ltr">Import</bdi> و <bdi dir="ltr">Reference</bdi> کن.
3. <bdi dir="ltr">`mvn verify`</bdi> را اجرا کن.
4. متن نقض را در <bdi dir="ltr">Workbook</bdi> ثبت کن.
5. <bdi dir="ltr">Reference</bdi> موقت و <bdi dir="ltr">Type</bdi> آزمایشی را حذف کن.
6. دوباره <bdi dir="ltr">`mvn verify`</bdi> را اجرا کن و نتیجهٔ سبز را ثبت کن.

این کد نقض‌کننده نباید <bdi dir="ltr">Commit</bdi> نهایی شود. فقط <bdi dir="ltr">Evidence</bdi> شکست و اصلاح در <bdi dir="ltr">Submission</bdi> می‌ماند.

### گزینهٔ <bdi dir="ltr">B: Unauthorized Dependency</bdi>

1. <bdi dir="ltr">Module</bdi>ای با <bdi dir="ltr">`allowedDependencies = {}`</bdi> انتخاب کن.
2. به <bdi dir="ltr">API Public</bdi> یک <bdi dir="ltr">Module</bdi> دیگر <bdi dir="ltr">Reference</bdi> موقت بده.
3. شکست <bdi dir="ltr">Allowlist</bdi> را ثبت و سپس اصلاح کن.

### گزینهٔ <bdi dir="ltr">C: Cycle</bdi>

فقط اگر دو <bdi dir="ltr">Dependency</bdi> مجاز فعلی داری، یک <bdi dir="ltr">Dependency</bdi> معکوس موقت بساز و <bdi dir="ltr">Cycle</bdi> را مشاهده کن. برای دیدن <bdi dir="ltr">Cycle</bdi>، قواعد دیگر نباید زودتر همان <bdi dir="ltr">Dependency</bdi> را به دلیل متفاوت رد کنند؛ در غیر این صورت آزمایش مبهم می‌شود.

برای این هفته گزینهٔ A پیشنهاد می‌شود، چون علت شکست روشن‌تر است.

## 7. <bdi dir="ltr">`verify()`</bdi> در برابر <bdi dir="ltr">`detectViolations()`</bdi>

<bdi dir="ltr">`verify()`</bdi> در صورت نقض <bdi dir="ltr">Exception</bdi> می‌دهد و <bdi dir="ltr">Test</bdi> را <bdi dir="ltr">Fail</bdi> می‌کند. انتخاب استاندارد <bdi dir="ltr">CI</bdi> همین است.

<bdi dir="ltr">`detectViolations()`</bdi> مجموعهٔ نقض‌ها را برای پردازش بیشتر می‌دهد:


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


این مسیر برای مشاهده و پردازش فهرست نقض‌هاست، اما <bdi dir="ltr">Build</bdi> را همچنان <bdi dir="ltr">Fail</bdi> می‌کند. اگر در آینده از <bdi dir="ltr">`filter(Predicate<Violation>)`</bdi> برای <bdi dir="ltr">Exception</bdi> استفاده شد، <bdi dir="ltr">Predicate</bdi> باید فقط نقض‌های غیرمستثنا را باقی بگذارد. <bdi dir="ltr">Filter</bdi> کردن برای سبزکردن ظاهری <bdi dir="ltr">Build</bdi> ممنوع است، مگر اینکه:

- <bdi dir="ltr">Debt</bdi> دقیقاً شناسایی شده باشد؛
- <bdi dir="ltr">Scope</bdi> کوچک باشد؛
- <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">Expiry date</bdi> داشته باشد؛
- <bdi dir="ltr">ADR</bdi> و <bdi dir="ltr">Issue</bdi> اصلاح وجود داشته باشد.

نادیده‌گرفتن عمومی نقض، <bdi dir="ltr">Fitness Function</bdi> را نمایشی می‌کند.

## <bdi dir="ltr">8. Module Integration Test</bdi>

<bdi dir="ltr">`verify()`</bdi> <bdi dir="ltr">Structure</bdi> را بررسی می‌کند. برای <bdi dir="ltr">Behavior</bdi> داخل یک <bdi dir="ltr">Module</bdi>، <bdi dir="ltr">Spring Modulith</bdi> ابزار <bdi dir="ltr">`@ApplicationModuleTest`</bdi> دارد.

طبق [<bdi dir="ltr">Testing Reference</bdi>](https://docs.spring.io/spring-modulith/reference/testing.html)، <bdi dir="ltr">Mode</bdi>ها:

| <bdi dir="ltr">Mode</bdi> | <bdi dir="ltr">Scope</bdi> | کاربرد |
|---|---|---|
| <bdi dir="ltr">`STANDALONE`</bdi> | فقط <bdi dir="ltr">Module</bdi> جاری | <bdi dir="ltr">Default</bdi>؛ استقلال و <bdi dir="ltr">Mock</bdi> کردن <bdi dir="ltr">Efferent Dependency</bdi>ها |
| <bdi dir="ltr">`DIRECT_DEPENDENCIES`</bdi> | <bdi dir="ltr">Module</bdi> + <bdi dir="ltr">Dependency</bdi>های مستقیم | <bdi dir="ltr">Integration</bdi> محدود |
| <bdi dir="ltr">`ALL_DEPENDENCIES`</bdi> | <bdi dir="ltr">Module</bdi> + تمام <bdi dir="ltr">Dependency tree</bdi> | سناریوی گسترده‌تر، با هزینه و <bdi dir="ltr">Coupling</bdi> بیشتر |

نمونهٔ <bdi dir="ltr">Skeleton:</bdi>


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


اگر برای بالا آمدن یک <bdi dir="ltr">Module</bdi> دائماً <bdi dir="ltr">`ALL_DEPENDENCIES`</bdi> لازم است، احتمال <bdi dir="ltr">High Coupling</bdi> یا <bdi dir="ltr">Boundary</bdi> ضعیف را بررسی کن. واکنش اول نباید بزرگ‌کردن <bdi dir="ltr">Test scope</bdi> باشد؛ <bdi dir="ltr">Dependency</bdi> بیرونی را می‌توان در <bdi dir="ltr">`STANDALONE`</bdi> <bdi dir="ltr">Mock</bdi> کرد.

در <bdi dir="ltr">Sprint 01</bdi>، <bdi dir="ltr">Architecture Verification</bdi> اجباری و <bdi dir="ltr">Module behavior test</bdi> در حد <bdi dir="ltr">Skeleton/Design</bdi> است. <bdi dir="ltr">Domain behavior</bdi> از <bdi dir="ltr">Sprint 02</bdi> اضافه می‌شود.

## 9. چه چیزی را این تست ثابت نمی‌کند؟

<bdi dir="ltr">`ApplicationModules.verify()`</bdi> نمی‌تواند ثابت کند:

- <bdi dir="ltr">Bounded Context</bdi>ها از نظر کسب‌وکار درست کشف شده‌اند.
- <bdi dir="ltr">Owner</bdi> داده و <bdi dir="ltr">Decision</bdi> درست است.
- <bdi dir="ltr">Event</bdi> نام و <bdi dir="ltr">Semantic</bdi> درست دارد.
- دو <bdi dir="ltr">Module</bdi> یک جدول مشترک را مستقیم <bdi dir="ltr">Update</bdi> نمی‌کنند.
- <bdi dir="ltr">HTTP call runtime</bdi> باعث <bdi dir="ltr">Cycle</bdi> یا <bdi dir="ltr">Availability coupling</bdi> نشده است.
- تراکنش، <bdi dir="ltr">Idempotency</bdi>، <bdi dir="ltr">Retry</bdi> یا <bdi dir="ltr">Reconciliation</bdi> صحیح است.
- <bdi dir="ltr">Journal balanced</bdi> است.
- <bdi dir="ltr">NFR</bdi>های <bdi dir="ltr">Latency</bdi> و <bdi dir="ltr">Availability</bdi> برآورده شده‌اند.

به همین دلیل <bdi dir="ltr">Architecture Evidence</bdi> لایه‌ای است:

| <bdi dir="ltr">Concern</bdi> | <bdi dir="ltr">Evidence</bdi> |
|---|---|
| <bdi dir="ltr">Strategic boundary</bdi> | <bdi dir="ltr">Domain/Context Map</bdi> + <bdi dir="ltr">expert review</bdi> |
| <bdi dir="ltr">Ownership</bdi> | <bdi dir="ltr">Ownership Matrix</bdi> + <bdi dir="ltr">scenario defense</bdi> |
| <bdi dir="ltr">Compile-time module rules</bdi> | <bdi dir="ltr">`ApplicationModules.verify()`</bdi> |
| <bdi dir="ltr">Module behavior</bdi> | <bdi dir="ltr">Unit</bdi> + <bdi dir="ltr">`@ApplicationModuleTest`</bdi> |
| <bdi dir="ltr">Runtime contracts</bdi> | <bdi dir="ltr">Contract/integration tests</bdi> در <bdi dir="ltr">Sprint</bdi>های بعد |
| <bdi dir="ltr">Data ownership</bdi> | <bdi dir="ltr">Schema access rules</bdi> + <bdi dir="ltr">migration checks</bdi> در <bdi dir="ltr">Sprint</bdi>های بعد |
| <bdi dir="ltr">Distributed failure</bdi> | <bdi dir="ltr">Failure tests</bdi> + <bdi dir="ltr">reconciliation evidence</bdi> در <bdi dir="ltr">Sprint</bdi>های بعد |

یک <bdi dir="ltr">Test</bdi> سبز همهٔ معماری را تأیید نمی‌کند؛ فقط <bdi dir="ltr">Property</bdi> تعریف‌شده را تأیید می‌کند.

## <bdi dir="ltr">10. Fitness Function</bdi>های آینده

این هفته فقط <bdi dir="ltr">Baseline</bdi> است. در ادامه می‌توانیم قواعد زیر را اضافه کنیم:

- <bdi dir="ltr">Domain code</bdi> نباید به <bdi dir="ltr">Spring/JPA</bdi> وابسته باشد.
- <bdi dir="ltr">Controller</bdi> نباید <bdi dir="ltr">Repository</bdi> را مستقیم فراخوانی کند.
- <bdi dir="ltr">Event</bdi>ها باید <bdi dir="ltr">Immutable</bdi> و <bdi dir="ltr">Versioned</bdi> باشند.
- هیچ <bdi dir="ltr">Service</bdi> به <bdi dir="ltr">Schema</bdi> دیگری دسترسی نداشته باشد.
- <bdi dir="ltr">Journal</bdi> باید <bdi dir="ltr">balanced</bdi> باشد.
- <bdi dir="ltr">Contract compatibility</bdi> باید در <bdi dir="ltr">CI</bdi> کنترل شود.
- <bdi dir="ltr">Dependency vulnerability</bdi> و <bdi dir="ltr">Secret scanning</bdi> باید پاس شوند.

هر <bdi dir="ltr">Rule</bdi> باید به <bdi dir="ltr">Risk</bdi> معماری واقعی وصل باشد؛ زیادکردن <bdi dir="ltr">Test</bdi> بدون <bdi dir="ltr">Intent</bdi> روشن، <bdi dir="ltr">Noise</bdi> تولید می‌کند.

## 11. خطاهای رایج

### <bdi dir="ltr">Test</bdi> سبز، پس <bdi dir="ltr">Boundary</bdi> درست است

ابزار فقط قواعد ساختاری را روی <bdi dir="ltr">Package layout</bdi> فعلی اجرا می‌کند. <bdi dir="ltr">Domain review</bdi> همچنان لازم است.

### نقض را با <bdi dir="ltr">Public</bdi> کردن <bdi dir="ltr">Package</bdi> حل کنیم

<bdi dir="ltr">Public/Named</bdi> کردن <bdi dir="ltr">Type</bdi> باید <bdi dir="ltr">Contract decision</bdi> باشد؛ نه راه فرار از <bdi dir="ltr">Test.</bdi>

### <bdi dir="ltr">Module</bdi> را <bdi dir="ltr">Open</bdi> کنیم

<bdi dir="ltr">Open Module</bdi> برای <bdi dir="ltr">Migration Legacy</bdi> مفید است، ولی در کد جدید <bdi dir="ltr">Encapsulation</bdi> را تضعیف می‌کند.

### <bdi dir="ltr">Cycle</bdi> را با <bdi dir="ltr">`common`</bdi> بشکنیم

انتقال همهٔ <bdi dir="ltr">Type</bdi>ها به <bdi dir="ltr">`common`</bdi> <bdi dir="ltr">Cycle</bdi> ظاهری را حذف و مدل مشترک عظیم می‌سازد. <bdi dir="ltr">Ownership</bdi> و <bdi dir="ltr">Direction</bdi> را اصلاح کن.

### فقط <bdi dir="ltr">Happy Path Test</bdi>

بدون آزمایش منفی نمی‌دانی <bdi dir="ltr">Fitness Function</bdi> واقعاً نقض را می‌گیرد یا <bdi dir="ltr">Module detection</bdi> ناقص است.

### <bdi dir="ltr">Filter</bdi> دائمی نقض‌ها

<bdi dir="ltr">Exception list</bdi> بدون <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">Expiry</bdi> به معماری واقعی تبدیل می‌شود.

## 12. تمرین مستقل

[<bdi dir="ltr">Day 06 Exercise</bdi> — <bdi dir="ltr">Module Verification</bdi>](../exercises/day-06-module-verification.md) را انجام بده. خروجی قرمز آزمایش منفی و خروجی سبز پس از اصلاح هر دو لازم‌اند.

## 13. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| <bdi dir="ltr">Architecture test</bdi> در <bdi dir="ltr">`mvn verify`</bdi> | ۲ |
| شش <bdi dir="ltr">Module</bdi> درست کشف شده | ۲ |
| <bdi dir="ltr">Negative experiment</bdi> معتبر | ۲ |
| <bdi dir="ltr">Repair</bdi> و نتیجهٔ سبز | ۲ |
| بیان محدودیت <bdi dir="ltr">Test</bdi> و <bdi dir="ltr">Evidence</bdi>های مکمل | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۸ از ۱۰. فقط <bdi dir="ltr">Screenshot</bdi> سبز بدون <bdi dir="ltr">Negative evidence</bdi> حداکثر ۶ می‌گیرد.

## 14. آزمون خروج

درس را ببند و [<bdi dir="ltr">Day 06 Exit Ticket</bdi>](../quizzes/day-06-exit-ticket.md) را پاسخ بده.

## 15. منابع اصلی

- [<bdi dir="ltr">Spring Modulith</bdi> — <bdi dir="ltr">Verification</bdi>](https://docs.spring.io/spring-modulith/reference/verification.html)
- [<bdi dir="ltr">Spring Modulith</bdi> — <bdi dir="ltr">Module Testing</bdi>](https://docs.spring.io/spring-modulith/reference/testing.html)

<bdi dir="ltr">API</bdi>ها و سه <bdi dir="ltr">Rule</bdi> اصلی <bdi dir="ltr">Verification</bdi> با مستند رسمی نسخهٔ 2.1.0 تطبیق داده شده‌اند.

</div>
