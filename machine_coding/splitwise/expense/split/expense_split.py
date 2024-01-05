from abc import ABC, abstractmethod


class ExpenseSplit(ABC):
    @abstractmethod
    def validate_split(self, splits):
        pass


class EqualSplit(ExpenseSplit):
    def validate_split(self, splits):
        pass


class UnequalSplit(ExpenseSplit):
    def validate_split(self, splits):
        pass


class PercentageSplit(ExpenseSplit):
    def validate_split(self, splits):
        pass
