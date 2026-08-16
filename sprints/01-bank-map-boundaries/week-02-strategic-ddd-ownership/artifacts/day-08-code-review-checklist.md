<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 08</span> — <span dir="ltr">Code Review</span> و <span dir="ltr">Pattern Decision</span>

- <span dir="ltr">Reviewer:</span>
- <span dir="ltr">Branch/commit:</span>
- <span dir="ltr">Baseline test result:</span>
- <span dir="ltr">Final test result:</span>

## <span dir="ltr">1. Smell map</span>

| <span dir="ltr">Symbol/file</span> | <span dir="ltr">Smell</span> | <span dir="ltr">Change/defect risk</span> | <span dir="ltr">Smallest useful refactor</span> | <span dir="ltr">Status</span> |
|---|---|---|---|---|
|  |  |  |  |  |

## <span dir="ltr">2. Pattern decision</span>

- <span dir="ltr">Problem:</span>
- <span dir="ltr">Forces:</span>
- <span dir="ltr">Simplest no-pattern option:</span>
- <span dir="ltr">Pattern option:</span>
- <span dir="ltr">Decision:</span> <span dir="ltr">`switch`</span> / <span dir="ltr">Strategy</span> + <span dir="ltr">Registry</span> / <span dir="ltr">other</span>
- <span dir="ltr">Complexity added:</span>
- <span dir="ltr">Coupling reduced:</span>
- <span dir="ltr">Revisit trigger:</span>

## <span dir="ltr">3. Behavior preservation</span>

| <span dir="ltr">Behavior</span> | <span dir="ltr">Baseline test</span> | <span dir="ltr">Final test</span> | <span dir="ltr">Changed intentionally</span>? |
|---|---|---|---|
| <span dir="ltr">INTERNAL fee</span> |  |  | <span dir="ltr">No</span> |
| <span dir="ltr">ACH minimum</span> |  |  | <span dir="ltr">No</span> |
| <span dir="ltr">ACH percentage</span> |  |  | <span dir="ltr">No</span> |
| <span dir="ltr">ACH maximum</span> |  |  | <span dir="ltr">No</span> |
| <span dir="ltr">RTGS fixed fee</span> |  |  | <span dir="ltr">No</span> |
| <span dir="ltr">Preferred pricing</span> |  |  | <span dir="ltr">No</span> |
| <span dir="ltr">Invalid input</span> |  |  | <span dir="ltr">No</span> |
| <span dir="ltr">New edge case</span> |  |  |  |

## <span dir="ltr">4. Clean Code review</span>

- [ ] <span dir="ltr">Type/Method names express banking intent.</span>
- [ ] <span dir="ltr">Calculation does not parse raw String codes.</span>
- [ ] <span dir="ltr">Constants live beside the policy they describe.</span>
- [ ] <span dir="ltr">Flag argument has been replaced by an explicit concept.</span>
- [ ] <span dir="ltr">Error behavior is visible in tests.</span>
- [ ] <span dir="ltr">Tests assert behavior rather than private structure.</span>
- [ ] <span dir="ltr">No generic</span> <span dir="ltr">`common`</span>/<span dir="ltr">`utils`</span> <span dir="ltr">dumping ground was introduced.</span>
- [ ] <span dir="ltr">Pattern classes have real responsibility and are not pass-through wrappers.</span>
- [ ] <span dir="ltr">Refactor and business-rule change are not mixed.</span>

## <span dir="ltr">5. Diff review</span>

- <span dir="ltr">Files/classes added:</span>
- <span dir="ltr">Branches before/after:</span>
- <span dir="ltr">Most valuable simplification:</span>
- <span dir="ltr">Most questionable new abstraction:</span>
- <span dir="ltr">What I would delete if requirements became simpler:</span>

## <span dir="ltr">6. Remaining debt</span>

| <span dir="ltr">Debt/unknown</span> | <span dir="ltr">Why not solved now</span> | <span dir="ltr">Risk</span> | <span dir="ltr">Revisit trigger</span> |
|---|---|---|---|
|  |  |  |  |

## <span dir="ltr">7. Verdict</span>

- <span dir="ltr">Score</span> / 10:
- <span dir="ltr">Accept</span> / <span dir="ltr">Revise:</span>
- <span dir="ltr">One-sentence reason:</span>

</div>
