from aiogram import Router, F, types


dishes_router = Router()


@dishes_router.message(F.text == 'Плов')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/pilaf.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Плов: рассыпчатый, ароматный рис с мясом и специями'
    )


@dishes_router.message(F.text == 'Лагман')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/Lagman.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Лагман: наваристая лапша с овощами и мясом'
    )


@dishes_router.message(F.text == 'Манты')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/manti.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Манты: сочные пельмени с начинкой'
    )


@dishes_router.message(F.text == 'Бешбармак')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/beshbarmak.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Бешбармак: традиционное казахское блюдо с мясом и лапшой'
    )


@dishes_router.message(F.text == 'Чебуреки')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/cheburek.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Чебуреки: хрустящие пирожки с начинкой'
    )


@dishes_router.message(F.text == 'Баурсаки')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/baursaki.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Баурсаки: воздушные пампушки'
    )


@dishes_router.message(F.text == 'Чай')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/tea.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Авторские чаи: коллекция из почти 15 видов'
    )


@dishes_router.message(F.text == 'Коктейли')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/koktel.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Авторские коктейли: представлены в барной карте'
    )


@dishes_router.message(F.text == 'Салаты')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/salat.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Салаты: свежие овощные и мясные салаты'
    )


@dishes_router.message(F.text == 'Десерты')
async def dishes_handler(message: types.Message):
    recipe = types.FSInputFile('images/desert.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Десерты: сладкие угощения для завершения восточного путешествия'
    )