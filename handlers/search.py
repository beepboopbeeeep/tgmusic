from telegram import Update
from telegram.ext import ContextTypes
from utils.search_engine import search_music

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text("لطفاً نام آهنگ، خواننده یا بخشی از متن آهنگ را وارد کنید")
        return
    
    try:
        results = await search_music(query)
        if results:
            response = "نتایج جستجو:\n\n"
            for idx, track in enumerate(results[:5], 1):
                response += f"{idx}. {track['name']} - {track['artist']}\n"
            response += "\nبرای دریافت متن آهنگ، شماره آهنگ را ارسال کنید"
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("نتیجه‌ای یافت نشد")
    except Exception as e:
        await update.message.reply_text(f"خطا در جستجو: {str(e)}")