from table import Table


class System:
    name: str
    tables: list[Table] = []

    def __init__(self, data: dict):
        self.name = data['name_system']
        for table_data in data['tables']:
            self.tables.append(
                Table(
                    name=table_data['name'],
                    default_settings={
                        'int': data['system_value_int'],
                        'str': data['system_value_str'],
                        'timestamp': data['system_value_timestamp'],
                    },
                    generate_data=table_data['generate_data'],
                    columns=table_data['column'],
                    row=table_data.get('row') or data['system_row']
                )
            )

    def get_tables(self) -> [Table]:
        return self.tables
