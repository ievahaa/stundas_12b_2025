class Masina:
    def __init__(self, marka, gads):
        self.marka = marka
        self.gads = gads
        self.iepirkuma_gads = 2025

    def info(self):
        print(f"Automašīna: {self.marka}, izlaiduma gads {self.gads}")

    def brauc(self, atrums):
        print(f"Automašīna {self.marka} brauc ar ātrumu {atrums} km/h.")

auto1 = Masina("Jaguar", 2023) #objekts jeb instance
auto2 = Masina("Triumph", 1946)

print(auto1.marka, auto1.gads)
print(auto2.marka)

auto1.info()
auto1.brauc(90)

auto3 = Masina("MAN", 2014)
auto3.brauc(120)

auto3.gads = 2015
print(auto3.gads)

#Mantošana - viens no OOP pamatprincipiem
class Dzivnieks:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    def est(self):
        print("es gribu ēst")

    def gulet(self):
        print("es gribu gulēt")

    def mainit(self):
        print("es mainu kažoku")


dzivienks1 = Dzivnieks("lācis")
print(dzivienks1.nosaukums)
dzivienks1.est()

class Suns(Dzivnieks):
    def riet(self):
        print("Es varu riet")
    
    def mainit(self):
        print("Es mainu saimnieku")

suns1 = Suns("suns")
suns1.riet()
suns1.gulet()
suns1.mainit()
dzivienks1.mainit()
