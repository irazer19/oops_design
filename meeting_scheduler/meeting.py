class Meeting:
    def __init__(self, id, participants_count, interval, room, subject):
        self.__id = id
        self.__participants_count = participants_count
        self.__participants = []
        self.__interval = interval
        self.__room = room
        self.__subject = subject

    def add_participants(self, participants):
        pass

    def remove_participants(self, participant):
        pass
