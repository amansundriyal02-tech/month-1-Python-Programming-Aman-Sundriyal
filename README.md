# Week 3: NumPy and Pandas for Data Manipulation

## Project Overview
This project practices NumPy arrays and operations, broadcasting, and Pandas Series, DataFrames, indexing, and grouping. The client project cleans a sample temperature dataset and calculates average temperature by city.

## Files
- `main.py` — Menu to run the Week 3 activities.
- `numpy_operations.py` — NumPy array creation, arithmetic, statistics, 2D arrays, and broadcasting.
- `pandas_operations.py` — Series, DataFrames, indexing, filtering, and grouping.
- `client_project.py` — Removes duplicate and incomplete records, then calculates average temperature by city.
- `sample_data.csv` — Sample temperature dataset containing duplicate and missing values for cleaning practice.
- `requirements.txt` — Required Python libraries.
- `README.md` — Summary of concepts and instructions.

## Concepts Learned

1. **NumPy arrays:** NumPy arrays store numerical data efficiently and support operations on whole arrays.
2. **Array operations:** Arithmetic operations such as addition, multiplication, and exponentiation can be applied element-wise.
3. **Broadcasting:** NumPy can apply an operation between arrays or between an array and a compatible single value/shape.
4. **Pandas Series:** A one-dimensional labelled data structure.
5. **Pandas DataFrame:** A two-dimensional table with rows and columns.
6. **Indexing:** Select columns and rows using column names, `.loc`, and `.iloc`.
7. **Data grouping:** `groupby()` groups rows by a category and allows calculations such as mean.

## Hands-On Activities
- Create NumPy one-dimensional and two-dimensional arrays.
- Perform arithmetic and statistical operations.
- Demonstrate broadcasting by adding a number to every matrix element.
- Create a Pandas Series and DataFrame.
- Select columns and rows, filter values, and calculate group averages.

## Client Project: Clean and Aggregate Temperature Data
The sample CSV includes duplicate records and missing city/temperature values. The project:
1. Reads the CSV file with Pandas.
2. Removes duplicate rows using `drop_duplicates()`.
3. Removes rows with missing required values using `dropna()`.
4. Converts temperature values to numeric data.
5. Trims extra spaces from city names.
6. Groups the cleaned data by city and calculates average temperature.
7. Saves the cleaned records to `cleaned_temperature_data.csv`.

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the menu:

```bash
python main.py
```

To run only the client project:

```bash
python client_project.py
```

## Expected Client Project Result
After cleaning the provided sample dataset, 6 valid unique records remain. Average temperatures are calculated separately for Delhi, Jaipur, and Mumbai. The exact results are printed when the script runs.

## Requirements
- Python 3
- NumPy
- Pandas
