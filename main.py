import asyncio
import logging

from aiogram import Bot
from bot_config import dp, bot, database
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.dishes import dishes_router
from handlers.myinfo import myinfo_router
from handlers.random_recipe import random_recipe_router
from handlers.review_dialog import review_dialog_router


async def on_startup(bot: Bot):
    database.create_tables()


async def main():
    dp.include_router(start_router)
    dp.include_router(review_dialog_router)
    dp.include_router(dishes_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_recipe_router)
    dp.include_router(echo_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
