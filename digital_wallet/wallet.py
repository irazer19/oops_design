class Wallet:
    def __init__(self, amount):
        self.__amount = amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount
