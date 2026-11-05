# Month 1 – Python Programming

A collection of beginner-friendly Python exercises and mini-projects covering core Python, data structures, NumPy, Pandas, data cleaning, and data visualization.

## Repository contents

| File | Purpose |
|---|---|
| `average_temperature.py` | Calculates the average of multiple temperature readings |
| `calculator.py` | Performs addition, subtraction, multiplication, and division |
| `temperature_converter.py` | Converts Celsius to Fahrenheit and Fahrenheit to Celsius |
| `data_structures.py` | Demonstrates lists, tuples, dictionaries, sets, and list comprehensions |
| `transformations.py` | Demonstrates functions, lambda, filter, sorting, recursion, and comprehensions |
| `data_cleaning.py` | Removes duplicate and invalid student records |
| `numpy_operations.py` | Demonstrates arrays, arithmetic, statistics, and broadcasting |
| `pandas_operations.py` | Demonstrates Series, DataFrames, selection, filtering, and grouping |
| `client_project.py` | Cleans temperature data and calculates city-wise averages |
| `dashboard.py` | Generates plots and a student-performance dashboard |
| `main.py` | Interactive menu for the NumPy/Pandas activities |
| `test_projects.py` | Automated unit and data-project tests |
| `sample_data.csv` | Sample temperature dataset for cleaning |
| `student_performance.csv` | Sample student dataset for visualization |

## Requirements

- Python 3.9 or newer
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Setup

Clone or download this repository, then open a terminal in the project folder.

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the programs

Run the Week 3 interactive NumPy/Pandas menu:

```bash
python main.py
```

Run individual exercises:

```bash
python calculator.py
python average_temperature.py
python temperature_converter.py
python data_cleaning.py
python transformations.py
```

Run the data projects:

```bash
python client_project.py
python dashboard.py
```

The temperature cleaning project creates `cleaned_temperature_data.csv`. The dashboard creates image files inside the `plots/` directory.

## Run automated tests

Run the tests from the repository root:

```bash
python -m unittest discover -v
```

The tests cover calculator operations and errors, temperature conversions, data cleaning, transformations, the temperature aggregation results, and dashboard plot generation.

## Learning outcomes

- Use variables, input, conditions, loops, and functions.
- Work with common Python data structures.
- Apply lambda functions, filtering, sorting, and recursion.
- Create and manipulate NumPy arrays.
- Analyze tabular data with Pandas.
- Handle missing, invalid, and duplicate data.
- Create data visualizations with Matplotlib and Seaborn.
- Write and run automated tests.

## Notes

- Run commands from the repository root so the sample CSV files are found.
- Do not commit virtual environments, cache files, or generated output files.
- The sample datasets are small learning examples, not real-world statistical samples.
