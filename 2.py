import requests
from bs4 import BeautifulSoup

url = "https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all('div', class_ = 'table-responsive mb-4')

for element in elements:
    print(element.text)
