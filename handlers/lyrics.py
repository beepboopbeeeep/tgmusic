from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
from utils.lyrics import get_lyrics

async def lyrics_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    try:
        # Parse callback data
        data = query.data.split('_', 2)
        if len(data) < 3:
            await query.edit_message_text("داده‌های نامعتبر")
            return
            
        title = data[1]
        artist = data[2]
        
        # Get lyrics
        lyrics_text = get_lyrics(title, artist)
        
        # Create keyboard
        keyboard = [[InlineKeyboardButton("متن کامل", callback_data=f"full_lyrics_{title}_{artist}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send preview (first 200 characters)
        await query.edit_message_text(
            text=f"متن آهنگ:\n\n{lyrics_text[:200]}...",
            reply_markup=reply_markup
        )
    except Exception as e:
        await query.edit_message_text(f"خطا در دریافت متن آهنگ: {str(e)}")