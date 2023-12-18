from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, username, password, person, status):
        self.__username = username
        self.__password = password
        self.__person = person
        self.__status = status

    @abstractmethod
    def reset_password(self):
        pass


class Admin(Account):
    def __init__(self, username, password, person, status):
        super().__init__(username, password, person, status)

    def add_parking_spot(self, spot):
        pass

    def add_entrance(self, entrance):
        pass

    def add_exit(self, exit):
        pass

    def reset_password(self):
        pass


class ParkingAttendant(Account):
    def __init__(self, username, password, person, status):
        super().__init__(username, password, person, status)

    def process_ticket(self, ticket_number):
        pass

    def reset_password(self):
        pass
