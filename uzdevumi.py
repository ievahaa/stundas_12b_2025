# Izveidot klasi Printeris ar vienu metodi - drukat(). Metodes mērķis ir izdrukāt tekstu

class Printeris:
    def __init__(self, teksts):
        self.teksts = teksts

    def drukat(self):
        print(self.teksts)

printeris = Printeris("Kas jauns?")
printeris.drukat()

# Uzraksti programmu saskaņā ar objektorientētās programmēšanas noteikumiem, kurā ir definēta klase Skaititajs ar vienu metodi skaitli()! Metodes mērķis ir izdrukāt secīgus skaitļus, sākot no skaitļa 1. Izdrukājamo skaitļu skaits ir dots kā metodes parametrs, un to ievada lietotjs.

class Skaititajs:
    def skaitli(self, skaitlis):
        for i in range (1, skaitlis + 1):
            print(i)


skaitli = int(input("Cik skaitļus izdrukāt?"))
skaititajs = Skaititajs()
skaititajs.skaitli(skaitli)


#Cilveks
class Cilveks:
    def __init__(self, vards, uzvards, vecums=0):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums

    def info(self):
        print("Vārds: ", self.vards)
        print("Uzvārds:", self.uzvards)
        print("Vecums:", self.vecums)

cilveks = Cilveks("Jānis", "Bērziņš", 23)
cilveks.info()

class Skolens(Cilveks):
    def __init__(self, vards, uzvards, klase, skola, vecums=0):
        super().__init__(vards, uzvards, vecums)
        self.klase = klase
        self.skola = skola

    def info_skolens(self):
        print("Klase:", self.klase)
        print("Skola:", self.skola)

skolens = Skolens("Jānis", "Bērziņš", "5.a", "Salaspils 1. vidusskola", 11)
skolens.info()
skolens.info_skolens()