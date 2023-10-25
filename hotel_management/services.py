from abc import ABC, abstractmethod
from datetime import datetime


class Service(ABC):
    def __init__(self):
        pass


class RoomCharge(ABC):
    def __init__(self):
        self.__issue_at = datetime.today()

    def add_invoice_item(self, invoice):
        pass


class Amenity(Service):
    def __init__(self, name, description):
        super().__init__()
        self.__name = name
        self.__description = description


class RoomService(Service):
    def __init__(self, is_chargeable, request_time):
        super().__init__()
        self.__is_chargeable = is_chargeable
        self.__request_time = request_time


class KitchenService(Service):
    def __init__(self, description):
        super().__init__()
        self.__description = description
