from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    def __init__(self, trip_metadata):
        self.trip_metadata = trip_metadata

    @abstractmethod
    def calculate_price(self):
        pass


class DefaultPricingStrategy(PricingStrategy):
    def __init__(self, trip_metadata):
        super().__init__(trip_metadata)

    def calculate_price(self):
        return 400


class RatingBasedPricingStrategy(PricingStrategy):
    def __init__(self, trip_metadata):
        super().__init__(trip_metadata)

    def calculate_price(self):
        driver_rating = self.trip_metadata.driver_rating
        if driver_rating > 3:
            return 500
        return 300
