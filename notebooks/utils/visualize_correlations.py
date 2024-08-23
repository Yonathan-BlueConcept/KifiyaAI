import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_correlations(file_path):
   
    df = pd.read_csv(file_path)
    
    # Step 1: Correlation Heatmap for Solar Radiation and Temperature Measures
    solar_temp_df = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]
    corr_matrix = solar_temp_df.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap: Solar Radiation Components & Temperature Measures')
    plt.show()

    # # Step 2: Pair Plots for Solar Radiation and Temperature Measures
    # sns.pairplot(solar_temp_df)
    # plt.suptitle('Pair Plot: Solar Radiation Components & Temperature Measures', y=1.02)
    # plt.show()

    # # Step 3: Scatter Matrix for Wind Conditions and Solar Irradiance
    # wind_solar_df = df[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']]
    # pd.plotting.scatter_matrix(wind_solar_df, figsize=(12, 10), diagonal='kde')
    # plt.suptitle('Scatter Matrix: Wind Conditions & Solar Irradiance', y=1.02)
    # plt.show()


