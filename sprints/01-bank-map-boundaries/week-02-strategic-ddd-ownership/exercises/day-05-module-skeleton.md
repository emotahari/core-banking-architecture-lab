# Day 05 Exercise — Six Spring Modulith Modules

- Implementation timebox: 75 minutes after the lesson
- Working directory: `backend/banking-modulith`
- Output: code + `artifacts/module-dependency-policy.md`

## Baseline

Run and record:

~~~bash
mvn verify
~~~

Do not build new work on an unexplained red baseline.

## Step 1 — Create six module base packages

Under `com.example.corebankinglab` create:

~~~text
partycustomer
productagreement
deposits
lending
payments
accounting
~~~

Each must have `package-info.java` with `@ApplicationModule`, a meaningful `displayName`, and an explicit initial dependency policy.

## Step 2 — Define surface and internals

For each module:

- identify one real Provided Interface candidate from your Domain Dossier
- keep it in the base package or an explicit Named Interface
- create an `internal` package for future implementation
- do not expose Entity/JPA types
- do not create global technical top-level packages

An empty package tree is not evidence. A fake `SomethingService` with no Domain meaning is also not evidence. Prefer package metadata plus a small, named Contract grounded in a Use Case.

## Step 3 — Implement one Named Interface

Choose one relationship from your Context Map where a subpackage needs deliberate exposure—for example a reference, snapshot or events contract. Implement:

- provider `@NamedInterface`
- minimal immutable Contract type written by you
- consumer `allowedDependencies = "provider::interface-name"`
- one compile-time usage proving the dependency

Do not copy the lesson's sample blindly; use your Context names and Ownership decision.

## Step 4 — Keep internals inaccessible

Add at least one internal implementation Type inside one module. No other module may Import it.

## Step 5 — Inspect detected modules

Use `ApplicationModules.of(CoreBankingLabApplication.class)` and print the model. Record:

- detected logical names
- base packages
- provided interfaces
- direct dependencies

## Step 6 — Update policy

Complete [Module Dependency Policy](../artifacts/module-dependency-policy.md). Every allowed dependency must trace to:

~~~text
Capability/Use Case → Context relationship → Contract → code dependency
~~~

## Acceptance criteria

- exactly the six intended domain modules are detected for this exercise
- modules are closed
- at least one meaningful Named Interface exists
- at least one explicit allowed dependency is demonstrated
- no dependency to `internal`
- no cycle
- no generic `common` dumping ground
- `mvn verify` passes before Day 06 architecture test is added

## Required evidence in Workbook

1. module tree
2. one `package-info.java`
3. one Named Interface
4. one consumer allowlist
5. `ApplicationModules` output summary
6. unresolved ownership/dependency question

Do not mark Day 05 Done before code review.
