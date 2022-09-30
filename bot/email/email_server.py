from bot.misc.env import Email
from email.mime.text import MIMEText
import smtplib


class Email_Server:
    def __init__(self):
        self.sender = Email.SENDER
        self.password = Email.PASS
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.sender, self.password)

    def send(self, to, msg):
        try:
            msg = MIMEText(msg)
            self.server.sendmail(self.sender, to, msg.as_string())

        except Exception as e:
            raise type(e)(str(e).rstrip() + "happens while sending verification email.")