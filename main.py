"""
Week 2: Data Structures and Functions
Menu-driven practice for lists, tuples, dictionaries, sets, functions,
lambda functions, recursion, list comprehension, and data cleaning.
"""

from data_structures import demonstrate_data_structures
from transformations import sum_of_squares, filter_even_numbers, recursive_sum
from data_cleaning import clean_records, sample_records


def main():
    while True:
        print("\n========== WEEK 2 PYTHON PROJECT ==========")
        print("1. Data structures demonstration")
        print("2. Sum of squares")
        print("3. Filter even numbers")
        print("4. Recursive sum")
        print("5. Client project: clean sample data")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            demonstrate_data_structures()
        elif choice == "2":
            values = [1, 2, 3, 4, 5]
            print("Numbers:", values)
            print("Sum of squares:", sum_of_squares(values))
        elif choice == "3":
            values = [1, 2, 3, 4, 5, 6, 7, 8]
            print("Numbers:", values)
            print("Even numbers:", filter_even_numbers(values))
        elif choice == "4":
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                print(f"Sum from 1 to {number}:", recursive_sum(number))
        elif choice == "5":
            cleaned = clean_records(sample_records())
            print("\nCleaned records:")
            for record in cleaned:
                print(record)
            print("Original record count:", len(sample_records()))
            print("Cleaned record count:", len(cleaned))
        elif choice == "6":
            print("Thank you for using the Week 2 project!")
            break
        else:
            print("Invalid choice. Select an option from 1 to 6.")


if __name__ == "__main__":
    main()
