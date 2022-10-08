import builtins


class BaseModel:

    uuid: str   # model class should have by default

    @classmethod
    def getCreateTableQuery(cls) -> str:
        return ''

    @classmethod
    def getTableName(cls) -> str:
        return ''

    @classmethod
    def _add_braces(cls, li: list) -> str:
        return '(' + ', '.join(li) + ')'

    def get_all_columns_and_values(self) -> (list, list):
        # None means skip it
        change = {'created_at': 'NOW()', 'updated_at': 'NOW()',
                  'deleted_at': None,
                  'id': None, 'ID': None, 'uuid': None, 'UUID': None}
        # Names without skipping
        names_changed = list(
            filter(lambda x: change.get(x) is not None,
                   map(lambda x: x[0],
                       change.items()
                       )
                   )
        )
        values_changed = list(
            map(lambda x: change.get(x),
                names_changed
                )
        )
        # Names witch not in change 'names_changed' list
        names = list(
            map(lambda x: x[0],
                filter(lambda x: x[0] not in change and x[1] is not None,
                       self.__dict__.items()
                       )
                )
        )
        values = list(
            map(lambda x: f'\'{x}\'' if type(x) is str else str(x),
                map(self.__dict__.get,
                    names
                    )
                )
        )

        return names + names_changed, values + values_changed

    def get_all_columns_and_values_str(self) -> (str, str):
        names, values = self.get_all_columns_and_values()
        return self._add_braces(names), self._add_braces(values)

    def create(self) -> str:
        names_str, values_str = self.get_all_columns_and_values_str()
        query = f'INSERT INTO {self.getTableName()}{names_str} VALUES {values_str}'
        return query

    def get(self) -> (str, callable):
        pass

    def read(self) -> str:
        pass

    def write(self, dict):
        pass

    def update(self) -> str:    # Should have UUID
        names_str, values_str = self.get_all_columns_and_values_str()

        query = f'UPDATE {self.getTableName()} SET {names_str} = {values_str} ' \
                f'WHERE uuid={self.uuid} AND created_at IS NULL'
        return query

    def delete(self) -> str:
        pass
