# N = int(input("Podaj liczbe: "))
N = 567856437868 ** 1723

kroki = 0
while True:
    suma = 0
    kroki += 1
    while N > 0:
        suma += N % 10
        N //= 10
        # print(f"{N=} {suma=}")
    # print(f"Ostateczna {suma=}")
    N = suma
    if suma < 10:
        break

print(kroki)
