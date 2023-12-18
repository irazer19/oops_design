from abc import ABC, abstractmethod


class Observable(ABC):
    def __init__(self):
        self.observers = []
        self.stock_count = 0

    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass

    @abstractmethod
    def get_data(self):
        pass


# For each item we create a concrete observable class.
class IphoneObservable(Observable):
    def __init__(self):
        super().__init__()

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def set_data(self, stock_count):
        self.stock_count = stock_count
        self.notify()

    def get_data(self):
        return self.stock_count
