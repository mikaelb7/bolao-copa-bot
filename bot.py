from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8825943117:AAElan3TQjQu_ZByQpj4Z3kfEv7BZmaTbU4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Bot do Bolão da Copa 2026 iniciado com sucesso!"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
