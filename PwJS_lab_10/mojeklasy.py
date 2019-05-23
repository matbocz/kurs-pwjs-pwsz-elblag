#18560 Mateusz Boczarski

def testy():
    #Zadanie 1
    #Zdefiniuj klase Student(), ktora zawiera pola (niestatyczne): imie, nazwisko, nr_indeksu, 
    #kierunek. Klasa ma posiadac __init__(), w ktorym podczas tworzenia instancji (obiektu) przypisywane 
    #beda wartosci do wskazanych pol. Pole nr_indeksu powinno byc prywatne. Pokaz na obiekcie, ze nie 
    #mozna sie do tego pola odwolac. Poslugujac sie przeciazona metoda __str__() napisz procedure 
    #drukujaca pola obiektu (w kodzie procedury bez print()) przy podaniu obiektu do print().
    print("Zadanie 1")
    
    s1 = Student("Jan", "Kowalski", 1885, "IE")
    
    print(s1.imie)
    print(s1.nazwisko)
    print(s1.kierunek)
    #print(s1.__nr_indeksu) - 'Student' object has no attribute '__nr_indeksu'
    print(s1)
    
    #Zadanie 2
    #Dla klasy Student() z zad.1 napisz przeciazona metode porownujaca dwa obiekty: 
    #mniejszy->wiekszy oraz rowny->rowny. Procedury maja porownywac pola zawierajace imiona i 
    #nazwiska, np. jezeli stduent1 ma nazwisko Adamczyk a student2 ma nazwisko Bakula metoda ma 
    #zwracac True (bo student1 < student2).
    print("\nZadanie 2")
    
    s2 = Student("Kamil", "Nowak", 1825, "IP")
    
    print(s1.__lt__(s2))
    print(s1.__eq__(s2))
    
    #Zadanie 3
    #Dodaj do klasy Student() prywatne pole statyczne o nazwie licznik. Napisz metode 
    #getLicznik(), ktora bedzie zwracala wartosc licznika. Pokaz, ze licznik funkcjonuje przy wywolaniu dla 
    #3 obiektow.
    print("\nZadanie 3")
    
    s3 = Student("Bartosz", "Kogut", 1878, "IE")
    
    print("Licznik: %s"%(s3.getLicznik()))
    
    #Zadanie 4
    #Zdefiniuj klase StudentInformatyki(), ktora dziedziczy po klasie Student(). Student 
    #informatyki jawnie wykorzystuje konstruktor klasy Student() (super()). Dodatkowo ma pole 
    #specjalnosc a pole kierunek wypelnione jest wstepnie wartoscia ,,IIS".
    print("\nZadanie 4")
    
    s4 = StudentInformatyki("Mariusz", "Mroz", 1971, "", "Bazy danych")
    
    print(s4.imie)
    print(s4.nazwisko)
    print(s4.kierunek)
    print(s4.specjalnosc)
    
    pass

class Student:
    __licznik = 0
    
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek
        
    def getLicznik(self):
        return self.__licznik
    
    def __lt__(self, other):
        if self.nazwisko < other.nazwisko:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.nazwisko == other.nazwisko:
            return True
        else:
            return False
    
    def __str__(self):
        return "Imie: %s, Nazwisko: %s, Nr_indeksu: %d, Kierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)

class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki, self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "IIS"
        self.specjalnosc = specjalnosc

if __name__ == "__main__":
    testy()