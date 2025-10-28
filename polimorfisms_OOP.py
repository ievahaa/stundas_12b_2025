#Polimorfisms ir veids kā dažādas klases var koplietot vienus un tos pašus metožu nosaukumus un šīs metodes var izsaukt no vienas un tās pašas vietas

#izveido divas klases

class Suns:
    def __init__(self, vards):
        self.vards = vards

    def runat(self):
        return (f"{self.vards} saka vau!")
    

class Kakis:
    def __init__(self, vards):
        self.vards = vards

    def runat(self):
        return (f"{self.vards} saka mjau!")
    
niko = Suns("Niko")
felikss = Kakis("Felikss")
tobis = Suns("Tobis")

#ar ciklu
for pet in [niko, tobis, felikss]:
    # print(type(pet))
    print(pet.runat())

#ar funkciju
def pet_runat(pet):
    print(pet.runat())

pet_runat(niko)
pet_runat(tobis)
pet_runat(felikss)