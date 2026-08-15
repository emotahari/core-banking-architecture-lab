# Day 08 — Code Review و Pattern Decision

- Reviewer:
- Branch/commit:
- Baseline test result:
- Final test result:

## 1. Smell map

| Symbol/file | Smell | Change/defect risk | Smallest useful refactor | Status |
|---|---|---|---|---|
|  |  |  |  |  |

## 2. Pattern decision

- Problem:
- Forces:
- Simplest no-pattern option:
- Pattern option:
- Decision: `switch` / Strategy + Registry / other
- Complexity added:
- Coupling reduced:
- Revisit trigger:

## 3. Behavior preservation

| Behavior | Baseline test | Final test | Changed intentionally? |
|---|---|---|---|
| INTERNAL fee |  |  | No |
| ACH minimum |  |  | No |
| ACH percentage |  |  | No |
| ACH maximum |  |  | No |
| RTGS fixed fee |  |  | No |
| Preferred pricing |  |  | No |
| Invalid input |  |  | No |
| New edge case |  |  |  |

## 4. Clean Code review

- [ ] Type/Method names express banking intent.
- [ ] Calculation does not parse raw String codes.
- [ ] Constants live beside the policy they describe.
- [ ] Flag argument has been replaced by an explicit concept.
- [ ] Error behavior is visible in tests.
- [ ] Tests assert behavior rather than private structure.
- [ ] No generic `common`/`utils` dumping ground was introduced.
- [ ] Pattern classes have real responsibility and are not pass-through wrappers.
- [ ] Refactor and business-rule change are not mixed.

## 5. Diff review

- Files/classes added:
- Branches before/after:
- Most valuable simplification:
- Most questionable new abstraction:
- What I would delete if requirements became simpler:

## 6. Remaining debt

| Debt/unknown | Why not solved now | Risk | Revisit trigger |
|---|---|---|---|
|  |  |  |  |

## 7. Verdict

- Score / 10:
- Accept / Revise:
- One-sentence reason:
