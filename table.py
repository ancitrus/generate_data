from typing import Optional
import re

from column import Column, ColumnType


class Table:
    """ Класс сущности таблица """
    name: str
    generate_data: bool
    row: Optional[int] = None
    columns: list[Column]
    default_settings: dict

    def __init__(
            self,
            name: str,
            default_settings: dict,
            generate_data: bool,
            columns: list[dict],
            row: Optional[int] = None
    ):
        self.columns = []
        self.name = name
        self.default_settings = default_settings
        if generate_data and not row:
            raise Exception('Количество рядов не задано')
        self.generate_data = generate_data
        columns_dict = {}
        for column in columns:
            columns_dict = columns_dict | column
        for column_name, settings in columns_dict.items():
            if (col_type := settings[0]) not in [col_type.value for col_type in ColumnType]:
                continue

            col_format = settings[1] if len(settings) > 1 else default_settings[settings[0]]

            if col_type == ColumnType.TIMESTAMP.value and not re.findall(r'^(%[A-Za-z %][\s\\/:-|]?)+$', col_format):
                continue

            self.columns.append(
                Column(
                    name=column_name,
                    col_type=ColumnType(col_type),
                    col_format=col_format
                )
            )
        self.row = row

    def get_data(self) -> list[str]:
        out = []
        if self.generate_data:
            for _ in range(self.row):
                out.append(f"{','.join([column.get_data() for column in self.columns])}")
        return out

    def get_header(self) -> str:
        return ','.join([column.name for column in self.columns])
