# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:02:59 2019

@author: jmat
"""

class Account:
    
    def __init__(self,filepath):
        self.path=filepath
        with open(self.path,"r") as file:
            self.balance=int( file.read() )
        #print(self.balance)

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount
    
    def commit(self):
        with open(self.path,"w") as file:
            file.write(str( self.balance) )

class Checking(Account):
       
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee
    
    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee
    

#
#account=Account("balance.txt")
##print(account)
##print(account.balance)
#account.deposit(3000)
##print(account.balance)
#account.commit()


checking=Checking("balance.txt",1)
#checking.deposit(10)
print(checking.balance)
checking.transfer(1000)
print(checking.balance)
checking.commit()

