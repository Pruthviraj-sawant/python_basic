
# Parent class
class Animal:
    def speak(self):
        pass  # Abstract method (not implemented)

# Child classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.speak())

# Using polymorphism
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
