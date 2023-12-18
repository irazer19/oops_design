class Product:
    def __init__(self, name, id, price, type):
        self.__name = name
        self.__id = id
        self.__price = price
        self.__type = type  # here type is an instance of ProductType


class Rack:
    def __init__(self, product_id, rack_number):
        self.__product_id = product_id
        self.__rack_number = rack_number

    def is_empty(self):
        pass


class Inventory:
    def __init__(self, no_of_products, products):
        self.__no_of_products = no_of_products
        self.__products = products  # List

    def add_product(self, product_id, rack_id):
        pass

    def remove_product(self, product_id, rack_id):
        pass
