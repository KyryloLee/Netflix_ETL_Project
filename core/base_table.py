class BaseTable():
    def __init__(self, connector):
        # Base commands
        self.create_table = "create table if not exists {0} ({1}) without rowid;"
        self.insert = 'insert into {0} values({1})'
        self.delete = 'delete from {0} where ?=?'
        self.update = 'update {0} set ?=? where ?=?'
        self.conn = connector

        #create or connect to table
        self._connect_to_table()

    def _connect_to_table(self):
        # Values like self.table_name must be defined in child classes
        print('Execute command:', self.create_table)
        c = self.conn.cursor()
        command = self.create_table.format(self.table_name, ','.join(self.columns))
        c.execute(command)

    def insert(self, data:list):
        c = self.conn.cursor()
        insert_values = ','.join(['?'] * len(data))
        values = data
        try:
            c.execute(
                self.insert.format(self.table_name, insert_values),
                values
            )
        except Exception as e:
            print(e)

    def delete(self, condition, value):
        c = self.conn.cursor()
        try:
            c.execute(
                self.delete.format(self.table_name),
                condition, 
                value
            )
        except Exception as e:
            print(e)

    def update(self, set_col, set_value, where_col, where_value):
        c = self.conn.cursor()
        try:
            c.execute(
                self.update.formta(self.table_name),
                set_col, set_value, where_col, where_value
            )
        except Exception as e:
            print(e)