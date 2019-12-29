import tkinter as tk
from tkinter import ttk, messagebox, font, StringVar
from tkcalendar import DateEntry
from tkcrud.controller.client_controller import ClientController


class FormClient(tk.Toplevel, ClientController):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.tree = ttk.Treeview(self, columns=('#0', '#1', '#2', '#3',
                                                '#4', '#5', '#6', '#7',
                                                '#8', '#9'), show='headings')
        self.form_client()

    def form_client(self):
        font_default = ('Sans Serif', 10, 'bold')
        self.geometry("980x580")
        self.title('Clients List')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        combo_list_font = font.Font(family='', size=12)
        self.option_add("*TCombobox*Listbox*Font", combo_list_font)

        label_search = tk.Label(self, text="Search by:", font=font_default)
        label_search.grid(row=0, column=0)
        type_search = ttk.Combobox(self, values=["ID", "Name"], state="readonly",
                                   font=('', 12, "bold"))
        type_search.grid(row=0, column=1)
        search_entry = tk.Entry(self, font=('', 12, "bold"))
        search_entry.grid(row=0, column=2)
        submit_search = tk.Button(self, text="Search",
                                  cursor="hand2", font=font_default)
        submit_search.grid(row=0, column=3)
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(row=1, columnspan=4, sticky='nsew')
        vsb.grid(row=1, column=4, rowspan=2, sticky='ns')
        hsb.grid(row=2, column=0, columnspan=4, sticky='ew')

        self.tree.heading('#1', text=self.table_fields[0])
        self.tree.heading('#2', text=self.table_fields[1])
        self.tree.heading('#3', text=self.table_fields[2])
        self.tree.heading('#4', text=self.table_fields[3])
        self.tree.heading('#5', text=self.table_fields[4])
        self.tree.heading('#6', text=self.table_fields[5])
        self.tree.heading('#7', text=self.table_fields[6])
        self.tree.heading('#8', text=self.table_fields[7])
        self.tree.heading('#9', text=self.table_fields[8])
        self.tree.heading('#10', text=self.table_fields[9])
        # self.tree.bind('<Double-1>', lambda event=None: FormClientUpdate(self.master, self.tree))

        # get_clients(self.tree, tk.END)

        frame = tk.LabelFrame(self, text='Actions')
        frame.grid(row=3, column=0, columnspan=4)
        button_add = tk.Button(frame, text="Create", width='10',
                               cursor="hand2", font=font_default)
        button_add.grid(row=1, column=1)
        button_edit = tk.Button(frame, text="Read All", width='10',
                                cursor="hand2", font=font_default)
        button_edit.grid(row=1, column=2)
        # TODO: Bug: Clicar no botão update sem registro selecionado;
        # AttributeError: 'FormClientUpdate' object has no attribute '_w'
        button_delete = tk.Button(frame, text="Update", width='10',
                                  cursor="hand2", font=font_default)
        button_delete.grid(row=1, column=3)
        button_delete = tk.Button(frame, text="Delete", width='10',
                                  cursor="hand2", font=font_default)
        button_delete.grid(row=1, column=4)

        self.resizable(0, 0)
        self.transient(self.master)
        self.grab_set()
        self.master.wait_window(self)
