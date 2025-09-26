def apstrada_datus(rindas):
    apstradatas = []
    for r in rindas:
        r = r.strip()        
        if r != "":         
            r = r.lower()  
            apstradatas.append(r)
    rezultats = " ".join(apstradatas)
    return rezultats

def main():
    with open("teksts.txt", "r", encoding="utf-8") as f:
        rindas = f.readlines()
    
    rezultats = apstrada_datus(rindas)
    
    print(rezultats)

if __name__ == "__main__":
    main()





# def apstrada_datus(rindas):
#     apstradatas = []
#     for r in rindas:
#         r = r.strip()
#         if r != "":
#             r = r.lower()
#             apstradatas.append(r)
#     rezultats = " ".join(apstradatas)
#     return rezultats

# def skaita_vardus(teksts):
#     vardu_saraksts = teksts.split()
#     return len(vardu_saraksts)

# def main():
#     with open("teksts.txt", "r", encoding="utf-8") as f:
#         rindas = f.readlines()
    
#     rezultats = apstrada_datus(rindas)
#     print(rezultats)
    
#     skaits = skaita_vardus(rezultats)
#     print("Vārdu skaits tekstā:", skaits)

# if __name__ == "__main__":
#     main()
