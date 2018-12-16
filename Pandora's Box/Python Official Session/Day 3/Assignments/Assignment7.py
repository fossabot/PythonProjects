#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:15:25 2018

@author: jmat
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:13:04 2018

@author: jmat
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:21:06 2018

@author: jmat
"""

class Account(object):
    def __init__(self):
        
        try:
            self.acc_name=input("Enter the Account Name")
            self.acc_number=int (input("Enter the Account Number") ) 
            self.acc_branch=input("Enter the Account Branch")
            self.acc_type=input("Enter the Account Type")
            self.__bal= float(input("Enter the Balance"))
            print("Created the object\n",self)
        except (TypeError,AttributeError,ValueError) as er:
            print("You have entered a wrong input.Exiting...")
            print("Traceback\n",er)
    def __str__(self):
        return '{} has {} account in Branch {} with Account number {} '.format(self.acc_name,
                                                         self.acc_type,
                                                         self.acc_branch,self.acc_number)
    def get_balance(self):
        return self.__bal
    
    def __withdraw(self):
        if int(self.__bal)< 5000:
            print("Balance is less than 5000. Cannot withdraw from this account")
        else:
            amt=input("Enter Amount do you want to withdraw ?")
            print("You have successfully withdrawn" ,amt, " from your account")
            self.__bal=self.__bal-float(amt)
            print("Your main balance is now",self.__bal)
            
    def __deposit(self):
        amt=input("Enter Amount do you want to deposit ?")
        print("You have successfully deposited" ,amt, " to your account")
        self.__bal=self.__bal+float(amt)
        print("Your main balance is now",self.__bal)
        
    def fun(self):
        ##Can Implement Pin validation here
        a=input("Which Operation do you want to do(d for deposit/w for withdraw): " )
        if a == "d" or a== "D":
            self.__deposit()
        elif a=="w" or a=="W":
            self.__withdraw()
        else:
            print("You have entered wrong input")
        

obj_1=Account()

#obj_1=Account("John","5432","USA","Savings",2000)
#print( obj_1.acc_name, obj_1.acc_number , obj_1.acc_branch , obj_1.acc_type,obj_1.get_balance())


obj_1.fun()
print("\nAfter updation, the values are\n",obj_1)
#print( obj_1.acc_name, obj_1.acc_number , obj_1.acc_branch , obj_1.acc_type,obj_1.get_balance())
