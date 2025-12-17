import sqlite3
import uuid

conn = sqlite3.connect("gramatas.db")
conn.execute("""CREATE TABLE IF NOT EXISTS gramatas (
             id TEXT PRIMARY KEY, 
             autora_vards TEXT,
             autora_uzvards TEXT,
             gramatas_nosaukums TEXT)""")
conn.commit()

def datu_ievade():
    myuuid = str(uuid.uuid4())
    vards = input("Ievadi autora vārdu: ")
    uzvards = input("Ievadi autora uzvārdu: ")
    nosaukums = input("Ievadi grāmatas nosaukumu: ")
    conn.execute("INSERT INTO gramatas (id, autora_vards, autora_uzvards, gramatas_nosaukums) VALUES (?, ?, ?, ?)", (myuuid, vards, uzvards, nosaukums))
    conn.commit()

# datu_ievade()

def datu_izvade():
    cursor = conn.execute("SELECT id, autora_vards, autora_uzvards, gramatas_nosaukums FROM gramatas")
    for i in cursor:
        print("ID:", i[0])
        print(f"Autors: {i[1]} {i[2]}")
        print("Nosaukums:", i[3])
        print()

# datu_izvade()

def datu_dzesana(nosaukums):
    apstiprinajums = input(f'Vai tiešām vēlies dzēst visus ierakstus ar "{nosaukums}"? (j/n) ')
    if apstiprinajums == "j":
        conn.execute("DELETE FROM gramatas WHERE gramatas_nosaukums = ?", (nosaukums,))
        conn.commit()
        print(f"Ieraksts ar nosaukumu '{nosaukums}' ir izdzēsts.")

def izvele():
    izvelets= input("Vai vēlies dzēst kādu ierakstu? (j/n)")
    if izvelets == "j":
        while True:
            nos_dzest = input("Kuru ierakstu dzēst? (norādi nosaukumu)")
            try:
                datu_dzesana(nos_dzest)
                break
            except:
                print("Šādu ierakstu neatrod")

# izvele()

def sakums():
    while True:
        ko_darit = input("Ko vēlies darīt: rakstīt datubāzē, lasīt datus, dzēst vai iziet no programmas? (r/l/d/q) ").lower()
        if ko_darit == "r":
            datu_ievade()
        elif ko_darit == "l":
            datu_izvade()
        elif ko_darit == "d":
            izvele()
        elif ko_darit == "q":
            break
        else:
            print("Nekorekta ievade.")

sakums()