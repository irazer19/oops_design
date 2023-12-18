# Enumerations
import enum


class PaymentStatus(enum.Enum):
    PENDING = 1
    CONFIRMED = 2
    DECLINED = 3
    REFUNDED = 4


class BookingStatus(enum.Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCELLED = 3
    DENIED = 4
    REFUNDED = 5


class SeatStatus(enum.Enum):
    AVAILABLE = 1
    BOOKED = 2
    RESERVED = 3
