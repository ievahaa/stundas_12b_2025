
# Programma pajautā vārdu un ieraksta to failā vards.txt

vards = input("Ievadi savu vārdu: ")

with open("vards.txt", "w", encoding="utf-8") as f:
    f.write(vards)

print("Vārds ierakstīts failā vards.txt")


# Programma nolasa faila saturu un izdrukā ekrānā

with open("vards.txt", "r", encoding="utf-8") as f:
    saturs = f.read()

print("Faila saturs:")
print(saturs)


# Programma pieraksta jaunu vārdu faila beigās, saglabājot vecos

jauns_vards = input("Ievadi jaunu vārdu: ")

with open("vards.txt", "a", encoding="utf-8") as f:
    f.write("\n" + jauns_vards)

print("Vārds pierakstīts failā vards.txt")


# Programma nolasa faila vardi.txt saturu un izdrukā, cik rindas tajā ir

with open("vards.txt", "r", encoding="utf-8") as f:
    rindas = f.readlines()   # Nolasa visas rindas sarakstā

print("Rindu skaits failā:", len(rindas))


# Programma nolasa faila vardi.txt saturu
# un izdrukā katru rindu ar tā garumu

with open("vards.txt", "r", encoding="utf-8") as f:
    rindas = f.readlines()

for rinda in rindas:
    vards = rinda.strip()  # Noņem atstarpes un \n
    print(vards, "-", len(vards), "burti")



# Programma nolasa failu vards.txt
# un izdrukā tikai tos vārdus, kas sākas ar burtu A

with open("vards.txt", "r", encoding="utf-8") as f:
    rindas = f.readlines()

for rinda in rindas:
    vards = rinda.strip()  # noņem atstarpes un \n
    if vards.startswith("A"):   # pārbauda, vai vārds sākas ar A
        print(vards)
