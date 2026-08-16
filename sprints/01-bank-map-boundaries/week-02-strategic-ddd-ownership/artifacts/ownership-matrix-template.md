<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <span dir="ltr">Data and Decision Ownership Matrix v1</span> — <span dir="ltr">Template</span>

- <span dir="ltr">Version: 0.1</span>
- <span dir="ltr">Status: Not started</span>
- <span dir="ltr">Rule: one semantic Fact/Decision has exactly one authority</span>; <span dir="ltr">other copies must declare their role.</span>

## <span dir="ltr">Allowed cell values</span>

- <span dir="ltr">`Authority`</span>: تنها <span dir="ltr">Context</span> مجاز به ایجاد/تغییر <span dir="ltr">Fact</span> یا گرفتن <span dir="ltr">Decision</span>
- <span dir="ltr">`Reference`</span>: فقط شناسه و رجوع به <span dir="ltr">Authority</span>
- <span dir="ltr">`Snapshot`</span>: کپی تاریخیِ مؤثر در لحظهٔ تعهد
- <span dir="ltr">`Derived`</span>: مقدار مشتق‌شده با <span dir="ltr">Source</span> و <span dir="ltr">Formula</span> مشخص
- <span dir="ltr">`Projection`</span>: مدل خواندنی قابل بازسازی
- <span dir="ltr">`Cache`</span>: کپی موقت با <span dir="ltr">Freshness/Expiry</span>
- <span dir="ltr">`Consumer`</span>: دریافت‌کنندهٔ <span dir="ltr">Fact</span> بدون مالکیت
- <span dir="ltr">`Not Allowed`</span>: نگهداری یا تغییر این داده در این <span dir="ltr">Context</span> ممنوع
- <span dir="ltr">`N/A`</span>: ارتباطی ندارد

## <span dir="ltr">Matrix</span>

| <span dir="ltr">Data/Decision</span> | <span dir="ltr">Party</span> & <span dir="ltr">Customer</span> | <span dir="ltr">Product</span> & <span dir="ltr">Agreement</span> | <span dir="ltr">Deposits</span> | <span dir="ltr">Lending</span> | <span dir="ltr">Payments</span> | <span dir="ltr">Accounting</span> | <span dir="ltr">Authority</span> / <span dir="ltr">Source of Record</span> | <span dir="ltr">Freshness/history rule</span> | <span dir="ltr">Reconciliation owner</span> | <span dir="ltr">Notes</span> |
|---|---|---|---|---|---|---|---|---|---|---|
| <span dir="ltr">Party identity</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Customer/KYC status</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Product definition/version</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Executed agreement terms</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Deposit account lifecycle</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Available deposit balance</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Operational deposit hold</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Loan principal outstanding</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Repayment schedule/state</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Payment order state</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Settlement state</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Journal Entry</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">GL/Subledger balance</span> |  |  |  |  |  |  |  |  |  |  |
| <span dir="ltr">Cross-domain process state</span> |  |  |  |  |  |  |  |  |  |  |

## <span dir="ltr">Decision ownership</span>

| <span dir="ltr">Decision</span> | <span dir="ltr">Trigger owner</span> | <span dir="ltr">Decision authority</span> | <span dir="ltr">State owner</span> | <span dir="ltr">Evidence required</span> | <span dir="ltr">Resulting fact/event</span> | <span dir="ltr">Consumers</span> |
|---|---|---|---|---|---|---|
| <span dir="ltr">Is customer identity valid</span>? |  |  |  |  |  |  |
| <span dir="ltr">Can this deposit accept a credit</span>? |  |  |  |  |  |  |
| <span dir="ltr">Can this hold be placed now</span>? |  |  |  |  |  |  |
| <span dir="ltr">Has the loan been granted</span>? |  |  |  |  |  |  |
| <span dir="ltr">Which journal template applies</span>? |  |  |  |  |  |  |

## <span dir="ltr">Quality checks</span>

1. برای یک ردیف بیش از یک <span dir="ltr">`Authority`</span> ننویس.
2. اگر دو مقدار هر دو «<span dir="ltr">Balance</span>» هستند، معنای آن‌ها را جدا کن؛ شاید دو <span dir="ltr">Fact</span> متفاوت باشند.
3. <span dir="ltr">`Snapshot`</span> باید زمان مؤثر و <span dir="ltr">Provenance</span> داشته باشد.
4. <span dir="ltr">`Derived`</span> باید <span dir="ltr">Source</span> و <span dir="ltr">Formula</span> داشته باشد.
5. <span dir="ltr">Process Manager</span> فقط وضعیت هماهنگی را مالک است، نه <span dir="ltr">State</span> داخلی <span dir="ltr">Domain</span>ها.
6. <span dir="ltr">Replication</span> فنی <span dir="ltr">Authority</span> جدید ایجاد نمی‌کند.

</div>
