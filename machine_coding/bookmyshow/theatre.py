class Theatre:
    def __init__(self, theatre_id, city, screens, shows):
        self.theatre_id = theatre_id
        self.city = city
        self.screens = screens
        self.shows = shows

    def add_screen(self, screen):
        self.screens.append(screen)

    def add_show(self, show):
        self.shows.append(show)
