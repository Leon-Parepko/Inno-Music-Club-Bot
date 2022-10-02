import re
import secrets
import string
from bot.email import get_email_server


def generate_secret():
    alphabet = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(alphabet) for i in range(6))
    return code


def is_registered(alias):
    # TODO Write code
    return False


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


def check_phone(phone):
    # TODO Write code
    return True


def check_email(email):
    # TODO Write code
    return True


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
