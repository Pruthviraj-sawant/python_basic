#tuple
thistuple=(1,2,3,4,5,5,5,5,5,5,5,5,5)
x=thistuple.count(5)
print(x)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(thistuple)
print(len(thistuple))
thistuple = ("apple")
print(type(thistuple))
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
# Define a tuple
person = ("Alice", 30, "Engineer")

# Accessing elements of the tuple directly
name = person[0]
age = person[1]
profession = person[2]

# Displaying tuple information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

# Tuples are immutable, so to change a value, create a new tuple
new_profession = "Data Scientist"
person = (name, age, new_profession)

# Displaying updated tuple information
print("\nAfter updating profession:")
print(f"Name: {person[0]}")
print(f"Age: {person[1]}")
print(f"Profession: {person[2]}")