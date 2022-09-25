import pyrogram.types as ptypes

class Dialogues:
    registration_1 = "You are already registered in the system!"
    registration_2 = "You are NOT registered yet."
    registration_3 = "Now you are registered."
    registration_4 = "Registration is NOT complete!"
    registration_5 = "Use Innopolis(fast) registration or ordinary one."

    registration_name_1 = "Write your name."
    registration_name_2 = "Wrong name format."
    registration_phone_1 = "Write your phone."
    registration_phone_2 = "Wrong phone format."
    registration_email_1 = "Write your email."
    registration_email_2 = "Wrong email format."

class Markups:
    exit_button = ptypes.ReplyKeyboardMarkup([[("Exit")]], one_time_keyboard=True, resize_keyboard=True)
    yes_no_exit_button = ptypes.ReplyKeyboardMarkup([[("Yes"), ("No")], [("Exit")]], one_time_keyboard=True, resize_keyboard=True)

    no_buttons = ptypes.ReplyKeyboardRemove()


