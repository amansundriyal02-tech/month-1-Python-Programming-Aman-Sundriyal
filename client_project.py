"""
Client Project: Clean and aggregate a dataset with Pandas.
The script removes rows with missing required values, removes duplicate
records, and calculates average temperature by city.
"""

from pathlib import Path
import pandas as pd


DATA_FILE = Path(__file__).with_name("sample_data.csv")
OUTPUT_FILE = Path(__file__).with_name("cleaned_temperature_data.csv")


def run_data_cleaning_project():
    if not DATA_FILE.exists():
        print(f"Dataset not found: {DATA_FILE}")
        return

    df = pd.read_csv(DATA_FILE)

    print("\nORIGINAL DATA:")
    print(df)
    print("\nOriginal row count:", len(df))

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Remove rows where city or temperature is missing
    df = df.dropna(subset=["City", "Temperature"])

    # Ensure temperature is numeric; invalid values become missing
    df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
    df = df.dropna(subset=["Temperature"])

    # Remove leading/trailing spaces from city names
    df["City"] = df["City"].astype(str).str.strip()

    # Remove rows with an empty city after trimming
    df = df[df["City"] != ""]

    # Aggregate: calculate average temperature for each city
    average_by_city = (
        df.groupby("City", as_index=False)["Temperature"]
        .mean()
        .rename(columns={"Temperature": "Average_Temperature"})
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nCLEANED DATA:")
    print(df)
    print("\nAverage temperature by city:")
    print(average_by_city)
    print("\nCleaned row count:", len(df))
    print(f"Cleaned dataset saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    run_data_cleaning_project()
