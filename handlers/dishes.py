from aiogram import Router, F, types
from bot_config import database


dishes_router = Router()


@dishes_router.message(F.text == 'Плов')
async def dishes_handler(message: types.Message):
    sqlquery = """
    SELECT dishes.*, categories_of_dishes.name FROM dishes
    JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
    WHERE categories_of_dishes.name = ?
    """
    categories_of_dishes = 'Плов'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/pilaf.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Плов: рассыпчатый, ароматный рис с мясом и специями'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Лагман')
async def dishes_handler(message: types.Message):
    sqlquery = """
        SELECT dishes.*, categories_of_dishes.name FROM dishes
        JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
        WHERE categories_of_dishes.name = ?
        """
    categories_of_dishes = 'Лагман'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/Lagman.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Лагман: наваристая лапша с овощами и мясом'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Манты')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Манты'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/manti.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Манты: сочные пельмени с начинкой'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Бешбармак')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Бешбармак'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/beshbarmak.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Бешбармак: традиционное казахское блюдо с мясом и лапшой'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Чебуреки')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Чебуреки'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/cheburek.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Чебуреки: хрустящие пирожки с начинкой'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Баурсаки')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Баурсаки'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/baursaki.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Баурсаки: воздушные пампушки'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Чай')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Чай'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/tea.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Авторские чаи: коллекция из почти 15 видов'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Коктейли')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Коктейли'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/koktel.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Авторские коктейли: представлены в барной карте'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Салаты')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Салаты'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/salat.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Салаты: свежие овощные и мясные салаты'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')


@dishes_router.message(F.text == 'Десерты')
async def dishes_handler(message: types.Message):
    sqlquery = """
            SELECT dishes.*, categories_of_dishes.name FROM dishes
            JOIN categories_of_dishes ON dishes_id = categories_of_dishes.id
            WHERE categories_of_dishes.name = ?
            """
    categories_of_dishes = 'Десерты'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories_of_dishes,),
    )
    print(dishes)
    recipe = types.FSInputFile('images/desert.jpg')
    await message.answer_photo(
        photo=recipe,
        caption='Десерты: сладкие угощения для завершения восточного путешествия'
    )
    for dish in dishes:
        await message.answer(f'Названия: {dish[1]}\nГраммы: {dish[2]}\nЦена: {dish[3]}')
