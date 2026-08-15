<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Day 08 Artifact</bdi> — <bdi dir="ltr">Code Review Checklist</bdi>

- <bdi dir="ltr">Baseline commit/state:</bdi>
- <bdi dir="ltr">Refactored commit/state:</bdi>
- <bdi dir="ltr">Reviewer/date:</bdi>

## <bdi dir="ltr">Baseline evidence</bdi>

- <bdi dir="ltr">Command:</bdi>
- <bdi dir="ltr">Test count/result:</bdi>
- <bdi dir="ltr">Full</bdi> <bdi dir="ltr">`mvn verify`</bdi> <bdi dir="ltr">result:</bdi>

## <bdi dir="ltr">Smell map</bdi>

| <bdi dir="ltr">Symbol</bdi> | <bdi dir="ltr">Smell</bdi> | <bdi dir="ltr">Concrete change/defect risk</bdi> | <bdi dir="ltr">Smallest move</bdi> | <bdi dir="ltr">Done</bdi>? |
|---|---|---|---|---:|
|  |  |  |  |  |

## <bdi dir="ltr">Refactor checkpoints</bdi>

| # | <bdi dir="ltr">Change</bdi> | <bdi dir="ltr">Test command/result</bdi> | <bdi dir="ltr">Behavior preserved</bdi>? | <bdi dir="ltr">Notes</bdi> |
|---:|---|---|---:|---|
| 1 | <bdi dir="ltr">AccountId</bdi> |  |  |  |
| 2 | <bdi dir="ltr">CustomerId/BranchId</bdi> |  |  |  |
| 3 | <bdi dir="ltr">Money</bdi> |  |  |  |
| 4 | <bdi dir="ltr">Creation API</bdi> |  |  |  |

## <bdi dir="ltr">Pattern decision</bdi>

- <bdi dir="ltr">Problem:</bdi>
- <bdi dir="ltr">Forces:</bdi>
- <bdi dir="ltr">Simplest no-pattern option:</bdi>
- <bdi dir="ltr">Options considered:</bdi>
- <bdi dir="ltr">Decision:</bdi>
- <bdi dir="ltr">Coupling reduced:</bdi>
- <bdi dir="ltr">Complexity added:</bdi>
- <bdi dir="ltr">Revisit trigger:</bdi>

## <bdi dir="ltr">Money decisions</bdi>

- <bdi dir="ltr">Signed/positive policy and owner:</bdi>
- <bdi dir="ltr">Equality/scale policy:</bdi>
- <bdi dir="ltr">Rounding policy:</bdi>
- <bdi dir="ltr">Currency representation:</bdi>

## <bdi dir="ltr">Safety</bdi>

- [ ] <bdi dir="ltr">Refactor</bdi> و <bdi dir="ltr">Rule change</bdi> جدا شده‌اند.
- [ ] حداقل یک <bdi dir="ltr">Edge Test</bdi> تازه وجود دارد.
- [ ] <bdi dir="ltr">`equals/hashCode`</bdi> سازگارند.
- [ ] <bdi dir="ltr">`double`</bdi> یا <bdi dir="ltr">Rounding</bdi> پنهان وجود ندارد.
- [ ] <bdi dir="ltr">Framework annotation</bdi> وارد <bdi dir="ltr">Value Object</bdi> نشده است.
- [ ] <bdi dir="ltr">Base hierarchy/Factory</bdi> نمایشی اضافه نشده است.
- [ ] <bdi dir="ltr">`mvn verify`</bdi> نهایی سبز است.

## <bdi dir="ltr">Self-review</bdi>

- <bdi dir="ltr">Most valuable improvement:</bdi>
- <bdi dir="ltr">Most questionable abstraction:</bdi>
- <bdi dir="ltr">Debt/unknown left:</bdi>
- <bdi dir="ltr">What I would remove if only one use case existed:</bdi>


</div>
