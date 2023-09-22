class Item:
    def __init__(self, item_id, quantity):
        self.__item_id = item_id
        self.__quantity = quantity


class Order:
    def __init__(self, order_id, items, delivery_location):
        self.__order_id = order_id
        self.__items = items  # List of items
        self.__delivery_location = delivery_location
