import pandas as pd
import matplotlib.pyplot as plt

def plot_numerical_histograms(df, numerical_columns, bins=30, figsize=(10, 8)):
    """
    Plot histograms for numerical columns in a DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to analyze.
    numerical_columns (list): A list of numerical column names.
    bins (int, optional): Number of bins in the histogram. Defaults to 30.
    figsize (tuple, optional): Figure size in inches. Defaults to (10, 8).

    Returns:
    None

    Example Usage:
    plot_numerical_histograms(df, numerical_columns)
    """
    df[numerical_columns].hist(bins=bins, figsize=figsize)
    plt.tight_layout()
    plt.show()

if __name__ == "__main":
    # Example usage:
    # Assuming you have a DataFrame 'df' and 'numerical_columns' as a list of column names
    plot_numerical_histograms(df, numerical_columns)
