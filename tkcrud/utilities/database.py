from mysql.connector import connect as connect_mysql
from sqlite3 import connect as connect_sqlite
# from tkinter import messagebox
from textwrap import dedent
from os.path import join, dirname, abspath, realpath
from tkcrud.utilities.base import Base


class Database(Base):

    def __init__(self):
        try:
            Base.__init__(self)
            if self.app_config['App']['database']['dbname'] == 'mysql':
                # MySQL get data for connection in file JSON.
                connection_data = self.app_config['App']['database']['mysql']
                self._conn = connect_mysql(**connection_data)
            elif self.app_config['App']['database']['dbname'] == 'sqlite':
                # SQLite3 connection
                sqlite_filename = self.app_config['App']['database']['sqlite']['filename']
                dbname = join(self.home_user, f'.config/tkcrud/data/{sqlite_filename}')
                connection_data = join(self.home_user, dbname)
                # connect_sqlite: Create file sqlite
                self._conn = connect_sqlite(connection_data)
                # print('Connection successfully!')
            self._cursor = self._conn.cursor()

        except Exception as e:
            msg = dedent("A connection error has occurred."
                         "Check connectivity data (config.json) and make sure"
                         "database is powered on.")
            # messagebox.showinfo('Warning', f'{msg, e}', parent=self)
            print(msg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def query_one(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchone()

# qry = open(sql_file, 'r').read()
# conn = sqlite3.connect('/path/to/db')
# c = conn.cursor()
# c.execute(qry)
# conn.commit()
# c.close()
# conn.close()
