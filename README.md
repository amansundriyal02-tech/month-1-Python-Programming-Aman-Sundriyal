# Week 2: Data Structures and Functions

## Project Overview
This project practices Python data structures and functions. It also includes a small client project that cleans sample records by removing duplicates, excluding missing values, and filtering out records below a minimum age.

## Files
- `main.py` — Menu-driven program to run the Week 2 activities.
- `data_structures.py` — Examples of lists, tuples, dictionaries, sets, and list comprehension.
- `transformations.py` — Functions for sum of squares, filtering, lambda expressions, sorting, and recursion.
- `data_cleaning.py` — Client project for cleaning a list of records.
- `README.md` — Project and concept summary.

## Concepts Learned

1. **Lists:** Ordered, changeable collections. Example: `["apple", "banana"]`.
2. **Tuples:** Ordered collections that cannot be changed after creation. Example: `(10, 20)`.
3. **Dictionaries:** Store data as key-value pairs. Example: `{"name": "Aman", "week": 2}`.
4. **Sets:** Store unique values and automatically remove duplicates.
5. **Functions:** Reusable blocks of code defined with `def`.
6. **Lambda functions:** Small anonymous functions, useful for short operations such as `lambda x: x * 2`.
7. **Recursion:** A function calls itself and uses a base case to stop.
8. **List comprehension:** A concise way to create a list, optionally applying a condition.

## Hands-On Activities
- Calculate the sum of squares of a list of numbers.
- Filter even numbers using `filter()` and a lambda function.
- Sort words by length using a lambda function.
- Calculate a sum recursively.
- Use list comprehension to filter values.

## Client Project: Data Cleaning
The sample dataset contains duplicate records, missing names, missing ages, and people below the minimum age. The `clean_records()` function:
1. Uses a set to track IDs already processed.
2. Skips duplicate IDs.
3. Skips records with a missing name or age.
4. Keeps only records whose age is at least 18.
5. Returns a new cleaned list without modifying the original records.

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run:

```bash
python main.py
```

To run only the client project:

```bash
python data_cleaning.py
```

## Expected Client Project Output
The sample data contains 7 records. After cleaning, 3 valid unique adult records remain: Asha, Rahul, and Vikas.

## Requirements
- Python 3
- No external libraries required
