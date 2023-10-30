import pandas as pd

def categorical_summary(df, categorical_features, fill=True):
    """
    Generate a summary of categorical features in a DataFrame, including counts, percentages, and missing values.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to analyze.
    categorical_features (list or str): A list of column names or a single column name as a string.
    fill (bool, optional): Whether to fill missing values with 'Missing'. Defaults to True.

    Returns:
    pandas.DataFrame: A tabular summary of categorical features, including counts, percentages, and missing values.

    Example Usage:
    summary = categorical_summary(df, categorical_features)
    print(summary)
    """
    # Ensure categorical_features is a list
    if not isinstance(categorical_features, list):
        categorical_features = [categorical_features]

    # Create a new DataFrame with missing values filled using the specified fill_value if fill is True
    if fill:
        df_new = df.fillna('Missing')
    else:
        df_new = df

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame(columns=["Count", "Percentage"])

    # Loop through all columns in the specified categorical features
    for column in categorical_features:
        # Calculate and store value counts and percentages
        value_counts = df_new[column].value_counts()
        total_values = len(df_new[column])
        value_percentages = (value_counts / total_values) * 100

        # Calculate and store missing values and percentages
        missing_values = df_new[column].eq('Missing').sum()
        missing_percentage = (missing_values / total_values) * 100

        # Create a DataFrame for the current column
        column_df = pd.DataFrame({
            "Count": value_counts,
            "Percentage": value_percentages
        })

        # Add a row for missing values
        column_df = column_df.append({"Count": missing_values, "Percentage": missing_percentage}, ignore_index=True)

        new_indices = value_counts.index.tolist()
        new_indices.append('Missing')
        column_df.set_index(pd.Index(new_indices), inplace=True)

        # Add the column name as a new index level
        column_df.index = pd.MultiIndex.from_tuples([(column, index) for index in column_df.index])

        # Append the current column's DataFrame to the result_df
        result_df = pd.concat([result_df, column_df])

    return result_df

if __name__ == "__main":
    # Example usage:
    # Assuming you have a DataFrame 'df' and 'categorical_features' as a list of column names or a single column name as a string
    summary = categorical_summary(df, categorical_features)
    print(summary)
