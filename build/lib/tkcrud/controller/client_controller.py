from tkcrud.utilities.database import Database
from tkcrud.model.client_model import ClientModel


def clean_table(tree):
    # cleaning Table
    records = tree.get_children()
    for element in records:
        tree.delete(element)


def window_popup(message_box, message):
    message_box.showinfo('Warning!', message)


def entry_validation(*args):
    entry_list = [*args]
    # TODO: Mensagem diferente para cada campo em branco.
    # if not entry_list[2]:
    #     window_popup(message_box, 'Address required.')
    return '' not in entry_list[2:11]


def get_clients(tree, end):
    clean_table(tree)
    # getting data
    db_rows = ClientModel(Database).get_all_clients()
    # filling data
    for row in db_rows:
        tree.insert("", end, values=row)


def saving_updating(tree, end, action, message_box, id_, *args):
    message_action = None
    # value = {'message_box': args[0], 'id': args[1]}
    if entry_validation(message_box, *args):
        if action == 'insert':
            message_action = ClientModel(Database).insert_client(*args[0:])
        elif action == 'update':
            message_action = ClientModel(Database).update_client(id_, *args[0:])
        window_popup(message_box, message_action)
        get_clients(tree, end)
    else:
        window_popup(message_box, 'There are required fields.')


class ClientController:
    table_fields = ['ID', 'Name', 'Address', 'Date of Birth', 'Sex',
                    'Marital Status', 'RG', 'CPF', 'Cell Phone',
                    'E-mail']

    def client_delete(self, tree, end, message_box):
        try:
            id_ = tree.item(tree.selection())['values'][0]
            message = message_box.askquestion('Delete register',
                                              f'Really want to delete the ID record {id_}?',
                                              icon='warning', parent=self)
            if message == 'yes':
                msg_delete = ClientModel(Database).delete_client(id_)
                window_popup(message_box, msg_delete)
                get_clients(tree, end)
        except IndexError:
            window_popup(message_box, 'Please, select record.')
        return

    def search_client(self, tree, end, message_box, *args):
        option = {'search_entry': args[0], 'type_search': args[1]}

        if not option['type_search']:
            window_popup(message_box, 'Select an type search in combo!')
        elif option['type_search'] == 'ID' and not option['search_entry'].isnumeric():
            window_popup(message_box, 'For this search use only numbers.')
        else:
            db_rows = ClientModel(Database).search_client(option['search_entry'],
                                                          option['type_search'])
            if db_rows:
                clean_table(tree)
                for row in db_rows:
                    tree.insert("", end, values=row)
            else:
                get_clients(tree, end)
                message_box.showinfo('Warning', f'No "{option["search_entry"]}"'
                                                f'Records Found', parent=self)
