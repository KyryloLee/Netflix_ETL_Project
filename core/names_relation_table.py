from .base_table import BaseTable

class NamesRelation(BaseTable):
    def __init__(self, table_name, table1: str, table1_id:str, table2:str, table2_name:str):
        self.table_name = table_name
        self.col = [
            'id text not null',
            'name text',
        ]

        BaseTable.__init__(cur)