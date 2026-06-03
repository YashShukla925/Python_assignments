"""Basic hands-on examples for built-in Python functions."""


def main():
    numbers = [5, 2, 9, 1, 7]
    words = ['python', 'is', 'fun']

    print('length:', len(numbers))
    print('sum:', sum(numbers))
    print('minimum:', min(numbers))
    print('maximum:', max(numbers))
    print('sorted:', sorted(numbers))
    print('reversed:', list(reversed(numbers)))

    print('all positive:', all(num > 0 for num in numbers))
    print('any even:', any(num % 2 == 0 for num in numbers))

    print('enumerate:')
    for index, word in enumerate(words, start=1):
        print(index, word)

    print('zip:')
    for word, number in zip(words, numbers):
        print(word, number)

    print('map squares:', list(map(lambda num: num * num, numbers)))
    print('filter odd:', list(filter(lambda num: num % 2 != 0, numbers)))

    value = '25'
    print('int:', int(value))
    print('float:', float(value))
    print('type:', type(value))
    print('round:', round(12.567, 2))


if __name__ == '__main__':
    main()
