from .utilities import *


class TkCrud(Base):

    def __init__(self):
        super(TkCrud, self).__init__()
        self.create_folder(self.home_user, '.config/tkcrud/config')
        self.create_folder(self.home_user, '.config/tkcrud/data')
        self.create_config()

    def __str__(self):
        return TkCrud()


if __name__ == '__main__':
    pass
