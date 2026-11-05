"""Functions, lambda functions, recursion, and list transformations."""


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
    if number == 0:
        return 0
    return number + recursive_sum(number - 1)


def clean_positive_numbers(numbers):
    """Use list comprehension to keep only non-negative numbers."""
    return [number for number in numbers if number >= 0]
