from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import json
import os

TOKEN = "8476029190:AAG-yC_YLv2uW7BmdZHZrrfKGU2rX9kMEEE"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

DATA_FILE = "balances.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бот-счётчик золотых. Используй /add, /spend, /balance.")

@dp.message_handler(commands=["add"])
async def cmd_add(message: types.Message):
    # ожидаем: "/add 10"
    parts = message.text.split()
    if len(parts) != 2 or not parts[1].isdigit():
        await message.reply("Используй: /add <кол-во>")
        return
    amount = int(parts[1])
    data = load_data()
    uid = str(message.from_user.id)
    data.setdefault(uid, 0)
    data[uid] += amount
    save_data(data)
    await message.reply(f"Добавлено {amount} золотых. Сейчас у тебя: {data[uid]} золота.")

@dp.message_handler(commands=["spend"])
async def cmd_spend(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2 or not parts[1].isdigit():
        await message.reply("Используй: /spend <кол-во>")
        return
    amount = int(parts[1])
    data = load_data()
    uid = str(message.from_user.id)
    current = data.get(uid, 0)
    if amount > current:
        await message.reply("Недостаточно золота.")
        return
    data[uid] = current - amount
    save_data(data)
    await message.reply(f"Потрачено {amount} золотых. Осталось: {data[uid]} золота.")

@dp.message_handler(commands=["balance"])
async def cmd_balance(message: types.Message):
    data = load_data()
    uid = str(message.from_user.id)
    current = data.get(uid, 0)
    await message.reply(f"У тебя сейчас: {current} золотых.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
