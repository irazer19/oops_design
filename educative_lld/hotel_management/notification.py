# Notification is an abstract class
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, notification_id, created_on, content):
        self.__notificationId = notification_id
        self.__created_on = created_on
        self.__content = content

    # account here refers to an instance of the Account class
    @abstractmethod
    def send_notification(self, person):
        pass


class SMSNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class
    def send_notification(self, person):
        # functionality
        pass


class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class
    def send_notification(self, person):
        # functionality
        pass
