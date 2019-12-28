from .utilities import *


class TKCrud(Utilities):

    def __init__(self):
        # from os.path import dirname, abspath
        super(TKCrud, self).__init__()
        self.create_folder(self.home_user, '.config/tkcrud/config')
        self.create_folder(self.home_user, '.config/tkcrud/data')
        self.create_config()
        d = Database()
        d.connection.close()

    def __str__(self):
        return TKCrud()


if __name__ == '__main__':
    print(TKCrud())
