import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_correlations(file_path):
   
    df = pd.read_csv(file_path)
    
 
    solar_temp_df = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]
    corr_matrix = solar_temp_df.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap: Solar Radiation Components & Temperature Measures')
    plt.show()

  


