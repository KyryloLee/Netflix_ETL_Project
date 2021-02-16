import sqlite3
from sqlite3 import Error

def create_connection(db_path):
    """
    Input:
        db_path - path to sqlite database
    Return:
        Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except Error as e:
        print(e)
    return conn
