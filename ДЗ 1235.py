from bs4 import BeautifulSoup
import requests

response = requests.get('https://bank.gov.ua/control/uk/curmetal/detail/currency?period=daily')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    currency_choice = input("Виберіть валюту (1 - USD, 2 - EUR, 3 - GBP, 4 - CZK, 5 - PLN, 6 - INR): ")

    if currency_choice == '1':
        usd_element = soup.select_one('td:-soup-contains("Долар США")')
        usd_exchange_rate = usd_element.find_next('td').text
        print(f"Курс USD: {usd_exchange_rate}")
    elif currency_choice == '2':
        eur_element = soup.select_one('td:-soup-contains("Євро")')
        eur_exchange_rate = eur_element.find_next('td').text
        print(f"Курс EUR: {eur_exchange_rate}")
    elif currency_choice == '3':
        gbp_element = soup.select_one('td:-soup-contains("Фунт стерлінгів")')
        gbp_exchange_rate = gbp_element.find_next('td').text
        print(f"Курс GBP: {gbp_exchange_rate}")
    elif currency_choice == '4':
        czk_element = soup.select_one('td:-soup-contains("Чеська крона")')
        czk_exchange_rate = czk_element.find_next('td').text
        print(f"Курс CZK: {czk_exchange_rate}")
    elif currency_choice == '5':
        pln_element = soup.select_one('td:-soup-contains("Злотий")')
        pln_exchange_rate = pln_element.find_next('td').text
        print(f"Курс PLN: {pln_exchange_rate}")
    elif currency_choice == '6':
        inr_element = soup.select_one('td:-soup-contains("Рупія")')
        inr_exchange_rate = inr_element.find_next('td').text
        print(f"Курс INR: {inr_exchange_rate}")
    else:
        print("Введіть число від 1 до 6.")
        exit()
