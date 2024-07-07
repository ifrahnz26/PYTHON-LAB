'''Write a python program to perform the following operations 
using user defined functions
• Display the maximum and minimum number from the array.
• Display the second largest number from the array without sorting'''

import numpy as np

def minmax(arr):
    min=max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<min:
            min=arr[i]
        elif arr[i]>max:
            max=arr[i]
    return min, max

'''Direct answer 
def minmax(arr):
    return np.min(arr), np.max(arr)'''

def secondMax(arr):
    max=smax=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            smax = max
            max = arr[i]
    return smax

arr = list(map(int,input("Enter the elements of array : ").split()))
arr = np.array(arr)
print("Minimum number is : ",minmax(arr)[0])
print("Maximum number is : ",minmax(arr)[1])
print("Second maximum number is : ",secondMax(arr))
