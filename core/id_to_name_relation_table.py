from .base_table import BaseTable

class IdToNamesRelation(BaseTable):
    def __init__(self, table_name, cur, table1: str, table2:str):
        self.table_name = table_name
        self.columns = [
            'id text not null',
            'name text',
            'foreign key (id) references {0}(id)'.format(table1),
            'foreign key (name) references {0}(name)'.format(table2),
            'primary key (id, name)',
            'unique (id, name)'
        ]

        BaseTable.__init__(self, cur)

    def insert_data(self, data:list):
        # Check if the data already exists
        insert_values = ','.join(['?'] * len(data))
        values = data
        cmd = 'select * from {0} where (id, name) = ({1});'.format(self.table_name, insert_values)
        same_data = self.cur.execute(cmd, data).fetchall()

        if len(same_data) == 0:
            BaseTable.insert_data(self, data)