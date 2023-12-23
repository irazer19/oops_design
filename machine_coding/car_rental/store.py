from reservation import Reservation
from enumerations import ReservationStatus
from datetime import datetime


class Store:
    def __init__(self, vehicle_inventory, location):
        self.vehicle_inventory = vehicle_inventory
        self.location = location
        self.reservations = {}
        self.reservation_id = 1

    def add_vehicle(self, vehicle):
        self.vehicle_inventory.add_vehicle(vehicle)

    def get_vehicles(self):
        return self.vehicle_inventory.get_all_vehicles()

    def reserve_vehicle(self, vehicle, user):
        self.reservation_id += 1
        reservation = Reservation(
            reservation_id=self.reservation_id,
            user=user,
            vehicle=vehicle,
            reservation_status=ReservationStatus.PENDING,
            start_date=datetime.now(),
            end_date=None,
        )
        self.reservations[self.reservation_id] = reservation
        self.vehicle_inventory.update_vehicle_status(vehicle)
        print(
            f"{user.username} booked vehicle {vehicle.vehicle_type} ID {vehicle.vehicle_id} and reservationID is {self.reservation_id}"
        )
        return reservation
