"""Assignments for Python lists, tuples, and nested lists.

Each task is implemented as a function so it can be tested or reused later.
Run this file to see sample outputs.
"""


def remove_duplicates(items):
    """Return a new list with duplicate values removed while keeping order."""
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


def second_largest(numbers):
    """Return the second largest unique number from a list."""
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]


def swap_first_last(items):
    """Swap the first and last item of a list."""
    if len(items) < 2:
        return items.copy()

    swapped_items = items.copy()
    swapped_items[0], swapped_items[-1] = swapped_items[-1], swapped_items[0]
    return swapped_items


def flatten_nested_list(nested_items):
    """Convert a nested list into a single list."""
    flattened_items = []
    for row in nested_items:
        flattened_items.extend(row)
    return flattened_items


def calculate_student_averages(students):
    """Return each student's average from a nested student marks list."""
    averages = []
    for student in students:
        name = student[0]
        marks = student[1:]
        average = sum(marks) / len(marks)
        averages.append((name, round(average, 2)))
    return averages


def tuple_summary(values):
    """Return count, minimum, maximum, and total for a tuple of numbers."""
    return {
        "count": len(values),
        "minimum": min(values),
        "maximum": max(values),
        "total": sum(values),
    }


def update_tuple_item(values, index, new_value):
    """Update a tuple item by converting it into a list first."""
    editable_values = list(values)
    editable_values[index] = new_value
    return tuple(editable_values)


def filter_even_numbers(numbers):
    """Return even numbers from a list using list comprehension."""
    return [number for number in numbers if number % 2 == 0]


def run_assignments():
    numbers = [10, 20, 10, 40, 30, 20, 50]
    names = ["Asha", "Ravi", "Meera", "Kabir"]
    marks = [
        ["Asha", 85, 90, 88],
        ["Ravi", 78, 82, 80],
        ["Meera", 95, 92, 96],
    ]
    nested_numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]
    tuple_numbers = (12, 45, 23, 45, 9)

    print("1. Remove duplicates:", remove_duplicates(numbers))
    print("2. Second largest number:", second_largest(numbers))
    print("3. Swap first and last name:", swap_first_last(names))
    print("4. Flatten nested list:", flatten_nested_list(nested_numbers))
    print("5. Student averages:", calculate_student_averages(marks))
    print("6. Tuple summary:", tuple_summary(tuple_numbers))
    print("7. Updated tuple:", update_tuple_item(tuple_numbers, 2, 99))
    print("8. Even numbers:", filter_even_numbers(numbers))


if __name__ == "__main__":
    run_assignments()
