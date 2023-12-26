class TheatreManager:
    def __init__(self):
        self.city_to_theatre = {}
        self.theatres = []

    def add_theatre(self, theatre, city):
        if city not in self.city_to_theatre:
            self.city_to_theatre[city] = []
        self.city_to_theatre[city].append(theatre)
        self.theatres.append(theatre)

    def get_theatre_by_city(self, city):
        return self.city_to_theatre.get(city, [])
