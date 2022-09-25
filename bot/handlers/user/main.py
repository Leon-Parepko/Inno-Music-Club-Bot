from pyrogram import filters
from bot.misc.content import Dialogues
import bot.misc.util as utils
from pyromod import listen
# from pyrogram.types import BotCommand



# Write here all handlers as decorators inside this function
def register_user_handlers(bot) -> None:


    # await bot.set_bot_commands([
    #     BotCommand("start", "Start the bot"),
    #     BotCommand("settings", "Bot settings")
    # ])


    @bot.on_message(filters.command("start") & filters.private)
    async def on_start(client, message):
        chat_id = message.chat.id
        user_alias = message.from_user.username
        user_data = {
                     "name": {"name": "", "surname": "", "patronymic": ""},
                     "alias": user_alias,
                     "chat_id": chat_id,
                     "phone": "",
                     "email": "",
                     }

        registered = utils.is_registered(alias=user_alias)

        # print(message)
        if not registered:

            # !!!DONT FORGET TO SET EXIT BUTTON!!!

            await message.reply(Dialogues.registration_2)

            # Get real First, Second, Third name
            while True:
                name = await client.ask(chat_id, Dialogues.registration_name_1)
                name = name.text
                if utils.check_name(name):
                    splited_name = name.split(" ")

                    user_data["name"]["name"] = splited_name[0]
                    user_data["name"]["surname"] = splited_name[1]
                    user_data["name"]["patronymic"] = splited_name[2]
                    break

                else:
                    await message.reply(Dialogues.registration_name_2)

            print(name)

            # Get real Phone number
            while True:
                phone = await client.ask(chat_id, Dialogues.registration_phone_1)
                phone = phone.text
                if utils.check_phone(phone):

                    user_data["phone"] = phone
                    break

                else:
                    await message.reply(Dialogues.registration_phone_2)

            print(phone)

            # Get user email
            while True:
                email = await client.ask(chat_id, Dialogues.registration_email_1)
                email = email.text
                if utils.check_email(email):

                    user_data["email"] = email
                    break

                else:
                    await message.reply(Dialogues.registration_email_2)

            print(email)


            # Write user_data to DB
            await message.reply(Dialogues.registration_3)

        else:
            await message.reply(Dialogues.registration_1)



    @bot.on_message(filters.text & filters.private)
    async def test_echo(client, message):
        await message.reply(message.text)