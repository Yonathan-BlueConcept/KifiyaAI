
import pandas as pd

def getSummaryStatistics(file_path):
    # Load the DataFrame
    df = pd.read_csv(file_path)
    
    # Identify and remove columns where all values are NaN
    all_null_columns = df.columns[df.isna().all()].tolist()
    df = df.drop(columns=all_null_columns)
    
    # Select only numerical columns
    numerical_columns = df.select_dtypes(include='number')
    
    # Return the summary statistics of numerical columns
    return numerical_columns.describe()
