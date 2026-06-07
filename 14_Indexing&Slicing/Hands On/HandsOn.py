"""Hands-on examples for indexing, slicing, and reverse indexing."""


def main():
    numbers = [10, 20, 30, 40, 50, 60, 70]
    text = "Python Programming"
    fruits = ("apple", "banana", "mango", "orange", "grapes")

    print("List:", numbers)
    print("String:", text)
    print("Tuple:", fruits)

    print("\n1. Positive Indexing")
    print("First number:", numbers[0])
    print("Third number:", numbers[2])
    print("First character:", text[0])
    print("Fourth fruit:", fruits[3])

    print("\n2. Reverse Indexing")
    print("Last number:", numbers[-1])
    print("Second last number:", numbers[-2])
    print("Last character:", text[-1])
    print("Last fruit:", fruits[-1])

    print("\n3. Basic Slicing")
    print("Numbers from index 1 to 4:", numbers[1:5])
    print("First 4 numbers:", numbers[:4])
    print("Numbers from index 3 to end:", numbers[3:])
    print("Text from index 0 to 5:", text[0:6])

    print("\n4. Slicing With Step")
    print("Every second number:", numbers[::2])
    print("Every third character:", text[::3])
    print("Fruits with step 2:", fruits[::2])

    print("\n5. Reverse Slicing")
    print("Reversed numbers:", numbers[::-1])
    print("Reversed text:", text[::-1])
    print("Reversed fruits:", fruits[::-1])

    print("\n6. Negative Index Slicing")
    print("Last 3 numbers:", numbers[-3:])
    print("Except last 2 numbers:", numbers[:-2])
    print("Middle text using negative index:", text[-11:-1])

    print("\n7. Updating List Using Index")
    numbers[1] = 200
    print("After changing index 1:", numbers)

    print("\n8. Updating List Using Slice")
    numbers[2:5] = [300, 400, 500]
    print("After slice update:", numbers)

    print("\n9. Copy List Using Slicing")
    copied_numbers = numbers[:]
    print("Copied list:", copied_numbers)


if __name__ == "__main__":
    main()
