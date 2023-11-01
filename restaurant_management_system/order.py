class Order:
    def __init__(self, order_id, status, __creation_time, meals, table, waiter, chef):
        self.__order_id = order_id
        self.__status = status
        self.__creation_time = None
        self.__meals = []
        self.__table = table
        self.__waiter = waiter
        self.__chef = chef

    def add_meal(self, meal):
        pass

    def remove_meal(self, meal):
        pass


class Kitchen:
    def __init__(self, name):
        self.__name = name
        self.__chefs = []

    def assign_chef(self, chef):
        pass


class Reservation:
    def __init__(self, id, people_count, notes, customer):
        self.__reservation_id = id
        self.__time_of_reservation = None
        self.__people_count = people_count
        self.__status = None
        self.__notes = notes
        self.__checkin_time = None
        self.__customer = customer
        self.__tables = []
        self.__notifications = []

    def update_people_count(self, count):
        pass
