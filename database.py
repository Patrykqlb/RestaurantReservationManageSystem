import sqlite3
from models import Table, Restaurant

DB_NAME = "restaurants2.db"
def connect_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = 1")
    return conn

####################################################################################################################
                                    #DataBase functions
####################################################################################################################

def init_db():
    create_restaurant_db()
    create_table_db()
    create_example()


#Creates Table with restaurants
def create_restaurant_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Restaurants(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_name TEXT NOT NULL
        )
    ''')
    conn.close()


# Creates Table with tables
def create_table_db():
    conn = connect_db()
    cursor = conn.cursor()
    # @formatter:off
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
    conn.close()

    # If the database is empty function creates example restaurants and tables
def create_example():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Restaurants")
    if cursor.fetchone()[0] == 0:
        print("Detected first program start: Generating test restaurant and tables...")

        cursor.execute("INSERT INTO Restaurants (restaurant_name) VALUES (?)", ("Test restaurant",))
        id_restaurant = cursor.lastrowid

        test_tables = [
            (id_restaurant, "Table 1", 2, 1),
            (id_restaurant, "Table 2", 4, 1),
            (id_restaurant, "Table 3", 6, 0)
        ]

        cursor.executemany('''
                           INSERT INTO Tables (restaurant_id, name, number_of_seats, isavailable)
                           VALUES (?, ?, ?, ?)
                           ''', test_tables)
    conn.commit()
    conn.close()


def choose_restaurant(r_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, restaurant_name FROM Restaurants WHERE id = ?", (r_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        my_restaurant = Restaurant(restaurant_id=row[0], restaurant_name=row[1],)
        return my_restaurant
    return None


#####################################################################################################################
                                    #Table functions
#####################################################################################################################
def reserve_db(table_id,restaurant_id):  # Function changes status of the table to reserved
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
            "UPDATE Tables SET isavailable = 0 WHERE id= ? AND restaurant_id = ?",
            (table_id, restaurant_id)
    )

    conn.commit()
    conn.close()

def free_table_db(table_id, restaurant_id):  # Function changes status of the table to free
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
            "UPDATE Tables SET isavailable = 1 WHERE id = ? AND restaurant_id = ?",
            (table_id, restaurant_id)
    )
    conn.commit()
    conn.close()

def add_table_db(restaurant_id, table_name, seats):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Tables ( name, number_of_seats, isavailable, restaurant_id)
        VALUES (?, ?, 1, ?)
    ''',(table_name, seats, restaurant_id,))
    conn.commit()
    conn.close()

def delete_table_db(table_id, restaurant_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Tables WHERE id = ? AND restaurant_id = ?",
            (table_id, restaurant_id,)
    )
    conn.commit()
    conn.close()
#####################################################################################################################
                                    #Restaurant Functions
#####################################################################################################################

# Function that downloads data from database and puts it in a list

def download_tables_from_db(restaurant_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, number_of_seats, isavailable FROM Tables WHERE restaurant_id = ?", (restaurant_id,))
    table_list = []
    for row in cursor.fetchall():
        temp_table = Table(db_id=row[0], name=row[1], number_of_seats=row[2], isavailable=bool(row[3]))
        table_list.append(temp_table)
    conn.close()
    return table_list



