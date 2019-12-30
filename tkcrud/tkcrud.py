import tkinter as tk
from tkcrud.utilities import *
from os.path import dirname, realpath
from tkcrud.views.client_view import FormClient


class TkCrud(Database, tk.Frame):

    def __init__(self, master=tk.Tk()):
        self.master = master
        Database.__init__(self)
        # Create Database
        self.create_schema(dirname(realpath(__file__)), Database())
        # Starting Tk default
        tk.Frame.__init__(self, self.master)
        self.font_menu = ('Sans Serif', 10, 'bold')
        self.font_submenu = ('Sans Serif', 10)
        self.master.title('System')
        self.master.geometry("1024x580")
        menu_bar = tk.Menu(self.master)
        cad_menu = tk.Menu(menu_bar, tearoff=0, font=self.font_submenu)
        cad_menu.add_command(label='Clients', command=lambda: FormClient(self.master))
        cad_menu.add_separator()
        cad_menu.add_command(label='Exit', command=lambda: master.destroy())
        menu_bar.add_cascade(label='Registration', menu=cad_menu, font=self.font_menu)
        tools = tk.Menu(menu_bar, tearoff=0)
        tools.add_command(label='Backup Database', font=self.font_submenu)
        menu_bar.add_cascade(label='Tools', menu=tools, font=self.font_menu)
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='About', font=self.font_submenu)
        menu_bar.add_cascade(label='Help', menu=help_menu, font=self.font_menu)
        self.master.config(menu=menu_bar)
        self.master.resizable(0, 0)

    def __str__(self):
        return TkCrud().mainloop()


if __name__ == '__main__':
    pass
