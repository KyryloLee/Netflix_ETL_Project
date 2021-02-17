from .base_table import BaseTable

class Movies(BaseTable):
    def __init__(self, table_name, cur):
        self.table_name = 'Movies'
        self.columns = [
            'show_id text primary key not null unquie',
            'type text not null',
            'title text not null',
            'country text'
            'date_added text not null',
            'release_year integer not null'
            'duration integer not null',
            'description text',
            'foreign key type references Types(name)',
            'foreign key country referenecs Countries(name)',
            'foreign key release_year references Realease_years(id)'
        ]

        BaseTable.__init__(cur)
