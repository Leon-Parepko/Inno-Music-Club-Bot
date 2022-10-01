import re
import secrets
import string
from bot.email import get_email_server


def generate_secret():
    alphabet = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(alphabet) for i in range(6))
    return code


def is_registered(alias):
    #TODO Write code
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
    #TODO Write code
    return True


def check_email(email):
    #TODO Write code
    return True


def send_verify_message(to):
    server = get_email_server()
    secret = generate_secret()
    server.send(to, f'Here is your verification key: {secret}. \nDO NOT pass it to anybody else!')
    return secret


