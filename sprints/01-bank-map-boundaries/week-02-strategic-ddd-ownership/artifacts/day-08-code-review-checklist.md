<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 08</bdi> — <bdi dir="ltr">Code Review</bdi> و <bdi dir="ltr">Pattern Decision</bdi>

- <bdi dir="ltr">Reviewer:</bdi>
- <bdi dir="ltr">Branch/commit:</bdi>
- <bdi dir="ltr">Baseline test result:</bdi>
- <bdi dir="ltr">Final test result:</bdi>

## <bdi dir="ltr">1. Smell map</bdi>

| <bdi dir="ltr">Symbol/file</bdi> | <bdi dir="ltr">Smell</bdi> | <bdi dir="ltr">Change/defect risk</bdi> | <bdi dir="ltr">Smallest useful refactor</bdi> | <bdi dir="ltr">Status</bdi> |
|---|---|---|---|---|
|  |  |  |  |  |

## <bdi dir="ltr">2. Pattern decision</bdi>

- <bdi dir="ltr">Problem:</bdi>
- <bdi dir="ltr">Forces:</bdi>
- <bdi dir="ltr">Simplest no-pattern option:</bdi>
- <bdi dir="ltr">Pattern option:</bdi>
- <bdi dir="ltr">Decision:</bdi> <bdi dir="ltr">`switch`</bdi> / <bdi dir="ltr">Strategy</bdi> + <bdi dir="ltr">Registry</bdi> / <bdi dir="ltr">other</bdi>
- <bdi dir="ltr">Complexity added:</bdi>
- <bdi dir="ltr">Coupling reduced:</bdi>
- <bdi dir="ltr">Revisit trigger:</bdi>

## <bdi dir="ltr">3. Behavior preservation</bdi>

| <bdi dir="ltr">Behavior</bdi> | <bdi dir="ltr">Baseline test</bdi> | <bdi dir="ltr">Final test</bdi> | <bdi dir="ltr">Changed intentionally</bdi>? |
|---|---|---|---|
| <bdi dir="ltr">INTERNAL fee</bdi> |  |  | <bdi dir="ltr">No</bdi> |
| <bdi dir="ltr">ACH minimum</bdi> |  |  | <bdi dir="ltr">No</bdi> |
| <bdi dir="ltr">ACH percentage</bdi> |  |  | <bdi dir="ltr">No</bdi> |
| <bdi dir="ltr">ACH maximum</bdi> |  |  | <bdi dir="ltr">No</bdi> |
| <bdi dir="ltr">RTGS fixed fee</bdi> |  |  | <bdi dir="ltr">No</bdi> |
| <bdi dir="ltr">Preferred pricing</bdi> |  |  | <bdi dir="ltr">No</bdi> |
| <bdi dir="ltr">Invalid input</bdi> |  |  | <bdi dir="ltr">No</bdi> |
| <bdi dir="ltr">New edge case</bdi> |  |  |  |

## <bdi dir="ltr">4. Clean Code review</bdi>

- [ ] <bdi dir="ltr">Type/Method names express banking intent.</bdi>
- [ ] <bdi dir="ltr">Calculation does not parse raw String codes.</bdi>
- [ ] <bdi dir="ltr">Constants live beside the policy they describe.</bdi>
- [ ] <bdi dir="ltr">Flag argument has been replaced by an explicit concept.</bdi>
- [ ] <bdi dir="ltr">Error behavior is visible in tests.</bdi>
- [ ] <bdi dir="ltr">Tests assert behavior rather than private structure.</bdi>
- [ ] <bdi dir="ltr">No generic</bdi> <bdi dir="ltr">`common`</bdi>/<bdi dir="ltr">`utils`</bdi> <bdi dir="ltr">dumping ground was introduced.</bdi>
- [ ] <bdi dir="ltr">Pattern classes have real responsibility and are not pass-through wrappers.</bdi>
- [ ] <bdi dir="ltr">Refactor and business-rule change are not mixed.</bdi>

## <bdi dir="ltr">5. Diff review</bdi>

- <bdi dir="ltr">Files/classes added:</bdi>
- <bdi dir="ltr">Branches before/after:</bdi>
- <bdi dir="ltr">Most valuable simplification:</bdi>
- <bdi dir="ltr">Most questionable new abstraction:</bdi>
- <bdi dir="ltr">What I would delete if requirements became simpler:</bdi>

## <bdi dir="ltr">6. Remaining debt</bdi>

| <bdi dir="ltr">Debt/unknown</bdi> | <bdi dir="ltr">Why not solved now</bdi> | <bdi dir="ltr">Risk</bdi> | <bdi dir="ltr">Revisit trigger</bdi> |
|---|---|---|---|
|  |  |  |  |

## <bdi dir="ltr">7. Verdict</bdi>

- <bdi dir="ltr">Score</bdi> / 10:
- <bdi dir="ltr">Accept</bdi> / <bdi dir="ltr">Revise:</bdi>
- <bdi dir="ltr">One-sentence reason:</bdi>

</div>
