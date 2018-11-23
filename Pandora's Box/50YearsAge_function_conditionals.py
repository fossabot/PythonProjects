# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:09:59 2018

@author: jmat
"""

def fifty_age(age):
    age=int(age)
    if age<0:
        print("Hey there buddy! You havent grown up a bit havent you. Grow up and try again!")
    elif age>150:
        print("How do you even have access to this program from the graveyard?")
    else:
        print ("In 50 Years you will be ",50+age," years old and grumpy")
        
    return 0
age=input("Please enter your age: ")
fifty_age(age) 