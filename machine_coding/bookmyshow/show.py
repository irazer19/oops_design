class Show:
    def __init__(self, show_id, theatre, screen, movie, booked_seats, start_time):
        self.show_id = show_id
        self.theatr = theatre
        self.screen = screen
        self.movie = movie
        self.booked_seats = booked_seats
        self.start_time = start_time

    def add_booked_seats(self, booked_seat):
        self.booked_seats.append(booked_seat)

    def remove_booked_seats(self, booked_seat):
        self.booked_seats.remove(booked_seat)
