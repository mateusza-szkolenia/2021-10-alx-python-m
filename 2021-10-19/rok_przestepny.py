# Napisz program, ktory sprawdzi, czy podany rok jest rokiem przestępnym.
# Latami przestępnymi są te, których numeracja:
#  - jest podzielna przez 4 i niepodzielna przez 100 lub
#  - jest podzielna przez 400
rok = int(input("Podaj rok"))
if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    print(f"Rok {rok} jest przestępny.")
else:
    print(f"Rok {rok} nie jest przestępny.")
