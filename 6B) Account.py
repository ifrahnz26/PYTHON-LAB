'''Write a python program to simulate saving account 
processing in a bank using constructors. 
Create Deposit and Withdraw with other member function 
and Check for Validation while withdrawing the amount. 
Raise the appropriate exceptions when depositing 
and withdrawing an incorrect amount. 
Display appropriate messages.'''

class InsufficientBalanceError(Exception):
    pass
class InvalidAmountError(Exception):
    pass
class Account:
    def __init__(self,Balance = 0):
        self.Balance = Balance
    def deposit(self,amount):
        if amount<=0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.Balance+=amount
        print(f"Deposited Rs: {amount}. New Balance: Rs{self.Balance}")
    def withdraw(self,amount):
        if amount>self.Balance:
            raise InsufficientBalanceError("Balance is not enough")
        if amount<=0:
            raise InvalidAmountError("Withdraw amount must be positive")
        self.Balance-=amount
        print(f"Withdrawn amount:Rs{amount}.New Balance: Rs{self.Balance}")
acc = Account(1000)
try:
    acc.deposit(500)
    acc.withdraw(200)
    acc.deposit(-400)
except InsufficientBalanceError as ib:
    print(ib)
except InvalidAmountError as ia:
    print(ia)

