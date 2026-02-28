from database import *
init_db()
#Main program with user service
while True:
    print("1. Show Tables")
    print("2. Reserve Table")
    print("3. Free Table")
    print("4. Quit")

    choice = int(input("Enter choice:  "))
    my_r = choose_restaurant(1)
    my_r.table_list = download_tables_from_db(my_r.restaurant_id)
    match choice:
        case 1:
            for s in my_r.table_list:
                print(s.table_name , s.number_of_seats, s.isavailable)
        case 2:
            table_name = input("Enter table name:  ")
            for t in my_r.table_list:
                if t.table_name == table_name:
                    reserve_db(t.id)
                    t.reserve()
        case 3:
            table_name = input("Enter table name:  ")
            for t in my_r.table_list:
                if t.table_name == table_name:
                    free_table_db(t.id)
                    t.free_table()

        case 4:
            break








