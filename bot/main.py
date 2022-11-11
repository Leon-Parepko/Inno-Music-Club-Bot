from pyrogram import Client
from bot.filters import register_all_filters
from bot.misc import TgKeys as Secret
from bot.handlers import register_all_handlers
from bot.email import register_email
from bot.database import register_db



def __on_start_up(bot):
    register_db()
    print("Database: OK")

    register_email()
    print("Email Server: OK")

    register_all_filters(bot)
    print("Filters: OK")

    register_all_handlers(bot)
    print("Handlers: OK")


def start_bot():
    bot = Client("Inno_Music_Club_Bot_v2", api_id=Secret.API_ID, api_hash=Secret.API_HASH, bot_token=Secret.TOKEN)
    __on_start_up(bot)
    bot.run()
