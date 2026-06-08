import sqlite3

def create_database():
    conn = sqlite3.connect("./flask_datubaze/database.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 name TEXT)""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()