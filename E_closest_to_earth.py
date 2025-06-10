import os
import numpy as np
import pandas as pd
from datetime import datetime

def closest_to_earth(df):
    # Validate required columns
    required_columns = ['Miss Dist.(kilometers)', 'Name']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame must contain '{col}' column")

    # Check if DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")

    # get index of closest astroid to earth
    closest_dist_index = df['Miss Dist.(kilometers)'].idxmin()

    # Get the name of the asteroid with closest_dist
    closest_dist_name = df.loc[closest_dist_index, 'Name']

    # return min of Miss Dist.(kilometers)
    return closest_dist_name


def test_closest_to_earth():
    """
    Test the closest_to_earth function with a sample DataFrame.
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
    name = closest_to_earth(df)

    # Print the result
    print(f"\nResult: name={name}")

    # Verify the result
    # Note: The function is looking for maximum distance, not minimum as the name might suggest
    expected_name = 1004  # Name at the row with maximum Miss Dist.(kilometers) (8000)

    assert name == expected_name, f"Expected name {expected_name}, but got {name}"

    print("Test passed!")

    # Test with an empty DataFrame
    try:
        empty_df = pd.DataFrame(columns=['Name', 'Miss Dist.(kilometers)'])
        closest_to_earth(empty_df)
        print("Empty DataFrame test failed: Expected an error but got none")
    except:
        print("Empty DataFrame test passed: Correctly raised an error")

    # Test with missing columns
    try:
        missing_columns_df = pd.DataFrame({
            'Neo Reference ID': [1, 2, 3],
            'Name': [1001, 1002, 1003]
        })
        closest_to_earth(missing_columns_df)
        print("Missing columns test failed: Expected an error but got none")
    except:
        print("Missing columns test passed: Correctly raised an error")


# Run the test if this script is executed directly
if __name__ == "__main__":
    test_closest_to_earth()