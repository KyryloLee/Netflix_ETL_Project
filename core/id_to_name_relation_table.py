from .base_table import BaseTable

class IdToNameRelation(BaseTable):
    def __init__(self, table_name, cur, ):
        self.table_name = table_name
        self.col = [
            'id text not null',
            'name text',

        ]

        BaseTable.__init__(cur)