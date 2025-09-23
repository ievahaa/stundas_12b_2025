# a) Funkcija, kas saskaita rindiņu skaitu failā
def file_line_len(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        rindas = f.readlines()
    return len(rindas)


# b) Funkcija, kas atgriež tikai dzejas rindas
def get_poem_lines(fpath):
    rezultats = []
    with open(fpath, "r", encoding="utf-8") as f:
        for rinda in f:
            rinda = rinda.strip()
            # izlaižam tukšās rindas
            if rinda == "":
                continue
            # izlaižam virsrakstus (pieņemam, ka virsraksti ir tikai lielajiem burtiem)
            if rinda.isupper():
                continue
            # citādi pievienojam kā dzejas rindu
            rezultats.append(rinda)
    return rezultats


# --- Pārbaude ---
print("Rindiņu skaits failā:", file_line_len("veidenbaums.txt"))  # vajadzētu būt 971

poem_lines = get_poem_lines("veidenbaums.txt")
print("Dzejas rindu skaits:", len(poem_lines))
print("Pirmās 5 dzejas rindas:", poem_lines[:5])
