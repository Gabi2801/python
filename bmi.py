name = input('Podaj swoje imię:"')
print('Cześć ', name)
weight = int(input("Ile kilogramów ważysz? "))
height = int(input("Ile masz wzrostu? "))
sum = weight / height

if sum > 18-25:
    print("Waga prawdidłowa")
if sum > 26:
    print("Masz nadwagę")

input("\n\nAby zakończyć program, naciśnij klawisz \"Enter\".")
