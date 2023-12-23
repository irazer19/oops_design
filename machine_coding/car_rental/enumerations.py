import enum


class VehicleType(enum.Enum):
    CAR = 1
    BIKE = 2


class ReservationStatus(enum.Enum):
    PENDING = 1
    INPROGRESS = 2
    RESERVED = 3


class VehicleStatus(enum.Enum):
    AVAILABLE = 1
    UNAVAILABLE = 2


class BillStatus(enum.Enum):
    PAID = 1
    UNPAID = 2
