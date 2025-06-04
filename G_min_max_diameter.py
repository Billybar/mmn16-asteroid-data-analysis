def min_max_diameter(df):
    """
    Count asteroids with maximum diameter above the average maximum diameter.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    int: Count of asteroids with maximum diameter above average
    """
    # Check if required column exists
    if 'Est Dia in KM(max)' not in df.columns:
        raise ValueError("DataFrame must contain 'Est Dia in KM(max)' column")

    # Calculate the average maximum diameter
    avg_max_diameter = df['Est Dia in KM(max)'].mean()

    # Count asteroids with maximum diameter above average
    count_above_avg = df[df['Est Dia in KM(max)'] > avg_max_diameter].shape[0]

    return count_above_avg


def test_min_max_diameter():
    """
    Test the min_max_diameter function with a sample DataFrame.
    """
    import pandas as pd
    import numpy as np

    # Create a sample DataFrame with test data
    test_data = {
        'Neo Reference ID': [1, 2, 3, 4, 5, 6],
        'Name': [1001, 1002, 1003, 1004, 1005, 1006],
        'Est Dia in KM(max)': [0.5, 1.2, 0.8, 2.5, 0.3, 1.5]
        # Average max diameter = (0.5+1.2+0.8+2.5+0.3+1.5)/6 = 1.133...
        # Values above average: 1.2, 2.5, 1.5 (3 asteroids)
    }

    df = pd.DataFrame(test_data)
    print("Test DataFrame:")
    print(df)

    # Calculate expected result manually for verification
    avg_diameter = np.mean(test_data['Est Dia in KM(max)'])
    count_above_avg = sum(1 for d in test_data['Est Dia in KM(max)'] if d > avg_diameter)

    print(f"\nAverage maximum diameter: {avg_diameter:.4f}")
    print(f"Expected count above average: {count_above_avg}")

    # Call the function to test
    result = min_max_diameter(df)

    # Print the result
    print(f"Function result: {result}")

    # Verify the result
    assert result == count_above_avg, f"Expected {count_above_avg}, but got {result}"

    print("Test passed!")

    # Test with an empty DataFrame
    try:
        empty_df = pd.DataFrame(columns=['Est Dia in KM(max)'])
        min_max_diameter(empty_df)
        print("Empty DataFrame test failed: Expected an error or special case handling")
    except:
        print("Empty DataFrame test passed: Correctly handled edge case")

    # Test with missing column
    try:
        missing_column_df = pd.DataFrame({'Name': [1001, 1002]})
        min_max_diameter(missing_column_df)
        print("Missing column test failed: Expected an error but got none")
    except ValueError as e:
        print(f"Missing column test passed: {e}")


# Run the test if this script is executed directly
if __name__ == "__main__":
    test_min_max_diameter()