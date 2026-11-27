import time


class Animal:
    def eat(self):
        print("Animal is eating")

    def walk(self):
        print("Animal is walking")

    def drink(self):
        print("Animal is drinking")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def cry(self):
        print("Cat is crying")


d1 = Dog()
c1 = Cat()

time.sleep(1)
d1.bark()
d1.drink()
d1.walk()

time.sleep(1)
c1.cry()
c1.walk()
c1.eat()
