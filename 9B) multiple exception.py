'''Develop a python program to demonstrate handling 
multiple exceptions using try, except , 
else and finally block statements..'''

def func(n):
    try:
        res = 10//n
    except TypeError:
        print("Invalid input!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Result is",res)
    finally:
        print("Finally block executed!")
func(0)
func(2)
func('a')