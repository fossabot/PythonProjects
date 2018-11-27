# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:59:25 2018

@author: jmat
Q.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string.
"""



#str1="He is not a poor guy"
str1="He is poor but not because of his selfless deeds "
print("The string you have entered is :  ",str1)
pos_not=str1.find("not")
pos_poor=str1.find("poor")
print("\nThe first occurence of \"not\" in the string at", pos_not+1 ,"position")

print("\n The first occurence of \"poor\" in the string at", pos_poor+1 ,"position")

if pos_poor < pos_not:
    str1=str1[:pos_poor]+"good"+str1[pos_not+3:]
print(str1)