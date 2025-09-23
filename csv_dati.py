import csv
with open("example.csv", encoding="utf-8") as datu_fails:
    dati = csv.reader(datu_fails) 
    vardi_s = []
    vardi_v = []
    for rinda in dati:
        if rinda[4] == "Female":
            vardi_s.append(rinda[1])
        else:
            vardi_v.append(rinda[1])
    print(vardi_s) 
    print(f"Datnē ir {len(vardi_s)} sieviešu vārdi un {len(vardi_v)} vīriešu vārdi.")
