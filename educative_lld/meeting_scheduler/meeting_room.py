class MeetingRoom:
    def __init__(self, id, capacity, is_available):
        self.__id = id
        self.__capacity = capacity
        self.__is_available = is_available
        self.__booked_intervals = []  # list of interval objects
