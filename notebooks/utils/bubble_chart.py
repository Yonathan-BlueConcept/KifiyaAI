import pandas as pd
import matplotlib.pyplot as plt





def plot_bubble_chart(df, x_var, y_var, size_var, color_var=None, xlabel='', ylabel='', title=''):
    
    
    plt.figure(figsize=(10, 8))

    # Normalize the bubble size for better visualization
    size = df[size_var] / df[size_var].max() * 1000

    # Plotting the bubble chart
    plt.scatter(df[x_var], df[y_var], s=size, alpha=0.5, c=df[color_var] if color_var else None, cmap='viridis')

    # Adding labels and title
    plt.xlabel(xlabel if xlabel else x_var)
    plt.ylabel(ylabel if ylabel else y_var)
    plt.title(title if title else f'{x_var} vs. {y_var} with bubble size representing {size_var}')

    # Adding color bar if a color variable is provided
    if color_var:
        plt.colorbar(label=color_var)

    plt.grid(True)
    plt.show()
