from os import getcwd
from os import path

from csv import DictReader
from collections import defaultdict
from core import create_connection, UniqueNameTable

RAW_DATA = path.join(getcwd(), 'raw_data', 'netflix_titles.csv')
DB_PATH = path.join(getcwd(), 'db', 'Netflix.db')
UNIQUE_NAME_COL = ['type', 'director'] 

if __name__=='__main__':
    conn = create_connection(DB_PATH)

    with conn:
        cursor = conn.cursor()
        
        type_table = TypesTable('Type', cursor)
        rating_table = RatingTable(conn)

        with open(RAW_DATA) as raw_data:
            reader = DictReader(raw_data)
            for row in reader:
                type_table.insert_data([row['type']])
                rating_table.insert_data([row['rating']])
        print('All done')