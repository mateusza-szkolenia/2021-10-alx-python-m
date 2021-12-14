from time import time_ns

slownik = {"ala": "kot"}
print(f"{'ala' in slownik = }")
print(f"{'kot' in slownik = }")

# Napisz program, który przyjmie napis i dla każdej litery tego napisu policzy ile razy wystąpiła.
# alakota
# a -> 3
# l -> 1
# k -> 1
# o -> 1
# t -> 1

# napis = "aaabcbababaa"
with open("tadek.txt", encoding="utf-8") as plik:
    napis = plik.read()

# licznik = {'a': 0, 'b': 0}
licznik = {}

# Rozwiązanie 1.
przed = time_ns()
for znak in set(napis):
    licznik[znak] = 0

# print(licznik)

for znak in napis:
    licznik[znak] += 1 #licznik[znak] = licznik[znak] + 1
po = time_ns()
print(licznik)
print(f"{(po - przed) / 10 ** 9}s")

licznik = {}
# Rozwiązanie 2.
przed = time_ns()
for znak in napis:
    if znak in licznik:
        licznik[znak] += 1
    else:
        licznik[znak] = 1
po = time_ns()
print(licznik)
print(f"{(po - przed) / 10 ** 9}s")