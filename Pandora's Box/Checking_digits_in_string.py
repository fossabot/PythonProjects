# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:39:37 2018

@author: jmat
"""
digits=0
str="This is a random string with 1234567892345678 ! "
for i  in str :
    if i.isdigit()==True:
        digits+=1
        
print(digits)
        

    
