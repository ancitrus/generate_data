""" Тесты главного цикла """
import os.path

import main


class TestMain:

    def test_input_file_exists(self):
        assert os.path.exists(path=main.INPUT_FILE)

    def test_inpt_file_not_empty(self):
        assert os.stat(path=main.INPUT_FILE).st_size

    def test_main(self):
        systems = main.main()
        for system in systems:
            for table in system.get_tables():
                assert os.path.exists(path=os.path.join(main.DATA_DIR, f'{system.name}_{table.name}.csv'))

    def test_out_files_header(self):
        systems = main.main()
        for system in systems:
            for table in system.get_tables():
                file = os.path.join(main.DATA_DIR, f'{system.name}_{table.name}.csv')
                with open(file, 'r') as f:
                    assert f.readline().rstrip('\n') == ','.join([column.name for column in table.columns])

    def test_out_files_data(self):
        systems = main.main()
        for system in systems:
            for table in system.get_tables():
                file = os.path.join(main.DATA_DIR, f'{system.name}_{table.name}.csv')
                with open(file, 'r') as f:
                    next(f)
                    line_count = len(f.readlines())
                    assert bool(line_count) == table.generate_data
                    if table.generate_data:
                        assert line_count == table.row
