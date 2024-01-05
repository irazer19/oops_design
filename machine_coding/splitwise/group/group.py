class Group:
    def __init__(self, group_id, group_name, users, expenses, expense_controller):
        self.group_id = group_id
        self.group_name = group_name
        self.users = users
        self.expenses = expenses
        self.expense_controller = expense_controller

    def create_expense(
        self, expense_id, description, splits, amount, split_type, paid_by
    ):
        pass

    def add_member(self, member):
        pass

    def remove_member(self, member):
        pass
