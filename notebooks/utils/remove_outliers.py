import pandas as pd

def removeOutliers(columns, df):
   
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        
        # Calculate IQR
        IQR = Q3 - Q1
        
        # Define lower and upper bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Remove outliers for the current column
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
   
    return df
