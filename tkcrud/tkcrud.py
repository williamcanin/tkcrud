from tkcrud.utilities import *
from os.path import dirname, realpath, join


class TkCrud(Database):

    def __init__(self):
        Database.__init__(self)
        # Create directory
        self.create_folder(self.home_user, '.config/tkcrud/config')
        self.create_folder(self.home_user, '.config/tkcrud/data')
        self.create_config()
        # Create SQL (Database)
        sql = join(dirname(realpath(__file__)), 'data/sql.sql')
        qry = open(sql, 'r').read()
        self.execute(qry)
        self.commit()
        self.connection.close()

    def __str__(self):
        return TkCrud()


if __name__ == '__main__':
    pass
