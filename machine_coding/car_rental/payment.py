from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self._amount = amount

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        pass


class UPI(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        pass
