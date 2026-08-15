# Day 02 Exercise — Language Conflicts and Boundary Hypotheses

- Timebox: 15 minutes
- Output: `artifacts/language-conflicts-working-draft.md`

## Part A — Five ambiguous terms

Choose at least five:

- Customer
- Account
- Product
- Agreement/Contract
- Balance
- Transaction
- Hold/Block
- Posting
- Settlement

For each term compare at least two Context candidates and answer:

1. Exact meaning in each Context
2. Lifecycle difference
3. Invariant/decision difference
4. Identity difference
5. Translation needed at the boundary

## Part B — Two Boundary Hypotheses

Write two hypotheses in this form:

> Because of [language/rule/lifecycle/authority/change] differences, we hypothesize [A] and [B] are separate Bounded Contexts. We will validate this with [evidence/action]. Counter-evidence is [X].

At least one hypothesis must concern `Product Definition` versus `Executed Agreement` or another pair with historical Snapshot semantics.

## Part C — False positive

Find one terminology difference that may be only a Synonym and not enough to create a new Context. Explain what additional evidence you need.

## Acceptance

- no Context named after a table or CRUD operation
- each hypothesis uses at least two Forces
- Context is not automatically mapped to a Microservice
- counter-evidence is explicit

## Submission

Record raw answers in [Week 02 Workbook](../submissions/week-02-workbook.md).
