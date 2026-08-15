# Day 03 Exercise — Context Map Relationships

- Timebox: 20 minutes
- Output: relationship table in `artifacts/context-map-template.md`

## Scenario slice

A murabaha loan has an executed agreement. Lending needs customer/KYC evidence, effective agreement terms, a credit to the customer's nominated deposit account, and financial recording of valid business facts.

## Required relationships

Analyze at least these six pairs:

1. Party & Customer ↔ Lending
2. Product/Agreement ↔ Lending
3. Deposits ↔ Lending
4. Lending ↔ Accounting
5. Deposits ↔ Accounting
6. Payments ↔ Deposits

Add `Legacy Deposits → new model` as a seventh relationship if you can defend an ACL.

## Required fields per relation

- Upstream
- Downstream
- model/decision that causes dependency
- Pattern
- Contract candidate
- data/fact shared
- Translation owner and location
- Failure impact
- Alternative Pattern and the Force that would make it preferable

## Two cautions

1. Command call direction is not automatically Upstream direction.
2. A pair may need more than one relationship if two contracts have different meanings.

## Diagram

After the table, draw a compact Context Map. Every edge must show direction and Pattern abbreviation. Transport is optional and must not be guessed.

## Acceptance

- at least six complete relationships
- no naked line
- at least one defended ACL
- at least one Published Language candidate
- at least one Open Question where organizational power is unknown

## Submission

Paste table and diagram link in [Week 02 Workbook](../submissions/week-02-workbook.md).
