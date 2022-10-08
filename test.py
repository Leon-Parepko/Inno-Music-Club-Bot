import unittest

import run
from bot.database import register_db
from bot.database.models.user import UserModel
from bot.database.models.base_model import BaseModel
from bot.database.methods import *


class MyTestCase(unittest.TestCase):    # TODO: link main test script with other tests
    def test_something(self):

        register_db()

        # usr = UserModel(9, 'fake_pizdbl')
        # # usr.id = 1
        # usr.name = 'Pizdabol'
        # usr.surname = 'Krasniy'
        # usr.patronymic = 'Vasilievich'
        # usr.sex = 'unknown'
        # usr.email = 'pizdabol1@vk.com'
        # usr.phone = 0
        # usr.from_inno = None
        #
        # print(usr.create())
        # print(usr.get_all_columns_and_values())
        # print(usr.__dict__.items())

        # print(str(read(usr)[1][0][1:-2]).split(','))
        # print(usr)





if __name__ == '__main__':
    unittest.main()
