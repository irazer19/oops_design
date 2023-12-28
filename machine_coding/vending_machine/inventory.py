class Inventory:
    def __init__(self, item_shelves):
        self.item_shelves = item_shelves

    def add_item_shelf(self, item_shelf):
        self.item_shelves.append(item_shelf)

    def display(self):
        for item_shelf in self.item_shelves:
            print(
                item_shelf.item.item_name,
                item_shelf.product_code,
                item_shelf.quantity,
                item_shelf.item.price,
            )
