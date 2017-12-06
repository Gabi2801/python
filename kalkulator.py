# Program kalkulator
# Program wykonuje łatwe obliczenia na liczbach całkowitych

dzialanie = input('Wybierz typ działania które chcesz przeprowadzić\n + dodawanie \n - odejmowanie\n * - mnożenie\n - dzielenie\n Wybieram ')

if dzialanie == '+':
    a = int(input('Podaj pierwszy składnik: '))
    b = int(input('Podaj drugi składnik: '))
    suma_plus = a + b
    print(suma_plus)

if dzialanie == '-':
    a = int(input('Podaj pierwszy składnik: '))
    b = int(input('Podaj drugi składnik: '))
    suma_minus = a - b
    print(suma_minus)

input('\nAby zakończyć naciśnij Enter')
