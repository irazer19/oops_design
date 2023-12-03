from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vtype, reg_num, color):
        self.vtype = vtype
        self.reg_num = reg_num
        self.color = color


class Car(Vehicle):
    def __init__(self, vtype, reg_num, color):
        super().__init__(vtype, reg_num, color)


class Truck(Vehicle):
    def __init__(self, vtype, reg_num, color):
        super().__init__(vtype, reg_num, color)


class Bike(Vehicle):
    def __init__(self, vtype, reg_num, color):
        super().__init__(vtype, reg_num, color)
