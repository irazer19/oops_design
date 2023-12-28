from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def click_on_insert_coin_button(self, vending_machine):
        pass

    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def refund_money(self, insert_amount):
        pass

    @abstractmethod
    def choose_product(self, product_code):
        pass

    @abstractmethod
    def get_change(self, change_amount):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def update_inventory(self):
        pass

    @abstractmethod
    def click_on_select_product_button(self):
        pass


class IdleState(State):
    def __init__(self):
        super().__init__(vending_machine=None)

    def click_on_insert_coin_button(self, vending_machine):
        vending_machine.state = HasMoneyState(vending_machine)

    def insert_coin(self, coin):
        pass

    def refund_money(self, insert_amount):
        pass

    def choose_product(self, product_code):
        pass

    def get_change(self, change_amount):
        pass

    def dispense_product(self):
        pass

    def update_inventory(self):
        pass

    def click_on_select_product_button(self):
        pass


class HasMoneyState(State):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def click_on_insert_coin_button(self, vending_machine):
        pass

    def insert_coin(self, coin):
        print("Coin inserted")
        self.vending_machine.add_coin(coin)

    def refund_money(self, insert_amount):
        print("Money refunded")
        pass

    def choose_product(self, product_code):
        pass

    def get_change(self, change_amount):
        pass

    def dispense_product(self):
        pass

    def update_inventory(self):
        pass

    def click_on_select_product_button(self):
        self.vending_machine.state = SelectionState(self.vending_machine)


class SelectionState(State):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def click_on_insert_coin_button(self, vending_machine):
        pass

    def insert_coin(self, coin):
        pass

    def refund_money(self, insert_amount):
        print("Money refunded")
        pass

    def choose_product(self, product_code):
        for item_shelf in self.vending_machine.inventory.item_shelves:
            if item_shelf.product_code == product_code:
                # check for product stock
                if item_shelf.quantity <= 0:
                    print("Sorry, this item is out of stock.")
                    return
                # Check for sufficient amount
                insert_amount = sum([c.value for c in self.vending_machine.coins])
                if insert_amount < item_shelf.item.price:
                    print("Insufficient money inserted")
                    self.refund_money(insert_amount)
                    return
                if insert_amount > item_shelf.item.price:
                    self.get_change(insert_amount - item_shelf.item.price)
                self.vending_machine.state = DispenseState(
                    self.vending_machine, item_shelf.product_code
                )

        pass

    def get_change(self, change_amount):
        print(f"Getting the change for amount: {change_amount}")
        pass

    def dispense_product(self):
        pass

    def update_inventory(self):
        pass

    def click_on_select_product_button(self):
        pass


class DispenseState(State):
    def __init__(self, vending_machine, product_code):
        super().__init__(vending_machine)
        self.product_code = product_code

    def click_on_insert_coin_button(self, vending_machine):
        pass

    def insert_coin(self, coin):
        pass

    def refund_money(self, insert_amount):
        pass

    def choose_product(self, product_code):
        pass

    def get_change(self, change_amount):
        pass

    def dispense_product(self):
        print(f"Product dispensed with code: {self.product_code}")
        self.update_inventory()
        self.vending_machine.state = IdleState()

    def update_inventory(self):
        for item_shelf in self.vending_machine.inventory.item_shelves:
            if item_shelf.product_code == self.product_code:
                item_shelf.quantity -= 1

    def click_on_select_product_button(self):
        pass
