# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:52:52 2018

@author: jmat
"""

def temp_conversion(temp):
    temp=float(temp)
    res= ( (9*temp)/5 ) +32
    return res

print("Welcome to the most cliche program written while learning Programming")
temp=input ("Enter the celsius temperature at which you wish to fry your enemies: ")
print("You will boil them to a crisp! But anyways here is the temp in Fahrenheit so that you dont mess it up ", temp_conversion(temp))