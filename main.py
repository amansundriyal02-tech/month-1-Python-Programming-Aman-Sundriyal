"""Week 3: NumPy and Pandas for Data Manipulation."""

from numpy_operations import demonstrate_numpy
from pandas_operations import demonstrate_pandas
from client_project import run_data_cleaning_project


def main():
    while True:
        print("\n========== WEEK 3: NUMPY AND PANDAS ==========")
        print("1. NumPy arrays and operations")
        print("2. Pandas Series, DataFrames, indexing and grouping")
        print("3. Client project: clean and aggregate dataset")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            demonstrate_numpy()
        elif choice == "2":
            demonstrate_pandas()
        elif choice == "3":
            run_data_cleaning_project()
        elif choice == "4":
            print("Thank you for using the Week 3 project!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
