import sqlite3

conn = sqlite3.connect("personas.db")
conn.execute("""CREATE TABLE IF NOT EXISTS personas (
             id INTEGER PRIMARY KEY, 
             vards TEXT)""")

conn.execute("""CREATE TABLE IF NOT EXISTS informacija (
             id INTEGER PRIMARY KEY,
             tel_nr TEXT,
             epasts TEXT,
             FOREIGN KEY (id) REFERENCES personas (id))""")

conn.commit()

def datu_ievade():
    conn.execute("INSERT INTO personas (id, vards) VALUES (2, 'Jānis')")
    conn.execute("INSERT INTO informacija (id, tel_nr, epasts) VALUES (2, '92345678', 'janis@skola.lv')")
    conn.commit()

# datu_ievade()

cursor = conn.execute("""SELECT personas.vards, informacija.tel_nr, informacija.epasts
                      FROM personas
                      LEFT JOIN informacija ON personas.id=informacija.id""")

for rinda in cursor:
    print(rinda)