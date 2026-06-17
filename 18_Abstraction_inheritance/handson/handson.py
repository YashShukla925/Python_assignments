"""
Hands-on examples for abstraction and inheritance in Python.

These examples use real development-style situations:
- sending notifications
- processing payments
- building common user classes
- creating reusable API services
"""

from abc import ABC, abstractmethod


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.email} logged in successfully.")

    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


class AdminUser(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role

    def delete_user(self, username):
        print(f"{self.name} deleted user account: {username}")

    def show_profile(self):
        super().show_profile()
        print(f"Role: {self.role}")


class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

    def log_notification(self, recipient):
        print(f"Notification sent to {recipient}.")


class EmailNotification(NotificationService):
    def send(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")
        self.log_notification(recipient)


class SMSNotification(NotificationService):
    def send(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")
        self.log_notification(recipient)


class PushNotification(NotificationService):
    def send(self, recipient, message):
        print(f"Sending push notification to {recipient}: {message}")
        self.log_notification(recipient)


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def validate_amount(self, amount):
        return amount > 0


class StripePayment(PaymentGateway):
    def pay(self, amount):
        if self.validate_amount(amount):
            print(f"Paid {amount} using Stripe.")
        else:
            print("Invalid payment amount.")

    def refund(self, amount):
        if self.validate_amount(amount):
            print(f"Refunded {amount} using Stripe.")
        else:
            print("Invalid refund amount.")


class RazorpayPayment(PaymentGateway):
    def pay(self, amount):
        if self.validate_amount(amount):
            print(f"Paid {amount} using Razorpay.")
        else:
            print("Invalid payment amount.")

    def refund(self, amount):
        if self.validate_amount(amount):
            print(f"Refunded {amount} using Razorpay.")
        else:
            print("Invalid refund amount.")


class APIService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_url(self, endpoint):
        return f"{self.base_url}/{endpoint}"

    def request(self, endpoint):
        print(f"Request sent to: {self.get_url(endpoint)}")


class ProductService(APIService):
    def get_products(self):
        self.request("products")

    def get_product_by_id(self, product_id):
        self.request(f"products/{product_id}")


class OrderService(APIService):
    def get_orders(self):
        self.request("orders")

    def get_order_by_id(self, order_id):
        self.request(f"orders/{order_id}")


print("Example 1: Inheritance in user management")
admin1 = AdminUser("Meera", "meera@example.com", "Super Admin")
admin1.login()
admin1.show_profile()
admin1.delete_user("old_customer_101")

print("\nExample 2: Abstraction in notification services")
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
]

for notification in notifications:
    notification.send("aarav@example.com", "Your order has been shipped.")

print("\nExample 3: Abstraction in payment gateways")
stripe = StripePayment()
razorpay = RazorpayPayment()

stripe.pay(2500)
stripe.refund(500)
razorpay.pay(1200)
razorpay.refund(300)

print("\nExample 4: Inheritance in API services")
product_service = ProductService("https://api.shopapp.com")
order_service = OrderService("https://api.shopapp.com")

product_service.get_products()
product_service.get_product_by_id(15)
order_service.get_orders()
order_service.get_order_by_id(501)

print("\nPractice Task:")
print("Create an abstract class called DatabaseConnector.")
print("Add abstract methods connect() and disconnect().")
print("Create MySQLConnector and MongoDBConnector classes that implement both methods.")
print("Create objects of both classes and call connect() and disconnect().")
