# If Else Conditional Statement Practice

# 1. Check positive, negative, or zero
number = -5

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")


# 2. Check even or odd
number = 24

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 3. Check voting eligibility
age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# 4. Find largest of two numbers
a = 45
b = 30

if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both numbers are equal")


# 5. Find largest of three numbers
x = 12
y = 55
z = 34

if x >= y and x >= z:
    print("X is largest")
elif y >= x and y >= z:
    print("Y is largest")
else:
    print("Z is largest")


# 6. Grade calculator
marks = 76

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")


# 7. Check leap year
year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 8. Login system
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")


# 9. Check discount eligibility
total_amount = 6000

if total_amount >= 5000:
    discount = total_amount * 10 / 100
    final_amount = total_amount - discount
    print("Discount:", discount)
    print("Final amount:", final_amount)
else:
    print("No discount")
    print("Final amount:", total_amount)


# 10. Nested if example
age = 22
has_id_card = True

if age >= 18:
    if has_id_card:
        print("Entry allowed")
    else:
        print("Entry denied: ID card required")
else:
    print("Entry denied: age must be 18 or above")
