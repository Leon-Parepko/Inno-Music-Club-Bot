from bot.database.main import get_connection
from bot.database.models import UserModel


class UserRepository:   # Need exception safety

    @classmethod
    def create(cls, user: UserModel):
        names_str, values_str = user.get_all_columns_and_values_str()
        query = f'INSERT INTO {user.getTableName()}{names_str} VALUES {values_str}'
        conn = get_connection()
        cur = conn.cursor()
        with conn.transaction():
            cur.execute(query)

    @classmethod
    def read(cls) -> list[UserModel]:
        query = f'SELECT * FROM {UserModel.getTableName()} ' \
                f'WHERE deleted_at IS NULL'
        conn = get_connection()
        cur = conn.cursor(row_factory=UserModel.row_factory)
        with conn.transaction():
            cur.execute(query)
        return cur.fetchall()

    @classmethod
    def get_one_by_uuid(cls, uuid) -> UserModel:
        query = f'SELECT * FROM {UserModel.getTableName()} ' \
                f'WHERE uuid=\'{uuid}\' ' \
                f'AND deleted_at IS NULL'
        conn = get_connection()
        cur = conn.cursor(row_factory=UserModel.row_factory)
        with conn.transaction():
            cur.execute(query)
        return cur.fetchone()

    @classmethod
    def get_one_by_chat_id(cls, chat_id) -> UserModel:
        query = f'SELECT * FROM {UserModel.getTableName()} ' \
                f'WHERE chat_id={chat_id} ' \
                f'AND deleted_at IS NULL'
        conn = get_connection()
        cur = conn.cursor(row_factory=UserModel.row_factory)
        with conn.transaction():
            cur.execute(query)
        return cur.fetchone()

    @classmethod
    def get_one_by_phone(cls, phone: int) -> UserModel:
        query = f'SELECT * FROM {UserModel.getTableName()} ' \
                f'WHERE phone={phone} ' \
                f'AND deleted_at IS NULL'
        conn = get_connection()
        cur = conn.cursor(row_factory=UserModel.row_factory)
        with conn.transaction():
            cur.execute(query)
        return cur.fetchone()

    @classmethod
    def get_one_by_email(cls, email: str) -> UserModel:
        query = f'SELECT * FROM {UserModel.getTableName()} ' \
                f'WHERE email=\'{email}\' ' \
                f'AND deleted_at IS NULL'
        conn = get_connection()
        cur = conn.cursor(row_factory=UserModel.row_factory)
        with conn.transaction():
            cur.execute(query)
        return cur.fetchone()


    @classmethod
    def delete(cls, uuid):
        query = f'UPDATE {UserModel.getTableName()} SET deleted_at = now() ' \
                f'WHERE uuid=\'{uuid}\' ' \
                f'AND deleted_at IS NULL'
        conn = get_connection()
        cur = conn.cursor()
        with conn.transaction():
            cur.execute(query)

    @classmethod
    def update(cls, user: UserModel):
        names_str, values_str = user.get_all_columns_and_values_str()

        query = f'UPDATE {user.getTableName()} SET {names_str} = {values_str} ' \
                f'WHERE uuid=\'{user.uuid}\' ' \
                f'AND deleted_at IS NULL'
        conn = get_connection()
        cur = conn.cursor()
        with conn.transaction():
            cur.execute(query)

    @classmethod
    def restore(cls, uuid):
        query = f'UPDATE {UserModel.getTableName()} SET deleted_at = NULL ' \
                f'WHERE uuid=\'{uuid}\' ' \
                f'AND deleted_at IS NOT NULL'
        conn = get_connection()
        cur = conn.cursor()
        with conn.transaction():
            cur.execute(query)
