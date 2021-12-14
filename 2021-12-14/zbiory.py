pusty = set()
zbior = {1, 2, 3, 2, 3, 5}

print(len(zbior))
print(zbior)
print({1,2,3,4,5})
print({"1","2","3","4","5"})

A = {1, 2, 3}
B = {3, 4, 5}
print(f"{A = }")
print(f"{B = }")
print(f"{A | B = }")
print(f"{A - B = }")
print(f"{A & B = }")

print(zbior)
zbior.add(12)
print(zbior)

if 3 in zbior:
    print("3 jest w zbiorze")
if 4 in zbior:
    print("4 jest w zbiorze")

print(f'{"kot" in "alamakota" = }')
print(list("aaaaaaa"))
print(set("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
