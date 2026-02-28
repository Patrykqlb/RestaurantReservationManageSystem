from database import *
init_db()

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'
def choice_id(my_r):
    temp_id = input("Enter table number:  ")
    if temp_id.isdigit():
        index = int(temp_id) - 1
        if 0 <= index < len(my_r.table_list):
            return  my_r.table_list[index]
    return None
def manage_restaurant(restaurant_id):
    while True:
        my_r = choose_restaurant(restaurant_id)
        if my_r:
            print(GREEN + "###########################################" + RESET)
            print("         MANAGE YOUR RESTAURANT")
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
                    for i, t in enumerate( my_r.table_list, start = 1):
                        if t.isavailable:
                            print(f"ID |{i}| {t.table_name} with {t.number_of_seats} seats {GREEN} is available {RESET}")
                        else:
                            print(f"ID |{i}| {t.table_name} with {t.number_of_seats} seats {RED} is not available {RESET}")

                case 2:
                    chosen_table = choice_id(my_r)
                    if chosen_table:
                        reserve_db(chosen_table.id, my_r.restaurant_id)
                        print(f"{chosen_table.table_name} is reserved now")
                    else:
                        print("Table not found")
                case 3:
                    chosen_table = choice_id(my_r)
                    if chosen_table:
                        free_table_db(chosen_table.id,my_r.restaurant_id)
                        print(f"{chosen_table.table_name} is free now")
                    else:
                        print("Table not found")
                case 4:
                    print("Creating Table")
                    t_name = input("Enter table name:  ")
                    t_seat = input("Enter number of seats:  ")
                    add_table_db(my_r.restaurant_id, t_name, t_seat)
                case 5:
                    print(RED + "Deleting Table" + RESET)
                    t = choice_id(my_r)
                    if t:
                        print(f"You chose |{t.id}| {t.table_name} with {t.number_of_seats} seats to be deleted")
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
                    else:
                        print("Table not found")
                case 6:
                    break
        else:
            print(RED + 3*"Restaurant not found\n" + RESET)
            break





#Main program with user service
while True:
    print(GREEN + "###########################################" + RESET)
    print("Welcome in table reservation manage system")
    print(GREEN + "###########################################" + RESET)
    print("1. Show Restaurants")
    print("2. Manage Restaurant")
    print("3. Add Restaurant")
    print("4. Delete Restaurant")
    print("5. Quit")

    rest_list = download_restaurants_from_db()
    selection = int(input("Enter choice:  "))

    match selection:
        case 1:
            for r in rest_list:
                print(f"{r.restaurant_id} {r.restaurant_name}")
        case 2:
            print("Which restaurant do you want to manage?")
            r_id = int(input("Enter restaurant ID:  "))
            manage_restaurant(r_id)
        case 3:
            print("Creating new restaurant")
            r_name = input("Enter restaurant name:  ")
            add_restaurant(r_name)
            print(f"Restaurant {r_name} created")
        case 4:
            print("Deleting restaurant")
        case 5:
            break










