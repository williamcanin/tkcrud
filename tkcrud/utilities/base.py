from os.path import join, isfile
from json import load
from json import dump
from pathlib import Path


class Base:

    def __init__(self):
        self.home_user = str(Path.home())
        config_json = '.config/tkcrud/config/config.json'
        self.app_config_path = join(self.home_user, config_json)
        if isfile(self.app_config_path):
            with open(self.app_config_path) as file:
                self._data = load(file)

    @property
    def app_config(self):
        return self._data

    @staticmethod
    def create_folder(path, folder):
        from pathlib import Path
        try:
            path = join(path, folder)
            Path(path).mkdir(parents=True, exist_ok=True)
        except OSError:
            return

    def create_config(self):

        config = {"App": {
                        "database": {
                            "dbname": "",
                            "mysql": {
                                "user": "",
                                "password": "",
                                "host": "",
                                "database": "",
                                "raise_on_warnings": True
                            },
                            "sqlite": {
                                "filename": ""
                            }
                        }
                    }
                  }

        configfile = join(self.home_user, '.config/tkcrud/config/config.json')

        if not isfile(configfile):
            with open(configfile, 'w') as file:
                dump(config, file, indent=4, separators=(',', ': '))

    # @staticmethod
    # def get_sql(sql_file_path):
    #     with open(sql_file_path, 'r', encoding='utf-8') as f:
    #         data = f.read().splitlines()
    #     stmt = ''
    #     stmts = []
    #     for line in data:
    #         if line:
    #             if line.startswith('--'):
    #                 continue
    #             stmt += line.strip() + ' '
    #             if ';' in stmt:
    #                 stmts.append(stmt.strip())
    #                 stmt = ''
    #     return stmts
