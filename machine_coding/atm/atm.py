class Atm:
    def __init__(self, balance, card, state, num_of_2k, num_of_500, num_of_100):
        self.balance = balance
        self.card = card
        self.state = state
        self.num_of_2k = num_of_2k
        self.num_of_500 = num_of_500
        self.num_of_100 = num_of_100

    def add_card(self, card):
        self.card = card

    def remove_card(self):
        self.card = None
