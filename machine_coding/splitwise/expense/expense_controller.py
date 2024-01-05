class ExpenseController:
    def __init__(self, balance_sheet):
        self.balance_sheet = balance_sheet

    def create_expense(
        self, expense_id, amount, description, paid_by, split_type, splits
    ):
        # Create expense and update the balance sheet.
        pass
