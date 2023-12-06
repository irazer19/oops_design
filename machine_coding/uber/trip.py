from strategy_manager import StrategyManager


class Trip:
    def __init__(
        self,
        rider,
        driver,
        src,
        dst,
        trip_id,
        price,
        pricing_strategy,
        driver_matching_strategy,
    ):
        self.rider = rider
        self.driver = driver
        self.src = src
        self.dst = dst
        self.trip_id = trip_id
        self.price = price
        self.pricing_strategy = pricing_strategy
        self.driver_matching_strategy = driver_matching_strategy

    def get_trip_id(self):
        return self.trip_id

    def display_trip_details(self):
        print(
            f"Rider: {self.rider.name}, driver: {self.driver.name}, Source: {self.src}, Destination: {self.dst}"
            f"trip_id: {self.trip_id}, Price: {self.price}"
        )


class TripMetadata:
    def __init__(self, rider_rating, driver_rating, src, dst):
        self.rider_rating = rider_rating
        self.driver_rating = driver_rating
        self.src = src
        self.dst = dst


class TripManager:
    def __init__(
        self,
        rider_manager,
        driver_manager,
        trip_metadata_map,
        trip_map,
    ):
        self.rider_manager = rider_manager
        self.driver_manager = driver_manager
        self.trip_metadata_map = trip_metadata_map
        self.trip_map = trip_map
        self.next_trip_id = 1

    def create_trip(self, rider, src, dst):
        """
        We need:
        - driver
        - rider
        - price
        - source location
        - destination location
        """
        trip_metadata = TripMetadata(
            rider_rating=rider.rating, driver_rating=None, src=src, dst=dst
        )
        strategy_manager = StrategyManager(
            trip_metadata=trip_metadata, driver_manager=self.driver_manager
        )
        driver_matching_object = strategy_manager.determine_driver_match_strategy()
        driver = driver_matching_object.match_driver()
        pricing_strategy_object = strategy_manager.determine_pricing_strategy()
        price = pricing_strategy_object.calculate_price()
        trip_id = self.next_trip_id
        trip = Trip(
            rider=rider,
            driver=driver,
            src=src,
            dst=dst,
            trip_id=trip_id,
            price=price,
            pricing_strategy=pricing_strategy_object,
            driver_matching_strategy=driver_matching_object,
        )
        self.trip_map[trip_id] = trip
        self.trip_metadata_map[trip_id] = trip_metadata
        print(f"Trip created with ID: {trip_id}")
        self.next_trip_id += 1

    def get_trip(self, trip_id):
        return self.trip_map.get(trip_id)
