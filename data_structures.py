"""Examples of Python lists, tuples, dictionaries, and sets."""


def demonstrate_data_structures():
    # List: ordered and changeable collection
    fruits = ["apple", "banana", "mango"]
    fruits.append("orange")
    print("\nLIST:", fruits)

    # Tuple: ordered and immutable collection
    coordinates = (28.6, 77.2)
    print("TUPLE:", coordinates)

    # Dictionary: key-value pairs
    student = {"name": "Aman", "week": 2, "status": "Learning"}
    student["status"] = "Completed"
    print("DICTIONARY:", student)

    # Set: stores unique values
    numbers = {1, 2, 2, 3, 3, 4}
    print("SET (duplicates removed):", numbers)

    # List comprehension
    squares = [number ** 2 for number in range(1, 6)]
    print("LIST COMPREHENSION (squares):", squares)
