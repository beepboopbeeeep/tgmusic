from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
🎵 به ربات موزیک خوش آمدید! 🎵

من می‌توانم:
✅ استخراج آهنگ از ویس، ویدیو و لینک‌های شبکه‌های اجتماعی
✅ دانلود محتوا از یوتیوب، اینستاگرام، تیک‌تاک و...
✅ جستجوی آهنگ بر اساس نام، خواننده یا متن آهنگ
✅ نمایش متن کامل آهنگ (لیریک)

برای شروع یکی از موارد زیر را ارسال کنید:
- لینک ویدیو/موسیقی از شبکه‌های اجتماعی
- فایل صوتی یا ویدیویی
- دستور /search برای جستجوی آهنگ
"""
    await update.message.reply_text(welcome_text)