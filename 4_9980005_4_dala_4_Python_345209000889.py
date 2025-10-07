import requests
import sys
import json

pieprasijums = requests.get('https://pro2025.azurewebsites.net/books')
if pieprasijums.status_code == 200:
    print("Pieprasījums ir veiksmīgs")
else:
    sys.exit()
dati = pieprasijums.json()

#############################################################

for rinda in dati:
    print(f"Grāmata '{rinda["name"]}' ({rinda["year_published"]}), {rinda["quantity"]} lpp.")

print()
#############################################################

with open("nosaukumi.json", "w") as f:
    for rinda in dati:
        f.write("Nosaukums: ")
        f.write(f'{rinda["name"]}\n')

print()
##############################################################

gadi = []
for rinda in dati:
   gadi.append(rinda["year_published"])

minimala_vertiba = min(gadi, key=len)
for rinda in dati:
    if rinda["year_published"] == minimala_vertiba:
        print(f"Visvecāko grāmatu uzrakstīja {rinda["author"]}, {minimala_vertiba} gadā.")
print()
####################################################################

kopejais_lpp_skaits = 0
kopeja_cena = 0
for rinda in dati:
    kopejais_lpp_skaits += int(rinda["pages"])
    kopeja_cena += int(rinda["price"])
    videja_cena = round(kopeja_cena / len(dati), 2)

print(f"Kopējais lappušu skaits ir {kopejais_lpp_skaits} lpp.")
print(f"Vidēja cena visām grāmatām ir {videja_cena} EUR.")

print()
#######################################################################

def garakais_nosaukums():
    visi_nosaukumi = []
    for rinda in dati:
        visi_nosaukumi.append(rinda["name"])
    tuple_elementi = tuple(visi_nosaukumi)
    lielakais_nosaukums = max(tuple_elementi, key=len)
    for rinda in dati:
        if rinda["name"] == lielakais_nosaukums:
            autors = rinda["author"]
            gads = rinda["year_published"]
    return print(f"Grāmata ar lielāko nosaukumu ir '{lielakais_nosaukums}' ({gads}), kuru uzrakstija {autors}")

garakais_nosaukums()
print()

#######################################################################
