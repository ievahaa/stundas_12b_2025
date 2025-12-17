import sqlite3
from random import randint

conn = sqlite3.connect("pers.db")
conn.execute("""CREATE TABLE IF NOT EXISTS personas (
             id INTEGER PRIMARY KEY,
             vards TEXT)""")

conn.execute("""CREATE TABLE IF NOT EXISTS dati (
             id INTEGER PRIMARY KEY,
             epasts TEXT,
             ip TEXT,
             FOREIGN KEY (id) REFERENCES personas (id))""")
conn.commit()

def datu_generators():
    for i in range(1, 11):
        cilveks = f"Cilvēks{i}"
        epasts = f"cilveks{i}@epasts.com"
        sk = randint(0,255)
        ip = f"80.232.216.{sk}"

        conn.execute("INSERT INTO personas (vards) VALUES (?)", (cilveks,))
        conn.execute("INSERT INTO dati (epasts, ip) VALUES (?, ?)", (epasts, ip))
        conn.commit()

# datu_generators()

#datu izvade
def datu_izvade():
    cursor = conn.execute("""SELECT personas.id, personas.vards, dati.epasts, dati.ip 
                          FROM personas
                          LEFT JOIN  dati ON personas.id = dati.id""")
    for rinda in cursor:
        print("ID:", rinda[0])
        print("Vārds:", rinda[1])
        print("E-pasts:", rinda[2])
        print("IP:", rinda[3])
        print("")
datu_izvade()

#datu dzēšana
def dzest_ierakstu(id):
    conn.execute("DELETE FROM personas WHERE id = ?", (id,))
    conn.commit()
    print(f"Ieraksts ar ID {id} ir izdzēsts.")


#datu  labošana

def labot_ierakstu(id):
    lauks = input("Ko labot? (vārds/epasts/ip)").strip().lower()
    if lauks == "vārds":
        jaunais = input("Jaunais vārds: ")
        conn.execute("UPDATE personas SET vards = ? WHERE id = ?", (jaunais, id))
    elif lauks == "epasts":
        jaunais = input("Jaunais e-pasts: ")
        conn.execute("UPDATE dati SET epasts = ? WHERE id = ?", (jaunais, id))
    elif lauks == "ip":
        jaunais = input("Jaunā IP adrese: ")
        conn.execute("UPDATE dati SET ip = ? WHERE id = ?", (jaunais, id))
    else:
        print("Neatbilstošs lauks.")
        return
    conn.commit()
    print(f"Ieraksts ar ID {id} ir atjaunināts.")



def izvele():
    izvelets= input("Ko vēlies darīt? (d - dzēst, l - labot, n - neko): ").strip().lower()

    if izvelets == "d":
        id = int(input("Kuru ID dzēst? "))
        dzest_ierakstu(id)

    elif izvelets == "l":
        id = int(input("Kuru ID labot? "))
        labot_ierakstu(id)

    else:
        print("Iziet no programmas.")

izvele()