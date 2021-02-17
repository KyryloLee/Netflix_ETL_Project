from .base_table import BaseTable

class RatingTable(BaseTable):
    def __init__(self, conn):

        self.table_name = 'Rating'
        
        self.columns = [
            'name text primary key not null unique'
        ]
        
        self.create_table = "create table if not exist {0} ({1}) without rowid"\
            .format(self.table_name, ','.join(self.columns))

        BaseTable.__init__(self, conn)
