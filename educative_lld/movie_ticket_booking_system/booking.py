class Booking:
    # Data members
    def __init__(
        self, booking_id, amount, total_seats, created_on, status, payment, show
    ):
        self.__booking_id = booking_id
        self.__amount = amount
        self.__total_seats = total_seats
        self.__created_on = created_on
        self.__status = status  # BookingStatus enum

        # Instances of classes
        self.__payment = payment
        self.__show = show
        self.__tickets = []  # List of movie tickets
        self.__seats = []  # List of seats
