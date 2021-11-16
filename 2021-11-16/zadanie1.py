#przyjmij 10 liczb i wypisz je w odwrotnej kolejności

from time import time

# Część 1.
# Zapamiętujemy podane liczby

czas_przed = time()

liczby = []
i = 0
while len(liczby) < 10:
    x = int(input("Podaj liczbę: "))
    # x = i
    # i += 1
    liczby.append(x)
    # if i % 10000 == 0:
    #     print(i)
#

czas_po = time()

print(liczby)
print(f"Czas liczenia = {czas_po - czas_przed}s")

# Część 2.
# Wypisujemy zawartość listy w odwrotnej kolejności

# liczby.reverse()
# print(liczby)

i = len(liczby) - 1
while i >= 0:
    print(liczby[i])
    i -= 1