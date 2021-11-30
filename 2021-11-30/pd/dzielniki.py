def dzielniki(n):
    lista = []
    for i in range(1, n + 1):
        if n % i == 0:
            lista.append(i)
    return lista

def dzielniki_fast(n):
    lista = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lista.append(i)
            lista.append(n // i)
    lista.sort()
    return lista

print(dzielniki(24))

# import math
# print(math.sqrt(2))
# print(2 ** 0.5)

from time import time
przed = time()
# d = dzielniki(1000000007)
d = dzielniki_fast(1000000000)
po = time()
print(d)
print(f"Czas {po - przed}s")

