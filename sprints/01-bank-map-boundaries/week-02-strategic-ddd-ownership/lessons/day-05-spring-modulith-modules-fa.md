<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 05</bdi> — تبدیل فرضیهٔ مرزها به <bdi dir="ltr">Spring Modulith</bdi>

- <bdi dir="ltr">Day budget: 100 minutes</bdi> — <bdi dir="ltr">20 lesson/reference</bdi> + <bdi dir="ltr">75 implementation</bdi> + <bdi dir="ltr">5 exit ticket</bdi>
- <bdi dir="ltr">Output: six logical Application Modules</bdi> + <bdi dir="ltr">dependency policy</bdi>
- <bdi dir="ltr">Code root:</bdi> <bdi dir="ltr">`backend/banking-modulith`</bdi>
- <bdi dir="ltr">Versions: Java 21</bdi>، <bdi dir="ltr">Spring Boot 4.1.0</bdi>، <bdi dir="ltr">Spring Modulith 2.1.0</bdi>

## 1. هدف قابل سنجش

در پایان باید بتوانی:

1. توضیح بدهی چرا <bdi dir="ltr">Application Module</bdi> یک <bdi dir="ltr">Boundary</bdi> منطقی است، نه <bdi dir="ltr">Microservice.</bdi>
2. شش <bdi dir="ltr">Module</bdi> را بر اساس <bdi dir="ltr">Package</bdi>های <bdi dir="ltr">Function-first</bdi> بسازی.
3. <bdi dir="ltr">Provided Interface</bdi>، <bdi dir="ltr">Internal Implementation</bdi> و <bdi dir="ltr">Required Interface</bdi> را تشخیص بدهی.
4. <bdi dir="ltr">`@ApplicationModule`</bdi>، <bdi dir="ltr">`allowedDependencies`</bdi> و <bdi dir="ltr">`@NamedInterface`</bdi> را درست به‌کار ببری.
5. <bdi dir="ltr">Dependency Policy</bdi> را از <bdi dir="ltr">Context Map</bdi> استخراج کنی؛ نه از ترتیب <bdi dir="ltr">Controller</bdi>ها.
6. از ساخت <bdi dir="ltr">`common`</bdi> یا <bdi dir="ltr">Shared Entity</bdi> بدون دلیل جلوگیری کنی.

## 2. چرا بعد از چهار روز تحلیل وارد کد می‌شویم؟

<bdi dir="ltr">Package Structure</bdi> یک تصمیم بی‌اثر نیست. <bdi dir="ltr">Dependency</bdi>های <bdi dir="ltr">Compile-time</bdi> و دسترسی به <bdi dir="ltr">Type</bdi>ها به‌تدریج مدل ذهنی تیم را تثبیت می‌کنند. اگر از روز اول <bdi dir="ltr">Package</bdi>ها را بر اساس جدول یا <bdi dir="ltr">Layer</bdi> بسازیم، حتی یک <bdi dir="ltr">Domain Map</bdi> خوب نیز در کد بی‌اثر می‌شود.

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


امروز کد «اثبات» نمی‌کند <bdi dir="ltr">Boundary</bdi> دامینی درست است. کد فقط فرضیهٔ فعلی را:

- آشکار می‌کند؛
- <bdi dir="ltr">Dependency</bdi>های آن را قابل‌مشاهده می‌کند؛
- نقض آن را قابل‌آزمون می‌کند؛
- امکان <bdi dir="ltr">Refactor</bdi> آینده را بالا می‌برد.

## <bdi dir="ltr">3. Application Module</bdi> در <bdi dir="ltr">Spring Modulith</bdi>

طبق [مستند رسمی <bdi dir="ltr">Fundamentals</bdi>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)، یک <bdi dir="ltr">Application Module</bdi> واحدی از <bdi dir="ltr">Functionality</bdi> است که سه بخش دارد:

### <bdi dir="ltr">Provided Interface</bdi>

آنچه <bdi dir="ltr">Module</bdi> به دیگر <bdi dir="ltr">Module</bdi>ها عرضه می‌کند:

- <bdi dir="ltr">Spring Bean</bdi>های <bdi dir="ltr">Public API</bdi>
- <bdi dir="ltr">Command/Query facade</bdi>های منطقی
- <bdi dir="ltr">Application/Domain Event</bdi>های <bdi dir="ltr">Published</bdi>
- <bdi dir="ltr">Type</bdi>های <bdi dir="ltr">Contract</bdi> که عمداً <bdi dir="ltr">Expose</bdi> شده‌اند

<bdi dir="ltr">Provided Interface</bdi> با <bdi dir="ltr">REST Controller</bdi> یکی نیست. <bdi dir="ltr">REST</bdi> می‌تواند <bdi dir="ltr">Adapter</bdi> بیرونی باشد؛ <bdi dir="ltr">Module API</bdi> یک <bdi dir="ltr">Boundary</bdi> داخل <bdi dir="ltr">Application</bdi> است.

### <bdi dir="ltr">Internal Implementation</bdi>

جزئیاتی که دیگر <bdi dir="ltr">Module</bdi>ها نباید بدانند:

- <bdi dir="ltr">Domain model internals</bdi>
- <bdi dir="ltr">Repository implementations</bdi>
- <bdi dir="ltr">Policy/Strategy implementations</bdi>
- <bdi dir="ltr">JPA mappings</bdi>
- <bdi dir="ltr">workflow details</bdi>

ممکن است <bdi dir="ltr">Type</bdi> داخلی برای استفاده در <bdi dir="ltr">Subpackage</bdi>های همان <bdi dir="ltr">Module</bdi> <bdi dir="ltr">`public`</bdi> باشد، اما <bdi dir="ltr">Spring Modulith</bdi> دسترسی <bdi dir="ltr">Module</bdi> دیگر به <bdi dir="ltr">Subpackage</bdi> داخلی را رد می‌کند.

### <bdi dir="ltr">Required Interface</bdi>

<bdi dir="ltr">API</bdi> یا <bdi dir="ltr">Event</bdi>هایی از <bdi dir="ltr">Module</bdi>های دیگر که این <bdi dir="ltr">Module</bdi> برای کارکردن نیاز دارد. <bdi dir="ltr">Required Interface</bdi> باید در <bdi dir="ltr">Dependency Policy</bdi> صریح باشد.

## 4. کشف <bdi dir="ltr">Module</bdi> با <bdi dir="ltr">Package</bdi>

<bdi dir="ltr">Application</bdi> اصلی در <bdi dir="ltr">Package</bdi> زیر است:


</div>

<div dir="ltr" align="left">

~~~text
com.example.corebankinglab
└── CoreBankingLabApplication
~~~

</div>

<div dir="rtl" align="right">


در <bdi dir="ltr">Detection</bdi> پیش‌فرض <bdi dir="ltr">Spring Modulith</bdi>، هر <bdi dir="ltr">Direct Subpackage</bdi> زیر <bdi dir="ltr">Package</bdi> اصلی یک <bdi dir="ltr">Application Module Candidate</bdi> است:


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


برای <bdi dir="ltr">Lab</bdi>، این شش <bdi dir="ltr">Module</bdi> یک فرضیهٔ آموزشی‌اند. <bdi dir="ltr">Domain Map</bdi> ممکن است نشان دهد <bdi dir="ltr">Product Catalog</bdi> و <bdi dir="ltr">Agreement</bdi> دو <bdi dir="ltr">Bounded Context</bdi> هستند، اما برای <bdi dir="ltr">Sprint 01</bdi> می‌توانند در یک <bdi dir="ltr">Module</bdi> موقت قرار بگیرند؛ این تفاوت باید در <bdi dir="ltr">Dossier</bdi> به‌عنوان <bdi dir="ltr">Constraint/Decision</bdi> ثبت شود.

## <bdi dir="ltr">5. API Package</bdi> و <bdi dir="ltr">Internal Package</bdi>

در <bdi dir="ltr">Module</bdi> بستهٔ پیش‌فرض:

- <bdi dir="ltr">Type</bdi>های <bdi dir="ltr">Public</bdi> در <bdi dir="ltr">Base Package</bdi>، <bdi dir="ltr">API</bdi> قابل‌دسترسی <bdi dir="ltr">Module</bdi> هستند.
- <bdi dir="ltr">Subpackage</bdi>ها <bdi dir="ltr">Internal</bdi> محسوب می‌شوند، مگر اینکه صریحاً <bdi dir="ltr">Named Interface</bdi> شوند.

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


در این هفته نیاز نیست منطق <bdi dir="ltr">Deposits</bdi> را پیاده کنی. هدف ساخت <bdi dir="ltr">Boundary</bdi> و <bdi dir="ltr">Verification</bdi> است. کلاس و <bdi dir="ltr">Interface</bdi> مصنوعی صرفاً برای پرکردن <bdi dir="ltr">Folder</bdi> نساز؛ هر <bdi dir="ltr">Type</bdi> باید <bdi dir="ltr">Purpose</bdi> داشته باشد.

## 6. <bdi dir="ltr">`package-info.java`</bdi> برای <bdi dir="ltr">Module</bdi>

نمونهٔ هدایت‌شده برای <bdi dir="ltr">Deposits</bdi> در اولین مرحله و بدون <bdi dir="ltr">Dependency</bdi> مستقیم:


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

- آرایهٔ خالی یعنی <bdi dir="ltr">Dependency</bdi> به <bdi dir="ltr">Module</bdi> دیگر مجاز نیست.
- حذف <bdi dir="ltr">`allowedDependencies`</bdi> یعنی <bdi dir="ltr">Spring Modulith Dependency</bdi>های <bdi dir="ltr">Module</bdi> را از این <bdi dir="ltr">Attribute</bdi> محدود نمی‌کند؛ <bdi dir="ltr">Internal-access</bdi> و <bdi dir="ltr">Cycle checks</bdi> همچنان قواعد خود را دارند.
- <bdi dir="ltr">Module</bdi> به‌صورت پیش‌فرض <bdi dir="ltr">`CLOSED`</bdi> است.
- <bdi dir="ltr">`OPEN`</bdi> برای <bdi dir="ltr">Migration</bdi> تدریجی <bdi dir="ltr">Legacy</bdi> وجود دارد؛ استفاده از آن در <bdi dir="ltr">Lab</bdi> جدید، <bdi dir="ltr">Encapsulation</bdi> را تضعیف می‌کند و ممنوع است مگر <bdi dir="ltr">ADR</bdi> مستقل.

## <bdi dir="ltr">7. Named Interface</bdi>

<bdi dir="ltr">Base Package API</bdi> پیش‌فرض را عرضه می‌کند. اگر یک <bdi dir="ltr">Subpackage</bdi> مشخص نیز باید <bdi dir="ltr">Expose</bdi> شود، آن را <bdi dir="ltr">Named Interface</bdi> کن.

مثال:


</div>

<div dir="ltr" align="left">

```java
@org.springframework.modulith.NamedInterface("events")
package com.example.corebankinglab.deposits.events;
```

</div>

<div dir="rtl" align="right">


اکنون یک <bdi dir="ltr">Module</bdi> مصرف‌کننده می‌تواند در <bdi dir="ltr">`allowedDependencies`</bdi> دقیقاً به این <bdi dir="ltr">Interface</bdi> اشاره کند:


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


این کد فقط <bdi dir="ltr">Syntax</bdi> را نشان می‌دهد. اینکه <bdi dir="ltr">Accounting</bdi> واقعاً باید <bdi dir="ltr">Compile-time</bdi> به <bdi dir="ltr">`deposits::events`</bdi> وابسته باشد یا <bdi dir="ltr">Contract</bdi> در <bdi dir="ltr">Integration Boundary</bdi> دیگری قرار گیرد، یک تصمیم معماری بعدی است. امروز هر <bdi dir="ltr">Dependency</bdi> را با <bdi dir="ltr">Context Map</bdi> و <bdi dir="ltr">Ownership</bdi> دفاع کن.

می‌توان بیش از یک <bdi dir="ltr">Dependency</bdi> را نوشت:


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


این نمونه نیز پاسخ نهایی <bdi dir="ltr">Lab</bdi> نیست. <bdi dir="ltr">Named Interface</bdi>ها باید واقعاً در <bdi dir="ltr">Provider</bdi> تعریف شده باشند و نام‌ها از <bdi dir="ltr">Language</bdi> همان <bdi dir="ltr">Boundary</bdi> بیایند.

## <bdi dir="ltr">8. Function-first</bdi>، نه <bdi dir="ltr">Layer-first</bdi>

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


این ساختار همهٔ <bdi dir="ltr">Domain</bdi>ها را در <bdi dir="ltr">Layer</bdi>های افقی مخلوط می‌کند و دسترسی متقابل را آسان می‌سازد.

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


هر <bdi dir="ltr">Module</bdi> می‌تواند در داخل خودش <bdi dir="ltr">Layer</bdi> یا <bdi dir="ltr">Hexagonal structure</bdi> داشته باشد؛ آن موضوع <bdi dir="ltr">Sprint 02</bdi> است. ابتدا <bdi dir="ltr">Boundary</bdi> کسب‌وکاری، سپس ساختار داخلی.

## <bdi dir="ltr">9. Dependency Policy</bdi> از کجا می‌آید؟

برای هر <bdi dir="ltr">Dependency Candidate</bdi> این سؤال‌ها را پاسخ بده:

1. کدام <bdi dir="ltr">Use Case</bdi> واقعاً آن را نیاز دارد؟
2. <bdi dir="ltr">Provider</bdi> کدام <bdi dir="ltr">Fact/Capability</bdi> را مالک است؟
3. <bdi dir="ltr">Consumer</bdi> به <bdi dir="ltr">Reference</bdi>، <bdi dir="ltr">Snapshot</bdi>، <bdi dir="ltr">Query</bdi>، <bdi dir="ltr">Command</bdi> یا <bdi dir="ltr">Event</bdi> نیاز دارد؟
4. آیا <bdi dir="ltr">Dependency</bdi> به یک <bdi dir="ltr">Named Interface</bdi> کوچک محدود می‌شود؟
5. آیا <bdi dir="ltr">Event</bdi> یا <bdi dir="ltr">Translation</bdi> می‌تواند <bdi dir="ltr">Compile-time Coupling</bdi> را کمتر کند؟
6. اگر <bdi dir="ltr">Provider</bdi> تغییر کند، چه چیزی در <bdi dir="ltr">Consumer Recompile/Release</bdi> می‌شود؟
7. آیا <bdi dir="ltr">Dependency</bdi> معکوس یا <bdi dir="ltr">Cycle</bdi> ایجاد می‌کند؟

وجود یک فلش در <bdi dir="ltr">Sequence Diagram</bdi> به‌تنهایی مجوز <bdi dir="ltr">Import Type</bdi>های داخلی نیست.

## <bdi dir="ltr">10. Mapping</bdi> پیشنهادی اولیه، نه پاسخ قطعی

| <bdi dir="ltr">Problem-space hypothesis</bdi> | <bdi dir="ltr">Lab module</bdi> | نکته |
|---|---|---|
| <bdi dir="ltr">Party/Customer Identity and Relationship</bdi> | <bdi dir="ltr">`partycustomer`</bdi> | <bdi dir="ltr">Consumer</bdi>ها <bdi dir="ltr">Reference/Snapshot</bdi> می‌گیرند |
| <bdi dir="ltr">Product Catalog</bdi> + <bdi dir="ltr">Agreement</bdi> | <bdi dir="ltr">`productagreement`</bdi> | ممکن است بعداً به دو <bdi dir="ltr">Context/Module</bdi> تفکیک شود |
| <bdi dir="ltr">Deposit Account Servicing</bdi> | <bdi dir="ltr">`deposits`</bdi> | مانده و <bdi dir="ltr">Hold</bdi> عملیاتی را محصور می‌کند |
| <bdi dir="ltr">Loan Lifecycle/Servicing</bdi> | <bdi dir="ltr">`lending`</bdi> | مانده و برنامهٔ عملیاتی <bdi dir="ltr">Loan</bdi> |
| <bdi dir="ltr">Payment Order/Clearing/Settlement</bdi> | <bdi dir="ltr">`payments`</bdi> | <bdi dir="ltr">Channel</bdi> مالک <bdi dir="ltr">Payment State</bdi> نیست |
| <bdi dir="ltr">Journal/Subledger/GL</bdi> | <bdi dir="ltr">`accounting`</bdi> | <bdi dir="ltr">Operational Domain state</bdi> را مالک نمی‌شود |

<bdi dir="ltr">`Legal Orders`</bdi> در <bdi dir="ltr">Gate</bdi> یک <bdi dir="ltr">Context</bdi> خارجی/<bdi dir="ltr">near-core</bdi> است و الزاماً <bdi dir="ltr">Module</bdi> هفتم <bdi dir="ltr">Lab</bdi> در این <bdi dir="ltr">Sprint</bdi> نیست. <bdi dir="ltr">Contract</bdi> آن با <bdi dir="ltr">Deposits</bdi> باید در <bdi dir="ltr">Context Map</bdi> نشان داده شود.

## <bdi dir="ltr">11. Type</bdi>های مشترک و دام <bdi dir="ltr">`common`</bdi>

<bdi dir="ltr">Week 01</bdi> ممکن است <bdi dir="ltr">`Money`</bdi> و <bdi dir="ltr">Typed ID</bdi>ها را ساخته باشی. اکنون باید محل آن‌ها را آگاهانه بازبینی کنی.

### <bdi dir="ltr">Typed ID</bdi>

- <bdi dir="ltr">`CustomerId`</bdi> بهتر است <bdi dir="ltr">Contract type</bdi> متعلق به <bdi dir="ltr">Authority</bdi> یا <bdi dir="ltr">Published Reference</bdi> باشد.
- <bdi dir="ltr">`AccountId`</bdi> نباید با شمارهٔ حساب بانکی یا <bdi dir="ltr">Accounting Account ID</bdi> یکی فرض شود.
- <bdi dir="ltr">Import</bdi> کردن <bdi dir="ltr">Entity</bdi> کامل برای گرفتن <bdi dir="ltr">ID</bdi> ممنوع است.

### <bdi dir="ltr">Money</bdi>

مفهوم پایهٔ <bdi dir="ltr">Amount/Currency</bdi> می‌تواند بسیار کوچک و مشترک باشد، اما <bdi dir="ltr">Policy</bdi>های <bdi dir="ltr">Scale</bdi>، <bdi dir="ltr">Rounding</bdi> و <bdi dir="ltr">Sign</bdi> ممکن است <bdi dir="ltr">Contextual</bdi> باشند. سه گزینهٔ قابل بررسی:

1. <bdi dir="ltr">Value Object</bdi> مستقل در هر <bdi dir="ltr">Context</bdi> با <bdi dir="ltr">Semantic</bdi> خاص
2. <bdi dir="ltr">Shared Kernel</bdi> بسیار کوچک با <bdi dir="ltr">Governance</bdi> سخت‌گیرانه
3. <bdi dir="ltr">Boundary Contract type</bdi> و <bdi dir="ltr">Translation</bdi> به مدل داخلی

در این <bdi dir="ltr">Sprint</bdi> یک <bdi dir="ltr">Package</bdi> عمومی <bdi dir="ltr">`common`</bdi> نساز. ابتدا <bdi dir="ltr">Usage</bdi>، <bdi dir="ltr">Owner</bdi> و <bdi dir="ltr">Change coupling</bdi> را ثبت کن. <bdi dir="ltr">Shared Kernel</bdi> یک تصمیم صریح است، نه سطل <bdi dir="ltr">Type</bdi>های راحت.

## 12. برنامهٔ ۷۵ دقیقه‌ای اجرا

### دقیقهٔ 0 تا 5 — <bdi dir="ltr">Baseline</bdi>

از مسیر <bdi dir="ltr">`backend/banking-modulith`</bdi> اجرا کن:


</div>

<div dir="ltr" align="left">

~~~bash
mvn verify
~~~

</div>

<div dir="rtl" align="right">


نتیجه و <bdi dir="ltr">Commit</bdi> پایه را ثبت کن. اگر <bdi dir="ltr">Baseline</bdi> قرمز است، <bdi dir="ltr">Module work</bdi> را روی شکست قبلی بنا نکن.

### دقیقهٔ 5 تا 15 — <bdi dir="ltr">Dependency Plan</bdi>

[<bdi dir="ltr">Module Dependency Policy</bdi>](../artifacts/module-dependency-policy.md) را باز کن. برای شش <bdi dir="ltr">Module</bdi>، <bdi dir="ltr">Purpose</bdi> و <bdi dir="ltr">Provided/Required Interface</bdi> فرضی را بنویس. هنوز <bdi dir="ltr">Import</bdi> نساز.

### دقیقهٔ 15 تا 35 — <bdi dir="ltr">Base Packages</bdi>

شش <bdi dir="ltr">Direct Subpackage</bdi> و <bdi dir="ltr">`package-info.java`</bdi> بساز. در مرحلهٔ اول <bdi dir="ltr">`allowedDependencies = {}`</bdi> قرار بده تا هر <bdi dir="ltr">Dependency</bdi> بعدی آگاهانه اضافه شود.

### دقیقهٔ 35 تا 50 — <bdi dir="ltr">Public/Internal Boundary</bdi>

برای هر <bdi dir="ltr">Module:</bdi>

- یک <bdi dir="ltr">Public API</bdi> واقعی یا <bdi dir="ltr">Placeholder</bdi> مستندشدهٔ حداقلی در <bdi dir="ltr">Base Package</bdi>
- یک <bdi dir="ltr">`internal`</bdi> <bdi dir="ltr">package</bdi>
- بدون <bdi dir="ltr">Public Entity</bdi> مشترک

اگر هنوز <bdi dir="ltr">Use Case</bdi> مشخصی نداری، <bdi dir="ltr">`package-info.java`</bdi> و <bdi dir="ltr">Module description</bdi> کافی است؛ <bdi dir="ltr">API</bdi> مصنوعی نساز.

### دقیقهٔ 50 تا 60 — <bdi dir="ltr">Named Interfaces</bdi>

فقط <bdi dir="ltr">Named Interface</bdi>هایی را بساز که <bdi dir="ltr">Context Map</bdi> نیاز آن‌ها را نشان داده است. برای هر مورد دلیل و <bdi dir="ltr">Consumer</bdi> را در <bdi dir="ltr">Policy</bdi> ثبت کن.

### دقیقهٔ 60 تا 68 — <bdi dir="ltr">Allowed Dependencies</bdi>

<bdi dir="ltr">Dependency</bdi>های لازم را یکی‌یکی اضافه کن. اگر برای حل <bdi dir="ltr">Compile</bdi> به <bdi dir="ltr">Dependency</bdi> متقابل نیاز شد، توقف کن: احتمالاً <bdi dir="ltr">Contract</bdi> یا <bdi dir="ltr">Direction</bdi> مشکل دارد.

### دقیقهٔ 68 تا 75 — <bdi dir="ltr">Inspect and verify</bdi>

با <bdi dir="ltr">`ApplicationModules`</bdi> ساختار کشف‌شده را چاپ کن و سپس <bdi dir="ltr">Verification</bdi> را اجرا کن. تست رسمی روز ششم اضافه می‌شود، ولی امروز باید شش <bdi dir="ltr">Module</bdi> تشخیص داده شوند.

## 13. مشاهدهٔ مدل <bdi dir="ltr">Module</bdi>ها

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

- <bdi dir="ltr">Logical name</bdi>
- <bdi dir="ltr">Base package</bdi>
- <bdi dir="ltr">Spring beans</bdi>
- <bdi dir="ltr">Exposed types</bdi>
- <bdi dir="ltr">Direct dependencies</bdi>

صرف دیدن شش نام کافی نیست؛ <bdi dir="ltr">Public surface</bdi> و <bdi dir="ltr">Dependency</bdi>ها را نیز بررسی کن.

## 14. خطاهای رایج

### شش <bdi dir="ltr">Domain</bdi> مساوی شش <bdi dir="ltr">Microservice</bdi>

ما فقط شش <bdi dir="ltr">Module</bdi> داخل یک <bdi dir="ltr">Deployment</bdi> ساخته‌ایم. استخراج <bdi dir="ltr">Service</bdi> نیازمند <bdi dir="ltr">ADR</bdi>، <bdi dir="ltr">NFR</bdi>، <bdi dir="ltr">Team autonomy</bdi>، <bdi dir="ltr">Data</bdi> و <bdi dir="ltr">Operational evidence</bdi> است.

### <bdi dir="ltr">`internal`</bdi> فقط <bdi dir="ltr">Convention</bdi> است

اگر <bdi dir="ltr">Architecture Test</bdi> نباشد، <bdi dir="ltr">Developer</bdi> می‌تواند <bdi dir="ltr">Type</bdi> عمومی داخل <bdi dir="ltr">Subpackage</bdi> را <bdi dir="ltr">Import</bdi> کند. <bdi dir="ltr">Day 06</bdi> آن را <bdi dir="ltr">enforce</bdi> می‌کند.

### همه‌چیز <bdi dir="ltr">Public</bdi> در <bdi dir="ltr">Base Package</bdi>

هر <bdi dir="ltr">Public Type</bdi> در <bdi dir="ltr">Base Package</bdi> بخشی از <bdi dir="ltr">Provided Interface</bdi> است. <bdi dir="ltr">Surface</bdi> بزرگ <bdi dir="ltr">Coupling</bdi> را زیاد می‌کند.

### <bdi dir="ltr">Named Interface</bdi> برای هر <bdi dir="ltr">Folder</bdi>

<bdi dir="ltr">Named Interface</bdi> باید <bdi dir="ltr">Consumer</bdi> و <bdi dir="ltr">Contract</bdi> مشخص داشته باشد؛ نه اینکه <bdi dir="ltr">Encapsulation</bdi> را بی‌اثر کند.

### <bdi dir="ltr">Dependency</bdi> برای استفادهٔ دوباره از <bdi dir="ltr">Entity</bdi>

<bdi dir="ltr">Reuse</bdi> کد دلیل کافی برای وابستگی <bdi dir="ltr">Domain</bdi> نیست. <bdi dir="ltr">Contract</bdi>، <bdi dir="ltr">Reference</bdi> یا <bdi dir="ltr">Translation</bdi> را بررسی کن.

### <bdi dir="ltr">Cycle</bdi> را با <bdi dir="ltr">Event</bdi> پنهان‌کردن

اگر مدل و فرآیند ذاتاً دوری و مبهم است، عوض‌کردن <bdi dir="ltr">Method call</bdi> با <bdi dir="ltr">Event</bdi> نامفهوم مسئله را حل نمی‌کند. <bdi dir="ltr">Ownership</bdi> و <bdi dir="ltr">Direction</bdi> را دوباره تحلیل کن.

## 15. تمرین مستقل

[<bdi dir="ltr">Day 05 Exercise</bdi> — <bdi dir="ltr">Module Skeleton</bdi>](../exercises/day-05-module-skeleton.md) را اجرا کن. کد را خودت بنویس و <bdi dir="ltr">Output</bdi> ماژول‌ها و تصمیم <bdi dir="ltr">Dependency</bdi> را در <bdi dir="ltr">Workbook</bdi> ثبت کن.

## 16. معیار ارزیابی

| معیار | امتیاز |
|---|---:|
| شش <bdi dir="ltr">Module</bdi> بر اساس <bdi dir="ltr">Direct Subpackage</bdi> | ۲ |
| <bdi dir="ltr">API/Internal boundary</bdi> عمدی | ۲ |
| <bdi dir="ltr">Named Interface</bdi> محدود و معنادار | ۲ |
| <bdi dir="ltr">Allowed dependencies</bdi> مستدل و بدون <bdi dir="ltr">Cycle</bdi> | ۲ |
| <bdi dir="ltr">Policy</bdi> و <bdi dir="ltr">Traceability</bdi> به <bdi dir="ltr">Context Map</bdi> | ۲ |
| **جمع** | **۱۰** |

حد عبور: ۷ از ۱۰. استفاده از <bdi dir="ltr">Open Module</bdi> یا <bdi dir="ltr">Import</bdi> داخلی بدون <bdi dir="ltr">ADR</bdi> پذیرفته نیست.

## 17. آزمون خروج

پس از پایان کدنویسی، [<bdi dir="ltr">Day 05 Exit Ticket</bdi>](../quizzes/day-05-exit-ticket.md) را بدون مراجعه به درس پاسخ بده.

## 18. منابع اصلی

- [<bdi dir="ltr">Spring Modulith Fundamentals 2.1.0</bdi>](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- [<bdi dir="ltr">ApplicationModule Javadoc 2.1.0</bdi>](https://docs.spring.io/spring-modulith/docs/2.1.0/api/org/springframework/modulith/ApplicationModule.html)

<bdi dir="ltr">Syntax</bdi>های <bdi dir="ltr">`allowedDependencies`</bdi>، آرایهٔ خالی، <bdi dir="ltr">Closed Module</bdi> و <bdi dir="ltr">Named Interface</bdi> با مستند رسمی 2.1.0 تطبیق داده شده‌اند.

</div>
