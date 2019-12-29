from tkcrud.utilities.database import Database
from tkcrud.model.client_model import ClientModel


def clean_table(tree):
    # cleaning Table
    records = tree.get_children()
    for element in records:
        tree.delete(element)


def get_clients(tree, end):
    clean_table(tree)
    # getting data
    db_rows = ClientModel(Database).get_all_clients()
    # filling data
    for row in db_rows:
        tree.insert("", end, values=row)


class ClientController:
    table_fields = ['ID', 'Name', 'Address', 'Date of Birth', 'Sex',
                    'Marital Status', 'RG', 'CPF', 'Cell Phone',
                    'E-mail']

    @staticmethod
    def entry_validation(*args):
        entry_list = [*args]
        # TODO: Mensagem diferente para cada campo em branco.
        # if not entry_list[2]:
        #     self.window_popup(message_box, 'Address required.')
        return '' not in entry_list[2:11]

    @staticmethod
    def window_popup(message_box, message):
        message_box.showinfo('Warning!', message)

    def saving_updating(self, tree, end, action, *args):
        message_action = None
        dic = {'message_box': args[0], 'id': args[1]}
        if self.entry_validation(dic['message_box'], *args):
            if action == 'insert':
                message_action = ClientModel(Database).insert_client(*args[2:11])
            elif action == 'update':
                message_action = ClientModel(Database).update_client(dic['id'], *args[2:11])
            self.window_popup(dic['message_box'], message_action)
            get_clients(tree, end)
        else:
            self.window_popup(dic['message_box'], 'There are required fields.')
