# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:40:16 2018

@author: jmat
"""
def divide(a,b):
    a=float(a)
    b=float(b)
    try:
        print( "The division result is  " , a/b )
    except ZeroDivisionError:
        print ("Trying to break my machine eh ? I dont know how to divide by zero")
        


a=input("Enter the first number: ")
b=input("Enter the second number: ")
divide(a,b) 
