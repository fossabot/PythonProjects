# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:20:25 2018

@author: jmat
"""

def temp_conversion(temp):
    temp=float(temp)
    if temp<-273.15:
        return ("But how is that even possible ? ")
    else:
        res= ( (9*temp)/5 ) +32
        return res
    

l=[100,273,400,1000,-100]
print("\n I have a list of celsius temperature at which you can fry your enemies: Here is the list:\n", l)
print("You will boil them to a crisp! But anyways here is the temp in Fahrenheit incase you dont have a celsius thermometer ")
for i in l:
    print ( temp_conversion(i) )
    
