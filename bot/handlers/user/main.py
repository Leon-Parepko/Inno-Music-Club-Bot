from pyrogram import filters


# Write here all handlers as decorators inside this function
def register_user_handlers(bot) -> None:

    @bot.on_message(filters.text & filters.private)
    async def test_echo(client, message):
        await message.reply(message.text)