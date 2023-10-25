class RoomBooking:
    def __init__(
        self, reservation_number, start_date, duration_in_days, booking_status
    ):
        self.__reservation_number = reservation_number
        self.__start_date = start_date
        self.__duration_in_days = duration_in_days
        self.__booking_status = booking_status
        self.__checkin = None
        self.__checkout = None
        self.__guest_id = 0
        self.__room = None
        self.__invoice = None
        self.__notifications = []

    def fetch_details(self, reservation_number):
        pass
