# Context Map v1 — Template

- Version: 0.1
- Status: Not started
- Scope: Party/Customer، Product/Agreement، Deposits، Lending، Payments، Accounting و Contextهای خارجی لازم

## Context inventory

| Bounded Context | Model purpose | Ubiquitous Language | In scope | Out of scope | Team/owner hypothesis | Confidence |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Relationships

For every relationship, record direction of model influence—not merely HTTP call direction.

| Upstream | Downstream | Pattern | Contract | Data/fact shared | Decision authority | Translation location | Failure impact | Evidence/status |
|---|---|---|---|---|---|---|---|---|
|  |  | Customer/Supplier / Conformist / ACL / OHS + Published Language / Partnership / Separate Ways |  |  |  |  |  |  |

## Diagram legend

- `U` = Upstream
- `D` = Downstream
- `C/S` = Customer/Supplier
- `CF` = Conformist
- `ACL` = Anticorruption Layer
- `OHS/PL` = Open Host Service + Published Language
- Solid line = synchronous or immediate dependency only if transport is already decided
- Dashed line = asynchronous only if transport is already decided

Transport line style is optional in Week 02. Direction, Pattern, Contract and Ownership are mandatory.

## Minimum map quality

- at least six Bounded Context candidates
- at least eight directional relationships
- no context named after a table or Controller
- no line without Pattern and Contract
- no shared Owner for the same semantic Fact
- at least one ACL decision defended
- at least one relationship explicitly marked `Pattern undecided` with an Open Question if evidence is insufficient

## Review questions

1. آیا Upstream را با «کسی که API را صدا می‌زند» اشتباه کرده‌ای؟
2. آیا Conformist را فقط برای کم‌کردن کدنویسی انتخاب کرده‌ای؟
3. آیا ACL واقعاً از مدل Core محافظت می‌کند یا فقط DTO Mapper است؟
4. آیا Published Language Version و Compatibility Policy دارد؟
5. آیا یک رابطهٔ دوطرفه را بدون تفکیک دو Dependency متفاوت رسم کرده‌ای؟
