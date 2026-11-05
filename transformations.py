"""Examples of functions, lambdas, recursion, and list transformations."""


def sum_of_squares(numbers):
    """Return the sum of the square of each number."""
    return sum(number ** 2 for number in numbers)


def filter_even_numbers(numbers):
    """Return only even numbers using filter() and a lambda function."""
    return list(filter(lambda number: number % 2 == 0, numbers))


def sort_words_by_length(words):
    """Sort words from shortest to longest using a lambda function."""
    return sorted(words, key=lambda word: len(word))


def recursive_sum(number):
    """Return 1 + 2 + ... + number using recursion."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 0:
        raise ValueError("number must be non-negative")
    if number > 900:
        raise ValueError("number is too large for this recursive example")
    if number == 0:
        return 0
    return number + recursive_sum(number - 1)


def clean_positive_numbers(numbers):
    """Keep non-negative numeric values, excluding booleans."""
    return [
        number for number in numbers
        if isinstance(number, (int, float)) and not isinstance(number, bool) and number >= 0
    ]


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    print("Sum of squares:", sum_of_squares(values))
    print("Even numbers:", filter_even_numbers(values))
    print("Words by length:", sort_words_by_length(["python", "is", "fun"]))
    print("Recursive sum (5):", recursive_sum(5))
    print("Non-negative values:", clean_positive_numbers([-2, 0, 3, 5]))
