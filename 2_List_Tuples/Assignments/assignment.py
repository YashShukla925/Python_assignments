print("Python List Assignment")


print("\nPart 1 - List Operations")

numbers = [1, 33, 56, 1001, 768]
print("Original list:", numbers)

numbers.append(89)
print("After adding 89 at end:", numbers)

numbers.insert(0, 39)
print("After adding 39 at beginning:", numbers)

numbers.extend([77, 66, 44])
print("After adding [77, 66, 44]:", numbers)

numbers.append([99, 88])
print("After adding [99, 88] as nested list:", numbers)

numbers.insert(2, "Apple")
print("After inserting Apple at position 2:", numbers)

numbers[2] = "Pineapple"
print("After replacing Apple with Pineapple:", numbers)

numbers.pop(4)
print("After removing element at position 4:", numbers)

numbers.remove("Pineapple")
print("After removing Pineapple:", numbers)


print("\nPart 2 - Pair Sum Problem")

values = [1, 2, 3, 4, 5, 6, 7, 8]
z = 9
pairs = []

for first_number in values:
    for second_number in values:
        if first_number < second_number and first_number + second_number == z:
            pairs.append((first_number, second_number))

final_pairs = tuple(pairs)
print("Final output:", final_pairs)
