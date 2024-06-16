import requests
import sqlite3

# result = requests.request("GET", "https://www.python.org/")
# print(result)
#
# print(dir(result))
# print(result.status_code)
# print(result.request)
# print(result.headers)
# print(result.headers["Content-Type"])
#
#
# result = requests.request("GET", "https://www.python.org/gdgdgdgdgdgdgdgdfgdfgdgdg")
# print(result.status_code)
#
# result = requests.request("GET", "https://api.kuna.io/v4/public/fees")
# print(result)
# print(result.headers["Content-Type"])
# print(result.text)
# print(result.headers)
# print(result.json())
#
# data = result.json()
# for el in data:
#     print(f"{el} - {result.json()[el]}")
#
#
# result = requests.request("GET", "https://api-seller.rozetka.com.ua/markets/business-types")
# print(result)
# print(result.text)
#
#
#
# result = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
# print(result)
# print(result.headers["Content-Type"])
#
#
# data = result.json()
# print(data)
#
# for dic in data:
#     print(dic)



db = sqlite3.connect("NBU_rates_16062024.db")
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS rates (
                r030 INTEGER,
                txt TEXT,
                rate REAl,
                exchangedate DATE)
                ''')

result = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
data = result.json()

for dic in data:
    cursor.execute("INSERT INTO rates VALUES (?,?,?,?)", (dic["r030"], dic["txt"], dic["rate"], dic["exchangedate"]))

db.commit()
db.close()














































































































































