# Week 01 Workbook — Student Submission

- Student:
- Start date:
- Status: Day 01 attempt exists; Day 02 not started
- Rule: پاسخ خام را پاک نکن؛ Review و Revision را زیر آن اضافه کن.

## Evidence convention

- `RAW`: پاسخ مستقل پیش از Review
- `REVIEW`: بازخورد استاد
- `REVISION`: پاسخ اصلاح‌شده پس از فهم بازخورد
- `EVIDENCE`: فایل، خروجی تست یا Commit
- `OPEN`: پرسش حل‌نشده

دادهٔ واقعی مشتری، Credential، کد محرمانهٔ بانک یا جزئیات Production را وارد نکن.

---

## Day 01 — Architecture Language and Baseline

- Lesson: [Day 01](../lessons/day-01-architecture-language-fa.md)
- Exercise: [Baseline](../exercises/day-01-baseline.md)
- Existing response: [Day 01 Submission](day-01-baseline-response.md)
- Existing quiz/answers: [Exit Ticket](../quizzes/day-01-exit-ticket.md)

### REVIEW


### REVISION — پاسخ خام قبلی پاک نشود


### OPEN


---

## Day 02 — Capability Distinctions

- Lesson: [Day 02](../lessons/day-02-capability-distinction-fa.md)
- Exercise: [Distinction Matrix](../exercises/day-02-capability-distinction.md)
- Exit Ticket: [Quiz](../quizzes/day-02-exit-ticket.md)

### RAW — Exercise


### RAW — Exit Ticket

1.
2.
3.
4.
5.
6.

### REVIEW / REVISION / OPEN


---

## Day 03 — Traceability Chains

- Lesson: [Day 03](../lessons/day-03-traceability-chain-fa.md)
- Exercise: [Two Chains](../exercises/day-03-traceability-chain.md)
- Exit Ticket: [Quiz](../quizzes/day-03-exit-ticket.md)

### RAW — Legal hold chain


### RAW — Loan disbursement chain


### RAW — Exit Ticket

1.
2.
3.
4.
5.
6.
7.

### REVIEW / REVISION / OPEN


---

## Day 04 — Coupling and Boundary Review

- Lesson: [Day 04](../lessons/day-04-design-forces-boundary-fa.md)
- Exercise: [Coupling Review](../exercises/day-04-coupling-review.md)
- Exit Ticket: [Quiz](../quizzes/day-04-exit-ticket.md)

### RAW — Coupling map and redesign


### RAW — Exit Ticket

1.
2.
3.
4.
5.
6.
7.

### REVIEW / REVISION / OPEN


---

## Day 05 — Capability Map and BIAN

- Lesson: [Day 05](../lessons/day-05-banking-capability-map-bian-fa.md)
- Exercise: [Map + Gap Check](../exercises/day-05-capability-map-bian-gap-check.md)
- Exit Ticket: [Quiz](../quizzes/day-05-exit-ticket.md)

### EVIDENCE — Capability Map v1

- path/commit:
- version/status:
- largest change from draft:

### RAW — BIAN Gap Check findings

- useful match:
- partial match:
- false friend:
- gap in our map:
- local gap/not applicable:

### RAW — Exit Ticket

1.
2.
3.
4.
5.
6.

### REVIEW / REVISION / OPEN


---

## Day 06 — Value Objects and Pipeline

- Lesson: [Day 06](../lessons/day-06-value-objects-pipeline-fa.md)
- Exercise: [Money and Typed IDs](../exercises/day-06-value-objects.md)
- Exit Ticket: [Quiz](../quizzes/day-06-exit-ticket.md)

### RAW — Design decisions

- Money signed/positive:
- equality/scale:
- rounding policy:
- ID format assumptions:
- constructor/static factory:

### EVIDENCE

- baseline `mvn verify`:
- targeted tests:
- final `mvn verify`:
- branch/commit:

### RAW — Exit Ticket

1.
2.
3.
4.
5.
6.
7.
8.

### REVIEW / REVISION / OPEN


---

## Day 07 — Core Week Defense

- Lesson: [Day 07](../lessons/day-07-week-defense-fa.md)
- Exercise: [Defense](../exercises/day-07-week-defense.md)
- Report: [Template](../artifacts/week-01-report-template.md)

### EVIDENCE — Gate

- evidence index:
- duration:
- self-score:
- instructor score:
- critical errors:
- remediation:

### REVIEW / REVISION / OPEN


---

## Day 08 — Code Craft: Primitive to Value Object

- Lesson: [Clean Code + Value Object Refactoring](../lessons/day-08-clean-code-value-object-refactoring-fa.md)
- Exercise: [Runnable Kata](../exercises/day-08-money-refactoring-kata.md)
- Review: [Checklist](../artifacts/day-08-code-review-checklist.md)
- Exit Ticket: [Quiz](../quizzes/day-08-exit-ticket.md)

### EVIDENCE — Baseline

- command/result:
- test count:
- branch/commit:

### RAW — Smell Map


### RAW — Pattern Decision

- Problem:
- Forces:
- Simplest alternative:
- Options:
- Decision:
- Cost:
- Revisit trigger:

### EVIDENCE — Checkpoints and Edge Test


### EVIDENCE — Final `mvn verify`


### RAW — Exit Ticket

1.
2.
3.
4.
5.
6.
7.
8.

### REVIEW / REVISION / OPEN


---

## Day 09 — Banking System Case: UPI

- Case: [UPI — capability to API network](../case-studies/week-01-upi-fa.md)
- Exercise: [Capability/Contract Review](../exercises/day-09-upi-capability-contract-review.md)

### RAW — Five-point timeline


### RAW — Fact / Inference / Unknown


### RAW — Ownership map


### RAW — Retry amplification


### RAW — ADR-lite


### REVIEW / REVISION / OPEN


## Week reflection

1. کدام پاسخ Day 01 بیشترین تغییر را کرد و چرا؟
2. کدام عبارت را قبلاً Capability می‌دانستی ولی اکنون System/Process می‌دانی؟
3. در زنجیرهٔ مسدودی، کدام Ownership هنوز نامطمئن است؟
4. کدام Coupling در پروژه‌های واقعی تو بیشترین خطر را دارد؟
5. BIAN چه Gap مفیدی نشان داد و کجا False Friend بود؟
6. کدام Rule Money را عمداً به Week/Context بعد موکول کردی؟
7. Refactor روز هشتم چه Complexity تازه‌ای ساخت؟
8. از UPI چه چیزی را انتقال می‌دهی و چه چیزی را Copy نمی‌کنی؟
9. یک سؤال که باید در Week 02 پاسخ داده شود چیست؟

## Instructor final review

- Core score/status:
- Expansion score/status:
- Critical errors:
- Required remediation:
- Week status: Review / Gate / Done Core / Done Expanded

