import pandas as pd
import numpy as np


def calculate_z_scores(df, columns):
    
    
    # Calculate the Z-scores for the specified columns
    z_scores = df[columns].apply(lambda x: (x - x.mean()) / x.std())
    
    return z_scores


