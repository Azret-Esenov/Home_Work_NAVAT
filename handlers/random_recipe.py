from aiogram import Router, types
from aiogram.filters.command import Command
import random

random_recipe_router = Router()


@random_recipe_router.message(Command('random_recipe'))
async def random_recipe_handler(message: types.Message):
    recipes = [
        'Плов: рассыпчатый, ароматный рис с мясом и специями',
        'Лагман: наваристая лапша с овощами и мясом',
        'Манты: сочные пельмени с начинкой',
        'Бешбармак: традиционное казахское блюдо с мясом и лапшой',
        'Чебуреки: хрустящие пирожки с начинкой',
        'Лепешки и баурсаки: воздушные пампушки',
        'Авторские чаи: коллекция из почти 15 видов',
        'Вина и авторские коктейли: представлены в барной карте',
        'Салаты: свежие овощные и мясные салаты',
        'Десерты: сладкие угощения для завершения восточного путешествия'
    ]
    random_recipe = random.choice(recipes)
    await message.answer(f'Ваш случайный рецепт: {random_recipe}')