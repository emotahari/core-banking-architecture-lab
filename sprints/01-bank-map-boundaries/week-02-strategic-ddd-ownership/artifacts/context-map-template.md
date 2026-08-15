<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Context Map v1</bdi> — <bdi dir="ltr">Template</bdi>

- <bdi dir="ltr">Version: 0.1</bdi>
- <bdi dir="ltr">Status: Not started</bdi>
- <bdi dir="ltr">Scope: Party/Customer</bdi>، <bdi dir="ltr">Product/Agreement</bdi>، <bdi dir="ltr">Deposits</bdi>، <bdi dir="ltr">Lending</bdi>، <bdi dir="ltr">Payments</bdi>، <bdi dir="ltr">Accounting</bdi> و <bdi dir="ltr">Context</bdi>های خارجی لازم

## <bdi dir="ltr">Context inventory</bdi>

| <bdi dir="ltr">Bounded Context</bdi> | <bdi dir="ltr">Model purpose</bdi> | <bdi dir="ltr">Ubiquitous Language</bdi> | <bdi dir="ltr">In scope</bdi> | <bdi dir="ltr">Out of scope</bdi> | <bdi dir="ltr">Team/owner hypothesis</bdi> | <bdi dir="ltr">Confidence</bdi> |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## <bdi dir="ltr">Relationships</bdi>

<bdi dir="ltr">For every relationship</bdi>, <bdi dir="ltr">record direction of model influence</bdi>—<bdi dir="ltr">not merely HTTP call direction.</bdi>

| <bdi dir="ltr">Upstream</bdi> | <bdi dir="ltr">Downstream</bdi> | <bdi dir="ltr">Pattern</bdi> | <bdi dir="ltr">Contract</bdi> | <bdi dir="ltr">Data/fact shared</bdi> | <bdi dir="ltr">Decision authority</bdi> | <bdi dir="ltr">Translation location</bdi> | <bdi dir="ltr">Failure impact</bdi> | <bdi dir="ltr">Evidence/status</bdi> |
|---|---|---|---|---|---|---|---|---|
|  |  | <bdi dir="ltr">Customer/Supplier</bdi> / <bdi dir="ltr">Conformist</bdi> / <bdi dir="ltr">ACL</bdi> / <bdi dir="ltr">OHS</bdi> + <bdi dir="ltr">Published Language</bdi> / <bdi dir="ltr">Partnership</bdi> / <bdi dir="ltr">Separate Ways</bdi> |  |  |  |  |  |  |

## <bdi dir="ltr">Diagram legend</bdi>

- <bdi dir="ltr">`U`</bdi> = <bdi dir="ltr">Upstream</bdi>
- <bdi dir="ltr">`D`</bdi> = <bdi dir="ltr">Downstream</bdi>
- <bdi dir="ltr">`C/S`</bdi> = <bdi dir="ltr">Customer/Supplier</bdi>
- <bdi dir="ltr">`CF`</bdi> = <bdi dir="ltr">Conformist</bdi>
- <bdi dir="ltr">`ACL`</bdi> = <bdi dir="ltr">Anticorruption Layer</bdi>
- <bdi dir="ltr">`OHS/PL`</bdi> = <bdi dir="ltr">Open Host Service</bdi> + <bdi dir="ltr">Published Language</bdi>
- <bdi dir="ltr">Solid line</bdi> = <bdi dir="ltr">synchronous or immediate dependency only if transport is already decided</bdi>
- <bdi dir="ltr">Dashed line</bdi> = <bdi dir="ltr">asynchronous only if transport is already decided</bdi>

<bdi dir="ltr">Transport line style is optional in Week 02. Direction</bdi>, <bdi dir="ltr">Pattern</bdi>, <bdi dir="ltr">Contract and Ownership are mandatory.</bdi>

## <bdi dir="ltr">Minimum map quality</bdi>

- <bdi dir="ltr">at least six Bounded Context candidates</bdi>
- <bdi dir="ltr">at least eight directional relationships</bdi>
- <bdi dir="ltr">no context named after a table or Controller</bdi>
- <bdi dir="ltr">no line without Pattern and Contract</bdi>
- <bdi dir="ltr">no shared Owner for the same semantic Fact</bdi>
- <bdi dir="ltr">at least one ACL decision defended</bdi>
- <bdi dir="ltr">at least one relationship explicitly marked</bdi> <bdi dir="ltr">`Pattern undecided`</bdi> <bdi dir="ltr">with an Open Question if evidence is insufficient</bdi>

## <bdi dir="ltr">Review questions</bdi>

1. آیا <bdi dir="ltr">Upstream</bdi> را با «کسی که <bdi dir="ltr">API</bdi> را صدا می‌زند» اشتباه کرده‌ای؟
2. آیا <bdi dir="ltr">Conformist</bdi> را فقط برای کم‌کردن کدنویسی انتخاب کرده‌ای؟
3. آیا <bdi dir="ltr">ACL</bdi> واقعاً از مدل <bdi dir="ltr">Core</bdi> محافظت می‌کند یا فقط <bdi dir="ltr">DTO Mapper</bdi> است؟
4. آیا <bdi dir="ltr">Published Language Version</bdi> و <bdi dir="ltr">Compatibility Policy</bdi> دارد؟
5. آیا یک رابطهٔ دوطرفه را بدون تفکیک دو <bdi dir="ltr">Dependency</bdi> متفاوت رسم کرده‌ای؟

</div>
