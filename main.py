from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
# from mysql import execute_query
from telegram_bot.telegram_info import start,handle_message

load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")



# 토큰을 봇에 연결
if __name__ == '__main__':
    app = ApplicationBuilder().token(telegram_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
