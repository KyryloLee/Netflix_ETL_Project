from os import getcwd
from os import path

from csv import DictReader
from core import create_connection, UniqueNameTable,\
    UniqueIdTable, Movies, IdToNamesRelation, create_main_view

# path to csv file
RAW_DATA = path.join(getcwd(), 'raw_data', 'netflix_titles.csv')
# path to db
DB_PATH = path.join(getcwd(), 'db', 'Netflix.db')

# Column to table relations
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

# Relation between tables
RELATION_COLUMNS_TO_TABLE = [
    ('Movie_directors', ('Movies','Directors'), ('show_id','director')),
    ('Movie_cast', ('Movies','Actors'), ('show_id','cast')),
    ('Movie_country', ('Movies','Countries'), ('show_id','country')),
    ('Movie_genre', ('Movies', 'Genres'), ('show_id', 'listed_in'))
]

def insert_data_into_tables(row: dict, tables: dict):
    """
    The function parses csv data row into tables.
    Input:
        row - csv row with data.
        tables - a dictionary with a column name to table name relation.
    """
    for k,table in tables.items():
        
        # if it unique name, add to related table
        if k in COL_TO_TABLE_NAMES.keys():
            table.insert_data([row[k].strip()])
        # if it unqiue id or number, add to related table
        elif k in INT_COL_TO_TABLE_NAMES.keys():
            table.insert_data([int(row[k])])
        # parse stirng and add data to table
        elif k in COL_WITH_MULTY_VALUES_TO_TABLE_NAMES.keys():
            for value in row[k].split(','):
                table.insert_data([value.strip()])
        # add data to main movie table
        else:
            table.parse_and_insert_data(row)

def insert_data_into_relation_tables(row: dict, relation: list):
    """
    The function adds a link to tables.
    Input:
        row - csv data row.
        tables - dictionary with the relation table name, data table names and columns in csv row.
    """
    for k, table in relation.items():
        movie_id, names = row.get(k[2][0]), row.get(k[2][1]).split(',')
        for x in names:
            table.insert_data([movie_id, x.strip()])

if __name__=='__main__':
    """
    The program opens the csv file, parse it and fill related architecture tables.
    """
    conn = create_connection(DB_PATH)

    with conn:
        cursor = conn.cursor()

        # Connect to tables
        tables = {k: UniqueNameTable(v, cursor) for k,v in COL_TO_TABLE_NAMES.items()}
        tables.update({k: UniqueIdTable(v, cursor) for k,v in INT_COL_TO_TABLE_NAMES.items()})
        tables.update({k: UniqueNameTable(v, cursor) for k,v in COL_WITH_MULTY_VALUES_TO_TABLE_NAMES.items()})
        tables.update({'Movies': Movies(cursor)})

        relation_tables = {k: IdToNamesRelation(k[0], cursor, *k[1]) for k in RELATION_COLUMNS_TO_TABLE}

        with open(RAW_DATA) as raw_data:
            reader = DictReader(raw_data)
            for row in reader:
                insert_data_into_tables(row, tables)
                insert_data_into_relation_tables(row, relation_tables)

        create_main_view(cursor)
        print('All done')