import pandas as pd

def filter_dataframe_by_age(data, age_column='Age', age_threshold=14, keep_missing=False):
    """
    Filter a DataFrame based on the specified age column.

    Parameters:
    data (pandas.DataFrame): The input DataFrame to filter.
    age_column (str, optional): The name of the age column (default is 'Age').
    age_threshold (int, optional): The age threshold for filtering (default is 14).
    keep_missing (bool, optional): Whether to keep rows with missing age values (default is False).

    Returns:
    pandas.DataFrame: The filtered DataFrame.
    """
    if keep_missing:
        filtered_data = data[data[age_column].isnull() | (data[age_column] >= age_threshold)]
    else:
        filtered_data = data[data[age_column] >= age_threshold]
    
    return filtered_data

# Example usage:
# filtered_data = filter_dataframe_by_age(new_data, age_column='Age', age_threshold=14, keep_missing=True)
# print(filtered_data.shape)
