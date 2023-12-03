from abc import ABC, abstractmethod


class Slot(ABC):
    def __init__(self, stype, slot_num, vehicle, status):
        self.stype = stype
        self.slot_num = slot_num
        self.vehicle = vehicle
        self.status = status
