# 2. Przyjmij 2 liczby, N oraz K, i wypisz czy N jest podzielne przez K.
n = int(input("Podaj N:"))
k = int(input("Podaj K:"))
if k == 0:
    print("Nie dziel przez zero!")
else:
    print("Podzielne:", n % k == 0)
