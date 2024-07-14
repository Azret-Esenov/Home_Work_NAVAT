from aiogram import Router
from aiogram.filters.command import Command

myinfo_router = Router()


@myinfo_router.message(Command('myinfo'))
async def myinfo_handler(message):
    print(message.from_user.id)
    await message.answer(f'Ваш id: {message.from_user.id}, '
                         f'Ваше ФИО: {message.from_user.first_name, message.from_user.last_name}')