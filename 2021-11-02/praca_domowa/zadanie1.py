# 1. user podaje liczby lub napis "koniec"
# 2. user poda co najmniej 1 liczbę
# po przyjęciu liczb od użytkownika chcemy wypisać największą i najmniejszą z nich

najwieksza = None
najmniejsza = None
while True:
    x = input("Podaj liczbę lub 'koniec':")
    if x == "koniec":
        break

    x = int(x)
    if najwieksza is None or x > najwieksza:
        najwieksza = x
    if najmniejsza is None or x < najmniejsza:
        najmniejsza = x

if najwieksza is None:
    print("Nie podano żadnej liczby!")
else:
    print(f"Największa liczba to {najwieksza}")
    print(f"Najmniejsza liczba to {najmniejsza}")