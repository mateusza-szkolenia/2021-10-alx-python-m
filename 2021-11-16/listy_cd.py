lista = [10, 20, "asdf", [1, 222, 3]]

print(lista[3][1])
lista[3][1] = 1234
print(lista)

print(f"{len(lista) = }")

lista.append("Ala ma kota")  # .append(x) dodaje nową wartość x na koncu listy

print(f"{len(lista) = }")
print(lista)

x = input("Podaj napis:")
lista.append(x)
print(lista)
lista.pop()  # .pop() usuwa ostatnią wartość z listy
print(lista)
