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

    @property
    def id(self):
        return self._db_id

class Restaurant:
    def __init__(self,restaurant_id,restaurant_name):
        self._restaurant_id = restaurant_id
        self._restaurant_name = restaurant_name
       # self._password = passwordS
        self.table_list = []
    @property
    def restaurant_name(self):
        return self._restaurant_name
    @property
    def restaurant_id(self):
        return self._restaurant_id

