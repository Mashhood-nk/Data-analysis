import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def box_plot_list(data, continuous_features, dependent_variable=None):
    """
    Plot boxplots for numerical columns, optionally grouped by a dependent variable.

    Parameters:
    data (pandas.DataFrame): The input DataFrame to analyze.
    continuous_features (list): A list of numerical column names.
    dependent_variable (str, optional): The column name used to group the boxplots.

    Returns:
    None

    Example Usage:
    # To plot boxplots for all continuous features
    box_plot_list(df, continuous_features)

    # To plot boxplots grouped by a dependent variable
    box_plot_list(df, continuous_features, dependent_variable='DependentVariable')
    """
    if dependent_variable:
        unique_values = data[dependent_variable].unique()
        unique_values = unique_values[~pd.isna(unique_values)]
        for feature in continuous_features:
            feature_df = data[[dependent_variable, feature]]
            ax = sns.boxplot(x=dependent_variable, y=feature, data=feature_df)
            ax.set_title(f"Boxplot of {feature} by {dependent_variable}")
            ax.set_ylabel("Values")
            ax.set_xticklabels(unique_values)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
    else:
        data[continuous_features].boxplot(figsize=(10, 8))
        plt.title("Boxplots for Numerical Columns")
        plt.ylabel("Values")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
