''' Write a python program to display 
all the prime numbers in the given range.'''

low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))
while low<high+1:
    if low>1:
        for i in range(2,low):
            if low%i==0:
                break
        else:
            print(low)
    low+=1
