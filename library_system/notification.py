from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, id, creation_date, content):
        self.__notification_id = id
        self.__creation_date = creation_date
        self.__content = content

    @abstractmethod
    def send(self):
        pass


class PostalNotification(Notification):
    def __init__(self, id, creation_date, content, address):
        super().__init__(id, creation_date, content)
        self.__address = address

    def send(self):
        pass


class EmailNotification(Notification):
    def __init__(self, id, creation_date, content, email):
        super().__init__(id, creation_date, content)
        self.__email = email

    def send(self):
        pass
