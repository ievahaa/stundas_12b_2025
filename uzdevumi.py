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

