  GNU nano 8.6            bot.py             Modified
                        from telegram.ext import Appli>

# Твой токен (НЕ ПОКАЗЫВАЙ НИКОМУ!)
BOT_TOKEN = "8476029190:AAG-yC_YLv2uW7BmdZHZrrfKGU2rX9>

async def hello_world(update, context):
    await update.message.reply_text("👋 Hello World!")

print("🚀 Запускаю бота...")
print("📱 Бот работает в Termux!")
print("⏹️ Чтобы остановить: Ctrl+C")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, hello_worl>
app.run_polling()


