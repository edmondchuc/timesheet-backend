import sqlite3
from config import Config
import os


def connect(database_name):
    conn = sqlite3.connect(os.path.join(Config.APP_DIR, database_name))

    if not conn:
        raise sqlite3.DatabaseError('Error connecting to SQLite database "{}".'.format(database_name))

    # Return row results accessible by its column name.
    conn.row_factory = sqlite3.Row

    return conn
