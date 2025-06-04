import os
import numpy as np
import pandas as pd
from datetime import datetime


def common_orbit(df):
    """
    Create a dictionary with orbit IDs as keys and count of asteroids in each orbit as values.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    dict: Dictionary where keys are Orbit IDs and values are counts of asteroids
    """
    # Check if required column exists
    if 'Orbit ID' not in df.columns:
        raise ValueError("DataFrame must contain 'Orbit ID' column")

    # Count asteroids by Orbit ID
    orbit_counts = df['Orbit ID'].value_counts().to_dict()

    return orbit_counts


def test_common_orbit():
    """
    Test the common_orbit function with a sample DataFrame.
    """
    import pandas as pd

    # Create a sample DataFrame with test data
    test_data = {
        'Neo Reference ID': [1, 2, 3, 4, 5, 6],
        'Name': [1001, 1002, 1003, 1004, 1005, 1006],
        'Orbit ID': [101, 102, 101, 103, 102, 103]  # 2 asteroids in orbit 101, 2 in orbit 102, 2 in orbit 103
    }

    df = pd.DataFrame(test_data)
    print("Test DataFrame:")
    print(df)

    # Call the function to test
    result = common_orbit(df)

    # Print the result
    print("\nResult:")
    print(result)

    # Verify the result
    expected_result = {101: 2, 102: 2, 103: 2}

    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    print("Test passed!")

    # Test with an empty DataFrame
    empty_df = pd.DataFrame(columns=['Orbit ID'])
    empty_result = common_orbit(empty_df)
    print("\nEmpty DataFrame result:")
    print(empty_result)
    assert len(empty_result) == 0, "Expected empty dictionary for empty DataFrame"

    # Test with missing Orbit ID column
    try:
        missing_column_df = pd.DataFrame({'Name': [1001, 1002]})
        common_orbit(missing_column_df)
        print("Missing column test failed: Expected an error but got none")
    except ValueError as e:
        print(f"\nMissing column test passed: {e}")


# Run the test if this script is executed directly
if __name__ == "__main__":
    test_common_orbit()