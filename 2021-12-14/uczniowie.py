uczniowie = {
    "Ania": {"matematyka": 4, "fizyka": 5, "biologia": 3},
    "Janek": {"matematyka": 2, "fizyka": 6, "biologia": 5},
    "Andrzej": {"matematyka": 1, "fizyka": 5, "biologia": 3},
    "Romek": {"matematyka": 5, "fizyka": 4, "biologia": 4, "WF": 1},
    "Kasia": {"matematyka": 6, "fizyka": 1, "biologia": 1}
}

# 1. Wypisz średnią ocen dla każdego ucznia

def srednia(oceny):
    suma = 0
    for p, ocena in oceny.items():
        suma += ocena
    return suma / len(oceny)

for uczen, oceny in uczniowie.items():
    print(uczen, srednia(oceny))

print('-' * 30)

# 2. Wypisz osoby niezdające (1 z jakiegoś przedmiotu) wraz z informacją jakie przedmioty oblała
for uczen, oceny in uczniowie.items():
    oblane = []
    for przedmiot, ocena in oceny.items():
        if ocena == 1:
            oblane.append(przedmiot)
    # if len(oblane) > 0:
    if oblane:
        print(f"{uczen}: {', '.join(oblane)}")