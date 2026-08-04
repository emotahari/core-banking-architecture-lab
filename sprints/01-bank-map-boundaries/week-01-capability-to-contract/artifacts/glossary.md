# واژه‌نامهٔ معماری و Core Banking

- Version: 0.1
- Target: حداقل ۴۰ اصطلاح تا پایان Week 01
- Current entries: ۵۴

این تعریف‌ها آموزشی و عملیاتی‌اند. تعریف رسمی هر استاندارد در صورت تفاوت با منبع خودش تفسیر می‌شود.

| # | اصطلاح | تعریف عملیاتی در این دوره |
|---:|---|---|
| ۱ | Business Goal | نتیجهٔ جهت‌دهنده‌ای که سازمان می‌خواهد به آن برسد؛ مانند کاهش زمان عرضهٔ محصول اعتباری. |
| ۲ | Business Outcome | تغییر قابل مشاهده و سنجشی که تحقق Goal را نشان می‌دهد. |
| ۳ | Business Capability | توان پایدار سازمان برای انجام یک کار کسب‌وکاری؛ می‌گوید چه کاری، نه با چه فرایند یا سامانه‌ای. |
| ۴ | Capability Map | نمایش سلسله‌مراتبی Capabilityهای سازمان، معمولاً از L1 تا L3، مستقل از چارت و فناوری. |
| ۵ | Capability Owner | نقش پاسخ‌گوی بلوغ، عملکرد و تحول یک Capability؛ لزوماً مدیر یک سامانه نیست. |
| ۶ | Value Stream | توالی مراحل ارزش‌آفرینی از یک Trigger تا Outcome برای ذی‌نفع. |
| ۷ | Customer Journey | تجربهٔ گام‌به‌گام مشتری در تعامل با بانک از نگاه مشتری، نه ساختار داخلی سامانه‌ها. |
| ۸ | Business Process | نحوه و ترتیب اجرای فعالیت‌ها برای تولید یک Outcome؛ نسبت به Capability تغییرپذیرتر است. |
| ۹ | Business Function | دسته‌ای از فعالیت‌های هم‌ماهیت که معمولاً به مسئولیت سازمانی نزدیک است. |
| ۱۰ | Business Service | ارزشی که یک Capability از طریق Interface کسب‌وکاری به مصرف‌کننده ارائه می‌کند. |
| ۱۱ | System | مجموعه‌ای از اجزای مرتبط با Boundary و هدف مشخص؛ می‌تواند انسانی، نرم‌افزاری یا ترکیبی باشد. |
| ۱۲ | Application | نرم‌افزاری که بخشی از Capabilityها و Processها را پشتیبانی می‌کند؛ خود Capability نیست. |
| ۱۳ | Domain | حوزهٔ مسئله و دانش کسب‌وکاری که مدل برای آن ساخته می‌شود؛ مانند Lending. |
| ۱۴ | Subdomain | بخش مسئله‌ای متمایز در یک Domain با دانش، هدف و پیچیدگی خاص. |
| ۱۵ | Core Subdomain | بخش متمایزکننده و راهبردی کسب‌وکار که مزیت یا ارزش کلیدی می‌سازد. |
| ۱۶ | Supporting Subdomain | بخش اختصاصی لازم برای کسب‌وکار که مزیت اصلی نیست ولی راه‌حل عمومی کافی ندارد. |
| ۱۷ | Generic Subdomain | مسئله‌ای عمومی که معمولاً خرید، استفاده از استاندارد یا برون‌سپاری برای آن منطقی است. |
| ۱۸ | Bounded Context | مرزی که درون آن یک مدل و زبان مشخص، سازگار و معتبر است. |
| ۱۹ | Ubiquitous Language | زبان مشترک و دقیق تیم فنی و خبرگان دامینی درون یک Bounded Context. |
| ۲۰ | Context Map | نقشهٔ رابطه و جهت وابستگی میان Bounded Contextها، همراه با Pattern و Contract. |
| ۲۱ | Model | ساده‌سازی هدفمند واقعیت برای پاسخ به پرسش‌ها و اجرای قواعد در یک Context. |
| ۲۲ | Entity | شیء دامینی با هویت پایدار که حالت آن در طول زمان تغییر می‌کند. |
| ۲۳ | Value Object | شیء بدون هویت مستقل که با مقدار و قواعدش تعریف می‌شود و ترجیحاً Immutable است. |
| ۲۴ | Aggregate | مرز سازگاری دامینی برای گروهی از Entity/Value Objectها با یک Aggregate Root. |
| ۲۵ | Invariant | قاعده‌ای که در تمام حالت‌های معتبر باید برقرار بماند. |
| ۲۶ | Module | واحد منطقی کد با API آشکار، جزئیات داخلی پنهان و وابستگی کنترل‌شده. |
| ۲۷ | Service | ارائه‌کنندهٔ یک Contract؛ بسته به سطح بحث می‌تواند Business، Application، Domain یا Deployable Service باشد. |
| ۲۸ | Microservice | واحد نرم‌افزاری کوچک و قابل استقرار مستقل با مالکیت داده و هزینه‌های توزیع؛ مترادف Module نیست. |
| ۲۹ | API | Contract قابل فراخوانی برای تعامل؛ API مرز را آشکار می‌کند ولی خود Domain یا Capability نیست. |
| ۳۰ | Command | درخواست انجام عملی که قصد تغییر State دارد و ممکن است پذیرفته یا رد شود. |
| ۳۱ | Query | درخواست اطلاعات بدون قصد تغییر State کسب‌وکاری. |
| ۳۲ | Domain Event | Fact معناداری که در Domain رخ داده و نام آن گذشته‌نگر است. |
| ۳۳ | Integration Event | Contract منتشرشده برای مصرف خارج از Context؛ ممکن است از Domain Event مشتق شود ولی همان شیء داخلی نیست. |
| ۳۴ | Contract | توافق صریح دربارهٔ معنا، داده، قواعد، خطا، Version و انتظار تعامل. |
| ۳۵ | Coupling | میزان دانشی که یک جزء برای کارکردن دربارهٔ جزء دیگر لازم دارد. |
| ۳۶ | Cohesion | میزان تعلق مسئولیت‌های داخل یک جزء به یک هدف یا تغییر مشترک. |
| ۳۷ | Encapsulation | قرار دادن State و رفتار مرتبط پشت یک Interface کنترل‌شده. |
| ۳۸ | Information Hiding | پنهان‌کردن تصمیم‌های طراحیِ محتمل‌التغییر تا اثر تغییر به مصرف‌کنندگان نشت نکند. |
| ۳۹ | Data Owner | Context مجاز به ایجاد، تغییر و تضمین معنای یک داده. |
| ۴۰ | Decision Owner | Contextی که قاعده و اختیار تصمیم کسب‌وکاری را دارد؛ ممکن است دادهٔ ورودی را از دیگری بگیرد. |
| ۴۱ | Source of Truth | مرجع معتبر برای یک Fact مشخص؛ مفهوم باید با نوع داده و زمان اعتبار تعریف شود. |
| ۴۲ | System of Record | سامانهٔ رسمی ثبت و نگهداری یک Record؛ همیشه مالک همهٔ تصمیم‌های مرتبط با آن نیست. |
| ۴۳ | Derived Data | داده‌ای که از Source دیگر محاسبه یا Project شده و باید قابلیت Rebuild/Reconcile داشته باشد. |
| ۴۴ | Consistency Boundary | محدوده‌ای که Invariantها باید درون یک تغییر اتمیک حفظ شوند. |
| ۴۵ | Transaction Boundary | محدودهٔ اجرایی Commit/Rollback یک تراکنش؛ باید با Invariant توجیه شود. |
| ۴۶ | Upstream | Contextی که Contract یا مدل مورد استفادهٔ Context دیگر را عرضه می‌کند و قدرت تغییر بیشتری دارد. |
| ۴۷ | Downstream | Context مصرف‌کنندهٔ Contract یا مدل Upstream. |
| ۴۸ | Customer/Supplier | رابطه‌ای که Upstream و Downstream برای نیازهای Downstream همکاری و مذاکره می‌کنند. |
| ۴۹ | Conformist | Downstream مدل Upstream را بدون لایهٔ ترجمه می‌پذیرد، معمولاً به‌دلیل نبود قدرت یا ارزش ترجمه. |
| ۵۰ | Anti-Corruption Layer | لایهٔ ترجمه‌ای که مدل داخلی را از نفوذ مدل بیرونی محافظت می‌کند. |
| ۵۱ | Published Language | زبان و Schema مستند و مشترکی که برای تبادل میان Contextها منتشر می‌شود. |
| ۵۲ | BIAN Business Domain | گروه‌بندی سطح بالای فعالیت‌های بانکی در Reference Architecture BIAN. |
| ۵۳ | BIAN Service Domain | پارتیشن منطقی استانداردشدهٔ مسئولیت بانکی در BIAN؛ تصمیم استقرار فیزیکی سازمان ما نیست. |
| ۵۴ | BIAN Semantic API | مشخصات Interface منطقی متناظر با Service Domainهای دارای Service Operation؛ نقطهٔ شروع تطبیق است، نه Contract نهایی بدون Context. |

## واژه‌های ممنوع بدون Qualifier

در اسناد معماری این واژه‌ها بدون مشخص‌کردن سطح مبهم‌اند:

- Service: Business Service، Domain Service، Application Service یا Deployable Service؟
- Account: Deposit Account، Loan Account، Ledger Account یا User Account؟
- Transaction: Business Transaction، Database Transaction یا Accounting Transaction؟
- Customer: Party، Prospect، Legal Customer یا Contract Holder؟
- Product: Product Definition، Product Version، Offer یا Agreement Terms؟

هر بار که یکی از این واژه‌ها به‌کار می‌رود، Context و معنای دقیق باید روشن باشد.
