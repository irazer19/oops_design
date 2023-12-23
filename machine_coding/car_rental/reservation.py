class Reservation:
    def __init__(
        self, reservation_id, user, vehicle, reservation_status, start_date, end_date
    ):
        self.reservation_id = reservation_id
        self.user = user
        self.vehicle = vehicle
        self.reservation_status = reservation_status
        self.start_date = start_date
        self.end_date = end_date
