import sqlite3

# Создаем базу данных и подключаемся
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Создаем таблицу для хранения книг
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    status TEXT DEFAULT 'Не начата'
)
''')
conn.commit()

# Функция для добавления новой книги
def add_book(title, author, genre):
    cursor.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", (title, author, genre))
    conn.commit()
    print(f"\nКнига \"{title}\" была добавлена.")

# Функция для отображения всех книг
def view_books():
    cursor.execute("SELECT id, title, author, genre, status FROM books")
    books = cursor.fetchall()
    if books:
        print("\nСписок книг:")
        for book in books:
            print(f"{book[0]}. {book[1]} - {book[2]} (Жанр: {book[3]}, Статус: {book[4]})")
    else:
        print("\nСписок книг пуст.")

# Функция для обновления статуса книги
def update_book_status(book_id, status):
    cursor.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
    conn.commit()
    print(f"\nСтатус книги {book_id} был обновлен на \"{status}\".")

# Функция для удаления книги
def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    print(f"\nКнига {book_id} была удалена.")

# Главная функция
def main():
    print("Добро пожаловать в библиотечную систему!")

    while True:
        print("\n1. Добавить книгу")
        print("2. Просмотреть книги")
        print("3. Обновить статус книги")
        print("4. Удалить книгу")
        print("5. Выйти")
        choice = input("\nВыберите опцию: ")

        if choice == '1':
            title = input("\nВведите название книги: ")
            author = input("Введите автора книги: ")
            genre = input("Введите жанр книги: ")
            add_book(title, author, genre)
        elif choice == '2':
            view_books()
        elif choice == '3':
            book_id = int(input("\nВведите ID книги: "))
            status = input("\nВведите новый статус (Не начата/Читается/Прочитана): ")
            update_book_status(book_id, status)
        elif choice == '4':
            book_id = int(input("\nВведите ID книги: "))
            delete_book(book_id)
        elif choice == '5':
            print("\nСпасибо за использование библиотечной системы!")
            break
        else:
            print("\nНеверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

# Закрываем соединение с базой данных при завершении
conn.close()
