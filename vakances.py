import pandas

dati = pandas.read_csv("vakances.csv", encoding="utf-8")

kategorijas = dati.Vakances_kategorija.unique()
for i in kategorijas:
    print(i, len(kategorijas))







vakances = (
    dati.groupby("Vakances_kategorija")
      .agg(Vakances_skaits=("Vakances_Nr", "count"),
           Videja_alga=("Alga_no", "mean"))
      .sort_values(by="Vakances_skaits", ascending=False)
)

print(vakances)
