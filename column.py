from enum import Enum


class ColumnType(Enum):
    INT = 'int'
    STR = 'str'
    TIMESTAMP = 'timestamp'


class Column:
    name: str
    type: ColumnType
    format: str

    def __init__(self, name: str, col_type: ColumnType, col_format: str):
        self.name = name
        self.type = col_type
        self.format = col_format

    def get_data(self) -> str:
        return 'f'
