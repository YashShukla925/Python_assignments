# Operators Practice

# 1. Arithmetic operators
a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# 2. Comparison operators
x = 15
y = 10

print("X is greater than Y:", x > y)
print("X is less than Y:", x < y)
print("X is equal to Y:", x == y)
print("X is not equal to Y:", x != y)
print("X is greater than or equal to Y:", x >= y)
print("X is less than or equal to Y:", x <= y)


# 3. Logical operators
age = 22
has_id_card = True

print("Allowed using and:", age >= 18 and has_id_card)
print("Allowed using or:", age >= 18 or has_id_card)
print("Opposite of has ID card:", not has_id_card)


# 4. Assignment operators
number = 10

number += 5
print("After += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 4
print("After /= :", number)


# 5. Membership operators
fruits = ["apple", "banana", "mango"]

print("Apple is in fruits:", "apple" in fruits)
print("Orange is not in fruits:", "orange" not in fruits)


# 6. Identity operators
list_one = [1, 2, 3]
list_two = list_one
list_three = [1, 2, 3]

print("List one is list two:", list_one is list_two)
print("List one is list three:", list_one is list_three)
print("List one is not list three:", list_one is not list_three)


# 7. Bitwise operators
p = 5
q = 3

print("Bitwise AND:", p & q)
print("Bitwise OR:", p | q)
print("Bitwise XOR:", p ^ q)
print("Bitwise NOT:", ~p)
print("Left shift:", p << 1)
print("Right shift:", p >> 1)


# 8. Calculate simple interest using operators
principal = 5000
rate = 8
time = 2

simple_interest = principal * rate * time / 100
print("Simple interest:", simple_interest)


# 9. Calculate area and perimeter of rectangle
length = 12
width = 8

area = length * width
perimeter = 2 * (length + width)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)


# 10. Check marks using comparison and logical operators
marks = 82

print("Marks are between 80 and 100:", marks >= 80 and marks <= 100)
print("Marks are below passing:", marks < 35)
