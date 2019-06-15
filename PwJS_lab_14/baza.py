import sqlite3 as sql

if __name__ == "__main__":
    #Tworzenie tabeli
    con = sql.connect('database.db')
    print("BD otwarta")
    	
    con.execute('CREATE TABLE pracownicy (imienazwisko TEXT, nrpracownika TEXT, adres TEXT)')
    print("Tabela utworzona")
    	
    con.close()
    print("BD zamknieta")
    
    
    #Wypelnianie tabeli
    con = sql.connect('database.db')
    print("\nBD otwarta")
    	
    cur = con.cursor()
    print("Kursor otwarty")
    	
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?, ?, ?)", ('Jan Kowalski', '2209', 'Elblag'))
    print("Rekord dodany")
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?, ?, ?)", ('Magda Nowak', '3510', 'Olsztyn'))
    print("Rekord dodany")
    con.commit()
    	
    cur.execute("SELECT * FROM pracownicy")
    print(cur.fetchall())
    	
    con.close()
    print("BD zamknieta")