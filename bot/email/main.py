from bot.email.email_server import Email_Server


email_server: Email_Server


def register_email():
    global email_server

    try:
        email_server = Email_Server()
        return

    except Exception as e:
        raise type(e)(str(e).rstrip() + ": happens while register email.")


def get_email_server():
    return email_server