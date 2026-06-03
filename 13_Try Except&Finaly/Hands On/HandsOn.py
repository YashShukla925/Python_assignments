"""Basic hands-on examples for try, except, else, and finally."""


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    else:
        print('division result:', result)
    finally:
        print('division attempt finished.')


def convert_to_int(value):
    try:
        number = int(value)
    except ValueError:
        print(f'{value!r} is not a valid integer.')
    else:
        print('converted number:', number)


def get_item(values, index):
    try:
        print('item:', values[index])
    except IndexError:
        print('Index is out of range.')


def main():
    divide_numbers(10, 2)
    divide_numbers(10, 0)

    convert_to_int('45')
    convert_to_int('python')

    get_item(['apple', 'banana', 'cherry'], 1)
    get_item(['apple', 'banana', 'cherry'], 5)

    try:
        file = open('sample.txt', 'r')
    except FileNotFoundError:
        print('sample.txt was not found.')
    finally:
        print('file example finished.')


if __name__ == '__main__':
    main()
