# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:54:23 2018

@author: jmat
Q. Prompt the user to input any numbers between 1 and 9. 
If User enters any other number, prompt the user to input again.
If the user enters valid input, display the pattern mentioned.
"""

k=-1
while k==-1:
    str1= input("Enter a value(1-9)") 
    if str1.isdigit()==True:
        str1=int(str1)
        k=1
        for i in range(0,str1) :
            for i in range(0,str1):
                print("*",end="")
                i-=1
            print("")
            str1-=1
        
    

