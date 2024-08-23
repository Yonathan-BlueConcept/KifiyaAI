import pandas as pd

def cleanData(file_path):
    # Load the DataFrame
    df = pd.read_csv(file_path)
    
    # Apply all filters in one step
    cleaned_df = df[(df['GHI'] > 0) & (df['DNI'] > 0) & (df['DHI'] > 0)]
    
    return cleaned_df