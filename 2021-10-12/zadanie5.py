miasto_A = input("Podaj miasto A:")
miasto_B = input("Podaj miasto B:")
print(f"Będziemy liczyć koszt trasy {miasto_A}-{miasto_B}")
print("Będziemy liczyć koszt trasy", miasto_A, "-", miasto_B)

dystans = int(input(f"Podaj dystans na trasie {miasto_A}-{miasto_B} [km]:"))
spalanie = float(input("Podaj spalanie na 100km [l/100km]:"))
cena_paliwa = float(input("Podaj cenę paliwa [PLN/l]:"))

koszt_przejazdu = dystans / 100 * spalanie * cena_paliwa
print(f"Koszt przejazdu {miasto_A}-{miasto_B} wynosi {koszt_przejazdu} PLN.")
