# Domain Dossier — Template

- Domain/Context:
- Version:
- Status: Draft / Review / Accepted
- Author:
- Business owner hypothesis:
- Team owner hypothesis:

Every claim must be marked as `Fact`, `Hypothesis`, `Decision`, or `Open Question`.

## 1. Purpose and outcomes

- Why this domain/context exists
- Business outcomes and KPIs
- Capabilities it enables

## 2. Scope boundary

### In scope

-

### Out of scope

-

### Boundary evidence

- language difference
- distinct rules/invariants
- lifecycle/change cadence
- authority/ownership
- team or regulatory constraint

## 3. Strategic classification

- Candidate subdomains:
- Core / Supporting / Generic per subdomain:
- Forces and evidence:
- Revisit trigger:

## 4. Ubiquitous Language

| Term | Exact meaning here | Example | Not the same as | Owner of definition |
|---|---|---|---|---|
|  |  |  |  |  |

## 5. Model and rules

- Aggregate candidates
- State machines
- Invariants
- Domain policies
- Domain events

These are hypotheses in Sprint 01; Tactical DDD starts in Sprint 02.

## 6. Data and decision ownership

| Fact/Decision | Owns? | If not, authority | Local copy type | Freshness/history | Reconciliation |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 7. Must not own

- State or decisions explicitly forbidden in this context
- Why ownership elsewhere is required

## 8. Use cases and contracts

| Use case | Command/Query | API/Message candidate | Result/Event | Idempotency/error semantics |
|---|---|---|---|---|
|  |  |  |  |  |

## 9. Context relationships

| Other context | Upstream/Downstream | Pattern | Contract | Translation | Failure impact |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 10. Consistency and failure hypotheses

- local transaction boundary
- cross-context consistency expectation
- duplicate/retry concern
- reconciliation/manual repair

Do not design Saga or Outbox here; only capture requirements and open questions.

## 11. Module/service hypothesis

- Initial Spring Modulith module:
- Public API / Named Interfaces:
- Internal packages:
- Allowed dependencies:
- Why this is not yet a Microservice decision:

## 12. NFR and governance

- security/privacy
- auditability
- latency/availability
- volume
- regulatory requirements
- team and change cadence

## Evidence log

| ID | Type | Claim | Evidence/source | Confidence | Validation action | Status |
|---|---|---|---|---|---|---|
| E-01 | Hypothesis |  |  | Low/Medium/High |  | Open |
