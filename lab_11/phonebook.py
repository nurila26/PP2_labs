import psycopg2
import csv
import re
from tabulate import tabulate

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="lab_10",
    user="postgres",
    password="on2606",
    port=5433
)

cur = conn.cursor()

# Создание таблицы
cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL

)
""")
conn.commit()

# Проверка телефона
def valid_phone(phone):
    return bool(re.match(r"^\+?\d{10,15}$", phone))

# Поиск по шаблону
def search_by_pattern(column, pattern):
    query = f"SELECT * FROM phonebook WHERE {column} LIKE %s"
    cur.execute(query, (f"%{pattern}%",))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="fancy_grid"))

# Вставка или обновление пользователя
def insert_or_update_user(name, phone):
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    existing_user = cur.fetchone()
    if existing_user:
        print(f"User {name} exists. Updating phone...")
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
    else:
        print(f"Adding new user: {name}")
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, '', %s)", (name, phone))
    conn.commit()

# Вставка нескольких пользователей
def insert_multiple_users(users):
    invalid_entries = []
    for name, phone in users:
        if valid_phone(phone):
            insert_or_update_user(name, phone)
        else:
            invalid_entries.append((name, phone))

    if invalid_entries:
        print("Invalid entries:")
        for entry in invalid_entries:
            print(f"Name: {entry[0]}, Phone: {entry[1]}")

# Пагинация
def get_paginated_data(limit, offset):
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="fancy_grid"))

# Удаление
def delete_by_name_or_phone(identifier, is_phone=False):
    if is_phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (identifier,))
    else:
        cur.execute("DELETE FROM phonebook WHERE name = %s", (identifier,))
    conn.commit()
    print(f"Deleted record(s) with {'phone' if is_phone else 'name'}: {identifier}")

# Главный цикл
while True:
    print("""
    Commands:
    1. 'i' to INSERT data (single or multiple).
    2. 'u' to UPDATE user data.
    3. 'q' to QUERY data by pattern.
    4. 'p' to PAGINATE data (LIMIT and OFFSET).
    5. 'd' to DELETE user by name or phone.
    6. 's' to SHOW all data.
    7. 'f' to FINISH.
    8. 'c' to CLEAR all data in the table.
    """)
    
    command = input("Enter command: ").strip().lower()
    print(f"DEBUG: command = '{command}'")  # отладка

    if command == 'i':
        choice = input("Type 'csv' for CSV input or 'con' for console input: ").strip().lower()
        if choice == 'con':
            name = input("Enter name: ").strip()
            surname = input("Enter surname: ").strip()
            phone = input("Enter phone: ").strip()
            if valid_phone(phone):
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
                conn.commit()
                print("User added successfully.")
            else:
                print("Invalid phone number.")
        elif choice == 'csv':
            filepath ="C:\\Users\\nuril\\PP2_labs\\lab_10\\students.csv"
            with open(str(filepath), 'r') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
            conn.commit()
            print("CSV data added.")


    elif command == 'u':
        column = input("Enter column to update (name, surname, phone): ").strip().lower()
        if column in ['name', 'surname', 'phone']:
            old_value = input(f"Enter old {column}: ").strip()
            new_value = input(f"Enter new {column}: ").strip()
            query = f"UPDATE phonebook SET {column} = %s WHERE {column} = %s"
            cur.execute(query, (new_value, old_value))
            conn.commit()
            print(f"{column} updated from {old_value} to {new_value}")
        else:
            print("Invalid column name.")

    elif command == 'q':
        col = input("Search by column (name, surname, phone): ").strip()
        pat = input("Enter search pattern: ").strip()
        search_by_pattern(col, pat)

    elif command == 'p':
        try:
            limit = int(input("Enter limit: ").strip())
            offset = int(input("Enter offset: ").strip())
            get_paginated_data(limit, offset)
        except ValueError:
            print("Limit and offset must be integers.")

    elif command == 'd':
        ident = input("Enter name or phone to delete: ").strip()
        ident_type = input("Is this a phone number? (y/n): ").strip().lower()
        delete_by_name_or_phone(ident, is_phone=(ident_type == 'y'))

    elif command == 's':
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="fancy_grid"))

    elif command == "c" :
        cur.execute("TRUNCATE TABLE phonebook RESTART IDENTITY")
        conn.commit()
        print("All data deleted and ID counter reset.")
        

    elif command == 'f':
        print("Exiting...")
        break

    else:
        print("Invalid command, please try again.")

# Закрытие соединения
conn.commit()
cur.close()
conn.close()