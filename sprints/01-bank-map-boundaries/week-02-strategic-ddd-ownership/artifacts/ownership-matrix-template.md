# Data and Decision Ownership Matrix v1 — Template

- Version: 0.1
- Status: Not started
- Rule: one semantic Fact/Decision has exactly one authority; other copies must declare their role.

## Allowed cell values

- `Authority`: تنها Context مجاز به ایجاد/تغییر Fact یا گرفتن Decision
- `Reference`: فقط شناسه و رجوع به Authority
- `Snapshot`: کپی تاریخیِ مؤثر در لحظهٔ تعهد
- `Derived`: مقدار مشتق‌شده با Source و Formula مشخص
- `Projection`: مدل خواندنی قابل بازسازی
- `Cache`: کپی موقت با Freshness/Expiry
- `Consumer`: دریافت‌کنندهٔ Fact بدون مالکیت
- `Not Allowed`: نگهداری یا تغییر این داده در این Context ممنوع
- `N/A`: ارتباطی ندارد

## Matrix

| Data/Decision | Party & Customer | Product & Agreement | Deposits | Lending | Payments | Accounting | Authority / Source of Record | Freshness/history rule | Reconciliation owner | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Party identity |  |  |  |  |  |  |  |  |  |  |
| Customer/KYC status |  |  |  |  |  |  |  |  |  |  |
| Product definition/version |  |  |  |  |  |  |  |  |  |  |
| Executed agreement terms |  |  |  |  |  |  |  |  |  |  |
| Deposit account lifecycle |  |  |  |  |  |  |  |  |  |  |
| Available deposit balance |  |  |  |  |  |  |  |  |  |  |
| Operational deposit hold |  |  |  |  |  |  |  |  |  |  |
| Loan principal outstanding |  |  |  |  |  |  |  |  |  |  |
| Repayment schedule/state |  |  |  |  |  |  |  |  |  |  |
| Payment order state |  |  |  |  |  |  |  |  |  |  |
| Settlement state |  |  |  |  |  |  |  |  |  |  |
| Journal Entry |  |  |  |  |  |  |  |  |  |  |
| GL/Subledger balance |  |  |  |  |  |  |  |  |  |  |
| Cross-domain process state |  |  |  |  |  |  |  |  |  |  |

## Decision ownership

| Decision | Trigger owner | Decision authority | State owner | Evidence required | Resulting fact/event | Consumers |
|---|---|---|---|---|---|---|
| Is customer identity valid? |  |  |  |  |  |  |
| Can this deposit accept a credit? |  |  |  |  |  |  |
| Can this hold be placed now? |  |  |  |  |  |  |
| Has the loan been granted? |  |  |  |  |  |  |
| Which journal template applies? |  |  |  |  |  |  |

## Quality checks

1. برای یک ردیف بیش از یک `Authority` ننویس.
2. اگر دو مقدار هر دو «Balance» هستند، معنای آن‌ها را جدا کن؛ شاید دو Fact متفاوت باشند.
3. `Snapshot` باید زمان مؤثر و Provenance داشته باشد.
4. `Derived` باید Source و Formula داشته باشد.
5. Process Manager فقط وضعیت هماهنگی را مالک است، نه State داخلی Domainها.
6. Replication فنی Authority جدید ایجاد نمی‌کند.
