from os import getcwd
from os import path

import sqlite3
from sqlite3 import Error

from core import create_connection, RatingTable

DB_PATH = path.join(getcwd(), 'db', 'Netflix.db')

if __name__=='__main__':
    conn = create_connection(DB_PATH)

    with conn:
        rating = RatingTable(conn)
        print('All done')