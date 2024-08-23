import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



def analyze_humidity_influence(file_path):


    df = pd.read_csv(file_path)
    
    # Step 1: Scatter Plots for RH vs Temperature
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='RH', y='TModA', data=df, color='blue')
    plt.title('Relative Humidity vs. Temperature (TModA)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (TModA)')

    plt.subplot(1, 2, 2)
    sns.scatterplot(x='RH', y='TModB', data=df, color='green')
    plt.title('Relative Humidity vs. Temperature (TModB)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (TModB)')
    
    plt.tight_layout()
    plt.show()

    # Step 2: Scatter Plots for RH vs Solar Radiation Components
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    sns.scatterplot(x='RH', y='GHI', data=df, color='red')
    plt.title('Relative Humidity vs. Global Horizontal Irradiance (GHI)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('GHI (W/m²)')

    plt.subplot(1, 3, 2)
    sns.scatterplot(x='RH', y='DNI', data=df, color='orange')
    plt.title('Relative Humidity vs. Direct Normal Irradiance (DNI)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('DNI (W/m²)')

    plt.subplot(1, 3, 3)
    sns.scatterplot(x='RH', y='DHI', data=df, color='purple')
    plt.title('Relative Humidity vs. Diffuse Horizontal Irradiance (DHI)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('DHI (W/m²)')

    plt.tight_layout()
    plt.show()

    # Step 3: Correlation Heatmap
    plt.figure(figsize=(8, 6))
    correlation_matrix = df[['RH', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap: RH, Temperature, and Solar Radiation')
    plt.show()

