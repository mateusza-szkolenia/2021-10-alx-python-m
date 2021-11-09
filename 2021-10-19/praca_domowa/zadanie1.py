# 1. Napisz program sprawdzajacy czy podana przez uzytkownika liczba
# jest:
# - wieksza od 10
# - mniejsza lub rowna 15
# - podzielna przez 2 (uzyj operatora modulo)

liczba = int(input("Podaj liczbę:"))

print("Większa od 10:", liczba > 10)
print("Mniejsza lub równa 15:", liczba <= 15)
print("Parzysta:", liczba % 2 == 0)