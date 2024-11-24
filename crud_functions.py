import sqlite3

connection = sqlite3.connect('not_telegram.db')

cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL, 
    description TEXT,
    price INTEGER
    )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL, 
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')


def add_user(username, email, age, balance=1000):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, balance))
    connection.commit()


def is_included(username):
    cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.commit()
    if user:
        return True
    else:
        return False


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    return all_products


# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f"Название: Продукт {i}", f"Описание: Описание {i}", f"{i * 100}"))
#

connection.commit()
