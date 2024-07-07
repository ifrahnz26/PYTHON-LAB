'''Write a python program to demonstrate handling of the following exceptions using try and except.
• Name Error
• Index Error
• Key Error
• Zero Division Error'''

try:
    print(abc)
except:
    print("Name Error")
try:
    lst = [1,2,3,4]
    print(lst[5])
except:
    print("Index Error")
try:
    dic = {'a':1,'b':2}
    print(dic['c'])
except:
    print("Key Error")
try:
    1/0
except:
    print("Zero Division Error")