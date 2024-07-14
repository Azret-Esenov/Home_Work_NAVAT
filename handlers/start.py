from aiogram import Router, types, F
from aiogram.filters.command import Command

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    # print(message.from_user.id)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Наш сайт', url='https://navat.kg'),
            ],
            [
                types.InlineKeyboardButton(text='Наш инстаграм', url='https://www.instagram.com/navat_kg')
            ],
            [
                types.InlineKeyboardButton(text='О нас', callback_data='about_us'),
            ],
            [
                types.InlineKeyboardButton(text='Контакты', callback_data='contacts_us'),
            ],
            [
                types.InlineKeyboardButton(text='Отзывы', callback_data='feedback'),
            ],
            [
                types.InlineKeyboardButton(text='Наши вакансии', callback_data='jobs'),
            ]
        ]
    )
    await message.answer(f'Добро пожаловать в ресторан Navat, {message.from_user.first_name}', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("Чайхана navat - оазис восточной культуры, "
                                  "где гости испытывают уникальнное путешествие через изумительные вкусы, "
                                  "аутентичную эстетику и безупречное гостеприимство.")


@start_router.callback_query(F.data == 'contacts_us')
async def contacts_us(callback: types.CallbackQuery):
    await callback.message.answer('ул. Ибраимова 42, +996 (551) 57 11 11')


@start_router.callback_query(F.data == 'jobs')
async def jobs(callback: types.CallbackQuery):
    await callback.message.answer("Отправляй своё резюме")