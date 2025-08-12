from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from dotenv import load_dotenv
import os
from loader import DataLoader

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

if BOT_TOKEN is None:
        raise ValueError("BOT_TOKEN environment variable not set")

loader = DataLoader("links.json")
loader.load_links()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Бот активирован и готов скидывать сочные рилсы от Сергея М!")

@dp.message(Command("get_reels"))
async def send_reels(message: types.Message):
    if message.chat.type == "private" or message.from_user.is_bot:
        return

    chat_id = message.chat.id
    link = loader.get_reel()
    await bot.send_message(
        chat_id=chat_id,
        text=link
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
