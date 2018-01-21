# program wykonany na cwiczeniach z podstaw programowania w Python
import smtplib
from email.mime.text import MIMEText

import bs4
import requests

# Pobranie strony ARMAAG
url = 'http://armaag.gda.pl/komunikat.htm'
response = requests.get(url)

# Sparsowanie strony i wyszukanie tabeli z jakoscia powietrza
soup = bs4.BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='jakoscpowietrza')

is_red = '/img2/czerwony.gif'
is_yellow = '/img2/zolty.gif'

# Sprawdzenie, czy w tabeli znajduja sie informacje o poziomie zoltym lub czerwonym
if is_red or is_yellow == true:

    # Sparsowanie tabeli i wyszukanie wierszy
    rows = table.find_all('tr')

    # Pobranie listy raportowanych substancji z wiersza naglowkowego
    substances = []
    for header in rows[0].find_all('th', class_='tabela_opis2'):
        substances.append(header.get_text())

    # Utworzenie listy ostrzezen na podstawie wierszy z pomiarami
    alerts = []
    measurements = rows[1:]
    for measurement in measurements:
        station = measurement.find('th').get_text()
        values = measurement.find_all('td')
        for index, value in enumerate(values):
            image = value.find('img')
            try:
                image_src = image.attrs['src']
            except AttributeError:
                continue
            if image_src == '/img2/zolty.gif':
                alerts.append((station, substances[index], 'staus', 'żółty'))
            elif image_src == '/img/czerwony.gif':
                alerts.append((station, substances[index], 'status', 'czerwony'))
    print(alerts)



    # Wyslanie wiadomosci e-mail z ostrzezeniem
    # Utworzenie tresci wiadomosci


    # # Wyslanie wiadomosci e-mail z ostrzezeniem
    # Utworzenie wiadomosci
    print('Ostrzeżenie')
    message_text = 'Raport o jakości powietrza: poziomy substancji są podwyższone.<br/>'
    message_text += '<ul>'
    message = MIMEText(message_text, 'html')

    for alert in alerts:
        message_text += ('<li>Stacja <b>%s</b> zarejestrowała dla <b>%s</b> poziom '
                         '<span style="background-color: %s">%s</span>.</li>' % alert)
    message_text += '</ul>'
    message['From'] = 'Smog <wsb_kontosztuczneZ@wp.pl>'
    message['To'] = 'lukaszgd@gmail.com'
    message['Subject'] = 'Ostrzeżenie o smogu'

    smtp = smtplib.SMTP_SSL('smtp.wp.pl', 465)  # łączenie z serwerem
    smtp.ehlo()
    smtp.sendmail(message['From'], message['To'], message.as_string())
    smtp.quit()
