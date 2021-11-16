# Korzystając z pętli for, wypisz liczby podzielne przez 3 lub przez 5 z przedziału 1-100.
# Wypisz ile jest tych liczb.

licznik = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        licznik += 1
print(f"Liczb podzielnych przez 3 lub przez 5 w przedziale 1-100 jest {licznik}.")
