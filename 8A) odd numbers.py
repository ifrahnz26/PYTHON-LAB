'''Develop a python program to read 
20 random numbers. Display all the odd numbers 
from this list which are of length 2 and 4.'''

import random
list1 = [random.randint(1,10000) for _ in range(20)]
print(list1)
odd2 = [i for i in list1 if i%2!=0 and len(str(i)) == 2 or len(str(i)) == 4]
print("Odd numbers of Length 2 and 4: ",odd2)
