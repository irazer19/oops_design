# definition of enumerations used in the Amazon Locker service
import enum


class LockerSize(enum.Enum):
    EXTRA_SMALL = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    EXTRA_LARGE = 5
    DOUBLE_EXTRA_LARGE = 6


class LockerState(enum.Enum):
    CLOSED = 1
    BOOKED = 2
    AVAILABLE = 3
