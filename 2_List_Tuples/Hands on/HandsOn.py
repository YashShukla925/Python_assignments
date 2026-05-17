"""Hands-on practice for Python lists, tuples, and nested lists.

Run this file to see examples for common list and tuple operations covered in
the W3Schools list/tuple sections.
"""


def show(title, value):
    """Print a labelled output block."""
    print(f"\n{title}")
    print("-" * len(title))
    print(value)


def list_basics():
    fruits = ["apple", "banana", "cherry", "mango"]

    show("Original list", fruits)
    show("First item", fruits[0])
    show("Last item using negative index", fruits[-1])
    show("Slice from index 1 to 3", fruits[1:3])

    fruits[1] = "blackcurrant"
    show("After changing index 1", fruits)

    fruits[1:3] = ["kiwi", "orange"]
    show("After changing a range", fruits)

    fruits.insert(2, "watermelon")
    show("After insert()", fruits)

    fruits.append("grapes")
    show("After append()", fruits)

    tropical = ["pineapple", "papaya"]
    fruits.extend(tropical)
    show("After extend()", fruits)

    fruits.remove("apple")
    show("After remove()", fruits)

    popped_item = fruits.pop(2)
    show("Item removed using pop(2)", popped_item)
    show("List after pop(2)", fruits)

    del fruits[0]
    show("After del fruits[0]", fruits)

    copied_fruits = fruits.copy()
    show("Copied list using copy()", copied_fruits)

    fruits.clear()
    show("After clear()", fruits)


def list_methods():
    numbers = [4, 2, 9, 2, 7, 1, 2]

    show("Numbers", numbers)
    show("count(2)", numbers.count(2))
    show("index(9)", numbers.index(9))

    numbers.sort()
    show("After sort()", numbers)

    numbers.sort(reverse=True)
    show("After sort(reverse=True)", numbers)

    numbers.reverse()
    show("After reverse()", numbers)

    squares = [number * number for number in numbers]
    show("Squares using list comprehension", squares)


def tuple_basics():
    coordinates = (28.6139, 77.2090)
    colors = ("red", "green", "blue", "green")
    single_item_tuple = ("python",)

    show("Coordinates tuple", coordinates)
    show("Tuple item by index", colors[1])
    show("Tuple slice", colors[1:3])
    show("Single item tuple", single_item_tuple)
    show("count('green')", colors.count("green"))
    show("index('blue')", colors.index("blue"))

    red, green, blue, repeated_green = colors
    show("Tuple unpacking", f"{red}, {green}, {blue}, {repeated_green}")

    editable_colors = list(colors)
    editable_colors.append("yellow")
    updated_colors = tuple(editable_colors)
    show("Tuple changed by converting to list and back", updated_colors)


def nested_lists():
    students = [
        ["Aarav", 86, 91, 78],
        ["Isha", 92, 88, 95],
        ["Kabir", 75, 84, 80],
    ]

    show("Nested student list", students)
    show("Second student's name", students[1][0])
    show("Kabir's science marks", students[2][2])

    students[0][3] = 82
    show("After updating Aarav's marks", students)

    averages = []
    for student in students:
        name = student[0]
        marks = student[1:]
        average = sum(marks) / len(marks)
        averages.append([name, round(average, 2)])

    show("Student averages", averages)


def list_tuple_conversion():
    weekdays = ("Monday", "Tuesday", "Wednesday")
    weekdays_list = list(weekdays)
    weekdays_list.append("Thursday")
    weekdays = tuple(weekdays_list)

    show("Tuple converted to list, updated, and converted back", weekdays)

    mixed_records = [
        ("Laptop", 55000),
        ("Mouse", 700),
        ("Keyboard", 1400),
    ]
    show("List of tuples", mixed_records)
    show("Total bill", sum(price for _, price in mixed_records))


def main():
    list_basics()
    list_methods()
    tuple_basics()
    nested_lists()
    list_tuple_conversion()


if __name__ == "__main__":
    main()
