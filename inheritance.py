class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says Woof")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow")


# Usage
d = Dog("Tommy")
d.eat()  # Tommy is eating       ← inherited
d.sleep()  # Tommy is sleeping     ← inherited
d.bark()  # Tommy says Woof       ← own method

c = Cat("Kitty")
c.eat()  # Kitty is eating       ← inherited
c.meow()  # Kitty says Meow
