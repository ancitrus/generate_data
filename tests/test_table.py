from table import Table


class TestTable:
    def test_get_header(self):
        table = Table(
            name='name',
            default_settings={},
            generate_data=False,
            columns=[
                {"Col_1": ["str", "12"]},
                {"Col_2": ["str", "12"]}
            ]
        )
        assert table.get_header() == 'Col_1,Col_2'

    def test_get_header_wrong_col_type(self):
        table = Table(
            name='name',
            default_settings={},
            generate_data=False,
            columns=[
                {"Col_1": ["str", "12"]},
                {"Col_2": ["str", "12"]},
                {"Col_3": ["string", "12"]}
            ]
        )
        assert table.get_header() == 'Col_1,Col_2'

    def test_get_header_wrong_timestamp(self):
        table = Table(
            name='name',
            default_settings={},
            generate_data=False,
            columns=[
                {"Col_1": ["str", "12"]},
                {"Col_2": ["str", "12"]},
                {"Col_3": ["timestamp", "12dvdfv%d"]}
            ]
        )
        assert table.get_header() == 'Col_1,Col_2'

    def test_get_data_num_rows(self):
        row = 5
        table = Table(
            name='name',
            default_settings={},
            generate_data=True,
            columns=[{"Col_1": ["str", "12"]}],
            row=row
        )
        assert len(table.get_data()) == row

    def test_get_data_not_generate(self):
        table = Table(
            name='name',
            default_settings={},
            generate_data=False,
            columns=[{"Col_1": ["str", "12"]}],
            row=1
        )
        assert not table.get_data()

    def test_get_data_col_format_default(self):
        default_str_len = 10
        table = Table(
            name='name',
            default_settings={'str': default_str_len},
            generate_data=True,
            columns=[{"Col_1": ["str"]}],
            row=1
        )
        assert len(table.get_data()[0]) == default_str_len

