from pyrogram import filters
from bot.misc.content import Dialogues
from bot.misc.content import Markups
import bot.misc.util as utils
from pyromod import listen


# Write here all handlers as decorators inside this function
def register_user_handlers(bot) -> None:
    @bot.on_message(filters.command("start") & filters.private)
    async def on_start(client, message):
        chat_id = message.chat.id
        user_alias = message.from_user.username
        user_data = {
            "name": {"name": None, "surname": None, "patronymic": None},
            "alias": user_alias,
            "chat_id": chat_id,
            "phone": None,
            "email": None,
            "from_inno": None,
        }

        registered = utils.is_registered(alias=user_alias)

        # Delete Start message
        await message.delete()

        if not registered:
            exit_code = False

            await message.reply(Dialogues.registration_2)

            # Choose Innopolis / ordinary registration
            while not exit_code:
                ans = await client.ask(chat_id, Dialogues.registration_5, reply_markup=Markups.yes_no_exit_button)
                await ans.delete()
                ans = ans.text

                # Check if exit button
                exit_code = utils.is_exit(ans)
                if exit_code:
                    break

                ans = utils.yes_no_check(ans)
                if ans is not None:
                    user_data["from_inno"] = ans
                    break

            # Get real First, Second, Third name
            while not exit_code:
                name = await client.ask(chat_id, Dialogues.registration_name_1, reply_markup=Markups.exit_button)
                await name.delete()
                name = name.text

                # Check if exit button
                exit_code = utils.is_exit(name)
                if exit_code:
                    break

                elif utils.check_name(name):
                    splited_name = name.split(" ")
                    user_data["name"]["name"] = splited_name[0]
                    user_data["name"]["surname"] = splited_name[1]
                    user_data["name"]["patronymic"] = splited_name[2]
                    break

                else:
                    await message.reply(Dialogues.registration_name_2)

            # Get real Phone number
            while not exit_code:
                phone = await client.ask(chat_id, Dialogues.registration_phone_1, reply_markup=Markups.exit_button)
                await phone.delete()
                phone = phone.text

                # Check if exit button
                exit_code = utils.is_exit(phone)
                if exit_code:
                    break

                elif utils.check_phone(phone):
                    user_data["phone"] = phone
                    break

                else:
                    await message.reply(Dialogues.registration_phone_2)

            # Get user email
            while not exit_code:
                email = await client.ask(chat_id, Dialogues.registration_email_1, reply_markup=Markups.exit_button)
                await email.delete()
                email = email.text

                # Check if exit button
                exit_code = utils.is_exit(email)
                if exit_code:
                    break

                elif utils.check_email(email):

                    secret = utils.send_verify_message(email)

                    # Ask for a secret in a loop
                    i = 0
                    while i <= 3:
                        ans = await client.ask(chat_id, Dialogues.registration_email_3,
                                               reply_markup=Markups.exit_button)
                        await ans.delete()
                        ans = ans.text

                        # Check if exit button
                        exit_code = utils.is_exit(ans)
                        if exit_code:
                            break

                        # Write to variable if answer is correct
                        if secret == ans:
                            user_data["email"] = email
                            break
                        else:
                            await message.reply(Dialogues.registration_email_4, reply_markup=Markups.exit_button)

                        # On third wrong answer ask for resending
                        if i == 2:
                            ans = await client.ask(chat_id, Dialogues.registration_email_5, reply_markup=Markups.email)
                            await ans.delete()
                            ans = ans.text

                            exit_code = utils.is_exit(email)
                            if exit_code:
                                break

                            if ans == "Send one more time":
                                secret = utils.send_verify_message(email)

                            i = 0

                        i += 1
                    break

                else:
                    await message.reply(Dialogues.registration_email_2)

            # TODO Check if all data is filled
            # TODO Write user_data to DB
            await message.reply(Dialogues.registration_3, reply_markup=Markups.no_buttons)

        else:
            await message.reply(Dialogues.registration_1, reply_markup=Markups.no_buttons)

    @bot.on_message(filters.text & filters.private)
    async def test_echo(client, message):
        await message.reply(message.text)
