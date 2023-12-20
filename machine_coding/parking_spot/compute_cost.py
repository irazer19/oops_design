from abc import ABC, abstractmethod


class ComputeCost(ABC):
    @abstractmethod
    def get_cost(self, ticket):
        pass


class HourlyComputeCost(ComputeCost):
    def get_cost(self, ticket):
        return 5


class MinuteComputeCost(ComputeCost):
    def get_cost(self, ticket):
        return 3
