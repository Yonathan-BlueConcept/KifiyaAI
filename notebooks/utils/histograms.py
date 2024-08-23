import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def plot_histograms(df):
   
    # Step 1: Define the variables to plot
    variables = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']
    titles = ['Global Horizontal Irradiance (GHI)',
              'Direct Normal Irradiance (DNI)',
              'Diffuse Horizontal Irradiance (DHI)',
              'Wind Speed (WS)',
              'Temperature (TModA)',
              'Temperature (TModB)']

    # Step 2: Create histograms
    plt.figure(figsize=(15, 10))
    for i, var in enumerate(variables):
        plt.subplot(2, 3, i + 1)
        sns.histplot(df[var], bins=30, kde=True, color='skyblue')
        plt.title(titles[i])
        plt.xlabel(var)
        plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

# Example usage:
# df = pd.read_csv('your_data.csv')
# plot_histograms(df)
