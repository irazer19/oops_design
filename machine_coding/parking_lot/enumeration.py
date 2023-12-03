import enum


class SlotStatus(enum.Enum):
    AVAILABLE = 1
    OCCUPIED = 2
    UNAVAILABLE = 3


class VehicleType(enum.Enum):
    CAR = 1
    TRUCK = 2
    BIKE = 3
