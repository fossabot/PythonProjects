# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:23:16 2018

@author: jmat
Q.Get the number from the user. Generate the list of square of 'n' numbers
"""
k=-1
lst=[]

while k==-1:
    str1= input("Enter an integer") 
    if str1.isdigit()==True:
        str1=int(str1)
        k=1
        for i in range(1,str1) :
            lst.append(i**2)
            str1-=1
print(lst)