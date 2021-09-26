import sqlite3


class DataBase:

    def __init__(self):

        self.conn = sqlite3.connect("message.db")
        self.cursor = self.conn.cursor()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS message(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        message TEXT
        )
        """)
        