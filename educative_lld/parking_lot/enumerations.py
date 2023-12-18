from enum import Enum


class PaymentStatus(Enum):
    COMPLETED = 1
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5


# Custom Person data type
class Person:
    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email


# Custom Address data type
class Address:
    def __init__(self, address, city, state, zip_code, country):
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country
