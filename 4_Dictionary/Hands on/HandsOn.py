# Dictionary Basics - Hands On

# Q1. Create a dictionary for student details
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "city": "Delhi"
}
print(student)


# Q2. Access value using key
print(student["name"])
print(student["course"])


# Q3. Access value using get()
print(student.get("city"))
print(student.get("marks"))


# Q4. Add a new key-value pair
student["marks"] = 85
print(student)


# Q5. Update an existing value
student["age"] = 22
print(student)


# Q6. Delete a key-value pair
student.pop("city")
print(student)


# Q7. Print all keys
print(student.keys())


# Q8. Print all values
print(student.values())


# Q9. Print all key-value pairs
print(student.items())


# Q10. Check if key exists in dictionary
print("name" in student)
print("city" in student)


# Q11. Loop through dictionary keys
for key in student:
    print(key)


# Q12. Loop through dictionary values
for value in student.values():
    print(value)


# Q13. Loop through dictionary keys and values
for key, value in student.items():
    print(key, value)


# Q14. Store marks of students and print marks greater than 80
marks = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 90,
    "John": 78
}

for name, mark in marks.items():
    if mark > 80:
        print(name, mark)


# Q15. Count frequency of each item using dictionary
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}

for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)


# Q16. Find student with highest marks
highest_student = ""
highest_marks = 0

for name, mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        highest_student = name

print(highest_student, highest_marks)


# Q17. Create dictionary from two lists
names = ["Rahul", "Amit", "Sneha"]
courses = ["Python", "SQL", "AWS"]
student_courses = {}

for i in range(len(names)):
    student_courses[names[i]] = courses[i]

print(student_courses)
