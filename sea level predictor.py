import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load data
def load_data(filepath):
    """
    Load the sea level data from a CSV file and return a DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

# Perform linear regression
def perform_linear_regression(df, start_year=None):
    """
    Perform linear regression on the data. Optionally filter data from start_year onwards.
    Returns the slope, intercept, and a function for the regression line.
    """
    if start_year:
        df = df[df['Year'] >= start_year]
    
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    regression_line = lambda year: intercept + slope * year
    return slope, intercept, regression_line

# Visualize the data and regression lines
def plot_sea_level(df, regression_line1=None, regression_line2=None):
    """
    Plot the sea level data and regression lines.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original data')
    if regression_line1:
        plt.plot(df['Year'], regression_line1(df['Year']), color='orange', label='Fitted line (All data)')
    if regression_line2:
        future_years = pd.Series(range(df['Year'].min(), 2051))
        plt.plot(future_years, regression_line2(future_years), color='green', label='Fitted line (From 2000)')
    
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
if __name__ == "__main__":
    # Load and preprocess data
    df = load_data('sea_level_data.csv')

    # Perform linear regression
    slope1, intercept1, regression_line1 = perform_linear_regression(df)
    slope2, intercept2, regression_line2 = perform_linear_regression(df, start_year=2000)

    # Visualize data and regression lines
    plot_sea_level(df, regression_line1, regression_line2)
