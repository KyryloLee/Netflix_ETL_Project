class BaseTable():
    def __init__(self, cur):
        # Base commands
        self.create_table = "create table if not exists {0} ({1}) without rowid;"
        self.insert = 'insert into {0} values({1});'
        self.cur = cur

        #create or connect to table
        self._connect_to_table()

    def _connect_to_table(self):
        # Values like self.table_name must be defined in child classes
        print('Execute command:', self.create_table)
        command = self.create_table.format(self.table_name, ','.join(self.columns))
        self.cur.execute(command)

    def insert_data(self, data:list):
        insert_values = ','.join(['?'] * len(data))
        values = data
        try:
            self.cur.execute(
                self.insert.format(self.table_name, insert_values),
                values
            )
        except Exception as e:
            print(e)

    def delete_data(self, value):
        pass

    def update_data(self, set_col, set_value, where_col, where_value):
        pass