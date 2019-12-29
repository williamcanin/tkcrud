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
        """

        :rtype: object
        """
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

    def client_delete(self, tree, end, message_box):
        try:
            _id = tree.item(tree.selection())['values'][0]
            message = message_box.askquestion('Delete register',
                                              f'Really want to delete the ID record {_id}?',
                                              icon='warning', parent=self)
            if message == 'yes':
                msg_delete = ClientModel(Database).delete_client(_id)
                self.window_popup(message_box, msg_delete)
                get_clients(tree, end)
        except IndexError:
            self.window_popup(message_box, 'Please, select record.')
        return

    def search_client(self, tree, end, *args):
        dic = {'message_box': args[0], 'search_entry': args[1], 'type_search': args[2]}

        if not dic['type_search']:
            self.window_popup(dic['message_box'], 'Select an type search in combo!')
        elif dic['type_search'] == 'ID' and not dic['search_entry'].isnumeric():
            self.window_popup(dic['message_box'], 'For this search use only numbers.')
        else:
            db_rows = ClientModel(Database).search_client(dic['search_entry'], dic['type_search'])
            if db_rows:
                clean_table(tree)
                for row in db_rows:
                    tree.insert("", end, values=row)
            else:
                get_clients(tree, end)
                dic['message_box'].showinfo('Warning', f'No "{dic["search_entry"]}" Records Found', parent=self)
