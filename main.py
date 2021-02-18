from os import getcwd
from os import path

from csv import DictReader
from core import create_connection, UniqueNameTable, UniqueIdTable, Movies

RAW_DATA = path.join(getcwd(), 'raw_data', 'netflix_titles.csv')
DB_PATH = path.join(getcwd(), 'db', 'Netflix.db')
COL_TO_TABLE_NAMES = {
    'type': 'Types',
    'rating': 'Ratings'
}

INT_COL_TO_TABLE_NAMES = {
    'release_year': 'Release_years'
}

COL_WITH_MULTY_VALUES_TO_TABLE_NAMES = {
    'director': 'Directors',
    'cast': 'Actors',
    'country': 'Countries',
    'listed_in': 'Genres'
}

def insert_data_in_tables(row, tables):
    for k,table in tables.items():
        
        if k in COL_TO_TABLE_NAMES.keys():
            table.insert_data([row[k].strip()])

        elif k in INT_COL_TO_TABLE_NAMES.keys():
            table.insert_data([int(row[k])])

        elif k in COL_WITH_MULTY_VALUES_TO_TABLE_NAMES.keys():
            for value in row[k].split(','):
                table.insert_data([value.strip()])

if __name__=='__main__':
    conn = create_connection(DB_PATH)

    with conn:
        cursor = conn.cursor()

        tables = {k: UniqueNameTable(v, cursor) for k,v in COL_TO_TABLE_NAMES.items()}
        tables.update({k: UniqueIdTable(v, cursor) for k,v in INT_COL_TO_TABLE_NAMES.items()})
        tables.update({k: UniqueNameTable(v, cursor) for k,v in COL_WITH_MULTY_VALUES_TO_TABLE_NAMES.items()})
        
        movie_table = Movies(cursor)

        with open(RAW_DATA) as raw_data:
            reader = DictReader(raw_data)
            for row in reader:
                insert_data_in_tables(row, tables)
                movie_table.insert_data(row)

        print('All done')