# 🍽️ Restaurant Reservation Management System 

A simple and efficient console-based (CLI) restaurant table reservation system.
This project is written in Python and utilizes a local SQLite database to store
information about restaurants, tables, and their availability.

## ✨ Features 
* **Restaurant Management** - Create, store, and select multiple restaurants within a single database.
* **Table Management** - Add new tables and specify their seating capacity.
* **Reservation System** - A straightforward mechanism to reserve and free up tables.
* **Dynamic Menu** - An interactive terminal interface allowing easy navigation via numeric inputs.
* **Automatic Initialization** - The program automatically creates the database file and generates the required tables on the first run if they don't already exist.

## 🏗️ Project Architecture 
The project is divided into logical modules:
* `main.py` - The main program loop and Command Line Interface (CLI).
* `models.py` - Object-oriented classes (`Restaurant`, `Table`) representing the data structures in Python.
* `database.py` - Handles all the SQLite database connections and logic.

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Patrykqlb/RestaurantReservationManageSystem.git
2. Start the program
   ```bash
    python main.py
3. The program will automatically generate a .db file and populate a 'Test Restaurant' with 3 tables in the database upon first execution.