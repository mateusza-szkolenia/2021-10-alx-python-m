uczniowie = {
    "Ania": {"matematyka": 4, "fizyka": 5, "biologia": 3},
    "Janek": {"matematyka": 2, "fizyka": 6, "biologia": 5},
    "Andrzej": {"matematyka": 1, "fizyka": 5, "biologia": 3},
    "Romek": {"matematyka": 5, "fizyka": 4, "biologia": 4, "WF": 1},
    "Kasia": {"matematyka": 6, "fizyka": 5, "biologia": 5}
}

# 1. Wypisz średnią ocen dla każdego ucznia

def srednia(oceny):
    suma = 0
    for p, ocena in oceny.items():
        suma += ocena
    return suma / len(oceny)

print(uczniowie["Ania"]["matematyka"])
for przedmiot, ocena in uczniowie["Ania"].items():
    print(przedmiot, ocena)

print("-" * 30)
for uczen in uczniowie:
    print(uczen, srednia(uczniowie[uczen]))

for uczen, oceny in uczniowie.items():
    print(uczen, srednia(oceny))

# 2. Wypisz osoby niezdające (1 z jakiegoś przedmiotu) wraz z informacją jakie przedmioty oblała