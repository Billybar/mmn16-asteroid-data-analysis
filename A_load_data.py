import os
import tempfile

import numpy as np
import pandas as pd

def load_data(file):
    """
    Load CSV data file into a pandas DataFrame.

    Parameters:
    file (str): Path to the CSV file

    Returns:
    pandas.DataFrame: DataFrame containing the loaded data
    """
    # if file parameter is None
    if file is None:
        raise ValueError("file parameter os None")

    # if file empty
    if not file:
        raise ValueError("File path is empty")

    # if file not exists on disk
    if not os.path.exists(file):
        raise FileNotFoundError(f"File does not exist: {file}")

    # if file not of csv
    if not file.lower().endswith('.csv'):
        raise ValueError(f"File must have .csv extension, got: {file}")

    # If all checks pass, load the CSV
    try:
        df = pd.read_csv(file, sep=',')
        return df
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty")
    except pd.errors.ParserError:
        raise ValueError("Unable to parse CSV file. Check file format.")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")


def test_load_data():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        # Test case 1: Valid file
        valid_file_path = os.path.join(temp_dir, "valid_data.csv")
        with open(valid_file_path, 'w') as f:
            f.write("col1,col2,col3\n1,2,3\n4,5,6")

        print("Testing valid file...")
        df = load_data(valid_file_path)
        print("✓ Success! Loaded DataFrame shape:", df.shape)

        # Test case 2: None parameter
        print("\nTesting None parameter...")
        try:
            load_data(None)
            print("✗ Failed: Should have raised ValueError")
        except ValueError as e:
            print(f"✓ Success! Correctly raised: {e}")

        # Test case 3: Empty string
        print("\nTesting empty string parameter...")
        try:
            load_data("")
            print("✗ Failed: Should have raised ValueError")
        except ValueError as e:
            print(f"✓ Success! Correctly raised: {e}")

        # Test case 4: Non-existent file
        non_existent_path = os.path.join(temp_dir, "doesnt_exist.csv")
        print("\nTesting non-existent file...")
        try:
            load_data(non_existent_path)
            print("✗ Failed: Should have raised FileNotFoundError")
        except FileNotFoundError as e:
            print(f"✓ Success! Correctly raised: {e}")

        # Test case 5: Empty file
        empty_file_path = os.path.join(temp_dir, "empty.csv")
        with open(empty_file_path, 'w') as f:
            pass

        print("\nTesting empty file...")
        try:
            load_data(empty_file_path)
            print("✗ Failed: Should have raised ValueError")
        except ValueError as e:
            print(f"✓ Success! Correctly raised: {e}")

        # Test case 6: Invalid CSV format
        invalid_file_path = os.path.join(temp_dir, "invalid.csv")
        with open(invalid_file_path, 'w') as f:
            f.write("col1,col2,col3\n1,2\n4,5,6,7")

        print("\nTesting invalid CSV format...")
        try:
            load_data(invalid_file_path)
            print("✗ Failed: Should have raised ValueError")
        except ValueError as e:
            print(f"✓ Success! Correctly raised: {e}")

    finally:
        # Clean up the temporary files
        import shutil
        shutil.rmtree(temp_dir)


# Run the test
if __name__ == "__main__":
    test_load_data()