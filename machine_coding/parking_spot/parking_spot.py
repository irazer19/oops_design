from abc import ABC, abstractmethod


class ParkingSpot(ABC):
    def __init__(self, vehicle, status, spot_type):
        self.vehicle = vehicle
        self.spot_type = spot_type
        self.status = status

    @abstractmethod
    def park_vehicle(self, vehicle):
        pass

    def unpark_vehicle(self):
        self.vehicle = None
        self.status = "AVAILABLE"


class CarSpot(ParkingSpot):
    def __init__(self, vehicle, status):
        super().__init__(vehicle, status, "CAR")

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.status = "OCCUPIED"
        print("You Car has been parked!")


class BikerSpot(ParkingSpot):
    def __init__(self, vehicle, status):
        super().__init__(vehicle, status, "BIKE")

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.status = "OCCUPIED"
        print("Your Bike has been parked!")
