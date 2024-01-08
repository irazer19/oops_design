from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def get_price(self):
        return self.price
