class Rider:
    def __init__(self, name, rating=5):
        self.name = name
        self.rating = rating


class RiderManager:
    def __init__(self):
        self.riders = {}

    def add_rider(self, name):
        r = Rider(name=name, rating=5)
        self.riders[name] = r

    def get_rider(self, name):
        return self.riders.get(name)
