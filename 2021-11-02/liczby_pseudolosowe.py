# import random
# print(random.randint(1, 10))

from random import randint, random

print(f"{randint(1, 10) = }")  # losowa liczba calkowita z przedzialu 1-10
print(f"{random() = }")  # losowa liczba rzeczywista z przedziału [0.0, 1.0)

# 1. Symulujemy rzut 2 kostkami 6-ściennymi, wypisujemy ich sumę oraz dodatkową informację czy wypadł dublet (2 takie same wartości)
a = randint(1, 6)
b = randint(1, 6)
print(a, b, "razem:", a + b)
if a == b:
    print("Dublet!")
# 2. Po rzucie z prawdopodobieństwem 40% wypisz jakiś komunikat (if randint(1, 10) <= 4:)
