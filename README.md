<div dir="rtl" align="right">

<h1 dir="rtl" align="right">فریمور زیرگذر برای Google WiFi با OpenWrt</h1>

فریمور **Google WiFi AC-1304 (Gale)** همراه با [زیرگذر](https://github.com/dreamboxone/zirgozar)، رابط وب LuCI و `mwan3` برای مدیریت چند اتصال اینترنت.

**این فایل‌ها فقط برای همین مدل هستند.** هدف ساخت `ipq40xx/chromium` و پروفایل `google_wifi` است.

<h2 dir="rtl" align="right">دریافت فریمور</h2>

از [آخرین انتشار](https://github.com/dreamboxone/openwrt-zirgozar/releases/latest) دانلود کنید:

- `factory.bin`: نصب اولیه طبق [راهنمای رسمی Google WiFi](https://openwrt.org/toh/google/wifi).
- `sysupgrade.bin`: ارتقای دستگاهی که OpenWrt دارد.
- `sha256sums`: کنترل SHA-256 فایل‌ها.
- `sources.txt` و `build.config`: شناسهٔ سورس‌ها، هش هسته‌ها و تنظیمات ساخت.

پیش از نصب از تنظیمات پشتیبان بگیرید. هنگام مهاجرت از فریمورهای دیگر، سازگاری تنظیمات قبلی را بررسی کنید. فریمور روی سخت‌افزار واقعی باید آزمایش شود.

<h2 dir="rtl" align="right">بررسی و انتشار خودکار</h2>

گردش‌کار GitHub Actions هر روز ساعت **۰۵:۵۳ تهران (۰۲:۲۳ UTC)** آخرین نسخهٔ پایدار رسمی OpenWrt دارای تصویر Google WiFi و آخرین انتشار پایدار [زیرگذر](https://github.com/dreamboxone/zirgozar) را بررسی می‌کند. زمان اجرای واقعی ممکن است با تأخیر GitHub همراه باشد.

اگر ترکیب این دو نسخه قبلاً با هر دو فایل فریمور منتشر نشده باشد، ساخت انجام می‌شود. انتشار ناموفق یا ناقص در بررسی بعدی دوباره تلاش می‌شود. تگ انتشار ثابت است تا بررسی روزانه، همان نسخه‌ها را بی‌دلیل دوباره نسازد.

از تب [Actions](https://github.com/dreamboxone/openwrt-zirgozar/actions/workflows/build.yml)، گزینهٔ **Run workflow** نیز در دسترس است؛ نسخهٔ OpenWrt، تگ زیرگذر و `force_build` اختیاری هستند. ساخت با push روی `main` هم بررسی می‌شود. در مخزن باید Actions فعال و اجازهٔ نوشتن `contents` برقرار باشد. Secret اضافی لازم نیست.

سورس هر دو پروژه روی تگ انتخاب‌شده ثابت می‌شود. Xray و sing-box با اسکریپت همان نسخهٔ زیرگذر دریافت و داخل فریمور قرار می‌گیرند؛ ماژول‌های کرنل و mwan3 همراه همان OpenWrt کامپایل می‌شوند. قابلیت‌های اختیاری زیرگذر از داخل برنامه قابل نصب هستند. تنظیمات پیش‌فرض خود زیرگذر حفظ می‌شود.

<h2 dir="rtl" align="right">مجوز و سورس</h2>

زیرگذر با مجوز AGPL-3.0-or-later منتشر می‌شود؛ متن مجوز در [LICENSE](LICENSE) و داخل تصویر در `/usr/share/licenses/zirgozar/LICENSE` قرار دارد. سورس دقیق هر انتشار از تگ درج‌شده در توضیحات آن قابل دریافت است. OpenWrt و بسته‌ها و هسته‌های همراه، مجوزهای خود را دارند.

</div>
