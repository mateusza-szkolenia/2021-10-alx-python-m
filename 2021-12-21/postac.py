from random import randint

class Przedmiot:
    def __init__(self, nazwa, bonus_atk):
        self.nazwa = nazwa
        self.bonus_atk = bonus_atk


class Postac:
    def __init__(self, imie, sila_ataku, max_hp):
        self.imie = imie
        self.atak = sila_ataku
        self.max_hp = max_hp
        self.hp = max_hp
        self.ekwipunek = []
    
    # wypisuje informacje na temat postaci, np.
    # Rufus, 5 ATK, 67/100 HP
    def wypisz_info(self):
        print(f"{self.imie}, {self.atak_z_bonusami()}({self.atak}) ATK, {self.hp}/{self.max_hp} HP")
    
    # odejmuje n od obecnego zdrowia postaci. Zdrowie nie może zejść poniżej 0
    def otrzymaj_obrazenia(self, n):
        self.hp -= n
        if self.hp < 0:
            self.hp = 0
    
    #  zwraca (return) informację, czy Postać żyje
    def czy_zyje(self):
        return self.hp > 0
    
    # leczy n punktów zdrowia. Zdrowie nie może przekroczyć wartości maksymalnej.
    # Nie robi nic jeśli postać nie żyje.
    def wylecz(self, n):
        if self.czy_zyje():
            self.hp += n
            if self.hp > self.max_hp:
                self.hp = self.max_hp

    # zwraca losową wartość całkowitą 0.5 * ATK <= N <= 1.5 ATK
    def zaatakuj(self):
        return randint(int(0.5 * self.atak_z_bonusami()), int(1.5 * self.atak_z_bonusami()))


    def daj_przedmiot(self, p: Przedmiot):
        self.ekwipunek.append(p)

    # Zwraca wartość ataku powiększoną o bonusy z ekwipunku
    def atak_z_bonusami(self):
        wynik = self.atak
        for p in self.ekwipunek:
            wynik += p.bonus_atk
        return wynik

def walka(postac1: Postac, postac2: Postac):
    while postac1.czy_zyje() and postac2.czy_zyje():
        postac1.otrzymaj_obrazenia(postac2.zaatakuj())
        postac2.otrzymaj_obrazenia(postac1.zaatakuj())

kij = Przedmiot("Kij od szczotki", 3)

rufus = Postac("Rufus", 4, 120)
rufus.daj_przedmiot(kij)
andrzej = Postac("Andrzej", 6, 85)
walka(rufus, andrzej)
rufus.wypisz_info()
andrzej.wypisz_info()
# rufus.wypisz_info()
# rufus.otrzymaj_obrazenia(70)
# rufus.wypisz_info() # Rufus, 4 ATK, 50/120 HP
# rufus.wylecz(5)
# rufus.wypisz_info() # Rufus, 4 ATK, 55/120 HP
# rufus.otrzymaj_obrazenia(70)
# rufus.wypisz_info() # Rufus, 4 ATK, 0/120 HP
# rufus.wylecz(5)
# rufus.wypisz_info() # Rufus, 4 ATK, 0/120 HP
