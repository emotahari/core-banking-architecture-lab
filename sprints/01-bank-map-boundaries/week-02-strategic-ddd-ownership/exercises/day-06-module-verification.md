# Day 06 Exercise — Module Verification and Negative Evidence

- Exercise timebox: 30 minutes after the lesson
- Output: architecture test + red/green evidence

## Part A — Permanent fitness test

Create:

~~~text
src/test/java/com/example/corebankinglab/ModulithArchitectureTests.java
~~~

The test must call:

```java
ApplicationModules.of(CoreBankingLabApplication.class).verify();
```

Run `mvn verify` and record the green baseline.

## Part B — Inspect model

Print Application Modules and verify:

- all six intended modules are detected
- no accidental seventh module exists
- API surface and dependency list match the policy

## Part C — Negative experiment

Recommended: internal access violation.

1. Create a temporary public Type inside one module's `internal` package.
2. Reference it from another module.
3. Run `mvn verify`.
4. Copy only the relevant violation message to the Workbook.
5. Remove the temporary violation.
6. Run `mvn verify` again.

Do not commit the violating code. Commit the test and written evidence.

## Part D — Explain the boundary

Answer in 150 words:

1. What architectural property did the test verify?
2. What did it not verify?
3. Which future test would cover one missing property?

## Optional module-test design

Choose one module and state whether its future integration test should start with `STANDALONE`, `DIRECT_DEPENDENCIES` or `ALL_DEPENDENCIES`. Defend the choice; do not add empty tests solely for coverage.

## Acceptance criteria

- permanent test runs under `mvn verify`
- red evidence corresponds to the intended rule
- green evidence exists after repair
- no violation filters or Open modules
- explanation does not claim domain correctness from structural verification

## Submission

Record both evidence states in [Week 02 Workbook](../submissions/week-02-workbook.md).
