from product import Product
from abc import ABC, abstractmethod


class Coupon(Product):
    pass


class PercentageCoupon(Coupon):
    def __init__(self, percentage, product):
        self.percentage = percentage
        self.product = product
        super().__init__(product.product_name, product.price)

    def get_price(self):
        return (self.product.get_price() * (100 - self.percentage)) / 100


class TypeCoupon(Coupon):
    alllowed_types = ["PHONE", "FURNITURE"]

    def __init__(self, prod_type, product):
        self.prod_type = prod_type
        self.product = product
        super().__init__(product.product_name, product.price)

    def get_price(self):
        if self.prod_type == "FURNITURE":
            return (self.product.get_price() * 20) / 100
        return self.product.get_price()
