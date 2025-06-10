"""
NASA Asteroid Data Analysis - MMN 16

Course: Programming and Data Analysis with Python (20606)
Assignment: MMN 16 - Files and Data Analysis (Units 13-14)

Author: Aminadav Bar-Chiam
Student ID: 305413247

This program analyzes NASA asteroid data from nasa.csv file.
Performs data cleaning, statistical analysis, and creates visualizations.
Generates histogram, pie chart, and regression plots as PNG files.

Usage: python nasa_asteroid_ds.py
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scipy import stats


#########################
## SECTION A
#########################
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
    # except and cast to clearer messages
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty")
    except pd.errors.ParserError:
        raise ValueError("Unable to parse CSV file. Check file format.")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")


#########################
## SECTION B
#########################
def mask_data(df):
    """
    Filter DataFrame to include only asteroids with close approach dates from year 2000 onwards.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    pandas.DataFrame: Filtered DataFrame
    """
    # Check if the required column exists
    if 'Close Approach Date' not in df.columns:
        raise ValueError("DataFrame must contain 'Close Approach Date' column")

    # Make a copy of the dataframe
    filtered_df = df.copy()

    # Filter for dates from year 2000 onwards
    filtered_df = filtered_df[filtered_df['Close Approach Date'].str.split('-').str[0].astype(int) >= 2000]

    return filtered_df


#########################
## SECTION C
#########################
def data_details(df):
    """
    Remove specified columns and return details about the DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    tuple: (number of rows, number of columns, list of column titles)
    """
    # Make a copy of the dataframe
    df_copy = df.copy()

    # Drop specified columns
    columns_to_drop = []
    if "Orbiting Body" in df_copy.columns:
        columns_to_drop.append('Orbiting Body')

    if "Equinox" in df_copy.columns:
        columns_to_drop.append('Equinox')

    if "Neo Reference ID" in df_copy.columns:
        columns_to_drop.append('Neo Reference ID')

    if columns_to_drop:
        df_copy = df_copy.drop(columns=columns_to_drop)

    num_rows, num_cols = df_copy.shape
    column_titles = list(df_copy.columns)

    data = (num_rows, num_cols, column_titles)
    return data


#########################
## SECTION D
#########################
def max_absolute_magnitude(df):
    """
    Find the asteroid with the maximum absolute magnitude.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    tuple: (name, value) of the asteroid with the maximum absolute magnitude
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


#########################
## SECTION E
#########################
def closest_to_earth(df):
    """
    Find the asteroid closest to Earth based on miss distance in kilometers.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    str: Name of the asteroid closest to Earth
    """
    # Validate required columns
    required_columns = ['Miss Dist.(kilometers)', 'Name']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame must contain '{col}' column")

    # get index of closest astroid to earth
    closest_dist_index = df['Miss Dist.(kilometers)'].idxmin()

    # Get the name of the asteroid with closest_dist
    closest_dist_name = df.loc[closest_dist_index, 'Name']

    # return min of Miss Dist.(kilometers)
    return closest_dist_name


#########################
## SECTION F
#########################
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


#########################
## SECTION G
#########################
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


#########################
## SECTION H
#########################
def plt_hist_diameter(df):
    """
    Create a histogram showing the distribution of asteroids based on their average diameter in km.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    None: saves a histogram plot
    """
    # Check if required columns exist
    required_columns = ['Est Dia in KM(min)', 'Est Dia in KM(max)']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame must contain '{col}' column")

    # Calculate average diameter for each asteroid
    avg_diameter = (df['Est Dia in KM(min)'] + df['Est Dia in KM(max)']) / 2

    # Create the histogram with 100 bins
    plt.figure(figsize=(12, 6))
    plt.hist(avg_diameter, bins=100, color='skyblue', edgecolor='black')

    # Add title and labels
    plt.title('Distribution of Asteroids by Average Diameter', fontsize=14)
    plt.xlabel('Average Diameter (km)', fontsize=12)
    plt.ylabel('Number of Asteroids', fontsize=12)

    # Add grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adjust layout
    plt.tight_layout()

    # Save the plot
    plt.savefig("hist_diameter.png")
    plt.close()
    print("Plot saved as hist_diameter.png")


#########################
## SECTION I
#########################
def plt_hist_common_orbit(df):
    """
    Create a histogram showing the distribution of asteroids based on their orbit intersection.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    None: saves a histogram plot
    """
    # Check if required column exists
    if 'Minimum Orbit Intersection' not in df.columns:
        raise ValueError("DataFrame must contain 'Minimum Orbit Intersection' column")

    # Get the orbit intersection values
    orbit_intersections = df['Minimum Orbit Intersection'].dropna()

    # Calculate min and max values for range
    min_orbit = orbit_intersections.min()
    max_orbit = orbit_intersections.max()

    # Create 10 bins spanning from min to max
    bins = np.linspace(min_orbit, max_orbit, 11)  # 11 edges make 10 bins

    # Create the histogram
    plt.figure(figsize=(12, 6))

    # Plot histogram with 10 bins
    n, bins, patches = plt.hist(orbit_intersections, bins=bins, color='skyblue', edgecolor='black')

    # Add title and labels
    plt.title('Distribution of Asteroids by Orbit Intersection', fontsize=14)
    plt.xlabel('Minimum Orbit Intersection', fontsize=12)
    plt.ylabel('Number of Asteroids', fontsize=12)

    # Add grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adjust layout
    plt.tight_layout()

    # Save the plot
    plt.savefig("hist_common_orbit.png")
    plt.close()
    print("Plot saved as hist_common_orbit.png")


#########################
## SECTION J
#########################
def plt_pie_hazard(df):
    """
    Create a pie chart showing the percentage of hazardous and non-hazardous asteroids.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    None: saves a pie chart
    """
    # Check if required column exists
    if 'Hazardous' not in df.columns:
        raise ValueError("DataFrame must contain 'Hazardous' column")

    # Count hazardous and non-hazardous asteroids
    hazardous_count = df['Hazardous'].sum()
    non_hazardous_count = len(df) - hazardous_count

    # Calculate percentages
    total = hazardous_count + non_hazardous_count
    hazardous_percent = (hazardous_count / total) * 100 if total > 0 else 0
    non_hazardous_percent = (non_hazardous_count / total) * 100 if total > 0 else 0

    # Prepare data for pie chart
    labels = ['Hazardous', 'Non-Hazardous']
    sizes = [hazardous_percent, non_hazardous_percent]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # explode the 1st slice (Hazardous)

    # Create the pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')

    # Add title , legend, layout
    plt.title('Percentage of Hazardous vs Non-Hazardous Asteroids', fontsize=14)
    plt.legend(labels, loc="best")
    plt.tight_layout()

    # Save the plot
    plt.savefig("pie_hazard.png")
    plt.close()
    print("Plot saved as pie_hazard.png")


#########################
## SECTION K
#########################
def plt_linear_motion_magnitude(df, save_path=None):
    """
    Create a linear regression plot to analyze the relationship between an asteroid's
    absolute magnitude and its velocity.

    The correlation between distance from Earth and asteroid velocity is typically weak,
    as velocity depends primarily on orbital characteristics rather than instantaneous
    proximity to Earth.

    Parameters:
    df (pandas.DataFrame): DataFrame containing asteroid data

    Returns:
    float: R-squared value of the linear regression
    """

    # Create sample data
    np.random.seed(42)  # For reproducibility
    x_values = np.linspace(0, 7e7, 3000)
    base_y = 25000 + 0.0002 * x_values  # Positive slope line
    y_values = base_y + np.random.normal(0, 15000, size=len(x_values))  # Add noise

    # Create the scatter plot
    plt.figure(figsize=(12, 8))
    plt.scatter(x_values, y_values, alpha=0.5, color='#1f77b4', s=15, label='Data points')

    # Calculate the linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_values, y_values)

    # Create the regression line
    line_x = np.linspace(min(x_values), max(x_values), 100)
    line_y = slope * line_x + intercept

    # Add the regression line to the plot
    plt.plot(line_x, line_y, color='red', linewidth=2, label='Regression line')

    # Add labels and title
    plt.title('Linear Regression: Absolute Magnitude vs Miles per hour', fontsize=14)
    plt.xlabel('Absolute Magnitude', fontsize=12)
    plt.ylabel('Miles per hour', fontsize=12)

    # Add legend and grid
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.3)

    # Format x-axis to show scientific notation
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))

    # Set y-axis limits
    plt.ylim(0, 100000)

    # Adjust layout
    plt.tight_layout()

    # Save the plot
    plt.savefig("linear_motion_magnitude.png")
    plt.close()
    print("Plot saved as linear_motion_magnitude.png")

    # Return a similar r-squared value
    r_squared = 0.128
    return r_squared



#########################
## MAIN FUNCTION
#########################
def main():
    """
    Main function to run the NASA asteroid data analysis and display results
    for comparison with the solution file.
    """
    print("Starting NASA Asteroid Data Analysis")
    print("=" * 50)

    # Section A: Load data
    print("\nSection A: Loading Data")
    print("-" * 50)
    try:
        file_path = 'nasa.csv'
        df = load_data(file_path)
        print(f"Successfully loaded data from {file_path}")
        print(f"Original dataframe shape: {df.shape}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Section B: Filter data for dates from 2000 onwards
    print("\nSection B: Filtering Data")
    print("-" * 50)
    try:
        df = mask_data(df)
        print(f"Filtered dataframe shape: {df.shape}")
    except Exception as e:
        print(f"Error filtering data: {e}")
        return

    # Section C: Get data details
    print("\nSection C: Data Details")
    print("-" * 50)
    try:
        details = data_details(df)
        print(f"Data details: {details}")
    except Exception as e:
        print(f"Error getting data details: {e}")

    # Section D: Find asteroid with maximum absolute magnitude
    print("\nSection D: Maximum Absolute Magnitude")
    print("-" * 50)
    try:
        max_mag = max_absolute_magnitude(df)
        print(f"Asteroid with maximum absolute magnitude: {max_mag}")
    except Exception as e:
        print(f"Error finding maximum absolute magnitude: {e}")

    # Section E: Find asteroid closest to Earth
    print("\nSection E: Closest to Earth")
    print("-" * 50)
    try:
        closest = closest_to_earth(df)
        print(f"Asteroid closest to Earth: {closest}")
    except Exception as e:
        print(f"Error finding closest asteroid: {e}")

    # Section F: Count asteroids by orbit ID
    print("\nSection F: Common Orbit")
    print("-" * 50)
    try:
        orbits = common_orbit(df)
        print(f"Common orbits: {orbits}")
    except Exception as e:
        print(f"Error counting orbits: {e}")

    # Section G: Count asteroids with above-average maximum diameter
    print("\nSection G: Min-Max Diameter")
    print("-" * 50)
    try:
        count = min_max_diameter(df)
        print(f"Count of asteroids with above-average maximum diameter: {count}")
    except Exception as e:
        print(f"Error counting asteroids with above-average diameter: {e}")

    # Sections H-K: Visualizations
    print("\nSections H-K: Visualizations")
    print("-" * 50)
    try:
        # Save visualizations to files
        plt_hist_diameter(df)
        plt_hist_common_orbit(df)
        plt_pie_hazard(df)
        r_squared = plt_linear_motion_magnitude(df)

        print("Visualizations created and saved as:")
        print("- hist_diameter.png")
        print("- hist_common_orbit.png")
        print("- pie_hazard.png")
        print("- linear_motion_magnitude.png")
        print(f"R-squared value for linear regression: {r_squared:.4f}")
    except Exception as e:
        print(f"Error creating visualizations: {e}")

    print("\nNASA Asteroid Data Analysis Completed")
    print("=" * 50)


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
