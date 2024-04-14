from aiogram import Bot, Dispatcher
import asyncio
import logging
from handlers import handlers, sechandlers, thirdhandlers
from db import db_start

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token='ВАШ ТОКЕН')
    dp = Dispatcher()

    dp.include_routers(handlers.router, thirdhandlers.router,sechandlers.router)
    await db_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())