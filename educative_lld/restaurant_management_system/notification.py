# Notification is an abstract class
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, notification_id, created_on, content):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content

    # account here refers to an instance of the Account class
    @abstractmethod
    def send(self, person):
        pass


class SmsNotification(Notification):
    def __init__(self, phone, notification_id, created_on, content):
        self.__phone = phone
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class
    def send(self, person):
        # functionality
        pass


class EmailNotification(Notification):
    def __init__(self, email, notification_id, created_on, content):
        self.__email = email
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class
    def send(self, person):
        # functionality
        pass
