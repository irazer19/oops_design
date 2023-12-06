from abc import ABC, abstractmethod
import random


class DriverMatchingStrategy(ABC):
    def __init__(self, trip_metadata, driver_manager):
        self.trip_metadata = trip_metadata
        self.driver_manager = driver_manager

    @abstractmethod
    def match_driver(self):
        pass


class LeastTimeBasedStrategy(DriverMatchingStrategy):
    def __init__(self, trip_metadata, driver_manager):
        super().__init__(trip_metadata, driver_manager)

    def match_driver(self):
        # Simple random decision
        return self.driver_manager.drivers.get(
            random.choice(list(self.driver_manager.drivers.keys()))
        )
