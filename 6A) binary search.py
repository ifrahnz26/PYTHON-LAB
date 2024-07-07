'''Write a python function binary Search () to read a sorted array 
and search for the key element. 
Display the appropriate messages.'''

import numpy as np
def binarySearch(arr, key, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(arr, key, low, mid - 1)
        else:
            return binarySearch(arr, key, mid + 1, high)
    return -1
arr = list(map(int,input("Enter elements of array : ").split()))
arr = np.array(arr)
key = int(input("Enter the key element : "))
result = binarySearch(arr, key, 0, len(arr) - 1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
