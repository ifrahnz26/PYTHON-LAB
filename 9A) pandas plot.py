'''Develop a python program read a dataset and perform the following using Pandas
• Visualize the dataset using plot ().
• Draw the Scatter plot for the dataset on any column.
• Display the scatter plot with different colors.
• Draw the Histogram for the dataset on any column'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")
print("Plot the dataset: ")
df.plot()
plt.show()
print("\nScatter plot :")
df.plot(kind = "scatter", x = 'sepal.length', y ='petal.length', color = 'lightpink')
plt.show()
print("\nScatter plot with different colors: ")
plt.scatter(x=df['sepal.length'], y = df['petal.length'], color = 'hotpink')
plt.scatter(x=df['sepal.width'], y = df['petal.width'], color = 'lightgreen')
plt.show()
print("\nHistogram: ")
df['sepal.width'].plot(kind = "hist",color = 'lavender', edgecolor = 'purple')
plt.show()