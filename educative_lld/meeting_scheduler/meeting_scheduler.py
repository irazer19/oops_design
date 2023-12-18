class __MeetingScheduler(object):
    __instances = None

    # Scheduler is a singleton class that ensures it will have only one active instance at a time
    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__MeetingScheduler, cls).__new__(cls)
        return cls.__instances


class MeetingScheduler(metaclass=__MeetingScheduler):
    def __init__(self, organizer, calendar):
        self.__organizer = organizer
        self.__calendar = calendar
        self.__rooms = []

    def schedule_meeting(self, users, interval):
        pass

    def cancel_meeting(self, users, interval):
        pass

    def book_room(self, room, number_of_persons, interval):
        pass

    def release_room(self, room, interval):
        pass

    def check_rooms_availability(self, number_of_persons, interval):
        pass
