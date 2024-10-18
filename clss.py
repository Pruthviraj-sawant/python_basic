class MyClass:
    # Class attribute (shared among all instances)
    class_attribute = "I am a class attribute"

    # Constructor method (called when an instance is created)
    def __init__(self, name):
        # Instance attribute (unique to each instance)
        self.name = name

    # Method (a function defined within a class)
    def greet(self):
        print( f"Hello, {self.name}!")



# Create an instance of MyClass
obj = MyClass("Alice")

# Accessing the instance attribute and method
print(obj.name)           # Output: Alice
print(obj.greet())        # Output: Hello, Alice!

# Accessing the class attribute
print(obj.class_attribute)  # Output: I am a class attribute

