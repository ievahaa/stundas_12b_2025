import sqlite3

def create_database():
    conn = sqlite3.connect("./iss_location/database.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS iss_loc (
                 id INTEGER PRIMARY KEY,
                 datums TEXT,
                 platums TEXT,
                 garums TEXT)""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()