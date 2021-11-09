suma = 0
i = 0
while i < 7:
    temp = int(input("Podaj temperaturę: "))
    suma += temp
    i += 1
print(f"Średnia temperatura: {suma / 7:.0f}")
print(f"Średnia temperatura: {suma / 7:.1f}")
print(f"Średnia temperatura: {suma / 7:.2f}")
