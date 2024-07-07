'''Write a python program to read the Iris dataset and perform the following operations using Pandas
• Display first 5 rows of the dataset.
• Display last 5 rows of the dataset.
• Display the information about the dataset.
• Display the overview of the values of each column.
• Visualize the dataset using plot ().'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")
#First 5 rows
print("First 5 rows: ")
print(df.head())
#Last 5 rows
print("\nLast 5 rows: ")
print(df.tail())
#Information about dataset
print("\nInformation about datset: ")
print(df.info())
#Overview of column values
print("\nOverview of column values: ")
print(df.describe())
#Visualize the dataset
print("Plot the dataset: ")
df.plot()
plt.show()