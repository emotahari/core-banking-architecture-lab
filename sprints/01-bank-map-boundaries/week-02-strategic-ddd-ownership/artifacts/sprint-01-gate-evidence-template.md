# Sprint 01 Gate Evidence — Legal Deposit Hold

- Status: Not started
- Timebox: 20 minutes preparation + maximum 10 minutes defense
- Rule: do not start from table, Controller, existing system or BIAN Service Domain.

## 1. Problem statement in your words


## 2. Traceability chain

| Level | Decision | Reason/evidence | Owner |
|---|---|---|---|
| Capability |  |  |  |
| Domain/Subdomain |  |  |  |
| Bounded Context |  |  |  |
| Module/Service candidate |  |  |  |
| Use case |  |  |  |
| Command/Query |  |  |  |
| API/Event |  |  |  |

## 3. Ubiquitous Language

| Term | Legal context meaning | Deposits context meaning | Translation/contract |
|---|---|---|---|
| Order |  |  |  |
| Restriction/Hold |  |  |  |
| Effective date |  |  |  |
| Amount/scope |  |  |  |

## 4. Ownership

| Fact/Decision | Authority | Who may keep a copy? | Who must not change it? |
|---|---|---|---|
| Order text/reference |  |  |  |
| Order validity/lifecycle |  |  |  |
| Target deposit resolution |  |  |  |
| Operational hold |  |  |  |
| Available balance |  |  |  |
| Accounting/control record |  |  |  |

## 5. Context Map relation

| Upstream | Downstream | Pattern | Command/query/event | Translation | Failure effect |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 6. Module evidence

- Module that receives operational hold request:
- Public interface:
- Internal implementation hidden:
- Allowed dependency:
- Verification test:

## 7. Failure questions

- duplicate request:
- stale/revoked order:
- account cannot accept hold:
- success with lost response:
- reconciliation authority:

Detailed distributed failure design is not required yet; ownership and expected outcome are required.

## 8. Assumptions and open questions

| ID | Type | Statement | Risk | Validation owner |
|---|---|---|---|---|
|  |  |  |  |  |

## 9. Defense summary

Write a maximum 200-word explanation that can be spoken without reading the tables.
