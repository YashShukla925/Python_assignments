# ==========================================
# 1. Basic Function
# ==========================================

def greet():
    print("Hello, Welcome!")


greet()

print("-" * 50)


# ==========================================
# 2. Functions are Objects
# ==========================================

def say_hello():
    print("Hello from say_hello")


another_variable = say_hello

another_variable()

print("-" * 50)


# ==========================================
# 3. Function Inside Function
# ==========================================

def outer_function():

    def inner_function():
        print("I am inner function")

    inner_function()


outer_function()

print("-" * 50)


# ==========================================
# 4. Returning a Function
# ==========================================

def outer():

    def inner():
        print("Returned function executed")

    return inner


returned_function = outer()

returned_function()

print("-" * 50)


# ==========================================
# 5. Manual Decorator
# ==========================================

def decorator_function(original_function):

    def wrapper():
        print("Before function execution")

        original_function()

        print("After function execution")

    return wrapper


def display():
    print("Display Function Running")


decorated_display = decorator_function(display)

decorated_display()

print("-" * 50)


# ==========================================
# 6. Actual Decorator Syntax (@)
# ==========================================

def my_decorator(func):

    def wrapper():
        print("Before execution")

        func()

        print("After execution")

    return wrapper


@my_decorator
def welcome():
    print("Welcome User")


welcome()

print("-" * 50)


# ==========================================
# 7. Decorator with Arguments
# ==========================================

def smart_decorator(func):

    def wrapper(name):
        print("Starting function")

        func(name)

        print("Function completed")

    return wrapper


@smart_decorator
def greet_user(name):
    print(f"Hello {name}")


greet_user("Rohan")

print("-" * 50)


# ==========================================
# 8. Decorator with Any Number of Arguments
# ==========================================

def universal_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before execution")

        result = func(*args, **kwargs)

        print("After execution")

        return result

    return wrapper


@universal_decorator
def add(a, b):
    return a + b


result = add(10, 20)

print("Result =", result)

print("-" * 50)



#  question
def multiply_by(n):

    def multiplier(x):
        return x * n

    return multiplier


double = multiply_by(2)
triple = multiply_by(3)

print(double(5))
print(triple(5))


