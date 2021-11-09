# 1. Napisz program, ktory na podstawie dwoch podanych liczb obliczy
# wynik zadanej operacji (dodawanie, odejmowanie, mnozenie,
# dzielenie). W przypadku podania nieprawidlowej operacji program
# ma wyswietlic odpowiedni komunikat o bledzie.

a = int(input("Podaj pierwszą liczbę:"))
b = int(input("Podaj drugą liczbę:"))
op = input("Podaj rodzaj operacji:")

if op == '+':
    print(f"{a} {op} {b} = {a + b}")
elif op == '-':
    print(f"{a} {op} {b} = {a - b}")
elif op == '/':
    if b == 0:
        print("Nie dziel przez 0!")
    else:
        print(f"{a} {op} {b} = {a / b}")
else:
    print("Błędna operacja!")