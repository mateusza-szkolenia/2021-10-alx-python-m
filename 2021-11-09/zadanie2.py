# Napisać program, który zapyta użytkownika o numer dnia tygodnia
# i napisze co to za dzień.
#
# Przykład:
# Podaj numer dnia tygodnia: 4
# czwartek
#
# (Nie używać ifów)

dni_tygodnia = [None, "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

n = int(input("Podaj numer dnia: "))

print(f"Dzień tygodnia nr {n} to {dni_tygodnia[n]}")
