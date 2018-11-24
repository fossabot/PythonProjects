# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:52:52 2018

@author: jmat
"""

def temp_conversion(temp):
    temp=float(temp)
    if temp<-273.15:
        print ("But how is that even possible ? ")
    else:
        res= ( (9*temp)/5 ) +32
        print("You will boil them to a crisp! But anyways here is the temp in Fahrenheit so that you dont mess it up ", res)
        
    return 0
    

print("Welcome to the most cliche program written while learning Programming")
temp=input ("Enter the celsius temperature at which you wish to fry your enemies: ")
temp_conversion(temp)