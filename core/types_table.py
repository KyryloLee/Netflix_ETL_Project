from .base_table import BaseTable

class TypesTable(BaseTable):
    def __init__(self, conn):
        self.table_name = 'Types'
        self.columns = [
            'type text primary key not null unqiue'
        ]
        super.__init__(self, conn)