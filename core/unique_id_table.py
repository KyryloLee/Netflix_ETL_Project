from .base_table import BaseTable

class UniqueIdTable(BaseTable):
    def __init__(self, table_name, cur):

        self.table_name = table_name
        self.columns = [
            'id integer primary key not null unique'
        ]

        BaseTable.__init__(self, cur)

    def insert_data(self, data:list):
        # Check if the data already exists
        insert_values = ','.join(['?'] * len(data))
        values = data
        cmd = 'select * from {0} where id = {1};'.format(self.table_name, insert_values)
        same_data = self.cur.execute(cmd, data).fetchall()

        if len(same_data) == 0:
            BaseTable.insert_data(self, data)