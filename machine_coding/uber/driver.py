from enumerations import DriverStatus


class Driver:
    def __init__(self, name, is_available, rating=5):
        self.name = name
        self.is_available = is_available
        self.rating = rating


class DriverManager:
    def __init__(self):
        self.drivers = {}

    def add_driver(self, name):
        d = Driver(name=name, is_available=DriverStatus.AVAILABLE, rating=5)
        self.drivers[name] = d

    def get_driver(self, name):
        return self.drivers.get(name)
