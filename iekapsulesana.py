#iekapsulēšana jeb inkapsulācija neļauj no ārpuses piekļūt klases atribūtiem un metodēm. Izmanto vienu vai divas zemsvītras

class Suns:
    def __init__(self, saimnieks):
        self.saimnieks = saimnieks
        #klases privātās īpašības
        self.__vards = "Lorīna"
        self.__vecums = 6

    #privātās īpašības vērtības maiņa
    def noradit_vardu(self, vards):
        self.__vards = vards

    #privātās īpašības vērtības maiņa
    def noradit_vecumu(self, vecums):
        self.__vecums = vecums

    #klases īpašību drukāšana
    def info(self):
        print(f"Sunim \"{self.__vards}\" ir {self.__vecums} gadi. Suņa saimnieks ir {self.saimnieks}.")

#izveido objektu
suns = Suns("Jānis")
suns2 = Suns("Ilze")

print("Sākotnējās klases īpašību vērtības:")

suns.info()
suns2.info()
print("Neveiksmīgs mēģinājums mainīt klases īpašību vērtības.")

suns.__vards = "Kaspers"
suns.__vecums = 8

suns.info()

print("Veiksmīgs mēģinājums mainīt klases īpašību vērtības:")
suns2.noradit_vardu("Kaspers")
suns2.noradit_vecumu(8)

suns2.info()