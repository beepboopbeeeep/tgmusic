import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.downloader import download_media
from config import MAX_FILE_SIZE, SUPPORTED_PLATFORMS

async def download_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    
    # Check if URL is from supported platform
    platform = None
    for p, domains in SUPPORTED_PLATFORMS.items():
        if any(domain in url for domain in domains):
            platform = p
            break
    
    if not platform:
        await update.message.reply_text("این پلتفرم پشتیبانی نمی‌شود")
        return
    
    try:
        file_path = download_media(url, platform)
        
        # Check file size
        if os.path.getsize(file_path) > MAX_FILE_SIZE:
            await update.message.reply_text("فایل دانلود شده بزرگتر از 30MB است. لطفاً لینک دیگری ارسال کنید.")
            os.remove(file_path)
            return
        
        # Send file
        if file_path.endswith(('.mp3', '.wav')):
            await update.message.reply_audio(audio=open(file_path, 'rb'))
        else:
            await update.message.reply_video(video=open(file_path, 'rb'))
            
        # Clean up
        os.remove(file_path)
    except Exception as e:
        await update.message.reply_text(f"خطا در دانلود: {str(e)}")