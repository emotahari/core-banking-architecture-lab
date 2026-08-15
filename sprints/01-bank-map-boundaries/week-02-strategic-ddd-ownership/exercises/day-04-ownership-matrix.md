# Day 04 Exercise — Data and Decision Ownership Matrix

- Timebox: 20 minutes
- Output: `artifacts/ownership-matrix-template.md`

## Part A — Semantic facts

Complete at least these 12 rows:

1. Party identity
2. KYC status/evidence
3. Product version
4. Executed agreement terms
5. Loan grant state
6. Operational principal outstanding
7. Repayment schedule/state
8. Deposit credit transaction state
9. Available deposit balance
10. Operational deposit hold
11. Journal Entry
12. GL/Subledger balance

For each row identify:

- exactly one Authority
- role of every other relevant Context
- Freshness/history rule
- Reconciliation owner
- one forbidden writer

## Part B — Decisions

Analyze at least five decisions:

- Is KYC valid?
- Is borrower eligible for this loan/product?
- Can the deposit accept this credit now?
- Has the loan been granted?
- Which accounting rule/template applies to a valid business fact?

Separate Trigger Owner, Decision Authority and State Owner.

## Part C — Balance challenge

Explain in a maximum of 150 words why `Lending Principal Outstanding` and `Accounting Receivable Balance` can both be valid without shared ownership. Include expected reconciliation.

## Part D — Copy challenge

Give one banking example for each:

- Reference
- Snapshot
- Cache
- Projection
- Derived data

## Critical checks

- exactly one Authority per semantic row
- Product current version is not used to silently mutate past agreement terms
- Accounting does not own operational deposit/loan decisions
- Orchestrator owns only process state

## Submission

Record raw answers in [Week 02 Workbook](../submissions/week-02-workbook.md).
