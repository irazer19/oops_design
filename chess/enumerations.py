# Enumerations
import enum


class GameStatus(enum.Enum):
    Active = 1
    BlackWin = 2
    WhiteWin = 3
    Forfeit = 4
    Stalemate = 5
    Resignation = 6


class AccountStatus(enum.Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5


# Custom Person data type class
class Person:
    def __init__(self, name, street_address, city, state, zip_code, country):
        self.__name = name
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country
