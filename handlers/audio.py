import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.acrcloud import recognize_audio
from config import MAX_FILE_SIZE, TEMP_PATH

async def audio_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.effective_attachment
    
    if file:
        # Check file size
        if file.file_size > MAX_FILE_SIZE:
            await update.message.reply_text("فایل بزرگتر از 30MB است. لطفاً فایل کوچکتری ارسال کنید.")
            return
        
        # Download file
        temp_file = f"{TEMP_PATH}temp_audio.mp3"
        await file.download_to_drive(temp_file)
        
        # Recognize with ACRCloud
        result = recognize_audio(temp_file)
        if result:
            try:
                result_data = json.loads(result)
                if result_data['status']['code'] == 0:
                    metadata = result_data['metadata']
                    if 'music' in metadata and metadata['music']:
                        track = metadata['music'][0]
                        title = track.get('title', 'نامشخص')
                        artist = track.get('artists', [{}])[0].get('name', 'نامشخص')
                        
                        response = f"آهنگ شناسایی شد:\n🎵 {title}\n🎤 {artist}"
                        keyboard = [[InlineKeyboardButton("دریافت متن آهنگ", callback_data=f"lyrics_{title}_{artist}")]]
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        await update.message.reply_text(response, reply_markup=reply_markup)
                        return
            except Exception as e:
                print(f"Error parsing ACRCloud result: {e}")
        
        await update.message.reply_text("متأسفم، نتونستم این آهنگ رو شناسایی کنم")
        
        # Clean up
        if os.path.exists(temp_file):
            os.remove(temp_file)