import enum


class Address:
    def __init__(self, zip_code, street_address, city, state, country):
        self.__zip_code = zip_code
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__country = country


class AccountStatus(enum.Enum):
    ACTIVE = 1
    DEACTIVATED = 2
    BLOCKED = 3
    DELETED = 4


class ConnectionInviteStatus(enum.Enum):
    PENDING = 1
    ACCEPTED = 2
    IGNORED = 3


class JobStatus(enum.Enum):
    OPEN = 1
    ON_HOLD = 2
    CLOSED = 3
