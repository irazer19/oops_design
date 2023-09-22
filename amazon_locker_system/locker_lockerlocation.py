class Locker:
    def __init__(self, locker_id, locker_size, location_id, locker_state):
        self.__locker_id = locker_id
        self.__locker_size = locker_size
        self.__location_id = location_id
        self.__locker_state = locker_state

    def add_package(self):
        pass

    def remove_package(self):
        pass


class LockerLocation:
    def __init__(self, name, lockers, longitude, latitude, open_time, close_time):
        self.__name = name
        self.__lockers = lockers  # list of lockers
        self.__longitude = longitude
        self.__latitude = latitude
        self.__open_time = open_time
        self.__close_time = close_time
