import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            date TEXT,
            time TEXT,
            temperature TEXT
        )
    """)
    conn.commit()
    conn.close()

# Функция для парсинга температуры
def fetch_weather():
    # Укажите URL сайта с погодой вашего города
    url = "https://yandex.ru/pogoda/your_city"  # Замените "your_city" на ваш город (например, "moscow")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Найдите элемент с температурой на сайте
    try:
        temperature = soup.find("div", class_="temp__value").text.strip()
        return temperature
    except AttributeError:
        raise Exception("Не удалось найти температуру на сайте. Проверьте URL и селектор.")

# Функция для записи данных в БД
def insert_weather_data():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_ = now.strftime("%H:%M:%S")
    try:
        temperature = fetch_weather()
        cursor.execute("INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)", (date, time_, temperature))
        conn.commit()
        print(f"[{date} {time_}] Температура: {temperature} добавлена в базу данных.")
    except Exception as e:
        print(f"Ошибка при парсинге данных: {e}")
    conn.close()

# Запуск регулярного обновления данных
def start_weather_updates():
    print("Начинаем обновление данных о погоде каждые 30 минут.")
    while True:
        insert_weather_data()
        time.sleep(1800)  # Обновление каждые 30 минут

if __name__ == "__main__":
    create_database()
    start_weather_updates()
