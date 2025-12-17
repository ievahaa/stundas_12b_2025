def saskaiti(sk1, sk2):
    return sk1+sk2

def atnem(sk1, sk2):
    return sk1-sk2

def reiz(sk1, sk2):
    return sk1*sk2

def dali(sk1, sk2):
    return sk1/sk2

print(saskaiti(3, 8))
print(atnem(3, 8))
print(reiz(3, 8))
print(dali(3, 8))

def kalkulators(sk1, sk2, operat):
    return operat(sk1, sk2)

print(kalkulators(2, 6, reiz))
print(kalkulators(45, 3, dali))

#Kas ir @ - Python dekorators
# nested function

# def areja_funkcija():
#     print("Es esmu ārējā funkcija")

#     def iekseja_funkcija():
#         print("Es esmu iekšējā funkcija")
#     #var izsaukt tikai caur ārējo funkciju
#     iekseja_funkcija()

# areja_funkcija()

# funkcijas var tikt izsauktas no citām funkcijām

def areja_funkcija():
    print("Es esmu ārējā funkcija")
    
    def iekseja_funkcija():
        print("Es esmu iekšējā funkcija")
    #var izsaukt tikai caur ārējo funkciju
    return iekseja_funkcija

ieks_fja = areja_funkcija()
ieks_fja()

# dekoratori
import time

def decorator_funkcija(function):
    def wrapper_function():
        function()


#izveido vienkāršu funkciju
def sveiki():
    time.sleep(2) #pieliek aizturi
    print("Sveiki!")

sveiki()

#Izveido vairākas līdzīgas funkcijas - kā uzlikt aizturi visām
def aizkave_decorator(function):
    def wrapper_function():
        time.sleep(3)
        function()
    return wrapper_function


def labdien():
    print("Labdien!")

@aizkave_decorator
def labrit():
    print("Labrit!")

@aizkave_decorator
def labvakar():
    print("Labvakar!")

labdien()
labrit()
labvakar()