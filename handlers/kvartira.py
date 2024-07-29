from aiogram import Router, types
from aiogram.filters.command import Command
from crawler.house_kg import HouseParser

house_router = Router()


@house_router.message(Command("house"))
async def show_house_links(message: types.Message):
    house_parser = HouseParser()
    house_parser.get_page()
    links = house_parser.get_house_links()
    print(links)
    for link in links:
        await message.answer(link)