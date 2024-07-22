from aiogram import Router, F, types
from aiogram.filters import Command

from bot_config import database


dishes_router = Router()


@dishes_router.message(Command('menu'))
async def menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Плов'),
            ],
            [
                types.KeyboardButton(text='Лагман'),
            ],
            [
                types.KeyboardButton(text='Манты'),
            ],
            [
                types.KeyboardButton(text='Бешбармак'),
            ],
            [
                types.KeyboardButton(text='Чебуреки'),
            ],
            [
                types.KeyboardButton(text='Баурсаки'),
            ],
            [
                types.KeyboardButton(text='Чай'),
            ],
            [
                types.KeyboardButton(text='Коктейли'),
            ],
            [
                types.KeyboardButton(text='Салаты'),
            ],
            [
                types.KeyboardButton(text='Десерты')
            ]

        ],
        resize_keyboard=True
    )
    await message.answer('choose cat', reply_markup=kb)

cats = ('Плов', 'Лагман', 'Манты', 'Бешбармак', 'Чебуреки', 'Баурсаки', 'Чай', 'Коктейли', 'Салаты', 'Десерты')
@dishes_router.message(lambda m:m.text in cats)
async def dishes_handler(message: types.Message):
    sqlquery = """
    SELECT dishes.*, categories_of_dishes.name FROM dishes
    JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
    WHERE categories_of_dishes.name = ?
    """

    dishes = database.fetch(
        query=sqlquery,
        params=(message.text,),
    )
    for dish in dishes:
        photo = types.FSInputFile(dish['cover'])
        await message.answer_photo(
            photo=photo,
            caption=f'{dish['name']}\n'
                    f'{dish['gram']}\n'
                    f'{dish["price"]}\n',
        )
