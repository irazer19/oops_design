class ParkingManager:
    def __init__(self, slots):
        self.slots = slots

    def add_slot(self, slot):
        self.slots.append(slot)
        print(f"Added slot {slot}")

    def remove_slot(self, slot):
        self.slots.remove(slot)
        print(f"Removed slot {slot}")

    def park_vehicle(self, vehicle, slot):
        slot.park_vehicle(vehicle)
        print(f"Vehicle {vehicle.vehicle_number} is parked!")

    def unpark_vehicle(self, ticket):
        slot = ticket.slot
        vehicle = ticket.vehicle
        slot.unpark_vehicle()
        print(f"Vehicle {vehicle.vehicle_number} is unparked!")

    def get_slot(self, vehicle):
        # We can use strategy to get the best slot according to vehicle types.
        for slot in self.slots:
            if slot.spot_type == vehicle.vehicle_type and slot.status == "AVAILABLE":
                return slot

        return None
