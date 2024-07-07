'''Write a python program to utilize NumPy and perform the following operations.
• Read and display a 2D Array.
• Display the array elements in the reverse order.
• Display all the elements of principal diagonal elements.
• Sort the 2D array in ascending and descending order'''
import numpy as np
rows = int(input("Enter number of rows: "))
lst  =[list(map(int,input(f"Enter elements of row {i}: ").split())) for i in range(rows)]
arr = np.array(lst)
print("Array is: ",arr)
print("Array in reverse order: \n",arr[::-1,::-1])
print("Principal diagonal elements: \n",arr.diagonal())
print("Ascending order: \n",np.sort(arr))
print("Descending order: \n",np.sort(arr)[::-1,::-1])