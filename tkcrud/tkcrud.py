import tkinter as tk
from tkcrud.utilities import *
from os.path import dirname, realpath
from tkcrud.views.client_view import FormClient


class TkCrud(Database, tk.Frame):

    def __init__(self, master=tk.Tk()):
        Database.__init__(self)
        # Create all directory
        self.create_folder(self.home_user, '.config/tkcrud/config')
        self.create_folder(self.home_user, '.config/tkcrud/data')
        self.create_config()
        # Create SQL (Database)
        self.create_schema(dirname(realpath(__file__)), Database())
        # Tk
        tk.Frame.__init__(self, master)
        self.font_menu = ('Sans Serif', 10, 'bold')
        self.font_submenu = ('Sans Serif', 10)
        master.title('System')
        master.geometry("1024x580")

        menu_bar = tk.Menu(master)

        cad_menu = tk.Menu(menu_bar, tearoff=0, font=self.font_submenu)
        cad_menu.add_command(label='Clientes', command=lambda: FormClient(master))
        cad_menu.add_separator()
        cad_menu.add_command(label='Sair')
        menu_bar.add_cascade(label='Cadastros', menu=cad_menu, font=self.font_menu)

        tools = tk.Menu(menu_bar, tearoff=0)
        tools.add_command(label='Backup Database', font=self.font_submenu)
        menu_bar.add_cascade(label='Tools', menu=tools, font=self.font_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='Sobre', font=self.font_submenu)
        menu_bar.add_cascade(label='Ajuda', menu=help_menu, font=self.font_menu)

        master.config(menu=menu_bar)
        master.resizable(0, 0)

    def __str__(self):
        # window = tk.Tk()
        # window.pack()
        TkCrud().mainloop()
        # window.mainloop()

        # return TkCrud()


if __name__ == '__main__':
    pass
