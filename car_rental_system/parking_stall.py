class ParkingStall:
    def __init__(self, stall_id, location_identifier):
        self.__stall_id = stall_id
        self.__location_identifier = location_identifier
        self.__vehicles = []


class Fine:
    def __init__(self, amount, reason):
        self.__amount = amount
        self.__reason = reason

    def calculate_fine(self):
        pass
