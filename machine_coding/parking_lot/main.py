from parking_lot import ParkingLot


if __name__ == "__main__":
    p = ParkingLot("PL1234", 2, 5)
    p.initialize_lot()
    print(p.floors)
    p.park_vehicle("CAR", "SK12344", "RED")
    print(p.get_free_slots_for_vehicletype("CAR"))
    p.add_floor()
    print(p.get_free_slots_for_vehicletype("CAR"))
