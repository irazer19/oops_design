from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Guest(Person):
    def __init__(self):
        self.__total_rooms_checked_in = 0

    def get_bookings(self):
        pass


class Receptionist(Person):
    def search_member(self, name):
        pass

    def create_booking(self):
        pass


class Housekeeper(Person):
    def assignToRoom(self):
        pass
