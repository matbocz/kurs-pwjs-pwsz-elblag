#18560 Mateusz Boczarski

import math

def testy():
    #Zadanie 1
    #Napisz klase Punkt2D zawierajaca dwa pola x, y definiujace wspolrzedne punktu. Zrealizuj 
    #metode Drukuj(), ktora wydrukuje wspolrzedne. Zrealizuj metode Zeruj(), ktora wyzeruje 
    #wspolrzedne. Pokaz w przykladowym kodzie jak dzialaja utworzone metody na egzemplarzu klasy 
    #(obiekcie).
    print("Zadanie 1")
    
    pkt2D = Punkt2D(3, 8)
    
    print("Przed wyzerowaniem")
    pkt2D.drukuj()
    
    print("Po wyzerowaniu")
    pkt2D.zeruj()
    pkt2D.drukuj()
    
    #Zadanie 2
    #Napisz klase Punkt3D, ktora dziedziczy po klasie Punkt2D. Klasa Punkt3D powinna miec 
    #dodatkowe pole (wzgledem klasy Punkt2D), ktore okresla trzecia wspolrzedna z. Sprawdz jak dzialaja 
    #metody Drukuj() i Zeruj()? Popraw metody tak aby drukowaly i zerowaly wszystkie wspolrzedne. 
    #Pokaz w przykladowym kodzie jak dzialaja utworzone metody na egzemplarzu klasy (obiekcie).
    print("\nZadanie 2")
    
    pkt3D = Punkt3D(2, 7, 16)
    
    print("Przed wyzerowaniem")
    pkt3D.drukuj()
    
    print("Po wyzerowaniu")
    pkt3D.zeruj()
    pkt3D.drukuj()
    
    #Zadanie 3
    #Utworz klase Odcinek() i wykorzystaj w niej do okreslenia wspolrzednych odcinka 
    #Punkt2D.  Napisz metode zwracajaca dlugosc odcinka. Pokaz w przykladowym kodzie jak dzialaja 
    #utworzone metody na egzemplarzu klasy (obiekcie).
    print("\nZadanie 3")
    
    pkt2D1 = Punkt2D(1, 4)
    pkt2D2 = Punkt2D(6, 9)
    odc = Odcinek(pkt2D1, pkt2D2)
    
    print("Wspolrzedne punktow")
    odc.drukuj()
    print("Dlugosc odcinka:", odc.dlugosc())
    pass

class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def drukuj(self):
        print("x =", self.x, "y =", self.y)
    
    def zeruj(self):
        self.x = 0
        self.y = 0

class Punkt3D(Punkt2D):
    def __init__(self, x, y, z):
        Punkt2D.__init__(self, x, y)
        self.z = z
    
    def drukuj(self):
        print("x =", self.x, "y =", self.y, "z =", self.z)
    
    def zeruj(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Odcinek:
    def __init__(self, pkt1, pkt2):
        self.x1 = pkt1.x
        self.y1 = pkt1.y
        self.x2 = pkt2.x
        self.y2 = pkt2.y
        
    def drukuj(self):
        print("x1 =", self.x1, "y1 =", self.y1)
        print("x2 =", self.x2, "y2 =", self.y2)
        
    def dlugosc(self):
        return math.sqrt(pow((self.x2 - self.x1), 2) + pow((self.y2 - self.y1), 2))

if __name__ == "__main__":
    testy()