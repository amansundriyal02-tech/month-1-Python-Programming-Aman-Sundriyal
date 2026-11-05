# Week 1: Introduction to Python Programming

## Project Overview
This repository contains beginner-level Python programs for Week 1. It demonstrates Python fundamentals and a small client project that calculates the average temperature.

## Files
- `main.py` — Menu-driven program combining all Week 1 activities.
- `temperature_converter.py` — Converts Celsius into Fahrenheit.
- `calculator.py` — Performs addition, subtraction, multiplication, and division.
- `average_temperature.py` — Accepts multiple temperature readings and calculates their average.

## Concepts Learned
1. **Variables:** Store values such as temperature, numbers, and totals.
2. **Data types:** `int` for whole numbers, `float` for decimal values, and `str` for text.
3. **Operators:** Arithmetic operators such as `+`, `-`, `*`, and `/`, plus comparison operators.
4. **Input and output:** `input()` accepts user input and `print()` displays results.
5. **Conditional statements:** `if`, `elif`, and `else` make decisions based on conditions.
6. **For loop:** Repeats a task a fixed number of times, such as collecting temperature readings.
7. **While loop:** Repeats the menu until the user chooses Exit.
8. **Functions:** Organize the program into reusable sections.

## Client Project: Average Temperature
The program asks the user how many temperature readings they want to enter. It uses a `for` loop to collect each reading, adds them to a running total, and divides the total by the number of readings to calculate the average. It also checks that the number of readings is greater than zero.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the menu-driven program:

```bash
python main.py
```

You can also run each program separately:

```bash
python temperature_converter.py
python calculator.py
python average_temperature.py
```

## Sample Test
For average temperature, enter 3 readings: `25`, `27`, and `29`.

Expected average: `27.00°C`

## Requirements
- Python 3
- No external libraries required
