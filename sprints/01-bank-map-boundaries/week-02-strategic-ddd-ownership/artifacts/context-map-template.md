<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Context Map v1</span> — <span dir="ltr">Template</span>

- <span dir="ltr">Version: 0.1</span>
- <span dir="ltr">Status: Not started</span>
- <span dir="ltr">Scope: Party/Customer</span>، <span dir="ltr">Product/Agreement</span>، <span dir="ltr">Deposits</span>، <span dir="ltr">Lending</span>، <span dir="ltr">Payments</span>، <span dir="ltr">Accounting</span> و <span dir="ltr">Context</span>های خارجی لازم

## <span dir="ltr">Context inventory</span>

| <span dir="ltr">Bounded Context</span> | <span dir="ltr">Model purpose</span> | <span dir="ltr">Ubiquitous Language</span> | <span dir="ltr">In scope</span> | <span dir="ltr">Out of scope</span> | <span dir="ltr">Team/owner hypothesis</span> | <span dir="ltr">Confidence</span> |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## <span dir="ltr">Relationships</span>

<span dir="ltr">For every relationship</span>, <span dir="ltr">record direction of model influence</span>—<span dir="ltr">not merely HTTP call direction.</span>

| <span dir="ltr">Upstream</span> | <span dir="ltr">Downstream</span> | <span dir="ltr">Pattern</span> | <span dir="ltr">Contract</span> | <span dir="ltr">Data/fact shared</span> | <span dir="ltr">Decision authority</span> | <span dir="ltr">Translation location</span> | <span dir="ltr">Failure impact</span> | <span dir="ltr">Evidence/status</span> |
|---|---|---|---|---|---|---|---|---|
|  |  | <span dir="ltr">Customer/Supplier</span> / <span dir="ltr">Conformist</span> / <span dir="ltr">ACL</span> / <span dir="ltr">OHS</span> + <span dir="ltr">Published Language</span> / <span dir="ltr">Partnership</span> / <span dir="ltr">Separate Ways</span> |  |  |  |  |  |  |

## <span dir="ltr">Diagram legend</span>

- <span dir="ltr">`U`</span> = <span dir="ltr">Upstream</span>
- <span dir="ltr">`D`</span> = <span dir="ltr">Downstream</span>
- <span dir="ltr">`C/S`</span> = <span dir="ltr">Customer/Supplier</span>
- <span dir="ltr">`CF`</span> = <span dir="ltr">Conformist</span>
- <span dir="ltr">`ACL`</span> = <span dir="ltr">Anticorruption Layer</span>
- <span dir="ltr">`OHS/PL`</span> = <span dir="ltr">Open Host Service</span> + <span dir="ltr">Published Language</span>
- <span dir="ltr">Solid line</span> = <span dir="ltr">synchronous or immediate dependency only if transport is already decided</span>
- <span dir="ltr">Dashed line</span> = <span dir="ltr">asynchronous only if transport is already decided</span>

<span dir="ltr">Transport line style is optional in Week 02. Direction</span>, <span dir="ltr">Pattern</span>, <span dir="ltr">Contract and Ownership are mandatory.</span>

## <span dir="ltr">Minimum map quality</span>

- <span dir="ltr">at least six Bounded Context candidates</span>
- <span dir="ltr">at least eight directional relationships</span>
- <span dir="ltr">no context named after a table or Controller</span>
- <span dir="ltr">no line without Pattern and Contract</span>
- <span dir="ltr">no shared Owner for the same semantic Fact</span>
- <span dir="ltr">at least one ACL decision defended</span>
- <span dir="ltr">at least one relationship explicitly marked</span> <span dir="ltr">`Pattern undecided`</span> <span dir="ltr">with an Open Question if evidence is insufficient</span>

## <span dir="ltr">Review questions</span>

1. آیا <span dir="ltr">Upstream</span> را با «کسی که <span dir="ltr">API</span> را صدا می‌زند» اشتباه کرده‌ای؟
2. آیا <span dir="ltr">Conformist</span> را فقط برای کم‌کردن کدنویسی انتخاب کرده‌ای؟
3. آیا <span dir="ltr">ACL</span> واقعاً از مدل <span dir="ltr">Core</span> محافظت می‌کند یا فقط <span dir="ltr">DTO Mapper</span> است؟
4. آیا <span dir="ltr">Published Language Version</span> و <span dir="ltr">Compatibility Policy</span> دارد؟
5. آیا یک رابطهٔ دوطرفه را بدون تفکیک دو <span dir="ltr">Dependency</span> متفاوت رسم کرده‌ای؟

</div>
