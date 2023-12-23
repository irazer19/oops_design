from enumerations import VehicleType
from abc import ABC
from enumerations import VehicleStatus


class Vehicle(ABC):
    def __init__(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.vehicle_status = VehicleStatus.AVAILABLE


class Car(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, VehicleType.CAR)


class Bike(Vehicle):
    def __init__(self, vehicle_id, vehicle_status):
        super().__init__(vehicle_id, VehicleType.BIKE)
