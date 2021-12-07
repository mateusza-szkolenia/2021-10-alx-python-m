from time import time

# odpowiada na pytanie czy n jest liczbą pierwszą
def czy_pierwsza(n):
    if n == 1:
        return False

    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # jeżeli znajdzemy jakikolwiek dzielnik > 1 i < n to na pewno nie jest to liczba pierwsza
    # jeśli nie znajdziemy dzielnka w przedziale od 2 do pierwiastka z n (włącznie) to mamy gwarancję, że już innych dzielników nie ma
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(f"{czy_pierwsza(1) = }")
print(f"{czy_pierwsza(2) = }")
print(f"{czy_pierwsza(3) = }")
print(f"{czy_pierwsza(4) = }")
print(f"{czy_pierwsza(5) = }")
print(f"{czy_pierwsza(121) = }")
print(f"{czy_pierwsza(200000) = }")
przed = time()
x = czy_pierwsza(100000007)
po = time()
print(f"czy_pierwsza(100000007) = {x}")
print(f"Czas: {po - przed:.9f}s")
