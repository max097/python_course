import requests
import sqlite3
import time
from datetime import date, datetime, timedelta




def get_rates():
    result = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

    if result.status_code == 200:
        return result.json()
    else:
        print("Failed to fetch data from API -", result.status_code)
        return None

def create_table(date):
    db = sqlite3.connect("NBU_rates_16062024.db")
    cursor = db.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS '{date}' (
                    r030 INTEGER,
                    txt TEXT,
                    rate REAL,
                    exchangedate DATE)
                    ''')
    db.commit()
    db.close()


def insert_data(data, table_name):
    db = sqlite3.connect("NBU_rates_16062024.db")
    cursor = db.cursor()

    for dic in data:
        cursor.execute(f'''INSERT OR REPLACE INTO '{table_name}' (r030, txt, rate, exchangedate)
                       VALUES (?, ?, ?, ?)
                   ''', (dic["r030"], dic["txt"], dic["rate"], dic["exchangedate"]))
    db.commit()
    db.close()


while True:
    rates = get_rates()

    if rates:
        table_name = date.today().strftime("%Y_%m_%d")
        create_table(table_name)
        insert_data(rates, table_name)

        print("DATA insertes succesfully")

        time_now = datetime.now()
        tomorrow = time_now + timedelta(days = 1)
        tomorrow_midnight = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 0)
        sleeping_time = (tomorrow_midnight - time_now).seconds

        time.sleep(sleeping_time)

    else:
        print("FAILED to fetch data, retrying in 1 minute...")
        time.sleep(60)




