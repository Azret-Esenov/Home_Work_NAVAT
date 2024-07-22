from aiogram import Router, F

from .dishes import dishes_router
from .myinfo import myinfo_router
from .start import start_router
from .echo import echo_router
from .review_dialog import review_dialog_router
from .random_recipe import random_recipe_router
from .group import group_router


private_router = Router()
private_router.include_router(start_router)
private_router.include_router(review_dialog_router)
private_router.include_router(dishes_router)
private_router.include_router(myinfo_router)
private_router.include_router(random_recipe_router)
private_router.include_router(echo_router)

private_router.message.filter(F.chat.type == 'private')
