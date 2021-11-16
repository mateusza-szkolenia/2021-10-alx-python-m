lista = [10, 20, 30, 40, 50]

# i = 0
# while i < len(lista):
#     print(lista[i])
#     i += 1

for x in lista:
    print(x)

for litera in "alamakota":
    print(litera)
    

print(list(range(10)))  # range(10) == range(0, 10)
print(list(range(3,10)))
print(list(range(0, 10, 2)))

for i in range(10):
    print(f"{i = }")

for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")
