print("Początek")

x = int(input("Liczba:"))

if x > 10:
    print("Jestem wewnątrz ifa")
    print("Ja też!")
    print("Liczba większa od 10")
elif x > 5:
    print("Liczba wieksza od 5, ale mniejsza lub równa 10")
elif x > 3:
    print("Liczba wieksza od 3, ale mniejsza lub równa 5")
elif x > 0:
    print("Liczba wieksza od 0, ale mniejsza lub równa 3")
else:
    print("Liczba niedodatnia")

print("Koniec")

# składnia:
# if warunek1:
#     kod - wykona się jeśli warunek1 jest prawdziwy
# elif warunek2:  # po ifie może nastąpić dowolnie wiele bloków elif (w szczególności 0)
#     kod - wykona się jeśli warunek2 jest prawdziwy, ale warunek1 nie był
# else:  # po ewentualnych elifach może wystąpić jeden blok else, który wykona się, jeśli żaden z warunków powyżej nie był prawdziwy
#     kod