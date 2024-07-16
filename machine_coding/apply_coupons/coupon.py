from abc import ABC, abstractmethod


class Coupon(ABC):
    @abstractmethod
    def apply(self, product):
        pass


class PercentageOffCoupon(Coupon):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, product):
        return product.get_price() * (1 - self.percentage / 100)


class FixedAmountOffCoupon(Coupon):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, product):
        return max(0, product.get_price() - self.amount)
