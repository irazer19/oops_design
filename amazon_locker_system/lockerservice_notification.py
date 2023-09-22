class LockerService:
    # Should be a singleton class
    def __init__(self, locations):
        self.__locations = locations


class Notification:
    def __init__(self, customer_id, order_id, locker_id, code):
        self.__customer_id = customer_id
        self.__order_id = order_id
        self.__locker_id = locker_id
        self.__code = code

    def send(self):
        pass
