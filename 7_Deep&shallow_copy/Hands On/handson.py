# Deep Copy and Shallow Copy Practice

import copy


# 1. Normal assignment
list_one = [10, 20, 30]
list_two = list_one

list_two.append(40)

print("Original list:", list_one)
print("Assigned list:", list_two)
print("Both are same object:", list_one is list_two)


# 2. Shallow copy
original_list = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original_list)

shallow_copy[0][0] = 100

print("Original list after shallow copy change:", original_list)
print("Shallow copied list:", shallow_copy)


# 3. Deep copy
numbers = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(numbers)

deep_copy[0][0] = 100

print("Original list after deep copy change:", numbers)
print("Deep copied list:", deep_copy)
