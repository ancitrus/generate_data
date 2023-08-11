import datetime

from column import Column, ColumnType


class TestColumn:
    def test_get_data_if_str(self):
        col_format = '12'
        column = Column(
            name='name',
            col_type=ColumnType.STR,
            col_format=col_format
        )
        assert len(column.get_data()) == int(col_format)

    def test_get_data_if_timestamp(self):
        col_format = "%Y-%m-%d"
        column = Column(
            name='name',
            col_type=ColumnType.TIMESTAMP,
            col_format=col_format
        )
        assert datetime.datetime.strptime(column.get_data(), col_format)

    def test_get_data_if_int(self):
        col_format = "38.12"
        column = Column(
            name='name',
            col_type=ColumnType.INT,
            col_format=col_format
        )
        assert column.get_data() == col_format
