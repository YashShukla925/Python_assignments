"""Hands-on practice for Python set basic operations."""


def show(title, value):
    """Print a labelled output block."""
    print(f"\n{title}")
    print("-" * len(title))
    print(value)


def set_basics():
    fruits = {"apple", "banana", "cherry", "apple"}

    show("Original set", fruits)
    show("Set length", len(fruits))
    show("Check banana in set", "banana" in fruits)

    fruits.add("mango")
    show("After add()", fruits)

    fruits.update(["orange", "grapes"])
    show("After update()", fruits)

    fruits.remove("banana")
    show("After remove()", fruits)

    fruits.discard("pineapple")
    show("After discard() with missing item", fruits)


def set_operations():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    show("Set A", a)
    show("Set B", b)
    show("Union", a.union(b))
    show("Intersection", a.intersection(b))
    show("Difference A - B", a.difference(b))
    show("Difference B - A", b.difference(a))
    show("Symmetric difference", a.symmetric_difference(b))


def set_relationships():
    students = {"Yash", "Aarav", "Isha", "Kabir"}
    python_students = {"Yash", "Isha"}

    show("All students", students)
    show("Python students", python_students)
    show("Is subset", python_students.issubset(students))
    show("Is superset", students.issuperset(python_students))


def main():
    set_basics()
    set_operations()
    set_relationships()


if __name__ == "__main__":
    main()
