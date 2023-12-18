"""
Whenever we want to keep adding new functionality to an existing class object, we use the decorator design pattern.
Example:
    If we want to make a coffee, we can add extra sugar and vanilla topping to the base coffee.

"""

from abc import ABC, abstractmethod


class BaseCoffee(ABC):
    @abstractmethod
    def cost(self):
        pass


class Coffee(BaseCoffee):
    def cost(self):
        return 2


class AddMilk(BaseCoffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 3


class AddSugar(BaseCoffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1


mycoffee = Coffee()
mycoffee = AddMilk(mycoffee)
mycoffee = AddSugar(mycoffee)
print(mycoffee.cost())
