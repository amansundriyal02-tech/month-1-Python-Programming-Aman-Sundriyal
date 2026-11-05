"""Interactive menu for the Week 3 NumPy and Pandas activities."""

from numpy_operations import demonstrate_numpy
from pandas_operations import demonstrate_pandas
from client_project import run_data_cleaning_project


def main():
    actions = {
        "1": demonstrate_numpy,
        "2": demonstrate_pandas,
        "3": run_data_cleaning_project,
    }
    while True:
        print("\n========== WEEK 3: NUMPY AND PANDAS ==========")
        print("1. NumPy arrays and operations")
        print("2. Pandas Series, DataFrames, indexing and grouping")
        print("3. Client project: clean and aggregate dataset")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "4":
            print("Thank you for using the Week 3 project!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue
        try:
            action()
        except (ValueError, OSError) as error:
            print(f"Could not complete that activity: {error}")


if __name__ == "__main__":
    main()
