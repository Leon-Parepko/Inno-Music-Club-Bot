import re

def is_registered(alias):
    # Write code
    return False

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