class VendingMachine:
    def __init__(self, inventory, state, coins):
        self.inventory = inventory
        self.state = state
        self.coins = coins

    def add_coin(self, coin):
        self.coins.append(coin)

    def display(self):
        self.inventory.display()
