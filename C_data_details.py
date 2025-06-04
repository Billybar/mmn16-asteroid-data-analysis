import os
import numpy as np
import pandas as pd
from datetime import datetime

def data_details(df):
    if "Orbiting Body" in df:
        df.drop('Orbiting Body', axis = 1)

    if "Equinox" in df:
        df.drop('Equinox', axis = 1)

    if "Neo Reference ID" in df:
        df.drop('Neo Reference ID', axis = 1)

    num_rows , num_cols = df.shape
    column_titles = list(df.columns)

    data = (num_rows, num_cols, column_titles)
    return data


def test_data_details():
    # Create a sample DataFrame with columns to be dropped and kept
    test_data = {
        'Neo Reference ID': [1, 2, 3, 4],
        'Name': [100, 200, 300, 400],
        'Orbiting Body': ['Earth', 'Mars', 'Earth', 'Venus'],
        'Equinox': ['J2000', 'J2000', 'J2000', 'J2000'],
        'Hazardous': [True, False, True, False],
        'Close Approach Date': ['2020-01-01', '2021-02-02', '2022-03-03', '2023-04-04']
    }

    df = pd.DataFrame(test_data)
    print("Original DataFrame:")
    print(df)
    print(f"Original shape: {df.shape}")
    print(f"Original columns: {list(df.columns)}")
    print("\n")

    # Test the data_details function
    result = data_details(df)
    print("Function result:")
    print(f"Returned tuple: {result}")
    print(f"Number of rows: {result[0]}")
    print(f"Number of columns: {result[1]}")
    print(f"Column titles: {result[2]}")

    # IMPORTANT: There's a bug in your function!
    # The drop operations need inplace=True or need to be assigned back to df
    # Let's check if the function actually dropped the columns
    print("\nColumns in DataFrame after function call:")
    print(list(df.columns))

    # Test with a DataFrame that doesn't have the columns to drop
    print("\n\nTest with DataFrame missing columns to drop:")
    df2 = pd.DataFrame({
        'Name': [100, 200, 300],
        'Hazardous': [True, False, True],
        'Close Approach Date': ['2020-01-01', '2021-02-02', '2022-03-03']
    })
    print(df2)

    result2 = data_details(df2)
    print("\nFunction result for second test:")
    print(f"Returned tuple: {result2}")
    print(f"Number of rows: {result2[0]}")
    print(f"Number of columns: {result2[1]}")
    print(f"Column titles: {result2[2]}")

    # Fixed version of the function for demo purposes
    print("\n\nDemonstrating fixed version of function:")

    def fixed_data_details(df):
        # Create a copy of the DataFrame to avoid modifying the original
        df_copy = df.copy()

        if "Orbiting Body" in df_copy.columns:
            df_copy = df_copy.drop('Orbiting Body', axis=1)

        if "Equinox" in df_copy.columns:
            df_copy = df_copy.drop('Equinox', axis=1)

        if "Neo Reference ID" in df_copy.columns:
            df_copy = df_copy.drop('Neo Reference ID', axis=1)

        num_rows, num_cols = df_copy.shape
        column_titles = list(df_copy.columns)

        data = (num_rows, num_cols, column_titles)
        return data

    fixed_result = fixed_data_details(df)
    print("Fixed function result:")
    print(f"Returned tuple: {fixed_result}")
    print(f"Number of rows: {fixed_result[0]}")
    print(f"Number of columns: {fixed_result[1]}")
    print(f"Column titles: {fixed_result[2]}")
    print("\nOriginal DataFrame columns still intact:")
    print(list(df.columns))


# Run the test
if __name__ == "__main__":
    test_data_details()