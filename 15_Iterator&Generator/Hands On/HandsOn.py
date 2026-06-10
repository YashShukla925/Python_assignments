"""Hands-on examples for iterators and generators."""


def square_generator(limit):
    for number in range(1, limit + 1):
        yield number * number


def even_number_generator(limit):
    for number in range(2, limit + 1, 2):
        yield number


def fibonacci_generator(count):
    first, second = 0, 1

    for _ in range(count):
        yield first
        first, second = second, first + second


def main():
    fruits = ["apple", "banana", "mango", "orange"]
    numbers = [10, 20, 30, 40, 50]

    print("1. Using iter() and next()")
    fruit_iterator = iter(fruits)
    print(next(fruit_iterator))
    print(next(fruit_iterator))
    print(next(fruit_iterator))

    print("\n2. Iterating Through a List")
    for fruit in fruits:
        print(fruit)

    print("\n3. Using Iterator With Numbers")
    number_iterator = iter(numbers)
    print(next(number_iterator))
    print(next(number_iterator))
    print(next(number_iterator))

    print("\n4. Looping Through an Iterator")
    for number in iter(numbers):
        print(number)

    print("\n5. Generator Function With yield")
    for square in square_generator(5):
        print(square)

    print("\n6. Even Number Generator")
    for even_number in even_number_generator(10):
        print(even_number)

    print("\n7. Fibonacci Generator")
    for fibonacci_number in fibonacci_generator(8):
        print(fibonacci_number)

    print("\n8. Generator Expression")
    cubes = (number ** 3 for number in range(1, 6))
    for cube in cubes:
        print(cube)


if __name__ == "__main__":
    main()
