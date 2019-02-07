# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:02:59 2019

@author: jmat
"""
##Class

#Data Member:- Instance Variables and Class varibales are called together as Data Members
class Account:
    
    def __init__(self,filepath):  ##Constructor
        self.path=filepath     ##Instance Variable--Accesible by object instances 
        with open(self.path,"r") as file:
            self.balance=int( file.read() )
        #print(self.balance)

    def withdraw(self,amount):  ##Methods
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount
    
    def commit(self):
        with open(self.path,"w") as file:
            file.write(str( self.balance) )

class Checking(Account):
    """This class generates checking account objects """
<<<<<<< HEAD
    type="Checking Account"
=======
    type="Checking Account"    ##Class Variable
>>>>>>> master
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


<<<<<<< HEAD
jack_checking=Checking("jack.txt",1)
=======
jack_checking=Checking("jack.txt",1) ##jack_checking is Object Instance and this statement is called Instantiation
>>>>>>> master
#checking.deposit(10)
print(jack_checking.balance)
jack_checking.transfer(1900)
print(jack_checking.balance)
jack_checking.commit()
<<<<<<< HEAD


=======
print(jack_checking.type) ## Accessing Attributes of Object Instance

>>>>>>> master
john_checking=Checking("john.txt",1)
#checking.deposit(10)
print(john_checking.balance)
john_checking.transfer(500000)
print(john_checking.balance)
john_checking.commit()

<<<<<<< HEAD
=======
print(john_checking.type)

>>>>>>> master
print(john_checking.__doc__)