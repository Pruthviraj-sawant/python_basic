my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

my_set.discard(10)  # Does nothing since 10 is not in the set

element = my_set.pop()
print(element)  # Output: (an arbitrary element, e.g., 1)
print(my_set)   # Output: (the set after popping, e.g., {2, 4, 5, 6})

print(4 in my_set)   # Output: True
print(10 in my_set)  # Output: False

set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


my_set.clear()
print(my_set)  # Output: set()
