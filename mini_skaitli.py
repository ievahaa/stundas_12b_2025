from random import randint

def parbaude(teksts):
    try:
        sk = int(teksts)
        if 1 <= sk <= 50:
            return sk
    except ValueError:
        return None
    return None


def ievade():
    while True:
        teksts = input("Ievadi skaitli no 1 līdz 50: ")
        sk = parbaude(teksts)
        if sk is not None:
            return sk
        print("Nekorekta ievade! Mēģini vēlreiz.")


def spele():
    skaitlis = randint(1, 50)
    meginajumi = 0
    
    while True:
        lietotaja_sk = ievade()
        meginajumi += 1

        if lietotaja_sk < skaitlis:
            print("Par mazu!")
        elif lietotaja_sk > skaitlis:
            print("Par lielu!")
        else:
            print(f"Apsveicu, uzminēji ar {meginajumi}. reizi!")
            break

def main():
    spele()

if __name__ == "__main":
    main()