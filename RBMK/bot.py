import asyncio
import logging
from aiogram import Bot, Dispatcher
# from aiogram.fsm.state import State, StatesGroup
from app1.handlers import *
from app1.config import TOKEN 
from aiogram import F


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router) 
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("InvalidError")
