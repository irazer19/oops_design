import sys

from wallet_system import WalletSystem
from account import Account
from user import User


def main():
    ws = WalletSystem()
    """
    1. Create Wallet
    2. Transfer amount
    3. Account Statement
    4. Overview
    5. Exit
    """
    while True:
        choice = int(
            input(
                """
            1. Create Wallet
            2. Transfer amount
            3. Account Statement
            4. Overview
            5. Exit
        
        """
            )
        )
        if choice == 1:
            name = input("Please enter your name: ")
            email = input("Please enter your email: ")
            amount = int(input("Please enter the amount: "))
            user = User(name=name, email=email)
            acc = Account(user=user, amount=amount)
            acc.create_wallet()
            ws.add_account(acc)
            print(
                f"Wallet successfully created. Account number: {acc.get_account_number()}"
            )
        elif choice == 2:
            to_user_acc_num = int(input("Please enter the receivers account number: "))
            from_user_acc_num = int(input("Please enter the senders account number: "))
            amount = int(input("Please enter the amount to be transfered: "))
            ws.transfer(
                to_user_acc_num=to_user_acc_num,
                from_user_acc_num=from_user_acc_num,
                amount=amount,
            )
        elif choice == 3:
            acc_num = int(
                input("Please enter the account number to view the statement: ")
            )
            ws.get_account_statement(acc_num=acc_num)

        elif choice == 4:
            ws.overview()

        elif choice == 5:
            sys.exit()


if __name__ == "__main__":
    main()
