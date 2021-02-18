from .base_table import BaseTable

class Movies(BaseTable):
    def __init__(self, cur):
        self.table_name = 'Movies'
        self.columns = [
            'show_id text primary key not null unique',
            'type text not null',
            'title text not null',
            'date_added text not null',
            'release_year integer not null',
            'duration integer',
            'seasons integer',
            'description text',
            'foreign key (type) references Types(name)',
            'foreign key (release_year) references Realease_years(id)'
        ]
        f = lambda x: x
        self.in_data_structure = [
            ('show_id', f),
            ('type', f),
            ('title', f),
            ('date_added', f),
            ('release_year', int),
            ('duration', lambda x: int(x.split()[0]) if x.split()[1].startswith('min') else None),
            ('duration', lambda x: int(x.split()[0]) if x.split()[1].startswith('Season') else None),
            ('description',f)
        ]
        BaseTable.__init__(self, cur)

    def parse_and_insert_data(self, data:dict):
        """
        Insertin data in Movie table.
        Input:
            data - dict with structure like self.in_data_structure and same key names.
        """
        parsed_data = [ x[1]( data[ x[0] ] ) for x in self.in_data_structure]
        BaseTable.insert_data(self, parsed_data)