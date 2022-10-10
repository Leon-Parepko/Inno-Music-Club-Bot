import re
import secrets
import string

from bot.database import UserMethods as db_user_methods
from bot.email import get_email_server


def generate_secret():
    alphabet = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(alphabet) for i in range(6))
    return code


# "chat_id" is unique account identifier
# Even if "alias" has been changed, the "chat_id" will remain the same
def is_registered(chat_id: int):
    return db_user_methods.get_one_by_chat_id(chat_id) is not None


def is_exit(str):
    return str == "Exit"


def yes_no_check(ans):
    if ans == "Yes":
        return True
    elif ans == "No":
        return False
    else:
        return None


def check_name(name):
    name = name.split()
    if len(name) == 3:
        for word in name:
            if not re.match("^([A-Z]([a-z]{1,30})$)", word):
                return False
        return True

    else:
        return False


def phone_parse(phone_raw: str) -> (int, bool):
    if re.search(r"[^0123456789\-_+ \(\)\[\]\{\}]", phone_raw) is not None:
        return 0, False
    number = re.sub("[^0-9+]", "", phone_raw)  # leave here only digits or '+'

    # Phone number can not have less than 7 digits due ITU-T E. 164,
    # but I can be wrong. So I reduced it to 2 digits to prevent some errors.
    if len(number) < 2:
        return 0, False
    # Variability of having '+' character makes phone identification hard
    if number[0] is not '+':
        return 0, False
    # Find if there is some extra '+' character.
    # It can ruin casting to integer and there is no reason to format number like that: "+7+(900)+123+45+67".
    if re.search(r"[+]", number[1:]) is not None:  # number[1:] - skipping first character which is '+'
        return 0, False

    return int(number), True


def phone_correct(phone_msg: str):
    phone, ok = phone_parse(phone_msg)
    if not ok:
        return False
    return db_user_methods.get_one_by_phone(phone) is not None


# returns parsed email and boolean(True if email form is correct)
def email_form_parse(email_raw: str) -> (str, bool):
    # If user put some unnecessary leading or trailing whitespace it will be removed
    email = email_raw.strip()

    #
    if email.count('@') is not 1:  # "#!$%&’*+-/=?^_`{}|~ @example.com .com" exists
        return email, False
    if email[0] is '@' or email[-1] is '@':  # check for empty username or domain
        return email, False
    return email, True


def email_correct(email_msg: str):
    email, ok = email_form_parse(email_msg)
    if not ok:
        return False
    return db_user_methods.get_one_by_email(email) is not None


def send_verify_message(to):
    server = get_email_server()
    secret = generate_secret()
    server.send(to, f'Here is your verification key: {secret}. \nDO NOT pass it to anybody else!')
    return secret


def get_class_field_value_by_name(class_obj: object, field_name: str) -> object:
    """
    @param class_obj: any class obj
    @param field_name: some string with name which field to find
    @return: object if found or None if Note

    Returns class field by its name.
    If field is empty, but declared return empty object like this: "return <class [field_name]>()".
    If there is no field with its name returns None
    """
    try:
        attr = getattr(class_obj, field_name)
        return attr
    except AttributeError as e:
        try:
            return class_obj.__class__.__dict__.get('__annotations__').get(field_name)()
        except Exception as e:
            return None
    except Exception as e:
        raise e
