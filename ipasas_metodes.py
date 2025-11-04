# Magic/ Dunder - atļauj izmantot iebūvētās funkcijas

mylist = [1, 2, 3, 4]
print(len(mylist))

class Piemers:
    pass

piemers = Piemers()
# len(piemers) - izdod kļūdu

print(piemers)

class Gramata:
    def __init__(self, nosaukums, autors, lpp):
        self.nosaukums = nosaukums
        self.autors = autors
        self.lpp = lpp

    def __str__(self):
        return f"Grāmatu \"{self.nosaukums}\" sarakstījis {self.autors}."
    
    def __len__(self):
        return self.lpp
    
    def __del__(self):
        print("Objekts ir izdzēsts.")

gramata = Gramata("Zelta zirgs", "Rainis", 300)
print(gramata)
print(len(gramata))
del(gramata)

# print(gramata)