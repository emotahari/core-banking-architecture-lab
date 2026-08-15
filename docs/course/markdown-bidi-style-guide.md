<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# استاندارد نگارش <bdi dir="ltr">Markdown</bdi> دوجهته

این استاندارد برای فایل‌هایی است که متن اصلی آن‌ها فارسی است اما اصطلاحات معماری، شناسه‌های کد، مسیر فایل، فرمان و قطعه‌کد انگلیسی دارند. هدف این است که متن در <bdi dir="ltr">GitHub Preview</bdi> راست‌به‌چپ و پایدار باشد، بدون اینکه کد یا علائم انگلیسی جابه‌جا شوند.

## قرارداد فایل

هر فایل فارسی با این ساختار آغاز و پایان می‌یابد:


</div>

<div dir="ltr" align="left">

```html
<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# عنوان فارسی

متن فارسی

</div>
```

</div>

<div dir="rtl" align="right">


وجود خط خالی پس از تگ باز و پیش از تگ بسته مهم است؛ در <bdi dir="ltr">GitHub Flavored Markdown</bdi> باعث می‌شود <bdi dir="ltr">Markdown</bdi> داخل ظرف <bdi dir="ltr">HTML</bdi> همچنان پردازش شود.

## اصطلاحات و <bdi dir="ltr">inline code</bdi>

عبارت‌های چپ‌به‌راست با عنصر معنایی <bdi dir="ltr">bdi</bdi> از متن فارسی جدا می‌شوند:


</div>

<div dir="ltr" align="left">

```html
مرز <bdi dir="ltr">Bounded Context</bdi> با <bdi dir="ltr">Deployable Service</bdi> یکسان نیست.
فرمان <bdi dir="ltr">`mvn verify`</bdi> باید سبز باشد.
```

</div>

<div dir="rtl" align="right">


قاعده‌ها:

1. اصطلاح یا شناسهٔ انگلیسی را داخل <bdi dir="ltr">bdi</bdi> با جهت <bdi dir="ltr">ltr</bdi> قرار بده.
2. برای <bdi dir="ltr">inline code</bdi>، <bdi dir="ltr">backtick</bdi> را نگه دار و کل <bdi dir="ltr">code span</bdi> را داخل <bdi dir="ltr">bdi</bdi> بگذار.
3. از نویسه‌های نامرئی کنترل جهت مانند <bdi dir="ltr">LRM</bdi>، <bdi dir="ltr">RLM</bdi>، <bdi dir="ltr">LRI</bdi>، <bdi dir="ltr">RLI</bdi> و <bdi dir="ltr">PDI</bdi> استفاده نکن؛ این نویسه‌ها در بازبینی امنیتی مبهم‌اند.
4. <bdi dir="ltr">URL</bdi> و مقصد <bdi dir="ltr">Markdown link</bdi> دست‌کاری نمی‌شود؛ فقط عنوان قابل‌مشاهدهٔ لینک ایزوله می‌شود.

## بلوک کد

پیش از هر <bdi dir="ltr">fenced code block</bdi>، ظرف <bdi dir="ltr">RTL</bdi> بسته و ظرف <bdi dir="ltr">LTR</bdi> باز می‌شود. پس از بلوک، مسیر برعکس طی می‌شود:


</div>

<div dir="ltr" align="left">

````html
</div>

<div dir="ltr" align="left">

```java
public record AccountId(String value) {}
```

</div>

<div dir="rtl" align="right">
````

</div>

<div dir="rtl" align="right">


این قرارداد برای <bdi dir="ltr">text</bdi>، <bdi dir="ltr">Java</bdi>، <bdi dir="ltr">JSON</bdi>، <bdi dir="ltr">SQL</bdi> و <bdi dir="ltr">Mermaid</bdi> یکسان است. محتوای داخل <bdi dir="ltr">fence</bdi> هرگز با <bdi dir="ltr">bdi</bdi> نشانه‌گذاری نمی‌شود.

## جدول، فهرست و عنوان

جدول‌ها و فهرست‌ها داخل ظرف <bdi dir="ltr">RTL</bdi> باقی می‌مانند. عبارت‌های انگلیسی داخل سلول‌ها یا عنوان‌ها ایزوله می‌شوند. در <bdi dir="ltr">Source</bdi>، عنوان و جمله را تا جای ممکن با واژهٔ فارسی آغاز کن تا <bdi dir="ltr">Editor</bdi> نیز جهت خط را بهتر تشخیص دهد.

## فرمان‌ها

برای قالب‌بندی همهٔ فایل‌های فارسی:


</div>

<div dir="ltr" align="left">

```bash
python3 scripts/markdown_bidi.py --write
```

</div>

<div dir="rtl" align="right">


برای کنترل قبل از <bdi dir="ltr">Commit:</bdi>


</div>

<div dir="ltr" align="left">

```bash
python3 scripts/markdown_bidi.py --check
```

</div>

<div dir="rtl" align="right">


این کنترل در <bdi dir="ltr">CI</bdi> نیز اجرا می‌شود و موارد زیر را رد می‌کند:

- متن فارسی بدون ظرف <bdi dir="ltr">RTL</bdi>؛
- اصطلاح یا <bdi dir="ltr">inline code</bdi> چپ‌به‌راست بدون <bdi dir="ltr">bdi</bdi>؛
- <bdi dir="ltr">fenced code block</bdi> خارج از ظرف <bdi dir="ltr">LTR</bdi>؛
- تگ‌های جهت نامتوازن؛
- نویسه‌های نامرئی کنترل <bdi dir="ltr">BiDi.</bdi>

## چک‌لیست <bdi dir="ltr">Review</bdi>

- متن در <bdi dir="ltr">GitHub Preview</bdi> از راست خوانده می‌شود.
- کد، مسیر، شناسه و فرمان از چپ خوانده می‌شوند.
- جدول‌ها ترتیب منطقی ستون‌ها را حفظ می‌کنند.
- هیچ نویسهٔ کنترل جهت نامرئی در <bdi dir="ltr">Diff</bdi> وجود ندارد.
- <bdi dir="ltr">Source</bdi> با <bdi dir="ltr">UTF-8</bdi> و <bdi dir="ltr">LF</bdi> ذخیره شده است.
- تغییر قالب، معنای درس یا پاسخ خام دانشجو را عوض نکرده است.

## منابع استاندارد

- [<bdi dir="ltr">GitHub Flavored Markdown — HTML blocks</bdi>](https://github.github.com/gfm/#html-blocks)
- [<bdi dir="ltr">MDN — bdi element</bdi>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)


</div>
