from decimal import Decimal


print("14 May Assignment")


print("\nQ1. How we store string in Python?")
name = "Python"
print("String is stored as characters.")
print("Example:", name)
print("Type:", type(name))
print("First character:", name[0])


print("\nQ2. Explore None == None")
a = None
b = None
print("a =", a)
print("b =", b)
print("a == b:", a == b)
print("a is b:", a is b)


print("\nQ3. DocStrings")


def add(a, b):
    """This function adds two numbers."""
    return a + b


print("Answer:", add(5, 3))
print("Docstring:", add.__doc__)


print("\nQ4. Float vs Decimal")
float_answer = 0.1 + 0.2
decimal_answer = Decimal("0.1") + Decimal("0.2")
print("Float answer:", float_answer)
print("Decimal answer:", decimal_answer)
print("Float is not always exact for decimal values.")


print("\nQ5. List Tuple Dictionary")
my_list = ["apple", "banana", "mango"]
my_tuple = ("red", "green", "blue")
my_dictionary = {
    "name": "Yash",
    "subject": "Python",
    "marks": 90,
}

print("List:", my_list)
print("Tuple:", my_tuple)
print("Dictionary:", my_dictionary)

my_list.append("orange")
print("After adding item in list:", my_list)
print("Tuple first item:", my_tuple[0])
print("Dictionary name:", my_dictionary["name"])
