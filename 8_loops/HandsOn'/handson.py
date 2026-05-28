# Loops Practice


# 1. For loop with a list
fruits = ["apple", "banana", "mango", "orange"]

print("Fruits:")
for fruit in fruits:
    print(fruit)


# 2. For loop with range
print("\nNumbers from 1 to 5:")
for number in range(1, 6):
    print(number)


# 3. For loop to find sum
total = 0

for number in range(1, 11):
    total += number

print("\nSum of numbers from 1 to 10:", total)


# 4. For loop with break
print("\nBreak example:")
for number in range(1, 10):
    if number == 5:
        break
    print(number)


# 5. For loop with continue
print("\nContinue example:")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)


# 6. While loop
count = 1

print("\nWhile loop from 1 to 5:")
while count <= 5:
    print(count)
    count += 1


# 7. While loop to print even numbers
number = 2

print("\nEven numbers from 2 to 10:")
while number <= 10:
    print(number)
    number += 2


# 8. While loop with break
number = 1

print("\nWhile loop break example:")
while number <= 10:
    if number == 6:
        break
    print(number)
    number += 1


# 9. While loop with continue
number = 0

print("\nWhile loop continue example:")
while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)


# 10. Nested loop
print("\nMultiplication table from 1 to 3:")
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end=" ")
    print()
