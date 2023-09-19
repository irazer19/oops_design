from transaction import Transcation


class WalletSystem:
    def __init__(self):
        self.__accounts = {}

    def overview(self):
        for acc_num in self.__accounts:
            acc = self.__accounts[acc_num]
            print(
                f"Account number: {acc.get_account_number()}, Balance: {acc.get_balance()}"
            )

    def add_account(self, account):
        self.__accounts[account.get_account_number()] = account

    def transfer(self, to_user_acc_num, from_user_acc_num, amount):
        to_user = self.__accounts.get(to_user_acc_num)
        from_user = self.__accounts.get(from_user_acc_num)
        if to_user and from_user:
            txn = Transcation(to_user=to_user, from_user=from_user, amount=amount)
            txn.send()
        else:
            print("Failed. One of the provided account number does not exist.")

    def get_account_statement(self, acc_num):
        stats = self.__accounts.get(acc_num).get_account_stats()
        print(
            f"Name: {stats['name']} \n "
            f"Account number: {stats['acc_num']} \n "
            f"Balance: {stats['balance']} \n"
            f"Status: {stats['status']}"
        )
