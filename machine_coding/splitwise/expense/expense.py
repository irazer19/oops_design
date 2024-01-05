class Expense:
    def __init__(self, expense_id, description, amount, splits, split_type, paid_by):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.splits = splits
        self.split_type = split_type
        self.paid_by = paid_by
