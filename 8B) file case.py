'''Develop a python program to create a text file 
and ask the user to enter 5-6 lines of text. 
Count the number of upper case, lower case 
and digits in the file. Display the details of the file.'''

lines = [input(f"Enter line {i+1}: ") for i in range(5)]
f = open("file.txt", "w")
f.writelines(lines)
f.close()
f = open("file.txt", "r")
lines = f.readlines()
f.close()
upper = lower = digit = 0
for line in lines:
    for char in line:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
print(f"Upper case: {upper}")
print(f"Lower case: {lower}")
print(f"Digits: {digit}")
