from aiogram import Router, types

echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    await message.answer('Я Вас не понимаю, вот команды, которые я понимаю:'
                         '/start - Запуск Бота'
                         )