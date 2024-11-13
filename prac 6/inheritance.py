# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} says: {dog.speak()}")  # Output: Buddy says: Woof!
print(f"{cat.name} says: {cat.speak()}")  # Output: Whiskers says: Meow!
