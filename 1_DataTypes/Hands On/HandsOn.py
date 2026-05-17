"""Short hands-on practice for Python data types."""


print("What to learn in Python data types")
print("-" * 35)

print("1. Basic types: str, int, float, bool, None")
print("2. Check type using type()")
print("3. Convert values using int(), float(), str(), bool()")
print("4. Know mutable vs immutable types")
print("5. Use list, tuple, dict, and set for collections")


name = "Yash"
age = 20
height = 5.8
is_learning = True
empty_value = None

print("\nExamples")
print("name:", name, type(name))
print("age:", age, type(age))
print("height:", height, type(height))
print("is_learning:", is_learning, type(is_learning))
print("empty_value:", empty_value, type(empty_value))


number_text = "100"
number = int(number_text)

print("\nType conversion")
print("Before:", number_text, type(number_text))
print("After:", number, type(number))
