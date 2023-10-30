import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_missing_data(df):
    """
    Analyzes missing data in a given DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to analyze.

    Returns:
    pandas.DataFrame: A summary of missing data, including the total number and percentage
    of missing values for each feature.
    """
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count() * 100).sort_values(ascending=False)
    ms = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    ms = ms[ms["Percent"] > 0]
    return ms

def plot_missing_data_summary(df):
    """
    Plots the missing data summary.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to analyze and plot missing data.
    """
    summary = analyze_missing_data(df)  # Analyze missing data on-the-fly
    f, ax = plt.subplots(figsize=(20, 6))
    plt.xticks(rotation='vertical')
    fig = sns.barplot(x=summary.index, y=summary["Percent"], color="green", alpha=0.8)
    plt.xlabel('Features', fontsize=15)
    plt.ylabel('Percent of missing values', fontsize=15)
    plt.title('Percent missing data by feature', fontsize=15)

# Example usage:
# plot_missing_data_summary(df)
