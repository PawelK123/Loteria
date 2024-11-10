import random
LISTA_LICZB = []
LICZBY_DO_LOSOWANIA = [LISTA_LICZB.append(i) for i in range(0,26)]
class Loteria:
    def __init__(self,lista_liczb):
        self.lista_liczb = lista_liczb
        self.wybrane_liczby = []
        self.kasa = 50
        self.wygrywajace = []
    def wybierz(self):
        for i in range(5):
            liczba = int(input("Podaj liczbę z zakresu 1-25 "))
            self.wybrane_liczby.append(liczba)
    def losuj(self):
        for i in range(5):
            k = random.choice(self.lista_liczb)
            if k in self.wygrywajace:
                k = random.choice(self.lista_liczb)
            self.wygrywajace.append(k)
        print(self.wygrywajace)
    def sprawdz(self):
        self.liczba_trafionych_liczb = set(self.wybrane_liczby).intersection(set(self.wygrywajace))
        if len(self.liczba_trafionych_liczb) == 0:
            print("Brak trafień!")
            self.wygrana = False
        elif len(self.liczba_trafionych_liczb) == 1:
            print("1 trafiona liczba!")
            self.wygrana = True
        elif len(self.liczba_trafionych_liczb) == 2:
            print("2 trafione liczby!")
            self.wygrana = True
        elif len(self.liczba_trafionych_liczb) == 3:
            print("3 trafione liczby!")
            self.wygrana = True
        elif len(self.liczba_trafionych_liczb) == 4:
            print("4 trafione liczby")
            self.wygrana = True
        elif len(self.liczba_trafionych_liczb) == 5:
            print("5 trafione liczby")
            self.wygrana = True
    def resetuj(self):
        self.wybrane_liczby = []
        self.wygrywajace = []
    def aktualizuj_kase(self):
        if self.wygrana == True:
            if len(self.liczba_trafionych_liczb) == 1:
                self.kasa += 1
            elif len(self.liczba_trafionych_liczb) == 2:
                self.kasa += 5
            elif len(self.liczba_trafionych_liczb) == 3:
                self.kasa += 10
            elif len(self.liczba_trafionych_liczb) == 4:
                self.kasa += 20
            elif len(self.liczba_trafionych_liczb) == 5:
                self.kasa += 50
        else:
            self.kasa -= 10
    def __repr__(self):
        return f"Twoje aktualne saldo to {self.kasa}zł, wygrywajace liczby to {self.wygrywajace} \ntwoje liczby to {self.wybrane_liczby}"
print("witaj w Loteri!")

gra = input(f"Twoje saldo wynosi 50zl Czy chcesz zagrać? Los kosztuje 10 zł Tak/Nie ").lower()
loteria = Loteria(LISTA_LICZB)
while gra == "tak":
    wybrane_liczby = []
    loteria.wybierz()
    loteria.losuj()
    loteria.sprawdz()
    loteria.aktualizuj_kase()
    print(loteria)
    loteria.resetuj()
    if loteria.kasa <= 0:
        gra = "nie"
    else:
        gra = input("Czy chcesz dalej grać? Los kosztuje 10 zł Tak/Nie ").lower()






