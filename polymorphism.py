class Dog:
    def sound(self):
        print("Dog says: Woof")


class Cat:
    def sound(self):
        print("Cat says: Meow")


class Cow:
    def sound(self):
        print("Cow says: Moo")


# Same method name — different behavior
for animal in [Dog(), Cat(), Cow()]:
    animal.sound()
