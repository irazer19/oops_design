from user import User
from vehicle import Car
from store import Store
from vehicle_inventory import VehicleInventory
from location import Location
from car_rental_system import CarRentalSystem
from bill import Bill
from enumerations import BillStatus


def run():
    user = User("Saurav", "irazer19@gmail.com")
    car1 = Car(vehicle_id=1)
    car2 = Car(vehicle_id=2)

    vinv = VehicleInventory()
    store_loc = Location("MG Road", "560065", "Bangalore")
    store1 = Store(vehicle_inventory=vinv, location=store_loc)
    store1.add_vehicle(car1)
    store1.add_vehicle(car2)
    print(vinv.get_all_vehicles())
    system = CarRentalSystem(users=[user], stores={})
    system.add_store(store1)
    ###################
    # get a store
    my_store = system.get_store(store_loc)
    # get vehicles
    cars = my_store.get_vehicles()

    reservation_obj = my_store.reserve_vehicle(cars[0], user)
    mybill = Bill(reservation=reservation_obj, bill_status=BillStatus.UNPAID)
    mybill.pay_bill()


if __name__ == "__main__":
    run()
