from base_table import BaseTable

class RatingTable(BaseTable):
    def __init__(self, conn):
        self.table_name = 'Rating'
        self.create_table = """
            create table {0} (
                name text primary key unique not null
            )
        """.format(self.table_name)
        BaseTable.__init__(conn)
