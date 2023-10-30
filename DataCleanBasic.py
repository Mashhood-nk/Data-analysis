import pandas as pd

def clean_dataframe(df):
    """
    Cleans a given DataFrame by converting any cell with a period (.) to a NaN (Not-a-Number) value
    and stripping leading and trailing whitespaces from column names.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to be cleaned.

    Returns:
    pandas.DataFrame: The cleaned DataFrame with NaN values and stripped column names.
    """
    for column in df.columns:
        df[column] = df[column].apply(lambda x: float('nan') if x == '.' else x)
    
    cleaned_columns = df.columns.str.strip()
    df.columns = cleaned_columns
    
    return df
