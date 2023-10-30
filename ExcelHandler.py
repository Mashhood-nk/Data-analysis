"""
Excel File Handling Script

This script handles the reading of Excel files and ensures that a file named 'InputDataset.xlsx' is read into a DataFrame.
If the file doesn't exist, it looks for other Excel files and renames one for reading.
It offers user prompts for handling multiple Excel files, including renaming and reading the first file.

Usage:
1. Place this script in the directory with your Excel data files.
2. Run the script to handle the Excel file.
3. The script will ensure 'InputDataset.xlsx' is available as a DataFrame.

Author: [Mashhood]
"""

import os
import pandas as pd
from tkinter import Tk, filedialog, messagebox

def ReadExcel():
    # Get a list of files in the current directory
    files = os.listdir()

    # Check if "InputDataset.xlsx" exists
    if "InputDataset.xlsx" in files:
        # If it exists, read it into a DataFrame
        df = pd.read_excel("InputDataset.xlsx")
        print("Found and read 'InputDataset.xlsx'.")
    else:
        # If it doesn't exist, look for Excel files
        excel_files = [file for file in files if file.endswith(".xlsx")]

        if len(excel_files) == 1:
            # If there's only one Excel file, rename and read it
            os.rename(excel_files[0], "InputDataset.xlsx")
            df = pd.read_excel("InputDataset.xlsx")
            print(f"Renamed '{excel_files[0]}' to 'InputDataset.xlsx' and read it.")
        elif len(excel_files) > 1:
            # If there are multiple Excel files, show a popup to confirm the renaming
            root = Tk()
            root.withdraw()
            choice = messagebox.askquestion("Multiple Excel Files Found",
                                            "Multiple Excel files found. Do you want to rename and read the first Excel file?",
                                            icon='warning')
            if choice == 'yes':
                os.rename(excel_files[0], "InputDataset.xlsx")
                df = pd.read_excel("InputDataset.xlsx")
                print(f"Renamed '{excel_files[0]}' to 'InputDataset.xlsx' and read it.")
            else:
                df = None
                print("No Excel file renamed or read.")
        else:
            df = None
            print("No Excel file found.")

    return df

if __name__ == "__main__":
    df = ReadExcel()
    # Now, you can work with the 'df' DataFrame as needed.
