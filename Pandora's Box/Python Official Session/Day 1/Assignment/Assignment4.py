# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:21:40 2018

@author: jmat
Q.Write a Python program to get a single string from two given strings, separated by a space and also
  swap the first two characters of each string.
"""

str1=input ("Enter the first String")
str2=input("Enter the second String")
str1=str1[1]+str1[0]+str1[2:]
str2=str2[1]+str2[0]+str2[2:]
res_str=str1+" " + str2
print ("The required String is ", res_str)