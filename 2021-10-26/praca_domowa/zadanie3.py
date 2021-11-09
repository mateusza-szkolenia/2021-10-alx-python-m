# 3. Przyjmij 3 liczby oznaczajace dlugosci odcinkow i wypisz komunikat, czy da sie z tych odcinkow zbudowac trojkat.
# Jesli sie da to wypisz, czy ten trojkat jest rownoboczny, rownoramienny czy roznoboczny.

a = int(input("Bok A:"))
b = int(input("Bok B:"))
c = int(input("Bok C:"))

if a + b > c and a + c > b and b + c > a:
    print("Da się ułożyć trójkąt")
    if a == b and b == c:
        print("Równoboczny")
    elif a == b or a == c or b == c:
        print("Równoramienny")
    else:  # a != b and b != c and a != c
        print("Różnoboczny")

    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print("Prostokątny")
else:
    print("Nie da się ułożyć trójkąta")
