slownik = {}
print(type(slownik))

prezydent = {"Polska": ("Duda", "Kaczyński"), "USA": "Biden", "klucz": "wartość", "lista": []}
print(prezydent)
print(prezydent["USA"])
print(prezydent["Polska"])

prezydent["lista"].append(17)
print(prezydent)

for x in prezydent:
    print(x, prezydent[x])

# przypisanie do nieistniejącego klucza dodaje ten klucz do słownika
prezydent["Francja"] = "Macron"
print(prezydent["Francja"])

for k, v in prezydent.items():
    print(f"Klucz: {k}, wartość: {v}")
