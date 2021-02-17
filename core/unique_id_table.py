from .base_table import BaseTable

class UniqueIdTable(BaseTable):
    def __init__(self, table_name, cur):

        self.table_name = table_name
        
        self.columns = [
            'id integer primary key not null unique'
        ]

        BaseTable.__init__(self, cur)