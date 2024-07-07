'''Write a python program to create a list of tuples having first element 
as the strings and the second element as the length of the string. 
Output the list of tuples sorted based on the length of the string.'''

def stringLenTuple(lst):
    t = [(i,len(i)) for i in lst]
    sorts_t = sorted(t,key = lambda x:x[1])
    return sorts_t
lst = list(map(str,input("Enter strings (space-separated): ").split()))
print(stringLenTuple(lst))