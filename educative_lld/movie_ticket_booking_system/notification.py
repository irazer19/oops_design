# Notification is an abstract class
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, notification_id, created_on, content):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content

    # person here refers to an instance of the Person class
    @abstractmethod
    def send_notification(self, person):
        pass


class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    # person here refers to an instance of the Person class
    def send_notification(self, person):
        # functionality
        pass


class PhoneNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    # person here refers to an instance of the Person class
    def send_notification(self, person):
        # functionality
        pass
