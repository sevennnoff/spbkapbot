from aiogram import Dispatcher, Bot, F
import asyncio
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from handlers import router
import os

load_dotenv()

bot = Bot(token=os.getenv("TGTOKEN"), default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)

if  __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped Successfully")


