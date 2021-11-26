import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.db")

'''connect to a database using sqlite3'''
def connect_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor