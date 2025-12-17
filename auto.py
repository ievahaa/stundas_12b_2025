import sqlite3
import random
import string

conn = sqlite3.connect("auto.db")
conn.execute("""CREATE TABLE IF NOT EXISTS ipasnieks (
             id INTEGER PRIMARY KEY,
             vards TEXT)""")
conn.execute("""CREATE TABLE IF NOT EXISTS auto (
             id INTEGER PRIMARY KEY,
             numurs TEXT,
             razotajs TEXT,
             FOREIGN KEY (id) REFERENCES ipasnieks (id))""")

conn.commit()

def auto_dati():
    for i in range(1, 11):
        auto = ["Rolls-Royce", "Maserati", "Bentley", "Ferrary"]
        vards = f"Īpašnieks {i}"
        razotajs = random.choice(auto)
        N = 2
        numurs = "".join(random.choices(string.ascii_uppercase, k = N)) + str(random.randint(0, 9999))

        conn.execute("INSERT INTO ipasnieks (vards) VALUES (?)", (vards,))
        conn.execute("INSERT INTO auto (razotajs, numurs) VALUES (?, ?)", (razotajs, numurs))
        conn.commit()

# auto_dati()

def datu_izvade(): 

    cursor = conn.execute("""SELECT ipasnieks.id, ipasnieks.vards, auto.id, auto.razotajs, auto.numurs 
    FROM ipasnieks 
    JOIN auto ON ipasnieks.id = auto.id""")  

    for rindas in cursor: 
        print("ID:",rindas[0]) 
        print("Vārds:", rindas[1]) 
        print("Ražotājs:",rindas[3]) 
        print("Numurs:",rindas[4]) 
        print("") 

datu_izvade()