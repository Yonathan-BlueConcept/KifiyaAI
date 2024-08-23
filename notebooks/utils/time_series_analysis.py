import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



def plot_time_series(file_path):
   
    # Load data
    df = pd.read_csv(file_path)

    # Ensure the time column is in datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Set the time column as the index
    df.set_index('Timestamp', inplace=True)

    # Plotting
    plt.figure(figsize=(14, 10))

    # Plot GHI, DNI, DHI, and Tamb over time
    plt.subplot(2, 2, 1)
    sns.lineplot(data=df, x=df.index, y='GHI', color='orange')
    plt.title('Global Horizontal Irradiance (GHI) over Timestamp')

    plt.subplot(2, 2, 2)
    sns.lineplot(data=df, x=df.index, y='DNI', color='blue')
    plt.title('Direct Normal Irradiance (DNI) over Timestamp')

    plt.subplot(2, 2, 3)
    sns.lineplot(data=df, x=df.index, y='DHI', color='green')
    plt.title('Diffuse Horizontal Irradiance (DHI) over Timestamp')

    plt.subplot(2, 2, 4)
    sns.lineplot(data=df, x=df.index, y='Tamb', color='red')
    plt.title('Ambient Temperature (Tamb) over Timestamp')

    plt.tight_layout()
    plt.show()