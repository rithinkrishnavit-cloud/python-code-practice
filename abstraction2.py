# ABC = used to create abstract class
# abstractmethod = a method that chiled class
from abc import ABC, abstractmethod


# create an abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# create child class
class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()
