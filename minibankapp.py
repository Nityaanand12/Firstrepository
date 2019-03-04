#mini bank application
class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    def printstatement(self):
        print("Account balance:",self.balance)

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=1000)
    def __str__(self):
        return "{}'s current account with balance {}".format(self.name,self.balance)
class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return "{}'s Savings Account with balance {}".format(self.name,self.balance)
c = Savings('Durga',2000)
print(c)
c.deposit(250)
c.withdraw(100)
c.printstatement()

s = Current('Durga',800)
print(s)
s.deposit(250)
s.withdraw(100)
s.printstatement()
