# definition of enumerations used in elevator system
import enum


class RoomStatus(enum.Enum):
    AVAILABLE = 1
    RESERVED = 2
    OCCUPIED = 3
    NOT_AVAILABLE = 4
    BEING_SERVICED = 5
    OTHER = 6


class BookingStatus(enum.Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CANCELED = 4
    ABANDONED = 5


class AccountStatus(enum.Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    BLOCKED = 5


class AccountType(enum.Enum):
    MEMBER = 1
    GUEST = 2
    MANAGER = 3
    RECEPTIONIST = 4


class PaymentStatus(enum.Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    FILLED = 4
    DECLINED = 5
    CANCELLED = 6
    ABANDONED = 7
    SETTLING = 8
    SETTLED = 9
    REFUNDED = 10
