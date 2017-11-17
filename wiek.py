x = input("Podaj swoje imię: ") #komentarz 
print ( "Witaj", x)
rok = int(input("Podaj swój rok urodzenia: "))

import datetime

today = datetime.date.today()
print('Dzisiaj jest:  :', today.ctime())
tt = today.timetuple()
wiek = (tt.tm_year - rok)
print('Jeśli teraz mamy rok', tt.tm_year, 'to obecnie masz', wiek , 'lata')
print("Przyjmując że rok ma 365 dni to żyjesz już około:", wiek * 365)
print("\a\n\t\t Miłego dnia życzę") # \t zmak tabulacji w Python \n znak nowego wiersza
input("\n\nAby zakończyć program, naciśnij klawisz \"Enter\".") #\" lub ' cudzysłów aby Python nie traktował jako końca łancucha

