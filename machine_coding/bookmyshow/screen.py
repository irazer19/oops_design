class Screen:
    def __init__(self, screen_id, seats):
        self.screen_id = screen_id
        self.seats = seats

    def add_seat(self, seat):
        self.seats.append(seat)
