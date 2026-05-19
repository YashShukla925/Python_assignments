# Sets Assignment - 18th May

python_students = {"Rahul", "Amit", "Sneha", "John"}
sql_students = {"John", "Sneha", "David", "Meena"}
aws_students = {"Rahul", "David", "Kiran"}

# Q1. Students in both Python and SQL
print(python_students & sql_students)

# Q2. Students in all 3 courses
print(python_students & sql_students & aws_students)

# Q3. Students only in Python
print(python_students - sql_students - aws_students)

# Q4. Total unique students
all_students = python_students | sql_students | aws_students
print(all_students)
print(len(all_students))

# Q5. Students not enrolled in AWS
print(all_students - aws_students)

# Q6. Students in more than 2 courses
more_than_two_courses = set()

for student in all_students:
    count = 0

    if student in python_students:
        count += 1

    if student in sql_students:
        count += 1

    if student in aws_students:
        count += 1

    if count > 2:
        more_than_two_courses.add(student)

print(more_than_two_courses)

# Q7. Students whose name starts with 'Ra'
ra_students = set()

for student in all_students:
    if student.startswith("Ra"):
        ra_students.add(student)

print(ra_students)

# Q8. Students whose name ends with 'na' or 'an'
ending_students = set()

for student in all_students:
    if student.endswith("na") or student.endswith("an"):
        ending_students.add(student)

print(ending_students)


# Q9. Frequency Counter Using Sets + Lists
data = [1, 2, 2, 3, 4, 4, 4, 5]

# Unique values
unique_values = set(data)
print(unique_values)

# Duplicate values
duplicate_values = set()
for value in unique_values:
    if data.count(value) > 1:
        duplicate_values.add(value)

print(duplicate_values)

# Frequency of each value
frequency = {}

for value in data:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

print(frequency)
