name = input("Podaj swoje imię: ") #komentarz 
print ( "Witaj", name)
year = int(input("Podaj swój rok urodzenia: ")) #int(input()) - podanie wartości całkowitej
#nazwa zmiennej nie może zaczynać się od cyfry
#
import datetime

today = datetime.date.today()
print('Dzisiaj jest:  :', today.ctime())
tt = today.timetuple()
old = (tt.tm_year - year)
print('Jeśli teraz mamy rok', tt.tm_year, 'to obecnie masz', old , 'lata')
print("Przyjmując że rok ma 365 dni to żyjesz już około:", old * 365) #operatory matematyczne -> // dzielenie z wynikiem całkowitym
print("\a\n\t\t Miłego dnia życzę") # \t zmak tabulacji w Python \n znak nowego wiersza
input("\n\nAby zakończyć program, naciśnij klawisz \"Enter\".") #\" lub ' cudzysłów aby Python nie traktował jako końca łancucha

