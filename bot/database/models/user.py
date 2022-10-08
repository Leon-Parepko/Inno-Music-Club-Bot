import builtins
import datetime
from bot.database.models.base_model import BaseModel

table_name = 'public.users'

create_table_query = f'''CREATE TABLE {table_name}(
    id          uuid            DEFAULT gen_random_uuid() PRIMARY KEY,
    chat_id 	INT 			UNIQUE 	NOT 	NULL,
	alias 		VARCHAR ( 50 ) 	UNIQUE 	NOT 	NULL,

    name 		VARCHAR ( 50 ) 			NOT 	NULL,	--first name
    surname 	VARCHAR ( 50 ) 			NOT 	NULL,	--second name
    patronymic 	VARCHAR ( 50 ) 			NOT 	NULL,	--third name

    sex			VARCHAR ( 50 ) 			NOT 	NULL,	--male, female ot user option
	email 		VARCHAR ( 255 ) UNIQUE 	NOT 	NULL,
	phone		INT						NOT 	NULL,
	from_inno	BOOL,

	created_at 	TIMESTAMP 				NOT 	NULL,
	updated_at 	TIMESTAMP 				NOT 	NULL,
	deleted_at 	TIMESTAMP 				DEFAULT NULL
);'''


class UserModel(BaseModel):

    # def __init__(self, chat_id, alias):
    #     self.chat_id = chat_id
    #     self.alias = alias

    def __init__(self, uuid, chat_id, alias,
                name, surname, patronymic,
                sex, email, phone, from_inno,
                created_at, updated_at, deleted_at
                ):
        self.uuid = uuid; self.chat_id = chat_id; self.alias = alias
        self.name = name; self.surname = surname; self.patronymic = patronymic
        self.sex = sex; self.email = email; self.phone = phone; self.from_inno = from_inno
        self.created_at = created_at; self.updated_at = updated_at; self.deleted_at = deleted_at

    @classmethod
    def getTableName(cls) -> str:
        return table_name

    @classmethod
    def getCreateTableQuery(cls) -> str:
        return create_table_query

    uuid: str
    chat_id: int
    alias: str

    name: str
    surname: str
    patronymic: str

    sex: str
    email: str
    phone: int
    from_inno: bool

    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime

    @classmethod
    def from_row(cls, *, uuid, chat_id, alias,
                 name, surname, patronymic,
                 sex, email, phone, from_inno,
                 created_at, updated_at, deleted_at
                 ):
        return cls(
            uuid=uuid, chat_id=chat_id, alias=alias,
            name=name, surname=surname, patronymic=patronymic,
            sex=sex, email=email, phone=phone, from_inno=from_inno,
            created_at=created_at, updated_at=updated_at, deleted_at=deleted_at
        )

    @classmethod
    def row_factory(cls, cursor):
        columns = [column.name for column in cursor.description]

        def make_row(values):
            row = dict(zip(columns, values))
            return cls.from_row(**row)

        return make_row

    def get(self) -> (str, callable):
        return f'SELECT {"(" + (", ".join(list(map(lambda x: x[0], self.__dict__.items())))) + ")"} ' \
               f'FROM {self.getTableName()}; ' \
               f'WHERE uuid=\'{self.uuid}\' ' \
               f'AND deleted_at IS NULL', \
               self.write

    def write(self, dict):
        pass

    def read(self) -> str:
        return f'SELECT {"(" + (", ".join(list(map(lambda x: x[0], self.__dict__.items())))) + ")"} ' \
               f'FROM {self.getTableName()} ' \
               f'WHERE deleted_at IS NULL'

    def update(self) -> str:
        pass

    def delete(self) -> str:
        pass
