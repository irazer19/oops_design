from item import Item
from state import IdleState
from item_shelf import ItemShelf
from inventory import Inventory
from vending_machine import VendingMachine
from coin import Coin


def run():
    soda = Item("Soda", 10)
    coke = Item("Coke", 15)
    s1 = ItemShelf(item=soda, quantity=3, product_code="S11")
    s2 = ItemShelf(item=coke, quantity=3, product_code="C11")
    inv = Inventory(item_shelves=[s1, s2])

    penny = Coin("PENNY", 1)
    nickel = Coin("NICKEL", 5)
    dime = Coin("DIME", 10)

    machine = VendingMachine(inventory=inv, state=IdleState(), coins=[])
    print(machine.display())
    state = machine.state
    print(f"Current state {state}")
    state.click_on_insert_coin_button(machine)
    state = machine.state
    print(f"Current state {state}")
    state.insert_coin(dime)
    state.insert_coin(nickel)
    state.click_on_select_product_button()
    state = machine.state
    print(f"Current state {state}")
    state.choose_product("S11")
    state = machine.state
    print(f"Current state {state}")
    state.dispense_product()
    state = machine.state
    print(f"Current state {state}")
    print(machine.display())
    pass


if __name__ == "__main__":
    run()
