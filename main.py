import requests
from constants.settings import API_URL
from datetime import datetime
from utils.save_to_excel import save_to_excel
from utils.save_to_sql import save_to_sql
import time

def weather_data():
    try:
        response = requests.get(API_URL)
        data = response.json()

        formated_data = {
            'Temperatura': data['main']['temp'],
            'Odczuwalna temp.': data['main']['feels_like'],
            'Zachmurzenie': data['clouds']['all'],
            'Ciśnienie': data['main']['pressure'],
            'Wilgotność': data['main']['humidity'],
            'Wiatr': data['wind']['speed'],
            'Opis': data['weather'][0]['description'],
            'Data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        save_to_excel(formated_data)
        save_to_sql(formated_data)


    except Exception as er:
        print("Wystąpił błąd", er)



# Start project
while True:
    weather_data()
    time.sleep(10)