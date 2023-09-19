from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, status):
        self.__status = status

    def press_down(self):
        self.__status = True

    def unpress(self):
        self.__status = False

    @abstractmethod
    def is_pressed(self, callback):
        pass


class HallButton(Button):
    def __init__(self, button_sign):
        self.__button_sign = button_sign
        super().__init__(False)

    def is_pressed(self, callback):
        callback()


class ElevatorButton(Button):
    def __init__(self, destination_floor_number):
        super().__init__(False)
        self.__destination_floor_number = destination_floor_number

    def is_pressed(self, callback):
        pass
