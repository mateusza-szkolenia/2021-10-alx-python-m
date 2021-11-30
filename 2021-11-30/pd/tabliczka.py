#     0  1  2  3  4  5  6  7  8  9

# 0   0  0  0  0  0  0  0  0  0  0
# 1   0  1  2  3  4  5  6  7  8  9
# 2   0  2  4  6  8 10 12 14 16 18
# 3   0  3  6  9 12 15 18 21 24 27
# 4   0  4  8 12 16 20 24 28 32 36
# 5   0  5 10 15 20 25 30 35 40 45
# 6   0  6 12 18 24 30 36 42 48 54
# 7   0  7 14 21 28 35 42 49 56 63
# 8   0  8 16 24 32 40 48 56 64 72
# 9   0  9 18 27 36 45 54 63 72 81

def wypisz_wiersz(nr_wiersza):
    for kolumna in range(10):
        wynik = nr_wiersza * kolumna
        print(f"{wynik:3}", end="")
    print()

# wypisujemy pierwszy wiersz
print(" " * 3, end="")
for kolumna in range(10):
    print(f"{kolumna:3}", end="")
print()
print()

for wiersz in range(10):
    # wypisujemy numer wiersza
    print(wiersz, end="  ")

    # wypisujemy wiersz
    wypisz_wiersz(wiersz)
    # for kolumna in range(10):
    #     wynik = wiersz * kolumna
    #     print(f"{wynik:3}", end="")
    # print()
