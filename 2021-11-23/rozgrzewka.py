# Wypisz liczby 1-100, ale
# Zamiast liczb podzielnych przez 3 wypisz "Hopsasa"
# Zamiast liczb podzielnych przez 5 wypisz "Tralala"
# jeśli liczba jest podzielna przez 3 i przez 5 to wypisz "HopsasaTralala"
# 1
# 2
# Hopsasa
# 4
# Tralala
# Hopsasa
# 7
# 8
# Hopsasa
# Tralala
# 11
# Hopsasa
# 13
# 14
# HopsasaTralala

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("HopsasaTralala")
#     elif i % 3 == 0:
#         print("Hopsasa")
#     elif i % 5 == 0:
#         print("Tralala")
#     else:
#         print(i)

for i in range(1, 110):
    czy_cos_wypisalismy = False
    if i % 3 == 0:
        print("Hopsasa", end="")
        czy_cos_wypisalismy = True

    if i % 5 == 0:
        print("Tralala", end="")
        czy_cos_wypisalismy = True

    if i % 7 == 0:
        print("Bum", end="")
        czy_cos_wypisalismy = True

    # jeśli nic nie wypisalismy dla `i` to wypisujemy `i`
    if not czy_cos_wypisalismy:
        print(i, end="")

    print()