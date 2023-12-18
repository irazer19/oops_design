class HotelBranch:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_rooms(self):
        pass


class Hotel:
    def __init__(self, name, hotel_branch):
        self.__name = name
        self.__hotel_branch = hotel_branch  # List

    def add_location(self, location):
        pass
