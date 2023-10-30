import pandas as pd

def convert_to_numeric(df, columns):
    """
    Converts specified columns in a DataFrame to numeric values with error handling.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to perform the conversion on.
    columns (list of str): A list of column names to be converted to numeric.

    Returns:
    pandas.DataFrame: The DataFrame with specified columns converted to numeric.

    """
    new_df = df.copy()
    new_df[columns] = new_df[columns].applymap(lambda x: pd.to_numeric(x, errors='coerce'))
    return new_df
