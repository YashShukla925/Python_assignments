"""
Hands-on exercises for Functions & Methods
"""

def basic_functions():
    def greet(name, greeting='Hello'):
        """Return a greeting message for a given name."""
        return f"{greeting}, {name}!"

    print(greet('Alice'))
    print(greet('Bob', greeting='Hi'))
    print(greet(name='Charlie', greeting='Welcome'))

    def describe(name, age, *, city='Unknown'):
        """Show a description using keyword-only arguments."""
        return f"{name} is {age} years old and lives in {city}."

    print(describe('Dana', 27, city='Paris'))

    def show_args(*args, **kwargs):
        print('args:', args)
        print('kwargs:', kwargs)

    show_args('apple', 'banana', color='red', count=2)


def function_return_values():
    def multiply(a, b=1):
        return a * b

    result = multiply(5, 3)
    print('multiply(5, 3) =', result)

    def split_sentence(sentence):
        return sentence.split(), len(sentence)

    words, length = split_sentence('Hello world')
    print('words:', words)
    print('length:', length)


def common_methods():
    text = 'python functions'
    print('upper:', text.upper())
    print('title:', text.title())
    print('contains "func"?', 'func' in text)

    numbers = [3, 1, 4]
    numbers.append(2)
    print('after append:', numbers)
    numbers.sort()
    print('after sort:', numbers)
    print('pop returns:', numbers.pop())
    print('remaining list:', numbers)

    data = {'name': 'Ava', 'age': 25}
    print('keys:', list(data.keys()))
    print('age:', data.get('age'))
    print('city default:', data.get('city', 'Unknown'))


def recursion_example(n):
    if n <= 1:
        return 1
    return n * recursion_example(n - 1)


def exercises():
    print('\nExercise 1: create a function that returns unique items from a list')
    def unique_items(values):
        return list(dict.fromkeys(values))

    print(unique_items([1, 2, 2, 3, 4, 4, 5]))

    print('\nExercise 2: write a function using both positional and keyword-only args')
    def order(item, quantity, *, urgent=False):
        return f"Order: {quantity} x {item}. Urgent={urgent}"

    print(order('pen', 10, urgent=True))
    print(order('notebook', 3))

    print('\nExercise 3: compare iterative and recursive factorial implementations')
    def factorial_iterative(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    print('iterative factorial(5):', factorial_iterative(5))
    print('recursive factorial(5):', recursion_example(5))


if __name__ == '__main__':
    print('--- Function Basics ---')
    basic_functions()
    print('\n--- Function Return Values ---')
    function_return_values()
    print('\n--- Common Object Methods ---')
    common_methods()
    print('\n--- Exercises ---')
    exercises()
