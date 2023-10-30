import matplotlib.pyplot as plt
import pandas as pd

def create_subplots(categorical_features, columns):
    """
    Create a grid of subplots for visualizations.

    Parameters:
    categorical_features (list): List of categorical feature names.
    columns (int): Number of columns for the subplot grid.

    Returns:
    matplotlib.figure.Figure: The figure for subplots.
    numpy.ndarray: Array of subplot axes.
    """
    figsize = (30, 20)
    total_plots = len(categorical_features)
    rows = (total_plots + columns - 1) // columns
    
    fig, axes = plt.subplots(rows, columns)

    # Remove any extra subplots in the last row
    if total_plots % columns != 0:
        for i in range(total_plots % columns, columns):
            fig.delaxes(axes[rows - 1, i])

    return fig, axes

def autopct_label(pct):
    """
    Format the autopct label for pie charts.

    Parameters:
    pct (float): The percentage to format.

    Returns:
    str: Formatted autopct label.
    """
    return f'{pct:.1f}%' if pct > 5 else ''

def pi_chart(new_data, categorical_features, columns):
    """
    Create and display pie charts for categorical data.

    Parameters:
    new_data (pandas.DataFrame): The input DataFrame.
    categorical_features (list or str): List of categorical feature names or a single feature name.
    columns (int): Number of columns for the subplot grid.
    """
    if isinstance(categorical_features, list):
        fig, axes = create_subplots(categorical_features, columns)
        
        # Handle the case when you have only one row of subplots
        if len(axes.shape) == 1:
            axes = axes.reshape(1, -1)
        
        for i, features in enumerate(categorical_features):
            row_idx = i // columns
            col_idx = i % columns
            ax = axes[row_idx, col_idx]
            new_data[features].value_counts().plot.pie(fontsize=15, figsize=(15, 15), autopct=autopct_label, ax=ax, startangle=140)
            ax.set_aspect('equal')
            ax.set_title(features) 
        plt.show()
    elif isinstance(categorical_features, str):
        new_data[features].value_counts().plot.pie(fontsize=10, figsize=(20, 10), autopct="%.1f")
        plt.show()
