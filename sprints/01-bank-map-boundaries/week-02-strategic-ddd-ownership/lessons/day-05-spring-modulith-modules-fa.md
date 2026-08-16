<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 05</span> — تبدیل فرضیهٔ مرزها به <span dir="ltr">Spring Modulith</span>

- <span dir="ltr">Day budget: 100 minutes</span> — <span dir="ltr">20 lesson/reference</span> + <span dir="ltr">75 implementation</span> + <span dir="ltr">5 exit ticket</span>
- <span dir="ltr">Output: six logical Application Modules</span> + <span dir="ltr">dependency policy</span>
- <span dir="ltr">Code root:</span> <span dir="ltr">`backend/banking-modulith`</span>
- <span dir="ltr">Versions: Java 21</span>، <span dir="ltr">Spring Boot 4.1.0</span>، <span dir="ltr">Spring Modulith 2.1.0</span>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. توضیح بدهی چرا <span dir="ltr">Application Module</span> یک <span dir="ltr">Boundary</span> منطقی است، نه <span dir="ltr">Microservice.</span>
2. شش <span dir="ltr">Module</span> را بر اساس <span dir="ltr">Package</span>های <span dir="ltr">Function-first</span> بسازی.
3. <span dir="ltr">Provided Interface</span>، <span dir="ltr">Internal Implementation</span> و <span dir="ltr">Required Interface</span> را تشخیص بدهی.
4. <span dir="ltr">`@ApplicationModule`</span>، <span dir="ltr">`allowedDependencies`</span> و <span dir="ltr">`@NamedInterface`</span> را درست به‌کار ببری.
5. <span dir="ltr">Dependency Policy</span> را از <span dir="ltr">Context Map</span> استخراج کنی؛ نه از ترتیب <span dir="ltr">Controller</span>ها.
6. از ساخت <span dir="ltr">`common`</span> یا <span dir="ltr">Shared Entity</span> بدون دلیل جلوگیری کنی.

## 2. چرا بعد از چهار روز تحلیل وارد کد می‌شویم؟

<span dir="ltr">Package Structure</span> یک تصمیم بی‌اثر نیست. <span dir="ltr">Dependency</span>های <span dir="ltr">Compile-time</span> و دسترسی به <span dir="ltr">Type</span>ها به‌تدریج مدل ذهنی تیم را تثبیت می‌کنند. اگر از روز اول <span dir="ltr">Package</span>ها را بر اساس جدول یا <span dir="ltr">Layer</span> بسازیم، حتی یک <span dir="ltr">Domain Map</span> خوب نیز در کد بی‌اثر می‌شود.

ترتیب این هفته عمداً چنین بود:


</div>

<div dir="ltr" align="left">

~~~text
Subdomain strategy
  → language boundaries
  → context relationships
  → data/decision ownership
  → module hypothesis in code
~~~

</div>

<div dir="rtl" align="right">


امروز کد «اثبات» نمی‌کند <span dir="ltr">Boundary</span> دامینی درست است. کد فقط فرضیهٔ فعلی را:

- آشکار می‌کند؛
- <span dir="ltr">Dependency</span>های آن را قابل‌مشاهده می‌کند؛
- نقض آن را قابل‌آزمون می‌کند؛
- امکان <span dir="ltr">Refactor</span> آینده را بالا می‌برد.

## <span dir="ltr">3. Application Module</span> در <span dir="ltr">Spring Modulith</span>

طبق [مستند رسمی <span dir="ltr">Fundamentals</span>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)، یک <span dir="ltr">Application Module</span> واحدی از <span dir="ltr">Functionality</span> است که سه بخش دارد:

### <span dir="ltr">Provided Interface</span>

آنچه <span dir="ltr">Module</span> به دیگر <span dir="ltr">Module</span>ها عرضه می‌کند:

- <span dir="ltr">Spring Bean</span>های <span dir="ltr">Public API</span>
- <span dir="ltr">Command/Query facade</span>های منطقی
- <span dir="ltr">Application/Domain Event</span>های <span dir="ltr">Published</span>
- <span dir="ltr">Type</span>های <span dir="ltr">Contract</span> که عمداً <span dir="ltr">Expose</span> شده‌اند

<span dir="ltr">Provided Interface</span> با <span dir="ltr">REST Controller</span> یکی نیست. <span dir="ltr">REST</span> می‌تواند <span dir="ltr">Adapter</span> بیرونی باشد؛ <span dir="ltr">Module API</span> یک <span dir="ltr">Boundary</span> داخل <span dir="ltr">Application</span> است.

### <span dir="ltr">Internal Implementation</span>

جزئیاتی که دیگر <span dir="ltr">Module</span>ها نباید بدانند:

- <span dir="ltr">Domain model internals</span>
- <span dir="ltr">Repository implementations</span>
- <span dir="ltr">Policy/Strategy implementations</span>
- <span dir="ltr">JPA mappings</span>
- <span dir="ltr">workflow details</span>

ممکن است <span dir="ltr">Type</span> داخلی برای استفاده در <span dir="ltr">Subpackage</span>های همان <span dir="ltr">Module</span> <span dir="ltr">`public`</span> باشد، اما <span dir="ltr">Spring Modulith</span> دسترسی <span dir="ltr">Module</span> دیگر به <span dir="ltr">Subpackage</span> داخلی را رد می‌کند.

### <span dir="ltr">Required Interface</span>

<span dir="ltr">API</span> یا <span dir="ltr">Event</span>هایی از <span dir="ltr">Module</span>های دیگر که این <span dir="ltr">Module</span> برای کارکردن نیاز دارد. <span dir="ltr">Required Interface</span> باید در <span dir="ltr">Dependency Policy</span> صریح باشد.

## 4. کشف <span dir="ltr">Module</span> با <span dir="ltr">Package</span>

<span dir="ltr">Application</span> اصلی در <span dir="ltr">Package</span> زیر است:


</div>

<div dir="ltr" align="left">

~~~text
com.example.corebankinglab
└── CoreBankingLabApplication
~~~

</div>

<div dir="rtl" align="right">


در <span dir="ltr">Detection</span> پیش‌فرض <span dir="ltr">Spring Modulith</span>، هر <span dir="ltr">Direct Subpackage</span> زیر <span dir="ltr">Package</span> اصلی یک <span dir="ltr">Application Module Candidate</span> است:


</div>

<div dir="ltr" align="left">

~~~text
com.example.corebankinglab.partycustomer
com.example.corebankinglab.productagreement
com.example.corebankinglab.deposits
com.example.corebankinglab.lending
com.example.corebankinglab.payments
com.example.corebankinglab.accounting
~~~

</div>

<div dir="rtl" align="right">


برای <span dir="ltr">Lab</span>، این شش <span dir="ltr">Module</span> یک فرضیهٔ آموزشی‌اند. <span dir="ltr">Domain Map</span> ممکن است نشان دهد <span dir="ltr">Product Catalog</span> و <span dir="ltr">Agreement</span> دو <span dir="ltr">Bounded Context</span> هستند، اما برای <span dir="ltr">Sprint 01</span> می‌توانند در یک <span dir="ltr">Module</span> موقت قرار بگیرند؛ این تفاوت باید در <span dir="ltr">Dossier</span> به‌عنوان <span dir="ltr">Constraint/Decision</span> ثبت شود.

## <span dir="ltr">5. API Package</span> و <span dir="ltr">Internal Package</span>

در <span dir="ltr">Module</span> بستهٔ پیش‌فرض:

- <span dir="ltr">Type</span>های <span dir="ltr">Public</span> در <span dir="ltr">Base Package</span>، <span dir="ltr">API</span> قابل‌دسترسی <span dir="ltr">Module</span> هستند.
- <span dir="ltr">Subpackage</span>ها <span dir="ltr">Internal</span> محسوب می‌شوند، مگر اینکه صریحاً <span dir="ltr">Named Interface</span> شوند.

نمونه:


</div>

<div dir="ltr" align="left">

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

</div>

<div dir="rtl" align="right">


در این هفته نیاز نیست منطق <span dir="ltr">Deposits</span> را پیاده کنی. هدف ساخت <span dir="ltr">Boundary</span> و <span dir="ltr">Verification</span> است. کلاس و <span dir="ltr">Interface</span> مصنوعی صرفاً برای پرکردن <span dir="ltr">Folder</span> نساز؛ هر <span dir="ltr">Type</span> باید <span dir="ltr">Purpose</span> داشته باشد.

## 6. <span dir="ltr">`package-info.java`</span> برای <span dir="ltr">Module</span>

نمونهٔ هدایت‌شده برای <span dir="ltr">Deposits</span> در اولین مرحله و بدون <span dir="ltr">Dependency</span> مستقیم:


</div>

<div dir="ltr" align="left">

```java
@org.springframework.modulith.ApplicationModule(
        displayName = "Deposits",
        allowedDependencies = {}
)
package com.example.corebankinglab.deposits;
```

</div>

<div dir="rtl" align="right">


نکات:

- آرایهٔ خالی یعنی <span dir="ltr">Dependency</span> به <span dir="ltr">Module</span> دیگر مجاز نیست.
- حذف <span dir="ltr">`allowedDependencies`</span> یعنی <span dir="ltr">Spring Modulith Dependency</span>های <span dir="ltr">Module</span> را از این <span dir="ltr">Attribute</span> محدود نمی‌کند؛ <span dir="ltr">Internal-access</span> و <span dir="ltr">Cycle checks</span> همچنان قواعد خود را دارند.
- <span dir="ltr">Module</span> به‌صورت پیش‌فرض <span dir="ltr">`CLOSED`</span> است.
- <span dir="ltr">`OPEN`</span> برای <span dir="ltr">Migration</span> تدریجی <span dir="ltr">Legacy</span> وجود دارد؛ استفاده از آن در <span dir="ltr">Lab</span> جدید، <span dir="ltr">Encapsulation</span> را تضعیف می‌کند و ممنوع است مگر <span dir="ltr">ADR</span> مستقل.

## <span dir="ltr">7. Named Interface</span>

<span dir="ltr">Base Package API</span> پیش‌فرض را عرضه می‌کند. اگر یک <span dir="ltr">Subpackage</span> مشخص نیز باید <span dir="ltr">Expose</span> شود، آن را <span dir="ltr">Named Interface</span> کن.

مثال:


</div>

<div dir="ltr" align="left">

```java
@org.springframework.modulith.NamedInterface("events")
package com.example.corebankinglab.deposits.events;
```

</div>

<div dir="rtl" align="right">


اکنون یک <span dir="ltr">Module</span> مصرف‌کننده می‌تواند در <span dir="ltr">`allowedDependencies`</span> دقیقاً به این <span dir="ltr">Interface</span> اشاره کند:


</div>

<div dir="ltr" align="left">

```java
@org.springframework.modulith.ApplicationModule(
        allowedDependencies = "deposits::events"
)
package com.example.corebankinglab.accounting;
```

</div>

<div dir="rtl" align="right">


این کد فقط <span dir="ltr">Syntax</span> را نشان می‌دهد. اینکه <span dir="ltr">Accounting</span> واقعاً باید <span dir="ltr">Compile-time</span> به <span dir="ltr">`deposits::events`</span> وابسته باشد یا <span dir="ltr">Contract</span> در <span dir="ltr">Integration Boundary</span> دیگری قرار گیرد، یک تصمیم معماری بعدی است. امروز هر <span dir="ltr">Dependency</span> را با <span dir="ltr">Context Map</span> و <span dir="ltr">Ownership</span> دفاع کن.

می‌توان بیش از یک <span dir="ltr">Dependency</span> را نوشت:


</div>

<div dir="ltr" align="left">

```java
@org.springframework.modulith.ApplicationModule(
        allowedDependencies = {
                "partycustomer::reference",
                "productagreement::agreement-snapshot"
        }
)
package com.example.corebankinglab.lending;
```

</div>

<div dir="rtl" align="right">


این نمونه نیز پاسخ نهایی <span dir="ltr">Lab</span> نیست. <span dir="ltr">Named Interface</span>ها باید واقعاً در <span dir="ltr">Provider</span> تعریف شده باشند و نام‌ها از <span dir="ltr">Language</span> همان <span dir="ltr">Boundary</span> بیایند.

## <span dir="ltr">8. Function-first</span>، نه <span dir="ltr">Layer-first</span>

ساختار ضعیف:


</div>

<div dir="ltr" align="left">

~~~text
controller/
service/
repository/
entity/
dto/
~~~

</div>

<div dir="rtl" align="right">


این ساختار همهٔ <span dir="ltr">Domain</span>ها را در <span dir="ltr">Layer</span>های افقی مخلوط می‌کند و دسترسی متقابل را آسان می‌سازد.

ساختار بهتر:


</div>

<div dir="ltr" align="left">

~~~text
partycustomer/
productagreement/
deposits/
lending/
payments/
accounting/
~~~

</div>

<div dir="rtl" align="right">


هر <span dir="ltr">Module</span> می‌تواند در داخل خودش <span dir="ltr">Layer</span> یا <span dir="ltr">Hexagonal structure</span> داشته باشد؛ آن موضوع <span dir="ltr">Sprint 02</span> است. ابتدا <span dir="ltr">Boundary</span> کسب‌وکاری، سپس ساختار داخلی.

## <span dir="ltr">9. Dependency Policy</span> از کجا می‌آید؟

برای هر <span dir="ltr">Dependency Candidate</span> این سؤال‌ها را پاسخ بده:

1. کدام <span dir="ltr">Use Case</span> واقعاً آن را نیاز دارد؟
2. <span dir="ltr">Provider</span> کدام <span dir="ltr">Fact/Capability</span> را مالک است؟
3. <span dir="ltr">Consumer</span> به <span dir="ltr">Reference</span>، <span dir="ltr">Snapshot</span>، <span dir="ltr">Query</span>، <span dir="ltr">Command</span> یا <span dir="ltr">Event</span> نیاز دارد؟
4. آیا <span dir="ltr">Dependency</span> به یک <span dir="ltr">Named Interface</span> کوچک محدود می‌شود؟
5. آیا <span dir="ltr">Event</span> یا <span dir="ltr">Translation</span> می‌تواند <span dir="ltr">Compile-time Coupling</span> را کمتر کند؟
6. اگر <span dir="ltr">Provider</span> تغییر کند، چه چیزی در <span dir="ltr">Consumer Recompile/Release</span> می‌شود؟
7. آیا <span dir="ltr">Dependency</span> معکوس یا <span dir="ltr">Cycle</span> ایجاد می‌کند؟

وجود یک فلش در <span dir="ltr">Sequence Diagram</span> به‌تنهایی مجوز <span dir="ltr">Import Type</span>های داخلی نیست.

## <span dir="ltr">10. Mapping</span> پیشنهادی اولیه، نه پاسخ قطعی

| <span dir="ltr">Problem-space hypothesis</span> | <span dir="ltr">Lab module</span> | نکته |
|---|---|---|
| <span dir="ltr">Party/Customer Identity and Relationship</span> | <span dir="ltr">`partycustomer`</span> | <span dir="ltr">Consumer</span>ها <span dir="ltr">Reference/Snapshot</span> می‌گیرند |
| <span dir="ltr">Product Catalog</span> + <span dir="ltr">Agreement</span> | <span dir="ltr">`productagreement`</span> | ممکن است بعداً به دو <span dir="ltr">Context/Module</span> تفکیک شود |
| <span dir="ltr">Deposit Account Servicing</span> | <span dir="ltr">`deposits`</span> | مانده و <span dir="ltr">Hold</span> عملیاتی را محصور می‌کند |
| <span dir="ltr">Loan Lifecycle/Servicing</span> | <span dir="ltr">`lending`</span> | مانده و برنامهٔ عملیاتی <span dir="ltr">Loan</span> |
| <span dir="ltr">Payment Order/Clearing/Settlement</span> | <span dir="ltr">`payments`</span> | <span dir="ltr">Channel</span> مالک <span dir="ltr">Payment State</span> نیست |
| <span dir="ltr">Journal/Subledger/GL</span> | <span dir="ltr">`accounting`</span> | <span dir="ltr">Operational Domain state</span> را مالک نمی‌شود |

<span dir="ltr">`Legal Orders`</span> در <span dir="ltr">Gate</span> یک <span dir="ltr">Context</span> خارجی/<span dir="ltr">near-core</span> است و الزاماً <span dir="ltr">Module</span> هفتم <span dir="ltr">Lab</span> در این <span dir="ltr">Sprint</span> نیست. <span dir="ltr">Contract</span> آن با <span dir="ltr">Deposits</span> باید در <span dir="ltr">Context Map</span> نشان داده شود.

## <span dir="ltr">11. Type</span>های مشترک و دام <span dir="ltr">`common`</span>

<span dir="ltr">Week 01</span> ممکن است <span dir="ltr">`Money`</span> و <span dir="ltr">Typed ID</span>ها را ساخته باشی. اکنون باید محل آن‌ها را آگاهانه بازبینی کنی.

### <span dir="ltr">Typed ID</span>

- <span dir="ltr">`CustomerId`</span> بهتر است <span dir="ltr">Contract type</span> متعلق به <span dir="ltr">Authority</span> یا <span dir="ltr">Published Reference</span> باشد.
- <span dir="ltr">`AccountId`</span> نباید با شمارهٔ حساب بانکی یا <span dir="ltr">Accounting Account ID</span> یکی فرض شود.
- <span dir="ltr">Import</span> کردن <span dir="ltr">Entity</span> کامل برای گرفتن <span dir="ltr">ID</span> ممنوع است.

### <span dir="ltr">Money</span>

مفهوم پایهٔ <span dir="ltr">Amount/Currency</span> می‌تواند بسیار کوچک و مشترک باشد، اما <span dir="ltr">Policy</span>های <span dir="ltr">Scale</span>، <span dir="ltr">Rounding</span> و <span dir="ltr">Sign</span> ممکن است <span dir="ltr">Contextual</span> باشند. سه گزینهٔ قابل بررسی:

1. <span dir="ltr">Value Object</span> مستقل در هر <span dir="ltr">Context</span> با <span dir="ltr">Semantic</span> خاص
2. <span dir="ltr">Shared Kernel</span> بسیار کوچک با <span dir="ltr">Governance</span> سخت‌گیرانه
3. <span dir="ltr">Boundary Contract type</span> و <span dir="ltr">Translation</span> به مدل داخلی

در این <span dir="ltr">Sprint</span> یک <span dir="ltr">Package</span> عمومی <span dir="ltr">`common`</span> نساز. ابتدا <span dir="ltr">Usage</span>، <span dir="ltr">Owner</span> و <span dir="ltr">Change coupling</span> را ثبت کن. <span dir="ltr">Shared Kernel</span> یک تصمیم صریح است، نه سطل <span dir="ltr">Type</span>های راحت.

## 12. برنامهٔ ۷۵ دقیقه‌ای اجرا

### دقیقهٔ 0 تا 5 — <span dir="ltr">Baseline</span>

از مسیر <span dir="ltr">`backend/banking-modulith`</span> اجرا کن:


</div>

<div dir="ltr" align="left">

~~~bash
mvn verify
~~~

</div>

<div dir="rtl" align="right">


نتیجه و <span dir="ltr">Commit</span> پایه را ثبت کن. اگر <span dir="ltr">Baseline</span> قرمز است، <span dir="ltr">Module work</span> را روی شکست قبلی بنا نکن.

### دقیقهٔ 5 تا 15 — <span dir="ltr">Dependency Plan</span>

[<span dir="ltr">Module Dependency Policy</span>](../artifacts/module-dependency-policy.md) را باز کن. برای شش <span dir="ltr">Module</span>، <span dir="ltr">Purpose</span> و <span dir="ltr">Provided/Required Interface</span> فرضی را بنویس. هنوز <span dir="ltr">Import</span> نساز.

### دقیقهٔ 15 تا 35 — <span dir="ltr">Base Packages</span>

شش <span dir="ltr">Direct Subpackage</span> و <span dir="ltr">`package-info.java`</span> بساز. در مرحلهٔ اول <span dir="ltr">`allowedDependencies = {}`</span> قرار بده تا هر <span dir="ltr">Dependency</span> بعدی آگاهانه اضافه شود.

### دقیقهٔ 35 تا 50 — <span dir="ltr">Public/Internal Boundary</span>

برای هر <span dir="ltr">Module:</span>

- یک <span dir="ltr">Public API</span> واقعی یا <span dir="ltr">Placeholder</span> مستندشدهٔ حداقلی در <span dir="ltr">Base Package</span>
- یک <span dir="ltr">`internal`</span> <span dir="ltr">package</span>
- بدون <span dir="ltr">Public Entity</span> مشترک

اگر هنوز <span dir="ltr">Use Case</span> مشخصی نداری، <span dir="ltr">`package-info.java`</span> و <span dir="ltr">Module description</span> کافی است؛ <span dir="ltr">API</span> مصنوعی نساز.

### دقیقهٔ 50 تا 60 — <span dir="ltr">Named Interfaces</span>

فقط <span dir="ltr">Named Interface</span>هایی را بساز که <span dir="ltr">Context Map</span> نیاز آن‌ها را نشان داده است. برای هر مورد دلیل و <span dir="ltr">Consumer</span> را در <span dir="ltr">Policy</span> ثبت کن.

### دقیقهٔ 60 تا 68 — <span dir="ltr">Allowed Dependencies</span>

<span dir="ltr">Dependency</span>های لازم را یکی‌یکی اضافه کن. اگر برای حل <span dir="ltr">Compile</span> به <span dir="ltr">Dependency</span> متقابل نیاز شد، توقف کن: احتمالاً <span dir="ltr">Contract</span> یا <span dir="ltr">Direction</span> مشکل دارد.

### دقیقهٔ 68 تا 75 — <span dir="ltr">Inspect and verify</span>

با <span dir="ltr">`ApplicationModules`</span> ساختار کشف‌شده را چاپ کن و سپس <span dir="ltr">Verification</span> را اجرا کن. تست رسمی روز ششم اضافه می‌شود، ولی امروز باید شش <span dir="ltr">Module</span> تشخیص داده شوند.

## 13. مشاهدهٔ مدل <span dir="ltr">Module</span>ها

نمونهٔ کد موقت یا تست:


</div>

<div dir="ltr" align="left">

```java
var modules = org.springframework.modulith.core.ApplicationModules
        .of(CoreBankingLabApplication.class);

modules.forEach(System.out::println);
```

</div>

<div dir="rtl" align="right">


خروجی را برای این موارد بخوان:

- <span dir="ltr">Logical name</span>
- <span dir="ltr">Base package</span>
- <span dir="ltr">Spring beans</span>
- <span dir="ltr">Exposed types</span>
- <span dir="ltr">Direct dependencies</span>

صرف دیدن شش نام کافی نیست؛ <span dir="ltr">Public surface</span> و <span dir="ltr">Dependency</span>ها را نیز بررسی کن.

## 14. خطاهای رایج

### شش <span dir="ltr">Domain</span> مساوی شش <span dir="ltr">Microservice</span>

ما فقط شش <span dir="ltr">Module</span> داخل یک <span dir="ltr">Deployment</span> ساخته‌ایم. استخراج <span dir="ltr">Service</span> نیازمند <span dir="ltr">ADR</span>، <span dir="ltr">NFR</span>، <span dir="ltr">Team autonomy</span>، <span dir="ltr">Data</span> و <span dir="ltr">Operational evidence</span> است.

### <span dir="ltr">`internal`</span> فقط <span dir="ltr">Convention</span> است

اگر <span dir="ltr">Architecture Test</span> نباشد، <span dir="ltr">Developer</span> می‌تواند <span dir="ltr">Type</span> عمومی داخل <span dir="ltr">Subpackage</span> را <span dir="ltr">Import</span> کند. <span dir="ltr">Day 06</span> آن را <span dir="ltr">enforce</span> می‌کند.

### همه‌چیز <span dir="ltr">Public</span> در <span dir="ltr">Base Package</span>

هر <span dir="ltr">Public Type</span> در <span dir="ltr">Base Package</span> بخشی از <span dir="ltr">Provided Interface</span> است. <span dir="ltr">Surface</span> بزرگ <span dir="ltr">Coupling</span> را زیاد می‌کند.

### <span dir="ltr">Named Interface</span> برای هر <span dir="ltr">Folder</span>

<span dir="ltr">Named Interface</span> باید <span dir="ltr">Consumer</span> و <span dir="ltr">Contract</span> مشخص داشته باشد؛ نه اینکه <span dir="ltr">Encapsulation</span> را بی‌اثر کند.

### <span dir="ltr">Dependency</span> برای استفادهٔ دوباره از <span dir="ltr">Entity</span>

<span dir="ltr">Reuse</span> کد دلیل کافی برای وابستگی <span dir="ltr">Domain</span> نیست. <span dir="ltr">Contract</span>، <span dir="ltr">Reference</span> یا <span dir="ltr">Translation</span> را بررسی کن.

### <span dir="ltr">Cycle</span> را با <span dir="ltr">Event</span> پنهان‌کردن

اگر مدل و فرآیند ذاتاً دوری و مبهم است، عوض‌کردن <span dir="ltr">Method call</span> با <span dir="ltr">Event</span> نامفهوم مسئله را حل نمی‌کند. <span dir="ltr">Ownership</span> و <span dir="ltr">Direction</span> را دوباره تحلیل کن.

## 15. تمرین مستقل

[<span dir="ltr">Day 05 Exercise</span> — <span dir="ltr">Module Skeleton</span>](../exercises/day-05-module-skeleton.md) را اجرا کن. کد را خودت بنویس و <span dir="ltr">Output</span> ماژول‌ها و تصمیم <span dir="ltr">Dependency</span> را در <span dir="ltr">Workbook</span> ثبت کن.

## 16. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| شش <span dir="ltr">Module</span> بر اساس <span dir="ltr">Direct Subpackage</span> | ۲ |
| <span dir="ltr">API/Internal boundary</span> عمدی | ۲ |
| <span dir="ltr">Named Interface</span> محدود و معنادار | ۲ |
| <span dir="ltr">Allowed dependencies</span> مستدل و بدون <span dir="ltr">Cycle</span> | ۲ |
| <span dir="ltr">Policy</span> و <span dir="ltr">Traceability</span> به <span dir="ltr">Context Map</span> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. استفاده از <span dir="ltr">Open Module</span> یا <span dir="ltr">Import</span> داخلی بدون <span dir="ltr">ADR</span> پذیرفته نیست.

## 17. آزمون خروج

پس از پایان کدنویسی، [<span dir="ltr">Day 05 Exit Ticket</span>](../quizzes/day-05-exit-ticket.md) را بدون مراجعه به درس پاسخ بده.

## 18. منابع اصلی

- [<span dir="ltr">Spring Modulith Fundamentals 2.1.0</span>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- [<span dir="ltr">ApplicationModule Javadoc 2.1.0</span>](https://docs.spring.io/spring-modulith/docs/2.1.0/api/org/springframework/modulith/ApplicationModule.html)

<span dir="ltr">Syntax</span>های <span dir="ltr">`allowedDependencies`</span>، آرایهٔ خالی، <span dir="ltr">Closed Module</span> و <span dir="ltr">Named Interface</span> با مستند رسمی 2.1.0 تطبیق داده شده‌اند.

</div>
