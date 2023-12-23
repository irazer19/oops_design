from enumerations import VehicleStatus


class VehicleInventory:
    def __init__(self):
        self.vehicles = {}

    def get_vehicle(self, vehicle_id):
        return self.vehicles.get(vehicle_id)

    def get_all_vehicles(self):
        return list(self.vehicles.values())

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle
        print(f"Your vehicle has been added with ID {vehicle.vehicle_id}")

    def update_vehicle_status(self, vehicle):
        vehicle.vehicle_status = VehicleStatus.UNAVAILABLE
