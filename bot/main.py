import asyncio
import psycopg2

from pyrogram import Client
from bot.filters import register_all_filters
from bot.misc import TgKeys as Secret
from bot.handlers import register_all_handlers
from bot.database.models import register_models


def __on_start_up(bot):
    register_all_filters(bot)
    print("Filters: OK")
    register_all_handlers(bot)
    print("Handlers: OK")
    register_models(bot)
    print("Database: OK")


def start_bot():
    bot = Client("Inno_Music_Club_Bot_v2", api_id=Secret.API_ID, api_hash=Secret.API_HASH, bot_token=Secret.TOKEN)
    __on_start_up(bot)
    bot.run()
