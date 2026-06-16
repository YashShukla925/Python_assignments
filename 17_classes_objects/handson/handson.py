"""
Basic hands-on examples for Python classes and objects.

Run this file and read the output from top to bottom.
"""


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I am {self.name}. I am {self.age} years old.")
        print(f"I am learning {self.course}.")

    def change_course(self, new_course):
        self.course = new_course
        print(f"{self.name}'s course changed to {self.course}.")


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"{self.account_holder}'s balance is {self.balance}.")


class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def details(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")
        print(f"Wheels: {Car.wheels}")


print("Example 1: Student class")
student1 = Student("Aarav", 20, "Python")
student2 = Student("Meera", 21, "Java")

student1.introduce()
student2.introduce()
student2.change_course("Data Science")

print("\nExample 2: BankAccount class")
account1 = BankAccount("Riya", 1000)
account1.show_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)

print("\nExample 3: Car class")
car1 = Car("Toyota", "Innova", 2022)
car2 = Car("Hyundai", "i20", 2023)

car1.details()
car1.start()
car2.details()

print("\nPractice Task:")
print("Create a class called Book with title, author, and price.")
print("Add a method called show_details() to print book information.")
