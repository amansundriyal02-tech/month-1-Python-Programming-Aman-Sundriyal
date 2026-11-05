"""Practice Pandas Series, DataFrames, indexing, and grouping."""

import pandas as pd


def demonstrate_pandas():
    # Series: one-dimensional labelled data
    marks = pd.Series([78, 85, 92], index=["Asha", "Rahul", "Neha"])
    print("\nPANDAS SERIES:")
    print(marks)

    # DataFrame: two-dimensional tabular data
    data = {
        "Name": ["Asha", "Rahul", "Neha", "Vikas"],
        "Department": ["CSE", "IT", "CSE", "IT"],
        "Marks": [78, 85, 92, 74],
    }
    df = pd.DataFrame(data)

    print("\nDATAFRAME:")
    print(df)

    # Indexing and selecting columns/rows
    print("\nMarks column:")
    print(df["Marks"])
    print("\nFirst two rows:")
    print(df.iloc[0:2])
    print("\nStudents with marks >= 80:")
    print(df.loc[df["Marks"] >= 80])

    # Grouping and aggregation
    print("\nAverage marks by department:")
    print(df.groupby("Department")["Marks"].mean())
