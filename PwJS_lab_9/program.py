#18560 Mateusz Boczarski

import mojeklasy

def testy():
    #Zadanie 1
    #Napisz klase Punkt2D zawierajaca dwa pola x, y definiujace wspolrzedne punktu. Zrealizuj 
    #metode Drukuj(), ktora wydrukuje wspolrzedne. Zrealizuj metode Zeruj(), ktora wyzeruje 
    #wspolrzedne. Pokaz w przykladowym kodzie jak dzialaja utworzone metody na egzemplarzu klasy 
    #(obiekcie).
    print("Zadanie 1")
    
    pkt2D = mojeklasy.Punkt2D(3, 8)
    
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
    
    pkt3D = mojeklasy.Punkt3D(2, 7, 16)
    
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
    
    pkt2D1 = mojeklasy.Punkt2D(1, 4)
    pkt2D2 = mojeklasy.Punkt2D(6, 9)
    odc = mojeklasy.Odcinek(pkt2D1, pkt2D2)
    
    print("Wspolrzedne punktow")
    odc.drukuj()
    print("Dlugosc odcinka:", odc.dlugosc())
    pass

if __name__ == "__main__":
    testy()