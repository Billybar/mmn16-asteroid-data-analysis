import os
import numpy as np
import pandas as pd
from datetime import datetime

def mask_data(df):
    # Check if the required column exists
    if 'Close Approach Date' not in df.columns:
        raise ValueError("DataFrame must contain 'Close Approach Date' column")

    # Make a copy of the dataframe
    filtered_df = df.copy()

    # Filter for dates from year 2000 onwards
    filtered_df = filtered_df[filtered_df['Close Approach Date'].str.split('-').str[0].astype(int) >= 2000]

    return filtered_df



# Test function for mask_data
def test_mask_data():
    # Create a sample DataFrame with asteroid data
    data = {
        'Neo Reference ID': [1, 2, 3, 4, 5],
        'Name': [111, 222, 333, 444, 555],
        'Close Approach Date': ['1998-05-15', '2000-01-20', '1999-12-31', '2005-07-04', '2022-11-30'],
        'Hazardous': [True, False, True, False, True]
    }

    # Create DataFrame with dates as string format
    test_df = pd.DataFrame(data)

    # Convert to datetime for testing
    test_df['Close Approach Date'] = pd.to_datetime(test_df['Close Approach Date'])

    print("Original DataFrame:")
    print(test_df)
    print("\n")

    # Test 1: Normal case - filter dates from 2000 onwards
    filtered_df = mask_data(test_df)
    print("Filtered DataFrame (2000 onwards):")
    print(filtered_df)
    print(f"Expected 3 rows, got {len(filtered_df)} rows")
    assert len(filtered_df) == 3, f"Expected 3 rows, got {len(filtered_df)}"

    # Test 2: Edge case - empty DataFrame after filtering
    early_data = {
        'Neo Reference ID': [1, 2, 3],
        'Name': [111, 222, 333],
        'Close Approach Date': ['1998-05-15', '1997-01-20', '1999-12-31'],
        'Hazardous': [True, False, True]
    }
    early_df = pd.DataFrame(early_data)
    early_df['Close Approach Date'] = pd.to_datetime(early_df['Close Approach Date'])

    filtered_early = mask_data(early_df)
    print("\nFiltered DataFrame (all before 2000):")
    print(filtered_early)
    print(f"Expected 0 rows, got {len(filtered_early)} rows")
    assert len(filtered_early) == 0, f"Expected 0 rows, got {len(filtered_early)}"

    # Test 3: Missing column test
    try:
        bad_df = pd.DataFrame({'Neo Reference ID': [1, 2], 'Name': [111, 222]})
        mask_data(bad_df)
        print("\nTest failed: Should have raised ValueError for missing column")
        assert False
    except ValueError as e:
        print(f"\nCorrectly raised error for missing column: {e}")

    print("\nAll tests passed!")


# Run the test
if __name__ == "__main__":
    test_mask_data()