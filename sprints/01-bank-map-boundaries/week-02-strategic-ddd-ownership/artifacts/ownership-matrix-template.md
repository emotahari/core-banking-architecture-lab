<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# <bdi dir="ltr">Data and Decision Ownership Matrix v1</bdi> — <bdi dir="ltr">Template</bdi>

- <bdi dir="ltr">Version: 0.1</bdi>
- <bdi dir="ltr">Status: Not started</bdi>
- <bdi dir="ltr">Rule: one semantic Fact/Decision has exactly one authority</bdi>; <bdi dir="ltr">other copies must declare their role.</bdi>

## <bdi dir="ltr">Allowed cell values</bdi>

- <bdi dir="ltr">`Authority`</bdi>: تنها <bdi dir="ltr">Context</bdi> مجاز به ایجاد/تغییر <bdi dir="ltr">Fact</bdi> یا گرفتن <bdi dir="ltr">Decision</bdi>
- <bdi dir="ltr">`Reference`</bdi>: فقط شناسه و رجوع به <bdi dir="ltr">Authority</bdi>
- <bdi dir="ltr">`Snapshot`</bdi>: کپی تاریخیِ مؤثر در لحظهٔ تعهد
- <bdi dir="ltr">`Derived`</bdi>: مقدار مشتق‌شده با <bdi dir="ltr">Source</bdi> و <bdi dir="ltr">Formula</bdi> مشخص
- <bdi dir="ltr">`Projection`</bdi>: مدل خواندنی قابل بازسازی
- <bdi dir="ltr">`Cache`</bdi>: کپی موقت با <bdi dir="ltr">Freshness/Expiry</bdi>
- <bdi dir="ltr">`Consumer`</bdi>: دریافت‌کنندهٔ <bdi dir="ltr">Fact</bdi> بدون مالکیت
- <bdi dir="ltr">`Not Allowed`</bdi>: نگهداری یا تغییر این داده در این <bdi dir="ltr">Context</bdi> ممنوع
- <bdi dir="ltr">`N/A`</bdi>: ارتباطی ندارد

## <bdi dir="ltr">Matrix</bdi>

| <bdi dir="ltr">Data/Decision</bdi> | <bdi dir="ltr">Party</bdi> & <bdi dir="ltr">Customer</bdi> | <bdi dir="ltr">Product</bdi> & <bdi dir="ltr">Agreement</bdi> | <bdi dir="ltr">Deposits</bdi> | <bdi dir="ltr">Lending</bdi> | <bdi dir="ltr">Payments</bdi> | <bdi dir="ltr">Accounting</bdi> | <bdi dir="ltr">Authority</bdi> / <bdi dir="ltr">Source of Record</bdi> | <bdi dir="ltr">Freshness/history rule</bdi> | <bdi dir="ltr">Reconciliation owner</bdi> | <bdi dir="ltr">Notes</bdi> |
|---|---|---|---|---|---|---|---|---|---|---|
| <bdi dir="ltr">Party identity</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Customer/KYC status</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Product definition/version</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Executed agreement terms</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Deposit account lifecycle</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Available deposit balance</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Operational deposit hold</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Loan principal outstanding</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Repayment schedule/state</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Payment order state</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Settlement state</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Journal Entry</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">GL/Subledger balance</bdi> |  |  |  |  |  |  |  |  |  |  |
| <bdi dir="ltr">Cross-domain process state</bdi> |  |  |  |  |  |  |  |  |  |  |

## <bdi dir="ltr">Decision ownership</bdi>

| <bdi dir="ltr">Decision</bdi> | <bdi dir="ltr">Trigger owner</bdi> | <bdi dir="ltr">Decision authority</bdi> | <bdi dir="ltr">State owner</bdi> | <bdi dir="ltr">Evidence required</bdi> | <bdi dir="ltr">Resulting fact/event</bdi> | <bdi dir="ltr">Consumers</bdi> |
|---|---|---|---|---|---|---|
| <bdi dir="ltr">Is customer identity valid</bdi>? |  |  |  |  |  |  |
| <bdi dir="ltr">Can this deposit accept a credit</bdi>? |  |  |  |  |  |  |
| <bdi dir="ltr">Can this hold be placed now</bdi>? |  |  |  |  |  |  |
| <bdi dir="ltr">Has the loan been granted</bdi>? |  |  |  |  |  |  |
| <bdi dir="ltr">Which journal template applies</bdi>? |  |  |  |  |  |  |

## <bdi dir="ltr">Quality checks</bdi>

1. برای یک ردیف بیش از یک <bdi dir="ltr">`Authority`</bdi> ننویس.
2. اگر دو مقدار هر دو «<bdi dir="ltr">Balance</bdi>» هستند، معنای آن‌ها را جدا کن؛ شاید دو <bdi dir="ltr">Fact</bdi> متفاوت باشند.
3. <bdi dir="ltr">`Snapshot`</bdi> باید زمان مؤثر و <bdi dir="ltr">Provenance</bdi> داشته باشد.
4. <bdi dir="ltr">`Derived`</bdi> باید <bdi dir="ltr">Source</bdi> و <bdi dir="ltr">Formula</bdi> داشته باشد.
5. <bdi dir="ltr">Process Manager</bdi> فقط وضعیت هماهنگی را مالک است، نه <bdi dir="ltr">State</bdi> داخلی <bdi dir="ltr">Domain</bdi>ها.
6. <bdi dir="ltr">Replication</bdi> فنی <bdi dir="ltr">Authority</bdi> جدید ایجاد نمی‌کند.

</div>
