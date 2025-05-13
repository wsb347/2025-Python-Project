from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


# /start 명령어 처리 함수
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"안녕하세요, {update.effective_user.first_name}님! 👋")

# 일반 메시지 처리 함수
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)