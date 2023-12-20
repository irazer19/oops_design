from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type


class Car(Vehicle):
    def __init__(self, vehicle_number, vehicle_type):
        super().__init__(vehicle_number, vehicle_type)


class Bike(Vehicle):
    def __init__(self, vehicle_number, vehicle_type):
        super().__init__(vehicle_number, vehicle_type)
