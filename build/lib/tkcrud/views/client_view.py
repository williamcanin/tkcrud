import tkinter as tk
from tkinter import ttk, messagebox, font, StringVar
from tkcalendar import DateEntry
from tkcrud.controller.client_controller import ClientController,\
    saving_updating, get_clients, window_popup


class FormClientRegister(tk.Toplevel, ClientController):

    def __init__(self, master, tree):
        tk.Toplevel.__init__(self, master)
        self.get_id = None
        self.title('Clients Register')
        frame = tk.LabelFrame(self, text='Register client')
        frame.grid(row=0, column=0, columnspan=33, pady=30)
        label_name = tk.Label(frame, text=self.table_fields[1])
        label_name.grid(row=1, column=0)
        name = tk.Entry(frame)
        name.focus()
        name.grid(row=1, column=1)
        label_address = tk.Label(frame, text=self.table_fields[2])
        label_address.grid(row=2, column=0)
        address = tk.Entry(frame)
        address.grid(row=2, column=1)
        label_date_of_birth = tk.Label(frame, text=self.table_fields[3])
        label_date_of_birth.grid(row=3, column=0)
        date_of_birth = DateEntry(frame, date_pattern='y-mm-dd')
        date_of_birth.grid(row=3, column=1)
        label_sex = tk.Label(frame, text=self.table_fields[4])
        label_sex.grid(row=4, column=0)
        sex = ttk.Combobox(frame, values=["Male", "Female"], state="readonly")
        sex.grid(row=4, column=1)
        label_marital_status = tk.Label(frame, text=self.table_fields[5])
        label_marital_status.grid(row=5, column=0)
        marital_status = tk.Entry(frame)
        marital_status.grid(row=5, column=1)
        label_rg = tk.Label(frame, text=self.table_fields[6])
        label_rg.grid(row=6, column=0)
        rg = tk.Entry(frame)
        rg.grid(row=6, column=1)
        label_cpf = tk.Label(frame, text=self.table_fields[7])
        label_cpf.grid(row=8, column=0)
        cpf = tk.Entry(frame)
        cpf.grid(row=8, column=1)
        label_cell_phone = tk.Label(frame, text=self.table_fields[8])
        label_cell_phone.grid(row=9, column=0)
        cell_phone = tk.Entry(frame)
        cell_phone.grid(row=9, column=1)
        label_email = tk.Label(frame, text=self.table_fields[9])
        label_email.grid(row=10, column=0)
        email = tk.Entry(frame)
        email.grid(row=10, column=1)
        btn_register_save = tk.Button(frame,
                                      text='Save', cursor="hand2",
                                      command=lambda: saving_updating(
                                            tree, tk.END, 'insert', messagebox,
                                            self.get_id, name.get(), address.get(),
                                            date_of_birth.get(), sex.get(),
                                            marital_status.get(), rg.get(),
                                            cpf.get(), cell_phone.get(),
                                            email.get()))
        btn_register_save.grid(row=12, columnspan=2, sticky='we')

        message = tk.Label(frame, text='', fg='red')
        message.grid(row=13, column=0, columnspan=2, sticky='we')

        self.resizable(0, 0)
        self.transient(master)
        self.grab_set()
        master.wait_window(self)


class FormClientUpdate(tk.Toplevel, ClientController):
    def __init__(self, master, tree):
        try:
            self.id = tree.item(tree.selection())['values'][0]
            tk.Toplevel.__init__(self, master)
            self.title('Update client')
            frame = tk.LabelFrame(self, text='Update client')
            frame.grid(row=0, column=0, columnspan=33, pady=30)

            self.label_name = tk.Label(frame, text=self.table_fields[1])
            self.label_name.grid(row=1, column=0)
            old_name = tree.item(tree.selection())['values'][1]
            name = tk.Entry(frame, textvariable=StringVar(self, value=old_name))
            name.focus()
            name.grid(row=1, column=1)

            label_address = tk.Label(frame, text=self.table_fields[2])
            label_address.grid(row=2, column=0)
            old_address = tree.item(tree.selection())['values'][2]
            address = tk.Entry(frame, textvariable=StringVar(self, value=old_address))
            address.grid(row=2, column=1)

            label_date_of_birth = tk.Label(frame, text=self.table_fields[3])
            label_date_of_birth.grid(row=3, column=0)
            old_date_of_birth = tree.item(tree.selection())['values'][3]
            date_of_birth = DateEntry(frame, date_pattern='y-mm-dd',
                                      value=old_date_of_birth)
            date_of_birth.grid(row=3, column=1)

            label_sex = tk.Label(frame, text=self.table_fields[4])
            label_sex.grid(row=4, column=0)
            old_sex = tree.item(tree.selection())['values'][4]
            sex_value = StringVar()
            sex = ttk.Combobox(frame, textvariable=sex_value, state="readonly")
            sex['values'] = ('Male', 'Female')
            if old_sex == sex['values'][0]:
                sex.current(0)
            else:
                sex.current(1)
            sex.grid(row=4, column=1)

            label_marital_status = tk.Label(frame, text=self.table_fields[5])
            label_marital_status.grid(row=5, column=0)
            old_marital_status = tree.item(tree.selection())['values'][5]
            marital_status = tk.Entry(frame,
                                      textvariable=StringVar(self,
                                                             value=old_marital_status))
            marital_status.grid(row=5, column=1)

            label_rg = tk.Label(frame, text=self.table_fields[6])
            label_rg.grid(row=6, column=0)
            old_rg = tree.item(tree.selection())['values'][6]
            rg = tk.Entry(frame, textvariable=StringVar(self, value=old_rg))
            rg.grid(row=6, column=1)

            label_cpf = tk.Label(frame, text=self.table_fields[7])
            label_cpf.grid(row=8, column=0)
            old_cpf = tree.item(tree.selection())['values'][7]
            cpf = tk.Entry(frame, textvariable=StringVar(self, value=old_cpf))
            cpf.grid(row=8, column=1)

            label_cell_phone = tk.Label(frame, text=self.table_fields[8])
            label_cell_phone.grid(row=9, column=0)
            old_cell_phone = tree.item(tree.selection())['values'][8]
            cell_phone = tk.Entry(frame,
                                  textvariable=StringVar(self,
                                                         value=old_cell_phone))
            cell_phone.grid(row=9, column=1)

            label_email = tk.Label(frame, text=self.table_fields[9])
            label_email.grid(row=10, column=0)
            old_email = tree.item(tree.selection())['values'][9]
            email = tk.Entry(frame, textvariable=StringVar(self, value=old_email))
            email.grid(row=10, column=1)

            btn_save = tk.Button(frame, text='Save', cursor='hand2',
                                 command=lambda event=None: saving_updating(
                                     tree, tk.END, 'update', messagebox,
                                     self.id, name.get(), address.get(),
                                     date_of_birth.get(), sex.get(),
                                     marital_status.get(), rg.get(), cpf.get(),
                                     cell_phone.get(), email.get()))
            btn_save.grid(row=12, columnspan=2, sticky='we')

            message = tk.Label(frame, text='', fg='red')
            message.grid(row=13, column=0, columnspan=2, sticky='we')

            self.resizable(0, 0)
            self.transient(master)
            self.grab_set()
            master.wait_window(self)

        except IndexError:
            window_popup(messagebox, 'Please, select record')
        return


class FormClient(tk.Toplevel, ClientController):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        tree = ttk.Treeview(self, columns=('#0', '#1', '#2', '#3',
                                           '#4', '#5', '#6', '#7',
                                           '#8', '#9'), show='headings')
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
                                  cursor="hand2", font=font_default,
                                  command=lambda event=None: self.search_client(
                                      tree, tk.END, messagebox,
                                      search_entry.get(),
                                      type_search.get()
                                  ))
        submit_search.grid(row=0, column=3)
        vsb = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(row=1, columnspan=4, sticky='nsew')
        vsb.grid(row=1, column=4, rowspan=2, sticky='ns')
        hsb.grid(row=2, column=0, columnspan=4, sticky='ew')

        tree.heading('#1', text=self.table_fields[0])
        tree.heading('#2', text=self.table_fields[1])
        tree.heading('#3', text=self.table_fields[2])
        tree.heading('#4', text=self.table_fields[3])
        tree.heading('#5', text=self.table_fields[4])
        tree.heading('#6', text=self.table_fields[5])
        tree.heading('#7', text=self.table_fields[6])
        tree.heading('#8', text=self.table_fields[7])
        tree.heading('#9', text=self.table_fields[8])
        tree.heading('#10', text=self.table_fields[9])
        tree.bind('<Double-1>',
                  lambda event=None: FormClientUpdate(master, tree))

        get_clients(tree, tk.END)

        frame = tk.LabelFrame(self, text='Actions')
        frame.grid(row=3, column=0, columnspan=4)
        button_add = tk.Button(frame, text="Create", width='10',
                               cursor="hand2", font=font_default,
                               command=lambda: FormClientRegister(master, tree))
        button_add.grid(row=1, column=1)
        button_edit = tk.Button(frame, text="Read All", width='10',
                                cursor="hand2", font=font_default,
                                command=lambda: get_clients(tree, tk.END))
        button_edit.grid(row=1, column=2)
        button_delete = tk.Button(frame, text="Update", width='10',
                                  cursor="hand2", font=font_default,
                                  command=lambda event=None:
                                  FormClientUpdate(master, tree))
        button_delete.grid(row=1, column=3)
        button_delete = tk.Button(frame, text="Delete", width='10',
                                  cursor="hand2", font=font_default,
                                  command=lambda event=None:
                                  self.client_delete(tree, tk.END, messagebox))
        button_delete.grid(row=1, column=4)

        self.resizable(0, 0)
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
