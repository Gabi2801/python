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
    



if language == 'en':
    height = float(input('Please enter your height input meters(decimals): '))
    weight = int(input('Please enter your weight input kg: '))
    bmi = weight /(height *height)
    
    if bmi <= 18.5:
        
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'overweight.')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')


input('\n\nPlease press enter to exit. \nAby zakończyć naciśnij Enter')
