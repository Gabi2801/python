language = input('Please select your language: \n EN English \n PL - Polish \n: ')

if language == 'pl':
    height = float(input('Podaj swój wzrost w cm: '))
    weight = int(input('Podaj swoją wagę w kg: '))
    bmi = weight /(height / 100 *height / 100)
    
    if bmi <= 18.5:
        
        print('Twoje BMI:', bmi,' czyli masz niedowagę.')

    elif bmi > 18.5 and bmi < 25:
        print('Twoje BMI:', bmi,' czyli Twoja waga jest prawidłowa')

    elif bmi > 25 and bmi < 30:
        print('Twoje BMI:', bmi,' masz nadwagę.')

    elif bmi > 30:
        print('Twoje BMI:', bmi,' Uwaga - Twoja waga wskazuje otyłość')

    else:
        print('Podałeś nieprawidłowe dane')
    
