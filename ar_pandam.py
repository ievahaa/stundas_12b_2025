import pandas as pd

dati = pd.read_csv("2018_Central_Park_Squirrel.csv")

melnas = len(dati[dati["Primary Fur Color"] == "Black"])
rudas = len(dati[dati["Primary Fur Color"] == "Cinnamon"])
pelekas = len(dati[dati["Primary Fur Color"] == "Gray"])

print(f"Parkā ir {melnas} melnās vāveres, {rudas} rudās vāveres un {pelekas} pelēkās vāveres.")


datu_dict = {
    "krāsa": ["melna", "ruda", "pelēka"],
    "skaits": [melnas, rudas, pelekas]
}

df = pd.DataFrame(datu_dict)
df.to_csv("vaveru_skaits.csv")