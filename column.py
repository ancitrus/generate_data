import datetime
import string
from enum import Enum
import random


class ColumnType(Enum):
    """ Перечисление типов полей """
    INT = 'int'
    STR = 'str'
    TIMESTAMP = 'timestamp'


class Column:
    """ Класс сущности колонка """
    name: str
    type: ColumnType
    format: str

    def __init__(self, name: str, col_type: ColumnType, col_format: str):
        self.name = name
        self.type = col_type
        self.format = col_format

    def get_data(self) -> str:
        if self.type == ColumnType.STR:
            return self._get_str()
        if self.type == ColumnType.TIMESTAMP:
            return self._get_timestamp()
        if self.type == ColumnType.INT:
            return self._get_int()

    def _get_str(self) -> str:
        return ''.join(random.choices(string.ascii_letters, k=int(self.format)))

    def _get_timestamp(self) -> str:
        return datetime.datetime.now().strftime(self.format)

    def _get_int(self) -> str:
        return self.format
