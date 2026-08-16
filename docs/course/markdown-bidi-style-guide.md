<!-- bidi: rtl; code: ltr -->
<div dir="rtl" align="right">

# استاندارد نگارش <span dir="ltr">Markdown</span> دوجهته

این استاندارد برای فایل‌هایی است که متن اصلی آن‌ها فارسی است اما اصطلاحات معماری، شناسه‌های کد، مسیر فایل، فرمان و قطعه‌کد انگلیسی دارند. هدف این است که متن در <span dir="ltr">GitHub Preview</span> راست‌به‌چپ و پایدار باشد، بدون اینکه کد یا علائم انگلیسی جابه‌جا شوند.

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


وجود خط خالی پس از تگ باز و پیش از تگ بسته مهم است؛ در <span dir="ltr">GitHub Flavored Markdown</span> باعث می‌شود <span dir="ltr">Markdown</span> داخل ظرف <span dir="ltr">HTML</span> همچنان پردازش شود.

## اصطلاحات و <span dir="ltr">inline code</span>

عبارت‌های چپ‌به‌راست با عنصر مجاز <span dir="ltr">`span`</span> و ویژگی <span dir="ltr">`dir="ltr"`</span> از متن فارسی جدا می‌شوند. این انتخاب عمدی است: پاک‌ساز <span dir="ltr">HTML</span> گیت‌هاب عنصر <span dir="ltr">`bdi`</span> را حذف می‌کند، اما <span dir="ltr">`span`</span> و ویژگی <span dir="ltr">`dir`</span> را نگه می‌دارد.


</div>

<div dir="ltr" align="left">

```html
مرز <span dir="ltr">Bounded Context</span> با <span dir="ltr">Deployable Service</span> یکسان نیست.
فرمان <span dir="ltr">`mvn verify`</span> باید سبز باشد.
```

</div>

<div dir="rtl" align="right">


قاعده‌ها:

1. اصطلاح یا شناسهٔ انگلیسی را داخل <span dir="ltr">`span dir="ltr"`</span> قرار بده.
2. برای <span dir="ltr">inline code</span>، <span dir="ltr">backtick</span> را نگه دار و کل <span dir="ltr">code span</span> را داخل <span dir="ltr">`span dir="ltr"`</span> بگذار.
3. از نویسه‌های نامرئی کنترل جهت مانند <span dir="ltr">LRM</span>، <span dir="ltr">RLM</span>، <span dir="ltr">LRI</span>، <span dir="ltr">RLI</span> و <span dir="ltr">PDI</span> استفاده نکن؛ این نویسه‌ها در بازبینی امنیتی مبهم‌اند.
4. <span dir="ltr">URL</span> و مقصد <span dir="ltr">Markdown link</span> دست‌کاری نمی‌شود؛ فقط عنوان قابل‌مشاهدهٔ لینک ایزوله می‌شود.
5. از عنصر <span dir="ltr">`bdi`</span> استفاده نکن؛ ممکن است در مرورگر عادی درست باشد، اما در خروجی گیت‌هاب حذف می‌شود.

## بلوک کد

پیش از هر <span dir="ltr">fenced code block</span>، ظرف <span dir="ltr">RTL</span> بسته و ظرف <span dir="ltr">LTR</span> باز می‌شود. پس از بلوک، مسیر برعکس طی می‌شود:


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


این قرارداد برای <span dir="ltr">text</span>، <span dir="ltr">Java</span>، <span dir="ltr">JSON</span>، <span dir="ltr">SQL</span> و <span dir="ltr">Mermaid</span> یکسان است. محتوای داخل <span dir="ltr">fence</span> هرگز با <span dir="ltr">span</span> جهت‌دار نشانه‌گذاری نمی‌شود.

## جدول، فهرست و عنوان

جدول‌ها و فهرست‌ها داخل ظرف <span dir="ltr">RTL</span> باقی می‌مانند. عبارت‌های انگلیسی داخل سلول‌ها یا عنوان‌ها ایزوله می‌شوند. در <span dir="ltr">Source</span>، عنوان و جمله را تا جای ممکن با واژهٔ فارسی آغاز کن تا <span dir="ltr">Editor</span> نیز جهت خط را بهتر تشخیص دهد.

## فرمان‌ها

برای قالب‌بندی همهٔ فایل‌های فارسی:


</div>

<div dir="ltr" align="left">

```bash
python3 scripts/markdown_bidi.py --write
```

</div>

<div dir="rtl" align="right">


برای کنترل قبل از <span dir="ltr">Commit:</span>


</div>

<div dir="ltr" align="left">

```bash
python3 scripts/markdown_bidi.py --check
```

</div>

<div dir="rtl" align="right">


این کنترل در <span dir="ltr">CI</span> نیز اجرا می‌شود و موارد زیر را رد می‌کند:

- متن فارسی بدون ظرف <span dir="ltr">RTL</span>؛
- اصطلاح یا <span dir="ltr">inline code</span> چپ‌به‌راست بدون <span dir="ltr">`span dir="ltr"`</span>؛
- عنصر ناسازگار <span dir="ltr">`bdi`</span> خارج از نمونه‌های کد؛
- <span dir="ltr">fenced code block</span> خارج از ظرف <span dir="ltr">LTR</span>؛
- تگ‌های جهت نامتوازن؛
- نویسه‌های نامرئی کنترل <span dir="ltr">BiDi.</span>

## چک‌لیست <span dir="ltr">Review</span>

- متن در <span dir="ltr">GitHub Preview</span> از راست خوانده می‌شود.
- کد، مسیر، شناسه و فرمان از چپ خوانده می‌شوند.
- جدول‌ها ترتیب منطقی ستون‌ها را حفظ می‌کنند.
- هیچ نویسهٔ کنترل جهت نامرئی در <span dir="ltr">Diff</span> وجود ندارد.
- <span dir="ltr">Source</span> با <span dir="ltr">UTF-8</span> و <span dir="ltr">LF</span> ذخیره شده است.
- تغییر قالب، معنای درس یا پاسخ خام دانشجو را عوض نکرده است.

## منابع استاندارد

- [<span dir="ltr">GitHub Flavored Markdown — HTML blocks</span>](https://github.github.com/gfm/#html-blocks)
- [<span dir="ltr">GitHub HTML Pipeline — sanitization allowlist</span>](https://github.com/gjtorikian/html-pipeline/blob/main/lib/html_pipeline/sanitization_filter.rb)
- [<span dir="ltr">WHATWG HTML — dir attribute</span>](https://html.spec.whatwg.org/dev/dom.html#the-dir-attribute)


</div>
