"""Automated tests for the Month 1 Python programming exercises."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import pandas as pd

from average_temperature import main as average_temperature_main
from calculator import calculate
from client_project import clean_temperature_data
from data_cleaning import clean_records, sample_records
from dashboard import create_dashboard
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius
from transformations import (
    clean_positive_numbers,
    filter_even_numbers,
    recursive_sum,
    sort_words_by_length,
    sum_of_squares,
)


ROOT = Path(__file__).resolve().parent


class CalculatorTests(unittest.TestCase):
    def test_all_operations(self):
        self.assertEqual(calculate(8, "+", 2), 10)
        self.assertEqual(calculate(8, "-", 2), 6)
        self.assertEqual(calculate(8, "*", 2), 16)
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_invalid_operator_and_zero_division(self):
        with self.assertRaises(ValueError):
            calculate(1, "%", 1)
        with self.assertRaises(ZeroDivisionError):
            calculate(1, "/", 0)


class UtilityTests(unittest.TestCase):
    def test_temperature_conversions(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

    def test_average_temperature_cli(self):
        output = StringIO()
        with patch("builtins.input", side_effect=["3", "10", "20", "30"]):
            with redirect_stdout(output):
                average_temperature_main()
        self.assertIn("20.00", output.getvalue())

    def test_data_cleaning(self):
        cleaned = clean_records(sample_records())
        self.assertEqual(len(cleaned), 3)
        self.assertEqual({row["name"] for row in cleaned}, {"Asha", "Rahul", "Vikas"})

    def test_transformations(self):
        self.assertEqual(sum_of_squares([1, 2, 3]), 14)
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(sort_words_by_length(["python", "is", "fun"]), ["is", "fun", "python"])
        self.assertEqual(recursive_sum(5), 15)
        self.assertEqual(clean_positive_numbers([-2, 0, 3]), [0, 3])

    def test_recursive_sum_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            recursive_sum(-1)
        with self.assertRaises(TypeError):
            recursive_sum(2.5)


class DataProjectTests(unittest.TestCase):
    def test_temperature_dataset_cleaning(self):
        source = pd.read_csv(ROOT / "sample_data.csv")
        cleaned, averages = clean_temperature_data(source)
        self.assertEqual(len(cleaned), 6)
        actual = dict(zip(averages["City"], averages["Average_Temperature"]))
        self.assertEqual(actual, {"Delhi": 33.0, "Jaipur": 34.0, "Mumbai": 29.0})

    def test_temperature_dataset_requires_columns(self):
        with self.assertRaises(ValueError):
            clean_temperature_data(pd.DataFrame({"Place": ["Delhi"]}))

    def test_dashboard_generates_all_plots(self):
        with TemporaryDirectory() as temporary_directory:
            temporary = Path(temporary_directory)
            source = pd.read_csv(ROOT / "student_performance.csv")
            csv_path = temporary / "student_performance.csv"
            source.to_csv(csv_path, index=False)
            plots_path = temporary / "plots"

            with patch("dashboard.DATA_FILE", csv_path), patch("dashboard.PLOTS", plots_path):
                create_dashboard()

            expected = {
                "histogram_final_scores.png",
                "scatter_study_hours_vs_score.png",
                "correlation_heatmap.png",
                "pairplot_student_performance.png",
                "student_performance_dashboard.png",
            }
            self.assertEqual({path.name for path in plots_path.iterdir()}, expected)


if __name__ == "__main__":
    unittest.main()
