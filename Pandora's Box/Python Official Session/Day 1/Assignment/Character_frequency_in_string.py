# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:44:11 2018

@author: jmat

Q. Write a Python program to count the number of characters (character frequency) in a string.

"""

str1=input("Please Enter a String")
#str1="Hello"
freq_lst=[ ]
str2=[]
for i in str1:
    if i not in str2:
        str2.append(i)
        freq_lst.append( str1.count(i) )

for i in range(0,len(str2) ) :
    print("Character:", str2[i] ,"-->Frequency:", freq_lst[i] )
