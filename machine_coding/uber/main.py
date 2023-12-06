from rider import RiderManager
from driver import DriverManager
from location import Location
from trip import TripManager


rider_manager = RiderManager()
driver_manager = DriverManager()
rider_manager.add_rider("Saurav")
rider = rider_manager.get_rider("Saurav")
src = Location("Salugara")
dst = Location("City Center")
driver_manager.add_driver("Guptaji")

trip_manager = TripManager(
    rider_manager=rider_manager,
    driver_manager=driver_manager,
    trip_metadata_map={},
    trip_map={},
)
trip_manager.create_trip(rider=rider, src=src, dst=dst)
my_trip = trip_manager.get_trip(1)
my_trip.display_trip_details()
