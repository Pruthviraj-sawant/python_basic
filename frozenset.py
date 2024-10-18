fruits = frozenset(["apple", "banana", "orange"])

print("orange" in fruits)  

print(len(fruits)) 
more_fruits = frozenset(["grape", "kiwi"])
combined_fruits = fruits.union(more_fruits)
print(combined_fruits)  
common_fruits = fruits.intersection(more_fruits)
print(common_fruits)  
diff_fruits = fruits.difference(more_fruits)
print(diff_fruits)  
print(fruits.issubset(combined_fruits))  
print(combined_fruits.issuperset(fruits)) 
print(fruits.isdisjoint(more_fruits))  

sym_diff_fruits = fruits.symmetric_difference(more_fruits)
print(sym_diff_fruits) 
for fruit in fruits:
    print(fruit)

print(str(fruits))  # Output: frozenset({'banana', 'orange', 'apple'})​
print(hash(fruits))

