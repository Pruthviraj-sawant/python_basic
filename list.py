my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.insert(2, 'a')
print(my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6]

my_list.extend([7, 8])
print(my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6, 7, 8]

my_list.remove('a')
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

popped_element = my_list.pop(3)
print(popped_element)  # Output: 4
print(my_list)         # Output: [1, 2, 3, 5, 6, 7, 8]

my_list.clear()
print(my_list)  # Output: []

my_list = [10, 20, 30, 40, 50]

print(my_list[0])  # Output: 10
print(my_list[-1]) # Output: 50

print(my_list[1:4])  # Output: [20, 30, 40]


my_list = [5, 3, 8, 2, 7]

my_list.sort()
print(my_list)  # Output: [2, 3, 5, 7, 8]

my_list.reverse()
print(my_list)  # Output: [8, 7, 5, 3, 2]

count_5 = my_list.count(5)
print(count_5)  # Output: 1

index_of_7 = my_list.index(7)
print(index_of_7)  # Output: 1

new_list = my_list.copy()
print(new_list)  # Output: [8, 7, 5, 3, 2]
