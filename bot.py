import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import TELEGRAM_TOKEN
from handlers import start, audio, download, search, lyrics

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start.start_handler))
    application.add_handler(MessageHandler(filters.AUDIO | filters.VIDEO | filters.VOICE, audio.audio_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download.download_handler))
    application.add_handler(CommandHandler("search", search.search_handler))
    application.add_handler(CallbackQueryHandler(lyrics.lyrics_callback_handler))

    # Start bot
    application.run_polling()

if __name__ == "__main__":
    main()