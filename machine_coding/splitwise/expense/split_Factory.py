from oops_design.machine_coding.splitwise.expense.split.expense_split import (
    EqualSplit,
    UnequalSplit,
    PercentageSplit,
)


class SplitFactory:
    def __init__(self, split_type):
        self.split_type = split_type

    def get_expense_split(self):
        if self.split_type == "EQUAL":
            return EqualSplit()
        elif self.split_type == "UNEQUAL":
            return UnequalSplit()
        elif self.split_type == "PERCENTAGE":
            return PercentageSplit()
