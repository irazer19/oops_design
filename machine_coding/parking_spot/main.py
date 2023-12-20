from entrance import Entrance
from parking_manager import ParkingManager
from parking_spot import CarSpot, BikerSpot
from vehicle import Car, Bike
from exit import Exit


def run():
    car = Car(vehicle_number="123", vehicle_type="CAR")
    spot1 = CarSpot(vehicle=None, status="AVAILABLE")
    spot2 = BikerSpot(vehicle=None, status="AVAILABLE")
    parking_manager = ParkingManager(slots=[])
    parking_manager.add_slot(spot1)
    parking_manager.add_slot(spot2)

    entrance = Entrance(parking_manager=parking_manager)
    exit = Exit(parking_manager=parking_manager, payment_manager=object)

    ticket = entrance.generate_ticket(vehicle=car)
    print(ticket)

    print(spot1.status, spot2.status)
    exit.unpark_vehicle(ticket)
    print(spot1.status, spot2.status)


if __name__ == "__main__":
    run()
