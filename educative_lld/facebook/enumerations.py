import enum


class Address:
    def __init__(self, zip_code, house_no, city, state, country):
        self.__zip_code = zip_code
        self.__house_no = house_no
        self.__city = city
        self.__state = state
        self.__country = country


class AccountStatus(enum.Enum):
    ACTIVE = 1
    BLOCKED = 2
    DISABLED = 3
    DELETED = 4


class FriendInviteStatus(enum.Enum):
    PENDING = 1
    ACCEPTED = 2
    REJECTED = 3
    CANCELED = 4


class PostPrivacySettings(enum.Enum):
    PUBLIC = 1
    FRIENDS_OF_FRIENDS = 2
    ONLY_FRIENDS = 3
    CUSTOM = 4
