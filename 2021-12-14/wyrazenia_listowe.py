lista = []
for i in range(1, 10):
    lista.append(i ** 2)

lista2 = [i ** 2 for i in range(1, 10)]

print(lista)
print(lista2)
print([i ** 3 for i in range(1, 10)])

napis = "alamakota"
slownik = {}
for x in set(napis):
    slownik[x] = 0
print(slownik)
print({x: 0 for x in set(napis)})

print([x * y for x in range(1, 4) for y in range(2, 5)])

podzielne = []
for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        podzielne.append(i)
print(podzielne)
print([i for i in range(1, 21) if i % 3 == 0 or i % 5 == 0])

print(f"lista = {[int(input('Podaj liczbę:')) for _ in range(5)]}")