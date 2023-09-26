# The __VendingMachine is a singleton class that ensures it will have only one active instance at a time


class VendingMachine:
    def __init__(self, current_state, amount, no_of_racks, racks, available_racks):
        self.__current_state = current_state
        self.__amount = amount
        self.__no_of_racks = no_of_racks
        self.__racks = racks  # List of racks
        self.__available_racks = available_racks

    def insert_money(self, amount):
        pass

    def press_button(self, rack_number):
        pass

    def return_change(self, amount):
        pass

    def update_inventory(self, rack_number):
        pass

    def dispense_product(self, rack_number):
        pass

    def get_product_id_at_rack(self, rack_number):
        pass
