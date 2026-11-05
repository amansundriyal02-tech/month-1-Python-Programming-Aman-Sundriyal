"""Clean temperature records and calculate average temperature by city."""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).with_name("sample_data.csv")
OUTPUT_FILE = Path(__file__).with_name("cleaned_temperature_data.csv")
REQUIRED_COLUMNS = {"City", "Temperature"}


def clean_temperature_data(dataframe):
    """Return cleaned records and average temperature by city."""
    missing = REQUIRED_COLUMNS.difference(dataframe.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(sorted(missing))}")

    cleaned = dataframe.copy()
    cleaned["City"] = cleaned["City"].astype("string").str.strip()
    cleaned["Temperature"] = pd.to_numeric(cleaned["Temperature"], errors="coerce")
    cleaned = cleaned.dropna(subset=["City", "Temperature"])
    cleaned = cleaned[cleaned["City"] != ""]
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    averages = (
        cleaned.groupby("City", as_index=False)["Temperature"]
        .mean()
        .rename(columns={"Temperature": "Average_Temperature"})
    )
    return cleaned, averages


def run_data_cleaning_project():
    if not DATA_FILE.exists():
        print(f"Dataset not found: {DATA_FILE}")
        return

    try:
        original = pd.read_csv(DATA_FILE)
        cleaned, averages = clean_temperature_data(original)
    except (OSError, pd.errors.ParserError, ValueError) as error:
        print(f"Could not process dataset: {error}")
        return

    cleaned.to_csv(OUTPUT_FILE, index=False)
    print("\nORIGINAL DATA:")
    print(original)
    print("\nCLEANED DATA:")
    print(cleaned)
    print("\nAVERAGE TEMPERATURE BY CITY:")
    print(averages)
    print(f"\nRows before cleaning: {len(original)}")
    print(f"Rows after cleaning: {len(cleaned)}")
    print(f"Cleaned dataset saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    run_data_cleaning_project()
