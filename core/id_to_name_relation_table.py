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