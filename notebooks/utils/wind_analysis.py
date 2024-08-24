import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def wind_analysis_polar(filePath):
   
    df  = pd.read_csv(filePath)
    # Extract wind speed, wind gust, and wind direction data
    ws = df['WS']  # Wind Speed
    ws_gust = df['WSgust']  # Wind Speed Gust
    wd = df['WD']  # Wind Direction in degrees

    # Convert wind direction to radians
    wd_rad = np.deg2rad(wd)

    # Step 1: Polar Plot for Wind Speed and Direction
    plt.figure(figsize=(10, 8))
    ax = plt.subplot(111, polar=True)

    # Scatter plot for wind speed
    scatter = ax.scatter(wd_rad, ws, c=ws, cmap='viridis', alpha=0.75, edgecolors='w', s=50)
    plt.colorbar(scatter, ax=ax, label='Wind Speed (WS)')

    # Overlay wind gusts to show significant wind events
    scatter_gust = ax.scatter(wd_rad, ws_gust, c=ws_gust, cmap='Reds', alpha=0.5, edgecolors='w', s=50)
    plt.colorbar(scatter_gust, ax=ax, label='Wind Speed Gust (WSgust)')

    # Set plot details
    ax.set_theta_direction(-1)  # Clockwise direction
    ax.set_theta_offset(np.pi / 2.0)  # Zero degrees at the top (North)
    ax.set_title('Wind Analysis: Distribution of Wind Speed and Direction', va='bottom')
    plt.show()


