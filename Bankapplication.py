import sys
class customer:
    '''customer class with bank operations'''
    bankname = 'State bank of india'
    address = 'Visakhapatnam'
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print('Balance afer deposit : %s'%self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds')
            sys.exit()
        self.balance -= amount
        print('Balance afer withdraw %s'%self.balance)
    #def Balance_enquiry(self):
        #print("your balance is:",self.balance)
print('Welcome to',customer.bankname,customer.address,'branch')
name = input('Enter your name: ')
print('Welcome', name)
c = customer(name)
while True:
    option = input("Please select operation you want to perform from menu\nd-deposit\nw-withdraw\nb-balance\ne-exit\n: ")
    if option.casefold() == 'd':
        amount = float(input('Enter an amount: '))
        c.deposit(amount)
    elif option.casefold() == 'w':
        amount = float(input("Enter an amount: "))
        c.withdraw(amount)
    elif option.casefold() =='b':
        print("your account balance is: ",c.balance)
    elif option.casefold() =='e':
        print("Thanks for banking at",c.bankname)
        sys.exit()
    else:
        print('please choose correct option')
