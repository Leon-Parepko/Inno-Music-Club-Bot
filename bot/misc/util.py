import re


def is_registered(alias):
    # Write code
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
    # Write code
    return True


def check_email(email):
    # Write code
    return True