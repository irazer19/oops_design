import pricing
import driver_matching


class StrategyManager:
    def __init__(self, trip_metadata, driver_manager):
        self.trip_metadata = trip_metadata
        self.driver_manager = driver_manager

    def determine_pricing_strategy(self):
        return pricing.DefaultPricingStrategy(trip_metadata=self.trip_metadata)

    def determine_driver_match_strategy(self):
        return driver_matching.LeastTimeBasedStrategy(
            trip_metadata=self.trip_metadata, driver_manager=self.driver_manager
        )
