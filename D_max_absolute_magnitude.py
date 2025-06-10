import os
import numpy as np
import pandas as pd
from datetime import datetime


def max_absolute_magnitude(df):
    """
    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    tuple: (index, name) of the asteroid with the maximum absolute magnitude
    """
    # Check if required columns exist
    required_columns = ['Absolute Magnitude', 'Name']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame must contain '{col}' column")

    # get index of the maximum absolute magnitude
    max_magnitude_index = df['Absolute Magnitude'].idxmax()

    # Get the name of the asteroid with maximum absolute magnitude
    max_magnitude_name = df.loc[max_magnitude_index, 'Name']

    # Get the val of the asteroid with maximum absolute magnitude
    max_magnitude_val = df.loc[max_magnitude_index, 'Absolute Magnitude']

    # Return the tuple of (name, val)
    return max_magnitude_name, max_magnitude_val


def test_max_absolute_magnitude():
    """
    Test the max_absolute_magnitude function with a sample DataFrame.
    """
    # Import pandas for creating the test DataFrame
    import pandas as pd

    # Create a sample DataFrame with test data
    test_data = {
        'Neo Reference ID': [1, 2, 3, 4, 5],
        'Name': [1001, 1002, 1003, 1004, 1005],
        'Absolute Magnitude': [15.7, 18.2, 22.5, 19.8, 16.3],
        'Miss Dist.(kilometers)': [1000, 5000, 2500, 8000, 4200]
    }

    df = pd.DataFrame(test_data)
    print("Test DataFrame:")
    print(df)

    # Call the function to test
    name, magnitude = max_absolute_magnitude(df)

    # Print the result
    print(f"\nResult: (name={name}, magnitude={magnitude})")

    # Verify the result
    expected_name = 1003  # Name at the row with maximum Absolute Magnitude (22.5)
    expected_magnitude = 22.5  # The maximum Absolute Magnitude value

    assert name == expected_name, f"Expected name {expected_name}, but got {name}"
    assert magnitude == expected_magnitude, f"Expected magnitude {expected_magnitude}, but got {magnitude}"

    print("Test passed!")

    # Test with an empty DataFrame
    empty_df = pd.DataFrame(columns=['Name', 'Absolute Magnitude'])
    try:
        max_absolute_magnitude(empty_df)
        print("Empty DataFrame test failed: Expected an error but got none")
    except:
        print("Empty DataFrame test passed: Correctly raised an error")

    # Test with missing columns
    missing_columns_df = pd.DataFrame({
        'Neo Reference ID': [1, 2, 3],
        'Miss Dist.(kilometers)': [1000, 5000, 2500]
    })
    try:
        max_absolute_magnitude(missing_columns_df)
        print("Missing columns test failed: Expected an error but got none")
    except ValueError as e:
        print(f"Missing columns test passed: {e}")


# Run the test if this script is executed directly
if __name__ == "__main__":
    test_max_absolute_magnitude()