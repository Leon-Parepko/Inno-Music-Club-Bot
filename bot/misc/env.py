from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ['TOKEN']
    API_ID: Final = environ['API_ID']
    API_HASH: Final = environ['API_HASH']


class Email:
    SENDER: Final[str] = environ.get('EMAIL')
    PASS: Final[str] = environ.get('EMAIL_PASS')


class PG:
    tables_created: Final[bool] = environ.get('PG_TABLES_CREATED', default=False)
    dbname: Final[str] = environ.get('PG_DB_NAME', default='innomusicclub')
    user: Final[str] = environ.get('PG_USER', default='postgres')
    host: Final[str] = environ.get('PG_HOST', default='localhost')
    password: Final[str] = environ['PG_PASS']
    port: Final[str] = environ.get('PG_PORT', default='5432')


class InnoID:
    app_token: Final[str] = environ.get('INNO_ID_TOKEN', default='')