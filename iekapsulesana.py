# Iekapsulēšana ir viena no galvenajām OOP īpašībām. Tā neļaujārējām klasēm piekļūt konkrētās klases atribūtiem vai metodēm un mainīt tos. Ar to iespējams paslēpt datus.
# izmanto vienu vai divas zemsvītras

#definē klasi
class Dog:
    def __init__(self):
        #klases privātās īpašības
        self.__vards = "Reksis"
        self.__vecums = 6

    #privātās īpašības vērtibas maiņa
    def iedot_vardu(self, vards):
        self.__vards = vards

    #privātās īpašības vērtibas maiņa
    def set_age(self, vecums):
        self.__vecums = vecums

    #klases īpašību drukāšana
    def show_info(self):
        print(f"Sunim \"{self.__vards}\" ir {self.__vecums} gadi.")

#izveido objektu
dog = Dog()

print("Sākotnējās klases īpašības vērtība:")
dog.show_info()

print("Neveiksmīgs mēģinājums mainīt klases īpašības vērtību:")
dog.vards = "Tontons"
dog.vecums = 8
dog.show_info()

print("Veiksmīgs mēģinājums mainīt klases īpašības vērtību:")
dog.iedot_vardu("Tontons")
dog.set_age(8)
dog.show_info()