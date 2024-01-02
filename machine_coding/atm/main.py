from bank_account import BankAccount
from card import Card
from atm import Atm
from state import IdleState
from user import User


def run():
    bank_account = BankAccount(5000)
    card = Card(card_number="12345", bank_account=bank_account, pin="1234")
    user = User(username="saurav", card=card, bank_account=bank_account)
    atm = Atm(
        balance=20000,
        card=None,
        state=IdleState(),
        num_of_2k=5,
        num_of_500=10,
        num_of_100=50,
    )

    state = atm.state
    state.insert_card(atm, user.card)
    state = atm.state
    state.authenticate_pin("1234")
    state = atm.state
    state.select_operation("SHOW_BALANCE")
    state = atm.state
    state.display_balance()

    pass


if __name__ == "__main__":
    run()
