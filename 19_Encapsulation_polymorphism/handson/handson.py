"""
Hands-on examples for encapsulation and polymorphism in Python.
- protecting bank account data
- calculating payments in different ways
- sending delivery updates through different channels
- processing different employee salary types
"""


class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return f"XXXX-{str(self.__account_number)[-4:]}"

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def show_account_summary(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.get_account_number()}")
        print(f"Balance: {self.__balance}")


class PaymentMethod:
    def pay(self, amount):
        print(f"Paid {amount}.")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        processing_fee = amount * 0.02
        total_amount = amount + processing_fee
        print(f"Paid {total_amount} using credit card.")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


class CashOnDelivery(PaymentMethod):
    def pay(self, amount):
        print(f"Pay {amount} in cash when the order is delivered.")


class EmailUpdate:
    def send_update(self, customer, message):
        print(f"Email sent to {customer}: {message}")


class SMSUpdate:
    def send_update(self, customer, message):
        print(f"SMS sent to {customer}: {message}")


class WhatsAppUpdate:
    def send_update(self, customer, message):
        print(f"WhatsApp message sent to {customer}: {message}")


class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class Freelancer(Employee):
    def __init__(self, name, projects_completed, amount_per_project):
        super().__init__(name)
        self.projects_completed = projects_completed
        self.amount_per_project = amount_per_project

    def calculate_salary(self):
        return self.projects_completed * self.amount_per_project


def make_payment(payment_method, amount):
    payment_method.pay(amount)


def send_order_update(update_service, customer, message):
    update_service.send_update(customer, message)


def print_salary_slip(employee):
    print(f"{employee.name}'s salary: {employee.calculate_salary()}")


print("Example 1: Encapsulation in a bank account")
account1 = BankAccount("Aarav Sharma", 9876543210, 15000)
account1.show_account_summary()
account1.deposit(5000)
account1.withdraw(3000)
print(f"Available balance: {account1.get_balance()}")
print(f"Masked account number: {account1.get_account_number()}")

print("\nExample 2: Polymorphism in payment methods")
payment_methods = [
    CreditCardPayment(),
    UPIPayment(),
    CashOnDelivery(),
]

for payment_method in payment_methods:
    make_payment(payment_method, 2500)

print("\nExample 3: Polymorphism in order updates")
update_services = [
    EmailUpdate(),
    SMSUpdate(),
    WhatsAppUpdate(),
]

for service in update_services:
    send_order_update(service, "meera@example.com", "Your order is out for delivery.")

print("\nExample 4: Polymorphism in employee salary calculation")
employees = [
    FullTimeEmployee("Riya", 60000),
    PartTimeEmployee("Kabir", 80, 500),
    Freelancer("Ananya", 4, 12000),
]

for employee in employees:
    print_salary_slip(employee)

print("\nPractice Task:")
print("Create a class called ShoppingCart.")
print("Keep cart items private using __items.")
print("Add methods add_item(), remove_item(), and show_items().")
print("Create DiscountPayment and WalletPayment classes with a pay() method.")
print("Use one function checkout(payment_method, amount) to call pay() for both classes.")
