# Module Dependency Policy — Working Draft

- Version: 0.1
- Status: Not started
- Code root: `backend/banking-modulith/src/main/java/com/example/corebankinglab`

## Module inventory

| Logical module | Base package | Provided interface | Internal implementation | Required interfaces | Domain/context hypothesis |
|---|---|---|---|---|---|
| Party & Customer | `partycustomer` |  | `internal` |  |  |
| Product & Agreement | `productagreement` |  | `internal` |  |  |
| Deposits | `deposits` |  | `internal` |  |  |
| Lending | `lending` |  | `internal` |  |  |
| Payments | `payments` |  | `internal` |  |  |
| Accounting | `accounting` |  | `internal` |  |  |

## Allowed dependency decisions

Do not copy a dependency merely because one process calls another. A compile-time dependency must be the smallest stable interface required by the downstream model.

| Consumer module | Provider module | Named interface/API | Why required | Alternative considered | Coupling risk | Verification rule |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Forbidden dependencies

| From | To | Forbidden target | Reason | How detected |
|---|---|---|---|---|
| any module | any other module | `..internal..` | breaks encapsulation | `ApplicationModules.verify()` |
|  |  |  |  |  |

## Review checklist

- [ ] Every direct subpackage is intentionally a module.
- [ ] No top-level technical packages such as global `controller`, `service` or `repository` were created.
- [ ] Base-package public types are deliberately exposed.
- [ ] Subpackages are internal unless a `@NamedInterface` is justified.
- [ ] `allowedDependencies` names only required module interfaces.
- [ ] Module graph is acyclic.
- [ ] Shared kernel/common module has not become a dumping ground.
- [ ] Passing an ID or Snapshot is preferred to sharing another module's Entity.
