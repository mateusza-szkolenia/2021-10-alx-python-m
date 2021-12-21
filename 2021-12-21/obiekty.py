class Osoba:
    # konstruktor - metoda, ktora zostanie automatycznie wywolana zaraz po stworzeniu obiektu
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}.")

    def zmien_imie(self, nowe_imie=None):
        if nowe_imie is None:
            nowe_imie = input("Podaj nowe imie:")
        self.imie = nowe_imie


jan = Osoba("Jan", "Nowak")
print(jan)
print(dir(jan))
print(dir(jan))
jan.przedstaw_sie()
anna = Osoba("Anna", "Kowalska")
anna.przedstaw_sie()
lista = [jan, anna]
print(lista)
lista[0].przedstaw_sie()
jan.zmien_imie("Andrzej")
jan.przedstaw_sie()
jan.zmien_imie()
jan.przedstaw_sie()