import psycopg2
import csv
from tabulate import tabulate 

conn = psycopg2.connect(
    host="localhost",
    dbname="lab_10", 
    user="postgres",     
    password="on2606", 
    port=5433
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL

)
""")

check = True
command = ''
temp = ''

name_var = ''
surname_var = ''
phone_var = ''
id_var = ''

start = True
back = False

back_com = ''
name_upd = ''
surname_upd = ''
phone_upd = ''

filepath = ''

while check:
    if start == True or back == True:
        start = False
        print("""
        List of the commands:
        1. Type "i" or "I" in order to INSERT data to the table.
        2. Type "u" or "U" in order to UPDATE data in the table.
        3. Type "q" or "Q" in order to make specidific QUERY in the table.
        4. Type "d" or "D" in order to DELETE data from the table.
        5. Type "f" or "F" in order to close the program.
        6. Type "s" or "S" in order to see the values in the table.
        7. Type "c" or "C" in order to CLEAR all data in the table.
        8. Type "p" or "P" to search with pattern using a function.
        9. Type "iu" to insert/update user using stored procedure.
        10. Type "bi" to batch insert users using stored procedure.
        11. Type "pg" for paginated view.
        12. Type "delp" to delete by name or phone using procedure.
        """)
        

        command = str(input())
        
        #insert
        if command == "i" or command == "I":
            print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
            command = ''
            temp = str(input())
            if temp == "con":
                name_var = str(input("Name: "))
                surname_var = str(input("Surname: "))
                phone_var = str(input("Phone: "))
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name_var, surname_var, phone_var))
                conn.commit()
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            if temp == "csv":
                filepath ="C:\\Users\\nuril\\PP2_labs\\lab_10\\students.csv"
                with open(str(filepath), 'r') as f:
                # Skip the header row.
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
                conn.commit()

                    
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

        #delete
        if command == "d" or command == "D":
            back = False
            command = ''
            phone_var = str(input('Type phone number which you want to delete: '))
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone_var,))
            conn.commit()
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True
        
        #update
        if command == 'u' or command == 'U':
            back = False
            command = ''
            temp = str(input('Type the name of the column that you want to change: '))
            if temp == "name":
                name_var = str(input("Enter name that you want to change: "))
                name_upd = str(input("Enter the new name: "))
                cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (name_upd, name_var))
                conn.commit()
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "surname":
                surname_var = str(input("Enter surname that you want to change: "))
                surname_upd = str(input("Enter the new surname: "))
                cur.execute("UPDATE phonebook SET surname = %s WHERE surname = %s", (surname_upd, surname_var))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "phone":
                name_var = str(input("Enter phone number that you want to change: "))
                name_upd = str(input("Enter the new phone number: "))
                cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (phone_upd, phone_var))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
        
        #query
        if command == "q" or command == "Q":
            back = False
            command = ''
            temp = str(input("Type the name of the column which will be used for searching data: "))
            if temp == "id":
                id_var = str(input("Type id of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE user_id = %s", (id_var, ))
                rows = cur.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            
            if temp == "name":
                name_var = str(input("Type name of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE name = %s", (name_var, ))
                rows = cur.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            
            if temp == "surname":
                surname_var = str(input("Type surname of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE surname = %s", (surname_var, ))
                rows = cur.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
                
            if temp == "phone":
                phone_var = str(input("Type phone number of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone_var, ))
                rows = cur.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

        
        #display
        if command == "s" or command == "S":
            back = False
            command = ''
            cur.execute("SELECT * from phonebook;")
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True
        #finish
        if command == "f" or command == "F":
            command = ''
            check = False
        # clear
        if command == "c" or command == "C":
            if command == "c" or "C":
                cur.execute("TRUNCATE TABLE phonebook RESTART IDENTITY")
                conn.commit()
                print("All data deleted and ID counter reset.")
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True
        
        if command == "p" or command == "P":
            pattern = input("Enter pattern (part of name, surname or phone): ")
            cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            back_com = str(input('Type "back" to return: '))
            if back_com == "back":
                back = True

        if command == "iu":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            phone = input("Enter phone: ")
            cur.execute("CALL insert_or_update_user(%s, %s, %s)", (name, surname, phone))
            conn.commit()
            print("User inserted or updated.")
            back_com = str(input('Type "back" to return: '))
            if back_com == "back":
                back = True


        if command == "bi":
            n = int(input("How many users to insert? "))
            names, surnames, phones = [], [], []
            for i in range(n):
                names.append(input(f"Name {i+1}: "))
                surnames.append(input(f"Surname {i+1}: "))
                phones.append(input(f"Phone {i+1}: "))
            cur.execute("CALL insert_many_users(%s, %s, %s)", (names, surnames, phones))
            conn.commit()
            print("All users inserted successfully.")
            back_com = str(input('Type "back" to return: '))
            if back_com == "back":
                back = True


        if command == "pg":
            limit = int(input("Enter number of results per page (limit): "))
            offset = int(input("Enter offset (e.g., 0 for first page): "))
            cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            back_com = str(input('Type "back" to return: '))
            if back_com == "back":
                back = True




        if command == "delp":
            val = input("Enter name or phone to delete: ")
            cur.execute("CALL delete_user(%s)", (val,))
            conn.commit()
            print("User deleted (if existed).")
            back_com = str(input('Type "back" to return: '))
            if back_com == "back":
                back = True


        

conn.commit()
cur.close()
conn.close()