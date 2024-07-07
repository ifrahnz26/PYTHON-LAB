'''Write a python program to simulate saving account 
processing in a bank using constructors. 
Create Deposit and Withdraw with other member function 
and Check for Validation while withdrawing the amount. 
Raise the appropriate exceptions when depositing 
and withdrawing an incorrect amount. 
Display appropriate messages.'''

class SavingsAccount:
    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited successfully. Current balance: Rs. {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn successfully. Current balance: Rs. {self.balance}")
    def display(self):
        print(f"Name: {self.name}\nAccount Number: {self.accountNumber}\nBalance: Rs. {self.balance}")
acc = SavingsAccount("ABC", 12345, 2000)
try:
    print("ACCOUNT DETAILS: ")
    acc.display()
    acc.deposit(1000)
    acc.withdraw(500)
    acc.withdraw(3000)
except ValueError as ve:
    print(ve)

