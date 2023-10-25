class Room:
    def __init__(self, room_number, style, status, booking_price, is_smoking):
        self.__room_number = room_number
        self.__style = style
        self.__status = status
        self.__booking_price = booking_price
        self.__is_smoking = is_smoking
        self.__keys = []
        self.__room_housekeeping_log = []

    def is_room_available(self):
        pass

    def checkin(self):
        pass

    def checkout(self):
        pass


class RoomKey:
    def __init__(self, key_id, barcode, is_active, is_master):
        self.__key_id = key_id
        self.__barcode = barcode
        self.__issued_at = None
        self.__is_active = is_active
        self.__is_master = is_master

    def assign_room(self, room):
        pass


class RoomHousekeeping:
    def __init__(self, description, duration, housekeeper):
        self.__description = description
        self.__start_datetime = None
        self.__duration = duration
        self.__housekeeper = housekeeper

    def add_housekeeping(self, room):
        pass
