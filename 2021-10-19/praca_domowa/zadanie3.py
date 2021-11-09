# 3*. Przyjmij 3 liczby calkowite oznaczajace liczbe godzin (0-23) i minut (0-59) na zegarze
# elektronicznym (24-godzinnym) oraz liczbe minut X
# Wypisz jaka godzina wyswietli sie na zegarze po uplynieciu X minut.
#
# Przyklad:
# Podaj godzine: 12
# Podaj minute: 47
# Podaj ile minut uplynelo: 15
# 13:02

godz = int(input("Podaj godzinę:"))
min = int(input("Podaj minutę:"))
x = int(input("Podaj ile minut upłynęło:"))

# 13:50, 100
min = min + x  # 150
godz = godz + min // 60
min = min % 60
godz = godz % 24

print(f"{godz}:{min}")
