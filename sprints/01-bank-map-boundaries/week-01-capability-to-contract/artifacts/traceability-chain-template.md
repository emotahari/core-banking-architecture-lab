# Day 03 Artifact — Capability-to-Contract Traceability Chain

- Scenario:
- Version:
- Status: Working / Reviewed / Accepted
- Author/date:

## Trigger and outcome

- Trigger:
- Expected business outcome:
- Safety property:
- Out of scope:

## Forward chain

| Step | Element | Type | Owner/authority | Evidence | Boundary rule | Open question |
|---:|---|---|---|---|---|---|
| 1 |  | Outcome/Driver |  |  |  |  |
| 2 |  | Capability |  |  |  |  |
| 3 |  | Domain/Subdomain |  |  |  |  |
| 4 |  | Bounded Context hypothesis |  |  |  |  |
| 5 |  | Module/Service candidate |  |  |  |  |
| 6 |  | Use Case |  |  |  |  |
| 7 |  | Command/Query |  |  |  |  |
| 8 |  | Result/Event |  |  |  |  |

## Contract card

- Contract name:
- Type: Command / Query / Event
- Business intent/fact:
- Producer/owner:
- Consumer role:
- Preconditions:
- Required data and meaning:
- Success outcome:
- Business rejections:
- Correlation/idempotency candidate:
- Sensitive data:
- Versioning concern:
- Unknown:

## Authority matrix

| Fact/decision | Single authority | Copy/projection elsewhere | Forbidden writer |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Reverse trace

```text
contract → use case → context → capability → outcome
```

## Review checks

- [ ] هیچ پرش Table/System به Service وجود ندارد.
- [ ] Command و Event از نظر Intent/Fact جدا هستند.
- [ ] Service candidate تصمیم Deployment اعلام نشده است.
- [ ] هر Fact یک Authority دارد.
- [ ] Unknownها صریح‌اند.

