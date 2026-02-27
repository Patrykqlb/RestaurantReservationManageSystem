import sqlite3
import os
class Table:
    def __init__(self,db_id, name, number_of_seats, isavailable = True): #Define object Table
        self._db_id = db_id
        self._name = name
        self._number_of_seats = number_of_seats
        self._isavailable = isavailable

    @property
    def table_name(self):  return self._name

    @property
    def number_of_seats(self): return self._number_of_seats

    @property
    def isavailable(self): return self._isavailable

    def reserve(self,db_cursor,db_conn): #Function changes status of the table to reserved
        if self._isavailable:
            self._isavailable = False

            db_cursor.execute("UPDATE Tables SET isavailable = 0 WHERE id= ?", (self._db_id,))
            db_conn.commit()
            print(f"Table number {self.table_name} reserved")
        else:
            print(f"Table {self.table_name} is already reserved")

    def free_table(self, db_cursor, db_conn): #Function changes status of the table to free
        if not self._isavailable:
            self._isavailable = True

            db_cursor.execute("UPDATE Tables SET isavailable = 1 WHERE id= ?", (self._db_id,))
            db_conn.commit()
            print("Table is free now")
        else:
            print("Table was not reserved")

conn = sqlite3.connect('restaurants.db')

conn.execute("PRAGMA foreign_keys = 1") #Turns on foreign keys for sqlite
cursor = conn.cursor()

#Creates Table with restaurants
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Restaurants(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant_name TEXT NOT NULL
    )
''')
#Creates Table with tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tables(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant_id INTEGER,
        name TEXT NOT NULL,
        number_of_seats INTEGER NOT NULL,
        isavailable INTEGER DEFAULT 1,
        FOREIGN KEY(restaurant_id) REFERENCES Restaurants(id)
        )
''')
#If the database is empty function creates example restaurants and tables
cursor.execute("SELECT COUNT(*) FROM Restaurants")
if cursor.fetchone()[0] == 0:
    print("Detected first program start: Generating test restaurant and tables...")

    cursor.execute("INSERT INTO Restaurants (restaurant_name) VALUES (?)", ("Test restaurant",))
    id_restaurant = cursor.lastrowid

    test_tables = [
        (id_restaurant, "Table 1",2,1),
        (id_restaurant, "Table 2",4,1),
        (id_restaurant, "Table 3",6,0)
    ]

    cursor.executemany('''
        INSERT INTO Tables (restaurant_id, name, number_of_seats, isavailable)
        VALUES (?,?,?,?)
    ''', test_tables)

#Function that downloads data from database and puts it in a list
def download_tables_from_db():
    cursor.execute("SELECT id, name, number_of_seats, isavailable FROM Tables")
    table_list = []
    for row in cursor.fetchall():
        temp_table = Table(db_id=row[0], name=row[1], number_of_seats=row[2], isavailable=bool(row[3]))
        table_list.append(temp_table)
    return table_list


#Main program with user service
while True:
    print("1. Show Tables")
    print("2. Show available tables")
    print("3. Reserve Table")
    print("4. Free Table")
    print("5. Quit")

    choice = int(input("Enter choice: "))

    tables = download_tables_from_db()
    match choice:
        case 1:
            for s in tables:
                print(s.table_name , s.number_of_seats, s.isavailable)
        case 2:
            for s in tables:
                if s.isavailable:
                    print(s.table_name , s.number_of_seats)
        case 3:
            temp_name = input("Enter Table name: ")
            for s in tables:
                if s.table_name == temp_name:
                    s.reserve(cursor, conn)
        case 4:
            temp_name = input("Enter Table name: ")
            for s in tables:
                if s.table_name == temp_name:
                    s.free_table(cursor,conn)

        case 5:
            conn.close()
            break








