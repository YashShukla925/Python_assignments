# Dictionary Assignment - 19th May

# Student Result System
students = {
    "Rahul": 85,
    "Sneha": 67,
    "Amit": 67,
    "John": 45
}

# Q1. Find topper
highest_marks = max(students.values())

for student, marks in students.items():
    if marks == highest_marks:
        print("Topper:", student, marks)

# Q2. Find failed students (<50)
failed_students = []

for student, marks in students.items():
    if marks < 50:
        failed_students.append(student)

print("Failed students:", failed_students)

# Q3. Find students with same marks
same_marks = {}

for student, marks in students.items():
    if marks in same_marks:
        same_marks[marks].append(student)
    else:
        same_marks[marks] = [student]

for marks, student_list in same_marks.items():
    if len(student_list) > 1:
        print("Same marks:", marks, student_list)

# Q4. Print grades
grades = {}

for student, marks in students.items():
    if marks >= 90:
        grades[student] = "A+"
    elif marks >= 80:
        grades[student] = "A"
    elif marks >= 70:
        grades[student] = "B"
    elif marks >= 60:
        grades[student] = "C"
    elif marks >= 50:
        grades[student] = "D"
    else:
        grades[student] = "Fail"

print("Grades:", grades)


# Merge Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged_dictionary = {}
merged_dictionary.update(d1)
merged_dictionary.update(d2)

print("Merged dictionary:", merged_dictionary)

# Sort dictionary by key
sorted_by_key = dict(sorted(merged_dictionary.items()))
print("Sorted by key:", sorted_by_key)

# Sort dictionary by value
sorted_by_value = dict(sorted(merged_dictionary.items(), key=lambda item: item[1]))
print("Sorted by value:", sorted_by_value)


# Shopping Cart System
cart = {
    "Laptop": {"price": 50000, "qty": 1},
    "Mouse": {"price": 500, "qty": 2}
}

# Q1. Add product
cart["Keyboard"] = {"price": 1500, "qty": 1}
print("After adding product:", cart)

# Q2. Update quantity
cart["Mouse"]["qty"] = 3
print("After updating quantity:", cart)

# Q3. Remove product
cart.pop("Keyboard")
print("After removing product:", cart)

# Q4. Calculate total bill
total_bill = 0

for product, details in cart.items():
    total_bill += details["price"] * details["qty"]

print("Total bill:", total_bill)

# Q5. Find most expensive product
most_expensive_product = ""
highest_price = 0

for product, details in cart.items():
    if details["price"] > highest_price:
        highest_price = details["price"]
        most_expensive_product = product

print("Most expensive product:", most_expensive_product, highest_price)

# Q6. Apply 10% discount if total > 50000
if total_bill > 50000:
    discount = total_bill * 10 / 100
    final_bill = total_bill - discount
else:
    discount = 0
    final_bill = total_bill

print("Discount:", discount)
print("Final bill:", final_bill)
