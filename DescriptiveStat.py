import pandas as pd
import numpy as np

def generate_descriptive_stats(df, continuous_variables, categorical_variables):
    """
    Generate descriptive statistics for a DataFrame's continuous and categorical variables.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to analyze.
    continuous_variables (list): A list of names of continuous variables.
    categorical_variables (list): A list of names of categorical variables.

    Returns:
    pandas.DataFrame: A DataFrame containing descriptive statistics for the specified variables.
    """
    # Initialize an empty list to store the descriptive statistics
    stats_list = []
    
    # Calculate statistics for continuous variables
    for col in continuous_variables:
        if col in df.columns:
            mean = df[col].mean()
            median = df[col].median()
            std_dev = df[col].std()
            percentile_25 = np.nanpercentile(df[col], 25)
            percentile_75 = np.nanpercentile(df[col], 75)
            stats_list.append({'Feature': col, 'Category': 'Continuous', 
                               'Frequency or mean': mean, 'Median': median,
                               'Percent or SD': std_dev,
                               '25th percentile': percentile_25,
                               '75th percentile': percentile_75})
    
    # Calculate statistics for categorical variables
    for col in categorical_variables:
        if col in df.columns:
            frequencies = df[col].value_counts()
            percentages = (frequencies / len(df)) * 100
            for category, freq, percent in zip(frequencies.index, frequencies, percentages):
                stats_list.append({'Feature': col, 'Category': category, 
                                   'Frequency or mean': freq, 'Median': '',
                                   'Percent or SD': percent,
                                   '25th percentile': '', '75th percentile': ''})
    
    # Convert the list of dictionaries to a DataFrame
    stats_df = pd.DataFrame(stats_list)
    
    return stats_df

# Example usage:
# Assuming you have a DataFrame 'df', a list of continuous variables 'continuous_vars',
# and a list of categorical variables 'categorical_vars', you can call the function like this:
# descriptive_stats = generate_descriptive_stats(df, continuous_vars, categorical_vars)
# print(descriptive_stats)
