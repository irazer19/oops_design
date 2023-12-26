"""
The Null object design pattern says that if we pass Null/None instead of creating an object, then we should replace
the Null/None with a default Null object with default behaviour.
It means, that instead of passing Null/None, we pass an object which handles the default or Null case properly.

In the below example, lets say for a condition we are unable to create an animal object, in this case we will not return
Null/None from the function but a NullAnimal object.

"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Dog Sound!!")


class NullAnimal(Animal):
    def make_sound(self):
        print("No Sound!!")


def make_animal_sound(animal):
    animal.make_sound()


dog = Dog()
make_animal_sound(dog)

null = NullAnimal()
make_animal_sound(null)
