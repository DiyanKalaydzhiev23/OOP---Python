from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        return


class Cat(Animal):

    def make_sound(self):
        return "meow"


class Dog(Animal):

    def make_sound(self):
        return "woof-woof"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat(), Dog()]
animal_sound(animals)
