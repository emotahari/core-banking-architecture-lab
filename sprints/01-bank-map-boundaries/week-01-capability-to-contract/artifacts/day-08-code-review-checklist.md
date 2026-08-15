# Day 08 Artifact — Code Review Checklist

- Baseline commit/state:
- Refactored commit/state:
- Reviewer/date:

## Baseline evidence

- Command:
- Test count/result:
- Full `mvn verify` result:

## Smell map

| Symbol | Smell | Concrete change/defect risk | Smallest move | Done? |
|---|---|---|---|---:|
|  |  |  |  |  |

## Refactor checkpoints

| # | Change | Test command/result | Behavior preserved? | Notes |
|---:|---|---|---:|---|
| 1 | AccountId |  |  |  |
| 2 | CustomerId/BranchId |  |  |  |
| 3 | Money |  |  |  |
| 4 | Creation API |  |  |  |

## Pattern decision

- Problem:
- Forces:
- Simplest no-pattern option:
- Options considered:
- Decision:
- Coupling reduced:
- Complexity added:
- Revisit trigger:

## Money decisions

- Signed/positive policy and owner:
- Equality/scale policy:
- Rounding policy:
- Currency representation:

## Safety

- [ ] Refactor و Rule change جدا شده‌اند.
- [ ] حداقل یک Edge Test تازه وجود دارد.
- [ ] `equals/hashCode` سازگارند.
- [ ] `double` یا Rounding پنهان وجود ندارد.
- [ ] Framework annotation وارد Value Object نشده است.
- [ ] Base hierarchy/Factory نمایشی اضافه نشده است.
- [ ] `mvn verify` نهایی سبز است.

## Self-review

- Most valuable improvement:
- Most questionable abstraction:
- Debt/unknown left:
- What I would remove if only one use case existed:

