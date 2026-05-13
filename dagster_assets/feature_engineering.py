import os
from dagster import asset
import pandas as pd

@asset
def cleaned_user_features():
    # Define the path to the CSV file
    # This assumes a 'data' folder exists in the directory from which you run Dagster
    file_path = os.path.join("data", "user_features.csv")
    
    # Check if the file exists to prevent cryptic errors
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find the data file at: {file_path}")

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    # (Optional) Add your actual cleaning or normalization logic here
    # Example: df['age_normalized'] = df['age'] / df['age'].max()
    
    return df