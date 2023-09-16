class DisplayBoard:
    def __init__(
        self,
        id,
        handicapped_spot: list,
        compact_spot: list,
        large_spot: list,
        motorbike_spot: list,
    ):
        self.__id = id
        self.__handicapped_spot = handicapped_spot
        self.__compact_spot = compact_spot
        self.__large_spot = large_spot
        self.__motorbike_spot = motorbike_spot

    def show_free_slot(self):
        pass


class ParkingRate:
    def __init__(self, hours, rate):
        self.__hours = hours
        self.__rate = rate

    def calculate(self):
        pass
