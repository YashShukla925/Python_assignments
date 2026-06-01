"""
Hands-on exercises for List and Dict Comprehensions
"""

def examples():
    # List comprehension examples
    nums = list(range(10))
    squares = [x*x for x in nums]
    evens = [x for x in nums if x % 2 == 0]

    # Nested comprehension (flatten)
    matrix = [[i + j*3 for i in range(3)] for j in range(3)]
    flat = [n for row in matrix for n in row]

    # Dict comprehension examples
    names = ["alice", "bob", "carol"]
    upper_map = {n: n.upper() for n in names}
    squares_map = {x: x*x for x in range(6)}

    print("nums:", nums)
    print("squares:", squares[:10])
    print("evens:", evens)
    print("matrix:", matrix)
    print("flat:", flat)
    print("upper_map:", upper_map)
    print("squares_map:", squares_map)


def exercises():
    # TODO 1: create a list of cubes for numbers 0..9 using comprehension
    # TODO 2: build a dict mapping each word in a sentence to its length
    # TODO 3: given a list of pairs, use comprehension to swap each pair

    sentence = "list and dict comprehensions are concise"
    words = sentence.split()

    cubes = [x**3 for x in range(10)]
    word_len = {w: len(w) for w in words}
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    swapped = [(b, a) for a, b in pairs]

    print("cubes:", cubes)
    print("word_len:", word_len)
    print("swapped:", swapped)


if __name__ == '__main__':
    print('--- List & Dict Comprehension Examples ---')
    examples()
    print('\n--- Exercises (solutions shown) ---')
    exercises()
