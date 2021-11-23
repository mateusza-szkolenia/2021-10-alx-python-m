def hello():
    print("Hello")
    print("Is it me you're looking for?")


def argument(x):
    print(f"Podany argument to {x}")

argument(5)
argument("Władimir Putin")


def fizz(i):
    czy_cos_wypisalismy = False
    if i % 3 == 0:
        print("Fizz", end="")
        czy_cos_wypisalismy = True
    if i % 5 == 0:
        print("Buzz", end="")
        czy_cos_wypisalismy = True
    if not czy_cos_wypisalismy:
        print(i, end="")
    print()

#
# for i in range(1, 101):
#     fizz(i)

def kwadrat(x):
    return x * x

x = kwadrat(3)
print(x)
print(f"{kwadrat(17) = }")


def podzielne(n, k):
    return n % k == 0


if podzielne(15, 3):
    print("15 jest podzielne przez 3")
else:
    print("15 nie jest podzielne przez 3")


# suma_cyfr(n) zwraca sumę cyfr liczby n
def suma_cyfr(n):
    suma = 0
    while n != 0:
        suma += n % 10
        n = n // 10
    return suma

print(f"{suma_cyfr(125364) = }")

def ile_razy_suma_cyfr(x):
    i = 0
    while x > 9:
        x = suma_cyfr(x)
        i += 1
    return i

print(f"{ile_razy_suma_cyfr(99999999999999999999999999999999999999) = }")
