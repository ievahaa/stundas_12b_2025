import pandas

dati = pandas.read_csv("dzimusie.csv")

meitenes = sum(dati.Sievietes)
zeni = sum(dati.Viriesi)
print(f"Dotajā laika periodā ir piedzimuši {zeni} zēni un {meitenes} meitenes.")

meit_max = max(dati.Sievietes)
zeni_max = max(dati.Viriesi)
print(zeni_max, meit_max)

meit_rinda = dati[dati.Sievietes == meit_max]
print(meit_rinda["Laika periods"])

zeni_rinda = dati[dati.Viriesi == zeni_max]
print(f'Visvairāk zēnu dzimuši laikā: {zeni_rinda["Laika periods"]}')