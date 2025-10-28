# abstraksta klase nozīmē, ka no tās netiks izveidots objekts (instance)
# tā tiek izmantota kā pamata klase (base)

class Animal:
    def __init__(self, vards):
        self.vards = vards

    def runat(self):
        raise NotImplementedError("Apakšklasei būtu jāimplementē šī abstraktā metode")

# my_animal = Animal("my animal")
# print(my_animal.runat())

# Tā vietā izmanto abstraktās klases mantošanu
class Suns(Animal):
    def runat(self):
        return f"{self.vards} saka vau!"
    

class Kakis(Animal):
    def runat(self):
        return f"{self.vards} saka mjau!"


bobis = Suns("Bobis")
muris = Kakis("Muris")
print(bobis.runat())
print(muris.runat())