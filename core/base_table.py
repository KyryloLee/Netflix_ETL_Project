import sqlite3

class BaseTable():
    """
    Class with base functionality (create, insert).
    """
    def __init__(self, cur: 'sqlite3.Cursor'):
        # Base commands
        self.create_table = "create table if not exists {0} ({1}) without rowid;"
        self.insert = 'insert into {0} values({1});'
        self.cur = cur

        #create or connect to table
        self._connect_to_table()

    def _connect_to_table(self):
        # Values like self.table_name must be defined in child classes
        command = self.create_table.format(self.table_name, ','.join(self.columns))
        self.cur.execute(command)

    def insert_data(self, data:list):
        insert_values = ','.join(['?'] * len(data))
        values = data
        self.cur.execute(
            self.insert.format(self.table_name, insert_values),
            values
        )
        print(data, 'inserted into ', self.table_name)

