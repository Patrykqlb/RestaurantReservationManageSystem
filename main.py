from database import *
init_db()

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'


#Main program with user service
while True:
    my_r = choose_restaurant(1)
    if my_r:

        print(GREEN + "###########################################" + RESET)
        print("Welcome in table reservation manage system")
        print(GREEN + "###########################################" + RESET)
        print("1. Show Tables")
        print("2. Reserve Table")
        print("3. Free Table")
        print("4. Add Table")
        print("5. Delete Table")
        print("6. Quit")

        choice = int(input("Enter choice:  "))



        my_r.table_list = download_tables_from_db(my_r.restaurant_id)
        match choice:
            case 1:
                for t in my_r.table_list:
                    if t.isavailable:
                        print(f"ID |{t.id}| {t.table_name} with {t.number_of_seats} {GREEN} seats is available {RESET}")
                    else:
                        print(f"ID |{t.id}| {t.table_name} with {t.number_of_seats} {RED} seats is not available {RESET}")

            case 2:
                temp_id = int(input("Enter table ID:  "))
                for t in my_r.table_list:
                    if t.id == temp_id:
                        reserve_db(t.id,my_r.restaurant_id)
                        break
                else:
                    print("Table not found")
            case 3:
                temp_id = int(input("Enter table ID:  "))
                for t in my_r.table_list:
                    if t.id == temp_id:
                        free_table_db(t.id, my_r.restaurant_id)
                        break
                else:
                    print("Table not found")
            case 4:
                print("Creating Table")
                t_name = input("Enter table name:  ")
                t_seat = input("Enter number of seats:  ")
                add_table_db(my_r.restaurant_id, t_name, t_seat)
            case 5:
                print(RED + "Deleting Table" + RESET)
                temp_id = int(input("Enter table ID:  "))
                for t in my_r.table_list:
                    if t.id == temp_id:
                        print(f"You chose ID|{t.id}| {t.table_name} with {t.number_of_seats} seats to be deleted")
                        while True:
                            print("1. Confirm")
                            print("2. Cancel")
                            choice = int(input("Enter choice:  "))
                            if choice == 1:break
                            elif choice == 2:break
                        if choice == 1:
                            delete_table_db(t.id, my_r.restaurant_id)
                        else:
                            break
            case 6:
                break
    else:
        print(RED + 3*"Restaurant not found\n" + RESET)
        break








