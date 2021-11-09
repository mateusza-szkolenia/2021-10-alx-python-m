# 1. Wypisz cyfrę jedności liczby x
x = 55624
cyfra_jednosci = x % 10 # 4
print(f"{cyfra_jednosci = }")

# 2. Wypisz cyfrę dziesiątek
dziesiatki = x // 10 % 10
print(f"{dziesiatki = }")
setki = x // 10 // 10 % 10
print(f"{setki = }")

# 3. Policz sumę cyfr liczby x
suma = 0
while x != 0:  # dopoki zostaly jakies cyfry:
    print(f"{x = }")
    suma += x % 10  # dodaj cyfrę jedności do sumy
    x = x // 10  # utnij cyfrę jednosci z liczby

print(f"{suma = }")