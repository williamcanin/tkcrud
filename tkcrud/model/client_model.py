#!/usr/bin/env python
# # -*- coding: utf-8 -*-


class ClientModel:
    _table = 'clients'

    def __init__(self, database, dbname):
        self.db = database
        self.parm = '?'
        if dbname == 'mysql':
            self.parm = '%s'

    def get_all_clients(self):
        #  ORDER BY name DESC
        sql = self.db.query(f"SELECT * FROM `{self._table}`")
        return sql

    def insert_client(self, *args):
        try:
            sql = f"""INSERT INTO `{self._table}` 
                      (name, address, date_of_birth, sex, marital_status,
                       rg, cpf, cell_phone, email)
                      VALUES ({self.parm}, {self.parm}, {self.parm}, {self.parm},
                              {self.parm}, {self.parm}, {self.parm}, {self.parm},
                              {self.parm});"""
            self.db.execute(sql, args)
            self.db.commit()
            return 'Record successfully inserted!'
        except Exception as e:
            return 'An error occurred while inserting record: ', e

    def update_client(self, id_, *args):
        try:
            sql_query = f'''UPDATE {self._table} SET name = {self.parm}, address = {self.parm},
                        date_of_birth = {self.parm}, sex = {self.parm}, marital_status = {self.parm},
                        rg = {self.parm}, cpf = {self.parm}, cell_phone = {self.parm},
                        email = {self.parm}
                        WHERE ID = {id_}'''
            self.db.execute(sql_query, args)
            self.db.commit()
            return 'Records updated successfully.'
        except Exception as e:
            return 'An error occurred while inserting record: ', e

    def search_client(self, get_value, type_search):
        if type_search == 'Name':
            sql_query = f"SELECT * FROM {self._table} WHERE name LIKE '%{get_value}%';"
        elif type_search == 'ID':
            sql_query = f'SELECT * FROM `{self._table}` WHERE `id` = {get_value};'
        else:
            sql_query = f'SELECT * FROM `{self._table}`;'
        search = self.db.query(sql_query)
        if search:
            return search
        # else:
        return False

    def delete_client(self, _id):
        try:
            sql_query = f'SELECT * FROM `{self._table}` WHERE ID = {_id};'
            get_id = self.db.query(sql_query)
            if len(get_id) == 0:
                return 'Record not found to delete.'
            else:
                sql_query = f'DELETE FROM `{self._table}` WHERE ID = {_id};'
                self.db.execute(sql_query)
                self.db.commit()
                return f'Record ID:{get_id[0][0]} deleted!'
        except Exception as e:
            print('An error occured while deleting: ', e)
            return False
