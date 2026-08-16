<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Day 08 Artifact</span> — <span dir="ltr">Code Review Checklist</span>

- <span dir="ltr">Baseline commit/state:</span>
- <span dir="ltr">Refactored commit/state:</span>
- <span dir="ltr">Reviewer/date:</span>

## <span dir="ltr">Baseline evidence</span>

- <span dir="ltr">Command:</span>
- <span dir="ltr">Test count/result:</span>
- <span dir="ltr">Full</span> <span dir="ltr">`mvn verify`</span> <span dir="ltr">result:</span>

## <span dir="ltr">Smell map</span>

| <span dir="ltr">Symbol</span> | <span dir="ltr">Smell</span> | <span dir="ltr">Concrete change/defect risk</span> | <span dir="ltr">Smallest move</span> | <span dir="ltr">Done</span>? |
|---|---|---|---|---:|
|  |  |  |  |  |

## <span dir="ltr">Refactor checkpoints</span>

| # | <span dir="ltr">Change</span> | <span dir="ltr">Test command/result</span> | <span dir="ltr">Behavior preserved</span>? | <span dir="ltr">Notes</span> |
|---:|---|---|---:|---|
| 1 | <span dir="ltr">AccountId</span> |  |  |  |
| 2 | <span dir="ltr">CustomerId/BranchId</span> |  |  |  |
| 3 | <span dir="ltr">Money</span> |  |  |  |
| 4 | <span dir="ltr">Creation API</span> |  |  |  |

## <span dir="ltr">Pattern decision</span>

- <span dir="ltr">Problem:</span>
- <span dir="ltr">Forces:</span>
- <span dir="ltr">Simplest no-pattern option:</span>
- <span dir="ltr">Options considered:</span>
- <span dir="ltr">Decision:</span>
- <span dir="ltr">Coupling reduced:</span>
- <span dir="ltr">Complexity added:</span>
- <span dir="ltr">Revisit trigger:</span>

## <span dir="ltr">Money decisions</span>

- <span dir="ltr">Signed/positive policy and owner:</span>
- <span dir="ltr">Equality/scale policy:</span>
- <span dir="ltr">Rounding policy:</span>
- <span dir="ltr">Currency representation:</span>

## <span dir="ltr">Safety</span>

- [ ] <span dir="ltr">Refactor</span> و <span dir="ltr">Rule change</span> جدا شده‌اند.
- [ ] حداقل یک <span dir="ltr">Edge Test</span> تازه وجود دارد.
- [ ] <span dir="ltr">`equals/hashCode`</span> سازگارند.
- [ ] <span dir="ltr">`double`</span> یا <span dir="ltr">Rounding</span> پنهان وجود ندارد.
- [ ] <span dir="ltr">Framework annotation</span> وارد <span dir="ltr">Value Object</span> نشده است.
- [ ] <span dir="ltr">Base hierarchy/Factory</span> نمایشی اضافه نشده است.
- [ ] <span dir="ltr">`mvn verify`</span> نهایی سبز است.

## <span dir="ltr">Self-review</span>

- <span dir="ltr">Most valuable improvement:</span>
- <span dir="ltr">Most questionable abstraction:</span>
- <span dir="ltr">Debt/unknown left:</span>
- <span dir="ltr">What I would remove if only one use case existed:</span>


</div>
