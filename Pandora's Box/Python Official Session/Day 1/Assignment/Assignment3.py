# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:13:29 2018

@author: jmat
Q. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
    If the string length is less than 2, return instead of the empty string.
"""

str1=input("Enter a string")
if len(str1)>2:
    str2=str1[:2]+str1[-2:]
    print("The required String is",str2)
else:
    print("Insufficent Length for String to perform operation on")

