import json
import os.path

from system import System

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
INPUT_FILE = os.path.join(DATA_DIR, 'generate_props.json')


def main() -> list[System]:
    systems: list[System] = []

    with open(INPUT_FILE, 'r') as f:
        data: list = json.load(f)

    for system_data in data:
        systems.append(
            system := System(data=system_data)
        )

        for table in system.get_tables():
            with open(os.path.join(DATA_DIR, f'{system.name}_{table.name}.csv'), 'w') as f:
                f.write(table.get_header())
                f.writelines(table.get_data())

    return systems


if __name__ == '__main__':
    main()
