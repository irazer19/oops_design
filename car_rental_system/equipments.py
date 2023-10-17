# Equipment is an abstract class
from abc import ABC, abstractmethod


class Equipment(ABC):
    def __init__(self, equipment_id, price):
        self.__equipment_id = equipment_id
        self.__price = price


class Navigation(Equipment):
    def __init__(self, equipment_id, price):
        super().__init__(equipment_id, price)


class ChildSeat(Equipment):
    def __init__(self, equipment_id, price):
        super().__init__(equipment_id, price)


class SkiRack(Equipment):
    def __init__(self, equipment_id, price):
        super().__init__(equipment_id, price)
