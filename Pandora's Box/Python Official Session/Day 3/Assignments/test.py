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
    def __init__(self,acc_name,acc_number,acc_branch,acc_type,bal):
        #print("Initializing the object",self)
        self.acc_name=acc_name
        self.acc_number=int(acc_number)
        self.acc_branch=acc_branch
        self.acc_type=acc_type
        self.__bal= bal
    def __str__(self):
        return '{} whose msisdn is {} of type {}'.format(self.subs_name,
                                                         self.msisdn,
                                                         self.subs_type)
    def __get_balance(self):
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
        
#    def fun(self):
#        a=input("Which Operation do you want to do(d for deposit/w for withdraw): " )
#        if a == "d" or a== "D":
#            self.__deposit()
#        if a=="w" or a=="W":
#            self.__withdraw()
        

#name=input("Enter the Account Name")
#number=input("Enter the Account Number")
#branch=input("Enter the Account Branch")
#typ=input("Enter the Account Type")
#bal=input("Enter the Balance")
#obj_1=Account(name,number,branch,typ,bal)

obj_1=Account("Jeen","5432","PTA","Savings",2000)
print( obj_1.acc_name, obj_1.acc_number , obj_1.acc_branch , obj_1.acc_type,obj_1.get_balance())


obj_1.withdraw()

print( obj_1.acc_name, obj_1.acc_number , obj_1.acc_branch , obj_1.acc_type,obj_1.get_balance())
#
obj_1.deposit()
