# definition of enumerations used in the car rental system
import enum


class VehicleStatus(enum.Enum):
    AVAILABLE = 1
    RESERVED = 2
    LOST = 3
    BEING_SERVICED = 4


class AccountStatus(enum.Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    BLOCKED = 5


class ReservationStatus(enum.Enum):
    ACTIVE = 1
    PENDING = 2
    CONFIRMED = 3
    COMPLETED = 4
    CANCELED = 5


class PaymentStatus(enum.Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    CANCELED = 4
    REFUNDED = 5


class VanType(enum.Enum):
    PASSENGER = 1
    CARGO = 2


class CarType(enum.Enum):
    ECONOMY = 1
    COMPACT = 2
    INTERMEDIATE = 3
    STANDARD = 4
    FULL_SIZE = 5
    PREMIUM = 6
    LUXURY = 7


class MotorcycleType(enum.Enum):
    STANDARD = 1
    CRUISER = 2
    TOURING = 3
    SPORTS = 4
    OFF_ROAD = 5
    DUAL_PURPOSE = 6


class TruckType(enum.Enum):
    LIGHT_DUTY = 1
    MEDIUM_DUTY = 2
    HEAVY_DUTY = 3


class VehicleLogType(enum.Enum):
    ACCIDENT = 1
    FUELING = 2
    CLEANING_SERVICE = 3
    OIL_CHANGE = 4
    REPAIR = 5
    OTHER = 6
