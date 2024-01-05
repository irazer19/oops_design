class BalanceSheet:
    def __init__(
        self, user_balance_map, total_expense, total_payment, total_get_back, total_owe
    ):
        self._user_balance_map = user_balance_map
        self._total_expense = total_expense
        self._total_payment = total_payment
        self._total_get_back = total_get_back
        self._total_owe = total_owe
