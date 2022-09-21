from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ.get('TOKEN')
    API_ID: Final = environ.get('API_ID')
    API_HASH: Final = environ.get('API_HASH')
