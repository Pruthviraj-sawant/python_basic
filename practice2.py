# string and charachters



name="pruthvi"
print(name.replace("pruthvi","sawant"))
print(name[0])
print(name[3:7])
print(name.upper())
print(name.lower())
print(name.count(name))

print(len(name))        




for char in "Python":
    print(char)

# list 

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'orange']

print(fruits[0])   # apple
print(fruits[-1])  # orange

# tuple
numbers = (1, 2, 3, 4)
print(numbers[0])  # 1
# numbers[0] = 5  # This will raise a TypeError because tuples are immutable.




# dictionary
student = {"name": "Alice", "age": 20, "major": "Computer Science"}
print(student["name"])  # Alice
student["age"] = 21     # Update age
student["grade"] = "A"  # Add a new key-value pair
print(student)  # {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'grade': 'A'}


for key, value in student.items():
    print(f"{key}: {value}")

# array



arr = [1, 2, 3, 4, 5]
print(arr[2])  # 3
arr.append(6)
arr.remove(2)
print(arr)  # [1, 3, 4, 5, 6]



from array import array
ar = array('i', [1, 2, 3, 4])
ar.append(5)
print(ar)  # array('i', [1, 2, 3, 4, 5])

# lambda
# lambda arguments: expression

add= lambda x,y : x+y
print(add(2, 3))

numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]



