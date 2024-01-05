"""
Used to build an object in steps.
Ex: To build a car, we use a CarBuilder class with which we interact to add wheels, engine, etc.
Once all the steps are completed ,then we call the build method which returns the Car.

Here the CarBuilder class interacts with the Car class to build it.

"""


class Car:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)


class CarBuilder:
    def __init__(self):
        self._car = Car()

    def add_wheel(self):
        self._car.add("Wheel")
        return self

    def add_engine(self):
        self._car.add("Engine")
        return self

    def build(self):
        return self._car
